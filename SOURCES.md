# Data Sources and Attribution

This document provides comprehensive information about all data sources used in the datathon-water-analysis project, including collection methodology, geographic coverage, licensing, and proper attribution guidelines.

## Primary Data Sources

### 1. Texas Department of Biological Resources (TWDB)

The Texas Department of Biological Resources (TWDB) is the primary source for comprehensive water planning data covering the entire state of Texas.

#### State Water Plan 2026

**Overview**

The State Water Plan is Texas's long-range water strategy developed cooperatively by TWDB and 16 regional water planning groups. The 2026 edition includes updated demand projections, supply assessments, and infrastructure recommendations for the next 50 years.

**Datasets**

| Dataset | File | Description | Records | Time Period |
|---------|------|-------------|---------|------------|
| Demands | `demands.csv` | Water demand by sector and region | ~8,000 | 1975-2024 |
| Existing Supply | `existing.csv` | Current water supply infrastructure capacity | ~5,000 | 1975-2024 |
| Water Needs | `needs.csv` | Projected water supply gaps | ~4,000 | 2025-2074 |
| Population | `population.csv` | Population projections by region | ~3,200 | 1975-2074 |
| Strategies | `strategies.csv` | Water management strategy effectiveness | ~2,500 | 2024-2074 |

**Field Descriptions**

- `demands.csv`:
  - `region`: TWDB Planning Region (A-P)
  - `year`: Fiscal year
  - `sector`: Water use sector (Municipal, Agricultural, Industrial, Steam Electric, Aquaculture, Mining)
  - `demand_af`: Water demand in acre-feet
  - `demand_mgd`: Water demand in million gallons per day

- `existing.csv`:
  - `region`: TWDB Planning Region
  - `year`: Fiscal year
  - `source_type`: Water source type (Surface, Groundwater, Reuse)
  - `capacity_af`: Supply capacity in acre-feet
  - `reliability_rating`: Supply reliability (1-10 scale)

- `needs.csv`:
  - `region`: TWDB Planning Region
  - `year`: Fiscal year
  - `demand_af`: Projected demand
  - `supply_af`: Available supply
  - `gap_af`: Supply-demand gap

- `population.csv`:
  - `region`: TWDB Planning Region
  - `county`: Texas county
  - `year`: Fiscal year
  - `population`: Population estimate/projection

- `strategies.csv`:
  - `region`: TWDB Planning Region
  - `year`: Implementation year
  - `strategy_name`: Strategy description
  - `capacity_af`: Additional supply capacity
  - `cost`: Implementation cost (millions)
  - `status`: Implementation status (Proposed, Authorized, Under Construction, Operational)

**Geographic Coverage**

All 16 TWDB Planning Regions:
- Region A: Panhandle
- Region B: South Plains
- Region C: North Central
- Region D: Northeast Texas
- Region E: East Texas
- Region F: Southeast Texas
- Region G: East Central
- Region H: Central
- Region I: Upper Colorado
- Region J: Lavaca
- Region K: Lower Colorado
- Region L: Brazos
- Region M: Trinity
- Region N: Sulphur
- Region O: Neches
- Region P: Sabine

**Time Period**

- Historical data: 1975-2024 (50 years)
- Projections: 2025-2074 (50 years)
- Real-time updates: Annually

**Website**

[https://texasstatewaterplan.org/](https://texasstatewaterplan.org/)

**License and Attribution**

- **License**: Public data
- **Attribution Required**: Yes
- **Proper Citation**:
  ```
  Texas Department of Biological Resources. (2024). State Water Plan 2026.
  Retrieved from https://texasstatewaterplan.org/
  ```
- **No Copyright Restrictions**: Data may be freely used, modified, and distributed with proper attribution

**Data Access**

Files are located in:
- Project repository: `data/raw/twdb/`
- Windows path: `C:\Users\Arath\Documents\Datathon\data\raw\twdb\`
- Mac path: `/Volumes/Arath/Automation_Station/Projects/Datathon/data/raw/twdb/`

**Last Update**

Access Date: [Update with actual access date]
Refresh Schedule: Annual (typically Q1)

---

### 2. USGS Water Services

The United States Geological Survey (USGS) provides real-time and historical water data from monitoring stations across the United States, including critical Texas water resources.

#### Real-time Water Data

**Overview**

USGS maintains continuous monitoring stations that measure streamflow, water elevation, and reservoir storage. Our project integrates data from 3 priority Texas monitoring stations.

**Monitoring Stations**

| Station | Site ID | Location | Metrics | Elevation |
|---------|---------|----------|---------|-----------|
| Big Sandy Creek near Bridgeport | 08046500 | Wise County | Streamflow, Gage Height | 760 ft |
| Bridgeport Reservoir | 08046550 | Wise County | Water Storage, Elevation | 760 ft |
| Nueces River | 08210000 | Uvalde County | Streamflow, Gage Height | 900 ft |

**Data Metrics**

- **Streamflow** (cubic feet per second, cfs)
  - Continuous 15-minute measurements
  - Derived from gage height using rating curves
  - Unit code: 00060

- **Gage Height** (feet above datum)
  - Continuous measurement of water elevation at station
  - Used for streamflow calculation
  - Unit code: 00065

- **Reservoir Storage** (acre-feet, af)
  - Daily measurements of water volume in reservoirs
  - Affects water availability forecasting
  - Unit code: 00301

- **Water Elevation** (feet above mean sea level)
  - Absolute elevation reference for water surface
  - Important for flood risk assessment
  - Unit code: 62615

**Data Collection**

- **Frequency**: Real-time data updated every 15 minutes
- **Historical Availability**: 2022-2024 (project collected data)
- **Data Quality**: Quality-assured; preliminary data marked
- **Updates**: Continuous; new data available daily

**Geographic Coverage**

Three stations in Texas:
- **Wise County**: Big Sandy Creek drainage basin (North Texas)
- **Uvalde County**: Nueces River basin (South Texas)
- Coverage of diverse water infrastructure and climatic zones

**Time Period**

- Project data collection: January 1, 2022 - December 31, 2024
- Extended historical data available from USGS back to station installation dates
- Real-time updates: Ongoing

**Website**

[https://waterservices.usgs.gov/](https://waterservices.usgs.gov/)

**API Access**

USGS provides a public REST API for programmatic data access:

```
https://waterservices.usgs.gov/nwis/iv/?sites=08046500&format=json&parameterCd=00060&startDT=2022-01-01
```

**Parameters**:
- `sites`: USGS site codes (comma-separated)
- `parameterCd`: USGS parameter codes (00060=streamflow, 00065=gage height)
- `startDT`/`endDT`: Date range ISO format
- `format`: json or waterml

**License and Attribution**

- **License**: Public domain
- **Attribution Required**: Recommended (not required by law)
- **Proper Citation**:
  ```
  U.S. Geological Survey. (2024). NWIS Water Services.
  Retrieved from https://waterservices.usgs.gov/
  ```
- **No Copyright Restrictions**: Data is public domain, freely usable

**Data Access**

Files are located in:
- Project repository: `data/raw/usgs/`
- Windows path: `C:\Users\Arath\Documents\Datathon\data\raw\usgs\`
- Mac path: `/Volumes/Arath/Automation_Station/Projects/Datathon/data/raw/usgs/`

**Last Update**

Access Date: [Update with actual access date]
Refresh Schedule: Daily (automatic API integration)

---

## Secondary Data Sources

The following agencies and institutions provide supplementary data and context:

### Texas Parks and Wildlife Department (TPWD)

- **Data**: Fish species, aquatic ecosystem data
- **Website**: https://tpwd.texas.gov/
- **Relevance**: Ecological impact of water management decisions

### Texas Commission on Environmental Quality (TCEQ)

- **Data**: Water quality standards, pollution data, environmental regulations
- **Website**: https://www.tceq.texas.gov/
- **Relevance**: Water quality constraints on infrastructure planning

### UT Water Resources Center

- **Data**: Research findings, hydrological studies
- **Website**: https://www.waterresources.utexas.edu/
- **Relevance**: Academic research and methodology validation

---

## Data Integration Methodology

### Processing Pipeline

```
Raw Data
    ↓
Data Cleaning (handling missing values, outliers)
    ↓
Data Validation (schema checks, range validation)
    ↓
Data Transformation (unit conversion, aggregation)
    ↓
Data Integration (cross-source joining)
    ↓
Processed Data (analysis-ready)
```

### Quality Assurance Steps

1. **Schema Validation**
   - Verify column names and data types
   - Check for required fields
   - Validate field formats (dates, numbers)

2. **Range Validation**
   - Confirm data values within expected ranges
   - Flag outliers for manual review
   - Document any removed data points

3. **Temporal Validation**
   - Verify chronological order
   - Identify data gaps
   - Confirm date format consistency

4. **Geographic Validation**
   - Verify region codes match TWDB standards
   - Check station coordinates
   - Validate county-region relationships

5. **Cross-source Validation**
   - Verify consistency between overlapping datasets
   - Reconcile units and measurement methodologies
   - Document any discrepancies

### Data Integration Points

**TWDB + USGS Integration**

- Spatial join: USGS stations matched to TWDB regions by geography
- Temporal join: Align USGS 15-minute data with TWDB annual data
- Conceptual join: Link streamflow measurements to water demand/supply planning

**Example**: USGS Big Sandy Creek streamflow data correlates with TWDB Region A municipal water demand to assess infrastructure reliability.

---

## Access Date Log

| Source | Dataset | Access Date | Version | Notes |
|--------|---------|-------------|---------|-------|
| TWDB | State Water Plan 2026 | [Date] | 2026 | Initial download |
| USGS | Big Sandy Creek (08046500) | [Date] | Current | API integration setup |
| USGS | Bridgeport Reservoir (08046550) | [Date] | Current | Continuous updates |
| USGS | Nueces River (08210000) | [Date] | Current | Continuous updates |

---

## Licensing Summary

### Data Licensing Matrix

| Source | License Type | Attribution | Commercial Use | Modification | Distribution |
|--------|-------------|-------------|-----------------|---------------|--------------|
| TWDB | Public Domain | Required | Allowed | Allowed | Allowed |
| USGS | Public Domain | Recommended | Allowed | Allowed | Allowed |
| TPWD | Public Domain | Required | Allowed | Allowed | Allowed |
| TCEQ | Public Domain | Required | Allowed | Allowed | Allowed |
| UT WRC | Varies | Required | Varies | Varies | Varies |

### Project Licensing

This project itself is licensed under the MIT License. Data from TWDB and USGS retains its public domain status regardless of project licensing.

**Project Use Guidelines**:
- Data may be used for any purpose (research, commercial, educational)
- Attribution to original sources is required
- This project's code is MIT licensed; data remains public domain
- Combined products (dashboards, visualizations, reports) should cite sources

---

## Data Access Instructions

### For Project Developers

1. **Clone repository and access raw data**:
   ```bash
   git clone https://github.com/yourusername/datathon-water-analysis.git
   cd datathon-water-analysis
   ls data/raw/
   ```

2. **Load TWDB data**:
   ```python
   import pandas as pd
   demands = pd.read_csv('data/raw/twdb/demands.csv')
   ```

3. **Load USGS data**:
   ```python
   import pandas as pd
   streamflow = pd.read_csv('data/raw/usgs/big_sandy_creek_streamflow.csv')
   ```

### For External Researchers

**TWDB Data Access**:
- Website: https://texasstatewaterplan.org/
- Download individual datasets
- No registration required
- Attribution required in publications

**USGS Data Access**:
- Website: https://waterservices.usgs.gov/
- Query by site ID or location
- API available for programmatic access
- Real-time and historical data

**This Project's Data**:
- GitHub repository: `data/raw/` directory
- Processed data available on request
- Documentation included in repository

---

## Citation Examples

### For Academic Publications

APA Format:
```
Texas Department of Biological Resources. (2024). State water plan 2026 [Data set].
Retrieved from https://texasstatewaterplan.org/

U.S. Geological Survey. (2024). NWIS water services [Data set].
Retrieved from https://waterservices.usgs.gov/
```

Chicago Format:
```
Texas Department of Biological Resources. "State Water Plan 2026."
Accessed [Access Date]. https://texasstatewaterplan.org/.

U.S. Geological Survey. "NWIS Water Services."
Accessed [Access Date]. https://waterservices.usgs.gov/.
```

### For Web/Dashboard Attribution

```
Data sources: Texas Department of Biological Resources (TWDB) State Water Plan 2026
and U.S. Geological Survey Water Services. Public domain data.
```

---

## Data Updates and Maintenance

### Update Schedule

- **TWDB Data**: Annual update (typically Q1, fiscal year basis)
- **USGS Real-time Data**: Continuous (daily new data)
- **USGS Historical Data**: Updated as data is quality-assured
- **Project Repository**: Updated upon source data release

### Version Control

All data versions are tracked in project repository:
```
data/
├── raw/
│   ├── twdb/
│   │   ├── demands_2024-12-15.csv
│   │   └── demands_latest.csv
│   └── usgs/
│       └── streamflow_continuous.csv
└── processed/
    └── integrated_dataset.csv
```

---

## Questions About Sources?

For questions about data sources, access, or attribution:

1. **Check this document** for detailed information
2. **Contact data providers**:
   - TWDB: https://texasstatewaterplan.org/contact
   - USGS: https://waterservices.usgs.gov/
3. **Open an issue** on project GitHub
4. **Email project maintainers** for attribution questions

---

**Document Version**: 1.0
**Last Updated**: [Date]
**Next Review**: [Date + 6 months]
