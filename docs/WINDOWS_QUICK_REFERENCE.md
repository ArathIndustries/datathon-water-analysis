# Windows Quick Reference - One-Page Cheat Sheet

Essential commands and shortcuts for Windows development with Datathon project.

---

## Essential Git Commands

```powershell
# Clone repository
git clone https://github.com/yourusername/datathon-water-analysis.git

# Check status
git status

# View recent commits
git log --oneline -10
git log --all --graph --oneline

# Stage files
git add file1.py file2.py          # Stage specific files
git add .                           # Stage all changes

# Commit
git commit -m "Your message here"
git commit -am "Message"            # Stage + commit tracked files

# Push/Pull
git push origin main                # Push to remote
git pull origin main                # Pull from remote

# Branches
git branch                          # List local branches
git branch -a                       # List all branches
git checkout -b feature-name        # Create new branch
git checkout main                   # Switch branches
git branch -d feature-name          # Delete local branch
git push origin --delete feature-name  # Delete remote branch

# Merge
git merge feature-name              # Merge branch to current
git merge --abort                   # Abort merge if conflicts

# Undo changes
git diff                            # Show unstaged changes
git diff --staged                   # Show staged changes
git reset file.py                   # Unstage file
git reset --soft HEAD~1             # Undo last commit (keep changes)
git reset --hard HEAD~1             # Undo last commit (discard changes)

# Compare branches
git diff main feature-name

# Stash (temporary save)
git stash                           # Save work without committing
git stash list
git stash pop                       # Restore stashed work

# Configure
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
git config --global credential.helper wincred
```

---

## Essential npm Commands

```powershell
# Install dependencies
npm install                         # Install from package.json
npm install package-name            # Install specific package
npm install package@1.2.3           # Install specific version
npm install -g package-name         # Install globally

# Development
npm start                           # Start development server
npm run build                       # Build for production
npm test                            # Run tests
npm run dev                         # Development mode

# Package management
npm list                            # Show installed packages
npm list -g --depth=0              # Show global packages
npm update                          # Update all packages
npm update package-name             # Update specific package

# Cleanup
npm uninstall package-name          # Remove package
npm cache clean --force             # Clear npm cache

# Info
npm info package-name               # Show package details
npm view package-name versions      # Show all versions

# Security
npm audit                           # Check for vulnerabilities
npm audit fix                       # Fix vulnerabilities

# Version management
npm version patch                   # Bump patch version
npm version minor                   # Bump minor version
npm version major                   # Bump major version
```

---

## Essential Python Commands

```powershell
# Virtual environment
python -m venv venv                 # Create venv
venv\Scripts\Activate.ps1          # Activate (PowerShell)
venv\Scripts\activate.bat           # Activate (Command Prompt)
deactivate                          # Deactivate

# Pip
pip install -r requirements.txt     # Install dependencies
pip install package-name            # Install package
pip install package==1.2.3         # Install specific version
pip install --upgrade pip           # Upgrade pip
pip list                            # Show installed packages
pip show package-name               # Show package info
pip uninstall package-name          # Remove package

# Create requirements
pip freeze > requirements.txt       # Export current environment

# Check package version
python -c "import pandas; print(pandas.__version__)"

# Run scripts
python script.py                    # Run Python file
python -m module_name              # Run as module

# Interactive
python                              # Start Python shell
quit() or Ctrl+Z, Enter             # Exit Python shell

# Check Python info
python --version
python -c "import sys; print(sys.executable)"
python -c "import sys; print('\n'.join(sys.path))"
```

---

## Streamlit Commands

```powershell
# Run app
streamlit run app.py                # Run on default port 8501
streamlit run app.py --server.port 8502  # Custom port
streamlit run app.py --logger.level debug # Debug mode

# Cache
streamlit cache clear               # Clear all cache

# Config
streamlit config show               # Show config
streamlit config locations          # Show config file locations
```

---

## Common File Paths (Windows Format)

```
Project Root:
C:\Users\Arath\Automation_Station\Projects\Datathon\web\

Key Directories:
C:\Users\Arath\Automation_Station\Projects\Datathon\web\docs\
C:\Users\Arath\Automation_Station\Projects\Datathon\web\src\
C:\Users\Arath\Automation_Station\Projects\Datathon\web\data\
C:\Users\Arath\Automation_Station\Projects\Datathon\raw_data\
C:\Users\Arath\Automation_Station\Projects\Datathon\processed_data\

Virtual Environment:
C:\Users\Arath\Automation_Station\Projects\Datathon\web\venv\Scripts\python.exe

Python executable:
C:\Users\Arath\AppData\Local\Programs\Python\Python311\python.exe

pip executable:
C:\Users\Arath\Automation_Station\Projects\Datathon\web\venv\Scripts\pip.exe

Data Files:
C:\Users\Arath\Automation_Station\Projects\Datathon\raw_data\*.csv
C:\Users\Arath\Automation_Station\Projects\Datathon\processed_data\*.csv

Home Directory:
C:\Users\Arath\
~\ (in PowerShell)

Config Files:
~\.streamlit\config.toml
~\.gitconfig
~\.ssh\id_ed25519.pub
```

**Tip**: Use `r'path'` (raw string) or `C:/path/to/file` in Python to avoid backslash issues.

---

## Port Mapping and Localhost

```
Streamlit default:        http://localhost:8501
Alternative Streamlit:    http://localhost:8502, 8503, ...
Flask default:            http://localhost:5000
Django default:           http://localhost:8000

Access by IP:
127.0.0.1:8501           (IPv4 loopback)
[::1]:8501               (IPv6 loopback)

Check what's using a port:
netstat -ano | findstr :8501

Kill process using port:
taskkill /PID 12345 /F
```

---

## Environment Variables

### Check Environment Variables

```powershell
# View all environment variables
Get-ChildItem env:

# Check specific variable
$env:PATH
$env:PYTHON_HOME
$env:USERNAME

# Check if command is in PATH
Get-Command python
Get-Command git
Get-Command node
```

### Set Environment Variables (Temporary - Current Session)

```powershell
$env:MYVAR = "value"
echo $env:MYVAR
```

### Set Environment Variables (Permanent - User Level)

```powershell
# Via PowerShell (Admin):
[Environment]::SetEnvironmentVariable("MYVAR", "value", "User")

# Or via GUI:
# Settings → System → About → Advanced system settings
# → Environment Variables → New User Variable
# Name: MYVAR
# Value: value
# Click OK and restart applications
```

### Common Environment Variables to Check

```powershell
$env:PATH           # Executable paths
$env:PYTHON_HOME    # Python installation
$env:USERNAME       # Current user
$env:USERPROFILE    # User home directory
$env:TEMP           # Temp folder
$env:OS             # Windows
```

---

## Keyboard Shortcuts

### PowerShell / Command Prompt

```
Ctrl+C              Stop current command
Ctrl+Z, Enter       Exit Python shell
Ctrl+L              Clear screen (or: cls)
Up Arrow            Previous command
Down Arrow          Next command
Tab                 Auto-complete
Ctrl+A              Select all text
Ctrl+V              Paste
Ctrl+C              Copy
```

### VS Code

```
Ctrl+`              Open/close terminal
Ctrl+Shift+`        New terminal
Ctrl+J              Toggle terminal
Ctrl+Alt+L          Format document
Ctrl+/              Toggle comment
Ctrl+H              Replace in files
Ctrl+Shift+F        Find in files
Ctrl+B              Toggle sidebar
Ctrl+Shift+D        Debug panel
F5                  Start debugging
Shift+F10           Run file
Ctrl+K Ctrl+0       Fold all regions
Ctrl+K Ctrl+J       Unfold all regions
```

### PyCharm

```
Ctrl+Alt+L          Format code
Ctrl+/              Toggle comment
Alt+Enter           Quick fix suggestions
Ctrl+Shift+F        Find in files
Ctrl+H              Replace in files
F2                  Go to next error
Shift+F10           Run selected configuration
Ctrl+Shift+D        Debug selected configuration
Ctrl+Shift+A        Find action
Ctrl+E              Recent files
Ctrl+N              Go to class
Ctrl+Shift+N        Go to file
```

### GitHub Desktop

```
Ctrl+Alt+G          Open repository in Explorer
Ctrl+1              Show history
Ctrl+2              Show changes
Ctrl+,              Open settings
Ctrl+Shift+N        Create new repository
Ctrl+Shift+O        Clone repository
```

---

## Where to Find Logs and Error Messages

### Streamlit Logs

```
Location (Windows):
~\.streamlit\logs\

View in terminal (running):
Terminal where you typed: streamlit run app.py
Shows all output and errors

Recent errors:
~\.streamlit\logger.log
```

### Python/pip Errors

```
In PowerShell terminal:
When you run: python script.py or pip install
Errors appear in terminal immediately

Debug with:
python -m pdb script.py          # Python debugger
python -c "import module_name"   # Test import
```

### Git Errors

```
In PowerShell terminal:
When you run: git commands
Errors and warnings appear immediately

Verbose output:
git -c core.askpass=echo clone https://...
```

### Node.js/npm Errors

```
In PowerShell terminal:
When you run: npm commands
Errors appear immediately

Detailed output:
npm install --verbose
npm install --loglevel verbose
```

### Windows Event Viewer (System Errors)

```
Right-click Start → Computer Management
→ Event Viewer → Windows Logs → Application
Shows system-level errors from applications
```

### Application Logs Directory

```
Temporary files:
C:\Users\Arath\AppData\Local\Temp

Python packages:
C:\Users\Arath\Automation_Station\Projects\Datathon\web\venv\Lib\site-packages

Cache:
C:\Users\Arath\AppData\Local\pip\cache
```

---

## PowerShell Tips and Tricks

```powershell
# Get help
Get-Help command-name
help dir
help ls

# Find command
Get-Command *keyword*
Get-Command *python*

# Search command history
(Get-History) | Where-Object { $_.CommandLine -like "*git*" }

# Measure command execution time
Measure-Command { command-here }

# Run command as administrator
Start-Process -Verb RunAs cmd.exe

# Change execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Check execution policy
Get-ExecutionPolicy

# View file contents
Get-Content filename.txt
type filename.txt

# Count files
(ls).Count

# Find file by name
Get-ChildItem -Recurse -Filter "*name*"

# Delete files matching pattern
Get-ChildItem -Filter "*.log" -Recurse | Remove-Item

# Check directory size
(Get-ChildItem -Recurse | Measure-Object -Property Length -Sum).Sum / 1MB

# Rename multiple files
Get-ChildItem *.txt | Rename-Item -NewName { $_.name -replace ".txt", ".bak" }
```

---

## Copy-Paste Quick Setup (From Scratch)

```powershell
# Step 1: Navigate to projects folder
cd C:\Users\Arath\Automation_Station\Projects

# Step 2: Clone
git clone https://github.com/yourusername/datathon-water-analysis.git
cd datathon-water-analysis\web

# Step 3: Create and activate venv
python -m venv venv
venv\Scripts\Activate.ps1

# Step 4: Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Step 5: Run
streamlit run app.py

# Browser opens automatically to http://localhost:8501
```

---

## Debugging Checklist

When something doesn't work:

```
□ Is venv activated? (Look for "(venv)" in prompt)
□ Are you in the right directory? (cd C:\Users\Arath\...\web)
□ Did you install requirements? (pip list | grep streamlit)
□ Is Python the right version? (python --version, need 3.8+)
□ Is Git configured? (git config --global --list)
□ Check internet connection? (ping google.com)
□ Is antivirus blocking? (Check firewall)
□ Is port in use? (netstat -ano | findstr :8501)
□ Read error message carefully? (scroll up in terminal)
□ Try clearing cache? (streamlit cache clear)
□ Restart terminal? (Close and reopen PowerShell)
□ Check documentation? (README.md, config.json)
```

---

## File Structure Reference

```
C:\Users\Arath\Automation_Station\Projects\Datathon\
│
├── web\                          ← Main project folder
│   ├── docs\                      ← Documentation
│   │   ├── WINDOWS_QUICK_START.md
│   │   ├── WINDOWS_DETAILED_SETUP.md
│   │   ├── WINDOWS_TROUBLESHOOTING.md
│   │   └── WINDOWS_QUICK_REFERENCE.md (YOU ARE HERE)
│   ├── src\                       ← Python source code
│   │   ├── data_processing.py
│   │   ├── visualization.py
│   │   └── utils.py
│   ├── data\                      ← Data folder
│   │   ├── raw\
│   │   └── processed\
│   ├── notebooks\                 ← Jupyter notebooks
│   ├── dashboards\                ← HTML dashboards
│   ├── venv\                      ← Virtual environment (you create this)
│   ├── app.py                     ← Main Streamlit app
│   ├── package.json               ← Node dependencies
│   ├── requirements.txt           ← Python dependencies
│   ├── config.json                ← Configuration
│   ├── index.html                 ← Static dashboard
│   ├── README.md                  ← Main documentation
│   └── .gitignore                 ← Git ignore rules
│
├── raw_data\                      ← Raw data files
├── processed_data\                ← Processed data
├── notebooks\                     ← Analysis notebooks
├── phases\                        ← Project phases
└── analysis\                      ← Analysis results
```

---

## Quick Fixes (Copy-Paste Ready)

```powershell
# Python not found
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Port in use
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Upgrade pip
python -m pip install --upgrade pip

# Fix virtual environment
Remove-Item -Recurse -Force venv
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Clear Streamlit cache
streamlit cache clear

# Find Python executable
python -c "import sys; print(sys.executable)"

# Check installed packages
pip list | grep streamlit

# Reset git credentials
git config --global --unset credential.helper

# Fix line endings
git config --global core.autocrlf true
git rm --cached -r .
git reset --hard HEAD
```

---

## Important Reminders

```
✓ Always activate venv before working: venv\Scripts\Activate.ps1
✓ Use raw strings in Python paths: r'C:\path\to\file'
✓ Restart terminal after installing tools
✓ Check WINDOWS_TROUBLESHOOTING.md for help
✓ Read error messages carefully - they tell you exactly what's wrong
✓ Keep backups before major operations
✓ Use commit messages that describe what changed
✓ Don't share .env files with passwords/tokens
```

---

## Getting Help

**Can't find something here?**

1. See **WINDOWS_QUICK_START.md** for 5-minute setup
2. See **WINDOWS_DETAILED_SETUP.md** for comprehensive guide
3. See **WINDOWS_TROUBLESHOOTING.md** for 50+ problem/solution pairs
4. Check main **README.md** for project overview
5. Search error in Google: `"error message" python streamlit windows`
6. Check Stack Overflow: Tag your question `[python]` `[streamlit]` `[windows]`

---

**Last Updated**: 2026-02-08
**For**: Datathon Water Analysis Project
**Windows**: 10/11, PowerShell recommended
