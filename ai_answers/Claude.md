<!-- markdownlint-disable-file -->

# Vibe / Context Coding FAQ — Answers

**Covering OpenCode and Claude Code | Updated March 2026**

* * *

## A Quick Note on Your Setup

You're using **OpenCode** (terminal/TUI agent, BYOM, open-source, ~95K GitHub stars) inside VS Code, and planning to add **Claude Code** (Anthropic's official terminal agent). The good news: these two tools share almost identical conventions. Both read `AGENTS.md` / `CLAUDE.md`, both use `.opencode/` or `.claude/` for commands and agents, and both respect `.gitignore`. Where behavior differs, this document calls it out explicitly.

* * *

## GIT / GITHUB

### Should I create a GitHub repo first and then clone it, or let the agent create it for me?

**Create the GitHub repo first, then clone it locally.** This is the cleanest workflow and is what the tools expect. Here's why:

1.  You get a remote from day one, which means every `git push` is a real backup.
2.  OpenCode and Claude Code read your git root to set their working directory — having an initialized repo before you start a session means they always have proper context.
3.  Both tools integrate with the `gh` CLI for creating issues and PRs; that integration assumes the remote already exists.

Practical steps:

```bash
# On GitHub: create an empty repo (no README, no .gitignore yet)
gh repo create my-project --private
git clone https://github.com/yourname/my-project.git
cd my-project
```

Then run `/init` (Claude Code) or the equivalent setup step in OpenCode to scaffold your `AGENTS.md` / `CLAUDE.md`.

* * *

### Should I include OpenCode or Claude Code config directories in `.gitignore`?

**Partially — here is the definitive breakdown:**

| Path | Commit? | Why |
| --- | --- | --- |
| `.opencode/agents/*.md` | ✅ Yes | Project-specific agents — share with team |
| `.opencode/commands/*.md` | ✅ Yes | Slash commands — share with team |
| `opencode.json` (project root) | ✅ Yes | Project config — safe to commit, no secrets |
| `.claude/commands/*.md` | ✅ Yes | Share slash commands |
| `AGENTS.md` (project root) | ✅ Yes | Core context file — always commit |
| `CLAUDE.md` (project root) | ✅ Yes | Core context file — always commit |
| `CLAUDE.local.md` | ❌ No | Personal overrides — auto-gitignored |
| `~/.config/opencode/` (global) | N/A | Lives outside repo |
| `~/.claude/` (global) | N/A | Lives outside repo |
| `.env`, `.env.*` | ❌ No | Secrets — never commit |

Add this to your `.gitignore`:

```
CLAUDE.local.md
.env
.env.*
*.pem
*.key
```

OpenCode's internal tools (grep, glob, list) already respect `.gitignore` patterns via ripgrep — files you ignore from git are also hidden from the agent's searches.

* * *

### As a solo developer, should I use branches and PRs, or just commit directly to main?

**Use feature branches — even solo.** This is not bureaucracy; it's a superpower with AI agents:

**Why branches matter with AI agents:**

- Claude Code and OpenCode write files directly to your working directory. If you're on `main` and the agent goes off-track, a branch lets you `git checkout main` and start fresh with no damage.
- Both tools support **git worktrees**, which let you run multiple agent sessions in parallel — each on its own branch. This is one of the highest-leverage workflows available: while one Claude session is building a feature, another can be fixing a bug, with zero interference.
- Claude Code has a `--worktree` flag built in: `claude --worktree feature-auth` creates an isolated directory automatically.

**Recommended solo workflow:**

```bash
# Start each feature on a branch
git checkout -b feature/user-auth

# Let the agent work
claude  # or opencode

# Review the diff, then merge
git push -u origin feature/user-auth
gh pr create --base main  # optional but good habit
```

You don't need formal PR reviews solo, but the branch structure gives you a clean diff to review before merging, and a safe revert point if the AI created something unexpected.

* * *

## PREPARATORY WORK

### Should I create context files before starting a session?

**Yes — this is the single highest-leverage thing you can do.** Both tools read context files at session start. An agent that knows your project structure, constraints, and tech stack will make far fewer wrong assumptions.

The recommended workflow for a new project:

1.  Write a brief `PRD.md` (product requirements document) describing what you're building — 1-2 pages maximum.
2.  Run `/init` in Claude Code or start OpenCode and ask it to generate `AGENTS.md` based on your PRD. Both tools will scan the project and generate a starter file.
3.  Review and refine what was generated — the auto-generated file is a starting point, not a finished product.

* * *

### One file or multiple files?

**Multiple files, with a clear hierarchy.** Think of it like a briefing structure:

```
project/
├── AGENTS.md          ← Main context file (read every session)
├── PRD.md             ← Product requirements (referenced from AGENTS.md)
├── SPEC.md            ← Technical spec / implementation plan
├── docs/
│   ├── architecture.md
│   └── api-conventions.md
└── .opencode/
    └── commands/
        └── review.md  ← Custom slash command
```

The key principle is **progressive disclosure**: `AGENTS.md` stays short and points to detailed files. Claude only loads the detailed files when the task requires them. This prevents your context window from filling up with irrelevant information at session start.

* * *

### What should go in the main context file, and how long should it be?

**Keep `AGENTS.md` / `CLAUDE.md` under 200 lines.** Files longer than this start consuming too much of the context window and, counterintuitively, the agent starts ignoring instructions — both Claude Code and OpenCode inject this file as a system reminder that the model may skip if it deems it irrelevant.

**The WHY / WHAT / HOW pattern:**

```markdown
# Project Name
One-line description. One-line tech stack summary.

## Why This Exists
What problem does this solve? Who is it for?

## Architecture
Key directories and their purpose:
- `src/api/` — REST handlers
- `src/models/` — SQLAlchemy models
- `src/services/` — Business logic

## Tech Stack
- Runtime: Node 22 / Python 3.12
- Framework: FastAPI
- DB: PostgreSQL via SQLAlchemy
- Tests: pytest

## Commands
```bash
npm run dev       # start dev server
npm run test      # run tests
npm run lint      # eslint + mypy
```

## Coding Conventions

- TypeScript strict mode
- Functional components only (React)
- All functions must have type hints (Python)
- Tests required for new modules

## Important Rules

- Never modify the database schema without a migration file
- Use the custom logger in `src/utils/logger.py`, not print/console.log
- Read `docs/api-conventions.md` before touching the API layer

```
What to **exclude**: exhaustive documentation of every file, instructions that only apply to one rare task, coding style rules enforceable by a linter (use a linter instead).

---

### Should I decide the tech stack, or let the agent suggest one?

**You decide the stack; let the agent fill in the details.** Here's why: the agent will suggest whatever is popular and well-documented (React, Next.js, FastAPI, etc.) — but it has no knowledge of your personal preferences, hosting constraints, or what you already know. Those are things only you know.

A good approach:
1. Write your constraints in `PRD.md`: "I want a Python backend, I'm hosting on a VPS, I don't want to learn Kubernetes."
2. Ask the agent: "Given these constraints, suggest a tech stack and explain the tradeoffs."
3. Discuss and decide together, then document the final choice in `AGENTS.md`.

---

### What should the preliminary files be named, and where should they live?

Use this naming convention, which is compatible with both tools:

| File | Location | Commit? | Purpose |
|------|----------|---------|---------|
| `AGENTS.md` | Project root | ✅ Yes | Main context (read every session) |
| `CLAUDE.md` | Project root | ✅ Yes | Fallback if no AGENTS.md (Claude Code) |
| `PRD.md` | Project root or `docs/` | ✅ Yes | Product requirements |
| `SPEC.md` | Project root or `docs/` | ✅ Yes | Technical specification / implementation plan |
| `CHANGELOG.md` | Project root | ✅ Yes | Log of changes (can be AI-maintained) |
| `CLAUDE.local.md` | Project root | ❌ No | Personal overrides, never shared |

You don't need a separate directory for these — keeping them in the project root means both tools find them without configuration.

---

## BEST PRACTICES

### What other files does a vibe/context coding project need?

Beyond the context files above, a well-structured project includes:

**`.opencode/` or `.claude/` directory (commit these):**
```

.opencode/ ├── commands/ │ ├── review.md ← /project:review — runs a code review │ ├── ship.md ← /project:ship — lint, test, commit, push │ └── process-issue.md ← /project:process-issue \$ISSUE_URL └── agents/ └── reviewer.md ← Custom review-only agent (read-only permissions)

```
**Root-level files:**
- `.gitignore` — standard for your stack + `CLAUDE.local.md`
- `README.md` — project documentation for humans
- `CHANGELOG.md` — ask the agent to update this after every feature
- `.env.example` — template for environment variables (commit this; not `.env`)

**Custom slash commands are one of the highest-leverage investments you can make.** A `/project:ship` command that runs your linter, tests, writes a commit message, and pushes — created once and reused forever — saves enormous repetitive prompting.

---

### Should I create agents, MCP servers, and tools in advance, or let the agent create them?

**In advance, for anything you'll use repeatedly. Let the agent create one-off tools.**

- **Agents** (OpenCode) / **Subagents** (Claude Code): Create a `reviewer` or `planner` agent in advance — these are used constantly and benefit from careful setup. OpenCode comes with `Build` (all tools, default) and `Plan` (read-only) agents built in; add custom ones as your workflow matures.
- **Slash commands**: Create these early. They're markdown files — trivial to write and immediately useful.
- **MCP servers**: Add MCP servers for services you use constantly (GitHub, Notion, your database). Run `claude mcp add` or configure in `opencode.json`. Don't pre-install MCP servers for things you might need someday.
- **Skills** (Claude Code): These are folder-based bundles of prompts + scripts. Build them after you've identified patterns — when you find yourself giving the same 10-line explanation every session, that's a skill.

---

### Should agents, MCP servers, and tools be global or project-specific?

**Both levels serve different purposes:**

| Level | Location | Use for |
|-------|----------|---------|
| Global | `~/.config/opencode/` or `~/.claude/` | Personal preferences, your coding style, tools you use in every project |
| Project | `.opencode/` or `.claude/` in project root | Project-specific agents, commands, conventions — share with team via git |

**Practical split for a solo developer:**
- Global `AGENTS.md`: your preferred code style, that you always use TypeScript strict mode, your commit message format.
- Project `AGENTS.md`: this specific project's architecture, stack, commands, and rules.
- Global commands: `/review`, `/daily-standup` — things you do in every project.
- Project commands: `/process-issue`, `/deploy-staging` — project-specific workflows.

---

### Is there a standard log file for changes and tasks?

**`CHANGELOG.md` is the standard,** following the [Keep a Changelog](https://keepachangelog.com) format. You can ask the agent to maintain it:

```markdown
## Instruction in AGENTS.md
After completing any feature or significant change, update CHANGELOG.md 
following Keep a Changelog format (https://keepachangelog.com).
```

For task tracking within sessions, many developers have the agent write a `TASKS.md` or a `plan.md` at the start of a complex feature. This becomes working memory that persists across sessions — when you come back to a project after a few days, `/init` or reading `TASKS.md` brings the agent back up to speed without repeating context.

* * *

### Are you missing anything important?

**Yes — several things that experienced vibe/agentic coders consider essential:**

**Context window hygiene:** Use `/clear` between distinct tasks (Claude Code) or start a new session (OpenCode) when switching to a new feature. Accumulated context from a previous task confuses the agent and wastes token budget.

**The plan-before-code loop:** Before writing any significant feature, ask the agent to write a plan to `SPEC.md` and confirm it with you *before* touching code. This is the single most effective way to avoid long debugging sessions caused by the agent misunderstanding your intent. Claude Code has a built-in `Plan` mode (Shift+Tab twice) that physically prevents the agent from writing files until you approve.

**Tight feedback loops:** Don't let the agent work for 20 minutes unattended on a complex task. Check in every few steps. Course-correct early — it's much faster to redirect than to debug a large block of wrong code.

**Git as your undo button:** Commit before any significant agent action. If the agent goes off-track, `git checkout .` resets everything. Claude Code's snapshot system provides in-session undo, but git is your persistent safety net.

**Security hygiene with AI agents:** Never put secrets (API keys, passwords, tokens) in files the agent can read. Use `.env` files (gitignored) and reference them via environment variables. For OpenCode, the `opencode-ignore` plugin can explicitly block the agent from reading sensitive files even if they're in the project directory.

**Agentic engineering mindset (the 2026 evolution of vibe coding):** Andrej Karpathy — who coined "vibe coding" in February 2025 — publicly updated his thinking in early 2026, calling the more mature approach "agentic engineering": you remain the architect, the AI is a very fast junior developer. Guide it with clear specs, review its output, and own the result. Fully accepting AI output without review leads to security issues and accumulated technical debt.

* * *

## RESOURCES

### Official Documentation

| Resource | URL |
| --- | --- |
| OpenCode official docs | https://opencode.ai/docs/ |
| OpenCode GitHub (source + issues) | https://github.com/opencode-ai/opencode |
| OpenCode config reference | https://opencode.ai/docs/config/ |
| OpenCode rules / AGENTS.md | https://opencode.ai/docs/rules/ |
| OpenCode agents | https://opencode.ai/docs/agents/ |
| OpenCode tools | https://opencode.ai/docs/tools/ |
| OpenCode IDE integration (VS Code) | https://opencode.ai/docs/ide/ |
| Claude Code official docs | https://code.claude.com/docs/en/overview |
| Claude Code best practices | https://code.claude.com/docs/en/best-practices |
| Claude Code common workflows | https://code.claude.com/docs/en/common-workflows |
| Claude Code changelog (GitHub) | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md |

* * *

### High-Quality Guides and Articles

| Resource | URL | Notes |
| --- | --- | --- |
| Using CLAUDE.md files (Anthropic blog) | https://claude.com/blog/using-claude-md-files | Official best practices |
| Writing a good CLAUDE.md (HumanLayer) | https://www.humanlayer.dev/blog/writing-a-good-claude-md | Deep dive on context engineering |
| How I Use Every Claude Code Feature (Shrivu Shankar) | https://blog.sshh.io/p/how-i-use-every-claude-code-feature | Practical, opinionated guide |
| Anatomy of the .claude/ Folder (Daily Dose of DS) | https://blog.dailydoseofds.com/p/anatomy-of-the-claude-folder | Structure reference |
| Parallel Vibe Coding with Git Worktrees | https://www.dandoescode.com/blog/parallel-vibe-coding-with-git-worktrees | Worktrees + Claude Code |
| Claude Code Best Practices (shanraisshan) | https://github.com/shanraisshan/claude-code-best-practice | Curated community list |
| Claude Code settings and agents (feiskyer) | https://github.com/feiskyer/claude-code-settings | Example commands/agents |
| Claude Code: The Complete Guide (Sid Bharath) | https://www.siddharthbharath.com/claude-code-the-complete-guide/ | Comprehensive tutorial |
| awesome-opencode | https://github.com/awesome-opencode/awesome-opencode | Curated plugins, themes, agents |

* * *

### Staying Current — News and Updates

| Resource | URL | What to Follow |
| --- | --- | --- |
| OpenCode changelog / releases | https://github.com/opencode-ai/opencode/releases | Watch for new releases |
| Claude Code changelog (fast mirror) | https://claudefa.st/blog/guide/changelog | Updated within hours of releases |
| Anthropic news | https://www.anthropic.com/news | Major Claude Code announcements |
| The New Stack — AI Engineering | https://thenewstack.io/category/ai/ | Industry trends, agentic engineering |
| Vibe Coding Newsletter (weekly) | https://www.vibecoding-newsletter.com/ | Free weekly digest |
| Alex Cloudstar's blog | https://www.alexcloudstar.com/blog/ | Context engineering, vibe coding trends |
| r/ClaudeAI (Reddit) | https://www.reddit.com/r/ClaudeAI/ | Community tips, issue reports |
| r/vibecoding (Reddit) | https://www.reddit.com/r/vibecoding/ | Community discussion |
| Anthropic on X/Twitter | https://x.com/AnthropicAI | Real-time announcements |
| OpenCode on X/Twitter | https://x.com/opencodeai | OpenCode-specific updates |

* * *

### Community and Templates

| Resource | URL |
| --- | --- |
| Claude Code workflows (shinpr) | https://github.com/shinpr/claude-code-workflows |
| Claude Code Docs / guides aggregator | https://claudelog.com/claude-code-tutorial/ |
| State of Vibe Coding 2026 (Taskade) | https://www.taskade.com/blog/state-of-vibe-coding-2026 |
| Keep a Changelog (CHANGELOG format) | https://keepachangelog.com |

* * *

## QUICK REFERENCE CHEATSHEET

```
New project checklist:
□ Create GitHub repo → clone locally
□ Write PRD.md (what + why + constraints)
□ Run /init to generate AGENTS.md → review and refine
□ Add .gitignore (include CLAUDE.local.md, .env)
□ Create .opencode/commands/ with your core slash commands
□ Set up global ~/.config/opencode/AGENTS.md with personal preferences
□ Install gh CLI for GitHub integration
□ Connect MCP servers you use daily (run: claude mcp add or opencode config)

Per-session workflow:
□ Start on a feature branch (git checkout -b feature/name)
□ Ask agent to plan first → confirm → then code
□ /clear between distinct tasks
□ Commit frequently — git is your undo button
□ Update CHANGELOG.md after features

Files to always commit:
□ AGENTS.md / CLAUDE.md
□ opencode.json (project config)
□ .opencode/commands/*.md
□ .opencode/agents/*.md
□ PRD.md, SPEC.md, CHANGELOG.md
□ .env.example (not .env)
```
