# Contributing to datathon-water-analysis

Thank you for your interest in contributing to our water analysis research project! We welcome contributions from developers, researchers, data scientists, and water resource professionals. This document outlines how to contribute effectively.

## How to Contribute

There are many ways to contribute to this project:

1. **Code Contributions** - Bug fixes, features, optimizations
2. **Data Contributions** - New datasets, data processing scripts, validation
3. **Documentation** - Improve existing docs, add tutorials, clarify procedures
4. **Visualization** - Create new charts, dashboards, or design improvements
5. **Research** - Analysis, forecasting models, methodology improvements
6. **Testing** - Unit tests, integration tests, quality assurance

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Clone your fork locally
git clone https://github.com/yourusername/datathon-water-analysis.git
cd datathon-water-analysis

# Add upstream remote
git remote add upstream https://github.com/original-owner/datathon-water-analysis.git
```

### 2. Create a Development Branch

Follow our branch naming conventions (see below):

```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes and Test

- Write clean, well-documented code
- Follow code style guidelines (see below)
- Add tests for new functionality
- Update documentation as needed

### 4. Commit and Push

Follow our commit message standards (see below):

```bash
git add .
git commit -m "feat: add new water demand visualization"
git push origin feature/your-feature-name
```

### 5. Create a Pull Request

- Create PR against the `main` branch
- Include clear description of changes
- Reference any related issues
- Wait for review and address feedback

## Branch Naming Conventions

Use descriptive branch names with appropriate prefixes:

### Feature Branches
```
feature/water-demand-forecast
feature/twdb-data-integration
feature/interactive-map
```

### Bug Fixes
```
bugfix/fix-streamflow-calculation
bugfix/correct-region-boundaries
bugfix/export-csv-encoding
```

### Documentation
```
docs/add-installation-guide
docs/update-api-reference
docs/contribution-guidelines
```

### Data Work
```
data/add-usgs-stations
data/clean-population-data
data/validate-source-attribution
```

### Other
```
refactor/optimize-data-pipeline
chore/update-dependencies
hotfix/critical-visualization-bug
```

## Commit Message Standards

Use clear, descriptive commit messages following this format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring without feature changes
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Maintenance tasks, dependency updates
- `data`: Data processing or dataset changes

### Scope
Specify the area affected: `(data)`, `(visualization)`, `(forecast)`, `(dashboard)`, etc.

### Subject
- Use imperative mood ("add" not "added" or "adds")
- Don't capitalize first letter
- No period at the end
- Limit to 50 characters

### Examples

```
feat(visualization): add interactive water demand chart

Implement new Plotly chart for visualizing water demand by sector
and region. Includes real-time filtering and hover tooltips.

Closes #123
```

```
fix(data): correct population calculation for West Texas

Fixed off-by-one error in population projection calculation
affecting 2024 West Texas forecasts.

Fixes #456
```

```
docs(readme): add Windows installation instructions

Added detailed step-by-step installation guide for Windows users
with common troubleshooting tips.
```

## Pull Request Process

### Before Submitting

1. **Sync with upstream**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run tests**
   ```bash
   pytest tests/
   ```

3. **Check code style**
   ```bash
   black src/
   flake8 src/
   ```

4. **Update documentation**
   - Update README if needed
   - Add docstrings to new functions
   - Update SOURCES.md if adding data sources

### PR Template

When creating a PR, use this template:

```markdown
## Description
Brief description of changes

## Related Issues
Closes #123

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Data addition
- [ ] Breaking change

## Testing
Describe testing performed:
- [ ] Unit tests added/updated
- [ ] Integration tests passed
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No new warnings generated
- [ ] SOURCES.md updated (if data related)
```

## Code Style Guidelines

### Python Code

We follow PEP 8 with these tools:

1. **Black** - Code formatting
   ```bash
   black src/
   ```

2. **Flake8** - Linting
   ```bash
   flake8 src/ --max-line-length=100
   ```

3. **isort** - Import sorting
   ```bash
   isort src/
   ```

### Style Rules

```python
# Good: Clear variable names, type hints
def calculate_water_demand(
    region: str,
    year: int,
    sector: str = "all"
) -> float:
    """Calculate water demand for specified region and year.

    Args:
        region: TWDB planning region name
        year: Year for which to calculate demand
        sector: Water use sector ('municipal', 'agricultural', 'industrial', 'all')

    Returns:
        Water demand in acre-feet per year
    """
    pass

# Bad: Unclear naming, no documentation
def calc_demand(r, y, s="all"):
    pass
```

### Docstring Format

Use Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> dict:
    """Brief one-line description.

    More detailed explanation if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When invalid parameters provided

    Example:
        >>> result = function_name("Texas", 2024)
        >>> result['demand']
        1500000
    """
    pass
```

## Testing Requirements

### Unit Tests

Write tests for all new functions:

```python
import pytest
from src.data_processing import calculate_water_demand

def test_calculate_water_demand_valid_inputs():
    result = calculate_water_demand("Region A", 2024, "municipal")
    assert isinstance(result, float)
    assert result > 0

def test_calculate_water_demand_invalid_region():
    with pytest.raises(ValueError):
        calculate_water_demand("Invalid Region", 2024)
```

### Test Coverage

- Maintain minimum 80% code coverage
- Run coverage report:
  ```bash
  pytest --cov=src tests/
  ```

### Integration Tests

Test interactions between modules:

```python
def test_data_processing_pipeline():
    # Test full pipeline from raw data to processed output
    raw_data = load_raw_twdb_data()
    processed = process_twdb_data(raw_data)
    assert len(processed) == len(raw_data)
    assert all(validate_processed_data(row) for row in processed)
```

## Documentation Requirements

### For New Features

1. **Code Comments** - Explain complex logic
2. **Docstrings** - Document all functions and classes
3. **README Updates** - Add feature to overview if significant
4. **SOURCES.md Updates** - Document any new data sources
5. **Examples** - Provide usage examples for public functions

### For Data Contributions

1. **Data Schema** - Document field names and types
2. **Source Attribution** - Update SOURCES.md with full details
3. **Validation** - Include data quality checks
4. **Metadata** - Add collection date, update frequency, geographic coverage

## Contribution Types

### Code Contributions

- Bug fixes
- Performance optimizations
- New analysis functions
- Dashboard enhancements
- Infrastructure improvements

**Requirements**:
- Tests required
- Code review required
- Documentation required

### Data Contributions

- New datasets from sources
- Data cleaning scripts
- Validation procedures
- Integration pipelines

**Requirements**:
- Complete SOURCES.md entry
- Data validation tests
- Documentation of processing steps
- Attribution and licensing confirmation

### Documentation Contributions

- Tutorials
- API documentation
- Data guides
- Installation instructions
- FAQ additions

**Requirements**:
- Clear, accessible writing
- Proper markdown formatting
- Examples where appropriate
- Reviewed by maintainers

### Visualization Contributions

- New chart types
- Dashboard improvements
- Interactive features
- Design enhancements

**Requirements**:
- Code for chart generation
- Documentation of usage
- Performance optimized
- Responsive design

### Research Contributions

- New forecasting models
- Analysis methodologies
- Findings and insights
- Recommendations

**Requirements**:
- Documented methodology
- Results with confidence intervals
- Reproducible code
- Peer review encouraged

## Code Review Process

All submissions undergo review:

1. **Automated Checks**
   - Tests must pass
   - Code coverage maintained
   - Style checks pass

2. **Maintainer Review**
   - Code quality assessment
   - Alignment with project goals
   - Documentation completeness
   - Testing adequacy

3. **Feedback and Iteration**
   - Address reviewer comments
   - Push follow-up commits to same branch
   - No force-push after review started

## Community Guidelines

We are committed to providing a welcoming and inclusive community:

- Be respectful to all contributors
- Welcome diverse perspectives
- Focus on the code, not the person
- Help others learn and grow
- Report inappropriate behavior to maintainers

## Questions?

- Check existing issues and discussions
- Review SOURCES.md for data questions
- Open a new issue for technical questions
- Email maintainers for urgent matters

## Recognition

Contributors are recognized in:
- README.md contributors section
- Release notes for significant contributions
- Project acknowledgments

Thank you for contributing to datathon-water-analysis!
