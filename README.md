# datathon-water-analysis

Interactive dashboard analyzing Texas water crisis and forecasting infrastructure viability.

## Overview

This project develops a comprehensive data analysis and visualization platform for understanding Texas water resources, demand patterns, and long-term infrastructure sustainability. Using real-world data from the Texas Department of Biological Resources (TWDB) and USGS Water Services, we provide interactive tools for exploring complex water management challenges across Texas.

## Features

- **Interactive Plotly Charts**: Dynamic, responsive visualizations for data exploration
- **Real-time Filtering**: Filter datasets by region, time period, and data type
- **Data Export**: Export processed datasets in multiple formats (CSV, JSON)
- **Streamlit Dashboard**: Interactive web application for real-time analysis
- **Static HTML Dashboard**: Standalone HTML reports for offline access and sharing
- **Multi-source Data Integration**: Combines TWDB and USGS datasets into unified analysis platform
- **Predictive Forecasting**: Infrastructure viability forecasts based on historical trends

## Quick Start

### Installation (Windows)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/datathon-water-analysis.git
   cd datathon-water-analysis
   ```

2. **Create a Python virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit dashboard**
   ```bash
   streamlit run app.py
   ```

5. **Access the dashboard**
   - Open your browser and navigate to `http://localhost:8501`

### Quick Configuration

Edit `config.json` to customize:
- Data directories (default: `C:\Users\Arath\Documents\water_data\`)
- Map boundaries and zoom levels
- Chart color schemes
- Export settings

## File Structure

```
datathon-water-analysis/
├── README.md                 # This file
├── CONTRIBUTING.md          # Contribution guidelines
├── SOURCES.md               # Data sources and attribution
├── requirements.txt         # Python dependencies
├── config.json              # Configuration settings
├── app.py                   # Main Streamlit application
├── data/
│   ├── raw/                 # Original datasets from sources
│   │   ├── twdb/            # TWDB datasets
│   │   └── usgs/            # USGS datasets
│   ├── processed/           # Cleaned and transformed data
│   └── metadata.json        # Data schema and documentation
├── src/
│   ├── data_processing.py   # Data cleaning and transformation
│   ├── visualization.py     # Chart and dashboard creation
│   ├── forecasting.py       # Predictive models
│   └── utils.py             # Helper functions
├── dashboards/
│   ├── static/              # HTML dashboard exports
│   └── templates/           # Jinja2 templates
├── notebooks/               # Jupyter notebooks for exploration
└── tests/                   # Unit and integration tests
```

## Data Sources

### Texas Department of Biological Resources (TWDB)

**State Water Plan 2026**

Comprehensive state water planning data with 50-year projections:

- **Datasets**:
  - `demands.csv` - Water demand by sector and region
  - `existing.csv` - Existing water supply infrastructure
  - `needs.csv` - Water supply needs projection
  - `population.csv` - Population projections by region
  - `strategies.csv` - Water management strategy effectiveness

- **Time Period**: 1975-2024
- **Geographic Coverage**: All 16 TWDB Planning Regions
- **Website**: [https://texasstatewaterplan.org/](https://texasstatewaterplan.org/)
- **License**: Public data, proper attribution required
- **Access Date**: [Update with actual access date]

### USGS Water Services

**Real-time and Historical Water Data**

- **Stations**: 3 Texas monitoring stations
  - Big Sandy Creek near Bridgeport
  - Bridgeport Reservoir
  - Nueces River

- **Metrics**:
  - Streamflow (cubic feet per second)
  - Gage height (feet above datum)
  - Reservoir storage (acre-feet)
  - Water elevation (feet)

- **Time Period**: 2022-2024 (collected data)
- **Website**: [https://waterservices.usgs.gov/](https://waterservices.usgs.gov/)
- **License**: Public domain
- **Update Frequency**: Daily (real-time data)

See [SOURCES.md](SOURCES.md) for detailed source documentation and attribution guidelines.

## Deployment

### GitHub Repository

This project is version controlled on GitHub:
```
https://github.com/yourusername/datathon-water-analysis
```

### Vercel Deployment

Static dashboards and web interface deployed on Vercel:

1. **Connect your GitHub repository** to Vercel
2. **Set environment variables** in Vercel dashboard
3. **Configure build settings**:
   - Framework: Other
   - Build command: `python build_static_dashboard.py`
   - Output directory: `dashboards/static/`

4. **Deploy**: Push to main branch to trigger automatic deployment

Deployment URL: `https://datathon-water-analysis.vercel.app/`

## Contributing

We welcome contributions from researchers, developers, and water resource professionals. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:

- How to contribute
- Branch naming conventions
- Commit message standards
- Code style requirements
- Testing procedures

## Team

**Project Leadership**
- Project Manager: [Name]
- Data Science Lead: [Name]
- Visualization Lead: [Name]

**Contributors**
- [Name] - Data processing and pipeline
- [Name] - Dashboard development
- [Name] - Forecasting models
- [Name] - Documentation and testing

## License

This project is licensed under the MIT License. See LICENSE file for details.

Data from TWDB is public domain. Data from USGS is public domain. When using this project or its data, please provide appropriate attribution to both TWDB and USGS.

## Questions & Support

For questions or support:
- Open an issue on GitHub
- Email: [contact@example.com]
- Check our documentation: [SOURCES.md](SOURCES.md) and [CONTRIBUTING.md](CONTRIBUTING.md)

## References

- Texas State Water Plan: https://texasstatewaterplan.org/
- USGS Water Services: https://waterservices.usgs.gov/
- TPWD Water Resources: https://tpwd.texas.gov/
- TCEQ Water Quality: https://www.tceq.texas.gov/
