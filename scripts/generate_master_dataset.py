"""
Generate Master County Dataset
==============================
Produces a single CSV with one row per Texas county containing:
  - County name, Region code
  - Population for each decade: 2020, 2030, 2040, 2050, 2060, 2070
  - Unmet needs for each decade: 2020, 2030, 2040, 2050, 2060, 2070
  - Severity score % and tier (based on 2050 deficit/demand ratio)
  - Data center count, semiconductor fab count, total facilities

Output: public/data/processed/master_county_dataset.csv

Usage:
    py scripts/generate_master_dataset.py
"""

import csv
import os
from collections import defaultdict

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'public', 'data')
OUTPUT_DIR = os.path.join(DATA_DIR, 'processed')

YEARS = ['2020', '2030', '2040', '2050', '2060', '2070']

DEFICIT_TIERS = [
    ('Critical', 50),
    ('Severe',   25),
    ('Moderate', 10),
    ('Low',      0.01),
    ('None',     0),
]


def read_csv(filename):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def get_deficit_tier(needs, demand):
    pct = (needs / demand * 100) if demand > 0 else 0.0
    for tier_name, threshold in DEFICIT_TIERS:
        if pct >= threshold:
            return tier_name, round(pct, 2)
    return 'None', 0.0


def main():
    print("Loading raw data...")
    demands   = read_csv('demands.csv')
    needs     = read_csv('needs.csv')
    population = read_csv('population.csv')
    datacenters = read_csv('datacenters_locations.csv')
    semifabs  = read_csv('semi_facilites_with_location.csv')

    # --- Aggregate needs for ALL years by county ---
    # needs_by_county[county][year] = total acre-feet
    needs_by_county = defaultdict(lambda: defaultdict(float))
    region_by_county = {}

    for row in needs:
        county = row.get('WugCounty', '').upper()
        if not county:
            continue
        region_by_county[county] = row.get('WugRegion', '')
        for yr in YEARS:
            col = f'N{yr}'
            try:
                needs_by_county[county][yr] += float(row.get(col, 0) or 0)
            except (ValueError, TypeError):
                pass

    # --- Aggregate demand for 2050 (used for severity calculation) ---
    demand_by_county = defaultdict(float)
    for row in demands:
        county = row.get('WugCounty', '').upper()
        if not county:
            continue
        if county not in region_by_county:
            region_by_county[county] = row.get('WugRegion', '')
        try:
            demand_by_county[county] += float(row.get('D2050', 0) or 0)
        except (ValueError, TypeError):
            pass

    # --- Aggregate population for ALL years by county ---
    pop_by_county = defaultdict(lambda: defaultdict(float))
    for row in population:
        county = row.get('WugCounty', '').upper()
        if not county:
            continue
        if county not in region_by_county:
            region_by_county[county] = row.get('WugRegion', '')
        for yr in YEARS:
            col = f'P{yr}'
            try:
                pop_by_county[county][yr] += float(row.get(col, 0) or 0)
            except (ValueError, TypeError):
                pass

    # --- Count facilities ---
    dc_by_county = defaultdict(int)
    for dc in datacenters:
        county = dc.get('COUNTY_NAME', '').upper().replace(' COUNTY', '').strip()
        if county:
            dc_by_county[county] += 1

    fab_by_county = defaultdict(int)
    for fab in semifabs:
        county = fab.get('COUNTY_NAME', '').upper().replace(' COUNTY', '').strip()
        if county:
            fab_by_county[county] += 1

    # --- Build union of all counties ---
    all_counties = set()
    all_counties.update(needs_by_county.keys())
    all_counties.update(demand_by_county.keys())
    all_counties.update(pop_by_county.keys())
    all_counties.update(dc_by_county.keys())
    all_counties.update(fab_by_county.keys())

    # --- Build output rows ---
    rows = []
    for county in sorted(all_counties):
        demand = demand_by_county.get(county, 0)
        needs_2050 = needs_by_county[county].get('2050', 0)
        tier, pct = get_deficit_tier(needs_2050, demand)
        dc = dc_by_county.get(county, 0)
        fab = fab_by_county.get(county, 0)

        row = {
            'county': county,
            'region': region_by_county.get(county, ''),
        }
        for yr in YEARS:
            row[f'population_{yr}'] = round(pop_by_county[county].get(yr, 0))
        for yr in YEARS:
            row[f'unmet_needs_{yr}_acft'] = round(needs_by_county[county].get(yr, 0))
        row['severity_pct'] = pct
        row['severity_tier'] = tier
        row['data_centers'] = dc
        row['semi_fabs'] = fab
        row['total_facilities'] = dc + fab

        rows.append(row)

    # --- Write output ---
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fieldnames = (
        ['county', 'region']
        + [f'population_{yr}' for yr in YEARS]
        + [f'unmet_needs_{yr}_acft' for yr in YEARS]
        + ['severity_pct', 'severity_tier',
           'data_centers', 'semi_fabs', 'total_facilities']
    )
    outpath = os.path.join(OUTPUT_DIR, 'master_county_dataset.csv')
    with open(outpath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows -> {outpath}")
    print(f"Columns: {', '.join(fieldnames)}")


if __name__ == '__main__':
    main()
