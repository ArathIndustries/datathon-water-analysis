# Windows Quick Start Guide (5 Minutes)

Get the Datathon water analysis dashboard running in 5 minutes on Windows 10/11.

## System Requirements Check

Before starting, verify you have Windows 10 or 11 installed:

```powershell
# Check Windows version (PowerShell)
Get-WmiObject -Class Win32_OperatingSystem | Select-Object Caption, Version
```

**Expected output**: Windows 10 (build 19041+) or Windows 11

## Step 1: Download Required Tools (2 minutes)

Copy-paste each command one at a time:

### Git
```powershell
# Option 1: Using Winget (Windows 11 recommended)
winget install Git.Git

# Option 2: Download and install manually
# Visit: https://git-scm.com/download/win
# Run the installer, keep all defaults
```

### Node.js (includes npm)
```powershell
# Option 1: Using Winget
winget install OpenJS.NodeJS

# Option 2: Download and install manually
# Visit: https://nodejs.org/
# Click "LTS" version
# Run installer, keep all defaults
```

### Python 3.8+
```powershell
# Option 1: Using Winget
winget install Python.Python.3.11

# Option 2: Download and install manually
# Visit: https://www.python.org/downloads/
# Click "Download Python 3.11"
# IMPORTANT: Check "Add Python to PATH" during installation
# Run installer
```

**Verify installations** (paste each command):

```powershell
git --version
node --version
npm --version
python --version
```

All should show version numbers. If any shows "not recognized", the tool didn't install properly.

## Step 2: Clone Repository (1 minute)

Copy-paste this entire command:

```powershell
git clone https://github.com/yourusername/datathon-water-analysis.git
cd datathon-water-analysis/web
```

Replace `yourusername` with the actual GitHub username.

**Expected result**: A folder appears in your user directory with all project files.

## Step 3: Setup Python Environment (30 seconds)

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**You'll see** `(venv)` at the start of your command prompt.

## Step 4: Install Dependencies (1 minute)

```powershell
pip install -r requirements.txt
```

This downloads and installs all needed Python packages. Takes 30-60 seconds.

## Step 5: Run the Dashboard

### Option A: Streamlit Dashboard (Interactive, recommended)

```powershell
streamlit run app.py
```

Browser should **automatically open** to `http://localhost:8501`

**You'll see**:
- Loading message in terminal
- Dashboard in browser with water analysis charts and filters
- Click "Stop" in your terminal to stop the dashboard

### Option B: HTML Dashboard (Static, offline-friendly)

```powershell
python build_static_dashboard.py
start index.html
```

Browser opens showing the static dashboard. No need to keep terminal running.

---

## Done! Troubleshooting

**If git clone failed:**
- Check internet connection
- Verify URL is correct
- Run: `git config --global http.sslVerify false` (if SSL error)

**If Python not found:**
- Restart PowerShell completely (close and reopen)
- Verify Python is in PATH: `python -c "import sys; print(sys.executable)"`

**If pip install failed:**
- Update pip: `python -m pip install --upgrade pip`
- Check internet connection
- Try: `pip install --upgrade --force-reinstall -r requirements.txt`

**If port 8501 already in use:**
- Change port: `streamlit run app.py --server.port 8502`
- Or close the application using port 8501

**If browser won't open:**
- Manually open: `http://localhost:8501` in your browser
- Check firewall isn't blocking localhost

---

## Quick Reference

| Task | Command |
|------|---------|
| Activate environment | `venv\Scripts\activate` |
| Deactivate environment | `deactivate` |
| Start Streamlit | `streamlit run app.py` |
| Start static dashboard | `python build_static_dashboard.py && start index.html` |
| Stop dashboard | `Ctrl+C` in terminal |
| View Python path | `python -c "import sys; print(sys.executable)"` |
| Check git status | `git status` |
| Update dependencies | `pip install --upgrade -r requirements.txt` |

---

## Next Steps

- Read **WINDOWS_DETAILED_SETUP.md** for advanced configuration
- Read **WINDOWS_TROUBLESHOOTING.md** if you encounter issues
- Read **WINDOWS_QUICK_REFERENCE.md** for command cheat sheet

**Need help?**
- Check docs folder for configuration details
- Open an issue on GitHub
- Review the main README.md for architecture overview
