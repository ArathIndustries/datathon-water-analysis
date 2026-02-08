# GitHub and Vercel Integrated Workflow Guide

## Overview
This guide describes the complete workflow for developing, deploying, and managing the Datathon Water Analysis project using GitHub for version control and Vercel for hosting.

---

## Part 1: Understanding the Workflow

### 1.1 The Development Pipeline

Here's how code moves from your computer to the live website:

```
Your Computer (Local Development)
    ↓
Git Commit & Push
    ↓
GitHub Repository
    ↓
Vercel Detects Changes
    ↓
Vercel Builds Project
    ↓
Vercel Deploys to Internet
    ↓
Live Website Available
```

### 1.2 Key Concepts

- **Main Branch:** Production code that's deployed live
- **Feature Branches:** Temporary branches for developing new features
- **Pull Requests (PR):** Propose changes before merging to main
- **Preview Deployments:** Test version of your changes before going live
- **Production Deployment:** Your live website that partners can access

### 1.3 Typical Workflow Steps

1. Create a feature branch
2. Make code changes
3. Commit changes to Git
4. Push to GitHub
5. Create a pull request (optional but recommended)
6. Review preview deployment
7. Merge to main
8. Vercel automatically deploys to production
9. Live website updates

---

## Part 2: Feature Branch Workflow

### 2.1 Create a Feature Branch

Always work on a feature branch instead of directly on main. This keeps main stable.

```powershell
# First, make sure you're on the main branch
git checkout main

# Pull latest changes from GitHub
git pull origin main

# Create and switch to a new feature branch
# Use descriptive names: feature/add-water-level-chart, fix/login-bug
git checkout -b feature/add-dashboard-widget

# Verify you're on the new branch
git branch
# Should show "* feature/add-dashboard-widget"
```

**Branch Naming Conventions:**
- `feature/description` - New features (e.g., `feature/add-export-csv`)
- `fix/description` - Bug fixes (e.g., `fix/charts-not-loading`)
- `docs/description` - Documentation updates (e.g., `docs/update-readme`)
- `refactor/description` - Code improvements (e.g., `refactor/optimize-api-calls`)
- `test/description` - Tests (e.g., `test/add-unit-tests`)

### 2.2 Make Code Changes

Edit your files in your code editor:
- Add new features
- Fix bugs
- Update documentation
- Improve design

Save your files and test locally.

### 2.3 Check What Changed

```powershell
# See which files were modified
git status

# See the actual changes in files
git diff

# See changes for a specific file
git diff filename.js
```

---

## Part 3: Commit Changes

### 3.1 Stage Files

```powershell
# Stage all changes
git add .

# Or stage specific files
git add filename.js
git add anotherfile.css

# Verify what's staged
git status
# Green text = staged, ready to commit
```

### 3.2 Commit with Clear Messages

```powershell
# Simple commit message
git commit -m "Add water level chart widget"

# Detailed commit message (recommended)
git commit -m "Add water level chart widget

- Display real-time water levels
- Include historical trend line
- Add refresh button
- Implement data caching for performance"
```

**Commit Message Guidelines:**
- First line: What changed (50 characters or less)
- Blank line
- Detailed description (why it changed, how it works)
- Be specific and descriptive
- Use present tense: "Add feature" not "Added feature"

### 3.3 Verify Your Commits

```powershell
# View commit history on current branch
git log --oneline

# Should show your new commits
```

---

## Part 4: Push Changes to GitHub

### 4.1 Push Your Feature Branch

```powershell
# First time pushing this branch
git push -u origin feature/add-dashboard-widget

# Subsequent pushes to the same branch
git push origin feature/add-dashboard-widget

# Or shorthand (if tracking is set up)
git push
```

The `-u` flag sets upstream tracking, so next time you can just use `git push`.

### 4.2 Verify Push on GitHub

1. Go to your repository: https://github.com/YOUR-USERNAME/datathon-water-analysis
2. You should see a notification: "Your branch was just pushed"
3. Click "Compare & pull request" button (optional)
4. Or go to the "Branches" tab to see your new branch

**Screenshot Reference:** You'll see a yellow banner at the top if you just pushed, with a "Compare & pull request" button.

---

## Part 5: Create a Pull Request (PR)

### 5.1 What is a Pull Request?

A pull request is a formal way to:
- Propose changes before merging
- Get feedback from teammates
- Run automatic checks
- Create a preview deployment
- Discuss the changes

### 5.2 Create a Pull Request on GitHub

1. Go to your repository: https://github.com/YOUR-USERNAME/datathon-water-analysis
2. Click the "Pull requests" tab
3. Click "New pull request"
4. Select:
   - **Base branch:** main (where your changes will go)
   - **Compare branch:** your feature branch (what you want to merge)
5. Click "Create pull request"

**Or use the quick method:**
1. After pushing your branch, look for the yellow banner at the top of the repository
2. Click "Compare & pull request"
3. Add your PR title and description
4. Click "Create pull request"

### 5.3 Pull Request Title and Description

**Title:** Should clearly describe what the PR does

Examples:
- "Add water level chart widget"
- "Fix navigation menu on mobile"
- "Update partner contact information"

**Description:** Should explain why this change is needed

Template:
```
## Summary
Brief description of what this PR does

## Changes Made
- Item 1
- Item 2
- Item 3

## How to Test
1. Step 1
2. Step 2
3. Expected result

## Screenshots (if applicable)
[Paste screenshots here]

Fixes #123 (if closing an issue)
```

### 5.4 Verify Preview Deployment

After creating the PR:
1. Scroll down in the PR page
2. Look for "Vercel" check showing "Deployment Preview"
3. Click "Visit Preview" to see the changes in a live preview
4. The preview URL looks like: `https://datathon-water-analysis-preview-xyz.vercel.app`
5. Test the new feature in the preview

**Screenshot Reference:** Under "Checks" section, you'll see a "Vercel" item with a link to visit the preview.

### 5.5 Review and Request Changes

**For solo projects:**
- Review your own changes
- Click "View Preview" to test
- If everything looks good, merge

**For team projects:**
- Ask teammates to review
- Address any feedback comments
- Make additional commits if needed (automatically updates PR)

### 5.6 Merge the Pull Request

When ready to merge:

1. On the PR page, scroll to the bottom
2. Click "Merge pull request" (green button)
3. Choose merge strategy:
   - **Create a merge commit** (recommended for clarity)
   - **Squash and merge** (combines all commits)
   - **Rebase and merge** (advanced)
4. Confirm the merge
5. Click "Delete branch" to clean up

**Screenshot Reference:** Green "Merge pull request" button at the bottom of the PR page.

---

## Part 6: Automatic Production Deployment

### 6.1 What Happens After Merging

When you merge to main:
1. GitHub receives the merge
2. GitHub notifies Vercel
3. Vercel automatically starts building
4. Vercel deploys to production
5. Your live site updates

**No additional steps needed** - it's automatic!

### 6.2 Monitor the Deployment

**From Vercel Dashboard:**
1. Go to https://vercel.com/dashboard
2. Click your project: "datathon-water-analysis"
3. Go to "Deployments" tab
4. Watch for the new deployment to build and deploy
5. Status will show: Building → Ready

**From GitHub:**
1. Go to your repository
2. Click the "Deployments" tab
3. See the production deployment status
4. Click on it to see details

**Timeline:**
- Building: 1-3 minutes
- Ready: Site is live!

### 6.3 Verify Live Changes

After deployment completes:
1. Go to your live site: `https://datathon-water-analysis-yourname.vercel.app`
2. Hard refresh (Ctrl+F5 or Cmd+Shift+R)
3. Verify your changes are visible
4. Test the new feature in production

---

## Part 7: Accessing Deployed Sites

### 7.1 Preview Deployments

Each pull request gets a unique preview URL:

```
https://datathon-water-analysis-feature-description.vercel.app
```

- Access any time without creating a commit
- Perfect for testing before merging
- URL changes with each update to the PR
- Share with teammates for feedback

**Find preview URL:**
1. Go to your pull request
2. Scroll to "Checks" section
3. Click "Details" next to Vercel
4. Click "Visit Preview"

### 7.2 Production Deployment

Your live site is always available at:

```
https://datathon-water-analysis-yourname.vercel.app
```

Or with a custom domain:
```
https://yourdomain.com
```

**Share this URL with project partners** - they access the production site here.

### 7.3 Development Locally

While developing, test on your computer before pushing:

```powershell
# For Next.js / React
npm run dev

# Visit http://localhost:3000

# For static sites
# Open index.html in your browser
```

Only push when you're confident the changes work.

---

## Part 8: Sharing Links with Project Partners

### 8.1 Live Site URL

Share your production URL with partners:

```
https://datathon-water-analysis-yourname.vercel.app
```

Partners can:
- View the live dashboard
- Interact with data
- Download data
- No setup required

### 8.2 Repository Access

Partners can access code on GitHub:

```
https://github.com/YOUR-USERNAME/datathon-water-analysis
```

**Permissions to grant:**
- **Read-only:** Can view code, download, but cannot push changes
- **Contributor:** Can propose changes via pull requests
- **Maintainer:** Full access including settings

**How to add collaborators:**
1. Go to GitHub repository Settings
2. Click "Collaborators" in the sidebar
3. Click "Add people"
4. Enter their GitHub username
5. Select permission level
6. Click "Invite"

### 8.3 Deployment Preview Links

Share preview deployments for testing new features:

```
https://datathon-water-analysis-feature-name.vercel.app
```

Perfect for:
- Beta testing new features
- Gathering feedback
- Testing before going live

---

## Part 9: Monitoring Deployments

### 9.1 Check Deployment Status

**From Vercel Dashboard:**
1. https://vercel.com/dashboard
2. Click your project
3. "Deployments" tab shows all deployments
4. Status indicators:
   - Blue "Building" - Currently building
   - Green "Ready" - Live and working
   - Red "Failed" - Deployment failed
   - Gray "Canceled" - Deployment was stopped

### 9.2 View Build Logs

If a deployment fails:
1. Click the failed deployment
2. Scroll to "Build" section
3. Read the error messages
4. Common errors:
   - "module not found" - Missing dependency
   - "syntax error" - Code error
   - "build failed" - Build command issue

### 9.3 Access Runtime Logs

To see what happens when your site is running:
1. Click a deployment
2. Scroll to "Runtime" section
3. View console output and errors
4. Useful for debugging production issues

---

## Part 10: Reverting Changes

### 10.1 Revert a Broken Deployment

If your last deploy broke the site:

**Method 1: Quick Rollback via Vercel**

1. Go to https://vercel.com/dashboard
2. Click your project → Deployments
3. Find the previous working deployment (before the broken one)
4. Click the three-dot menu ("...")
5. Select "Promote to Production"
6. Confirm - the old version is now live
7. Fix the issue and deploy again

**Method 2: Revert via GitHub**

```powershell
# View recent commits
git log --oneline

# Find the commit before the problem
# Example: abc1234 was the last good commit
# xyz5678 was the broken commit

# Revert the broken commit
git revert xyz5678

# This creates a new commit that undoes the changes
# Push to GitHub
git push origin main

# Vercel automatically deploys the reverted version
```

### 10.2 Revert a Pull Request

If a merged PR caused issues:

1. Go to the PR on GitHub
2. Click "Revert" button (if visible)
3. GitHub creates a new PR that reverts the changes
4. Merge the revert PR
5. Vercel automatically deploys the revert

---

## Part 11: Team Collaboration Workflow

### 11.1 Multi-Person Development

When working with teammates:

```
Team Member 1                Team Member 2
    ↓                            ↓
Create branch 1            Create branch 2
    ↓                            ↓
Push branch 1              Push branch 2
    ↓                            ↓
Create PR 1                Create PR 2
    ↓                            ↓
Preview deployment 1       Preview deployment 2
    ↓                            ↓
Code review & feedback     Code review & feedback
    ↓                            ↓
Merge PR 1                 Merge PR 2
    ↓                            ↓
Both changes in production
```

### 11.2 Review and Approval Process

1. Team Member A creates PR with changes
2. Team Member B reviews the PR:
   - Read the description
   - Check the code changes
   - Visit the preview deployment
   - Test the new feature
3. Team Member B leaves comments:
   - "Looks great!" - Approve
   - "Change X to Y" - Request changes
   - Questions or suggestions
4. Team Member A responds and makes adjustments
5. After approval, merge the PR

### 11.3 Handling Merge Conflicts

When two branches edit the same lines:

```powershell
# After trying to merge
git merge feature-branch

# If you get a conflict message:
# 1. Open the conflicted files
# 2. Look for sections marked with <<<<<<< and >>>>>>>>
# 3. Edit these sections to resolve the conflict
# 4. Delete the conflict markers
# 5. Save the file

# Then stage and commit
git add conflicted-file.js
git commit -m "Resolve merge conflict"

# Push the merge
git push origin main
```

---

## Part 12: Review and Approval Process

### 12.1 Code Review Best Practices

**As a reviewer:**
- Check the PR description - does it explain the change?
- Review the code changes
- Test the preview deployment
- Look for:
  - Syntax errors
  - Missing functionality
  - Performance issues
  - Security concerns

**As the developer:**
- Provide clear PR descriptions
- Keep changes focused (one feature per PR)
- Respond to feedback promptly
- Thank reviewers for their time

### 12.2 GitHub Review Features

**Requesting Reviews:**
1. Go to your PR
2. Look for "Reviewers" section (right sidebar)
3. Click the icon and select team members
4. They'll get notified to review

**Leaving Comments:**
1. In the PR, click "Files changed" tab
2. Hover over a line number
3. Click the comment icon
4. Type your comment
5. Click "Comment" to post

**Approving or Requesting Changes:**
1. Click "Review changes" button
2. Select:
   - "Approve" - Looks good, merge when ready
   - "Request changes" - Need updates before merging
   - "Comment" - Feedback without blocking
3. Click "Submit review"

---

## Part 13: Deployment Checklist

Before pushing to main and deploying to production, verify:

### 13.1 Pre-Deployment Checklist

- [ ] Code has been tested locally
- [ ] No console errors (check browser DevTools)
- [ ] New features work as expected
- [ ] No broken existing features
- [ ] Commit messages are clear and descriptive
- [ ] Code follows project style guidelines
- [ ] Documentation is updated (if needed)
- [ ] No sensitive data in code (no API keys, passwords)
- [ ] Files to ignore are in .gitignore (no node_modules pushed)
- [ ] Changes have been reviewed (if team project)

### 13.2 Pre-Production Checklist

After pull request approval, before clicking "Merge":

- [ ] Preview deployment working correctly
- [ ] All tests passing (if applicable)
- [ ] No merge conflicts
- [ ] Main branch is up to date
- [ ] All feedback has been addressed
- [ ] Commit history is clean

### 13.3 Post-Deployment Checklist

After merging and Vercel deploys:

- [ ] Production deployment shows "Ready"
- [ ] Live site loads without errors
- [ ] New features work in production
- [ ] No 404 errors
- [ ] Links work correctly
- [ ] Data is displaying correctly

---

## Part 14: Hot-Fixes for Production Issues

When a critical issue needs immediate fixing:

### 14.1 Create a Hot-Fix Branch

```powershell
# Start from main
git checkout main
git pull origin main

# Create a hotfix branch
git checkout -b hotfix/fix-login-button

# Make your changes
# Test locally thoroughly

# Commit
git commit -m "Fix login button not responsive"

# Push
git push -u origin hotfix/fix-login-button
```

### 14.2 Merge Hot-Fix Quickly

1. Create a PR for the hotfix branch
2. Keep description clear and concise
3. Review the preview deployment
4. After approval, merge immediately
5. Vercel will deploy within minutes

### 14.3 After Hot-Fix is Deployed

Once the hotfix is in production:
1. Verify the live site shows the fix
2. Alert team members that it's deployed
3. Monitor for any side effects
4. If rollback is needed, use the revert process

---

## Part 15: Version Tagging for Releases

### 15.1 Create Release Tags

When you reach a stable version worth sharing:

```powershell
# View existing tags
git tag

# Create a new tag
git tag -a v1.0.0 -m "Release version 1.0.0 - Initial deployment"

# Or tag a previous commit
git tag -a v1.0.0 COMMIT_HASH -m "Release version 1.0.0"

# Push tags to GitHub
git push origin --tags
```

### 15.2 Create GitHub Release

1. Go to your repository
2. Click "Releases" (or "Code" → scroll down to "Releases")
3. Click "Draft a new release"
4. Select your tag (e.g., v1.0.0)
5. Add release title and description
6. Click "Publish release"

**Release Notes Template:**
```
# Version 1.0.0 - Initial Release

## Features
- Dashboard with real-time water levels
- Historical data visualization
- Data export functionality

## Improvements
- Performance optimization for large datasets
- Mobile-responsive design
- Improved error handling

## Bug Fixes
- Fixed charts not loading on slow connections
- Fixed filter dropdown issues

## Known Issues
- Export to CSV not available for datasets larger than 100k rows

## Contributors
- Team members who contributed

## Download
[Links to download data/releases]
```

---

## Part 16: Daily Workflow Examples

### 16.1 Adding a New Feature

```powershell
# 1. Start fresh from main
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature/add-water-quality-filter

# 3. Make changes (edit files in your code editor)

# 4. Test locally
npm run dev
# Test at http://localhost:3000

# 5. Commit changes
git add .
git commit -m "Add water quality filter to dashboard"

# 6. Push to GitHub
git push -u origin feature/add-water-quality-filter

# 7. Create pull request on GitHub
# Go to https://github.com/YOUR-USERNAME/datathon-water-analysis
# Click "Pull requests" → "New pull request"
# Select feature/add-water-quality-filter to merge into main

# 8. Test preview deployment

# 9. Merge when ready
```

### 16.2 Fixing a Bug

```powershell
# 1. Create fix branch
git checkout main
git pull origin main
git checkout -b fix/charts-not-rendering

# 2. Find and fix the bug (edit files)

# 3. Test the fix locally
npm run dev

# 4. Commit
git add .
git commit -m "Fix charts not rendering on Safari browsers"

# 5. Push
git push -u origin fix/charts-not-rendering

# 6. Create PR and merge after testing preview
```

### 16.3 Updating Documentation

```powershell
# 1. Create docs branch
git checkout main
git pull origin main
git checkout -b docs/update-installation-guide

# 2. Edit documentation files (README.md, CONTRIBUTING.md, etc.)

# 3. Commit
git add .
git commit -m "Update installation guide with Windows instructions"

# 4. Push and create PR
git push -u origin docs/update-installation-guide

# 5. Merge after review
```

---

## Part 17: Common Issues and Solutions

### 17.1 "Your branch is behind origin/main"

```powershell
# Pull the latest changes first
git pull origin main

# Then make your changes and push
git add .
git commit -m "Your message"
git push origin feature-branch
```

### 17.2 "Merge conflict" when pushing

```powershell
# Pull and resolve
git pull origin main

# Open the conflicted files and fix them
# Then commit and push
git add conflicted-files.js
git commit -m "Resolve merge conflict"
git push origin feature-branch
```

### 17.3 Accidentally committed to main instead of a branch

```powershell
# See your recent commits
git log --oneline

# Create a new branch at your last commit
git branch feature/fix-name

# Reset main to before your commits
git reset --hard origin/main

# Switch to your feature branch
git checkout feature/fix-name

# Now continue with the feature branch
```

### 17.4 Vercel deployment fails but GitHub shows no errors

1. Check Vercel dashboard for build logs
2. Look for errors in the build output
3. Common causes:
   - Missing environment variables
   - Build command is incorrect
   - A dependency wasn't installed
4. Fix the issue locally, commit, and push again

### 17.5 Preview deployment works but production doesn't

1. Check that main branch actually has your changes
2. Verify Vercel is building from main branch
3. Hard refresh your browser (Ctrl+F5)
4. Check browser console for errors (F12)
5. If still failing, check Vercel logs for hints

---

## Quick Reference: Complete Workflow Command

```powershell
# ===== SETUP (one time) =====
git clone https://github.com/YOUR-USERNAME/datathon-water-analysis.git
cd datathon-water-analysis
git config user.name "Your Name"
git config user.email "your.email@example.com"

# ===== START NEW FEATURE =====
git checkout main
git pull origin main
git checkout -b feature/your-feature-name

# ===== DEVELOPMENT =====
# Edit files, test locally, repeat...

# ===== COMMIT AND PUSH =====
git status
git add .
git commit -m "Description of changes"
git push -u origin feature/your-feature-name

# ===== CREATE PR ON GITHUB =====
# Visit https://github.com/YOUR-USERNAME/datathon-water-analysis
# Click "Pull requests" → "New pull request"
# Create PR and test preview deployment

# ===== MERGE TO PRODUCTION =====
# Click "Merge pull request" on GitHub
# Vercel automatically deploys!

# ===== BACK TO MAIN =====
git checkout main
git pull origin main
# Ready to start next feature
```

---

## Best Practices Summary

1. **Always use feature branches** - Never work directly on main
2. **Write clear commit messages** - Help your future self and teammates
3. **Test before pushing** - Verify changes work locally first
4. **Use pull requests** - Even for solo projects, they're useful
5. **Test preview deployments** - Review changes before going live
6. **Keep main stable** - Only merge reviewed, tested code
7. **Pull regularly** - Keep your branch up to date with main
8. **Communicate with team** - Use PR descriptions and comments
9. **Monitor deployments** - Check Vercel dashboard after merging
10. **Have a rollback plan** - Know how to revert if needed

---

## Next Steps

- **Initial Setup:** Follow GITHUB_SETUP.md
- **Deploy to Vercel:** Follow VERCEL_DEPLOYMENT.md
- **Share with Partners:** Follow PARTNER_SHARING.md

---

## Resources

- Git Documentation: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com/
- GitHub PR Guide: https://docs.github.com/en/pull-requests
- Vercel Deployments: https://vercel.com/docs/concepts/deployments/overview
- Git Workflows: https://www.atlassian.com/git/tutorials/comparing-workflows

