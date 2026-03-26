# Best Practices

## The 5 things experienced vibe coders do differently

### 1. Plan before coding

Before the agent writes a single line, ask it to write a plan.

```text
"Before touching code, write a plan to docs/SPEC.md and wait for my approval."
```

This is the single most effective way to avoid long debugging sessions caused by the agent misunderstanding your intent. Claude Code has a built-in Plan mode (Shift+Tab twice) that physically prevents the agent from editing files until you approve. OpenCode has a `plan` agent that is read-only by default.

Once you approve the plan, the agent executes it. If it goes wrong, you have a written spec to refer back to.

### 2. Work in small iterations

Never ask the agent to build an entire feature in one prompt.

```text
❌ Bad:  "Build the entire authentication system."
✅ Good: "Add a login form that calls POST /api/auth/login and handles errors."
```

Check in every few steps. Course-correct early — redirecting is much faster than debugging a large block of wrong code.

### 3. Use git as your undo button

Commit before any significant agent action. If the output is bad, `git checkout .` resets everything instantly.

```bash
git add . && git commit -m "checkpoint before agent refactor"
# let the agent work
# review the result
# if bad: git checkout .
# if good: git add . && git commit -m "feat: ..."
```

### 4. Clear context between tasks

Both tools accumulate context from previous work. When switching to a new unrelated task, clear the session.

- **Claude Code:** `/clear`
- **OpenCode:** start a new session

Accumulated irrelevant context wastes token budget and can cause the agent to conflate different tasks.

### 5. Treat the agent as a fast junior developer

You are the architect. The agent is a very fast implementer. Guide it with clear specs, review its output, and own the result. Accepting AI output without review leads to security issues and accumulated technical debt.

---

## Slash commands — your highest-leverage investment

Custom slash commands are markdown files that trigger a pre-written prompt. Create them once, reuse forever.

```text
.opencode/commands/review.md     → /review
.opencode/commands/ship.md       → /ship
.opencode/commands/push.md       → /push
```

A `/ship` command that runs lint, tests, writes a commit message, and pushes — created once — saves enormous repeated prompting.

**Example: a `/review` command**

```markdown
---
description: Review the current diff for issues
---

Review all changes since the last commit.
Check for: logic errors, security issues, missing error handling,
hardcoded values that should be env vars, and missing tests.
Be concise. List issues as checkboxes.
```

Both OpenCode and Claude Code support this format. See `docs/CONVENTIONS.md` for OpenCode-specific frontmatter options.

---

## Agents and skills

### OpenCode agents

OpenCode ships with two built-in agents:

| Agent | Tools | Use for |
| --- | --- | --- |
| `build` (default) | All tools | Normal coding sessions |
| `plan` | Read-only | Planning and exploration |

Create custom agents in `.opencode/agents/` for specialized roles — a `reviewer` agent with read-only permissions, or a `documenter` agent focused only on docs.

### Claude Code subagents

Claude Code can spawn subagents for parallel work. Use them for investigation tasks that would otherwise fill the main context window.

```text
"Use a subagent to explore how the payment system works, then report back."
```

### When to create agents and skills

- **In advance:** for anything you'll use repeatedly — a `reviewer`, a `planner`, slash commands for your core workflows.
- **On the fly:** for one-off tasks. Let the agent create and run ad-hoc scripts.
- **As patterns emerge:** when you find yourself giving the same 10-line explanation every session, that's a candidate for a skill or custom agent.

---

## MCP servers

MCP (Model Context Protocol) connects the agent to external tools — GitHub, databases, web search, Notion, etc.

### Where to configure

| Scope | Location | Use for |
| --- | --- | --- |
| Project | `.claude/mcp.json` or `opencode.json` | Team-shared integrations |
| Global | `~/.claude.json` or `~/.config/opencode/` | Personal tools across all projects |

**Add via CLI:**

```bash
# Claude Code
claude mcp add github

# OpenCode
# Configure in opencode.json under "mcp" key
```

### Guidelines

- Install only what the project actually needs. Each MCP server consumes context tokens.
- Keep to 5–8 MCP servers maximum per session.
- Never hardcode API keys in MCP config files — use environment variables.
- Add GitHub MCP early if your project involves issues, PRs, or repo management.

---

## Logging changes — CHANGELOG.md

`CHANGELOG.md` is the standard. Use the [Keep a Changelog](https://keepachangelog.com) format and instruct the agent to maintain it.

Add to `AGENTS.md`:

```markdown
## Rules for This Agent
- After completing any feature, update CHANGELOG.md following
  Keep a Changelog format (https://keepachangelog.com).
```

**Format:**

```markdown
## [Unreleased]

## [1.1.0] - 2026-03-26
### Added
- User authentication with JWT
- Password reset flow

### Fixed
- Race condition in session refresh
```

The agent's session history + git commit messages + `CHANGELOG.md` gives you a complete audit trail.

---

## Security hygiene

- Never put API keys, passwords, or tokens in files the agent can read.
- Use `.env` files (gitignored) and reference via environment variables only.
- In Claude Code, use `deny` rules in `.claude/settings.json` to block the agent from reading `.env`:

```json
{
  "deny": [
    "Read(.env)",
    "Read(secrets/*)"
  ]
}
```

- In OpenCode, the `opencode-ignore` plugin can explicitly block file reads.
- Add `.env.example` (committed) to show what variables are needed without exposing values.
