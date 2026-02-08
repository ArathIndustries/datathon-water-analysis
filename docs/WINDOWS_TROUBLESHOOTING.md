# Windows Troubleshooting Guide (50+ Solutions)

Comprehensive troubleshooting guide for common Windows development issues with the Datathon project.

---

## Table of Contents

- [Git Issues](#git-issues)
- [Python Issues](#python-issues)
- [Virtual Environment Issues](#virtual-environment-issues)
- [Module and Package Issues](#module-and-package-issues)
- [Port and Network Issues](#port-and-network-issues)
- [File and Data Issues](#file-and-data-issues)
- [Streamlit Specific Issues](#streamlit-specific-issues)
- [Git Repository Issues](#git-repository-issues)
- [Performance and Encoding Issues](#performance-and-encoding-issues)
- [IDE and Editor Issues](#ide-and-editor-issues)

---

## Git Issues

### 1. "git: command not found"

**Problem**: Git is not in your PATH or not installed.

**Solution 1: Verify Installation (Easiest)**

```powershell
# Check if Git is installed
git --version

# If not found, reinstall Git
# Download from: https://git-scm.com/download/win
# Make sure to check "Add to PATH" during installation
# Restart PowerShell after installation
```

**Solution 2: Add Git to PATH Manually**

```powershell
# Check your Git installation location
Get-Command git
# If found, PATH is already set

# If not found, manually add to PATH:
# Typical installation location: C:\Program Files\Git\cmd

# Add to PATH (Admin PowerShell):
[Environment]::SetEnvironmentVariable(
    "Path",
    "$env:Path;C:\Program Files\Git\cmd",
    "User"
)

# Restart PowerShell and verify
git --version
```

**Solution 3: Use Git from Git Bash**

```powershell
# Windows installs "Git Bash" as separate shell
# Click Start → Search "Git Bash" → Open
# Commands work the same in Git Bash
```

---

### 2. "fatal: Authentication failed" (When Cloning)

**Problem**: GitHub credentials rejected.

**Solution 1: Use Personal Access Token (Most Common)**

```powershell
# GitHub deprecated password authentication
# Generate new token at: https://github.com/settings/tokens

# When git asks for credentials:
# Username: your-github-username
# Password: paste-your-personal-access-token-here

# To store credentials permanently:
git config --global credential.helper wincred

# Test: Try cloning again
git clone https://github.com/yourusername/datathon-water-analysis.git
```

**Solution 2: Setup SSH Keys**

```powershell
# Generate SSH key (run once in home directory)
cd ~
ssh-keygen -t ed25519 -C "your.email@example.com"

# When prompted, press Enter for all prompts (no passphrase needed)

# View your public key
Get-Content ~/.ssh/id_ed25519.pub

# Add to GitHub:
# 1. Visit https://github.com/settings/ssh/new
# 2. Title: "Windows Machine"
# 3. Paste the output from above
# 4. Click "Add SSH key"

# Clone using SSH (use this URL format instead)
git clone git@github.com:yourusername/datathon-water-analysis.git
```

**Solution 3: Reset Stored Credentials**

```powershell
# If wrong credentials cached, clear them:
git config --global --unset credential.helper
# or:
cmdkey /delete:git:https://github.com
# Then try cloning again - will prompt for credentials
```

---

### 3. "fatal: could not read Username" (Headless)

**Problem**: Git can't prompt for credentials (no interactive terminal).

**Solution**: Use SSH keys or Personal Access Token in URL:

```powershell
# With PAT in URL (less secure, not recommended):
git clone https://username:personal_access_token@github.com/username/repo.git

# Better: Use SSH (see Solution 2 above)
git clone git@github.com:username/repo.git

# Or use stored credentials with helper:
git config --global credential.helper wincred
```

---

### 4. "LF will be replaced by CRLF" (Line Endings Warning)

**Problem**: Git warns about line ending conversions (harmless but annoying).

**Solution 1: Configure Line Endings Globally (Recommended)**

```powershell
# Set global configuration (should already be done in setup)
git config --global core.autocrlf true

# Verify it's set
git config --global core.autocrlf
# Output should be: true
```

**Solution 2: Fix Existing Repository**

```powershell
# If warning persists, normalize all line endings in current repo:
git config core.autocrlf true
git rm --cached -r .
git reset --hard HEAD

# Verify
git status  # Should show no changes
```

**Solution 3: Suppress Warning (Not Recommended)**

```powershell
# Suppress the warning (but doesn't fix the issue)
git config core.safecrlf false
```

---

### 5. "SSL: CERTIFICATE_VERIFY_FAILED"

**Problem**: Git can't verify SSL certificates (antivirus/firewall issue).

**Solution 1: Trust GitHub's Certificate (Temporary)**

```powershell
# Disable SSL verification (for current command only)
git -c http.sslVerify=false clone https://github.com/yourusername/repo.git

# After cloning, reenable SSL:
git config --global http.sslVerify true
```

**Solution 2: Trust GitHub's Certificate (Permanent)**

```powershell
# NOT recommended, but if necessary:
git config --global http.sslVerify false

# Re-enable later:
git config --global http.sslVerify true
```

**Solution 3: Fix Antivirus/Firewall (Better)**

- Check your antivirus - it's likely intercepting HTTPS
- Add GitHub to antivirus exclusions
- Or disable antivirus temporarily for cloning
- Restart PowerShell after changing antivirus settings

---

### 6. "Permission denied (publickey)" (SSH Error)

**Problem**: SSH key not recognized.

**Solution 1: Verify SSH Key Exists**

```powershell
# Check if SSH key files exist
dir ~/.ssh

# Should show: id_ed25519, id_ed25519.pub

# If not, generate them:
ssh-keygen -t ed25519 -C "your.email@example.com"
# Press Enter for all prompts
```

**Solution 2: SSH Agent Not Running**

```powershell
# Check SSH agent status
Get-Service ssh-agent | Select-Object Status

# If status is Stopped, start it:
Start-Service ssh-agent
Set-Service -Name ssh-agent -StartupType Automatic

# Add your key to agent:
ssh-add ~/.ssh/id_ed25519

# Test connection:
ssh -T git@github.com
# Should output: "Hi yourusername! You've successfully authenticated..."
```

**Solution 3: Wrong Key Added to GitHub**

```powershell
# View your public key again
Get-Content ~/.ssh/id_ed25519.pub

# Go to https://github.com/settings/ssh
# Make sure this exact key is listed
# Delete old/wrong keys
# Add the correct one
```

---

## Python Issues

### 7. "python: command not found"

**Problem**: Python is not installed or not in PATH.

**Solution 1: Verify Installation**

```powershell
python --version

# If not found:
python3 --version

# If neither works, Python isn't installed
```

**Solution 2: Install Python**

```powershell
# Download from: https://www.python.org/downloads/
# Download Python 3.11 or later
# IMPORTANT: Check "Add Python to PATH" during installation
# Run installer and wait for completion

# Restart PowerShell completely
# Then verify:
python --version
```

**Solution 3: Add Python to PATH Manually**

```powershell
# Find Python installation
python -c "import sys; print(sys.executable)"
# Example output: C:\Users\Arath\AppData\Local\Programs\Python\Python311\python.exe

# Add folder to PATH (Admin PowerShell):
$pythonPath = "C:\Users\Arath\AppData\Local\Programs\Python\Python311"
[Environment]::SetEnvironmentVariable(
    "Path",
    "$env:Path;$pythonPath",
    "User"
)

# Restart PowerShell
python --version
```

**Solution 4: Use python3 Instead**

```powershell
# Windows sometimes installs as python3
python3 --version

# If this works, use it going forward:
python3 -m venv venv
python3 -m pip install -r requirements.txt
```

---

### 8. Python Path Issues

**Problem**: Different Python versions installed, unsure which one is active.

**Solution 1: Check Active Python**

```powershell
# See which Python is being used
python -c "import sys; print(sys.executable)"

# Output example:
# C:\Users\Arath\AppData\Local\Programs\Python\Python311\python.exe

# Check version
python --version
```

**Solution 2: Use Specific Python Version**

```powershell
# If multiple versions installed, specify explicitly
C:\Users\Arath\AppData\Local\Programs\Python\Python311\python.exe --version

# Use full path for venv:
C:\Users\Arath\AppData\Local\Programs\Python\Python311\python.exe -m venv venv

# Or use python3.11:
py -3.11 --version
py -3.11 -m venv venv
```

**Solution 3: Use py Launcher**

```powershell
# Windows has py launcher for managing multiple Python versions
py --list
# Shows all installed Python versions

# Run specific version:
py -3.11 --version
py -3.11 -m venv venv
py -3.11 -m pip install -r requirements.txt

# Check default version:
py --version
```

---

### 9. "ModuleNotFoundError: No module named 'streamlit'"

**Problem**: Packages not installed in active Python environment.

**Solution 1: Verify Virtual Environment Active**

```powershell
# Check if (venv) appears in your prompt
# If not, activate it:
cd C:\Users\Arath\Automation_Station\Projects\Datathon\web
venv\Scripts\Activate.ps1

# You should now see (venv) at start of prompt
```

**Solution 2: Install Requirements**

```powershell
# Make sure venv is active (see above)
pip install -r requirements.txt

# Wait for installation to complete
# Verify:
pip list | grep streamlit
```

**Solution 3: Check Which Python pip Uses**

```powershell
# Verify pip is using the right Python
pip --version
# Should show path to venv's Python

# If not, use explicit path:
venv\Scripts\pip --version
venv\Scripts\pip install -r requirements.txt
```

**Solution 4: Fresh Install**

```powershell
# If still not working, try fresh installation:
deactivate  # Exit venv if active

# Delete old environment:
Remove-Item -Recurse -Force venv

# Create new one:
python -m venv venv
venv\Scripts\Activate.ps1

# Install again:
python -m pip install --upgrade pip
pip install -r requirements.txt

# Verify:
pip list
```

---

## Virtual Environment Issues

### 10. "venv\Scripts\Activate.ps1 cannot be loaded"

**Problem**: PowerShell execution policy prevents script execution.

**Solution 1: Set Execution Policy (Recommended)**

```powershell
# Set policy to allow local scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# You may be prompted to confirm
# Type 'Y' and press Enter

# Try activation again:
venv\Scripts\Activate.ps1

# You should see (venv) in prompt
```

**Solution 2: Use Command Prompt Instead**

```powershell
# Switch to Command Prompt (cmd.exe)
cmd

# Then activate with .bat file:
venv\Scripts\activate.bat

# You should see (venv) in prompt
```

**Solution 3: Use Full Path**

```powershell
# Run with full path without execution policy:
& "C:\Users\Arath\Automation_Station\Projects\Datathon\web\venv\Scripts\Activate.ps1"
```

---

### 11. Virtual Environment Not Found

**Problem**: venv folder doesn't exist or is in wrong location.

**Solution 1: Create Virtual Environment**

```powershell
# Navigate to project folder
cd C:\Users\Arath\Automation_Station\Projects\Datathon\web

# Create venv
python -m venv venv

# Activate
venv\Scripts\Activate.ps1
```

**Solution 2: Verify Location**

```powershell
# Check if venv exists
dir venv
# Should list: Include, Lib, Scripts, pyvenv.cfg

# Or:
ls venv
```

**Solution 3: venv Corrupted**

```powershell
# Delete and recreate:
Remove-Item -Recurse -Force venv
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

### 12. "pip: command not found" (In Virtual Environment)

**Problem**: pip not working even with venv activated.

**Solution 1: Upgrade pip**

```powershell
# Activate venv (should already be active)
venv\Scripts\Activate.ps1

# Upgrade pip:
python -m pip install --upgrade pip

# Verify:
pip --version
```

**Solution 2: Use Python Module Directly**

```powershell
# If pip command doesn't work, use module directly:
python -m pip install streamlit
python -m pip install -r requirements.txt
python -m pip list
```

**Solution 3: Check Python Path**

```powershell
# Verify you're using venv's Python
python -c "import sys; print(sys.executable)"

# Should output path with 'venv' in it:
# C:\Users\Arath\Automation_Station\Projects\Datathon\web\venv\Scripts\python.exe

# If not, venv isn't activated
venv\Scripts\Activate.ps1
```

---

## Module and Package Issues

### 13. "ModuleNotFoundError" for Other Packages

**Problem**: Package like pandas, plotly, numpy not found.

**Solution 1: Install Missing Package**

```powershell
# Activate venv
venv\Scripts\Activate.ps1

# Install package
pip install pandas
pip install plotly
pip install numpy

# Or install all at once:
pip install -r requirements.txt
```

**Solution 2: Check Package Spelling**

```powershell
# Common package name mistakes:
# ✓ pandas (not panda, not pandas-lib)
# ✓ numpy (not num-py)
# ✓ plotly (not plot-ly)
# ✓ streamlit (not stream-lit)

# Verify package name:
pip search pandas  # Search PyPI
# Or visit: https://pypi.org/

# Correct installation:
pip install pandas
```

**Solution 3: Version Compatibility**

```powershell
# Check if specific version is required:
pip install pandas==2.0.0  # Specific version

# Or use compatible version:
pip install pandas>=1.5.0,<2.0.0

# Check what's installed:
pip show pandas
```

---

### 14. "ImportError" When Running Script

**Problem**: Module can't be imported during runtime.

**Solution 1: Check Python Path**

```powershell
# When running script, verify correct Python is used
python -c "import sys; print('\n'.join(sys.path))"

# Make sure venv's site-packages is listed
# Example: C:\Users\Arath\...\venv\Lib\site-packages
```

**Solution 2: Reinstall Package**

```powershell
# Reinstall the problematic package:
pip uninstall pandas -y
pip install pandas

# Or force reinstall:
pip install --force-reinstall --no-cache-dir pandas
```

**Solution 3: Check sys.path in Script**

```powershell
# Add debugging to your script:
import sys
print("Python executable:", sys.executable)
print("Python path:", sys.path)

# Run it:
python your_script.py

# Check if venv's site-packages is in the path
```

---

### 15. "pip install" Takes Forever

**Problem**: Package download is very slow.

**Solution 1: Use Different PyPI Mirror**

```powershell
# Default PyPI can be slow
# Use official mirror:
pip install -i https://pypi.org/simple/ package-name

# Or Aliyun mirror (fast in some regions):
pip install -i https://mirrors.aliyun.com/pypi/simple/ package-name

# Set permanently:
pip config set global.index-url https://pypi.org/simple/
```

**Solution 2: Install with Caching**

```powershell
# Use local cache of previously downloaded packages
pip install --no-cache-dir -r requirements.txt
# (This is sometimes slower, actually)

# Better: Keep cache
pip install -r requirements.txt
# Subsequent installs use cache
```

**Solution 3: Install Smaller Packages First**

```powershell
# Install critical packages first, then others
pip install numpy  # Small
pip install pandas  # Medium
pip install streamlit  # Larger

# Or check for dependency conflicts:
pip install pipdeptree -q
pipdeptree
```

---

### 16. "Conda vs Pip" Conflicts

**Problem**: Mixed conda and pip installs cause conflicts.

**Solution 1: Use Consistent Manager**

```powershell
# If using venv with pip:
pip install -r requirements.txt  # ONLY use pip

# If using Anaconda:
conda install --file requirements.txt  # Use conda
# Don't mix with pip

# Check what's installed:
pip list
conda list  # If using conda
```

**Solution 2: Identify Conflict**

```powershell
# Check conflicting packages:
pip check
# Lists any conflicts

# If found, reinstall affected package:
pip uninstall conflicting-package -y
pip install conflicting-package
```

**Solution 3: Fresh Environment**

```powershell
# Start over:
deactivate
Remove-Item -Recurse -Force venv
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Port and Network Issues

### 17. "Address already in use" / "Port 8501 in use"

**Problem**: Streamlit's port is already used by another process.

**Solution 1: Use Different Port**

```powershell
# Run Streamlit on different port:
streamlit run app.py --server.port 8502

# Or use another port:
streamlit run app.py --server.port 8503
```

**Solution 2: Find and Kill Process Using Port**

```powershell
# Find what's using port 8501:
netstat -ano | findstr :8501

# Output example:
# TCP    127.0.0.1:8501    0.0.0.0:0    LISTENING    12345

# Kill the process (where 12345 is the PID):
taskkill /PID 12345 /F

# Now try Streamlit again:
streamlit run app.py
```

**Solution 3: Find Available Port**

```powershell
# Find random available port:
$port = Get-Random -Minimum 8000 -Maximum 9000
Write-Host "Using port: $port"
streamlit run app.py --server.port $port
```

---

### 18. "Could not connect to localhost:8501"

**Problem**: Browser can't reach Streamlit server.

**Solution 1: Verify Server Is Running**

```powershell
# In Streamlit terminal, should see:
# Streamlit is running... URL: http://localhost:8501

# If not, check for errors above this message
# Look for red text or [error] messages
```

**Solution 2: Manually Open URL**

```powershell
# Copy the URL shown in terminal
# Paste into browser address bar:
http://localhost:8501

# If page loads, networking is fine (just wasn't opened automatically)
# If page doesn't load, proceed to Solution 3
```

**Solution 3: Check Firewall**

```powershell
# Windows Defender might be blocking localhost
# Check firewall:
Get-NetFirewallProfile | Select Name, Enabled

# Disable firewall temporarily (Admin PowerShell):
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False

# Test Streamlit again
# Re-enable firewall:
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True

# Or add exception (Admin):
New-NetFirewallRule -DisplayName "Allow Streamlit" -Direction Inbound -Program "C:\path\to\python.exe" -Action Allow
```

**Solution 4: Check 127.0.0.1 Specifically**

```powershell
# Try explicit IP instead of localhost:
http://127.0.0.1:8501

# If this works but localhost doesn't:
# Check hosts file (rarely an issue):
notepad C:\Windows\System32\drivers\etc\hosts
# Should contain: 127.0.0.1 localhost
```

---

### 19. "Network Error" when Loading Data from URL

**Problem**: Dashboard can't fetch data from online sources.

**Solution 1: Check Internet Connection**

```powershell
# Test connectivity:
ping google.com
ping github.com
ping waterservices.usgs.gov

# If ping fails, check internet connection
```

**Solution 2: Check Firewall/Proxy**

```powershell
# If behind corporate proxy, configure pip:
pip install -r requirements.txt --proxy [user:passwd@]proxy.server:port

# For Streamlit, may need to:
# Open Streamlit terminal
# Edit ~/.streamlit/config.toml:
notepad $env:USERPROFILE\.streamlit\config.toml

# Add:
[client]
gatherUsageStats = false
[server]
headless = true
```

**Solution 3: Disable SSL Verification (Temporary)**

```powershell
# In your Python script:
import requests
import urllib3

# For requests library:
requests.get(url, verify=False)

# Or disable globally (not recommended):
urllib3.disable_warnings()
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

---

### 20. "Connection Refused" on Port 8000/8501

**Problem**: Can't connect to development server.

**Solution 1: Verify Server Process**

```powershell
# Check if Python process is running:
Get-Process | grep python
# Or:
tasklist | findstr python

# If process running but connection refused:
# Might be binding to wrong IP address
```

**Solution 2: Force Bind to 0.0.0.0**

```powershell
# Edit your run script to bind to all interfaces:
streamlit run app.py --server.address 0.0.0.0

# Or for Flask/other frameworks:
# In your Python code:
app.run(host='0.0.0.0', port=8501)
```

**Solution 3: Check Hosts File**

```powershell
# Verify localhost resolves correctly:
nslookup localhost
ping localhost

# Expected output:
# ::1 (IPv6) or 127.0.0.1 (IPv4)
```

---

## File and Data Issues

### 21. "FileNotFoundError" / "No such file or directory"

**Problem**: Python script can't find data file.

**Solution 1: Check File Path Exists**

```powershell
# Verify file location:
dir "C:\Users\Arath\Automation_Station\Projects\Datathon\raw_data"

# Check if file exists:
Test-Path "C:\Users\Arath\Automation_Station\Projects\Datathon\raw_data\data.csv"
# Should return: True
```

**Solution 2: Use Absolute Path in Script**

```python
# In your Python code, use absolute Windows paths:
import os

# Instead of:
df = pd.read_csv('data.csv')  # WRONG - relative path

# Use:
filepath = r'C:\Users\Arath\Automation_Station\Projects\Datathon\raw_data\data.csv'
df = pd.read_csv(filepath)

# Or build path safely:
import pathlib
filepath = pathlib.Path(r'C:\Users\Arath\Automation_Station\Projects\Datathon\raw_data') / 'data.csv'
df = pd.read_csv(filepath)
```

**Solution 3: Use Raw String (r prefix)**

```python
# Backslashes in Windows paths need to be raw strings:
# DON'T:
path = 'C:\Users\Arath\...'  # \U and \A are escape sequences!

# DO:
path = r'C:\Users\Arath\...'  # Raw string, backslashes literal
df = pd.read_csv(path)
```

**Solution 4: Use Forward Slashes**

```python
# Python accepts forward slashes on Windows:
path = 'C:/Users/Arath/Automation_Station/Projects/Datathon/raw_data/data.csv'
df = pd.read_csv(path)
```

---

### 22. "CSV File Not Loading / Encoding Error"

**Problem**: CSV file shows encoding error or reads incorrectly.

**Solution 1: Specify Encoding**

```python
# If you get: UnicodeDecodeError

# Try UTF-8 explicitly:
df = pd.read_csv('data.csv', encoding='utf-8')

# If that fails, try other common encodings:
df = pd.read_csv('data.csv', encoding='latin-1')
df = pd.read_csv('data.csv', encoding='cp1252')  # Windows-1252
df = pd.read_csv('data.csv', encoding='iso-8859-1')

# Or let pandas detect:
df = pd.read_csv('data.csv', encoding='unicode_escape')
```

**Solution 2: Check File Actually Exists**

```python
import os
import pandas as pd

filepath = r'C:\Users\Arath\...\data.csv'

if os.path.exists(filepath):
    print(f"File found: {filepath}")
    print(f"File size: {os.path.getsize(filepath)} bytes")
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} rows")
else:
    print(f"File NOT found: {filepath}")
    print(f"Current dir: {os.getcwd()}")
    print(f"Files in current dir: {os.listdir('.')}")
```

**Solution 3: Handle Different Encodings Automatically**

```python
import chardet

# Detect file encoding:
with open('data.csv', 'rb') as f:
    result = chardet.detect(f.read(10000))
    encoding = result['encoding']

print(f"Detected encoding: {encoding}")
df = pd.read_csv('data.csv', encoding=encoding)
```

---

### 23. "CORS Error" when Loading Remote Data

**Problem**: JavaScript/Streamlit can't fetch data from external API.

**Solution 1: Check CORS Headers (Server-side)**

```python
# If you control the API, add CORS headers:
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def get_data():
    return {'data': [1, 2, 3]}
```

**Solution 2: Use CORS Proxy (Client-side)**

```python
# If API doesn't support CORS, use proxy:
import requests

# Instead of direct request:
# requests.get('https://api.example.com/data')

# Use proxy:
proxy_url = 'https://cors-anywhere.herokuapp.com/'
response = requests.get(proxy_url + 'https://api.example.com/data')
```

**Solution 3: Fetch Data Server-side**

```python
# In Streamlit app.py (server-side, no CORS issue):
import pandas as pd
import requests

@st.cache_data
def load_remote_data():
    response = requests.get('https://waterservices.usgs.gov/...')
    df = pd.read_json(response.json())
    return df

df = load_remote_data()
st.dataframe(df)
```

---

### 24. ".gitignore Not Working"

**Problem**: Files that should be ignored are being tracked.

**Solution 1: Remove Cached Files**

```powershell
# Files already committed won't be ignored by .gitignore
# Remove them from git tracking but keep local copy:

git rm --cached filename.txt
git rm --cached -r folder_name/

# Commit the removal:
git commit -m "Stop tracking filename.txt"
```

**Solution 2: Check .gitignore Syntax**

```powershell
# View your .gitignore:
Get-Content .gitignore

# Common patterns:
*.pyc              # Ignore all .pyc files
__pycache__/       # Ignore pycache folder
venv/              # Ignore virtual environment
.env               # Ignore environment file
*.log              # Ignore log files
data/raw/          # Ignore raw data folder
```

**Solution 3: Verify .gitignore Location**

```powershell
# .gitignore must be in repository root:
cd C:\Users\Arath\Automation_Station\Projects\Datathon\web

# Check if it exists:
Test-Path .gitignore
```

**Solution 4: Force Update .gitignore**

```powershell
# Clear git cache and reapply gitignore:
git rm -r --cached .
git add .
git commit -m "Update gitignore"
```

---

### 25. "Large File Upload Fails"

**Problem**: Can't upload file larger than size limit.

**Solution 1: Increase Streamlit Upload Limit**

```python
# In ~/.streamlit/config.toml:
[client]
maxUploadSize = 200  # MB

# Restart Streamlit app
```

**Solution 2: Use Git LFS for Large Files**

```powershell
# Install Git LFS:
git lfs install

# Track large files:
git lfs track "*.csv"
git add .gitattributes

# Now add large files:
git add large_file.csv
git commit -m "Add large data file"
```

**Solution 3: Split Large Files**

```python
# Instead of one large file, split it:
import pandas as pd

# Read in chunks:
df_chunks = pd.read_csv('large_file.csv', chunksize=10000)
for i, chunk in enumerate(df_chunks):
    chunk.to_csv(f'data_part_{i}.csv', index=False)

# Read back in app:
dfs = []
import glob
for file in glob.glob('data_part_*.csv'):
    dfs.append(pd.read_csv(file))
df = pd.concat(dfs, ignore_index=True)
```

---

## Streamlit Specific Issues

### 26. "Streamlit Run Fails with Error"

**Problem**: Streamlit app crashes on startup.

**Solution 1: Check Error Message**

```powershell
# Run with verbose output:
streamlit run app.py --logger.level=debug

# Carefully read the error traceback
# Usually shows exactly which line and what's wrong
```

**Solution 2: Test Imports**

```powershell
# Create test script to verify all imports:
# test_imports.py:
import streamlit as st
print("Streamlit OK")

import pandas as pd
print("Pandas OK")

import plotly.graph_objects as go
print("Plotly OK")

# Run test:
python test_imports.py
# All should print OK
```

**Solution 3: Start with Minimal App**

```python
# Create simple app.py to verify Streamlit works:
import streamlit as st

st.title("Test App")
st.write("If you see this, Streamlit works!")

# Run:
streamlit run app.py
```

Then gradually add complexity back.

---

### 27. "Streamlit App Reloads Constantly"

**Problem**: App refreshes repeatedly instead of staying stable.

**Solution 1: Check for Infinite Loops**

```python
# Common mistake - calling functions at top level:
# DON'T do this:
while True:
    data = load_data()
    st.dataframe(data)

# Instead, let Streamlit rerun on its own:
# DO this:
@st.cache_data
def load_data():
    return pd.read_csv('data.csv')

data = load_data()
st.dataframe(data)
```

**Solution 2: Disable Auto-rerun**

```python
# If your code has side effects:
import streamlit as st
from streamlit.script_run_context import get_script_run_context

# Prevent reruns:
if 'initialized' not in st.session_state:
    # Run initialization only once
    st.session_state.initialized = True
    expensive_operation()

# Now use cached result
result = st.session_state.result
st.write(result)
```

---

### 28. "Streamlit Cache Not Working"

**Problem**: Changes to data file aren't reflected until cache cleared.

**Solution 1: Clear Cache**

```python
# Add clear button in your app:
if st.button("Clear Cache"):
    st.cache_data.clear()
    st.rerun()

# Or from terminal:
streamlit cache clear
```

**Solution 2: Disable Caching (Development)**

```python
# During development, disable caching:
# command line:
streamlit run app.py --logger.level=debug

# Or in code:
import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed")

# For specific functions:
# DON'T use @st.cache_data during development
def load_data():  # No decorator
    return pd.read_csv('data.csv')
```

**Solution 3: Cache Key Issues**

```python
# If caching data with file path, include file mtime:
import os
from datetime import datetime

@st.cache_data
def load_data(filepath):
    # Make cache key unique when file changes
    mtime = os.path.getmtime(filepath)
    return pd.read_csv(filepath)

# Or use _hash_funcs:
@st.cache_data(hash_funcs={dict: lambda x: x})
def load_data(config_dict):
    return process_data(config_dict)
```

---

### 29. "Plotly Charts Won't Render"

**Problem**: Plotly charts show blank or error.

**Solution 1: Check Plotly Installation**

```powershell
pip show plotly
pip install --upgrade plotly
```

**Solution 2: Test Chart Rendering**

```python
import streamlit as st
import plotly.graph_objects as go

# Simple test chart:
fig = go.Figure(data=[go.Bar(y=[2, 3, 1])])
st.plotly_chart(fig)

# If this works, issue is with your data
```

**Solution 3: Check Data for Issues**

```python
import plotly.graph_objects as go
import pandas as pd

# Common issues:
df = pd.read_csv('data.csv')

# Check for NaN values:
print(df.isnull())

# Check data types:
print(df.dtypes)

# Check numeric columns actually contain numbers:
print(df['value_column'].dtype)

# If object type, convert:
df['value_column'] = pd.to_numeric(df['value_column'], errors='coerce')

# Now try chart:
fig = go.Figure()
fig.add_trace(go.Bar(x=df['x_col'], y=df['y_col']))
st.plotly_chart(fig)
```

---

## Git Repository Issues

### 30. "Merge Conflicts"

**Problem**: Git merge shows conflicts you must resolve.

**Solution 1: Understand Conflict Markers**

```python
# File will show markers like:
<<<<<<< HEAD
# Your current changes
# (local version)
=======
# Incoming changes
# (branch being merged)
>>>>>>> feature-branch
```

**Solution 2: Resolve Conflicts Manually**

```powershell
# 1. Open conflicted files:
code your_file.py
# or:
notepad your_file.py

# 2. Choose which version to keep:

# Option A: Keep your version:
# Delete everything from <<<<<<< to =======
# Delete everything from ======= to >>>>>>>
# Keep your code

# Option B: Keep their version:
# Delete everything from <<<<<<< to =======
# Delete everything from ======= to >>>>>>>
# Keep their code

# Option C: Keep both (if compatible):
# Delete markers, keep both versions of code

# 3. Save file

# 4. Complete merge:
git add your_file.py
git commit -m "Resolve merge conflicts"
```

**Solution 3: Use Mergetool (GUI)**

```powershell
# Configure mergetool (e.g., VS Code):
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Run mergetool:
git mergetool

# This opens your editor to resolve conflicts
```

---

### 31. "Branch Not Tracking Remote"

**Problem**: `git pull` says "no tracking information".

**Solution 1: Set Upstream Branch**

```powershell
# When first pushing new branch:
git push --set-upstream origin feature-branch

# Or:
git push -u origin feature-branch
```

**Solution 2: Set Tracking for Existing Branch**

```powershell
# If branch already exists on remote:
git branch --set-upstream-to=origin/feature-branch feature-branch

# Or:
git branch -u origin/feature-branch

# Verify:
git branch -vv
# Should show: feature-branch → origin/feature-branch
```

**Solution 3: Track Remote Branch Locally**

```powershell
# If branch exists on remote but not local:
git checkout --track origin/feature-branch

# Or:
git branch --track feature-branch origin/feature-branch
git checkout feature-branch
```

---

### 32. "Accidental Commit to Wrong Branch"

**Problem**: You committed to main instead of feature branch.

**Solution 1: Move Commit to New Branch**

```powershell
# Create new branch with the commit:
git branch feature-branch

# Reset main back to before commit:
git checkout main
git reset --hard HEAD~1

# Switch to feature branch:
git checkout feature-branch

# Now you have the commit on feature-branch
```

**Solution 2: Cherry-pick Commit**

```powershell
# If you already pushed to main:
git checkout feature-branch
git cherry-pick main

# Then reset main:
git checkout main
git reset --hard HEAD~1

# Force push (only if you control the repo):
git push --force-with-lease origin main
```

---

### 33. "Lost Commits / Deleted Branch"

**Problem**: Accidentally deleted branch or lost commits.

**Solution 1: Find Commit Hash**

```powershell
# View all commits you've made:
git reflog

# Find your commit hash
# Example output:
# a1b2c3d HEAD@{0}: reset: moving to HEAD~1
# e4f5g6h HEAD@{1}: commit: Fix bug

# Recover the commit:
git checkout e4f5g6h

# Create branch from it:
git checkout -b recovered-branch
```

**Solution 2: Restore Deleted Branch**

```powershell
# List all branches (deleted too):
git reflog show --all

# Find deleted branch:
git reflog show deleted-branch-name

# Restore it:
git checkout -b deleted-branch-name commit-hash
```

---

## Performance and Encoding Issues

### 34. "Slow App Performance"

**Problem**: Streamlit app is slow or freezes.

**Solution 1: Add Caching**

```python
import streamlit as st

# Cache data loading:
@st.cache_data
def load_data():
    return pd.read_csv('large_file.csv')

# Cache computations:
@st.cache_data
def process_data(df):
    return df.groupby('category').sum()

df = load_data()
processed = process_data(df)
st.dataframe(processed)
```

**Solution 2: Lazy Load / Pagination**

```python
# Instead of loading all data at once:
# DON'T:
df = pd.read_csv('huge_file.csv')  # Takes forever
st.dataframe(df)

# DO:
# Read in chunks:
chunk_size = 1000
page = st.number_input("Page:", 1)
df_chunk = pd.read_csv('huge_file.csv', skiprows=(page-1)*chunk_size, nrows=chunk_size)
st.dataframe(df_chunk)
```

**Solution 3: Profile Code**

```python
# Find slow spots:
import time

start = time.time()
data = load_data()
print(f"Load took {time.time() - start} seconds")

start = time.time()
result = process_data(data)
print(f"Process took {time.time() - start} seconds")
```

---

### 35. "Character Encoding Issues in Output"

**Problem**: Special characters display as ??? or mojibake.

**Solution 1: Ensure UTF-8 Encoding**

```python
# When reading files:
df = pd.read_csv('data.csv', encoding='utf-8')

# When writing files:
df.to_csv('output.csv', encoding='utf-8', index=False)

# In Python code (beginning of file):
# -*- coding: utf-8 -*-
```

**Solution 2: Handle Problematic Characters**

```python
import pandas as pd

# Read with error handling:
df = pd.read_csv('data.csv', encoding='utf-8', errors='replace')

# Clean up bad characters:
df = df.apply(lambda x: x.str.encode('utf-8', 'ignore').str.decode('utf-8') if isinstance(x, object) else x)

# Output with proper encoding:
df.to_csv('output.csv', encoding='utf-8', index=False)
```

---

### 36. "Antivirus Interfering with Development"

**Problem**: Antivirus slows down or blocks development.

**Solution 1: Add Project to Exclusions**

```
Most antivirus software (Avast, AVG, McAfee, Kaspersky, etc.):

1. Open antivirus settings
2. Find "Exclusions" or "Whitelist"
3. Add folder:
   C:\Users\Arath\Automation_Station\Projects\Datathon\web\
4. Add these extensions to ignore:
   .py, .pyc, .pyd, .so
5. Apply and restart
```

**Solution 2: Disable Scanning on Port**

```powershell
# Some antivirus blocks localhost
# Disable port scanning in antivirus settings:
# Typical options:
# - Network scanning: Off
# - Browser protection: Off (temporarily)
# - Sandbox: Off
```

**Solution 3: Use WSL Instead**

```powershell
# Windows Subsystem for Linux can bypass some antivirus issues:
wsl --install

# Then develop in WSL environment
# More info: docs.microsoft.com/windows/wsl
```

---

## IDE and Editor Issues

### 37. "VS Code Python Extension Issues"

**Problem**: VS Code doesn't recognize Python or packages.

**Solution 1: Select Python Interpreter**

```
1. Press Ctrl+Shift+`  (open terminal in VS Code)
2. Click on Python version in bottom right
3. Select "Enter interpreter path"
4. Browse to: C:\Users\Arath\Automation_Station\Projects\Datathon\web\venv\Scripts\python.exe
5. Reload VS Code
```

**Solution 2: Install Python Extension**

```
1. Click Extensions (left sidebar)
2. Search "Python"
3. Install "Python" by Microsoft
4. Reload VS Code
```

**Solution 3: Configure Linter**

```python
# Create .vscode/settings.json in your project:
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.pylintPath": "${workspaceFolder}/venv/Scripts/pylint.exe",
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true
}
```

---

### 38. "PyCharm Can't Find Modules"

**Problem**: PyCharm shows red squiggles for imports that work.

**Solution 1: Configure Python Interpreter**

```
1. File → Settings → Project → Python Interpreter
2. Click gear icon → Add
3. Select "Existing Environment"
4. Browse to: C:\Users\Arath\...\web\venv\Scripts\python.exe
5. Click OK
6. Reload project
```

**Solution 2: Invalidate Caches**

```
1. File → Invalidate Caches
2. Check "Clear VCS Log Caches" if available
3. Click "Invalidate and Restart"
4. Wait for PyCharm to restart and rebuild indexes
```

**Solution 3: Mark Source Folder**

```
1. Right-click src/ folder
2. Mark Directory as → Sources Root
3. Same for tests/ if you have it
```

---

## Summary

**Most Common Issues and Quick Fixes:**

| Issue | Quick Fix |
|-------|-----------|
| venv not active | `venv\Scripts\Activate.ps1` |
| Module not found | `pip install -r requirements.txt` |
| Port in use | `streamlit run app.py --server.port 8502` |
| Authentication failed | Use Personal Access Token from GitHub |
| File not found | Use full path: `r'C:\Users\...'` |
| Streamlit won't open | Check firewall: `Get-NetFirewallProfile` |
| Python not found | Add to PATH or use `py -3.11` launcher |
| Merge conflicts | Edit file, resolve manually, `git add .`, commit |

**When Stuck:**

1. Read the error message carefully - it usually says exactly what's wrong
2. Check this file for your specific error
3. Try Solution 1 (usually quickest)
4. If that doesn't work, try Solution 2 (more thorough)
5. If still stuck, try Solution 3 (nuclear option - fresh install)

**Need More Help?**

- GitHub issues: https://github.com/yourusername/datathon-water-analysis/issues
- Stack Overflow: Search error message with `[python]` or `[streamlit]` tags
- Official docs: https://docs.streamlit.io, https://pandas.pydata.org/, https://git-scm.com/doc
