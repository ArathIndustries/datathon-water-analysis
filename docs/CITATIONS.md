# Citations and References Guide

## Overview

This document provides comprehensive citation formats and examples for referencing data sources, analytical tools, and research materials used in the Texas Water Dashboard Datathon project. Use the format most appropriate for your publication venue, discipline, or institutional requirements.

---

## Citation Format Examples

### 1. APA Format (7th Edition)

APA format emphasizes author, date of publication, and is commonly used in social sciences, psychology, education, and business.

#### Template:
```
Author, A. A., & Author, B. B. (Year). Title of work. Publisher/Source.
```

#### Examples:

**TWDB State Water Plan 2026**
```
Texas Water Development Board. (2026). State water plan: 2026 update.
    Texas Water Development Board.
    https://www.twdb.texas.gov/
```

**USGS Water Services API**
```
U.S. Geological Survey. (2024). Water services: Real-time data.
    National Water Information System (NWIS)
    [Database]. U.S. Department of the Interior.
    https://waterservices.usgs.gov/
```

**This Project (Texas Water Dashboard)**
```
[Author/Team Name]. (2025). Texas water dashboard: Data center viability
    analysis [Interactive web application].
    Datathon 2025 Repository.
    Retrieved from [Project Repository URL]
```

**Example Academic Reference**
```
Scanlon, B. R., Faunt, C. C., Longuevergne, L., Reedy, R. C.,
    Alley, W. M., McGuire, V. L., & McMahon, P. B. (2012). Groundwater
    depletion and sustainability of irrigation in the US high plains and
    central valley. Proceedings of the National Academy of Sciences, 109(24),
    9320–9325. https://doi.org/10.1073/pnas.1200311109
```

---

### 2. Chicago Style (Notes and Bibliography)

Chicago style is traditionally used in history and some humanities disciplines. Provides two options: Notes and Bibliography, or Author-Date.

#### Notes Format:

**Template:**
```
Author First Name Last Name, Title of Work (Publisher: Place of Publication, Year), page number(s).
```

**Examples:**

**TWDB State Water Plan 2026 (First Reference)**
```
1. Texas Water Development Board, State Water Plan: 2026 Update
   (Austin: Texas Water Development Board, 2026), https://www.twdb.texas.gov/.
```

**TWDB State Water Plan 2026 (Subsequent Reference)**
```
2. TWDB, State Water Plan 2026 Update.
```

**USGS Water Services API (First Reference)**
```
3. U.S. Geological Survey, Water Services: Real-Time Data,
   National Water Information System (NWIS) (U.S. Department of the Interior, 2024),
   https://waterservices.usgs.gov/.
```

**This Project (First Reference)**
```
4. [Author/Team Name], "Texas Water Dashboard: Data Center Viability Analysis,"
   Datathon 2025 Repository (2025), [Project URL].
```

**Example Academic Reference (First Reference)**
```
5. Brian R. Scanlon, Claudia C. Faunt, Laurent Longuevergne, et al.,
   "Groundwater Depletion and Sustainability of Irrigation in the US High
   Plains and Central Valley," Proceedings of the National Academy of Sciences 109,
   no. 24 (2012): 9320–9325, https://doi.org/10.1073/pnas.1200311109.
```

#### Bibliography Format:

**Template:**
```
Last Name, First Name. Title of Work. Publisher, Place of Publication, Year.
```

**Examples:**

```
Texas Water Development Board. State Water Plan: 2026 Update.
    Austin: Texas Water Development Board, 2026.
    https://www.twdb.texas.gov/.

U.S. Geological Survey. Water Services: Real-Time Data.
    National Water Information System (NWIS).
    U.S. Department of the Interior, 2024.
    https://waterservices.usgs.gov/.

[Author/Team Name]. "Texas Water Dashboard: Data Center Viability Analysis."
    Datathon 2025 Repository, 2025. [Project URL].

Scanlon, Brian R., Claudia C. Faunt, Laurent Longuevergne, Rachel C. Reedy,
    William M. Alley, Victor L. McGuire, and Patrick B. McMahon.
    "Groundwater Depletion and Sustainability of Irrigation in the US High
    Plains and Central Valley." Proceedings of the National Academy of Sciences
    109, no. 24 (2012): 9320–9325.
    https://doi.org/10.1073/pnas.1200311109.
```

---

### 3. MLA Format (9th Edition)

MLA is commonly used in humanities, literature, and composition courses.

#### Template:
```
Author. "Title of Work." Website/Publisher, Date, URL.
```

#### Examples:

**TWDB State Water Plan 2026**
```
Texas Water Development Board. "State Water Plan: 2026 Update."
    Texas Water Development Board, 2026, www.twdb.texas.gov/.
```

**USGS Water Services API**
```
U.S. Geological Survey. "Water Services: Real-Time Data."
    National Water Information System (NWIS), U.S. Department of the Interior,
    2024, waterservices.usgs.gov/.
```

**This Project (Texas Water Dashboard)**
```
[Author/Team Name]. "Texas Water Dashboard: Data Center Viability Analysis."
    Datathon 2025 Repository, 2025, [Project Repository URL].
```

**Example Academic Reference**
```
Scanlon, Brian R., et al. "Groundwater Depletion and Sustainability of
    Irrigation in the US High Plains and Central Valley."
    Proceedings of the National Academy of Sciences, vol. 109, no. 24, 2012,
    pp. 9320–9325, doi:10.1073/pnas.1200311109.
```

---

### 4. BibTeX Format

BibTeX is used with LaTeX document preparation systems, common in STEM fields.

#### Examples:

**TWDB State Water Plan 2026**
```bibtex
@report{TWDB2026,
  author = {Texas Water Development Board},
  title = {State Water Plan: 2026 Update},
  organization = {Texas Water Development Board},
  year = {2026},
  url = {https://www.twdb.texas.gov/},
  note = {Accessed: February 8, 2025}
}
```

**USGS Water Services API**
```bibtex
@dataset{USGS2024,
  author = {{U.S. Geological Survey}},
  title = {Water Services: Real-Time Data},
  organization = {National Water Information System (NWIS)},
  url = {https://waterservices.usgs.gov/},
  year = {2024},
  note = {Accessed: February 8, 2025}
}
```

**This Project (Texas Water Dashboard)**
```bibtex
@software{WaterDashboard2025,
  author = {[Author/Team Name]},
  title = {Texas Water Dashboard: Data Center Viability Analysis},
  year = {2025},
  url = {[Project Repository URL]},
  note = {Datathon 2025 Project}
}
```

**Example Academic Reference**
```bibtex
@article{Scanlon2012,
  author = {Scanlon, Brian R. and Faunt, Claudia C. and Longuevergne, Laurent
            and Reedy, Rachel C. and Alley, William M. and McGuire, Victor L.
            and McMahon, Patrick B.},
  title = {Groundwater Depletion and Sustainability of Irrigation in the {US}
           High Plains and Central Valley},
  journal = {Proceedings of the National Academy of Sciences},
  year = {2012},
  volume = {109},
  number = {24},
  pages = {9320--9325},
  doi = {10.1073/pnas.1200311109}
}
```

---

### 5. Harvard Format

Harvard is widely used in UK universities and social sciences.

#### Template:
```
Author(s) surname, initials. (Year) 'Title of work', Publisher/Source.
Available at: URL (Accessed: date).
```

#### Examples:

**TWDB State Water Plan 2026**
```
Texas Water Development Board (2026) 'State water plan: 2026 update'.
    Available at: https://www.twdb.texas.gov/ (Accessed: 8 February 2025).
```

**USGS Water Services API**
```
U.S. Geological Survey (2024) 'Water services: Real-time data'.
    National Water Information System (NWIS), U.S. Department of the Interior.
    Available at: https://waterservices.usgs.gov/ (Accessed: 8 February 2025).
```

**This Project (Texas Water Dashboard)**
```
[Author/Team Name] (2025) 'Texas water dashboard: Data center viability analysis'.
    Datathon 2025 Repository. Available at: [Project Repository URL]
    (Accessed: 8 February 2025).
```

**Example Academic Reference**
```
Scanlon, B.R., Faunt, C.C., Longuevergne, L., Reedy, R.C., Alley, W.M.,
    McGuire, V.L. and McMahon, P.B. (2012) 'Groundwater depletion and
    sustainability of irrigation in the US high plains and central valley',
    Proceedings of the National Academy of Sciences, 109(24), pp. 9320–9325.
    doi: 10.1073/pnas.1200311109.
```

---

## In-Context Citation Examples

### Example 1: Data Integration Statement (APA)

```
This analysis integrates two primary data sources. The Texas Water Development
Board's State Water Plan 2026 (Texas Water Development Board, 2026) provides
historical water use and availability data spanning 1975–2024 across 16 planning
regions. Current monitoring data (U.S. Geological Survey, 2024) from more than
200 stream gauges and groundwater stations are accessed via the Water Services
API, providing near-real-time stream flow and aquifer level measurements.
```

### Example 2: Data Integration Statement (Chicago Notes)

```
This analysis integrates two primary data sources. The Texas Water Development
Board's State Water Plan 2026¹ provides historical water use and availability
data spanning 1975–2024 across 16 planning regions. Current monitoring data²
from more than 200 stream gauges and groundwater stations are accessed via the
Water Services API, providing near-real-time stream flow and aquifer level
measurements.

1. Texas Water Development Board, State Water Plan: 2026 Update
   (Austin: Texas Water Development Board, 2026), https://www.twdb.texas.gov/.
2. U.S. Geological Survey, Water Services: Real-Time Data,
   National Water Information System (NWIS) (U.S. Department of the Interior, 2024),
   https://waterservices.usgs.gov/.
```

### Example 3: Methodology Citation (APA)

```
Trend analysis follows established methods in hydrological forecasting (Scanlon
et al., 2012). ARIMA models are applied to decompose historical time series into
trend, seasonal, and residual components, enabling probabilistic forecasting of
future availability scenarios. Regional comparisons employ stratified analysis
techniques to account for hydrographic variations across the Texas Water
Development Board's 16 planning regions.
```

### Example 4: Findings Citation (MLA)

```
Historical data from the Texas Water Development Board (2026) demonstrates
accelerating groundwater depletion in the Panhandle region, with annual usage
exceeding recharge rates by an average of 2.3 million acre-feet. USGS monitoring
stations (U.S. Geological Survey, 2024) in the Ogallala Aquifer document water
table declines of 0.5–1.5 feet per year in high-use areas, consistent with
previous findings on irrigation impacts (Scanlon et al., 2012).
```

### Example 5: Dashboard Reference (Harvard)

```
The interactive analysis platform developed for this project (Texas Water
Dashboard, 2025) enables users to explore temporal trends, regional variations,
and scenario comparisons across data sources. The application integrates both
historical (1975–2024) and current (2022–2024) measurements, with data validation
performed according to USGS quality assurance standards.
```

### Example 6: Stakeholder Communication (APA)

```
Water availability projections for major metropolitan regions are informed by
Texas Water Development Board (2026) demand forecasts and USGS (2024)
hydrological observations. The analysis accounts for competing water demands
across agricultural, municipal, and industrial sectors, as detailed in the State
Water Plan's multi-sector accounting framework. Regional risk stratification
employs probability thresholds derived from historical exceedance analysis and
expert elicitation methods.
```

### Example 7: Comparative Analysis (Chicago Bibliography)

```
Multiple studies have examined water constraints on industrial development.
Scanlon et al.'s (2012) comprehensive assessment of groundwater depletion in
the High Plains identified accelerating resource stress in regions targeted for
data center development. The Texas Water Development Board (2026) projects
continued pressure on both surface and groundwater resources, with particular
challenges anticipated in the Panhandle and Trans-Pecos regions. Current
monitoring by the USGS (2024) confirms ongoing depletion trends, providing
empirical validation of these projections.
```

---

## Quick Reference Table

| Format | Discipline | Best For |
|--------|-----------|----------|
| APA | Social Sciences, Psychology, Education, Business | Most academic and professional contexts |
| Chicago | History, Humanities, Some Interdisciplinary | Books, longer publications, notes-heavy work |
| MLA | Literature, Humanities, Composition | Humanities papers, high school/college essays |
| BibTeX | Physics, Engineering, Computer Science, Math | LaTeX documents, technical papers |
| Harvard | UK Universities, Social Sciences | Business, management, some sciences |

---

## DOI and URL Formatting

### Digital Object Identifiers (DOIs)

When available, DOIs should be included in citations:

**APA with DOI:**
```
Scanlon, B. R., Faunt, C. C., Longuevergne, L., Reedy, R. C., Alley, W. M.,
McGuire, V. L., & McMahon, P. B. (2012). Groundwater depletion and
sustainability of irrigation in the US high plains and central valley.
Proceedings of the National Academy of Sciences, 109(24), 9320–9325.
https://doi.org/10.1073/pnas.1200311109
```

### Direct URLs

For web resources without DOIs:

**APA with URL:**
```
Texas Water Development Board. (2026). State water plan: 2026 update.
Retrieved from https://www.twdb.texas.gov/
```

---

## Data Accessibility Statements

Include statements acknowledging data accessibility:

```
Data Accessibility: Historical water use and availability data are publicly
available through the Texas Water Development Board's website (https://www.twdb.texas.gov/).
Real-time hydrological observations are accessible via the USGS Water Services API
(https://waterservices.usgs.gov/). All integrated and processed datasets used in
this analysis are available in the project repository [URL].
```

---

## Recommended Additional References

### Texas Water Policy and Planning
- Texas Water Development Board. (2026). State Water Plan 2026.
- Texas Parks and Wildlife Department. (2023). Environmental flow standards.
- Texas Commission on Environmental Quality. (2024). Water rights and allocation policies.

### Water-Energy Nexus and Data Centers
- Scanlon, B. R., et al. (2012). Groundwater depletion and sustainability of irrigation.
- Sharma, T. C., et al. (2023). Water requirements for data center sustainability.
- U.S. Environmental Protection Agency. (2024). Data center water efficiency guidelines.

### Hydrological Methods and Forecasting
- Box, G. E. P., Jenkins, G. M., & Reinsel, G. C. (2015). Time series analysis.
- Hyndman, R. J., & Athanasopoulos, G. (2021). Forecasting: principles and practice.

### Climate and Drought Analysis
- Milly, P. C. D., et al. (2008). Climate change and water resources.
- Seager, R., et al. (2007). Model projections of an imminent transition to a more arid climate in southwestern North America.

---

## Notes for Citation Management

### Using Citation Managers

Popular citation management tools that support all formats above:
- **Zotero** (free, open-source): https://www.zotero.org/
- **Mendeley** (free with limitations): https://www.mendeley.com/
- **EndNote** (subscription): https://endnote.com/
- **BibTeX managers**: JabRef (free), BibTeX Editor

### Best Practices

1. **Consistency**: Use the same format throughout your document
2. **Completeness**: Include all available information (author, date, title, source, URL, access date)
3. **Accessibility**: Provide direct links to data sources when possible
4. **Transparency**: Note the access date for web resources
5. **Verification**: Double-check citations against original sources
6. **Attribution**: Always credit original data creators and analysts

---

**Document Version**: 1.0
**Last Updated**: February 8, 2025
**Project**: Texas Water Dashboard Datathon
**Prepared For**: Research Documentation Standards
