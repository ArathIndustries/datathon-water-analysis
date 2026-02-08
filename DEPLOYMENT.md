# Datathon Water Analysis - Deployment Guide

This guide provides step-by-step instructions for deploying the interactive Texas water crisis analysis dashboard to production using Vercel and GitHub.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [GitHub Setup](#github-setup)
3. [Vercel Deployment](#vercel-deployment)
4. [Environment Variables](#environment-variables)
5. [Custom Domain Configuration](#custom-domain-configuration)
6. [Monitoring and Logs](#monitoring-and-logs)
7. [Rollback Procedures](#rollback-procedures)
8. [Platform-Specific Instructions](#platform-specific-instructions)
9. [Troubleshooting](#troubleshooting)
10. [CI/CD with GitHub Actions](#cicd-with-github-actions)

---

## Prerequisites

Before deploying, ensure you have the following:

### Required Accounts
- **GitHub Account** - Free account at https://github.com
- **Vercel Account** - Free account at https://vercel.com (sign up with GitHub for easier integration)
- **Git** - Version control system installed locally

### Required Software
- Git (v2.30+) - https://git-scm.com/download
- Node.js (v18.0.0+) - https://nodejs.org
- npm (v9.0.0+) - Included with Node.js

### Verify Installation
```bash
# Check Git version
git --version

# Check Node.js version
node --version

# Check npm version
npm --version
```

---

## GitHub Setup

### Step 1: Create a GitHub Repository

1. Go to https://github.com/new
2. Repository name: `datathon-water-analysis`
3. Description: `Interactive dashboard for Texas water crisis analysis`
4. Choose visibility: **Public** (recommended for portfolio/educational projects)
5. Initialize with README: Optional (we'll add our own)
6. Click **Create repository**

### Step 2: Clone the Repository Locally

**macOS/Linux:**
```bash
cd ~/Projects
git clone https://github.com/YOUR_USERNAME/datathon-water-analysis.git
cd datathon-water-analysis
```

**Windows (PowerShell):**
```powershell
cd $env:USERPROFILE\Projects
git clone https://github.com/YOUR_USERNAME/datathon-water-analysis.git
cd datathon-water-analysis
```

**Windows (Git Bash):**
```bash
cd ~/Projects
git clone https://github.com/YOUR_USERNAME/datathon-water-analysis.git
cd datathon-water-analysis
```

### Step 3: Configure Git User (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 4: Add Project Files

Copy all project files to the repository directory:

**macOS/Linux:**
```bash
# Copy HTML, CSS, JS files
cp /Volumes/Arath/Automation_Station/Projects/Datathon/web/* .
```

**Windows (PowerShell):**
```powershell
# Copy files from source
Copy-Item 'D:\Automation_Station\Projects\Datathon\web\*' -Destination '.' -Recurse
```

**Windows (Git Bash):**
```bash
cp /c/Volumes/Arath/Automation_Station/Projects/Datathon/web/* .
```

### Step 5: Commit and Push

```bash
# Check status
git status

# Stage all files
git add .

# Commit with message
git commit -m "Initial commit: Water analysis dashboard with Vercel configuration"

# Push to GitHub (main branch)
git branch -M main
git push -u origin main
```

**Windows PowerShell equivalent:**
```powershell
git status
git add .
git commit -m "Initial commit: Water analysis dashboard with Vercel configuration"
git branch -M main
git push -u origin main
```

---

## Vercel Deployment

### Step 1: Sign Up / Log In to Vercel

1. Go to https://vercel.com/signup
2. Click **Continue with GitHub**
3. Authorize Vercel to access your GitHub account
4. Complete the signup process

### Step 2: Import Your Repository

1. In Vercel dashboard, click **Add New...** → **Project**
2. Find and select your `datathon-water-analysis` repository
3. Click **Import**

### Step 3: Configure Project Settings

**Build and Output Settings:**
- Framework Preset: Select **Other** (Static Site)
- Build Command: (leave empty - no build needed)
- Output Directory: (leave empty)
- Install Command: (leave empty)

**Environment Variables:**
- Since this is a static site, no environment variables are required
- However, if you plan to add API endpoints later, configure them here

Click **Deploy**

### Step 4: Deployment Confirmation

Vercel will:
1. Clone your repository
2. Deploy the files
3. Generate a unique URL (e.g., `https://datathon-water-analysis.vercel.app`)
4. Show deployment progress and logs

Once deployment is complete (indicated by green checkmark), your site is live!

---

## Environment Variables

### For Static Site
No environment variables are required for this static project. The site works with hardcoded paths to data files and CDN-hosted libraries.

### For Future API Integration
If you add backend functionality, configure variables in Vercel:

1. Project → Settings → Environment Variables
2. Add your variables for:
   - API endpoint URLs
   - Authentication tokens
   - Data source credentials
   - etc.

**Important:** Never commit `.env` files to Git. Always add them to `.gitignore` (already configured).

---

## Custom Domain Configuration

### Point a Custom Domain to Vercel

1. **In Vercel Dashboard:**
   - Go to Project Settings → Domains
   - Click **Add Domain**
   - Enter your domain (e.g., `wateranalysis.example.com`)

2. **DNS Configuration (varies by registrar):**

   **If using Vercel Nameservers (Easiest):**
   - Vercel will provide 2 nameserver addresses
   - Update nameservers at your domain registrar
   - Wait 24-48 hours for propagation

   **If using CNAME record:**
   - Create CNAME record pointing to `cname.vercel.com`
   - TTL: 3600 (1 hour) or as recommended by your registrar

3. **Verify Domain:**
   - Check status in Vercel dashboard
   - Once verified, your site is accessible at your custom domain

### Example DNS Records

**Nameserver approach (recommended):**
```
Nameserver 1: ns1.vercel-dns.com
Nameserver 2: ns2.vercel-dns.com
```

**CNAME approach:**
```
Type:   CNAME
Name:   wateranalysis
Value:  cname.vercel.com
TTL:    3600
```

---

## Monitoring and Logs

### Access Deployment Logs

1. **In Vercel Dashboard:**
   - Select your project
   - Click **Deployments**
   - Click a deployment to view logs

2. **View Real-Time Logs:**
   ```bash
   vercel logs --follow
   ```

### Monitor Site Performance

1. Go to Project → Analytics
2. View metrics:
   - Page load times
   - Error rates
   - Geography distribution
   - Browser/device breakdown

### Enable Error Tracking

1. Settings → Error Tracking
2. Configure error notifications
3. View detailed error reports

### Access Application Logs

For client-side issues, open browser console:
- **Chrome/Firefox/Safari:** Press F12 → Console tab
- **Check for JavaScript errors** - will appear in red

---

## Rollback Procedures

### Method 1: Revert to Previous Deployment (via Vercel)

1. **In Vercel Dashboard:**
   - Select your project
   - Go to **Deployments**
   - Find the previous successful deployment
   - Click **...** → **Promote to Production**

### Method 2: Revert via Git

If you need to revert code changes:

```bash
# View commit history
git log --oneline

# Revert to specific commit
git revert <commit-hash>

# Or reset to specific commit (destructive, use carefully)
git reset --hard <commit-hash>

# Push changes
git push origin main
```

**Windows PowerShell:**
```powershell
git log --oneline
git revert <commit-hash>
git push origin main
```

### Automatic Redeployment

Once you push to `main` branch, Vercel automatically deploys the latest version. This happens within 30-60 seconds.

### Rollback Steps

1. Identify the issue
2. In GitHub, create a new commit that fixes the problem OR revert to previous commit
3. Push to `main` branch
4. Vercel automatically deploys the fix
5. Monitor new deployment in Vercel dashboard

---

## Platform-Specific Instructions

### macOS Deployment

```bash
# Prerequisites
brew install git node

# Verify installation
git --version && node --version

# Clone repository
cd ~/Projects
git clone https://github.com/YOUR_USERNAME/datathon-water-analysis.git
cd datathon-water-analysis

# Add files
cp /Volumes/Arath/Automation_Station/Projects/Datathon/web/* .

# Commit and push
git add .
git commit -m "Initial commit: Water analysis dashboard"
git push -u origin main

# Test locally (optional)
npm install http-server
npm run dev
# Visit http://localhost:3000
```

### Linux Deployment

```bash
# Prerequisites (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install git nodejs npm

# Verify installation
git --version && node --version

# Clone and setup (same as macOS from here)
cd ~/Projects
git clone https://github.com/YOUR_USERNAME/datathon-water-analysis.git
cd datathon-water-analysis

# Commit and push
git add .
git commit -m "Initial commit: Water analysis dashboard"
git push -u origin main
```

### Windows Deployment (PowerShell)

**Step 1: Install Prerequisites**

```powershell
# Install Chocolatey (if not already installed)
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install Git and Node.js
choco install git nodejs -y

# Verify
git --version
node --version
npm --version
```

**Step 2: Clone Repository**

```powershell
# Create Projects folder
New-Item -ItemType Directory -Path "$env:USERPROFILE\Projects" -Force
cd "$env:USERPROFILE\Projects"

# Clone repository
git clone https://github.com/YOUR_USERNAME/datathon-water-analysis.git
cd datathon-water-analysis
```

**Step 3: Copy Project Files**

```powershell
# Copy files from network/external location
Copy-Item 'D:\Automation_Station\Projects\Datathon\web\*' -Destination '.' -Recurse -Force

# Or if files are on network drive
Copy-Item '\\NetworkPath\Projects\Datathon\web\*' -Destination '.' -Recurse -Force
```

**Step 4: Configure Git**

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Step 5: Commit and Push**

```powershell
# Check status
git status

# Stage files
git add .

# Commit
git commit -m "Initial commit: Water analysis dashboard with Vercel config"

# Rename branch (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Step 6: Verify on GitHub**

- Go to https://github.com/YOUR_USERNAME/datathon-water-analysis
- Confirm all files are visible

### Windows Deployment (Git Bash)

```bash
# Install Git for Windows from https://git-scm.com/download/win
# Install Node.js from https://nodejs.org

# Open Git Bash and run:
cd ~/Projects
git clone https://github.com/YOUR_USERNAME/datathon-water-analysis.git
cd datathon-water-analysis

# Copy files
cp /c/path/to/Automation_Station/Projects/Datathon/web/* .

# Configure and push
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git add .
git commit -m "Initial commit: Water analysis dashboard"
git push -u origin main
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: "Authentication failed" when pushing to GitHub

**Solution:**
```bash
# Use GitHub Personal Access Token instead of password
# 1. Go to GitHub Settings → Developer settings → Personal access tokens
# 2. Create new token with 'repo' scope
# 3. Use token as password when prompted
# Or configure SSH keys:

# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Add public key to GitHub
cat ~/.ssh/id_ed25519.pub  # Copy output
# Go to GitHub Settings → SSH and GPG keys → New SSH key → Paste
```

#### Issue: "Repository not found" error

**Solution:**
- Verify you created the GitHub repository
- Check that the URL is correct
- Confirm you're logged into GitHub
- Check repository visibility (should be Public)

**Windows PowerShell Debug:**
```powershell
# Test GitHub connection
ssh -T git@github.com

# Should output: "Hi USERNAME! You've successfully authenticated..."
```

#### Issue: Vercel deployment shows blank page

**Solution:**
1. Check that `index.html` is in the root directory
2. Verify all CSS/JS file paths are relative (not absolute)
3. Check browser console for errors (F12)
4. Verify CDN scripts are loading (check Network tab)

```bash
# Debug file structure
ls -la  # macOS/Linux
dir     # Windows PowerShell
```

#### Issue: 404 Error on Vercel

**Solution:**
```bash
# Ensure correct folder structure
# Root directory should contain:
# - index.html
# - style.css
# - script.js
# - data/
# - assets/
# etc.

# Check git ignore isn't excluding HTML files
cat .gitignore | grep -i "html"
```

#### Issue: CORS errors loading data files

**Solution:**
- Ensure data files are committed to Git
- Check file paths in HTML match actual file locations
- Verify no special characters in filenames
- Use relative paths: `data/myfile.csv` not `/data/myfile.csv`

#### Issue: Changes not deploying

**Solution:**
```bash
# Verify you pushed to main branch
git log --oneline
git branch -a
git status

# Force push only if absolutely necessary
git push origin main --force  # Use with caution!
```

**Windows verification:**
```powershell
git log --oneline
git branch -a
git status
git push origin main
```

#### Issue: Vercel build takes too long or times out

**Solution:**
- Static sites should deploy in seconds
- Check for large files (>5MB per file)
- Optimize images before committing
- Check deployment logs in Vercel dashboard

```bash
# Check file sizes
ls -lh  # macOS/Linux
dir /h  # Windows

# Remove large files
git rm --cached largeFile.bin
echo "largeFile.bin" >> .gitignore
git commit -m "Remove large file"
git push
```

#### Issue: Outdated dependencies

**Solution:**
```bash
npm outdated
npm update

# Or update specific package
npm install plotly.js@latest
git add package.json package-lock.json
git commit -m "Update dependencies"
git push
```

---

## CI/CD with GitHub Actions

### Optional: Automated Testing and Deployment

GitHub Actions allows you to automate tests and deployments.

### Step 1: Create Workflow File

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Vercel

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Install Vercel CLI
        run: npm install -g vercel

      - name: Deploy to Vercel
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
          VERCEL_ORG_ID: ${{ secrets.VERCEL_ORG_ID }}
          VERCEL_PROJECT_ID: ${{ secrets.VERCEL_PROJECT_ID }}
        run: vercel deploy --prod --token $VERCEL_TOKEN
```

### Step 2: Configure GitHub Secrets

1. Go to repository → Settings → Secrets and variables → Actions
2. Add new secrets:
   - `VERCEL_TOKEN` - From Vercel Account Settings
   - `VERCEL_ORG_ID` - Your Vercel organization ID
   - `VERCEL_PROJECT_ID` - Project ID from Vercel dashboard

### Step 3: Commit Workflow

```bash
git add .github/workflows/deploy.yml
git commit -m "Add GitHub Actions CI/CD workflow"
git push origin main
```

Now every push to `main` will:
1. Run any tests
2. Automatically deploy to Vercel production

Monitor workflow execution in GitHub → Actions tab.

---

## Deployment Checklist

Before deploying, verify:

- [ ] All HTML files have correct paths to CSS/JS
- [ ] All data files are committed to Git
- [ ] No sensitive information in code or data
- [ ] `.gitignore` properly configured
- [ ] `package.json` metadata is accurate
- [ ] `vercel.json` configuration is correct
- [ ] GitHub repository is created and pushed
- [ ] Vercel account connected to GitHub
- [ ] Project imported into Vercel
- [ ] Deployment successful (green checkmark)
- [ ] Site accessible at Vercel URL
- [ ] All pages loading without errors
- [ ] Console has no critical errors (F12)
- [ ] Responsive design tested on mobile
- [ ] Data visualizations loading correctly
- [ ] CDN scripts (Plotly, Papa Parse) loaded

---

## Post-Deployment

### Monitor Performance

1. Check Vercel Analytics dashboard daily for first week
2. Monitor error logs for issues
3. Test functionality regularly
4. Gather user feedback

### Update and Maintenance

To make updates:

```bash
# Pull latest changes
git pull origin main

# Make changes to files
# Edit index.html, style.css, etc.

# Commit and push
git add .
git commit -m "Update dashboard with new data"
git push origin main

# Vercel automatically deploys within 30-60 seconds
```

### Scaling Considerations

- Current setup handles unlimited visitors (static site)
- Cache headers optimized for performance
- Security headers configured for production
- No backend required (fully static)

---

## Support and Resources

- **Vercel Docs:** https://vercel.com/docs
- **GitHub Docs:** https://docs.github.com
- **Plotly.js:** https://plotly.com/javascript/
- **Papa Parse:** https://www.papaparse.com

For issues or questions, refer to the troubleshooting section above.

---

**Last Updated:** February 2025
**Project:** Datathon Water Analysis Dashboard
**Framework:** Static HTML/CSS/JavaScript
**Deployment Platform:** Vercel
