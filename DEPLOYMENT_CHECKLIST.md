# ✅ Deployment Checklist
## datathon-water-analysis

Use this checklist to verify everything is ready before deploying to GitHub and Vercel.

---

## 🖥️ Local System Requirements

- [ ] Windows 10 or Windows 11
- [ ] Administrator access (for installations)
- [ ] Internet connection
- [ ] ~500 MB free disk space

---

## 📦 Software Installation

### Git
- [ ] Git installed (`git --version` shows version)
- [ ] Git configured with username: `git config --global user.name "Your Name"`
- [ ] Git configured with email: `git config --global user.email "your@email.com"`
- [ ] Can authenticate with GitHub (personal access token or SSH key)

### Node.js & npm
- [ ] Node.js 16+ installed (`node --version` shows version)
- [ ] npm 9+ installed (`npm --version` shows version)
- [ ] npm can install packages (`npm list -g` works)

### Python (optional, for static server)
- [ ] Python 3.8+ installed (`python --version` shows version)
- [ ] Python added to PATH (can run `python` from PowerShell anywhere)

### Code Editor (recommended)
- [ ] VS Code installed (or preferred editor)
- [ ] VS Code extensions: Live Server, Git Graph (optional)

---

## 📁 Project Files

### Project Location
- [ ] Project exists at: `C:\Users\Arath\Automation_Station\Projects\Datathon\web\`
- [ ] Folder is accessible and readable
- [ ] No special characters in file paths causing issues

### Required Root Files
- [ ] `index.html` exists (main dashboard)
- [ ] `.gitignore` exists
- [ ] `package.json` exists
- [ ] `vercel.json` exists
- [ ] `README.md` exists

### Data Folder
- [ ] `public/data/` folder exists
- [ ] `demands.csv` present (227 KB)
- [ ] `existing.csv` present (650 KB)
- [ ] `needs.csv` present (197 KB)
- [ ] `population.csv` present (224 KB)
- [ ] `strategies.csv` present (1.3 MB)
- [ ] All CSV files readable (not corrupted)

### Documentation Folder
- [ ] `docs/` folder exists
- [ ] At least 15+ markdown files present
- [ ] `METADATA.json` present and valid JSON
- [ ] `WINDOWS_QUICK_START.md` readable
- [ ] `SETUP_AND_DEPLOY.md` readable

---

## 🧪 Local Testing

### Dashboard Loads
- [ ] Run: `python -m http.server 8000`
- [ ] Open: `http://localhost:8000` in browser
- [ ] Dashboard appears without errors
- [ ] No CORS warnings in browser console (F12)
- [ ] Close server with Ctrl+C

### Interactive Features Work
- [ ] Region dropdown loads and can select regions
- [ ] WUG Type dropdown loads and has options
- [ ] Year input field accepts numbers
- [ ] Charts appear with data
- [ ] Hovering over charts shows tooltips
- [ ] Download CSV button works

### Data Files Load
- [ ] Browser console (F12) shows no "404 Not Found" errors
- [ ] All 5 CSV files are accessible
- [ ] Charts have data from CSV files
- [ ] No timeout errors loading data

---

## 🐙 GitHub Preparation

### GitHub Account
- [ ] Have active GitHub account
- [ ] Can access https://github.com/yourusername
- [ ] Have generated Personal Access Token (Settings → Developer Settings → Tokens)
- [ ] Token saved safely (you'll need it once)

### Repository Setup
- [ ] Ready to create new repository named `datathon-water-analysis`
- [ ] Planned to make it Public (not private)
- [ ] Plan to add: .gitignore, MIT License (already included)
- [ ] Have HTTPS clone URL ready to use

### Git Configuration
- [ ] Can run: `git status` (shows not a git repo yet - that's correct)
- [ ] Can run: `git --version` (shows version)
- [ ] Test git is working in target folder

---

## 🚀 Vercel Preparation

### Vercel Account
- [ ] Have Vercel account (or will create free one)
- [ ] Can access https://vercel.com/dashboard
- [ ] GitHub account connected to Vercel
- [ ] Vercel has permission to see your GitHub repositories

### Vercel Project
- [ ] Know your GitHub username (for verification URL)
- [ ] Plan for project name: `datathon-water-analysis`
- [ ] Understand auto-deploy works: push to main → auto-deploy
- [ ] Ready to wait 2-3 minutes for first deployment

---

## 📋 Pre-Deployment Steps (In Order)

### Step 1: Test Locally ✅
- [ ] Dashboard runs locally without errors
- [ ] All interactive features work
- [ ] Data loads correctly
- [ ] Browser console clean of errors

### Step 2: GitHub Repository ✅
- [ ] Created new repository at github.com/username/datathon-water-analysis
- [ ] Marked as Public
- [ ] Has description: "Interactive dashboard for Texas water crisis analysis"

### Step 3: Initialize Git Locally ✅
- [ ] Ran: `git init`
- [ ] Ran: `git add .`
- [ ] Ran: `git commit -m "Initial commit: Texas water analysis dashboard"`
- [ ] No errors in commit output

### Step 4: Connect to GitHub ✅
- [ ] Ran: `git branch -M main`
- [ ] Ran: `git remote add origin https://github.com/username/datathon-water-analysis.git`
- [ ] Ran: `git push -u origin main`
- [ ] Verification: Checked github.com/username/datathon-water-analysis shows files

### Step 5: Vercel Deployment ✅
- [ ] Logged into Vercel at vercel.com
- [ ] Created new project from GitHub repository
- [ ] Vercel connected to your GitHub account
- [ ] Selected datathon-water-analysis repository
- [ ] Clicked Deploy and waited for completion
- [ ] Got live URL: datathon-water-analysis.vercel.app

### Step 6: Verify Live Deployment ✅
- [ ] Opened live Vercel URL in browser
- [ ] Dashboard loads and displays correctly
- [ ] Filters work on live version
- [ ] Charts render with data
- [ ] Download button works
- [ ] No console errors (F12)

---

## 🔄 Post-Deployment

### Share with Partners
- [ ] Copied live Vercel URL
- [ ] Sent to project partners via email
- [ ] Partners can access dashboard
- [ ] Partners understand how to use filters and export

### Set Up Collaboration
- [ ] Added GitHub collaborators (if team contributing)
- [ ] Explained GitHub Issues for feedback
- [ ] Shared `docs/PARTNER_SHARING.md` with team
- [ ] Set up GitHub Discussions (optional)

### Document Everything
- [ ] GitHub repository links correctly
- [ ] All documentation readable in repo
- [ ] README.md displays correctly on GitHub
- [ ] Source links work (TWDB, USGS)

---

## 🆘 Troubleshooting Flags

If any of these apply, you have an issue to solve:

- [ ] Dashboard won't start locally → See WINDOWS_TROUBLESHOOTING.md
- [ ] Git command fails → Check WINDOWS_DETAILED_SETUP.md
- [ ] GitHub authentication fails → Use Personal Access Token instead of password
- [ ] Vercel deployment fails → Check vercel.json in root, check .gitignore isn't excluding files
- [ ] Charts don't appear → Check public/data/ folder has CSV files
- [ ] CORS errors → You're running from wrong location, check file paths
- [ ] Port 8000 already in use → Use different port: `python -m http.server 8001`

---

## ✅ Final Verification

After completing all steps:

- [ ] **Local**: Dashboard runs at `http://localhost:8000`
- [ ] **GitHub**: Code visible at `github.com/username/datathon-water-analysis`
- [ ] **Vercel**: Dashboard live at `datathon-water-analysis.vercel.app`
- [ ] **Sharing**: Live URL sent to project partners
- [ ] **Documentation**: All docs accessible in GitHub repo
- [ ] **Data**: All 5 CSV files accessible in both local and live versions

---

## 📊 Success Indicators

You've succeeded when:

✅ Local dashboard works perfectly
✅ GitHub repository shows all files
✅ Vercel deployment shows "Ready" status
✅ Live dashboard loads in browser
✅ All filters and charts work on live version
✅ Project partners can access and use dashboard
✅ CSV export works on live version
✅ TWDB and USGS links in footer work

---

## 🎉 You're Done!

Once all checkboxes are complete and success indicators met, your project is:
- ✅ Deployed to production
- ✅ Accessible to team members
- ✅ Ready for analysis and presentation
- ✅ Properly documented and credited

**Congratulations!**

---

## 📝 Notes

### Useful Commands Reference

```powershell
# Test local dashboard
python -m http.server 8000

# Check git status
git status

# View git log
git log --oneline

# Check what's staged
git diff --cached

# Undo last commit (if needed)
git reset --soft HEAD~1

# Check GitHub authentication
git credential approve
```

### File Locations (Windows)

```
Project:  C:\Users\Arath\Automation_Station\Projects\Datathon\web\
Data:     C:\Users\Arath\Automation_Station\Projects\Datathon\web\public\data\
Docs:     C:\Users\Arath\Automation_Station\Projects\Datathon\web\docs\
```

### URLs to Have Ready

```
GitHub Account:   https://github.com/your-username
GitHub Repo:      https://github.com/your-username/datathon-water-analysis
Vercel Dashboard: https://vercel.com/dashboard
Live Dashboard:   https://datathon-water-analysis.vercel.app
```

---

**Date Created**: February 8, 2025
**Last Updated**: February 8, 2025
**Status**: Ready for Use

👉 **Next Step**: Follow `SETUP_AND_DEPLOY.md`
