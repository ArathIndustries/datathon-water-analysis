# GitHub Setup Guide for Datathon Water Analysis Project

## Overview
This guide walks you through setting up a new GitHub repository for the Datathon Water Analysis project and uploading all project files. Follow each step carefully to ensure proper setup.

---

## Part 1: Prerequisites

### 1.1 Create a GitHub Account
If you don't already have a GitHub account:

1. Go to https://github.com
2. Click the "Sign up" button in the top-right corner
3. Enter your email address, create a password, and choose a username
4. Complete the verification steps
5. Choose the free plan when prompted
6. Verify your email address by clicking the link sent to your inbox

### 1.2 Install Git on Your Computer
Download and install Git from: https://git-scm.com/downloads

**For Windows:**
- Download the Windows installer
- Run the installer and follow the default options
- After installation, open PowerShell and verify: `git --version`

### 1.3 Configure Git (First Time Only)
Open PowerShell and run these commands (replace with your information):

```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify configuration:
```powershell
git config --global user.name
git config --global user.email
```

---

## Part 2: Create the GitHub Repository

### 2.1 Create a New Repository on GitHub

1. Log in to your GitHub account at https://github.com
2. Click the "+" icon in the top-right corner
3. Select "New repository"
4. Fill in the repository details:
   - **Repository name:** `datathon-water-analysis`
   - **Description:** `Water level and quality analysis dashboard for Texas water bodies using TWDB and USGS data`
   - **Visibility:** Select "Public" (for sharing with project partners)
   - **Initialize this repository with:**
     - Check "Add a .gitignore" and select "Node" from the dropdown (or "Python" if applicable)
     - Check "Choose a license" and select "MIT License" (or "CC-BY-4.0" for data projects)
   - Leave other options unchecked

5. Click "Create repository"

**Screenshot Reference:** You should see these highlighted options in the GitHub web interface:
- Repository name field at the top
- Public/Private toggle switch
- "Add a .gitignore" checkbox with dropdown menu
- "Choose a license" checkbox with dropdown menu
- Green "Create repository" button at the bottom

### 2.2 Repository Settings (Optional but Recommended)

After creating the repository:

1. Go to your repository at `https://github.com/YOUR-USERNAME/datathon-water-analysis`
2. Click the "Settings" tab
3. Update the following:
   - **Description:** Ensure it matches your intended purpose
   - **Website:** Add project website URL if applicable
   - **Topics:** Add tags like `water-analysis`, `datathon`, `texas`, `environmental-data`

---

## Part 3: Clone Repository to Your Local Machine

### 3.1 Get the Repository URL

1. On your GitHub repository page (https://github.com/YOUR-USERNAME/datathon-water-analysis)
2. Click the green "Code" button
3. Copy the HTTPS URL (it will look like: `https://github.com/YOUR-USERNAME/datathon-water-analysis.git`)

**Screenshot Reference:** The green "Code" button is in the upper right of the file list area, showing a dropdown with HTTPS/SSH options.

### 3.2 Clone to Your Local Machine

Open PowerShell and navigate to where you want to store your project:

```powershell
# Navigate to your desired directory
cd "C:\Users\YourUsername\Documents"

# Clone the repository
git clone https://github.com/YOUR-USERNAME/datathon-water-analysis.git

# Enter the repository directory
cd datathon-water-analysis
```

You now have a local copy of the empty repository.

---

## Part 4: Add Project Files

### 4.1 Copy Project Files

Copy all files from the Datathon project directory to your cloned repository:

**PowerShell Command:**
```powershell
# Set source and destination paths
$source = "D:\Automation_Station\Projects\Datathon\web\docs\*"
$destination = "C:\Path\To\Your\datathon-water-analysis\"

# Copy all files (keeping directory structure)
Copy-Item -Path $source -Destination $destination -Recurse -Force
```

Or manually:
1. Open File Explorer
2. Navigate to your original Datathon project folder: `/Volumes/Arath/Automation_Station/Projects/Datathon/web/docs/`
3. Select all files (Ctrl+A)
4. Copy them (Ctrl+C)
5. Navigate to your cloned repository folder
6. Paste the files (Ctrl+V)

### 4.2 Verify Files Were Added

```powershell
# List files in the repository
git status

# This should show all the files you just added as "Untracked files"
```

### 4.3 Understand .gitignore

The .gitignore file (created when you initialized the repository) tells Git which files to ignore. Common ignored files:
- `node_modules/` - npm packages
- `.env` - environment variables and secrets
- `dist/` - compiled/build files
- `.DS_Store` - macOS system files
- Large data files (optional)

**Do NOT commit:**
- API keys or secrets
- Personal configuration files
- Large binary files (unless necessary)

---

## Part 5: Create Initial Commit

### 5.1 Stage Files for Commit

```powershell
# Stage all files for commit
git add .

# Verify files are staged
git status
```

You should see green text listing all the files that will be committed.

### 5.2 Create Your First Commit

```powershell
git commit -m "Initial commit: Add Datathon water analysis project files

- Add dashboard and data visualization components
- Include TWDB and USGS data integration
- Add project documentation
- Configure build and deployment settings"
```

**Commit Message Guidelines:**
- First line: Short summary (50 characters or less)
- Blank line
- Detailed description (optional but recommended):
  - What was added/changed
  - Why it was changed
  - Any relevant context

### 5.3 Verify the Commit

```powershell
# View commit history
git log --oneline

# Should show your commit message
```

---

## Part 6: Push to GitHub

### 6.1 Push Your Commits

```powershell
# Push your commits to the remote repository
git push -u origin main
```

**Note:** If you get an authentication error, you may need to set up Git credentials. See the troubleshooting section below.

### 6.2 Verify on GitHub

1. Go to https://github.com/YOUR-USERNAME/datathon-water-analysis
2. Refresh the page
3. You should now see all your files in the repository
4. Click on the commit link (showing the commit hash) to view your commit details

**Screenshot Reference:** In the file list area, you should see your project files listed. Above the file list, you'll see "Initial commit" with a timestamp.

---

## Part 7: Setting Up Collaborators

If you want to add project partners as collaborators:

### 7.1 Invite Collaborators

1. Go to your repository: https://github.com/YOUR-USERNAME/datathon-water-analysis
2. Click "Settings" tab
3. In the left sidebar, click "Collaborators"
4. Click "Add people"
5. Search for your project partner's GitHub username
6. Select the appropriate permission level:
   - **Pull access (read-only):** View files, cannot make changes
   - **Push access (read/write):** Can view and push code changes
   - **Admin access:** Full control including settings
7. Click "Invite" and they'll receive an invitation

**Recommendation:** Start with "Pull access" and upgrade as needed.

---

## Part 8: Optional - Repository Protection Rules

To prevent accidental pushes to the main branch:

### 8.1 Enable Branch Protection

1. Go to your repository Settings
2. Click "Branches" in the left sidebar
3. Under "Branch protection rules," click "Add rule"
4. Enter "main" in the branch name pattern
5. Check these options:
   - "Require a pull request before merging"
   - "Require status checks to pass before merging"
6. Click "Create"

This requires all changes to go through a pull request (PR) process before being merged.

---

## Part 9: Optional - GitHub Pages Setup

To serve your project as a website directly from GitHub:

### 9.1 Enable GitHub Pages

1. Go to your repository Settings
2. Scroll down to "GitHub Pages" section
3. Under "Source," select the branch to publish from (usually "main")
4. Select the folder: "/" (root) if files are at the top level, or "/docs" if they're in a docs folder
5. Click "Save"

Your site will be available at: `https://YOUR-USERNAME.github.io/datathon-water-analysis`

**Note:** If using Vercel for deployment (recommended), you don't need GitHub Pages.

---

## Troubleshooting

### Error: "fatal: not a git repository"
- Make sure you're in the cloned repository directory
- Run `git status` to verify you're in a Git repository

### Error: "fatal: origin already exists"
- The remote is already configured
- Run `git remote -v` to see existing remotes

### Error: "Please tell me who you are" when committing
- Configure your Git user info (see Part 1.3)
- Run the user.name and user.email commands again

### Error: Authentication failed when pushing
**On Windows, use these steps:**

1. Open PowerShell
2. If you haven't set up GitHub credentials:
   ```powershell
   git config --global user.email "your.email@example.com"
   git config --global user.name "Your Name"
   ```
3. When prompted for authentication, you have two options:

**Option A: Use Personal Access Token (Recommended)**
- Go to https://github.com/settings/tokens
- Click "Generate new token"
- Name it "datathon-project"
- Select scopes: `repo`, `workflow`
- Copy the token
- When Git asks for password, paste the token instead

**Option B: Set up SSH Keys (Advanced)**
- Follow GitHub's SSH setup guide: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
- Use SSH URL instead of HTTPS when cloning

### Error: "Updates were rejected because the tip of your current branch is behind"
```powershell
# Pull latest changes first
git pull origin main

# Then push your changes
git push origin main
```

### Files not showing up after push
- Check that files weren't excluded by .gitignore
- Verify they were staged and committed (git status)
- Wait a few seconds for GitHub to refresh
- Hard refresh your browser (Ctrl+F5)

---

## Next Steps

1. **Share with collaborators:** Send them the repository URL
2. **Set up deployment:** Follow the VERCEL_DEPLOYMENT.md guide
3. **Create workflow:** Follow the GITHUB_VERCEL_INTEGRATED_WORKFLOW.md guide
4. **Share with partners:** Follow the PARTNER_SHARING.md guide

---

## Quick Reference Commands

```powershell
# Check status
git status

# Stage files
git add .
git add filename.txt          # Stage specific file

# Commit
git commit -m "Your message"

# Push
git push origin main
git push origin feature-branch  # Push specific branch

# Pull
git pull origin main

# View history
git log --oneline
git log --graph --all --oneline  # Show branch graph

# Create branch
git checkout -b feature-name
git push -u origin feature-name

# Switch branch
git checkout branch-name
```

---

## Resources

- GitHub Getting Started: https://docs.github.com/en/get-started
- Git Documentation: https://git-scm.com/doc
- GitHub CLI: https://cli.github.com/ (advanced alternative to Git)
- GitHub Desktop: https://desktop.github.com/ (GUI alternative)

