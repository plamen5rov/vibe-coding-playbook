# Context Files: Briefing the AI Before You Start

![Header](../pictures/02-context-files.png)

The single highest-leverage thing you can do in vibe coding is create context files before the first session. An agent that knows your project's goals, tech stack, and constraints makes far fewer wrong assumptions.

Both OpenCode and Claude Code auto-load these files at session start. Without them, you're starting from zero every time.

---

## The minimum set

For any new project, create these before running `opencode` or `claude` for the first time:

| File | Purpose | Length |
| --- | --- | --- |
| `AGENTS.md` | Main context — read every session | Under 200 lines |
| `README.md` | Human-readable project overview | As needed |
| `docs/PROJECT.md` | Goals, audience, constraints | 1 page |
| `docs/TASKS.md` | Current work items | Living doc |
| `.gitignore` | What to exclude from git | Standard |

Claude Code also reads `CLAUDE.md` if no `AGENTS.md` is found. Both names work. `AGENTS.md` is the cross-tool standard that works with OpenCode, Claude Code, Cursor, and others.

---

## What goes in `AGENTS.md`

Keep it **under 200 lines**. Longer files start being skimmed, not read — and both tools inject this file as a system reminder that the model may deprioritize if it grows too large.

Every line should pass this test: *"Would removing this line cause the agent to make mistakes?"*

**The WHY / WHAT / HOW pattern:**

```markdown
# Project Name
One-line description. One-line tech stack.

## Why This Exists
What problem does this solve? Who is it for?

## Architecture
Key directories and their purpose:
- `src/api/` — REST handlers
- `src/models/` — data models
- `src/services/` — business logic

## Tech Stack
- Runtime: Node 22
- Framework: Next.js 14 (App Router)
- DB: PostgreSQL via Prisma
- Tests: Vitest

## Commands
```bash
pnpm dev       # start dev server
pnpm test      # run tests
pnpm lint      # eslint
```

## Coding Conventions

- TypeScript strict mode — no `any`
- Functional components only (React)
- Conventional commit messages

## Rules for This Agent

- Read docs/TASKS.md before starting
- Never modify the DB schema without a migration
- Ask before adding new dependencies
- Never commit .env or secrets

```text

**What to exclude from `AGENTS.md`:**
- Exhaustive documentation of every file
- Instructions that only apply to one rare task
- Coding style rules already enforced by a linter
- API documentation (link to a doc file instead)

---

## Use progressive disclosure for complex projects

Don't cram everything into `AGENTS.md`. Reference additional files when they're needed:

```markdown
## References
- When working on payments: read @docs/payments.md
- When modifying the API: read @docs/api-conventions.md
- When writing tests: read @docs/testing.md
```

This way, `AGENTS.md` stays short and the agent loads detailed context only when the task requires it. Claude Code's context window is 200K tokens, but quality degrades after 60% usage — loading irrelevant context wastes capacity.

---

## Multiple files vs one file

**Use multiple files.** Start with one, split as the project grows.

```text
project-root/
├── AGENTS.md              ← main context (always loaded)
├── docs/
│   ├── PROJECT.md         ← goals and constraints
│   ├── TASKS.md           ← current work items
│   ├── ARCHITECTURE.md    ← system design (loaded on demand)
│   └── API.md             ← API conventions (loaded on demand)
└── .opencode/
    └── commands/
        └── review.md      ← custom /review slash command
```

The key principle: `AGENTS.md` stays short and points outward. Detailed docs are loaded when relevant.

---

## Decide the tech stack yourself

Let the agent help implement, not choose. The agent will suggest whatever is most popular in its training data — it has no knowledge of your constraints, preferences, or existing expertise.

**Recommended approach:**

1. Write constraints in `docs/PROJECT.md`: "Python backend, single VPS, no Kubernetes."
2. Ask the agent: "Given these constraints, suggest a tech stack and explain the tradeoffs."
3. Discuss, decide, then document the final choice in `AGENTS.md`.

Once the stack is in `AGENTS.md`, the agent will use it consistently without you repeating it.

---

## The `/init` shortcut

Both tools can generate a starter `AGENTS.md` from your codebase:

```bash
# Claude Code
claude
/init

# OpenCode
# Ask: "Scan this project and generate an AGENTS.md for me"
```

The auto-generated file is a starting point — review and refine it before relying on it. Add your constraints, rules, and gotchas.

---

## Naming and location

| File | Location | Notes |
| --- | --- | --- |
| `AGENTS.md` | Project root | Universal cross-tool standard |
| `CLAUDE.md` | Project root | Claude Code native name — same content |
| `CLAUDE.local.md` | Project root | Personal overrides — never commit |
| `docs/*.md` | `docs/` folder | Referenced from AGENTS.md |
| `.opencode/commands/*.md` | `.opencode/commands/` | Slash commands |
| `.claude/commands/*.md` | `.claude/commands/` | Same for Claude Code |

**Always commit** `AGENTS.md`, `CLAUDE.md`, and all `docs/` files — they are your project's intelligence and should travel with the repo.
