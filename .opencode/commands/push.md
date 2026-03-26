---
description: Stage, commit, and push pending changes
---

Stage all pending changes, create a commit with a descriptive message, and push to the remote repository.

## Steps

1. Run `git status` to show what will be committed
2. Run `git diff` to show the actual changes
3. Run `git log --oneline -5` to review recent commit style
4. Draft a concise, descriptive commit message (e.g., "Add error handling to user validation")
5. Run `git add .` to stage all changes
6. Run `git commit -m "<message>"` with the drafted message
7. Run `git push` to push to remote
8. Confirm success with `git status`

## Do NOT

- Commit secrets or API keys
- Amend previous commits
- Force push to main/master
