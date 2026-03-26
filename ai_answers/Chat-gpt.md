# Vibe / Context Coding FAQ — Practical Guide (2026)

This guide answers your FAQ with modern best practices for AI-assisted development using tools like OpenCode, Claude Code, and similar agentic coding environments.

---

# 1. Git / GitHub

## Should I create a GitHub repo first?

**Best practice (2026):**

- Create the repo FIRST on GitHub → then clone locally.

**Why:**

- Ensures proper remote setup
- Easier CI/CD later
- Avoids auth/config issues

**Alternative (acceptable):**

- Initialize locally → push → create repo via CLI (`gh repo create`)

**Avoid:** letting tools auto-create repos blindly — they often:

- misconfigure `.gitignore`
- skip branch protection

---

## Should OpenCode / Claude config files go in `.gitignore`?

**Rule of thumb:**

| File Type | Commit? |
|----------|--------|
| Project-specific AI instructions | ✅ YES |
| Secrets / API keys | ❌ NO |
| Local cache / embeddings | ❌ NO |
| Tool config reusable by team | ✅ YES |

### Example `.gitignore`

```
# AI tools
.opencode/cache/
.claude/cache/
*.embeddings
.env

# OS
.DS_Store
```

---

## Solo dev: branches or not?

**Modern recommendation:** YES — but lightweight.

Use:

- `main` → always stable
- `dev` → active work
- feature branches → optional

**Simple workflow:**

```
main
 └── dev
      ├── feature/auth
      ├── feature/ui
```

**Why even solo:**

- safer experimentation
- easier rollback
- cleaner AI-assisted diffs

**Shortcut (acceptable):**

- commit directly to `main` for very small projects

---

# 2. Preparatory Work

## Should I create project context files BEFORE coding?

**YES — this is critical in context coding.**

AI performs MUCH better with structured context.

---

## One file or multiple?

**Best practice: multiple small files (modular context).**

---

## What files to create

### 1. `PROJECT.md`

Core description

Include:

- purpose
- target users
- main features
- constraints

---

### 2. `ARCHITECTURE.md`

System design

Include:

- tech stack
- folder structure
- data flow

---

### 3. `TASKS.md`

Living roadmap

Include:

- TODOs
- current tasks
- completed tasks

---

### 4. `CONVENTIONS.md`

Coding rules

Include:

- naming conventions
- formatting
- API patterns

---

### 5. `STACK.md`

Explicit tech decisions

---

## How long should they be?

- 200–800 lines total across files
- concise but structured

**Avoid:**

- giant unstructured documents

---

## Should you pick the tech stack or let AI decide?

**Best approach: hybrid**

- YOU define constraints:
  - language
  - environment
  - goals

- AI suggests:
  - frameworks
  - libraries

**Example:**

```
Constraint: "Frontend must be pure HTML/CSS/JS"
AI decides: "Use Vite + vanilla JS modules"
```

---

## Naming and structure

```
project-root/
├── docs/
│   ├── PROJECT.md
│   ├── ARCHITECTURE.md
│   ├── STACK.md
│   ├── CONVENTIONS.md
│   └── TASKS.md
```

---

## Should these be committed?

✅ YES — ALWAYS

They are part of the project intelligence.

---

# 3. Best Practices

## Additional important files

### `README.md`

Public-facing overview

### `CHANGELOG.md`

Track changes

Use format:

```
## [1.0.0] - 2026-03-26
### Added
- Authentication
```

---

### `.env.example`

Template for environment variables

---

### `AI.md` (optional but powerful)

Instructions specifically for AI agents:

```
- Never refactor entire project without request
- Prefer small changes
- Follow CONVENTIONS.md
```

---

## Skills, Agents, MCP, Tools

### Should you create them in advance?

**Recommendation:**

- Start minimal
- Let AI create → then refactor

---

### Where to store them?

**Two-layer strategy:**

#### 1. Global (reusable)

```
~/.opencode/
~/.claude/
```

#### 2. Project-specific

```
project-root/.ai/
```

---

## Logging changes

Use BOTH:

### 1. Git commits (primary truth)

### 2. `CHANGELOG.md`

### 3. Optional: `DEVLOG.md`

---

## Critical things most people miss

### 1. Context decay

AI forgets over time → refresh context manually

### 2. Over-generation

AI tends to:

- over-engineer
- create unnecessary abstractions

**Fix:** enforce constraints in `CONVENTIONS.md`

---

### 3. Deterministic prompts

Bad:

```
"Improve this"
```

Good:

```
"Refactor only this function, do not change API"
```

---

### 4. Small iterations

Never ask AI to:

- build entire app in one prompt

Instead:

- feature by feature

---

# 4. OpenCode vs Claude Code Notes

## OpenCode (VS Code ecosystem)

Best for:

- tight editor integration
- fast iteration

Tips:

- use workspace context
- pin important files

---

## Claude Code

Best for:

- long reasoning
- architecture decisions

Tips:

- give structured docs
- rely on multi-file context

---

# 5. Resources (2026 Updated)

## Official / Core

- <https://docs.anthropic.com/claude/docs>
- <https://platform.openai.com/docs>
- <https://github.com/features/copilot>

---

## AI Coding / Agentic Dev

- <https://github.com/microsoft/autogen>
- <https://github.com/langchain-ai/langchain>
- <https://github.com/crewAIInc/crewAI>

---

## Prompt Engineering

- <https://www.promptingguide.ai>

---

## Communities / News

- <https://news.ycombinator.com>
- <https://www.reddit.com/r/LocalLLaMA>
- <https://www.reddit.com/r/MachineLearning>

---

## YouTube (high signal)

- <https://www.youtube.com/@Fireship>
- <https://www.youtube.com/@TwoMinutePapers>

---

# Final Advice

If you remember only 5 things:

1. Always create structured context files
2. Keep AI instructions explicit and constrained
3. Work in small iterations
4. Use Git properly even solo
5. Treat AI like a junior dev, not an oracle

---

**End of Guide**
