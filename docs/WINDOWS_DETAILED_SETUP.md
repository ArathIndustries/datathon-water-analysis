# Windows Detailed Setup Guide

Comprehensive Windows setup guide for the Datathon water analysis project. Follow this guide for a professional development environment setup.

---

## Table of Contents

1. [Prerequisites & System Requirements](#prerequisites--system-requirements)
2. [Git Configuration for Windows](#git-configuration-for-windows)
3. [Node.js and npm Setup](#nodejs-and-npm-setup)
4. [Python 3.8+ Setup with Virtual Environment](#python-38-setup-with-virtual-environment)
5. [Folder Structure & Navigation](#folder-structure--navigation)
6. [Step-by-Step: Clone → Install → Run](#step-by-step-clone--install--run)
7. [PowerShell vs Command Prompt](#powershell-vs-command-prompt)
8. [Anaconda/Miniconda Alternative Setup](#anacondaminiconda-alternative-setup)
9. [PyCharm Integration](#pycharm-integration)
10. [GitHub Desktop Setup](#github-desktop-setup)
11. [Common Commands Reference](#common-commands-reference)

---

## Prerequisites & System Requirements

### Windows Version
- **Windows 10**: Build 19041 or later (May 2020 Update or newer)
- **Windows 11**: Any version

**Check your version:**

```powershell
Get-WmiObject -Class Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber
```

Example output:
```
Caption                  Version BuildNumber
-------                  ------- -----------
Microsoft Windows 11 Pro 10.0    22621
```

### System Resources
- **RAM**: Minimum 4 GB (8 GB recommended)
- **Disk Space**: 2 GB free
- **Administrator Access**: Required for some installations

---

## Git Configuration for Windows

### Installation

**Method 1: Windows Package Manager (Recommended)**

```powershell
winget install Git.Git
```

**Method 2: Manual Installation**

1. Visit https://git-scm.com/download/win
2. Download the latest installer
3. Run installer with these recommended settings:
   - Editor: Use Visual Studio Code as Git's default editor
   - Line endings: Checkout as-is, commit as Unix-style (LF)
   - Terminal emulation: Use Windows' default console window
4. Click Install

### Global Configuration

After installation, configure Git globally:

```powershell
# Set your name (appears in commits)
git config --global user.name "Your Full Name"

# Set your email (must match GitHub account)
git config --global user.email "your.email@example.com"

# Configure line endings (critical for Windows)
git config --global core.autocrlf true

# Set default branch name
git config --global init.defaultBranch main

# View all global settings
git config --global --list
```

### Credentials Setup (Important!)

**Option 1: GitHub Personal Access Token (Recommended for 2024+)**

GitHub deprecated password authentication. Use Personal Access Token instead:

1. Visit https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Set permissions:
   - ✓ repo (full control of private repositories)
   - ✓ workflow
4. Click "Generate token" and copy the token
5. In PowerShell, store the token:

```powershell
# First time you push, you'll be prompted for credentials
# Username: your-github-username
# Password: paste-your-token-here

# To store permanently:
git config --global credential.helper wincred
# Or on newer Windows 11:
git config --global credential.helper manager-core
```

**Option 2: SSH Keys (For advanced users)**

```powershell
# Generate SSH key (in your user home directory)
cd ~
ssh-keygen -t ed25519 -C "your.email@example.com"

# When prompted "Enter file in which to save the key", press Enter
# When prompted for passphrase, press Enter (or set one)

# View your public key
Get-Content ~/.ssh/id_ed25519.pub
```

Then add this public key to GitHub:
1. Visit https://github.com/settings/ssh/new
2. Title: "Windows Machine"
3. Paste the public key
4. Click "Add SSH key"

### Line Endings Warning

Windows uses CRLF (`\r\n`), Unix uses LF (`\n`). Git can auto-convert:

```powershell
# Already set above, but verify:
git config --global core.autocrlf
# Should output: true
```

**If you see merge conflicts with line endings:**

```powershell
# Fix in current repository
git config core.autocrlf true
git rm --cached -r .
git reset --hard HEAD
```

---

## Node.js and npm Setup

### Installation

**Method 1: Windows Package Manager**

```powershell
winget install OpenJS.NodeJS
```

**Method 2: Manual Installation**

1. Visit https://nodejs.org/
2. Download "LTS" (Long Term Support) version
3. Run installer, use all defaults
4. Restart PowerShell when complete

### Verification

```powershell
node --version
npm --version
```

Expected output:
```
v20.10.0
10.2.4
```

### npm Configuration

```powershell
# Update npm to latest
npm install -g npm@latest

# Set npm registry (default is fine, but you can verify)
npm config get registry
# Should output: https://registry.npmjs.org/

# Set npm to use auth tokens if needed
npm login
# Follow prompts (optional, only if publishing packages)
```

### Global npm Packages (Optional)

```powershell
# Useful development tools
npm install -g typescript
npm install -g ts-node
npm install -g nodemon

# Verify
npm list -g --depth=0
```

---

## Python 3.8+ Setup with Virtual Environment

### Python Installation

**Method 1: Windows Package Manager**

```powershell
winget install Python.Python.3.11
```

**Method 2: Microsoft Store**

```powershell
# Opens Microsoft Store
start ms-windows-store://pdp/?ProductId=9NRWMJP3717K
```

**Method 3: Manual Installation**

1. Visit https://www.python.org/downloads/
2. Click "Download Python 3.11" (or latest 3.x)
3. **CRITICAL**: Check the "Add Python to PATH" checkbox
4. Click "Install Now"
5. Wait for completion

### Verification

```powershell
python --version
python -c "import sys; print(sys.executable)"
```

Expected output:
```
Python 3.11.7
C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\python.exe
```

### Virtual Environment Setup

Virtual environments isolate project dependencies. **Always use one**.

```powershell
# Navigate to project folder
cd C:\Users\Arath\Automation_Station\Projects\Datathon\web

# Create virtual environment (creates 'venv' folder)
python -m venv venv

# Activate it (on Windows with PowerShell)
venv\Scripts\Activate.ps1

# If you get execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Activate again:
venv\Scripts\Activate.ps1
```

You'll see `(venv)` prefix in your prompt:
```
(venv) C:\Users\Arath\Automation_Station\Projects\Datathon\web>
```

### Virtual Environment Management

```powershell
# Activate environment (before any project work)
venv\Scripts\Activate.ps1

# Deactivate environment (when done)
deactivate

# Delete environment (if needed to start fresh)
Remove-Item -Recurse -Force venv

# Create new environment
python -m venv venv

# Install packages in environment
pip install -r requirements.txt
```

### pip Configuration

```powershell
# Upgrade pip (important!)
python -m pip install --upgrade pip

# Check pip version
pip --version

# View installed packages
pip list

# Check package versions
pip show numpy
pip show pandas
pip show streamlit
```

---

## Folder Structure & Navigation

### Windows File Paths

```
C:\Users\Arath\Automation_Station\Projects\Datathon\
├── web\                    # Main web project folder
│   ├── docs\               # Documentation (where this file is)
│   ├── src\                # Python source code
│   ├── data\               # Data files
│   ├── dashboards\         # HTML dashboards
│   ├── notebooks\          # Jupyter notebooks
│   ├── app.py              # Main Streamlit app
│   ├── package.json        # Node.js dependencies
│   ├── requirements.txt    # Python dependencies
│   ├── index.html          # Static HTML dashboard
│   ├── config.json         # Configuration file
│   ├── README.md           # Main README
│   └── venv\               # Virtual environment (created by you)
│
├── raw_data\               # Original data files
├── processed_data\         # Cleaned data
├── notebooks\              # Analysis notebooks
├── phases\                 # Project phases
├── analysis\               # Analysis results
└── [documentation files]   # METHODOLOGY.md, etc.
```

### Navigation in PowerShell

```powershell
# Go to project folder
cd C:\Users\Arath\Automation_Station\Projects\Datathon\web

# Show current folder
pwd
# Output: C:\Users\Arath\Automation_Station\Projects\Datathon\web

# List contents
ls
# Or:
dir

# Go to docs folder
cd docs

# Go back to parent folder
cd ..

# Go to home folder
cd ~

# Go to specific folder (absolute path)
cd C:\Users\Arath\Desktop

# Create new folder
mkdir my_folder

# Create file
New-Item -Path . -Name "test.txt" -ItemType "file"
```

### Environment Variables

Check if tools are in your PATH:

```powershell
# Check Python path
$env:Path -split ';' | Select-String python

# Check Git path
$env:Path -split ';' | Select-String git

# View all environment variables
Get-ChildItem env:

# Set temporary variable (for current session)
$env:MYVAR = "value"
echo $env:MYVAR

# Set permanent environment variable (Windows)
# Via GUI: Settings → Environment Variables
# Via PowerShell (Admin):
[Environment]::SetEnvironmentVariable("MYVAR", "value", "User")
```

---

## Step-by-Step: Clone → Install → Run

### Complete Setup From Scratch

```powershell
# 1. Create project parent folder (if it doesn't exist)
cd C:\Users\Arath\Automation_Station\Projects

# 2. Clone repository
git clone https://github.com/yourusername/datathon-water-analysis.git
cd datathon-water-analysis
cd web

# 3. Create Python virtual environment
python -m venv venv

# 4. Activate virtual environment
venv\Scripts\Activate.ps1

# 5. Upgrade pip
python -m pip install --upgrade pip

# 6. Install Python dependencies
pip install -r requirements.txt

# 7. Install Node dependencies (if using Node.js dashboards)
npm install

# 8. Verify configuration
python -c "import streamlit; print(f'Streamlit {streamlit.__version__} installed')"
python -c "import pandas; print(f'Pandas {pandas.__version__} installed')"

# 9. Run Streamlit dashboard
streamlit run app.py

# 10. Dashboard opens at: http://localhost:8501
```

### Expected Output

```
Streamlit is running...
  URL: http://localhost:8501
  Ready to accept connections
```

---

## PowerShell vs Command Prompt

### PowerShell (Recommended)

Modern, powerful, object-oriented shell. Recommended for this project.

```powershell
# Activation command (PowerShell)
venv\Scripts\Activate.ps1

# If you get "cannot be loaded because running scripts is disabled":
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Navigation
cd C:\Users\Arath\...

# File operations
ls              # List files
pwd             # Print working directory
mkdir name      # Create folder
copy file1 file2
move file1 file2
del file1
```

**Opening PowerShell:**
- Press `Win + X` → "Windows Terminal" or "PowerShell"
- Or: Right-click folder → "Open Terminal here"

### Command Prompt (Legacy)

Still works, but less powerful. Use PowerShell instead.

```cmd
# Activation command (Command Prompt)
venv\Scripts\activate.bat

# Navigation
cd C:\Users\Arath\...

# File operations
dir              # List files
cd               # Print current directory
mkdir name
copy file1 file2
move file1 file2
del file1
```

### Key Differences

| Operation | PowerShell | Command Prompt |
|-----------|-----------|----------------|
| Activate venv | `venv\Scripts\Activate.ps1` | `venv\Scripts\activate.bat` |
| View path | `$env:Path` | `echo %PATH%` |
| Run .exe | Direct name | Direct name |
| Piping output | `cmd1 \| cmd2` | `cmd1 \| cmd2` |
| Execution policy | May need to set | Not required |

---

## Anaconda/Miniconda Alternative Setup

If you prefer Anaconda/Miniconda for package management:

### Miniconda Installation (Lighter than Anaconda)

1. Download: https://docs.conda.io/projects/miniconda/en/latest/
2. Choose "Miniconda3 Windows 64-bit"
3. Run installer
4. Check "Add Miniconda3 to my PATH" during installation
5. Restart PowerShell

### Verification

```powershell
conda --version
conda config --show channels
```

### Virtual Environment with Conda

```powershell
# Create conda environment
conda create --name datathon python=3.11

# Activate it
conda activate datathon

# You'll see (datathon) in your prompt

# Install dependencies
pip install -r requirements.txt

# Deactivate when done
conda deactivate
```

### Useful Conda Commands

```powershell
# List all environments
conda env list

# Remove environment
conda remove --name datathon --all

# Export environment to file
conda env export > environment.yml

# Create environment from file
conda env create -f environment.yml

# Update all packages in environment
conda update --all

# Check package version
conda list streamlit
```

### Conda vs Pip Gotchas

```powershell
# ✓ GOOD: Install all from pip
pip install -r requirements.txt

# ✓ GOOD: Install all from conda
conda install pandas numpy streamlit plotly

# ✗ AVOID: Mixing conda and pip excessively
# Can cause version conflicts!
conda install pandas
pip install streamlit  # Usually OK, but can break things

# BEST PRACTICE: Use one package manager consistently
# If using Anaconda, prefer: conda install package_name
# If using venv, prefer: pip install package_name
```

---

## PyCharm Integration

### PyCharm Installation

Download Community Edition (free): https://www.jetbrains.com/pycharm/download/

### Configure Project

1. **Open project in PyCharm**
   - File → Open → Navigate to `C:\Users\Arath\Automation_Station\Projects\Datathon\web`
   - Click "Open as Project"

2. **Configure Python Interpreter**
   - File → Settings (or PyCharm → Preferences on Mac)
   - Project: datathon-water-analysis → Python Interpreter
   - Click "Add Interpreter" → "Add Local Interpreter"
   - Select "Existing Environment"
   - Browse to: `C:\Users\Arath\Automation_Station\Projects\Datathon\web\venv\Scripts\python.exe`
   - Click OK

3. **Verify Setup**
   - Open `src/data_processing.py` (or any Python file)
   - Hover over import: should show no red squiggles
   - Bottom right should show your Python version

### Run Streamlit from PyCharm

```
# Create Run Configuration
Run → Edit Configurations → + → Python

Name: Streamlit App
Script: streamlit
Parameters: run app.py
Python Interpreter: datathon-water-analysis

Then: Run → Run Streamlit App (or press Shift+F10)
```

### Useful PyCharm Features

```
Ctrl+Alt+L    # Format code
Ctrl+/        # Toggle comment
Alt+Enter     # Quick fix
Ctrl+Shift+F  # Find in files
Ctrl+H        # Replace in files
F2            # Go to next error
Shift+F10     # Run selected configuration
```

---

## GitHub Desktop Setup

If you prefer GUI over command line:

### Installation

1. Download: https://desktop.github.com/
2. Run installer
3. Sign in with GitHub account
4. Configure Git name and email when prompted

### Clone Repository

1. File → Clone Repository
2. URL tab → Paste: `https://github.com/yourusername/datathon-water-analysis.git`
3. Local Path: `C:\Users\Arath\Automation_Station\Projects\`
4. Click "Clone"

### Common Operations

**Making Changes:**
1. Edit files in your IDE
2. GitHub Desktop shows changed files
3. Enter commit message in text field
4. Click "Commit to main"
5. Click "Push origin" to send to GitHub

**Pulling Updates:**
1. Click "Fetch origin" (checks for updates)
2. Click "Pull origin" (downloads updates)

**Creating Branches:**
1. Click "Current Branch" → "New Branch"
2. Name your branch
3. Select "main" as base branch
4. Click "Create Branch"
5. Work on your branch
6. Commit changes
7. Click "Push origin"
8. Go to GitHub and create Pull Request

---

## Common Commands Reference

### Git Commands

```powershell
# Clone repository
git clone https://github.com/yourusername/repo.git

# Check status
git status

# See recent commits
git log --oneline -10

# Stage specific files
git add file1.py file2.py

# Stage all changes
git add .

# Commit changes
git commit -m "Fix bug in data processing"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# Create new branch
git checkout -b feature-branch-name

# Switch branches
git checkout main
git checkout feature-branch-name

# View branches
git branch -a

# Delete local branch
git branch -d feature-branch-name

# Delete remote branch
git push origin --delete feature-branch-name

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# View differences
git diff                    # Unstaged changes
git diff --staged           # Staged changes
git diff main feature       # Compare branches

# Merge branch to main
git checkout main
git merge feature-branch-name

# Resolve merge conflicts
# Edit conflicted files, then:
git add .
git commit -m "Resolve merge conflicts"
```

### npm Commands

```powershell
# Install dependencies from package.json
npm install

# Install specific package
npm install package-name

# Install globally
npm install -g package-name

# Start development server
npm start

# Build for production
npm run build

# List installed packages
npm list

# List global packages
npm list -g --depth=0

# Update all packages
npm update

# Check for security vulnerabilities
npm audit

# Fix security vulnerabilities
npm audit fix

# View package info
npm info package-name
```

### Python/pip Commands

```powershell
# Activate virtual environment
venv\Scripts\Activate.ps1

# Deactivate virtual environment
deactivate

# Install dependencies
pip install -r requirements.txt

# Install specific package
pip install package-name

# Install specific version
pip install package-name==1.2.3

# Upgrade package
pip install --upgrade package-name

# List installed packages
pip list

# Show package info
pip show package-name

# Freeze dependencies (create requirements.txt)
pip freeze > requirements.txt

# Install with upgrade
pip install -U -r requirements.txt

# Search for package
pip search package-name

# Check for outdated packages
pip list --outdated
```

### Streamlit Commands

```powershell
# Run Streamlit app
streamlit run app.py

# Run on different port
streamlit run app.py --server.port 8502

# Run with debugging
streamlit run app.py --logger.level=debug

# Clear cache
streamlit cache clear
```

### File Operations

```powershell
# Create file
New-Item -Path . -Name "filename.txt" -ItemType "file"

# Create folder
mkdir folder-name

# Copy file/folder
Copy-Item source.txt destination.txt
Copy-Item -Recurse source-folder destination-folder

# Move file/folder
Move-Item source.txt destination.txt

# Delete file
Remove-Item file.txt

# Delete folder (with contents)
Remove-Item -Recurse folder-name

# List files
ls
dir
Get-ChildItem

# Find files
ls -Recurse -Filter "*.py"
Get-ChildItem -Recurse -Filter "*.py"

# Change to directory
cd path\to\directory
cd ..              # Parent directory
cd ~               # Home directory

# Print current directory
pwd

# View file contents
Get-Content filename.txt
type filename.txt  # Alternative

# Edit file
notepad filename.txt
code filename.txt  # If VS Code installed
```

---

## Firewall and Antivirus Configuration

If localhost connections are blocked:

### Windows Defender Firewall

```powershell
# Check firewall status
Get-NetFirewallProfile

# Allow Python through firewall (Admin PowerShell)
New-NetFirewallRule -DisplayName "Allow Python" -Direction Inbound -Program "C:\Users\Arath\AppData\Local\Programs\Python\Python311\python.exe" -Action Allow

# Allow Node.js through firewall
New-NetFirewallRule -DisplayName "Allow Node.js" -Direction Inbound -Program "C:\Program Files\nodejs\node.exe" -Action Allow

# View all firewall rules
Get-NetFirewallRule | Where-Object {$_.DisplayName -like "*Python*"}
```

### Third-Party Antivirus

Add these to exclusions (depends on antivirus, but typically):
- `C:\Users\Arath\Automation_Station\Projects\Datathon\web\venv\`
- `C:\Users\Arath\Automation_Station\Projects\Datathon\web\node_modules\`
- `localhost:8501`
- `127.0.0.1:8501`

---

## Environment File Configuration

### config.json Setup

```json
{
  "data_paths": {
    "raw_data": "C:\\Users\\Arath\\Automation_Station\\Projects\\Datathon\\raw_data",
    "processed_data": "C:\\Users\\Arath\\Automation_Station\\Projects\\Datathon\\processed_data",
    "export_path": "C:\\Users\\Arath\\Documents\\Datathon_Exports"
  },
  "database": {
    "host": "localhost",
    "port": 5432,
    "name": "datathon"
  },
  "api": {
    "usgs_url": "https://waterservices.usgs.gov/",
    "timeout": 30
  }
}
```

Note: Use `\\` for path separators in JSON (Windows format).

### Environment Variables (.env file)

Create `.env` file in `C:\Users\Arath\Automation_Station\Projects\Datathon\web\`:

```
# Data Configuration
DATA_PATH=C:\Users\Arath\Automation_Station\Projects\Datathon\raw_data
OUTPUT_PATH=C:\Users\Arath\Automation_Station\Projects\Datathon\processed_data

# API Configuration
API_TIMEOUT=30
MAX_FILE_SIZE=104857600

# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_LOGGER_LEVEL=info

# Development
DEBUG=false
ENV=production
```

Load in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()
data_path = os.getenv('DATA_PATH')
```

---

## Troubleshooting Quick Links

Having issues? See **WINDOWS_TROUBLESHOOTING.md** for:
- Git errors and permission issues
- Python path problems
- Module import failures
- Port conflicts
- File encoding issues
- And 40+ more solutions

---

## Next Steps

1. Complete the setup by following "Step-by-Step: Clone → Install → Run" above
2. Verify everything works: `streamlit run app.py`
3. Review **WINDOWS_QUICK_REFERENCE.md** for command cheat sheet
4. Check **WINDOWS_TROUBLESHOOTING.md** if you encounter issues

**Questions?**
- Review the main README.md for project overview
- Check GitHub issues for common problems
- Review config.json documentation
