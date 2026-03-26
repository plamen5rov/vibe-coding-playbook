<!-- markdownlint-disable-file -->

# COMPREHENSIVE FAQ: VIBE/CONTEXT CODING WITH OPENCODE & CLAUDE CODE

> **Version:** 2025-03-26 | **Status:** Latest Best Practices | **Target:** OpenCode (VS Code) + Claude Code (Local/Cloud)

---

## TABLE OF CONTENTS

1. [Git/GitHub Workflow](#1-gitgithub-workflow)
2. [Preparatory Work & Context Files](#2-preparatory-work--context-files)
3. [Best Practices & Project Structure](#3-best-practices--project-structure)
4. [Resources & Official Documentation](#4-resources--official-documentation)

---

## 1. GIT/GITHUB WORKFLOW

### 1.1 Should I create a GitHub repo first, or let the AI create it for me?

**Answer:** Create the GitHub repo yourself first, then clone it locally. Here's why:

| Approach | Recommendation | Reasoning |
|----------|---------------|-----------|
| **You create repo first** | ✅ **RECOMMENDED** | You control repo settings, visibility, license, and initial structure. Clone with `git clone <repo-url>` then start OpenCode/Claude Code in that directory. |
| **AI creates repo** | ⚠️ Possible but risky | Claude Code can use `gh` CLI to create repos, but you lose control over initial setup (license, .gitignore templates, visibility). |

**Best Practice:**
```bash
# 1. Create repo on GitHub (with README, .gitignore, license)
# 2. Clone locally
git clone https://github.com/username/my-project.git
cd my-project
# 3. Now start your AI coding session
claude  # or start OpenCode in VS Code
```

**For Solo Developers:** Even if working alone, use GitHub for backup and the ability to review your own PRs later. [^1^]

---

### 1.2 Should I include OpenCode/Claude Code config directories in .gitignore?

**Answer:** Yes, selectively. Commit shared configs, ignore personal ones.

**Standard .gitignore for AI Coding:**

```gitignore
# ============================================
# AI CODING ASSISTANT CONFIGURATIONS
# ============================================

# --- CLAUDE CODE ---
# Personal/local settings (DO NOT COMMIT)
.claude/settings.local.json
.claude/*.local.*
.claude/.env

# --- OPENCODE ---
# Local configuration files
.opencode/config.local.json
.opencode/.env
.opencode/plugins/local/

# ============================================
# STANDARD PROJECT IGNORES
# ============================================
node_modules/
dist/
build/
.env
.env.local
*.log
.DS_Store
.vscode/settings.json  # Personal VS Code settings
```

**What to Commit vs. Ignore:**

| File/Directory | Commit? | Location | Purpose |
|----------------|---------|----------|---------|
| `CLAUDE.md` | ✅ Yes | Project root | Team-shared project context |
| `.claude/settings.json` | ✅ Yes | Project root | Team permission rules |
| `.claude/settings.local.json` | ❌ No | Project root | Personal permission overrides |
| `.claude/commands/` | ✅ Yes | Project root | Shared slash commands |
| `.claude/skills/` | ✅ Yes | Project root | Reusable skills |
| `.claude/agents/` | ✅ Yes | Project root | Sub-agent definitions |
| `.claude/hooks/` | ✅ Yes | Project root | Automation hooks |
| `.claude/mcp.json` | ✅ Yes* | Project root | MCP server configs (use env vars for secrets) |
| `~/.claude/CLAUDE.md` | ❌ No | Home directory | Personal global preferences (automatically outside git) |
| `AGENT.md` | ✅ Yes | Project root | Alternative to CLAUDE.md for team rules |

*Use environment variables like `${GITHUB_TOKEN}` instead of hardcoding secrets. [^14^][^21^]

---

### 1.3 As a solo developer, should I use branches and PRs or just commit directly?

**Answer:** Use a **hybrid approach** - lightweight but structured:

**Recommended Solo Workflow:**

```bash
# Option A: Direct commits for small, safe changes
git add .
git commit -m "feat: add user authentication"
git push origin main

# Option B: Feature branches for significant changes
# (Even solo, this lets you review your own work via PR)
git checkout -b feature/payment-integration
# ... do work ...
git add . && git commit -m "feat: integrate Stripe payments"
git push origin feature/payment-integration
# Create PR on GitHub, review yourself, merge
```

**Why branches matter even solo:**
- **Checkpoints:** Easy to abandon a bad approach (`git checkout main`)
- **Self-review:** PR interface helps you review your own diff
- **CI/CD:** Can set up GitHub Actions to run tests before merge
- **Context for AI:** Claude Code can read PR descriptions for additional context

**Claude Code Integration:**
- Use `gh` CLI for PR management: `gh pr create`, `gh pr merge`
- Claude can generate PR descriptions from commit history
- Use `/project:review` command (custom skill) to review your own PRs [^1^][^14^]

---

## 2. PREPARATORY WORK & CONTEXT FILES

### 2.1 Should I create context files before starting OpenCode/Claude Code?

**Answer:** **YES - absolutely essential.** Without context files, the AI operates blind and makes poor architectural decisions.

**Minimum Required Before First Session:**

| File | Priority | Purpose |
|------|----------|---------|
| `CLAUDE.md` | 🔴 **CRITICAL** | Core project context loaded every session |
| `README.md` | 🟡 **HIGH** | Project overview for humans and AI |
| `.claude/settings.json` | 🟡 **HIGH** | Permission and safety rules |

**Quick Start Command:**
```bash
# Let Claude Code generate the initial CLAUDE.md
claude /init
```

This scans your codebase and creates a starter CLAUDE.md. [^6^][^19^]

---

### 2.2 One file or multiple files?

**Answer:** **Multiple files using Progressive Disclosure.** Don't put everything in one bloated CLAUDE.md.

**Recommended Structure:**

```
project-root/
├── CLAUDE.md                    # Core rules (always loaded)
├── README.md                    # Project overview
├── docs/
│   ├── ARCHITECTURE.md          # System design (loaded on demand)
│   ├── API_CONVENTIONS.md       # API standards (loaded on demand)
│   ├── TESTING.md               # Testing strategies (loaded on demand)
│   └── DECISIONS.md             # ADRs - Architecture Decision Records
└── .claude/
    ├── commands/                # Custom slash commands
    ├── skills/                  # Specialized capabilities
    └── agents/                  # Sub-agent definitions
```

**Progressive Disclosure Pattern:**

```markdown
<!-- In root CLAUDE.md -->
# Core Rules (Always Loaded)
- Use TypeScript strict mode
- Prefer functional components over classes

## Domain-Specific Context
- When working with payments, read: @docs/payments/ARCHITECTURE.md
- When modifying APIs, read: @docs/API_CONVENTIONS.md
- When testing, read: @docs/TESTING.md
```

**Why this matters:** Claude Code has ~200K token context window, but quality degrades after 60% usage. Loading everything upfront wastes tokens on irrelevant context. [^3^][^6^]

---

### 2.3 What to include in CLAUDE.md? How long should it be?

**Answer:** Keep it **concise and actionable**. Maximum 200-300 lines. Every line should pass the test: *"Would removing this cause Claude to make mistakes?"*

**CLAUDE.md Template:**

```markdown
# [Project Name] - Claude Context

## Tech Stack
- **Framework:** Next.js 14 (App Router)
- **Language:** TypeScript 5.0 (strict mode)
- **Styling:** Tailwind CSS + shadcn/ui
- **Database:** PostgreSQL with Prisma ORM
- **Testing:** Vitest + React Testing Library
- **Package Manager:** pnpm

## Code Style Rules
- Use ES modules (import/export), never CommonJS
- Destructure imports: `import { foo } from 'bar'`
- File naming: PascalCase for components, camelCase for utils
- YOU MUST use type hints for all function signatures
- NEVER use `any` type - use `unknown` with type guards instead

## Workflow Commands
```bash
# Install dependencies
pnpm install

# Run dev server
pnpm dev

# Type check (MUST run before commits)
pnpm typecheck

# Run tests (single file for speed)
pnpm test -- --grep "test name"

# Lint (MUST pass before commits)
pnpm lint
```

## Project Conventions
- API routes: RESTful, kebab-case URLs, camelCase JSON
- Database: Migrations must be backward compatible
- Components: Co-locate tests as `[Component].test.tsx`
- Environment: Use `process.env.VAR_NAME` with validation

## Common Gotchas
- If build fails with memory error: `NODE_OPTIONS=--max-old-space-size=4096`
- Database URL must include `?schema=public` for Prisma
- Webhook handlers must return 200 quickly, process async

## Architecture References
- See @docs/ARCHITECTURE.md for system design
- See @docs/DATABASE.md for schema conventions
```

**Include:** Bash commands, code style rules, testing instructions, project-specific conventions, common gotchas
**Exclude:** Standard language conventions, detailed API docs (link instead), file-by-file descriptions, tutorials [^6^][^19^]

---

### 2.4 Should I decide the tech stack or let the AI suggest?

**Answer:** **You decide the stack, AI helps implement.** The AI is excellent at execution but lacks product vision.

**Decision Matrix:**

| Decision | Who Decides | Why |
|----------|-------------|-----|
| **Core stack** (React vs Vue, Python vs Node) | **You** | Based on your expertise, hiring, long-term maintenance |
| **Specific libraries** (which UI kit, ORM) | **Collaborative** | You set requirements, AI suggests options with trade-offs |
| **Architecture patterns** | **You** | AI implements your chosen pattern (microservices vs monolith) |
| **Code style details** | **AI** | Let AI follow conventions from CLAUDE.md |

**Best Practice:**
1. Write a `PRD.md` (Product Requirements Document) describing what you want to build
2. Include any stack preferences or constraints
3. Ask Claude: *"Review @PRD.md and suggest a tech stack based on these requirements"*
4. Review suggestions, make final call
5. Claude updates CLAUDE.md with the decided stack [^3^][^20^]

---

### 2.5 If multiple preliminary files, what are they and how to name them?

**Answer:** Use this standardized file structure:

**Core Context Files:**

| Filename | Location | Purpose | When to Use |
|----------|----------|---------|-------------|
| `CLAUDE.md` | Project root | Primary context file | Every session |
| `AGENT.md` | Project root | Alternative to CLAUDE.md | If you prefer the name |
| `CLAUDE.local.md` | Project root | Personal overrides | Deprecated, use `~/.claude/CLAUDE.md` instead |
| `README.md` | Project root | Human + AI project overview | Always |
| `PRD.md` | Project root or `docs/` | Product requirements | Before coding starts |
| `docs/ARCHITECTURE.md` | `docs/` folder | System design | When implementing features |
| `docs/API.md` | `docs/` folder | API specifications | When working on endpoints |
| `docs/DECISIONS.md` | `docs/` folder | Architecture Decision Records | When making big changes |

**Claude Code Specific:**

| Filename | Location | Purpose |
|----------|----------|---------|
| `.claude/settings.json` | `.claude/` | Permission rules, hooks |
| `.claude/commands/<name>.md` | `.claude/commands/` | Custom slash commands |
| `.claude/skills/<skill>/SKILL.md` | `.claude/skills/` | Specialized capabilities |
| `.claude/agents/<name>.md` | `.claude/agents/` | Sub-agent definitions |
| `.claude/hooks/<event>.json` | `.claude/hooks/` | Automation triggers |

**Naming Convention:**
- Use UPPERCASE for root context files: `CLAUDE.md`, `README.md`
- Use lowercase for directories: `.claude/`, `docs/`
- Use kebab-case for command/skill files: `code-review.md`, `fix-issue.md`
- Skills MUST be named `SKILL.md` inside their folder [^14^][^18^][^20^]

---

### 2.6 Should I create files in a separate directory?

**Answer:** **Yes, use `.claude/` directory for Claude Code configs.** Keep project docs in `docs/`.

**Recommended Directory Structure:**

```
my-project/
├── .claude/                    # Claude Code configuration
│   ├── settings.json            # Team permission settings (commit)
│   ├── settings.local.json      # Personal overrides (gitignore)
│   ├── commands/                # Custom slash commands
│   │   ├── review.md            # /project:review
│   │   └── fix-issue.md         # /project:fix-issue
│   ├── skills/                  # Specialized capabilities
│   │   ├── pdf/
│   │   │   ├── SKILL.md
│   │   │   └── extract.py
│   │   └── csv/
│   │       ├── SKILL.md
│   │       └── analyze.py
│   ├── agents/                  # Sub-agent definitions
│   │   ├── code-reviewer.md
│   │   └── security-auditor.md
│   └── hooks/                   # Event automation
│       ├── pre-edit.json
│       └── post-command.json
├── docs/                        # Project documentation
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── TESTING.md
├── src/                         # Source code
├── CLAUDE.md                    # Root context file
└── README.md
```

**Commit Strategy:**
- ✅ Commit: `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/`, `.claude/agents/`
- ❌ Gitignore: `.claude/settings.local.json`, any `*.local.*` files
- 📁 **Never** put `.claude/` in separate repo - it belongs with the project [^14^][^21^]

---

## 3. BEST PRACTICES & PROJECT STRUCTURE

### 3.1 What other files do I need for vibe/context coding?

**Answer:** Beyond CLAUDE.md, you need these for a complete setup:

**Essential Files:**

| File | Purpose | Priority |
|------|---------|----------|
| `CLAUDE.md` | Core project context | 🔴 Critical |
| `.claude/settings.json` | Permission & hook configuration | 🔴 Critical |
| `.claude/commands/` | Frequently used operations | 🟡 High |
| `docs/ARCHITECTURE.md` | System design decisions | 🟡 High |
| `.claude/skills/` | Specialized operations (PDF, Excel, etc.) | 🟢 Medium |
| `.claude/agents/` | Parallel task execution | 🟢 Medium |
| `.cursorrules` | If using Cursor alongside | 🟢 Medium |
| `.vscode/settings.json` | VS Code workspace settings | 🟢 Medium |

**OpenCode Specific:**

| File | Purpose | Location |
|------|---------|----------|
| `.opencode/config.json` | OpenCode configuration | Project root |
| `.opencode/plugins/` | Custom plugins | Project root or `~/.config/opencode/plugins/` |

**Example `.claude/settings.json`:**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "allow": [
    "Bash(npm run *)",
    "Bash(make *)",
    "Bash(git *)",
    "Read",
    "Write",
    "Edit",
    "Glob",
    "Grep"
  ],
  "deny": [
    "Bash(rm -rf *)",
    "Bash(curl *)",
    "Bash(wget *)",
    "Read(.env)",
    "Read(secrets/*)"
  ],
  "hooks": {
    "Stop": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/afplay /System/Library/Sounds/Glass.aiff"
          }
        ]
      }
    ]
  }
}
```

**Example `.opencode/config.json`:**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "compaction": {
    "auto": true,
    "prune": true,
    "reserved": 10000
  },
  "watcher": {
    "ignore": ["node_modules/**", "dist/**", ".git/**"]
  },
  "mcp": {}
}
```

[^4^][^14^]

---

### 3.2 Should I create skills, agents, MCP, and tools in advance or let AI create them?

**Answer:** **Create the infrastructure upfront, let AI fill the details.**

**Recommended Approach:**

| Component | Create Before? | How |
|-----------|---------------|-----|
| **Skills** | ✅ Yes - skeletons | Create `.claude/skills/<name>/SKILL.md` with frontmatter, let Claude fill the implementation |
| **Agents** | ✅ Yes - definitions | Create `.claude/agents/<name>.md` with role definitions when you identify recurring tasks |
| **Commands** | 🟡 As needed | Create when you find yourself repeating the same prompt |
| **MCP Servers** | 🟡 As needed | Add when you need external integrations (GitHub, databases, etc.) |
| **Hooks** | 🟡 As needed | Add when you need automation (format on save, etc.) |

**Example: Creating a Skill Skeleton**

```markdown
<!-- .claude/skills/pdf-processing/SKILL.md -->
---
name: pdf-processing
description: Extract and analyze text from PDF documents. Use when users ask to process PDFs.
allowed-tools: Read, Bash(python:*)
---

# PDF Processing

Extract text from PDFs using Python.

## Requirements
- pypdf
- pdfplumber

## Basic Usage
```python
import pdfplumber
with pdfplumber.open("doc.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

For advanced operations, see [REFERENCE.md](REFERENCE.md).
```

Then ask Claude: *"Complete the pdf-processing skill with proper error handling and all necessary scripts."* [^14^][^18^][^24^]

---

### 3.3 Where to store skills, agents, MCP - project directory or global config?

**Answer:** **Both - use scope-appropriate locations:**

| Scope | Location | Use Case |
|-------|----------|----------|
| **Project-only** | `.claude/skills/`, `.claude/agents/` | Team-shared, project-specific capabilities |
| **Personal global** | `~/.claude/skills/`, `~/.claude/agents/` | Your personal shortcuts across all projects |
| **Enterprise** | Managed settings | Organization-wide standards |

**Resolution Priority:** Enterprise > Personal > Project > Plugin

**Example:**

```
# Project-specific (committed to git)
my-project/.claude/skills/deployment/SKILL.md

# Personal (available everywhere)
~/.claude/skills/pr-description/SKILL.md
~/.claude/commands/daily-standup.md

# Usage difference:
# - Project skill: automatically suggested when relevant
# - Personal command: accessed via /user:daily-standup
```

**MCP Servers:**
- **Project scope:** `claude mcp add <name> --scope project` → writes to `.claude/mcp.json`
- **User scope:** `claude mcp add <name>` → writes to `~/.claude.json`

**Recommendation:** Start with project scope for team consistency, move to user scope only for personal tools like Brave Search. [^14^][^16^][^18^]

---

### 3.4 Is there a standard file for logging changes and tasks?

**Answer:** **Yes - use `CLAUDE_LOG.md` or `TASK_LOG.md` in project root.**

**Standard Logging File:**

```markdown
# Claude Session Log

## 2025-03-26 - Session: auth-implementation

### Completed
- [x] Set up NextAuth.js with credentials provider
- [x] Created login/logout API routes
- [x] Added middleware for route protection

### Decisions Made
- Using JWT strategy with 30-day expiry
- Storing sessions in Redis for scalability
- Password hashing with bcrypt (10 rounds)

### Open Issues
- [ ] Need to implement password reset flow
- [ ] Email verification pending (SendGrid integration)

### Files Modified
- `src/app/api/auth/[...nextauth]/route.ts`
- `src/middleware.ts`
- `src/lib/auth.ts`

### Next Steps
1. Create password reset token generation
2. Set up SendGrid for transactional emails
3. Add OAuth providers (Google, GitHub)
```

**Alternative: Use the Document & Clear Pattern**

When context gets heavy (60%+ used):

1. **Dump context to file:**
   ```bash
   # Ask Claude: "Save our current progress to progress.md and summarize what's done"
   ```

2. **Clear session:**
   ```
   /clear
   ```

3. **Resume with context:**
   ```bash
   # Ask Claude: "Read @progress.md and continue with [next task]"
   ```

**Pro Tip:** Create a custom `/transfer-context` skill that automates this handoff process. [^3^][^7^]

---

### 3.5 What else am I missing that's important?

**Answer:** Critical elements often overlooked:

**1. Context Management Strategy**
- **Problem:** Claude Code's 200K context fills up fast; quality degrades after 60%
- **Solution:** 
  - Use `/clear` between unrelated tasks
  - Use `/compact focus on [specific topic]` when heavy
  - Use subagents for deep investigation: *"Use subagent to explore how auth works"*

**2. Permission Configuration**
- Don't run with `--dangerously-skip-permissions` in production
- Set up proper allow/deny lists in `.claude/settings.json`
- Use auto-mode for trusted workflows after initial validation

**3. MCP Server Security**
- Always use `-e ENV_VAR` for tokens, never hardcode in `.mcp.json`
- Use `--scope project` for repo-specific integrations
- Limit to 5-8 MCP servers max (each consumes context tokens)

**4. Sub-agents for Parallel Work**
- Enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
- Use for: code review, refactoring, documentation updates
- Never have two agents edit the same file simultaneously

**5. Voice Dictation**
- Run `/voice` for push-to-talk (Space key)
- Speaks 3-4x faster than typing
- Mix voice and text in same message

**6. Checkpointing**
- Double-tap `Esc` or `/rewind` to restore previous states
- Checkpoints persist across sessions
- Use instead of manual git commits for experimental changes

**7. Local Model Setup (Claude Code)**
```bash
# Run Claude Code with local models via Ollama
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL="http://localhost:11434"
claude --model devstral-small-2
```

**8. OpenCode Specifics**
- OpenCode uses `.opencode/` directory (similar to `.claude/`)
- Supports plugins via `.opencode/plugins/` or npm packages
- Configuration in `.opencode/config.json` with schema validation

[^1^][^3^][^5^][^6^][^10^][^16^]

---

## 4. RESOURCES & OFFICIAL DOCUMENTATION

### 4.1 Official Resources

| Resource | URL | Description |
|----------|-----|-------------|
| **Claude Code Official Docs** | https://docs.anthropic.com/en/docs/claude-code/overview | Authoritative source from Anthropic |
| **Claude Code Best Practices** | https://code.claude.com/docs/en/best-practices | Official best practices guide |
| **Claude Code Skills Docs** | https://code.claude.com/docs/en/skills | Skills development guide |
| **MCP Specification** | https://modelcontextprotocol.io | Model Context Protocol standard |
| **Awesome MCP Servers** | https://github.com/punkpeye/awesome-mcp-servers | Community-curated MCP servers |
| **OpenCode Docs** | https://opencode.ai/docs/ | OpenCode VS Code extension docs |
| **OpenCode Config Schema** | https://opencode.ai/config.json | JSON schema for validation |

### 4.2 Community Resources & News

| Resource | URL | Description |
|----------|-----|-------------|
| **Claude Code Subreddit** | https://www.reddit.com/r/ClaudeAI/ | Community discussions |
| **Anthropic Discord** | https://www.anthropic.com/discord | Official Discord server |
| **MCP Community Servers** | https://github.com/modelcontextprotocol/servers | Official MCP server examples |
| **Claude Code Tips** | https://www.builder.io/blog/claude-code-tips-best-practices | 50 tips for daily use |
| **Vibe Coding Guide** | https://github.com/anthropics/claude-code/wiki | Community wiki |

### 4.3 Tools & Extensions

| Tool | URL | Purpose |
|------|-----|---------|
| **Ollama** | https://ollama.com | Local LLM hosting for Claude Code |
| **LM Studio** | https://lmstudio.ai | GUI for local models |
| **LiteLLM** | https://github.com/BerriAI/litellm | Proxy for multiple LLM providers |
| **anyclaude** | https://github.com/coder/anyclaude | Multi-provider wrapper |

### 4.4 News & Updates Monitoring

**To stay current:**

1. **Official Channels:**
   - Follow [@AnthropicAI](https://twitter.com/AnthropicAI) on Twitter/X
   - Subscribe to Anthropic's newsletter at https://www.anthropic.com/news
   - Join the [Anthropic Discord](https://www.anthropic.com/discord)

2. **Release Notes:**
   - Claude Code: Check `claude --version` and update with `npm install -g @anthropic-ai/claude-code`
   - OpenCode: Updates via VS Code marketplace (check Extensions panel)

3. **Community:**
   - r/ClaudeAI for user tips
   - Hacker News "claude code" searches
   - YouTube: Search "Claude Code 2025" for recent tutorials

---

## QUICK REFERENCE: FILE STRUCTURE TEMPLATE

```
my-project/
├── .claude/
│   ├── settings.json              # Team permissions (COMMIT)
│   ├── settings.local.json        # Personal overrides (GITIGNORE)
│   ├── commands/
│   │   ├── review.md              # /project:review
│   │   └── deploy.md              # /project:deploy
│   ├── skills/
│   │   ├── database/
│   │   │   └── SKILL.md
│   │   └── testing/
│   │       └── SKILL.md
│   ├── agents/
│   │   ├── code-reviewer.md
│   │   └── security-auditor.md
│   └── hooks/
│       └── post-edit.json
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── DECISIONS.md
├── src/
├── CLAUDE.md                      # Main context (COMMIT)
├── README.md
├── .gitignore                     # Include .claude/*.local.*
└── CLAUDE_LOG.md                  # Session log (OPTIONAL)
```

---

## SUMMARY CHECKLIST

**Before First Session:**
- [ ] Create GitHub repo and clone locally
- [ ] Create `CLAUDE.md` with tech stack and rules (or run `/init`)
- [ ] Create `.claude/settings.json` with permissions
- [ ] Set up `.gitignore` for local config files
- [ ] Create `docs/ARCHITECTURE.md` if complex project

**During Development:**
- [ ] Use `/clear` between unrelated tasks
- [ ] Create skills when you notice repeated complex tasks
- [ ] Use subagents for investigation (keeps main context clean)
- [ ] Log important decisions to `CLAUDE_LOG.md`
- [ ] Run `/compact` when context exceeds 60%

**Team/Project Maintenance:**
- [ ] Commit shared `.claude/` configs (not local ones)
- [ ] Review and prune CLAUDE.md monthly (remove outdated rules)
- [ ] Update skills as project evolves
- [ ] Document architectural decisions in `docs/DECISIONS.md`

---

*Document Version: 2025-03-26 | For OpenCode (VS Code) & Claude Code (Local/Cloud)*
