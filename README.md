# Texas Water Crisis Analysis Dashboard

Interactive dashboard analyzing which Texas counties can support data center and semiconductor infrastructure without triggering a water crisis. Built for **TXST Love Data Week 2026**.

**Live:** Deployed via Vercel from `public/` directory.

---

## Quick Start

Clone and open — no build step, no dependencies:

```bash
git clone https://github.com/ArathIndustries/datathon-water-analysis.git
cd datathon-water-analysis
```

**Option A** — Open directly:
```
open public/index.html    # macOS
start public/index.html   # Windows
```

**Option B** — Local server (enables data loading):
```bash
python -m http.server 8000 -d public
# then open http://localhost:8000
```

---

## Research Question

> Which Texas counties can support data center and semiconductor infrastructure over 5, 10, and 20 years without triggering a water crisis?

## Key Findings (2030-2050 projections)

- **36 of 207** deficit counties hold **80%** of total statewide deficit (Pareto pattern)
- Industrial counties average **21.7%** deficit vs **19.2%** for non-industrial
- **31** data centers across 18 counties, **138** semiconductor fabs across 20 counties
- Deficit is highly concentrated, not uniformly distributed

---

## Dashboard Features

- **Interactive choropleth map** — 254 Texas counties, color-coded by Water Needs, Demand, Population, or Supply
- **Counties / Regions toggle** — switch between county-level and TWDB planning region views
- **Data Center + Semiconductor Fab overlays** — facility markers from EPA FRS
- **Risk Matrix** — ISO 31000 framework: water stress tiers x facility concentration
- **Pareto Chart** — 80/20 rule: cumulative deficit concentration + facility co-location
- **Scatter Plot** — Severity score (%) vs industrial facility count with tier bands
- **Box Plot** — Severity distribution comparison: industrial vs non-industrial counties
- **Risk Table** — Top 25 counties ranked by unmet need with severity coloring
- **Global filters** — Region (A-P) and Year (2020-2070) update all charts simultaneously
- **Export** — CSV download and Plotly built-in PNG export on all charts
- **[Data Viewer](public/data.html)** — Browse all source and processed datasets with column definitions, source attribution, search, sort, and CSV download

---

## Project Structure

```
datathon-water-analysis/
├── README.md
├── vercel.json                              # Vercel config (serves public/)
├── .gitignore
│
├── docs/
│   ├── METHODOLOGY.md                       # Chart methodology (IE frameworks)
│   └── METADATA.json                        # Machine-readable dataset metadata
│
├── scripts/
│   ├── process_data.py                      # Data processing pipeline
│   └── generate_master_dataset.py           # Master county dataset generator
│
└── public/
    ├── index.html                           # Main dashboard (HTML + CSS + JS)
    ├── data.html                            # Dataset viewer with source docs
    └── data/
        ├── demands.csv                      # TWDB demand projections (3,341 rows)
        ├── existing.csv                     # TWDB existing supply (6,415 rows)
        ├── needs.csv                        # TWDB unmet needs (3,341 rows)
        ├── population.csv                   # TWDB population projections (3,341 rows)
        ├── strategies.csv                   # TWDB water management strategies
        ├── datacenters_locations.csv        # EPA FRS data centers (31 rows)
        ├── semi_facilites_with_location.csv # EPA FRS semiconductor fabs (138 rows)
        ├── tx-counties.geojson              # 254 Texas county boundaries
        ├── tx-regions.geojson               # 16 TWDB region boundaries
        └── processed/                       # Generated outputs from scripts/
```

---

## Data Sources

| Source | Description | Link |
|--------|-------------|------|
| TWDB State Water Plan 2026 | Demand, supply, needs, population projections (2020-2070) | [texasstatewaterplan.org](https://texasstatewaterplan.org/) |
| EPA Facility Registry Service | Data center and semiconductor fab locations | [epa.gov/frs](https://www.epa.gov/frs) |
| TWDB / US Census | County and region boundary geometries | [twdb.texas.gov](https://www.twdb.texas.gov/) |

---

## Reproducing Processed Data

The dashboard loads raw CSVs client-side and computes everything in the browser. The Python scripts are for offline analysis and reproducibility:

```bash
# Generate processed datasets (requires Python 3)
python scripts/process_data.py --year 2050
python scripts/generate_master_dataset.py
```

Output goes to `public/data/processed/`.

---

## Tech Stack

- **Frontend:** Vanilla HTML/CSS/JS (single file, no build step)
- **Charts:** [Plotly.js](https://plotly.com/javascript/) 2.35.2 (CDN)
- **CSV Parsing:** [PapaParse](https://www.papaparse.com/) 5.4.1 (CDN)
- **Map:** Plotly `choroplethmapbox` with OpenStreetMap tiles (no API key)
- **Hosting:** [Vercel](https://vercel.com/) (auto-deploy from GitHub)

---

## Methodology

See [docs/METHODOLOGY.md](docs/METHODOLOGY.md) for detailed chart methodology documentation, including:
- Aggregation process and severity classification
- IE framework justification for each chart (ISO 31000, Pareto, OLS, distribution analysis)
- Log-scale normalization for map visualization

## Dataset Metadata

See [docs/METADATA.json](docs/METADATA.json) for machine-readable field-level documentation of all datasets.

## Data Viewer

The dashboard includes an interactive [Data Viewer](public/data.html) page where you can browse all raw and processed datasets. Each dataset includes source attribution (TWDB / EPA FRS), column definitions, and download links. The processed **Master County Dataset** combines all sources into a single county-level analytical file.
