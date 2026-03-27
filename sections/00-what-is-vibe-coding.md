# What is Vibe Coding?

This chapter gives you the mental model you need before touching any tools. Vibe coding is simple once you understand how to think about it.

---

## The one-sentence definition

Vibe coding = you act as the architect, the AI acts as a very fast junior developer.

That's it. You describe what you want. The AI writes the code. You review, correct, and own the result.

---

## What the AI actually does

The agent can:

- Read and understand your project files
- Write and edit code in any language
- Run shell commands (install deps, run tests, start servers)
- Search the web for documentation
- Create git commits and branches
- Run your test suite and report results

The agent cannot:

- Read your mind — you must describe what you want
- Know things you haven't told it — context is your job
- Detect bugs without running code — always verify
- Make architectural decisions well — it doesn't know your constraints

---

## The human-agent loop

```text
┌─────────────────────────────────────────────────────────┐
│  YOU (architect)                                        │
│  - Define the goal                                      │
│  - Provide context (AGENTS.md, docs/)                   │
│  - Review output                                        │
│  - Make decisions                                       │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│  AI AGENT (implementer)                                │
│  - Reads your context                                  │
│  - Writes code                                         │
│  - Runs commands                                       │
│  - Reports results                                     │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
                         (you review, then repeat)
```

The loop runs continuously. You're always in the driver's seat.

---

## Common beginner misconceptions

### "The AI will figure it out"

No. The AI makes assumptions based on its training data. If you don't tell it what you want, it guesses — and often guesses wrong.

**Fix:** Write down constraints in `AGENTS.md`. Be explicit about what you don't want.

### "I can just let it run and come back to working code"

Sometimes this works for trivial tasks. For anything real, you'll need to check in frequently. Plan-first, then execute in small steps.

### "I don't need to understand the code it writes"

Wrong. You own the result. If something breaks in production, you fix it — not the AI. Read every file the agent creates. Understand what it does.

### "More context is always better"

Overstuffing `AGENTS.md` hurts. The model deprioritizes long context. Keep `AGENTS.md` under 200 lines, use progressive disclosure.

---

## How to read this playbook

This guide is ordered to build your skills progressively:

1. **[Section 1 — GitHub](01-git-github.md)** — Set up GitHub (do this first, always)
2. **[Section 2 — Context Files](02-context-files.md)** — Create context files (critical skill)
3. **[Section 3 — Best Practices](03-best-practices.md)** — Best practices (start doing these from day one)
4. **[Section 4 — Workflow](04-workflow.md)** — The actual workflow (your session loop)
5. **[Section 5 — OpenCode vs Claude Code](05-opencode-vs-claude-code.md)** — Tool comparison (pick your tool)
6. **[Section 6 — Resources](06-resources.md)** — Resources (bookmark these)
7. **[Section 7 — Prompt Engineering](07-prompt-engineering.md)** — Prompt engineering (how to talk to agents)
8. **[Section 8 — Debugging](08-debugging-with-agents.md)** — Debugging (what to do when things break)
9. **[Section 9 — Project Types](09-project-types.md)** — Project types (how to start different projects)
10. **[Section 10 — Cost and Models](10-cost-and-models.md)** — Cost management (avoid overspending)

Read in order. Each section builds on the previous.

---

## Your first vibe coding session

The full walkthrough — including the exact commands — is in the [README quick start](../README.md#quick-start-your-first-session-).

In short: create the repo, add context files, start a branch, run the agent, review the output, commit. That's it. The rest of this playbook makes you faster, safer, and more effective.

---

← _Start here_ | [Next: Git & GitHub →](01-git-github.md)
