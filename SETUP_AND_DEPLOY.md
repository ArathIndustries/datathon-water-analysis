# Complete Setup & Deployment Guide
## datathon-water-analysis Project

> **Time**: 30-45 minutes total
> **Target**: Windows 10/11 users
> **Goal**: Set up local project, push to GitHub, and deploy to Vercel

---

## 📋 Quick Overview

This guide will walk you through:
1. **Local Setup** - Get project running on your Windows machine
2. **GitHub** - Create repository and push code
3. **Vercel** - Deploy live dashboard for project partners
4. **Sharing** - Share live URL with team

**What you'll have after this:**
- ✅ Local project folder with all code and data
- ✅ GitHub repository for version control and collaboration
- ✅ Live dashboard at `datathon-water-analysis.vercel.app`
- ✅ Sharable link for project partners

---

## 🖥️ Step 1: Local Setup (10 minutes)

### 1.1 Install Prerequisites

**If you haven't already, install these once:**

1. **Git** - https://git-scm.com/download/win
   - Download and run installer
   - Accept defaults during installation
   - Verify: Open PowerShell and type `git --version`

2. **Node.js** - https://nodejs.org/ (Choose LTS)
   - Download and run installer
   - Accept defaults
   - Verify: Open PowerShell and type `node --version`

3. **Python 3.9+** - https://www.python.org/downloads/
   - Download latest Python 3.11+
   - **IMPORTANT**: Check "Add Python to PATH" during installation
   - Verify: `python --version`

### 1.2 Clone the Project (from Current Location)

Your project is already in:
```
C:\Users\Arath\Automation_Station\Projects\Datathon\web\
```

This folder contains:
- `index.html` - Static HTML dashboard
- `public/data/` - TWDB CSV files (demands, existing, needs, population, strategies)
- `docs/` - All documentation files
- `.gitignore`, `package.json`, `vercel.json` - Configuration files

**No need to clone yet** - you already have the files locally!

### 1.3 Test the Dashboard Locally

Open PowerShell and navigate to your project:

```powershell
cd C:\Users\Arath\Automation_Station\Projects\Datathon\web
```

**Option A: Use Python's built-in server**
```powershell
python -m http.server 8000
```

Then open your browser and go to: `http://localhost:8000`

The dashboard should load with:
- Interactive Plotly charts
- Region and WUG type filters
- Real-time data visualization
- Download buttons for CSV export

**Press Ctrl+C to stop the server**

**Option B: Use Node.js (if npm installed)**
```powershell
npx http-server -p 8000
```

✅ If the dashboard loads and charts appear, you're ready for GitHub!

---

## 🐙 Step 2: GitHub Setup (10 minutes)

### 2.1 Create GitHub Repository

1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `datathon-water-analysis`
   - **Description**: `Interactive dashboard for Texas water crisis analysis and infrastructure viability forecasting`
   - **Visibility**: `Public` (so project partners can view)
   - **Add .gitignore**: Already included in your project
   - Click **Create repository**

3. You'll see instructions. Copy the HTTPS link (looks like):
   ```
   https://github.com/YOUR-USERNAME/datathon-water-analysis.git
   ```

### 2.2 Initialize Git Locally

Open PowerShell in your project folder:

```powershell
cd C:\Users\Arath\Automation_Station\Projects\Datathon\web
```

Configure Git (first time only):
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Initialize the repository:
```powershell
git init
```

Add all files:
```powershell
git add .
```

Create initial commit:
```powershell
git commit -m "Initial commit: Texas water analysis dashboard with TWDB data"
```

### 2.3 Connect to GitHub and Push

Replace `YOUR-USERNAME` with your GitHub username:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/datathon-water-analysis.git
git push -u origin main
```

When prompted, enter your GitHub credentials.

✅ Your code is now on GitHub! Go to your repository to verify.

---

## 🚀 Step 3: Vercel Deployment (10 minutes)

### 3.1 Create Vercel Account

1. Go to https://vercel.com/signup
2. Click "Continue with GitHub"
3. Authorize Vercel to access your GitHub account
4. Complete setup by verifying email

### 3.2 Deploy from GitHub

1. After login, click **"Add New..."** → **"Project"**
2. You should see your `datathon-water-analysis` repository
3. Click **Import**
4. Vercel detects it's a static site - keep defaults
5. Click **Deploy**

Vercel will:
- Clone your repository
- Build the project
- Deploy to `datathon-water-analysis.vercel.app`
- Show you a live URL

⏳ **Wait 2-3 minutes** for deployment to complete.

✅ Once complete, open the URL and verify the dashboard loads!

### 3.3 (Optional) Configure Custom Domain

If you want a custom domain instead of vercel.app:

1. In Vercel dashboard, go to your project
2. Click **Settings** → **Domains**
3. Add your custom domain
4. Follow DNS instructions for your domain provider

---

## 📤 Step 4: Share with Project Partners (5 minutes)

### 4.1 Get Your Live Dashboard URL

From Vercel dashboard:
- Go to your project
- Copy the URL (top of page, looks like: `https://datathon-water-analysis.vercel.app`)

### 4.2 Share with Partners

Email them:
```
Hi team,

Our Texas Water Crisis Analysis dashboard is now live!

📊 View Dashboard: https://datathon-water-analysis.vercel.app

Features:
- Interactive TWDB data visualization
- Filter by region and WUG type
- 50-year demand projections (2020-2070)
- Download data as CSV
- Full source attribution

GitHub Repository (for technical details):
https://github.com/YOUR-USERNAME/datathon-water-analysis

Questions? See PARTNER_SHARING.md for more info.
```

### 4.3 Add Collaborators

If partners want to contribute:

1. Go to GitHub repository Settings → **Collaborators**
2. Click **Add people**
3. Search for their GitHub username
4. Choose permission level (usually "Maintain" for contributors)

---

## 🔄 Making Updates

### When You Update Code:

1. Make changes to files in your local folder
2. Test locally: `python -m http.server 8000`
3. Commit changes:
   ```powershell
   git add .
   git commit -m "Update: describe your change"
   git push origin main
   ```
4. Vercel automatically deploys! ✅

### When You Update Data:

1. Replace CSV files in `public/data/`
2. Commit and push
3. Vercel auto-deploys with new data
4. Dashboard reflects changes immediately

---

## 📚 Documentation Structure

Your project includes comprehensive documentation:

### For Getting Started:
- `WINDOWS_QUICK_START.md` - 5-minute setup
- `WINDOWS_DETAILED_SETUP.md` - Comprehensive guide
- `WINDOWS_QUICK_REFERENCE.md` - Command cheat sheet

### For Deployment:
- `GITHUB_SETUP.md` - GitHub step-by-step
- `VERCEL_DEPLOYMENT.md` - Vercel configuration
- `GITHUB_VERCEL_INTEGRATED_WORKFLOW.md` - Full workflow

### For Sharing:
- `PARTNER_SHARING.md` - Partner onboarding guide
- `README.md` - Project overview (in root)

### For Understanding Data:
- `docs/DATA_DICTIONARY.md` - Field documentation
- `docs/SOURCES.md` - Where data came from
- `docs/METADATA.json` - Machine-readable metadata

### For Development:
- `docs/ARCHITECTURE.md` - System design
- `docs/SETUP_LOCAL.md` - Local development
- `docs/PUBLIC_README.md` - Frontend documentation

---

## ✅ Verification Checklist

After completing all steps, verify:

- [ ] Local dashboard runs at `http://localhost:8000`
- [ ] Charts load and are interactive
- [ ] Data filters work (Region, WUG Type, Year)
- [ ] CSV export button works
- [ ] GitHub repository exists with all files
- [ ] Vercel deployment shows "Ready" status
- [ ] Live URL opens without errors
- [ ] Charts render on live dashboard
- [ ] Vercel auto-deploys when you push to GitHub

---

## 🆘 Troubleshooting

### Dashboard won't load locally
```powershell
# Make sure you're in the right directory
cd C:\Users\Arath\Automation_Station\Projects\Datathon\web

# Try a different port
python -m http.server 8001

# Check firewall isn't blocking port
```

### Git authentication fails
- Use personal access token instead of password:
  - GitHub → Settings → Developer Settings → Personal Access Tokens
  - Create new token with `repo` scope
  - Use token as password when prompted

### Vercel deployment fails
- Check `vercel.json` is in root folder
- Verify `public/` folder structure is correct
- Check .gitignore isn't excluding important files
- See `docs/VERCEL_DEPLOYMENT.md` for detailed troubleshooting

### Charts don't appear on live dashboard
- Check `public/data/` folder has CSV files
- Verify file paths in `index.html` match your folder structure
- Check browser console for errors (F12 in browser)
- See `docs/PUBLIC_README.md` for technical details

---

## 📞 Next Steps

1. **Get feedback** - Share live URL with project partners
2. **Document findings** - Use the dashboard to present analysis
3. **Add features** - Check `docs/ARCHITECTURE.md` for customization
4. **Cite properly** - Use `docs/CITATIONS.md` format for papers
5. **Update data** - Replace CSVs in `public/data/` as needed

---

## 📖 For More Information

| Topic | File |
|-------|------|
| Windows setup issues | `WINDOWS_TROUBLESHOOTING.md` |
| Project structure | `docs/ARCHITECTURE.md` |
| Data sources | `docs/SOURCES.md` |
| How to update data | `docs/DATA_DICTIONARY.md` |
| Partner collaboration | `PARTNER_SHARING.md` |
| Local development | `docs/SETUP_LOCAL.md` |

---

## 🎉 You're Done!

Your Texas Water Crisis Analysis dashboard is now:
- ✅ Running locally
- ✅ On GitHub
- ✅ Deployed to Vercel
- ✅ Shared with partners

Congratulations! You've created a research-grade data analysis project with professional deployment infrastructure.

---

**Questions?** Check the docs folder or reach out to your team.

**Last Updated**: February 8, 2025
