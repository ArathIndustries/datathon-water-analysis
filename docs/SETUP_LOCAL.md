# Local Development Setup Guide

Complete instructions for setting up the Texas Water Crisis Dashboard for local development, including Windows-specific commands and multiple execution methods.

---

## System Prerequisites

### Required Software

**Node.js & npm**
- Version: Node.js 16+ (recommended 18 LTS or newer)
- Download: https://nodejs.org/
- Check version:
  ```bash
  node --version
  npm --version
  ```

**Git**
- Version: 2.30+
- Download: https://git-scm.com/
- Needed for: Version control, cloning repository
- Check version:
  ```bash
  git --version
  ```

**Code Editor**
- Recommended: Visual Studio Code (free)
- Download: https://code.visualstudio.com/
- Alternative: Sublime Text, Atom, WebStorm

**Python 3 (Optional - for Streamlit dashboard)**
- Version: 3.8+
- Download: https://www.python.org/
- Used for: Interactive analytics dashboard
- Check version:
  ```bash
  python --version
  ```

### Optional Tools

**Git Bash (Windows)**
- Provides Unix-like terminal on Windows
- Included with Git installation
- Better terminal experience than CMD

**PowerShell**
- Windows 10/11 default terminal
- Supports most Unix commands
- Recommended over Command Prompt

**VS Code Extensions (Optional)**
- "Live Server" - Local HTTP server in VS Code
- "Python" - Python language support
- "Prettier" - Code formatter
- "ESLint" - JavaScript linting

---

## Repository Setup

### Step 1: Clone the Repository

**Windows PowerShell or Git Bash**:
```powershell
# Navigate to your projects directory
cd C:\Users\YourName\Documents\Projects

# Clone the repository
git clone https://github.com/username/datathon-water-analysis.git

# Enter the project directory
cd datathon-water-analysis
```

**macOS/Linux Terminal**:
```bash
cd ~/Projects
git clone https://github.com/username/datathon-water-analysis.git
cd datathon-water-analysis
```

### Step 2: Verify Clone Structure

```powershell
# Windows: List project files
dir

# Or in PowerShell (all platforms):
ls -la
```

Expected output:
```
index.html
package.json
README.md
vercel.json
.gitignore
docs/
  ├── ARCHITECTURE.md
  ├── SETUP_LOCAL.md
  └── PUBLIC_README.md
```

### Step 3: Install Node Dependencies

```powershell
# Windows PowerShell or Git Bash
npm install

# Output should show:
# npm warn (ignored warnings are okay)
# added X packages in Y.Z seconds
```

This installs `http-server` for local development.

---

## Folder Structure Explanation

### Project Root Structure

```
datathon-water-analysis/
│
├── index.html                    # Main dashboard (all-in-one file)
│   ├── HTML structure            # Semantic markup, forms, containers
│   ├── CSS styling               # Responsive layout, theming
│   └── JavaScript logic          # Data loading, filtering, charts
│
├── package.json                  # Project metadata & npm scripts
│   ├── "dev" script             # Start development server
│   ├── "build" script           # Build static assets
│   └── Dependencies section     # External libraries (loaded via CDN)
│
├── vercel.json                   # Vercel deployment config
│   └── Configures production hosting
│
├── README.md                     # Quick reference documentation
│
├── docs/                         # Documentation folder
│   ├── ARCHITECTURE.md          # System design (read first for understanding)
│   ├── SETUP_LOCAL.md           # This file - development setup
│   └── PUBLIC_README.md         # User guide for frontend features
│
├── data/                         # CSV data files (created at runtime)
│   ├── demands.csv              # Water demand projections
│   ├── existing.csv             # Existing infrastructure
│   ├── needs.csv                # Future needs
│   ├── population.csv           # Population projections
│   └── strategies.csv           # Management strategies
│
└── .gitignore                    # Git ignore patterns
```

### Why This Structure?

**Single HTML File Design**:
- **Advantage**: Deploy as single file, no build step needed
- **Simplicity**: No need for webpack, Babel, or build tools
- **Performance**: Direct browser loading, no transpilation overhead
- **Portability**: Works offline, easy to share

**CDN Dependencies**:
- **External Loading**: JavaScript libraries loaded from CDN in HTML
- **Caching**: Browser caches libraries (faster repeat loads)
- **Maintenance**: Update library versions by changing CDN URL
- **No npm install needed**: Libraries already available via CDN

**Data Folder**:
- **Created at runtime**: Folder structure expects data files
- **Served locally**: Python or Node.js server needed to load CSV files
- **Simulated data**: For development, use sample CSV files

---

## Execution Methods

### Method 1: Static HTTP Server (Recommended for Most Users)

#### On Windows (PowerShell)

**Step 1: Navigate to project directory**
```powershell
cd C:\Users\YourName\Documents\Projects\datathon-water-analysis
```

**Step 2: Start HTTP server**
```powershell
npm run dev
```

Or manually:
```powershell
npx http-server . -p 3000 --cors
```

**Step 3: Open dashboard**
- Open browser: http://localhost:3000
- Dashboard loads: http://localhost:3000/index.html

**Output in terminal**:
```
Starting up http-server, serving .
Hit CTRL-C to stop the server
http-server version 14.1.1

http://192.168.1.100:3000

Press CTRL-C to stop the server
```

**Stop the server**:
```powershell
# Press CTRL+C in the terminal
# You'll see: ^C
```

#### On macOS/Linux (Terminal)

```bash
# Same commands work
cd ~/Projects/datathon-water-analysis
npm run dev

# Or manually
npx http-server . -p 3000 --cors
```

**Benefits of This Method**:
- ✓ Simple single command
- ✓ Handles CORS for loading CSV files
- ✓ Automatic MIME type detection
- ✓ Hot reload when files change (with VS Code Live Server)
- ✓ Works on macOS, Linux, Windows

### Method 2: Python HTTP Server

#### Windows PowerShell

**Python 3**:
```powershell
# Navigate to project
cd C:\Users\YourName\Documents\Projects\datathon-water-analysis

# Start server on port 8000
python -m http.server 8000

# Or specify a different port
python -m http.server 3000
```

**Open dashboard**: http://localhost:3000

**Stop server**: CTRL+C

#### macOS/Linux Terminal

```bash
cd ~/Projects/datathon-water-analysis

# Python 3 (default on modern systems)
python -m http.server 8000

# Or if you need Python 3 explicitly
python3 -m http.server 8000
```

**Benefits of This Method**:
- ✓ No npm install needed
- ✓ Python available on most systems
- ✓ Minimal dependencies
- ✓ Good for testing CORS behavior

**Drawbacks**:
- ✗ Doesn't automatically reload files
- ✗ Less features than http-server

### Method 3: Streamlit Interactive Dashboard (Data Analysis Focus)

Uses Python backend for advanced analytics alongside the HTML dashboard.

#### Windows PowerShell Setup

**Step 1: Create virtual environment**
```powershell
# Navigate to project
cd C:\Users\YourName\Documents\Projects\datathon-water-analysis

# Create virtual environment
python -m venv venv

# Activate virtual environment
# IMPORTANT: Run from PowerShell, not Command Prompt
.\venv\Scripts\Activate.ps1

# You should see: (venv) in prompt like:
# (venv) PS C:\Users\...>
```

**If you get an execution policy error**:
```powershell
# Allow running scripts in PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try again:
.\venv\Scripts\Activate.ps1
```

**Step 2: Install Python dependencies**
```powershell
# With venv activated (you should see (venv) in prompt)
pip install streamlit pandas plotly numpy

# Verify installation
pip list
```

**Step 3: Copy Streamlit app**

Create file: `C:\Users\YourName\Documents\Projects\datathon-water-analysis\streamlit_app.py`

Copy from: `/Volumes/Arath/Automation_Station/Projects/Datathon/analysis/04_interactive_dashboard.py`

Or minimal example:
```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Water Dashboard", page_icon="💧", layout="wide")

st.title("Texas Water Crisis Analysis")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/demands.csv')
    return df

try:
    df = load_data()
    st.metric("Total Records", len(df))
    st.dataframe(df.head(20))
except Exception as e:
    st.error(f"Could not load data: {e}")
```

**Step 4: Run Streamlit**
```powershell
# Make sure venv is activated
streamlit run streamlit_app.py
```

**Expected output**:
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
Network URL: http://192.168.1.100:8501
```

**Step 5: Open browser**
- Navigate to: http://localhost:8501
- Streamlit app loads with hot reload enabled
- Changes to Python files auto-refresh

**Stop Streamlit**: CTRL+C in terminal

**Deactivate venv** (when done):
```powershell
deactivate
```

#### macOS/Linux Terminal Setup

```bash
# Navigate to project
cd ~/Projects/datathon-water-analysis

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install streamlit pandas plotly numpy

# Create streamlit_app.py (same Python code as above)

# Run Streamlit
streamlit run streamlit_app.py

# Stop: CTRL+C
# Deactivate venv: deactivate
```

**Benefits of This Method**:
- ✓ Interactive data exploration
- ✓ Real-time code changes (hot reload)
- ✓ Advanced data visualization
- ✓ Perfect for exploratory analysis
- ✓ Can add filters, widgets, forms

**Drawbacks**:
- ✗ Requires Python installation
- ✗ Requires more dependencies
- ✗ Slower startup than static HTML

### Method 4: VS Code Live Server Extension

**For Visual Studio Code only**

**Step 1: Install Live Server**
- Open VS Code
- Extensions panel (Ctrl+Shift+X / Cmd+Shift+X)
- Search "Live Server"
- Click Install (by Ritwick Dey)

**Step 2: Open project in VS Code**
```powershell
# Navigate to project
cd C:\Users\YourName\Documents\Projects\datathon-water-analysis

# Open in VS Code
code .
```

**Step 3: Start Live Server**
- Right-click on `index.html`
- Select "Open with Live Server"
- Or: Click "Go Live" button in status bar

**Step 4: Dashboard opens**
- Browser automatically opens to http://localhost:5500
- Dashboard displays
- Any file changes trigger auto-reload

**Stop Live Server**: Click "Go Live" button again (toggles off)

**Benefits of This Method**:
- ✓ Fastest workflow for editing
- ✓ Automatic browser reload
- ✓ No command line needed
- ✓ Great for quick iterations

**Drawbacks**:
- ✗ VS Code required
- ✗ Extension adds overhead
- ✗ Less control over server settings

---

## Environment Variables Setup

### Configuration File (Optional)

Create file: `config.json` in project root

```json
{
  "data_path": "/data/",
  "server_port": 3000,
  "charts": {
    "bar": {
      "color": "#667eea",
      "height": 400
    },
    "line": {
      "color": "#764ba2",
      "height": 400
    }
  },
  "features": {
    "enable_export": true,
    "enable_download": true,
    "default_year": 2050
  }
}
```

### Loading Configuration (in index.html)

```javascript
// Add to script section
async function loadConfig() {
  try {
    const response = await fetch('./config.json');
    const config = await response.json();
    return config;
  } catch (e) {
    console.warn('Config file not found, using defaults');
    return { data_path: '/data/' };
  }
}

// Use in initialization
const config = await loadConfig();
const dataPath = config.data_path || '/data/';
```

### Environment Variables (Node.js / Vercel)

For production deployment, set in Vercel dashboard:

```
DATA_PATH=/data/
ENVIRONMENT=production
LOG_LEVEL=error
```

---

## First-Time Contributor Checklist

- [ ] Node.js 16+ installed and verified
- [ ] Git configured (`git config --global user.name "Your Name"`)
- [ ] Repository cloned to local machine
- [ ] Entered project directory
- [ ] Ran `npm install` successfully
- [ ] Started HTTP server with `npm run dev`
- [ ] Opened http://localhost:3000 in browser
- [ ] Dashboard displays (shows title, controls, empty charts)
- [ ] Opened `index.html` in text editor
- [ ] Located HTML structure (lines 1-250)
- [ ] Located CSS styling (lines 9-239)
- [ ] Located JavaScript logic (lines 318-521)
- [ ] Read ARCHITECTURE.md to understand system
- [ ] Read PUBLIC_README.md to understand features
- [ ] Created sample CSV in `/data/` folder for testing
- [ ] Successfully modified a chart color (edit `#667eea` in CSS)
- [ ] Refreshed browser and verified color change
- [ ] Successful local development setup!

---

## Troubleshooting Guide

### Issue 1: "npm command not found"

**Cause**: Node.js/npm not installed or not in PATH

**Solution Windows**:
```powershell
# Check if Node.js installed
node --version
npm --version

# If not installed:
# 1. Download from https://nodejs.org/
# 2. Run installer
# 3. Restart PowerShell
# 4. Try again: node --version
```

**Solution macOS/Linux**:
```bash
# Check installation
which node
which npm

# If not found, install with Homebrew:
brew install node

# Verify:
node --version
npm --version
```

### Issue 2: "Cannot find module 'http-server'"

**Cause**: Dependencies not installed

**Solution**:
```powershell
# Navigate to project directory
cd C:\Users\...\datathon-water-analysis

# Install dependencies
npm install

# Verify (should see node_modules folder)
dir node_modules
```

### Issue 3: "CORS error when loading CSV files"

**Cause**: Browser CORS policy blocks local file access

**Solution**:
- Use `http-server` with `--cors` flag (included in npm run dev)
- Use Python HTTP server (also handles CORS)
- DO NOT open `file:///` in browser (violates CORS)

**Command that works**:
```powershell
# Correct - uses http-server with CORS
npm run dev

# Correct - uses Python
python -m http.server 8000

# Incorrect - will have CORS errors
# Don't double-click index.html or use file:// protocol
```

### Issue 4: Charts not rendering

**Cause**:
1. CSV files not loaded (wrong path)
2. Plotly library not loaded (CDN issue)
3. Data format incorrect (CSV parsing error)

**Debug Steps**:
```javascript
// Open browser console: F12
// Check for errors in Console tab

// Add to console to test:
console.log(allData);  // Should show loaded data
console.log(Plotly);   // Should show Plotly object
```

**Solutions**:
1. Verify CDN URLs are correct in HTML:
   - Plotly: `https://cdn.plot.ly/plotly-2.26.0.min.js`
   - PapaParse: `https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js`

2. Create sample `demands.csv` in `/data/` folder:
```csv
EntityName,WugType,WugRegion,WugCounty,D2020,D2030,D2040,D2050,D2060,D2070
Austin,Municipal,Region4,Travis,400,420,440,450,470,490
San Antonio,Municipal,Region15,Bexar,350,370,390,410,430,450
```

3. Check browser Network tab (F12):
   - Should see successful requests to `/data/demands.csv`
   - Status should be 200 (not 404)

### Issue 5: Dropdown menus empty

**Cause**: Data loaded but population fails

**Debug**:
```javascript
// In browser console (F12):
allData.demands.length  // Should be > 0
allData.demands[0]      // Should show object with data
```

**Solution**:
- Verify CSV has header row with exact column names
- Verify data rows have values in WugRegion and WugType columns
- Check browser console for parsing errors

### Issue 6: Port already in use (3000 or 8000)

**Cause**: Another application using the port

**Solution - Windows PowerShell**:
```powershell
# Find process using port 3000
Get-NetTCPConnection -LocalPort 3000 | Select-Object -Property State, OwningProcess

# Get process details
Get-Process -Id (Get-NetTCPConnection -LocalPort 3000).OwningProcess

# Kill the process (replace 1234 with actual PID)
Stop-Process -Id 1234 -Force

# Or start on different port:
npm run dev -- --port 3001
```

**Solution - macOS/Linux**:
```bash
# Find process using port 3000
lsof -i :3000

# Kill the process (replace 1234 with PID)
kill -9 1234

# Or start on different port:
http-server . -p 3001 --cors
```

### Issue 7: Python virtual environment issues (Windows)

**Cause**: Execution policy prevents script running

**Error message**:
```
cannot be loaded because running scripts is disabled on this system
```

**Solution**:
```powershell
# Allow script execution (one-time)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# If asked, type 'Y' and press Enter
# Then activate venv:
.\venv\Scripts\Activate.ps1
```

**Permanent solution** (safer):
```powershell
# Create batch file activation instead:
# File: activate.bat
@echo off
call venv\Scripts\activate.bat
```

### Issue 8: Git clone fails

**Cause**:
- Git not installed
- Network issue
- Repository URL incorrect

**Solution**:
```powershell
# Verify Git installed
git --version

# If not found, install from https://git-scm.com/

# Verify URL is correct (no typos)
git clone https://github.com/username/datathon-water-analysis.git

# If network issue, try again with verbose:
git clone --verbose https://github.com/username/datathon-water-analysis.git
```

### Issue 9: Browser caching old files

**Cause**: Browser cached outdated CSS/JavaScript

**Solution**:
```
Hard refresh:
Windows/Linux: Ctrl+Shift+R
macOS: Cmd+Shift+R

Or:
1. Press F12 to open Developer Tools
2. Right-click refresh button
3. Select "Empty cache and hard refresh"
```

### Issue 10: "Cannot find '/data/demands.csv'"

**Cause**: CSV files not created or wrong path

**Solution**:
```powershell
# Create data folder
mkdir data

# Create sample CSV file
# File: data/demands.csv
# Content (copy to text editor, save as demands.csv):
```

Content for `demands.csv`:
```csv
EntityName,WugType,WugRegion,WugCounty,D2020,D2030,D2040,D2050,D2060,D2070
Austin,Municipal,Region 4,Travis,400,420,440,450,470,490
San Antonio,Municipal,Region 15,Bexar,350,370,390,410,430,450
Houston,Municipal,Region 12,Harris,480,510,540,570,600,630
Dallas,Municipal,Region 7,Dallas,420,450,480,510,540,570
Fort Worth,Municipal,Region 7,Tarrant,320,340,360,380,400,420
```

**Verify**:
```powershell
# Check file exists
ls data/
dir data/

# Should show:
# demands.csv
# existing.csv (if needed)
```

---

## IDE Configuration for VS Code

### Recommended Extensions

**Extension 1: Python (Official Microsoft)**
- Install command in VS Code terminal: `code --install-extension ms-python.python`
- Provides: Python language support, debugging, formatting
- Use for: Running Python analysis, Streamlit development

**Extension 2: Live Server**
- Install: Search "Live Server" in Extensions, by Ritwick Dey
- Provides: Local HTTP server with hot reload
- Use for: Quick HTML/CSS/JS development

**Extension 3: Prettier**
- Install: Search "Prettier", by Prettier
- Provides: Code formatting (HTML, CSS, JavaScript)
- Use for: Consistent code style

**Extension 4: ESLint**
- Install: Search "ESLint", by Microsoft
- Provides: JavaScript error checking
- Use for: Catching syntax errors early

**Extension 5: Thunder Client / REST Client**
- Install: "Thunder Client" or "REST Client"
- Provides: API testing without Postman
- Use for: Testing API endpoints (future)

### VS Code Settings Configuration

Create/Edit: `.vscode/settings.json`

```json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "[python]": {
    "editor.defaultFormatter": "ms-python.python",
    "editor.formatOnSave": true
  },
  "[html]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true
  },
  "[css]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "editor.formatOnSave": true
  },
  "editor.tabSize": 2,
  "editor.insertSpaces": true,
  "editor.trimAutoWhitespace": true,
  "files.trimTrailingWhitespace": true,
  "files.trimFinalNewlines": true
}
```

### VS Code Launch Configuration for Debugging

Create: `.vscode/launch.json`

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Chrome - Debug HTML",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:3000/index.html",
      "webRoot": "${workspaceFolder}"
    },
    {
      "name": "Python - Streamlit",
      "type": "python",
      "request": "launch",
      "module": "streamlit",
      "args": [
        "run",
        "streamlit_app.py"
      ],
      "jinja": true,
      "justMyCode": true
    }
  ]
}
```

### Keyboard Shortcuts (Windows/Linux)

| Action | Shortcut |
|--------|----------|
| Open Terminal | Ctrl+` |
| Open Explorer | Ctrl+Shift+E |
| Open Search | Ctrl+Shift+F |
| Open Debug | Ctrl+Shift+D |
| Format Document | Shift+Alt+F |
| Go to Definition | F12 |
| Go to Line | Ctrl+G |
| Find/Replace | Ctrl+H |
| Save All | Ctrl+K Ctrl+S |

### Keyboard Shortcuts (macOS)

| Action | Shortcut |
|--------|----------|
| Open Terminal | Cmd+` |
| Open Explorer | Cmd+Shift+E |
| Open Search | Cmd+Shift+F |
| Format Document | Shift+Option+F |
| Go to Definition | Cmd+] |
| Go to Line | Cmd+G |
| Find/Replace | Cmd+Option+F |

---

## Development Workflow

### Typical Development Session

**Windows PowerShell**:
```powershell
# 1. Open VS Code
code .

# 2. Open terminal in VS Code (Ctrl+`)
# 3. Start dev server
npm run dev

# 4. Browser should auto-open to http://localhost:3000
# 5. Edit files in VS Code
# 6. Browser auto-refreshes (if using Live Server)

# When done, stop server:
# CTRL+C in terminal
```

### File Editing Workflow

1. **Edit HTML Structure** (`index.html` lines 241-316)
   - Add new control elements
   - Add new chart containers
   - Update semantic structure

2. **Edit CSS Styling** (`index.html` lines 9-239)
   - Change colors, spacing, layout
   - Update responsive breakpoints
   - Add new component styles

3. **Edit JavaScript Logic** (`index.html` lines 318-521)
   - Modify chart rendering
   - Add new filters
   - Implement new features

4. **Save File** (Ctrl+S / Cmd+S)
   - Auto-formatting applies (if Prettier enabled)
   - Browser auto-refreshes (if Live Server enabled)

5. **Open Browser DevTools** (F12)
   - Console tab: Check for JavaScript errors
   - Network tab: Verify CSV files loading
   - Elements tab: Inspect HTML structure
   - Sources tab: Debug JavaScript

### Testing Workflow

```powershell
# 1. Create test data file
# File: data/test_demands.csv
EntityName,WugType,WugRegion,WugCounty,D2020,D2050,D2070
TestCity1,Municipal,TestRegion,TestCounty,100,150,200
TestCity2,Industrial,TestRegion,TestCounty,50,75,100

# 2. Update JavaScript to load test file
# Change line 345 from:
# const response = await fetch(`/data/demands.csv`);
# To:
# const response = await fetch(`/data/test_demands.csv`);

# 3. Reload browser and test

# 4. Revert when done
```

---

## Deployment Preparation

### Pre-Deployment Checklist

- [ ] All local development completed
- [ ] Charts render correctly with live data
- [ ] All interactive features work
- [ ] CSV files organized in `/data/` folder
- [ ] No console errors (F12 > Console)
- [ ] Mobile responsiveness tested (F12 > Toggle device toolbar)
- [ ] All browsers tested (Chrome, Firefox, Safari, Edge)
- [ ] Documentation updated
- [ ] Git changes committed

### Push to GitHub

```powershell
# Check what changed
git status

# Add files to commit
git add .

# Create commit
git commit -m "Feature: Add water demand visualization dashboard"

# Push to GitHub
git push origin main

# Verify on GitHub website
```

### Deploy to Vercel

1. Connect GitHub repository to Vercel
2. Configure build settings:
   - Framework: Static
   - Build Command: (leave empty)
   - Output Directory: ./
3. Add CSV files to Vercel project
4. Deploy branch to production

---

## Conclusion

You now have everything needed to set up, run, develop, and deploy the Texas Water Crisis Dashboard locally. Choose the execution method that best fits your workflow:

- **Static HTTP Server**: Best for most users, minimal dependencies
- **Python Server**: Good if Python already installed
- **Streamlit**: Best for data analysis and exploration
- **VS Code Live Server**: Best for rapid frontend development

For questions, refer to ARCHITECTURE.md for system design or PUBLIC_README.md for feature documentation.
