# 🗃️ Git Quick Commands Cheat Sheet



## 🚀 Initialize Local Repository
```bash
# Initialize a new Git repository
git init

# Add all files to staging area
git add .

# Commit with a message
git commit -m "initial commit"

# Add remote origin
git remote add origin <repo-link>

# Rename branch to main
git branch -M main

# Force pull from remote with rebase
git pull origin main --rebase

# Push local commits to remote
git push origin main
```




## 🔗 Remote Repositories
```bash
# Check remote repository URLs
git remote -v

```



## ✅ Stage Changes
```bash
# Add all changes to staging area
git add -A
```



## 👤 Configure Git User
```bash
# Set global username
git config --global user.name "Your Name"

# Set global user email
git config --global user.email "you@example.com"
```




## 📥 Clone a Repository
```bash
# Clone a remote repository
git clone <repo-url>
```




## 🌿 Branch Management
```bash
# List all branches
git branch

# Create a new branch
git branch <branch-name>

# Switch to another branch
git switch <branch-name>

# Alternative: checkout to another branch
git checkout <branch-name>

# Merge a branch into current branch
git merge <branch-name>

# Delete a branch
git branch -d <branch-name>
```




## 🗑️ Remove Files from Tracking
```bash
# Delete a file from Git and disk
git rm <file-name>

# Remove a file from tracking but keep it on disk
git rm --cached -r <file-name>
```






## 📜 View Commit History
```bash
# View commit history
git log

# Compact log view with branch graph
git log --oneline --graph

# Show details of a specific commit
git show <commit-hash>
```


## 🏷️ Tags
```bash
# List all tags
git tag

# Create a tag
git tag <tag-name>

# Push a tag to remote
git push origin <tag-name>
```


## 🧹 Remove Committed Files with git-filter-repo
```bash
# Install git-filter-repo
pip install git-filter-repo

# Remove file from Git history after it’s committed
git filter-repo --force --path <file-to-remove> --invert-paths
```


