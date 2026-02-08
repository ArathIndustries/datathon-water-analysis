# Vercel Deployment Guide for Datathon Water Analysis Project

## Overview
This guide walks you through deploying the Datathon Water Analysis project to Vercel, a platform that automatically builds and hosts your application with continuous deployment from GitHub.

---

## Part 1: Vercel Account Setup

### 1.1 Create a Free Vercel Account

1. Go to https://vercel.com
2. Click "Sign Up" in the top-right corner
3. Choose your sign-up method:
   - **Recommended:** Click "Continue with GitHub" to link your GitHub account
   - Or create a Vercel account with email
4. If using GitHub login:
   - Authorize Vercel to access your GitHub account
   - You may need to verify your GitHub account again
5. Complete the onboarding steps
6. You'll be taken to the Vercel dashboard

**Screenshot Reference:** The "Sign Up" button is in the top-right corner. After clicking, you'll see options for GitHub, GitLab, or email sign-up.

### 1.2 Verify Your Account

- Check your email for a verification link (if you used email sign-up)
- Click the link to verify your account
- You can now access the Vercel dashboard at https://vercel.com/dashboard

---

## Part 2: Create Vercel Project from GitHub

### 2.1 Connect Your GitHub Repository to Vercel

**Method 1: From Vercel Dashboard (Recommended)**

1. Go to https://vercel.com/dashboard
2. Click "Add New..." button
3. Select "Project"
4. Find "datathon-water-analysis" in the list of your GitHub repositories
   - If you don't see it, click "Configure GitHub App" and authorize Vercel to access more repositories
5. Click "Import"

**Method 2: From GitHub Repository**

1. Go to your GitHub repository: https://github.com/YOUR-USERNAME/datathon-water-analysis
2. Click the "Deploy" button (if visible), or
3. Look for Vercel integration in the repository settings and click "Deploy with Vercel"

**Screenshot Reference:** In the Vercel dashboard, you'll see a list of your repositories with "Import" buttons next to each one.

### 2.2 Configure Project Settings

After clicking "Import," you'll see the project configuration page:

1. **Project Name:** This will be auto-filled with "datathon-water-analysis"
   - Can be changed, but keep it descriptive
2. **Framework Preset:**
   - If it's a React/Next.js project: Select "Next.js"
   - If it's a static HTML/CSS/JS project: Select "Other"
   - Let Vercel auto-detect if unsure
3. **Root Directory:**
   - Leave as default (.) if files are in the root
   - Set to the correct path if files are in a subdirectory
4. **Build and Output Settings:**
   - **Build Command:** Usually auto-detected (e.g., `next build`, `npm run build`)
   - **Output Directory:** Usually auto-detected (e.g., `.next`, `dist`, `out`)
   - **Install Command:** Leave as default (auto-detected)

5. **Environment Variables:** See Part 4 below
6. Click "Deploy"

**Note:** Don't click "Deploy" yet if you need to set environment variables (see Part 4).

---

## Part 3: Initial Deployment

### 3.1 Wait for Deployment to Complete

1. After clicking "Deploy," you'll see a deployment progress screen
2. Vercel will:
   - Clone your GitHub repository
   - Install dependencies
   - Build your project
   - Deploy to the Vercel platform
3. This typically takes 2-5 minutes
4. You'll see messages like:
   - "Cloning..."
   - "Installing..."
   - "Building..."
   - "Deploying..."

**Screenshot Reference:** Watch for the checkmark or "READY" status next to each step.

### 3.2 Verify Successful Deployment

When deployment completes:
1. You'll see a "Visit" button with a Vercel URL (something like `https://datathon-water-analysis-yourname.vercel.app`)
2. Click "Visit" to view your deployed project
3. The project should load and display correctly
4. You're now deployed to the internet!

**Vercel URL Format:** `https://PROJECT-NAME-USERNAME.vercel.app`

### 3.3 Access Your Deployment Dashboard

Go to https://vercel.com/dashboard and click on your project name to access the project dashboard.

---

## Part 4: Environment Variables (If Needed)

### 4.1 About Environment Variables

Environment variables are configuration values like API keys, database URLs, or feature flags that your application might need.

**Check if you need them:**
1. Does your project make API calls to external services?
2. Are there API keys or secrets in your code?
3. Does it use a database?

If no external APIs or secrets, you can skip this section.

### 4.2 Add Environment Variables to Vercel

1. Go to your project dashboard: https://vercel.com/dashboard
2. Click on your project name: "datathon-water-analysis"
3. Click the "Settings" tab
4. In the left sidebar, click "Environment Variables"
5. For each environment variable you need:
   - Enter the variable name (e.g., `API_KEY`, `DATABASE_URL`)
   - Enter the variable value
   - Select which environments it applies to:
     - **Production:** Available in live deployments
     - **Preview:** Available in preview deployments
     - **Development:** Available when running locally
   - Click "Save"

### 4.3 Redeploy After Adding Variables

If you added environment variables:
1. Go back to the "Deployments" tab
2. Find your latest deployment
3. Click the three-dot menu ("...")
4. Select "Redeploy"
5. Choose "Use existing Build Cache" for faster deployment
6. Wait for the new deployment to complete

---

## Part 5: Automatic Deployments from GitHub

### 5.1 How Automatic Deployments Work

Once connected to GitHub, Vercel automatically deploys your project whenever you push code:

1. **Main branch push:** Automatically deploys to production
   - URL: `https://datathon-water-analysis-yourname.vercel.app`
2. **Other branch push:** Creates a preview deployment
   - URL: `https://datathon-water-analysis-main-yourname.vercel.app` (example)
3. **Pull requests:** Creates a preview deployment
   - Review the changes before merging

### 5.2 Verify Automatic Deployments Are Enabled

1. Go to your project Settings
2. Click "Git" in the left sidebar
3. Verify these settings:
   - **Production Branch:** Set to "main"
   - **Automatic Deployments:** Should be ON
   - **Framework:** Should be set correctly
4. Save any changes

**Screenshot Reference:** You'll see toggles for each deployment type in the Git settings.

---

## Part 6: Custom Domain Setup (Optional)

### 6.1 Purchase or Use Existing Domain

If you want a custom domain (e.g., `datathon-water-analysis.com`):

1. Purchase a domain from a registrar like:
   - GoDaddy
   - Namecheap
   - Google Domains
   - Cloudflare

2. Or use a free domain from:
   - Freenom (free TLDs like .tk, .ml)
   - GitHub Pages (USERNAME.github.io)

### 6.2 Add Custom Domain to Vercel

1. Go to your project Settings
2. Click "Domains" in the left sidebar
3. Enter your domain name
4. Click "Add"
5. Vercel will show you DNS configuration instructions

### 6.3 Update DNS Records

This varies by registrar. General steps:

1. Log in to your domain registrar's dashboard
2. Find "DNS Settings" or "Name Servers"
3. Depending on Vercel's instructions, either:
   - **Option A:** Point to Vercel name servers (change Name Servers)
   - **Option B:** Add CNAME or A records to point to Vercel

**Example CNAME record:**
```
Name: (your domain or subdomain)
Type: CNAME
Value: cname.vercel-dns.com
```

4. Save the DNS changes
5. DNS propagation takes 15 minutes to 48 hours
6. Return to Vercel and verify the domain is connected
7. Vercel will automatically provision an SSL certificate

**Detailed Instructions by Registrar:**
- GoDaddy: https://vercel.com/docs/concepts/projects/domains/add-a-domain#godaddy
- Namecheap: https://vercel.com/docs/concepts/projects/domains/add-a-domain#namecheap
- See Vercel docs for others: https://vercel.com/docs/concepts/projects/domains

### 6.4 SSL/TLS Certificate

Vercel automatically provisions SSL/TLS certificates for all domains. This means:
- Your domain uses HTTPS (secure connection)
- The certificate is automatically renewed
- No additional configuration needed

You can verify the certificate is working by visiting `https://yourdomain.com`.

---

## Part 7: Preview Deployments

### 7.1 Understanding Preview Deployments

Every time you push code (except to main) or create a pull request, Vercel creates a preview deployment. This lets you:
- Test changes before deploying to production
- Share working versions with collaborators
- Verify your changes work in the cloud

### 7.2 Access Preview Deployments

**From Vercel Dashboard:**
1. Go to your project: https://vercel.com/dashboard
2. Click on your project name
3. Go to the "Deployments" tab
4. Each deployment shows:
   - Status (Building, Ready, Failed)
   - Branch name
   - URL to view the deployment
   - Commit message

**From GitHub Pull Requests:**
1. Create a pull request on GitHub
2. Scroll down to see the "Checks" section
3. You'll see "Vercel" with a link to the preview deployment
4. Click "Visit Preview" to see the changes

**Screenshot Reference:** In the Deployments tab, you'll see a list with "Production" marked, and Preview deployments listed below.

### 7.3 Share Preview Deployments

Each preview has a unique URL you can share:
- Send the preview URL to teammates
- They can test the changes without cloning the repository
- Perfect for gathering feedback

---

## Part 8: Production Deployment

### 8.1 Deploy to Production

When you're ready to go live:

1. Merge your feature branch to the main branch (via pull request on GitHub)
2. Vercel automatically detects the push to main
3. Vercel builds and deploys to production
4. Your live site updates

**PowerShell Commands to Push to Main:**
```powershell
# Switch to main branch
git checkout main

# Pull latest changes from GitHub
git pull origin main

# Merge feature branch (if using branches)
git merge feature-branch-name

# Push to GitHub
git push origin main

# Vercel will automatically deploy!
```

### 8.2 Verify Production Deployment

1. Go to https://vercel.com/dashboard
2. Click your project
3. Check the "Deployments" tab
4. The production deployment should show "Ready" status
5. Visit your live site:
   - `https://datathon-water-analysis-yourname.vercel.app` (default)
   - Or your custom domain if configured

---

## Part 9: Rollback to Previous Deployment

### 9.1 Revert a Broken Deployment

If a deployment breaks your site:

**Method 1: Rollback via Vercel Dashboard**
1. Go to your project Deployments
2. Find the previous working deployment
3. Click the three-dot menu ("...")
4. Select "Promote to Production"
5. Confirm - the previous deployment becomes live again
6. Fix the issue in your code and re-deploy

**Method 2: Revert on GitHub**
```powershell
# View commit history
git log --oneline

# Find the commit hash of the last working version
# Reset to that commit
git revert COMMIT_HASH

# Or hard reset (be careful!)
git reset --hard COMMIT_HASH

# Push to GitHub (this triggers a new Vercel deployment)
git push origin main
```

---

## Part 10: Monitoring and Analytics

### 10.1 Access Deployment Logs

1. Go to your project: https://vercel.com/dashboard
2. Click on your project name
3. Click the "Deployments" tab
4. Click on a specific deployment
5. You'll see:
   - **Build Logs:** Output from the build process
   - **Runtime Logs:** Any errors or console output while running
   - **Deployment Status:** Success/Failed indicators

### 10.2 View Build Errors

If a deployment fails:
1. Click on the failed deployment
2. Scroll to the "Build" section
3. Red error messages show what went wrong
4. Common issues:
   - Missing build command
   - Dependency installation failure
   - Code syntax errors

**Example Error Message:**
```
Error: Deployment failed
→ Build error: module not found: 'package-name'
→ Install dependencies and re-deploy
```

### 10.3 Access Analytics (Pro Plans)

Analytics are available on paid Vercel plans, but free tier includes basic monitoring:
1. Go to your project Settings
2. Click "Analytics" (if available for your plan)
3. View:
   - Page views and traffic
   - Performance metrics
   - Web Core Vitals
   - Error rates

---

## Part 11: Team Access and Collaboration

### 11.1 Add Team Members to Vercel Project

1. Go to your project Settings
2. Click "Members" in the left sidebar
3. Click "Add Member"
4. Enter the email address of the team member
5. Select their role:
   - **Owner:** Full control
   - **Member:** Can view and manage deployments
   - **Viewer:** Read-only access
6. Click "Send Invite"
7. They'll receive an email to join your Vercel team

### 11.2 Link GitHub and Vercel Accounts

Ensure all team members:
1. Have GitHub accounts
2. Have access to the GitHub repository
3. Have Vercel accounts (can use same GitHub login)
4. Are added to the Vercel project as members

This ensures seamless collaboration and automatic deployments.

---

## Part 12: Windows-Specific Setup

### 12.1 Setting Up Git Credentials for Vercel

When Vercel clones your GitHub repository, it needs authentication.

**If using GitHub Login for Vercel (Recommended):**
1. Sign up for Vercel with your GitHub account
2. Vercel automatically has permission to access your repositories
3. No additional credentials needed

**If Using Username/Password:**
1. This is less secure - use personal access tokens instead

**If Using SSH Keys:**
1. This is advanced but most secure
2. Set up SSH keys on GitHub: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
3. Vercel will use your SSH key for authentication

### 12.2 Test Connection from PowerShell

```powershell
# Test GitHub connection
git ls-remote https://github.com/YOUR-USERNAME/datathon-water-analysis.git

# Should show a list of branches if connection works
```

---

## Part 13: Vercel CLI Setup (Advanced - Optional)

The Vercel CLI allows you to deploy from your computer without using GitHub.

### 13.1 Install Vercel CLI

```powershell
# Install globally using npm
npm install -g vercel

# Verify installation
vercel --version
```

### 13.2 Login to Vercel via CLI

```powershell
# Login to your Vercel account
vercel login

# Follow the prompts and authenticate via GitHub
```

### 13.3 Deploy Using CLI

```powershell
# Navigate to your project directory
cd C:\Path\To\datathon-water-analysis

# Deploy
vercel

# For production deployment
vercel --prod

# View deployment logs
vercel logs
```

### 13.4 View Project Status

```powershell
# List all deployments
vercel list

# View specific deployment details
vercel inspect [url]

# Remove a deployment
vercel rm [url]
```

---

## Part 14: Troubleshooting

### 14.1 Deployment Fails with "Build Error"

**Check the build logs:**
1. Go to your failed deployment
2. Look at the build output for error messages
3. Common issues:
   - Missing dependencies: `npm install` before building
   - Wrong framework detected: Set framework in settings
   - Incorrect build command: Check settings

**Fix and redeploy:**
```powershell
# After fixing the issue in your code
git add .
git commit -m "Fix build error"
git push origin main

# Vercel will automatically rebuild
```

### 14.2 Website Shows 404 Error

**Check the following:**
1. Your site is deployed at the right URL
2. Your index.html or appropriate entry file exists
3. If using a subdirectory, ensure "Root Directory" is set correctly in Vercel settings

**For static sites:**
- Make sure your HTML files are in the root directory
- The main page should be named `index.html`

**For frameworks (Next.js, etc.):**
- The build process generates the necessary files
- Check that the output directory is set correctly

### 14.3 Environment Variables Not Working

**Verify configuration:**
1. Variables are saved in Vercel Settings → Environment Variables
2. Variables are set for the correct environment (Production, Preview, Development)
3. Redeploy after adding new variables
4. Check variable names are spelled correctly and used in your code

**Test locally:**
```powershell
# Create a .env.local file in your project
# Add your variables there
API_KEY=your_key_here

# When deployed to Vercel, use Vercel's Environment Variables setting instead
```

### 14.4 Changes Not Showing After Push

**Solution:**
1. Verify the push was successful: `git log --oneline` shows your commit
2. Check Vercel deployments tab - deployment should be "Ready"
3. Hard refresh your browser (Ctrl+F5 or Cmd+Shift+R)
4. Check for browser cache issues: Open in incognito/private mode
5. Wait 1-2 minutes for Vercel to propagate the changes

### 14.5 Domain Not Connecting

**Check DNS propagation:**
1. Use a DNS checker: https://mxtoolbox.com/dnschecker.aspx
2. Enter your domain and check if DNS records point to Vercel
3. DNS changes can take up to 48 hours to propagate
4. Verify records match what Vercel requested

**Common issues:**
- Incorrect CNAME value
- Missing DNS record
- Pointing to wrong hosting provider
- TTL (Time To Live) not yet expired

### 14.6 Can't Connect GitHub Repository

**Solution:**
1. Go to https://vercel.com/dashboard
2. Click your user profile icon (top-right)
3. Select "Settings"
4. Click "Git" in the sidebar
5. Click "Manage" next to GitHub
6. Authorize Vercel to access more repositories
7. Try importing the repository again

---

## Part 15: Auto-Deploy vs Manual Deploy Configuration

### 15.1 Auto-Deploy (Recommended)

Auto-deploy is enabled by default and works like this:

1. You push code to GitHub
2. GitHub notifies Vercel
3. Vercel automatically builds and deploys

**To verify auto-deploy is enabled:**
1. Go to project Settings
2. Click "Git"
3. Confirm "Automatic Deployments" is ON

### 15.2 Manual Deploy

You can disable auto-deploy and deploy manually:

**Disable auto-deploy:**
1. Go to project Settings
2. Click "Git"
3. Toggle "Automatic Deployments" OFF
4. Save changes

**Deploy manually:**
```powershell
# Using Vercel CLI
vercel --prod

# Or through the dashboard
# Go to Deployments tab and click "Redeploy" on an old deployment
```

**Use manual deploy when:**
- You want to test locally before deploying
- You need time to prepare for a release
- You're working with a team and want controlled deployments

### 15.3 Recommended Workflow

1. **Enable auto-deploy** for the main branch
2. **Use feature branches** for development
3. **Use pull requests** to preview changes before merging
4. **Review preview deployments** before merging to main
5. **Merge to main** when ready - auto-deploy handles the rest

This ensures:
- Production is always stable
- Changes are reviewed before going live
- Deployments are automatic and consistent

---

## Part 16: Testing Deployment Locally Before Pushing

### 16.1 Build Your Project Locally

Before pushing to GitHub (and triggering Vercel), test locally:

**For Next.js projects:**
```powershell
# Install dependencies
npm install

# Build the project
npm run build

# Run the production build locally
npm run start

# Visit http://localhost:3000
```

**For static HTML/CSS/JS projects:**
```powershell
# No build step needed - just verify files are correct
# Open index.html in your browser or use a local server

# Or use a simple local server
python -m http.server 8000
# Then visit http://localhost:8000
```

### 16.2 Verify Everything Works

- Check all pages load correctly
- Test all interactive features
- Verify no console errors (F12 → Console tab)
- Check mobile responsiveness
- Test links and navigation

### 16.3 Only Push When Confident

```powershell
# If everything looks good locally
git add .
git commit -m "Your commit message"
git push origin main

# Vercel will deploy automatically
```

---

## Quick Reference

### Dashboard Links
- Vercel Dashboard: https://vercel.com/dashboard
- Project Settings: https://vercel.com/dashboard/[project-name]/settings
- Deployments: https://vercel.com/dashboard/[project-name]/deployments
- Domains: https://vercel.com/dashboard/[project-name]/settings/domains

### Common Commands

```powershell
# View live deployment
vercel --list

# Deploy manually
vercel --prod

# View logs
vercel logs [deployment-url]

# Remove old deployment
vercel rm [deployment-url]
```

### After Deployment
- Live URL: `https://datathon-water-analysis-yourname.vercel.app`
- Share this URL with project partners
- They can access the live project without any setup

---

## Next Steps

1. **Follow the GitHub setup guide** (GITHUB_SETUP.md) first if not already done
2. **Return here to deploy** to Vercel
3. **Share the live URL** with project partners (PARTNER_SHARING.md)
4. **Set up workflow** for continuous development (GITHUB_VERCEL_INTEGRATED_WORKFLOW.md)

---

## Resources

- Vercel Documentation: https://vercel.com/docs
- Vercel Deployment: https://vercel.com/docs/concepts/deployments/overview
- Custom Domains: https://vercel.com/docs/concepts/projects/domains
- Environment Variables: https://vercel.com/docs/concepts/projects/environment-variables
- Vercel CLI: https://vercel.com/docs/cli
- Troubleshooting: https://vercel.com/docs/troubleshootings

