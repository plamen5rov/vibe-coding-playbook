# Git & GitHub for Vibe Coding

## Create the repo yourself — always

All 10 AI models surveyed agree on this: **create the GitHub repo first, then clone locally.**

```bash
# Option A: GitHub CLI (recommended)
gh repo create my-project --private
git clone https://github.com/yourname/my-project.git
cd my-project

# Option B: Create on GitHub.com, then:
git clone https://github.com/yourname/my-project.git
cd my-project
```

**Why not let the AI create the repo?**

- You lose control over visibility, license, and `.gitignore` templates.
- Auth and remote-origin setup is less reliable when agent-initialized.
- Both OpenCode and Claude Code work best when the remote already exists — they rely on `git` context and `gh` CLI integrations that assume a proper remote.

Start with an empty repo (no README, no `.gitignore`) if you plan to add your own `AGENTS.md` and context files immediately. Add README + `.gitignore` if you want GitHub's templates.

---

## What to commit, what to ignore

This is the most misunderstood topic for new vibe coders. The rule is: **commit context, ignore secrets and local state.**

| File / Path | Commit? | Why |
| --- | --- | --- |
| `AGENTS.md` / `CLAUDE.md` | ✅ Yes | Core context — always commit |
| `opencode.json` (project-level) | ✅ Yes | Project config, no secrets |
| `.opencode/commands/*.md` | ✅ Yes | Slash commands — share across machines |
| `.opencode/agents/*.md` | ✅ Yes | Project-specific agents |
| `.claude/commands/*.md` | ✅ Yes | Same for Claude Code |
| `.claude/settings.json` | ✅ Yes | Permission rules — share with team |
| `docs/` context files | ✅ Yes | Part of project intelligence |
| `.env` | ❌ No | Secrets — never commit |
| `.env.*` (except `.env.example`) | ❌ No | Secrets |
| `CLAUDE.local.md` | ❌ No | Personal overrides — auto-gitignored |
| `.claude/settings.local.json` | ❌ No | Personal permission overrides |
| `node_modules/`, `dist/`, `build/` | ❌ No | Generated — always ignore |

**The `.env.example` pattern:** commit this file with all variable names but empty values. It shows the AI (and your future self) what environment variables exist without exposing secrets.

```bash
# .env.example — commit this
DATABASE_URL=
API_KEY=
SECRET_TOKEN=

# .env — never commit this
DATABASE_URL=postgres://user:pass@localhost/mydb
API_KEY=sk-abc123...
SECRET_TOKEN=supersecret
```

**Security note:** Even if `.env` is in `.gitignore`, some agents may still read it if they have file access. In OpenCode, the `opencode-ignore` plugin can explicitly block the agent from reading specific files. In Claude Code, use `deny` rules in `.claude/settings.json`.

---

## Branches and PRs — even solo

**Use feature branches, even as a solo developer.** This is the unanimous recommendation from experienced vibe coders.

**Why branches matter with AI agents specifically:**

- OpenCode and Claude Code write directly to your working directory. If the agent goes off-track on `main`, you have no clean rollback point.
- A branch lets you `git checkout main && git branch -D bad-branch` to discard everything and start fresh.
- Claude Code supports `--worktree` to run multiple sessions in parallel, each on their own branch.

### Recommended solo workflow

```bash
# Start each feature on a branch
git checkout -b feature/user-auth

# Work with the agent
opencode  # or: claude

# Review the diff before merging
git diff main

# Merge when satisfied
git checkout main
git merge feature/user-auth
git push
```

### PR workflow (optional but good habit)

```bash
git push -u origin feature/user-auth
gh pr create --base main --title "Add user auth" --body "Implemented via OpenCode session"
# Review the PR diff on GitHub
gh pr merge --squash
```

You don't need formal PR reviews when solo. But the PR diff view on GitHub is a clean way to review everything the agent did before it hits `main`.

### Commit frequently

Treat `git commit` as your undo button. Commit before any significant agent action. If the agent produces something unexpected, `git checkout .` resets the working directory to the last commit.

```bash
# Before asking the agent to do something large
git add . && git commit -m "checkpoint before refactor"

# After the agent finishes and you've reviewed
git add . && git commit -m "feat: add user authentication"
```

Ask the agent to write commit messages — both OpenCode and Claude Code are good at conventional commit format.

---

## The `.gitignore` for a vibe-coding project

Use the `starter-template/.gitignore` in this repo as a base. Key additions beyond the standard:

```gitignore
# AI tool — personal overrides only
CLAUDE.local.md
.opencode/config.local.json
.claude/settings.local.json

# Secrets
.env
.env.*
!.env.example
```

Do **not** ignore `.opencode/` or `.claude/` wholesale — the commands, agents, and settings inside them are project context that should travel with the repo.
