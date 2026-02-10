# Project Status Report
## datathon-water-analysis

**Date**: February 9, 2026
**Status**: Dashboard fully functional with interactive dual-view map
**Latest Commit**: `610a78b` on `main`

---

## What's Live

**Repository**: https://github.com/ArathIndustries/datathon-water-analysis
**Vercel**: Auto-deploys from `main` branch

### Dashboard Layout (top to bottom)
1. **Slim header** — Title + subtitle
2. **3 Insight cards** — Statewide Deficit, Counties with Unmet Needs, People at Risk
3. **Controls bar** — Region dropdown, Year dropdown (2020-2070), Color metric dropdown, Export CSV
4. **Interactive map** — Full-width, 550px desktop / 350px mobile
5. **Sector breakdown bar** — Horizontal stacked bar showing demand % by sector
6. **Two charts** — Water Balance by Region (grouped bars), Statewide Projection (line chart 2020-2070)
7. **Risk table** — Top 25 counties ranked by unmet need with deficit % severity coloring
8. **Footer** — Data attribution + GitHub link

### Map Features
- **Counties/Regions toggle** — Pill buttons to switch views
- **Counties view**: Per-county choropleth colored by selected metric (log-normalized), dark county borders
- **Regions view**: Same metric aggregated by region, same color scale, with:
  - Thick dissolved region boundary lines (2.5px dark overlay from `tx-regions.geojson`)
  - Near-invisible county borders within regions
  - Region letter labels at centroids
- **Gray-out**: Selecting a region grays out the rest of the state at ~75% (subtle data variation preserved in gray)
- **No zoom on region select** — Map stays at full Texas view, gray-out provides visual focus
- **4 color metrics**: Water Needs (YlOrRd), Demand (Blues), Population (Purples), Supply (Greens)
- **Hover popups**: County name, region, population, demand, supply, needs
- **Custom HTML legend**: Gradient bar with tick labels (replaces Plotly's built-in colorbar)

### Auto-Update Behavior
- All dropdowns trigger `updateDashboard()` on change (no button needed)
- Map metric dropdown independently triggers `updateCountyMap()`
- Counties/Regions toggle independently triggers `updateCountyMap()`
- Insight cards, charts, risk table, and sector bar all scope to selected region

---

## Key Files

| File | Purpose | Size |
|------|---------|------|
| `public/index.html` | Entire dashboard (HTML + CSS + JS) | ~750 lines |
| `index.html` | Synced copy of above (Vercel serves from root) | same |
| `public/data/tx-counties.geojson` | 254 Texas county boundaries (FIPS filtered) | 166 KB |
| `public/data/tx-regions.geojson` | 16 dissolved TWDB region boundaries | 29 KB |
| `public/data/demands.csv` | TWDB demand projections 2020-2070 | 227 KB |
| `public/data/existing.csv` | TWDB existing supply 2020-2070 | 650 KB |
| `public/data/needs.csv` | TWDB unmet needs 2020-2070 | 197 KB |
| `public/data/population.csv` | TWDB population projections 2020-2070 | 224 KB |
| `public/data/strategies.csv` | TWDB water strategies | 1.3 MB |

---

## Tech Stack

- **Frontend**: Vanilla HTML/CSS/JS (single file, no build step)
- **Charts**: Plotly.js 2.35.2 (CDN)
- **CSV Parsing**: PapaParse 5.4.1 (CDN)
- **Map**: Plotly `choroplethmapbox` with OpenStreetMap tiles (no API key)
- **Region boundaries**: Dissolved with shapely, served as static GeoJSON
- **Hosting**: Vercel (auto-deploy from GitHub)
- **Version Control**: GitHub (`ArathIndustries/datathon-water-analysis`)

---

## Recent Session Work (Feb 8-9, 2026)

1. Added Counties/Regions map toggle
2. Replaced sector dropdown with visual stacked breakdown bar
3. Implemented gentle 25% zoom on region select, then removed it
4. Redesigned Regions view from categorical colors to data-driven (responsive to metric/year)
5. Added gray-out effect for non-selected regions (~75% grayscale with data variation)
6. Created dissolved `tx-regions.geojson` and overlaid thick region boundary lines in Regions mode
7. Map always shows full Texas view — gray-out provides focus instead of zoom

### Previous Session Work
- Built interactive county choropleth map from scratch
- Log-normalized color scales, custom HTML legend
- Mobile responsive fixes (dynamic height, overflow fix)
- Replaced generic charts with meaningful ones (regional balance, projection, risk table)
- Auto-updating dropdowns, insight cards, readable sector labels
- Slim header redesign, removed update button

---

## No Known Blockers

Dashboard is fully functional locally and on Vercel. All features working.

---

## Possible Next Steps (discussed but not started)
- Timescale projections on the map (user mentioned wanting to discuss later)
- Any further polish or new data views

---

**Last Updated**: February 9, 2026
**Project Path**: `C:\Users\Arath\Automation_Station\Projects\Datathon\web\`
