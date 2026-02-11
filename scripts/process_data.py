"""
Texas Water Crisis Analysis — Data Processing Pipeline
=======================================================
TXST Datathon 2026 — Love Data Week

This script demonstrates the data manipulation and transformation process
behind the interactive dashboard. It reads the raw TWDB and EPA datasets,
aggregates them to county level, computes derived metrics, and exports the
manipulated datasets as reproducible CSV outputs.

The datathon competition emphasizes the exploration and manipulation of data.
This pipeline makes the transformations explicit and reproducible — the
dashboard (index.html) performs the same computations client-side in JavaScript,
but this script lets reviewers inspect the intermediate results as flat files.

Note: Some outputs (sankey_flows.csv, regression_data.csv) correspond to chart
types that were explored during development but later removed from the final
dashboard. We kept these analyses in the pipeline because they represent
additional data manipulation work, even though the final dashboard chose not
to visualize them — they were re-visualizing patterns already captured by the
Risk Matrix, Pareto, and Scatter charts.

Usage:
    python scripts/process_data.py [--year 2050] [--region ""]

Output (written to public/data/processed/):
    - county_water_summary.csv    : Per-county aggregated water + facility data
    - sankey_flows.csv            : Sector-level flow data (explored, not in final dashboard)
    - risk_matrix.csv             : County counts by (stress tier, facility bin)
    - pareto_ranked.csv           : Counties ranked by deficit with cumulative %
    - regression_data.csv         : Facility count vs deficit for R² analysis (explored, not in final dashboard)
    - regression_stats.txt        : OLS regression coefficients and R² (explored, not in final dashboard)
    - distribution_comparison.csv : Deficit % for industrial vs non-industrial counties

Data Sources:
    - TWDB State Water Plan 2026: demands.csv, existing.csv, needs.csv, population.csv
    - EPA FRS: datacenters_locations.csv, semi_facilites_with_location.csv
"""

import csv
import os
import math
import argparse
from collections import defaultdict


# ============================================================================
# CONFIGURATION
# ============================================================================

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'public', 'data')
OUTPUT_DIR = os.path.join(DATA_DIR, 'processed')

# Deficit severity tiers — thresholds as percent of demand
# These match the classification used in the dashboard's getDeficitTier()
DEFICIT_TIERS = [
    ('Critical', 50),    # >= 50% of demand is unmet
    ('Severe',   25),    # 25-49.9%
    ('Moderate', 10),    # 10-24.9%
    ('Low',      0.01),  # 0.01-9.9%
    ('None',     0),     # 0%
]

# Facility count bins for the risk matrix X-axis
FACILITY_BINS = ['0', '1-3', '4-10', '10+']


# ============================================================================
# FILE I/O HELPERS
# ============================================================================

def read_csv(filename):
    """Read a CSV file and return a list of dicts (one per row)."""
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def write_csv(filename, rows, fieldnames):
    """Write a list of dicts to a CSV file in the processed output directory."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  Wrote {len(rows)} rows -> {filepath}")


# ============================================================================
# STEP 1: LOAD RAW DATA
# ============================================================================

def load_all_data():
    """Load all raw CSV files into memory."""
    print("Loading raw data files...")
    data = {
        'demands':     read_csv('demands.csv'),
        'existing':    read_csv('existing.csv'),
        'needs':       read_csv('needs.csv'),
        'population':  read_csv('population.csv'),
        'datacenters': read_csv('datacenters_locations.csv'),
        'semifabs':    read_csv('semi_facilites_with_location.csv'),
    }
    for key, rows in data.items():
        print(f"  {key}: {len(rows)} rows")
    return data


# ============================================================================
# STEP 2: COUNT INDUSTRIAL FACILITIES PER COUNTY
# ============================================================================

def count_facilities_by_county(data):
    """
    Count data centers and semiconductor fabs per county.

    The EPA FRS data stores county as "HARRIS" or "Harris County".
    We normalize to uppercase and strip " COUNTY" suffix to match
    the TWDB data format (e.g., "HARRIS").
    """
    print("\nCounting facilities per county...")
    dc_by_county = defaultdict(int)
    fab_by_county = defaultdict(int)

    for dc in data['datacenters']:
        county = dc.get('COUNTY_NAME', '').upper().replace(' COUNTY', '').strip()
        if county:
            dc_by_county[county] += 1

    for fab in data['semifabs']:
        county = fab.get('COUNTY_NAME', '').upper().replace(' COUNTY', '').strip()
        if county:
            fab_by_county[county] += 1

    print(f"  Data centers across {len(dc_by_county)} counties")
    print(f"  Semiconductor fabs across {len(fab_by_county)} counties")
    return dict(dc_by_county), dict(fab_by_county)


# ============================================================================
# STEP 3: AGGREGATE WATER DATA BY COUNTY
# ============================================================================

def aggregate_by_county(rows, prefix, year, region_filter=''):
    """
    Aggregate a TWDB dataset to county level for a given year.

    Parameters:
        rows:           List of dicts from CSV
        prefix:         Column prefix ('D' for demand, 'WS' for supply, etc.)
        year:           Year string (e.g., '2050')
        region_filter:  Optional TWDB region letter to filter by

    Returns:
        Dict mapping uppercase county name -> { total: float, region: str }

    The column name is constructed as prefix + year (e.g., 'D2050', 'WS2050').
    Multiple entities in the same county are summed together.
    """
    col = f"{prefix}{year}"
    by_county = {}

    for row in rows:
        if region_filter and row.get('WugRegion', '') != region_filter:
            continue
        county = row.get('WugCounty', '').upper()
        if not county:
            continue
        if county not in by_county:
            by_county[county] = {'total': 0.0, 'region': row.get('WugRegion', '')}
        try:
            by_county[county]['total'] += float(row.get(col, 0) or 0)
        except (ValueError, TypeError):
            pass

    return by_county


# ============================================================================
# STEP 4: CLASSIFY DEFICIT SEVERITY
# ============================================================================

def get_deficit_tier(needs, demand):
    """
    Classify a county's water stress level.

    deficit_pct = (needs / demand) * 100

    Returns (tier_name, deficit_pct).
    Tiers are checked in order from most severe to least.
    """
    pct = (needs / demand * 100) if demand > 0 else 0.0
    for tier_name, threshold in DEFICIT_TIERS:
        if pct >= threshold:
            return tier_name, pct
    return 'None', 0.0


# ============================================================================
# STEP 5: BUILD COUNTY WATER SUMMARY
# ============================================================================

def build_county_summary(data, year, region):
    """
    Build the master county-level dataset that feeds all charts.

    For each county, we aggregate:
    - demand (D{year})
    - supply (WS{year})
    - needs/deficit (N{year})
    - population (P{year})
    - data center count
    - semiconductor fab count
    - deficit severity tier
    - deficit as % of demand
    """
    print(f"\nBuilding county summary for year={year}, region={region or 'ALL'}...")

    demand_agg = aggregate_by_county(data['demands'], 'D', year, region)
    supply_agg = aggregate_by_county(data['existing'], 'WS', year, region)
    needs_agg = aggregate_by_county(data['needs'], 'N', year, region)
    pop_agg = aggregate_by_county(data['population'], 'P', year, region)
    dc_counts, fab_counts = count_facilities_by_county(data)

    # Union of all counties from every dataset
    all_counties = set()
    for agg in [demand_agg, supply_agg, needs_agg, pop_agg]:
        all_counties.update(agg.keys())
    all_counties.update(dc_counts.keys())
    all_counties.update(fab_counts.keys())

    summary = []
    for county in sorted(all_counties):
        demand = demand_agg.get(county, {}).get('total', 0)
        supply = supply_agg.get(county, {}).get('total', 0)
        needs = needs_agg.get(county, {}).get('total', 0)
        pop = pop_agg.get(county, {}).get('total', 0)
        region_code = (demand_agg.get(county, {}).get('region', '') or
                       needs_agg.get(county, {}).get('region', ''))
        dc = dc_counts.get(county, 0)
        fab = fab_counts.get(county, 0)
        tier_name, deficit_pct = get_deficit_tier(needs, demand)

        summary.append({
            'county': county,
            'region': region_code,
            'population': round(pop),
            'demand_acft': round(demand),
            'supply_acft': round(supply),
            'deficit_acft': round(needs),
            'deficit_pct': round(deficit_pct, 2),
            'severity_tier': tier_name,
            'data_centers': dc,
            'semi_fabs': fab,
            'total_facilities': dc + fab,
        })

    print(f"  {len(summary)} counties in summary")
    return summary


# ============================================================================
# STEP 6: GENERATE SANKEY FLOW DATA
# Note: The Sankey diagram was explored during development but removed from the
# final dashboard. It visualized sector-level supply/demand flows, but we found
# this duplicated insights already shown by the Risk Matrix and Pareto charts.
# The data manipulation is preserved here as part of the datathon deliverable.
# ============================================================================

def build_sankey_flows(data, year, region):
    """
    Build sector-level flow data for a Sankey diagram.

    The Sankey shows:  Existing Supply -> [Sectors] -> Demand Met / Water Deficit

    For each sector:
        supply  = SUM(WS{year}) for that sector
        unmet   = SUM(N{year}) for that sector
        met     = max(0, supply - unmet)

    Links:
        Supply -> Sector  (volume = supply)
        Sector -> Met     (volume = met)
        Sector -> Deficit (volume = unmet)

    Note: This chart was explored but not included in the final dashboard.
    The output is retained to demonstrate the data manipulation process.
    """
    print(f"\nBuilding Sankey flows for year={year}...")

    sector_supply = defaultdict(float)
    sector_demand = defaultdict(float)
    sector_needs = defaultdict(float)

    for row in data['existing']:
        if region and row.get('WugRegion', '') != region:
            continue
        sector = row.get('WugType', 'OTHER')
        try:
            sector_supply[sector] += float(row.get(f'WS{year}', 0) or 0)
        except (ValueError, TypeError):
            pass

    for row in data['demands']:
        if region and row.get('WugRegion', '') != region:
            continue
        sector = row.get('WugType', 'OTHER')
        try:
            sector_demand[sector] += float(row.get(f'D{year}', 0) or 0)
        except (ValueError, TypeError):
            pass

    for row in data['needs']:
        if region and row.get('WugRegion', '') != region:
            continue
        sector = row.get('WugType', 'OTHER')
        try:
            sector_needs[sector] += float(row.get(f'N{year}', 0) or 0)
        except (ValueError, TypeError):
            pass

    flows = []
    for sector in sorted(sector_demand.keys(), key=lambda s: -sector_demand[s]):
        supply = sector_supply.get(sector, 0)
        unmet = sector_needs.get(sector, 0)
        met = max(0, supply - unmet)
        demand = sector_demand.get(sector, 0)

        flows.append({
            'sector': sector,
            'demand_acft': round(demand),
            'supply_acft': round(supply),
            'met_acft': round(met),
            'deficit_acft': round(unmet),
            'deficit_pct': round(unmet / demand * 100, 2) if demand > 0 else 0,
        })

    print(f"  {len(flows)} sectors")
    return flows


# ============================================================================
# STEP 7: GENERATE RISK MATRIX
# ============================================================================

def build_risk_matrix(county_summary):
    """
    Build the risk matrix: Water Stress (rows) x Industrial Concentration (cols).

    Facility bins: 0, 1-3, 4-10, 10+
    Stress tiers:  None, Low, Moderate, Severe, Critical

    Each cell contains the count of counties in that category.
    """
    print("\nBuilding risk matrix...")

    def facility_bin(n):
        if n == 0: return '0'
        if n <= 3: return '1-3'
        if n <= 10: return '4-10'
        return '10+'

    tier_names = ['None', 'Low', 'Moderate', 'Severe', 'Critical']
    matrix = []

    for tier in tier_names:
        for fbin in FACILITY_BINS:
            counties = [c['county'] for c in county_summary
                        if c['severity_tier'] == tier
                        and facility_bin(c['total_facilities']) == fbin]
            matrix.append({
                'stress_tier': tier,
                'facility_bin': fbin,
                'county_count': len(counties),
                'example_counties': '; '.join(counties[:5]),
            })

    print(f"  {len(matrix)} cells (5 tiers x 4 bins)")
    return matrix


# ============================================================================
# STEP 8: GENERATE PARETO RANKING
# ============================================================================

def build_pareto_ranking(county_summary):
    """
    Rank counties by deficit (descending) and compute cumulative percentages.

    The Pareto principle asks: do a small number of counties account for
    the majority of the deficit? We also track cumulative facility concentration.

    Output includes the rank, county name, deficit, facilities,
    cumulative deficit %, and cumulative facilities %.
    """
    print("\nBuilding Pareto ranking...")

    ranked = sorted(
        [c for c in county_summary if c['deficit_acft'] > 0],
        key=lambda c: -c['deficit_acft']
    )

    total_deficit = sum(c['deficit_acft'] for c in ranked)
    total_facilities = sum(c['total_facilities'] for c in ranked)

    cum_deficit = 0
    cum_facilities = 0
    pareto = []

    for i, c in enumerate(ranked):
        cum_deficit += c['deficit_acft']
        cum_facilities += c['total_facilities']
        pareto.append({
            'rank': i + 1,
            'county': c['county'],
            'region': c['region'],
            'deficit_acft': c['deficit_acft'],
            'deficit_pct': c['deficit_pct'],
            'severity_tier': c['severity_tier'],
            'total_facilities': c['total_facilities'],
            'data_centers': c['data_centers'],
            'semi_fabs': c['semi_fabs'],
            'cumulative_deficit_pct': round(cum_deficit / total_deficit * 100, 2) if total_deficit > 0 else 0,
            'cumulative_facilities_pct': round(cum_facilities / total_facilities * 100, 2) if total_facilities > 0 else 0,
        })

    # Report the 80% threshold
    idx_80 = next((i for i, p in enumerate(pareto) if p['cumulative_deficit_pct'] >= 80), None)
    if idx_80 is not None:
        print(f"  80% of deficit concentrated in {idx_80 + 1} of {len(pareto)} counties")
    print(f"  {len(pareto)} counties with deficit > 0")
    return pareto


# ============================================================================
# STEP 9: GENERATE REGRESSION DATA
# Note: The R² regression chart was explored during development but removed
# from the final dashboard. The scatter plot with severity tier bands provides
# a more intuitive view of the same facility-vs-deficit relationship. The OLS
# computation is preserved here to demonstrate statistical data manipulation.
# ============================================================================

def build_regression_data(county_summary):
    """
    Prepare data for R² regression analysis: X=facilities, Y=deficit.

    Also computes the OLS regression coefficients and R² in-script
    so the output CSV includes the predicted value and residual for
    each county.

    OLS formulas:
        m = (n * SUM(xy) - SUM(x) * SUM(y)) / (n * SUM(x²) - SUM(x)²)
        b = (SUM(y) - m * SUM(x)) / n
        R² = 1 - SS_res / SS_tot

    Note: This chart was explored but not included in the final dashboard.
    The scatter plot with severity tiers conveys this relationship more clearly.
    """
    print("\nBuilding regression data...")

    # Filter: counties with either facilities or deficit
    reg = [c for c in county_summary if c['deficit_acft'] > 0 or c['total_facilities'] > 0]

    if len(reg) < 3:
        print("  Insufficient data for regression")
        return []

    x = [c['total_facilities'] for c in reg]
    y = [c['deficit_acft'] for c in reg]
    n = len(x)

    # ---- OLS Linear Regression ----
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi ** 2 for xi in x)

    denom = n * sum_x2 - sum_x ** 2
    m = (n * sum_xy - sum_x * sum_y) / denom if denom != 0 else 0
    b = (sum_y - m * sum_x) / n

    # ---- R² Calculation ----
    mean_y = sum_y / n
    ss_res = sum((yi - (m * xi + b)) ** 2 for xi, yi in zip(x, y))
    ss_tot = sum((yi - mean_y) ** 2 for yi in y)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

    print(f"  R² = {r2:.4f}")
    print(f"  Regression: deficit = {m:.1f} * facilities + {b:.1f}")
    print(f"  n = {n}")

    rows = []
    for c in reg:
        predicted = m * c['total_facilities'] + b
        rows.append({
            'county': c['county'],
            'region': c['region'],
            'total_facilities': c['total_facilities'],
            'data_centers': c['data_centers'],
            'semi_fabs': c['semi_fabs'],
            'deficit_acft': c['deficit_acft'],
            'predicted_deficit': round(predicted, 1),
            'residual': round(c['deficit_acft'] - predicted, 1),
            'severity_tier': c['severity_tier'],
        })

    # Append regression metadata as a comment row
    print(f"  {len(rows)} data points")
    return rows, {'slope': m, 'intercept': b, 'r_squared': r2, 'n': n}


# ============================================================================
# STEP 10: GENERATE DISTRIBUTION COMPARISON
# ============================================================================

def build_distribution_comparison(county_summary):
    """
    Compare deficit-as-%-of-demand between industrial and non-industrial counties.

    Groups:
        - Industrial:     counties with total_facilities > 0 AND demand > 0
        - Non-industrial: counties with total_facilities == 0 AND demand > 0

    This is the data behind the box plot chart.
    """
    print("\nBuilding distribution comparison...")

    rows = []
    for c in county_summary:
        if c['demand_acft'] <= 0:
            continue
        group = 'Industrial' if c['total_facilities'] > 0 else 'Non-Industrial'
        rows.append({
            'county': c['county'],
            'region': c['region'],
            'group': group,
            'total_facilities': c['total_facilities'],
            'demand_acft': c['demand_acft'],
            'deficit_acft': c['deficit_acft'],
            'deficit_pct_of_demand': c['deficit_pct'],
        })

    industrial = [r for r in rows if r['group'] == 'Industrial']
    non_industrial = [r for r in rows if r['group'] == 'Non-Industrial']

    avg_ind = (sum(r['deficit_pct_of_demand'] for r in industrial) / len(industrial)
               if industrial else 0)
    avg_non = (sum(r['deficit_pct_of_demand'] for r in non_industrial) / len(non_industrial)
               if non_industrial else 0)

    print(f"  Industrial counties:     n={len(industrial)}, mean deficit={avg_ind:.1f}%")
    print(f"  Non-industrial counties: n={len(non_industrial)}, mean deficit={avg_non:.1f}%")
    return rows


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description='Process Texas water crisis data')
    parser.add_argument('--year', default='2050', help='Projection year (default: 2050)')
    parser.add_argument('--region', default='', help='TWDB region letter filter (default: all)')
    args = parser.parse_args()

    year = args.year
    region = args.region

    print("=" * 60)
    print("Texas Water Crisis — Data Processing Pipeline")
    print(f"Year: {year}  |  Region: {region or 'ALL'}")
    print("=" * 60)

    # Load raw data
    data = load_all_data()

    # Build master county summary
    summary = build_county_summary(data, year, region)
    write_csv('county_water_summary.csv', summary, [
        'county', 'region', 'population', 'demand_acft', 'supply_acft',
        'deficit_acft', 'deficit_pct', 'severity_tier',
        'data_centers', 'semi_fabs', 'total_facilities',
    ])

    # Sankey flows
    flows = build_sankey_flows(data, year, region)
    write_csv('sankey_flows.csv', flows, [
        'sector', 'demand_acft', 'supply_acft', 'met_acft', 'deficit_acft', 'deficit_pct',
    ])

    # Risk matrix
    matrix = build_risk_matrix(summary)
    write_csv('risk_matrix.csv', matrix, [
        'stress_tier', 'facility_bin', 'county_count', 'example_counties',
    ])

    # Pareto ranking
    pareto = build_pareto_ranking(summary)
    write_csv('pareto_ranked.csv', pareto, [
        'rank', 'county', 'region', 'deficit_acft', 'deficit_pct', 'severity_tier',
        'total_facilities', 'data_centers', 'semi_fabs',
        'cumulative_deficit_pct', 'cumulative_facilities_pct',
    ])

    # Regression data
    reg_result = build_regression_data(summary)
    if reg_result:
        reg_rows, reg_stats = reg_result
        write_csv('regression_data.csv', reg_rows, [
            'county', 'region', 'total_facilities', 'data_centers', 'semi_fabs',
            'deficit_acft', 'predicted_deficit', 'residual', 'severity_tier',
        ])
        # Write regression stats summary
        stats_path = os.path.join(OUTPUT_DIR, 'regression_stats.txt')
        with open(stats_path, 'w') as f:
            f.write(f"OLS Linear Regression: deficit = {reg_stats['slope']:.2f} * facilities + {reg_stats['intercept']:.2f}\n")
            f.write(f"R² = {reg_stats['r_squared']:.4f}\n")
            f.write(f"n = {reg_stats['n']}\n")
        print(f"  Wrote regression stats -> {stats_path}")

    # Distribution comparison
    dist = build_distribution_comparison(summary)
    write_csv('distribution_comparison.csv', dist, [
        'county', 'region', 'group', 'total_facilities',
        'demand_acft', 'deficit_acft', 'deficit_pct_of_demand',
    ])

    print("\n" + "=" * 60)
    print("Processing complete. Output in: public/data/processed/")
    print("=" * 60)


if __name__ == '__main__':
    main()
