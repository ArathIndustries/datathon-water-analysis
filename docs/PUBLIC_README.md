# Texas Water Crisis Analysis - Frontend User Guide

Complete documentation for users and developers working with the interactive HTML dashboard for analyzing Texas water resource data.

---

## Table of Contents

1. [Frontend Project Overview](#frontend-project-overview)
2. [Project Structure](#project-structure)
3. [Key JavaScript Libraries](#key-javascript-libraries)
4. [HTML Organization](#html-organization)
5. [CSS Styling Guide](#css-styling-guide)
6. [Data Loading Mechanism](#data-loading-mechanism)
7. [5 Chart Types with Examples](#5-chart-types-with-examples)
8. [Export Functionality](#export-functionality)
9. [Mobile Responsiveness](#mobile-responsiveness)
10. [Browser Support Matrix](#browser-support-matrix)
11. [Performance Considerations](#performance-considerations)
12. [Common Tasks](#common-tasks)
13. [Troubleshooting](#troubleshooting)

---

## Frontend Project Overview

The Texas Water Crisis Analysis dashboard is an interactive, client-side web application for visualizing water demand projections across Texas regions. All processing happens in your browser - no server backend required.

### Key Features

**Interactive Visualizations**
- Bar charts showing top water demand entities
- Line charts displaying 50-year trend projections
- Responsive charts that adapt to window size
- Hover tooltips with detailed information
- Download individual charts as PNG images

**Dynamic Filtering**
- Filter by region (all 16 Texas water planning regions)
- Filter by water user group type (municipal, agricultural, industrial)
- Select specific year for analysis (2020-2070)
- Real-time chart updates after filtering

**Data Export**
- Download filtered data as CSV file
- Export includes entity names, regions, and demand values
- Works entirely in browser (no server upload)

**Statistics Dashboard**
- Total records in dataset
- Number of regions represented
- Number of WUG types
- Data coverage period (2020-2070)

**Responsive Design**
- Works on desktop, tablet, and mobile
- Touch-friendly on mobile devices
- Automatic layout adjustment for screen size
- Horizontal scroll on small screens

### Technology Stack

| Layer | Technologies |
|-------|--------------|
| **Visualization** | Plotly.js 2.26.0+ |
| **CSV Parsing** | PapaParse 5.4.1+ |
| **Markup** | HTML5 semantic elements |
| **Styling** | CSS3 Grid, Flexbox, Media Queries |
| **Programming** | Vanilla JavaScript (ES6+) |
| **No Backend Required** | All processing in browser |

### Data Source

**Texas Department of Biological Resources (TWDB)**
- State Water Plan 2026
- Water demand projections by entity and region
- Time period: 2020-2070 (50-year projection)
- Coverage: All 16 Texas water planning regions
- Dataset contains: demands.csv, existing.csv, needs.csv, population.csv, strategies.csv

---

## Project Structure

### Single-File Architecture

The dashboard is contained in a single `index.html` file for simplicity and portability.

```
index.html (~23 KB)
├── <head> section
│   ├── Meta tags (charset, viewport, title)
│   ├── External library CDN links
│   │   ├── Plotly.js for charting
│   │   └── PapaParse for CSV parsing
│   └── <style> section with all CSS
│
├── <body> section
│   ├── <header> - Title and description
│   ├── <div class="controls"> - Filters and buttons
│   ├── <div class="stats-grid"> - Summary statistics
│   ├── <div class="charts-grid"> - Multiple charts
│   ├── <div class="data-table"> - HTML table view
│   └── <footer> - Attribution and links
│
└── <script> section with all JavaScript
    ├── Data loading functions
    ├── Filtering logic
    ├── Chart rendering functions
    ├── Export functionality
    └── Event handlers
```

### Why Single File?

**Advantages**:
- ✓ Deploy as single file (no setup needed)
- ✓ No build step required
- ✓ Easy to understand (see all code in one place)
- ✓ Works offline (except CDN dependencies)
- ✓ Portable (copy one file to share)

**Disadvantages**:
- ✗ File size is larger (~23 KB)
- ✗ Harder to maintain at scale
- ✗ No code splitting

---

## HTML Organization

### Semantic Structure

The HTML follows W3C semantic guidelines for accessibility and SEO.

### Header Section (Lines 243-250)

```html
<header>
    <h1>💧 Texas Water Crisis Analysis</h1>
    <p class="subtitle">Interactive Dashboard - TWDB Data Analysis</p>
    <div class="intro">
        <p><strong>Project:</strong> TXST Love Data Week 2026...</p>
        <p><strong>Data Source:</strong> Texas Department of Biological Resources...</p>
    </div>
</header>
```

**Purpose**: Introduce the dashboard and provide context

**Components**:
- `<h1>`: Main title (h1 for SEO, only one per page)
- `<p class="subtitle">`: Subtitle
- `<div class="intro">`: Project description and data source

### Controls Section (Lines 252-265)

```html
<div class="controls">
    <select id="regionSelect">
        <option value="">All Regions</option>
        <!-- Options populated by JavaScript -->
    </select>

    <select id="wugTypeSelect">
        <option value="">All WUG Types</option>
        <!-- Options populated by JavaScript -->
    </select>

    <input type="number" id="yearSelect"
           placeholder="Select Year (2020-2070)"
           min="2020" max="2070" value="2050">

    <button onclick="updateDashboard()">Update Dashboard</button>
    <button onclick="downloadData()">📥 Download Data</button>
</div>
```

**Purpose**: Allow users to filter data and control dashboard

**Components**:
- `<select id="regionSelect">`: Dropdown for region filtering
- `<select id="wugTypeSelect">`: Dropdown for water user group type
- `<input id="yearSelect">`: Numeric input for year selection
- Update Button: Triggers `updateDashboard()` function
- Download Button: Triggers `downloadData()` function

**JavaScript Connection**:
```javascript
// Data flows from controls to these functions:
document.getElementById('regionSelect').value    // → updateDashboard()
document.getElementById('wugTypeSelect').value   // → updateDashboard()
document.getElementById('yearSelect').value      // → updateDashboard()
```

### Statistics Grid (Lines 271-288)

```html
<div class="stats-grid" id="statsGrid">
    <div class="stat-box">
        <div class="stat-label">Total Records</div>
        <div class="stat-value" id="totalRecords">--</div>
    </div>
    <!-- Similar for totalRegions, totalWugTypes, dataCoverage -->
</div>
```

**Purpose**: Display summary statistics

**Dynamic Content**: JavaScript populates these on data load:
```javascript
document.getElementById('totalRecords').textContent = allData.demands.length;
document.getElementById('totalRegions').textContent =
    new Set(allData.demands.map(d => d.WugRegion)).size;
```

### Charts Grid (Lines 290-306)

```html
<div class="charts-grid">
    <div class="chart-box">
        <div class="chart-title">Demands by Region (2050)</div>
        <div class="chart" id="demandsChart"></div>
    </div>

    <div class="chart-box">
        <div class="chart-title">Demand Projection Over Time</div>
        <div class="chart" id="projectionChart"></div>
    </div>
</div>
```

**Purpose**: Container for Plotly charts

**Container IDs**: JavaScript targets these IDs to render charts:
- `demandsChart` - Bar chart
- `projectionChart` - Line chart (future: add more chart IDs)

### Data Table (Lines 301-306)

```html
<div class="chart-box">
    <div class="chart-title">Detailed Data Table</div>
    <div id="dataTable" class="data-table">
        <div class="loading">Loading data...</div>
    </div>
</div>
```

**Purpose**: Display filtered data in tabular format

**Dynamic Content**: JavaScript populates with HTML table:
```javascript
document.getElementById('dataTable').innerHTML = html;  // Where html is <table>...</table>
```

### Footer (Lines 308-315)

```html
<footer>
    <p>Texas Water Crisis Analysis - TXST Datathon 2026</p>
    <p>Data Source: <a href="...">Texas State Water Plan</a></p>
    <a href="https://github.com/...">📂 View on GitHub</a>
</footer>
```

**Purpose**: Attribution and external links

**Elements**:
- Project credit
- Data source links
- GitHub repository link

---

## CSS Styling Guide

All CSS is embedded in the `<style>` section (lines 9-239).

### CSS Architecture

```
Global Reset & Variables
    ↓
Base Element Styling (body, header, footer, etc.)
    ↓
Component Styling (buttons, forms, cards)
    ↓
Layout Styling (grid, flexbox, containers)
    ↓
Responsive Media Queries
```

### CSS Variables (Not Used - Could Be Added)

**Potential Enhancement**:
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --background-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    --border-radius: 10px;
    --transition-duration: 0.3s;
}

/* Then use throughout */
button {
    background: var(--primary-color);
    border-radius: var(--border-radius);
    transition: background var(--transition-duration);
}
```

### Core Color Scheme

| Color | Hex | Usage |
|-------|-----|-------|
| Primary Blue | #667eea | Buttons, borders, primary text |
| Secondary Purple | #764ba2 | Hover states, line charts |
| Light Gray | #f5f5f5 | Table headers, backgrounds |
| Dark Text | #333 | Main body text |
| Light Text | #666 | Secondary text, labels |

### Layout Components

**Container**:
```css
.container {
    max-width: 1400px;      /* Desktop: 1400px max width */
    margin: 0 auto;         /* Center horizontally */
    padding: 20px;          /* Inner spacing */
}
```

**Grid Layout for Charts**:
```css
.charts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
    gap: 20px;              /* Space between cards */
}
```
- Auto-fits as many 600px columns as fit screen
- Responsive: 2 columns on desktop, 1 on mobile

**Flexbox for Controls**:
```css
.controls {
    display: flex;
    gap: 20px;              /* Space between items */
    flex-wrap: wrap;        /* Wrap on small screens */
    align-items: center;    /* Vertically center items */
}
```

### Form Styling

**Dropdowns and Inputs**:
```css
select, input {
    padding: 10px;
    border: 2px solid #ddd;
    border-radius: 5px;
    font-size: 1em;
    transition: border-color 0.3s;
}

select:focus, input:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
}
```

**Button Styling**:
```css
button {
    background: #667eea;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s;
}

button:hover {
    background: #764ba2;    /* Darker on hover */
}
```

### Card Components

All content boxes use `.chart-box` or `.stat-box`:
```css
.chart-box {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.stat-box {
    border-left: 4px solid #667eea;  /* Color accent */
}
```

### Responsive Design (Mobile-First)

```css
/* Base: All screens */
.charts-grid {
    grid-template-columns: 1fr;     /* 1 column (mobile) */
}

/* Tablet and above: 768px+ */
@media (min-width: 768px) {
    .charts-grid {
        grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
    }

    .controls {
        flex-direction: row;        /* Horizontal layout */
    }
}

/* Mobile: < 768px */
@media (max-width: 768px) {
    h1 {
        font-size: 1.8em;           /* Smaller heading */
    }

    .controls {
        flex-direction: column;     /* Stack vertically */
        align-items: stretch;       /* Full width buttons */
    }
}
```

### Typography

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #333;
    line-height: 1.6;
}

h1 {
    font-size: 2.5em;
    color: #667eea;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 1.1em;
    color: #666;
}

.stat-label {
    font-size: 0.9em;
    text-transform: uppercase;     /* Capital letters */
    color: #666;
}

.stat-value {
    font-size: 2em;
    color: #667eea;
    font-weight: bold;
}
```

### Theming Extension

To create a dark theme, add:
```css
body.dark-theme {
    background: #1a1a1a;
    color: #e0e0e0;
}

body.dark-theme .chart-box {
    background: #2a2a2a;
    color: #e0e0e0;
}

body.dark-theme button {
    background: #764ba2;
}
```

---

## Key JavaScript Libraries

### Plotly.js

**What It Does**: Interactive data visualization library

**CDN Link**: `https://cdn.plot.ly/plotly-2.26.0.min.js`

**Usage in Dashboard**:
```javascript
Plotly.newPlot(
    'chartId',           // HTML element ID to render into
    [trace],             // Array of data traces
    layout,              // Chart layout configuration
    { responsive: true } // Options
);
```

**Example Trace (Bar Chart)**:
```javascript
const trace = {
    x: ['Austin', 'Houston', 'San Antonio'],     // X-axis values
    y: [450, 520, 380],                          // Y-axis values
    type: 'bar',                                 // Chart type
    marker: { color: '#667eea' },               // Styling
    hovertemplate: '<b>%{x}</b><br>Demand: %{y:.0f}<extra></extra>'
};
```

**Key Features**:
- 40+ chart types (we use: bar, scatter/line, box, histogram)
- Interactive hover information
- Zoom and pan capabilities
- Download chart as PNG
- Responsive resizing
- Touch support for mobile

**Documentation**: https://plotly.com/javascript/

### PapaParse

**What It Does**: Parses CSV files into JavaScript objects

**CDN Link**: `https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js`

**Usage in Dashboard**:
```javascript
const data = Papa.parse(csvText, {
    header: true,                    // Use first row as headers
    dynamicTyping: false,           // Keep as strings (except numbers)
    skipEmptyLines: true            // Ignore blank lines
});

// Result: data.data = [{EntityName: "...", WugRegion: "...", ...}, ...]
```

**Example CSV Parsing**:
```javascript
// Input: CSV text
const csvText = "EntityName,WugType,D2050\nAustin,Municipal,450\n";

// Parse
const result = Papa.parse(csvText, { header: true });

// Output:
// result.data = [
//   { EntityName: "Austin", WugType: "Municipal", D2050: "450" },
//   ...
// ]
```

**Key Features**:
- Automatic header detection
- Handles quoted fields with commas
- Skip empty lines
- Error detection for malformed CSV
- Streaming large files
- Dynamic type detection

**Documentation**: https://www.papaparse.com/

### Vanilla JavaScript ES6+ Features Used

**Arrow Functions**:
```javascript
// Cleaner syntax for callbacks
allData.demands.map(d => d.WugRegion)
```

**Template Literals**:
```javascript
// String interpolation
console.log(`Loading from /data/${fileName}`)
```

**Async/Await**:
```javascript
// Cleaner asynchronous code
async function loadCSVFiles() {
    const response = await fetch(`/data/demands.csv`);
    const text = await response.text();
    // ...
}
```

**Spread Operator**:
```javascript
// Create new array without mutation
const uniqueRegions = [...new Set(allData.demands.map(d => d.WugRegion))];
```

**Array Methods**:
```javascript
.map()      // Transform elements
.filter()   // Select elements matching condition
.reduce()   // Aggregate into single value
.find()     // Get first element matching condition
.some()     // Check if any element matches
.every()    // Check if all elements match
```

**Set for Unique Values**:
```javascript
// Get unique regions
const regions = new Set(allData.demands.map(d => d.WugRegion));
const regionsArray = [...regions];  // Convert back to array
```

---

## Data Loading Mechanism

### Initialization Flow

```
Page Load Event
    ↓
initDashboard() called
    ↓
loadCSVFiles() fetches and parses CSV files
    ↓
allData object populated with parsed data
    ↓
populateSelects() creates dropdown options
    ↓
updateDashboard() renders initial charts
    ↓
Dashboard ready for user interaction
```

### Step 1: Window Load Event

```javascript
window.addEventListener('load', initDashboard);
```

Triggers when page fully loads (HTML parsed, images loaded, etc.)

### Step 2: Initialize Dashboard

```javascript
async function initDashboard() {
    try {
        await loadCSVFiles();           // Load all CSV files
        populateSelects();              // Populate dropdowns
        updateDashboard();              // Render initial charts
    } catch (error) {
        console.error('Error loading data:', error);
    }
}
```

**Try/Catch**: Handles errors gracefully

### Step 3: Load CSV Files

```javascript
async function loadCSVFiles() {
    const files = ['demands.csv', 'existing.csv', 'needs.csv', 'population.csv', 'strategies.csv'];

    for (const file of files) {
        try {
            // 1. Fetch file from server
            const response = await fetch(`/data/${file}`);

            // 2. Convert to text
            const text = await response.text();

            // 3. Parse CSV with PapaParse
            const data = Papa.parse(text, { header: true });

            // 4. Store in allData object
            allData[file.replace('.csv', '')] = data.data;
        } catch (e) {
            console.warn(`Could not load ${file}:`, e);
        }
    }

    // 5. Update statistics
    document.getElementById('totalRecords').textContent = allData.demands.length;
    // ...
}
```

### Data Structure After Loading

```javascript
allData = {
    demands: [
        { EntityName: "Austin", WugType: "Municipal", WugRegion: "Region 4", D2020: 400, D2050: 450, D2070: 490 },
        { EntityName: "Houston", WugType: "Municipal", WugRegion: "Region 12", D2020: 480, D2050: 570, D2070: 630 },
        // ... more entries
    ],
    existing: [ /* ... */ ],
    needs: [ /* ... */ ],
    population: [ /* ... */ ],
    strategies: [ /* ... */ ]
}
```

### Step 4: Populate Dropdowns

```javascript
function populateSelects() {
    if (allData.demands.length === 0) return;

    // Extract unique regions
    const regions = [...new Set(allData.demands.map(d => d.WugRegion))];

    // Extract unique WUG types
    const wugTypes = [...new Set(allData.demands.map(d => d.WugType))];

    // Add to DOM
    const regionSelect = document.getElementById('regionSelect');
    regions.forEach(r => {
        const option = document.createElement('option');
        option.value = r;
        option.textContent = r;
        regionSelect.appendChild(option);
    });

    // Same for wugTypes dropdown
}
```

### Step 5: Render Initial Dashboard

```javascript
function updateDashboard() {
    // 1. Get filter values
    const region = document.getElementById('regionSelect').value;
    const wugType = document.getElementById('wugTypeSelect').value;
    const year = document.getElementById('yearSelect').value || '2050';

    // 2. Filter data
    let filtered = allData.demands.filter(d =>
        (!region || d.WugRegion === region) &&
        (!wugType || d.WugType === wugType)
    );

    // 3. Update all visualizations
    updateDemandsChart(filtered, year);
    updateProjectionChart(filtered);
    updateDataTable(filtered);
}
```

### Data Caching

**Browser Caching**:
- CSV files cached by browser after first load
- Subsequent page visits load from cache
- User sees instant load on repeat visits

**In-Memory Caching**:
```javascript
let allData = { ... };  // Loaded once, reused for all operations
```
- No server requests for filtering
- All filtering happens in JavaScript
- Fast response (< 100ms typically)

---

## 5 Chart Types with Examples

### Chart 1: Bar Chart - Top Demands by Entity

**Type**: Horizontal or vertical bar chart

**Purpose**: Compare water demand across different entities

**Configuration**:
```javascript
function updateDemandsChart(data, year) {
    // Select the column for chosen year (D2020, D2050, D2070)
    const yearCol = `D${year}`;

    // Transform data for Plotly
    const demands = data
        .filter(d => d[yearCol])                    // Only rows with data
        .slice(0, 20)                              // Top 20 only
        .map(d => ({
            entity: d.EntityName,
            demand: parseFloat(d[yearCol]) || 0
        }))
        .sort((a, b) => b.demand - a.demand);      // Sort descending

    // Create Plotly trace
    const trace = {
        x: demands.map(d => d.entity),             // Entity names on X-axis
        y: demands.map(d => d.demand),             // Demand values on Y-axis
        type: 'bar',
        marker: { color: '#667eea' },
        hovertemplate: '<b>%{x}</b><br>Demand: %{y:.0f} acre-feet<extra></extra>'
    };

    // Layout configuration
    const layout = {
        title: `Top 20 Demands - ${year}`,
        xaxis: { title: 'Entity' },
        yaxis: { title: 'Demand (acre-feet)' },
        hovermode: 'closest',
        margin: { b: 100 }                         // Bottom margin for labels
    };

    // Render
    Plotly.newPlot('demandsChart', [trace], layout, { responsive: true });
}
```

**Visual Appearance**:
```
         Top 20 Demands - 2050
600 |     ███████████  ███████
500 |     ███████████  ███████
400 |  ███ ███████████  ███████
300 |  ███ ███████████  ███████
200 |  ███ ███████████  ███████
100 |  ███ ███████████  ███████
  0 |__███_███████████__███████___
      Austin Houston San Antonio...
```

**Interactive Features**:
- Hover: Shows entity name and exact demand
- Click legend: Can toggle individual cities
- Download: Click camera icon to save as PNG
- Zoom: Click and drag to zoom into area

**Data Example**:
```javascript
// Input:
data = [
    { EntityName: "Austin", D2050: 450 },
    { EntityName: "Houston", D2050: 570 },
    { EntityName: "San Antonio", D2050: 410 }
]

// Output chart shows:
Houston:        ████████████████████  570
Austin:         ████████████████      450
San Antonio:    ███████████████       410
```

### Chart 2: Line Chart - Demand Projections Over Time

**Type**: Scatter with lines and markers

**Purpose**: Show trend of demand growth from 2020-2070

**Configuration**:
```javascript
function updateProjectionChart(data) {
    // Year columns in CSV
    const yearColumns = ['D2020', 'D2030', 'D2040', 'D2050', 'D2060', 'D2070'];
    const years = [2020, 2030, 2040, 2050, 2060, 2070];

    // Calculate average demand per year
    const avgByYear = yearColumns.map((col, i) => {
        const avg = data
            .filter(d => d[col])
            .reduce((sum, d) => sum + (parseFloat(d[col]) || 0), 0) / data.length;
        return avg;
    });

    // Create Plotly trace
    const trace = {
        x: years,                                   // X-axis: Years
        y: avgByYear,                              // Y-axis: Average demand
        type: 'scatter',
        mode: 'lines+markers',                     // Both lines and points
        line: { color: '#764ba2', width: 3 },     // Purple, thick line
        marker: { size: 8 },
        fill: 'tozeroy',                           // Fill under curve
        hovertemplate: '<b>%{x}</b><br>Avg Demand: %{y:.0f} acre-feet<extra></extra>'
    };

    // Layout
    const layout = {
        title: 'Average Demand Projection (2020-2070)',
        xaxis: { title: 'Year' },
        yaxis: { title: 'Average Demand (acre-feet)' },
        hovermode: 'x unified'
    };

    // Render
    Plotly.newPlot('projectionChart', [trace], layout, { responsive: true });
}
```

**Visual Appearance**:
```
400 |        ◆ Avg Demand Projection
350 |      /   \
300 |    /       \
250 |  /           \
200 |/               \
150 |                 ◆
  0 |___________________
    2020  2030  2040  2050  2060  2070
```

**Interactive Features**:
- Hover: Shows year and average demand
- Zoom: Click and drag to zoom into time period
- Pan: Drag to move time window
- Download: Save as PNG

**Data Example**:
```
Year    Avg Demand
2020    250
2030    280
2040    310
2050    340
2060    365
2070    390
```

### Chart 3: Box Plot - Distribution Analysis (Future)

**Type**: Box and whisker plot

**Purpose**: Show demand distribution across regions

**Configuration** (not yet implemented):
```javascript
function updateBoxPlotChart(data) {
    // Group by region
    const regions = [...new Set(data.map(d => d.WugRegion))];

    // Create trace for each region
    const traces = regions.map(region => ({
        y: data
            .filter(d => d.WugRegion === region)
            .map(d => parseFloat(d.D2050)),
        name: region,
        type: 'box',
        boxmean: 'sd'  // Show mean and standard deviation
    }));

    const layout = {
        title: 'Demand Distribution by Region (2050)',
        yaxis: { title: 'Demand (acre-feet)' }
    };

    Plotly.newPlot('boxPlotChart', traces, layout, { responsive: true });
}
```

**Visual Appearance**:
```
700 |
600 |        ×──◆──×    (Whiskers = min/max)
500 |        │  │  │    (Box = Q1 to Q3)
400 |    ┌───┤  │  ├───┐ (Line = median)
300 |    │   │  │  │   │ (× = outliers)
200 |    └───┤  │  ├───┘
100 |        │  │  │
  0 |___________│__│__
      Region1 Region2
```

**Shows**:
- Min/max values (whiskers)
- First and third quartile (box)
- Median (line inside box)
- Mean (dot)
- Outliers (×)

### Chart 4: Histogram - Frequency Distribution (Future)

**Type**: Histogram

**Purpose**: Show frequency of demand values

**Configuration** (not yet implemented):
```javascript
function updateHistogramChart(data) {
    const demands = data.map(d => parseFloat(d.D2050)).filter(d => d > 0);

    const trace = {
        x: demands,
        type: 'histogram',
        nbinsx: 30,  // Number of bins
        marker: { color: '#667eea' }
    };

    const layout = {
        title: 'Distribution of Water Demands (2050)',
        xaxis: { title: 'Demand (acre-feet)' },
        yaxis: { title: 'Frequency' }
    };

    Plotly.newPlot('histogramChart', [trace], layout, { responsive: true });
}
```

**Visual Appearance**:
```
Frequency
    20 |
    18 |     ████
    16 |     ████  ████
    14 |     ████  ████
    12 |  ████████████
    10 |  ████████████
     8 |  ████████████  ████
     6 |  ████████████  ████
     4 |  ████████████  ████  ████
     2 |  ████████████  ████  ████
     0 |__████████████__████__████___
       0   100  200  300  400  500
              Demand (acre-feet)
```

**Shows**:
- How many entities fall into each demand range
- Identifies common demand levels
- Reveals if there's bimodal distribution

### Chart 5: Comparison Chart - Multiple Years (Future)

**Type**: Grouped or stacked bar chart

**Purpose**: Compare demand across multiple years side-by-side

**Configuration** (not yet implemented):
```javascript
function updateComparisonChart(data) {
    // Top 10 entities
    const top10 = data
        .sort((a, b) => parseFloat(b.D2050) - parseFloat(a.D2050))
        .slice(0, 10);

    // Create trace for each year
    const years = [2020, 2050, 2070];
    const traces = years.map(year => ({
        x: top10.map(d => d.EntityName),
        y: top10.map(d => parseFloat(d[`D${year}`])),
        name: year.toString(),
        type: 'bar'
    }));

    const layout = {
        title: 'Top 10 Entities: Demand Projection',
        barmode: 'group',  // Side-by-side bars
        yaxis: { title: 'Demand (acre-feet)' }
    };

    Plotly.newPlot('comparisonChart', traces, layout, { responsive: true });
}
```

**Visual Appearance**:
```
500 |  █ █ █
400 |  █ █ █
300 |  █ █ █  █ █ █
200 |  █ █ █  █ █ █
100 |  █ █ █  █ █ █  █ █ █
  0 |__█_█_█__█_█_█__█_█_█__
      Austin     Houston    SA

      2020 2050 2070 (legend)
```

**Shows**:
- Growth trajectory for each entity
- Which entities growing fastest
- Which regions stable vs. volatile

---

## Export Functionality

### CSV Export Feature

**Button**: "📥 Download Data" in controls section

**Functionality**: Downloads filtered data as CSV file

**Implementation**:
```javascript
function downloadData() {
    // Get selected year
    const year = document.getElementById('yearSelect').value || '2050';
    const yearCol = `D${year}`;

    // Create CSV text
    let csv = 'EntityName,WugType,Region,County,' + yearCol + '\n';
    allData.demands.forEach(d => {
        csv += `${d.EntityName},${d.WugType},${d.WugRegion},${d.WugCounty},${d[yearCol]}\n`;
    });

    // Create downloadable blob
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);

    // Create link and click it
    const a = document.createElement('a');
    a.href = url;
    a.download = `texas-water-data-${year}.csv`;
    a.click();

    // Cleanup
    window.URL.revokeObjectURL(url);
}
```

**User Experience**:
1. User selects filters (region, WUG type, year)
2. User clicks "Download Data" button
3. Browser downloads file: `texas-water-data-2050.csv`
4. File opens in default spreadsheet application
5. User can view, edit, or share data

**Downloaded File Format**:
```csv
EntityName,WugType,Region,County,D2050
Austin,Municipal,Region 4,Travis,450
San Antonio,Municipal,Region 15,Bexar,410
Houston,Municipal,Region 12,Harris,570
```

### Chart Export (Plotly Built-In)

**Method**: Click camera icon on any chart

**What Happens**:
1. Hover over chart
2. Toolbar appears in top-right
3. Click camera icon
4. Chart downloads as PNG image

**File Name**: `chart.png` (browser default)

**Image Quality**: High resolution, good for presentations

### Potential Future Export Formats

**Excel (.xlsx)**:
```javascript
// Would require xlsx library
// Creates multi-sheet workbook
```

**JSON**:
```javascript
// Export as JSON for data analysis
const json = JSON.stringify(filteredData, null, 2);
```

**PDF Report**:
```javascript
// Requires pdf library (jsPDF)
// Creates formatted document with charts and tables
```

---

## Mobile Responsiveness

### Design Approach: Mobile-First

CSS written for mobile first, enhanced with media queries for larger screens.

### Breakpoints

| Device | Width | Breakpoint | Layout |
|--------|-------|-----------|--------|
| Mobile Phone | 320-480px | Base | 1 column, full-width buttons |
| Tablet (Portrait) | 481-768px | @media (min-width: 480px) | 2 rows, flexible |
| Tablet (Landscape) | 769-1024px | @media (min-width: 768px) | 2 columns |
| Desktop | 1025px+ | @media (min-width: 1024px) | Full layout |

### Mobile-Specific CSS

**Charts on Mobile**:
```css
/* Base: Mobile */
.chart {
    height: 300px;    /* Smaller on mobile */
}

.charts-grid {
    grid-template-columns: 1fr;  /* Single column */
    gap: 15px;                   /* Less space */
}

/* Tablet/Desktop */
@media (min-width: 768px) {
    .chart {
        height: 400px;            /* Larger on desktop */
    }

    .charts-grid {
        grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
    }
}
```

**Controls on Mobile**:
```css
/* Base: Mobile */
.controls {
    flex-direction: column;    /* Stack vertically */
    gap: 10px;
}

select, input, button {
    width: 100%;              /* Full width */
    min-height: 44px;         /* Touch-friendly size */
}

/* Tablet/Desktop */
@media (min-width: 768px) {
    .controls {
        flex-direction: row;   /* Horizontal layout */
        flex-wrap: wrap;
        gap: 20px;
    }

    select, input, button {
        width: auto;
    }
}
```

**Typography on Mobile**:
```css
/* Base: Mobile */
h1 {
    font-size: 1.8em;      /* Smaller heading */
}

.subtitle {
    font-size: 0.95em;
}

/* Desktop */
@media (min-width: 1024px) {
    h1 {
        font-size: 2.5em;
    }

    .subtitle {
        font-size: 1.1em;
    }
}
```

**Table on Mobile**:
```css
/* Base: Mobile */
.data-table {
    overflow-x: auto;        /* Horizontal scroll */
    font-size: 0.9em;
}

/* Tablet/Desktop */
@media (min-width: 768px) {
    .data-table {
        overflow-x: visible;
        font-size: 1em;
    }
}
```

### Touch Optimization

**Button Sizing**:
- Minimum 44x44 pixels (Apple Human Interface Guidelines)
- Adequate padding: 12px minimum
- Spacing: 20px+ between tap targets

**Form Elements**:
- Native `<select>` used (shows OS picker on mobile)
- Large input fields (44px height minimum)
- Autocomplete for common values

**Scrolling**:
- Smooth scrolling on mobile
- Horizontal scroll for tables
- Sticky headers for easy navigation

### Testing on Mobile

**iOS Safari**:
```
iPhone SE (375px): Single column, touch-friendly buttons
iPhone 13 Pro (390px): Similar to SE
iPad Air (768px): Two-column layout
iPad Pro (1024px): Full desktop layout
```

**Android Chrome**:
```
Pixel 4 (412px): Single column
Pixel 5 (393px): Similar
Samsung S21 (360px): Single column
Tablet (600px+): Multi-column
```

---

## Browser Support Matrix

### Supported Browsers

| Browser | Min Version | Status | Notes |
|---------|-------------|--------|-------|
| Chrome | 90 (2021) | Full Support | ✓ All features work |
| Firefox | 88 (2021) | Full Support | ✓ All features work |
| Safari | 14 (2021) | Full Support | ✓ All features work |
| Edge | 90 (2021) | Full Support | ✓ All features work |
| Internet Explorer | 11 | Not Supported | ✗ Use Edge instead |

### Feature Compatibility

| Feature | Chrome | Firefox | Safari | Edge | IE11 |
|---------|--------|---------|--------|------|------|
| HTML5 Semantic | ✓ | ✓ | ✓ | ✓ | △ |
| CSS Grid | ✓ | ✓ | ✓ (11.1+) | ✓ | ✗ |
| CSS Flexbox | ✓ | ✓ | ✓ (9+) | ✓ | △ |
| Fetch API | ✓ | ✓ | ✓ (10.1+) | ✓ | ✗ |
| Promises | ✓ | ✓ | ✓ (9+) | ✓ | ✗ |
| Arrow Functions | ✓ | ✓ | ✓ (10+) | ✓ | ✗ |
| Template Literals | ✓ | ✓ | ✓ (9+) | ✓ | ✗ |
| Plotly.js | ✓ | ✓ | ✓ | ✓ | △ |
| PapaParse | ✓ | ✓ | ✓ | ✓ | ✓ |

**Legend**: ✓ = Full support | △ = Partial support | ✗ = Not supported

### Fallbacks for Older Browsers

**For users on older browsers** (IE 11, older Safari):

1. **Polyfills** (not included currently):
```html
<!-- For older browsers, add: -->
<script src="https://cdn.jsdelivr.net/npm/@babel/polyfill@7/dist/polyfill.min.js"></script>
```

2. **Feature Detection**:
```javascript
// Check if browser supports Fetch
if (!window.fetch) {
    alert('Your browser is too old. Please upgrade to Chrome, Firefox, Safari 14+, or Edge.');
}
```

3. **Graceful Degradation**:
- Charts still render (Plotly.js handles most older browsers)
- CSV export works (doesn't use modern APIs)
- Basic styling works (CSS Grid degrades to single column)

### Testing Across Browsers

**Cross-Browser Testing Tools**:
- BrowserStack: Test on real devices
- Sauce Labs: Cloud-based testing
- Local testing: Install multiple browsers

**Test Checklist**:
- [ ] Charts render correctly
- [ ] Filters work properly
- [ ] Download button works
- [ ] Mobile layout correct
- [ ] Hover tooltips display
- [ ] No console errors

---

## Performance Considerations

### Data Size Limits

**Current Dashboard Handles**:
- Up to 10,000 entity records
- 5 CSV files loaded simultaneously
- 6 chart instances rendered
- Responsive on most devices

**Performance Targets**:
- Initial page load: < 2 seconds
- Chart update after filter: < 500ms
- CSV download: Instant
- Mobile rendering: Smooth scrolling

### Optimization Techniques

**1. Data Caching**:
```javascript
let allData = { ... };  // Loaded once
// All filtering reuses this data (no server calls)
```

**2. Lazy Rendering**:
```javascript
.slice(0, 20)   // Only render top 20 bars
.slice(0, 50)   // Only show 50 rows in table
```

**3. Efficient Filtering**:
```javascript
.filter(d =>
    (!region || d.WugRegion === region) &&
    (!wugType || d.WugType === wugType)
)
// Uses short-circuit evaluation (stops when first condition fails)
```

**4. Responsive Charts**:
```javascript
Plotly.newPlot('chart', [trace], layout, { responsive: true });
// Charts resize without re-rendering all data
```

### Performance Monitoring

**Browser DevTools**:
1. Open F12
2. Performance tab
3. Record session
4. Analyze timeline

**Key Metrics**:
- **Page Load Time**: < 3 seconds
- **Time to Interactive**: < 2 seconds
- **First Paint**: < 1 second
- **Filter Response Time**: < 500ms

### Bottlenecks to Monitor

| Bottleneck | Symptom | Solution |
|-----------|---------|----------|
| Large CSV files | Slow loading | Split data, implement pagination |
| Too many DOM nodes | Slow rendering | Limit table rows, virtual scrolling |
| Complex filtering | Slow updates | Use Web Workers, optimize logic |
| Chart re-rendering | Jank on interactions | Increase debounce delay |

### Scaling to Larger Datasets

**Current Capacity**: 10,000+ entities

**Scaling Strategies**:

1. **Pagination**:
```javascript
// Show 50 items per page
const perPage = 50;
const page = 1;
const startIdx = (page - 1) * perPage;
const pageData = filteredData.slice(startIdx, startIdx + perPage);
```

2. **Virtual Scrolling**:
```javascript
// Only render visible items in scrollable container
// Libraries: react-window, vue-virtual-scroll
```

3. **Web Workers**:
```javascript
// Offload data processing to background thread
const worker = new Worker('processor.js');
worker.postMessage({ data, filters });
```

4. **Server-Side Processing**:
```javascript
// Move filtering to server
fetch('/api/demands?region=Region4&year=2050');
```

---

## Common Tasks

### Task 1: Adding a New Chart Type

**Step 1: Add HTML container**
```html
<div class="chart-box">
    <div class="chart-title">My New Chart</div>
    <div class="chart" id="myNewChart"></div>
</div>
```

**Step 2: Create rendering function**
```javascript
function updateMyNewChart(data, year) {
    const trace = {
        // Define your trace
    };

    const layout = {
        title: 'My New Chart Title',
        xaxis: { title: 'X Axis Label' },
        yaxis: { title: 'Y Axis Label' }
    };

    Plotly.newPlot('myNewChart', [trace], layout, { responsive: true });
}
```

**Step 3: Call function from updateDashboard**
```javascript
function updateDashboard() {
    // ... existing code ...
    updateMyNewChart(filtered, year);  // Add this line
}
```

**Step 4: Test**
- Reload page
- Chart should render with live data

### Task 2: Adding a New Filter Option

**Step 1: Add HTML dropdown**
```html
<select id="newFilter">
    <option value="">All Options</option>
    <!-- Options populated by JavaScript -->
</select>
```

**Step 2: Populate in populateSelects()**
```javascript
function populateSelects() {
    // ... existing code ...

    const newOptions = [...new Set(allData.demands.map(d => d.NewField))];
    const select = document.getElementById('newFilter');
    newOptions.forEach(opt => {
        const option = document.createElement('option');
        option.value = opt;
        option.textContent = opt;
        select.appendChild(option);
    });
}
```

**Step 3: Apply filter in updateDashboard()**
```javascript
function updateDashboard() {
    const region = document.getElementById('regionSelect').value;
    const wugType = document.getElementById('wugTypeSelect').value;
    const newFilter = document.getElementById('newFilter').value;  // Add this

    let filtered = allData.demands.filter(d =>
        (!region || d.WugRegion === region) &&
        (!wugType || d.WugType === wugType) &&
        (!newFilter || d.NewField === newFilter)  // Add this condition
    );

    // ... rest of function ...
}
```

### Task 3: Changing Chart Colors

**Option 1: Edit CSS color variables**
```css
:root {
    --primary-color: #667eea;   /* Change this */
    --secondary-color: #764ba2; /* Or this */
}
```

**Option 2: Edit inline in JavaScript**
```javascript
marker: { color: '#667eea' }  // Change hex color

// Or use RGB
marker: { color: 'rgb(102, 126, 234)' }

// Or use CSS color names
marker: { color: 'steelblue' }
```

**Option 3: Create theme switcher**
```javascript
function applyTheme(theme) {
    if (theme === 'dark') {
        document.body.classList.add('dark-theme');
    } else {
        document.body.classList.remove('dark-theme');
    }
}

// Add CSS for dark theme
```

### Task 4: Adding CSV Export Options

**Current**: Exports single year as CSV

**Enhancement: Multi-year export**
```javascript
function downloadDataMultiYear() {
    let csv = 'EntityName,WugType,Region,D2020,D2050,D2070\n';

    allData.demands.forEach(d => {
        csv += `${d.EntityName},${d.WugType},${d.WugRegion},${d.D2020},${d.D2050},${d.D2070}\n`;
    });

    const blob = new Blob([csv], { type: 'text/csv' });
    // ... rest of download logic ...
}
```

**Enhancement: JSON export**
```javascript
function downloadDataJSON() {
    const json = JSON.stringify(allData.demands, null, 2);
    const blob = new Blob([json], { type: 'application/json' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'texas-water-data.json';
    a.click();
}
```

---

## Troubleshooting

### Issue 1: Charts Not Displaying

**Symptoms**: Empty chart containers, no error messages

**Causes**:
1. CSV files not loading
2. Data format incorrect
3. Plotly library not loaded

**Debug Steps**:
```javascript
// In browser console (F12):
console.log(allData);         // Check if data loaded
console.log(Plotly);          // Check if Plotly available
console.log(window.location); // Check URL
```

**Solutions**:
1. Verify CSV files in `/data/` folder
2. Check column names in CSV match code
3. Verify CDN URLs are correct
4. Check Network tab (F12) for failed requests

### Issue 2: Dropdown Menus Empty

**Symptoms**: Select elements show no options

**Cause**: Data not loaded or populated incorrectly

**Debug**:
```javascript
// In console:
allData.demands[0]           // Check first record
allData.demands.length       // Check data count
new Set(allData.demands.map(d => d.WugRegion)) // Check unique values
```

**Solution**:
- Ensure CSV has header row
- Verify column name is exactly "WugRegion"
- Check data loads (use network tab)

### Issue 3: Filters Not Working

**Symptoms**: Filter changes don't affect charts

**Cause**: updateDashboard() not triggered or filtering logic broken

**Debug**:
```javascript
// Add to updateDashboard():
console.log('Filter called');
console.log('Region:', document.getElementById('regionSelect').value);
console.log('Filtered data count:', filtered.length);
```

**Solution**:
- Verify button onclick calls updateDashboard()
- Check filter conditions in filter() function
- Verify column names match CSV headers

### Issue 4: CSV Download Not Working

**Symptoms**: Download button does nothing

**Cause**: Blob/URL API not supported or blocked

**Debug**:
```javascript
// In console:
new Blob(['test'])          // Check if supported
window.URL.createObjectURL  // Check if available
```

**Solution**:
- Use newer browser (IE 11 not supported)
- Check browser console for errors
- Verify download handler code is correct

### Issue 5: Slow Performance

**Symptoms**: Charts take long time to render, interface feels sluggish

**Cause**: Too much data, complex filtering, or device limitations

**Solutions**:
1. Limit chart data:
```javascript
.slice(0, 20)  // Reduce from 20 to 10
```

2. Debounce filter changes:
```javascript
let filterTimeout;
function updateDashboardDebounced() {
    clearTimeout(filterTimeout);
    filterTimeout = setTimeout(updateDashboard, 500);
}
```

3. Monitor performance:
```javascript
console.time('updateDashboard');
updateDashboard();
console.timeEnd('updateDashboard');
```

### Issue 6: Mobile Layout Issues

**Symptoms**: Controls overlapping, charts too small, text unreadable

**Cause**: CSS media queries not applying

**Debug**:
```javascript
// In console:
window.innerWidth    // Check viewport width
getComputedStyle(document.body).fontSize  // Check font size
```

**Solutions**:
- Force hard refresh (Ctrl+Shift+R)
- Check media queries in CSS (lines 225-238)
- Test viewport: F12 > Toggle Device Toolbar

---

## Additional Resources

### Plotly.js Documentation
- Full Chart Types: https://plotly.com/javascript/
- Customization: https://plotly.com/javascript/how-to-use-plotly/
- API Reference: https://plotly.com/javascript/plotly-javascript-open-source-graphing-library/

### PapaParse Documentation
- Guide: https://www.papaparse.com/
- API: https://www.papaparse.com/docs

### Web Standards
- HTML5: https://html.spec.whatwg.org/
- CSS: https://www.w3.org/Style/CSS/
- JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript/

### Data Sources
- TWDB State Water Plan: https://texasstatewaterplan.org/
- TWDB Main Site: https://www.twdb.texas.gov/

---

## Getting Help

**For Developers**: See ARCHITECTURE.md for system design details

**For Setup**: See SETUP_LOCAL.md for local development instructions

**For Questions**: Check the troubleshooting section above

**For Contributions**: See CONTRIBUTING.md (if available)

---

**Last Updated**: February 2026
**Project**: Texas Water Crisis Analysis - TXST Love Data Week 2026
**License**: CC-BY-4.0 (Creative Commons Attribution)
