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
deficit_pct = (needs / demand) * 100
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

### 1. Sankey Diagram — "Where Does the Water Go?"

**Framework:** Mass/flow balance analysis (Industrial Engineering — process flow)

**Purpose:** Visualize the flow of water from supply through demand sectors to identify where shortfalls occur.

**Methodology:**
1. Aggregate existing supply (`WS{year}`) by sector across all counties
2. Aggregate unmet needs (`N{year}`) by sector
3. Compute met demand per sector: `met = max(0, supply - unmet)`
4. Construct flow links:
   - **Existing Supply -> Sector**: volume = sector supply
   - **Sector -> Demand Met**: volume = met demand
   - **Sector -> Water Deficit**: volume = unmet needs

**Interpretation:** Width of each flow is proportional to volume. The red "Water Deficit" node on the right shows the total system shortfall. Sectors with thick red links are the primary drivers of the deficit.

---

### 2. Risk Matrix — "Which Counties Are in Danger?"

**Framework:** Risk assessment matrix (ISO 31000 / IE safety analysis)

**Purpose:** Categorize counties by two independent risk dimensions to identify the intersection of water stress and industrial development.

**Methodology:**
1. **Y-axis — Water Stress Level:** Classify each county using the deficit tier system above (None / Low / Moderate / Severe / Critical)
2. **X-axis — Industrial Concentration:** Bucket counties by total facility count (Data Centers + Semiconductor Fabs):
   - 0 facilities
   - 1-3 facilities
   - 4-10 facilities
   - 10+ facilities
3. Count counties in each (stress, facility) cell
4. Render as a heatmap where color intensity = county count

**Interpretation:** The top-right quadrant (Critical stress + 10+ facilities) is the "Danger Zone" — counties with both severe water shortfalls and high industrial water demand. These are the highest-priority targets for intervention.

---

### 3. Pareto Chart — "How Concentrated Is the Problem?"

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

### 4. R² Regression — "Is There a Statistical Link?"

**Framework:** Ordinary Least Squares (OLS) linear regression

**Purpose:** Quantify the statistical relationship between industrial facility presence and water deficit.

**Methodology:**
1. For each county with either facilities or deficit > 0:
   - X = total industrial facilities (DC + Fabs)
   - Y = water deficit in acre-feet
2. Compute OLS regression coefficients:
   ```
   m = (n * SUM(X*Y) - SUM(X) * SUM(Y)) / (n * SUM(X²) - SUM(X)²)
   b = (SUM(Y) - m * SUM(X)) / n
   ```
3. Compute coefficient of determination (R²):
   ```
   SS_res = SUM((y_i - (m * x_i + b))²)    // residual sum of squares
   SS_tot = SUM((y_i - mean(Y))²)           // total sum of squares
   R² = 1 - SS_res / SS_tot
   ```
4. Plot scatter with regression line overlay

**Interpretation:**
- R² close to 1.0 = strong linear relationship
- R² close to 0.0 = no linear relationship
- The regression line shows the expected deficit increase per additional facility
- Points are colored by severity tier to show stress clustering

**Limitations:** Linear regression assumes a monotonic linear relationship. With most counties having 0 facilities, the R² may be low even if there's a meaningful pattern among counties that DO have facilities. The box plot distribution chart complements this analysis.

---

### 5. Box Plot Distribution — "Are Industrial Counties Worse Off?"

**Framework:** Comparative distribution analysis (statistical hypothesis testing)

**Purpose:** Compare the distribution of water stress between counties with and without industrial facilities.

**Methodology:**
1. Split counties into two groups:
   - **Industrial:** counties where `(data_centers + semi_fabs) > 0` AND `demand > 0`
   - **Non-industrial:** counties where `facilities = 0` AND `demand > 0`
2. For each county, compute: `deficit_pct = (needs / demand) * 100`
3. Generate box-and-whisker plot for each group showing:
   - **Median** (center line)
   - **Q1, Q3** (box edges — interquartile range)
   - **Whiskers** (1.5 * IQR)
   - **Mean** (diamond marker, `boxmean: true`)
   - **All data points** (jittered for visibility)
4. Annotate with group means

**Interpretation:** If the industrial group's box is higher (larger median, higher mean), counties hosting data centers and semiconductor fabs tend to face worse water deficits relative to their demand. The sample sizes (n=) show the balance between groups.

---

### 6. Statewide Projection — "How Fast Is It Getting Worse?"

**Framework:** Time-series trend analysis

**Purpose:** Show the trajectory of supply, demand, and deficit over the 50-year planning horizon.

**Methodology:**
1. For each year in [2020, 2030, 2040, 2050, 2060, 2070]:
   ```
   total_demand[year] = SUM(D{year}) across all entities
   total_supply[year] = SUM(WS{year}) across all entities
   total_needs[year]  = SUM(N{year}) across all entities
   ```
2. Plot three lines: Demand, Supply, Unmet Need
3. Fill the area under Unmet Need to visualize the growing gap

**Interpretation:** The widening gap between demand and supply lines shows the accelerating crisis. The red-filled deficit area makes the problem's growth rate visceral.

---

## Interactive Filtering

All charts respond to two global filters:
- **Region selector:** Restricts all calculations to a single TWDB planning region (A through P)
- **Year selector:** Changes the projection year (2020, 2030, 2040, 2050, 2060, 2070)

When a region is selected, non-selected counties are grayed out on the map but remain visible for geographic context.

## Map Visualization

The choropleth map uses **log-scale normalization** for the color gradient:

```
display_value = log10(raw_value + 1)
```

This prevents a small number of high-value counties (e.g., Harris County) from making all other counties appear uniformly low. The legend ticks are converted back to raw values for readability.
