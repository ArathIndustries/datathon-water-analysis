# Methodology — Texas Water Crisis Analysis

## Data Sources

| Dataset | Source | Description |
|---------|--------|-------------|
| `demands.csv` | TWDB State Water Plan 2026 | Projected water demand by entity, sector, region, and county (2020-2070) |
| `existing.csv` | TWDB State Water Plan 2026 | Existing water supply by entity and source (2020-2070) |
| `needs.csv` | TWDB State Water Plan 2026 | Unmet water needs (demand minus supply, where positive) by entity (2020-2070) |
| `population.csv` | TWDB State Water Plan 2026 | Population projections by entity and county (2020-2070) |
| `strategies.csv` | TWDB State Water Plan 2026 | Recommended water management strategies and their projected supply gains |
| `datacenters_locations.csv` | EPA FRS (Facility Registry Service) | Data center facility locations in Texas with coordinates |
| `semi_facilites_with_location.csv` | EPA FRS | Semiconductor fabrication facility locations in Texas with coordinates |
| `tx-counties.geojson` | US Census / TWDB | Texas county boundary geometries |
| `tx-regions.geojson` | TWDB | Texas water planning region boundaries |

## Column Naming Conventions

- `D{year}` — Water demand in acre-feet (e.g., `D2050`)
- `WS{year}` — Water supply (existing sources) in acre-feet
- `N{year}` — Unmet needs (deficit) in acre-feet
- `P{year}` — Population count
- `SS{year}` — Strategy supply in acre-feet
- `WugType` — Water User Group type (MUNICIPAL, IRRIGATION, MANUFACTURING, MINING, LIVESTOCK, STEAM ELECTRIC POWER)
- `WugRegion` — TWDB planning region letter (A through P)
- `WugCounty` — County name

## Aggregation Process

All metrics are aggregated from entity-level to **county-level** before visualization:

```
county_demand[county] = SUM(D{year}) for all entities in that county
county_supply[county] = SUM(WS{year}) for all entities in that county
county_needs[county]  = SUM(N{year}) for all entities in that county
county_pop[county]    = SUM(P{year}) for all entities in that county
```

Facility counts are aggregated by matching `COUNTY_NAME` from EPA FRS data to TWDB county names (normalized to uppercase, " COUNTY" suffix stripped).

## Severity Classification

Counties are classified into deficit tiers based on the ratio of unmet needs to total demand:

```
severity_pct = (needs / demand) * 100
```

| Tier | Deficit % Range | Color Code |
|------|----------------|------------|
| Critical | >= 50% | #b71c1c (deep red) |
| Severe | 25% - 49.9% | #e65100 (orange) |
| Moderate | 10% - 24.9% | #f57f17 (amber) |
| Low | 0.01% - 9.9% | #558b2f (light green) |
| None | 0% | #2e7d32 (green) |

---

## Chart Methodologies

### 1. Risk Matrix — "Which Counties Are in Danger?"

**Framework:** Risk assessment matrix (ISO 31000 / IE safety analysis)

**Purpose:** Categorize counties by two independent risk dimensions to identify the intersection of water stress and industrial development.

**Methodology:**
1. **Y-axis — Water Stress Level:** Classify each county using the severity tier system above (None / Low / Moderate / Severe / Critical)
2. **X-axis — Industrial Concentration:** Bucket counties by total facility count (Data Centers + Semiconductor Fabs):
   - 0 facilities
   - 1-3 facilities
   - 4-10 facilities
   - 10+ facilities
3. Count counties in each (stress, facility) cell
4. Render as a heatmap where color intensity = county count

**Interpretation:** The top-right quadrant (Critical stress + 10+ facilities) is the "Danger Zone" — counties with both severe water shortfalls and high industrial water demand.

---

### 2. Pareto Chart — "How Concentrated Is the Problem?"

**Framework:** Pareto principle / 80-20 rule (IE quality management — Juran's vital few)

**Purpose:** Determine whether the water deficit is concentrated in a small number of counties, and whether industrial facilities co-locate with those counties.

**Methodology:**
1. Filter counties with `needs > 0`
2. Sort descending by deficit (acre-feet)
3. Compute cumulative percentages:
   ```
   cumulative_deficit_pct[i] = SUM(needs[0..i]) / total_deficit * 100
   cumulative_facilities_pct[i] = SUM(facilities[0..i]) / total_facilities * 100
   ```
4. Plot both curves against county rank
5. Draw horizontal reference line at 80%
6. Annotate the x-value where cumulative deficit crosses 80%

**Interpretation:** If the deficit curve rises steeply, the problem is concentrated — a small number of counties drive most of the shortfall. If the facilities curve tracks the deficit curve, industrial buildout is correlated with water stress.

---

### 3. Scatter Plot — "Water Stress vs. Industrial Presence"

**Framework:** Exploratory data analysis with severity tier overlay

**Purpose:** Visualize the relationship between industrial facility count and water stress severity for each county.

**Methodology:**
1. For each county with `demand > 0` and either facilities or deficit > 0:
   - X = total industrial facilities (Data Centers + Semiconductor Fabs)
   - Y = severity score (%) = `(needs / demand) * 100`
2. Color each point by its severity tier
3. Overlay horizontal severity tier bands (Low, Moderate, Severe, Critical) as colored background regions
4. Display county name and details on hover

**Interpretation:** Points in the upper-right indicate counties with both high industrial presence and severe water stress. The tier bands provide immediate visual context for how each county's severity compares to the classification thresholds.

---

### 4. Box Plot Distribution — "Are Industrial Counties Worse Off?"

**Framework:** Comparative distribution analysis (statistical hypothesis testing)

**Purpose:** Compare the distribution of water stress between counties with and without industrial facilities.

**Methodology:**
1. Split counties into two groups:
   - **Industrial:** counties where `(data_centers + semi_fabs) > 0` AND `demand > 0`
   - **Non-industrial:** counties where `facilities = 0` AND `demand > 0`
2. For each county, compute: `severity_pct = (needs / demand) * 100`
3. Generate box-and-whisker plot for each group showing:
   - **Median** (center line)
   - **Q1, Q3** (box edges — interquartile range)
   - **Whiskers** (1.5 * IQR)
   - **Mean** (diamond marker, `boxmean: true`)
   - **All data points** (jittered for visibility)
4. Overlay severity tier bands matching the scatter plot
5. Annotate with group means

**Interpretation:** If the industrial group's box is higher (larger median, higher mean), counties hosting data centers and semiconductor fabs tend to face worse water deficits relative to their demand. The sample sizes (n=) show the balance between groups.

---

## Interactive Filtering

All charts respond to two global filters:
- **Region selector:** Restricts all calculations to a single TWDB planning region (A through P)
- **Year selector:** Changes the projection year (2020, 2030, 2040, 2050, 2060, 2070)

When a region is selected, non-selected counties are grayed out on the map but remain visible for geographic context.

### 5. Severity Map — "Where Is the Crisis?"

**Framework:** Choropleth mapping with severity tier classification

**Purpose:** Provide an at-a-glance geographic view of water stress across all 254 Texas counties, with facility overlays to show where industrial demand concentrates.

**Methodology:**
1. Color each county polygon by the selected metric (Water Needs, Demand, Population, or Supply)
2. Apply **log-scale normalization** to the color gradient:
   ```
   display_value = log10(raw_value + 1)
   ```
   This prevents a small number of high-value counties (e.g., Harris County) from making all other counties appear uniformly low. The legend ticks are converted back to raw values for readability.
3. Overlay data center markers (blue) and semiconductor fab markers (red) at their GPS coordinates
4. Support county-level and region-level toggle — region view aggregates all county values within each TWDB planning region
5. When a region filter is active, non-selected counties are grayed out but remain visible for geographic context

**Interpretation:** Deep red counties on the "Water Needs" layer have the largest absolute water deficits. Facility markers clustered in red zones indicate industrial buildout in water-stressed areas.

---

## Data Viewer

The [data viewer page](../public/data.html) provides interactive access to all source and processed datasets. Each dataset card includes:
- **Source attribution** — TWDB or EPA FRS with direct links
- **Column definitions** — key field names and their meaning
- **Row counts** — loaded dynamically from the CSV
- **Download links** — direct CSV download for each dataset

The processed data section includes the **Master County Dataset** (`data/processed/master_county_dataset.csv`), which aggregates all TWDB entity-level data to county level, joins EPA facility counts, and computes severity tiers. This is the primary analytical dataset behind the dashboard charts.
