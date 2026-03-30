# Vibe Coding Playbook

![Header](pictures/README.png)

A practical guide to building software with AI coding agents — specifically OpenCode and Claude Code.

No theory. No fluff. Just workflows, templates, and checklists you can use today.

---

## How this playbook was made

This guide started as an experiment. The author had real, practical questions about vibe coding — the kind a solo developer faces before starting their first AI-assisted project.

Those questions became [`FAQ.md`](FAQ.md). They were then submitted, unchanged, to the **top 10 AI LLMs**: ChatGPT, Claude, DeepSeek, Gemini, Grok, Kimi, Mistral, Perplexity, Qwen, and another Mistral model (to ensure diversity). Every raw answer is preserved in [`ai_answers/`](ai_answers/).

The answers were then read side by side, consensus patterns extracted, and contradictions resolved. This playbook is that synthesis — not one person's opinion, not one model's advice, but the distilled agreement across 10 different AI systems.

When a section says "all 10 AI models surveyed agree", that is literally what happened.

---

## Quick start (your first session) 🚀

```bash
# 1. Create a GitHub repo
gh repo create my-first-project --private
git clone https://github.com/yourname/my-first-project.git
cd my-first-project

# 2. Create context files (section 2)
# Create AGENTS.md, docs/PROJECT.md, docs/TASKS.md, .gitignore
# Or copy from starter-template/

# 3. Start a branch
git checkout -b feature/hello-world

# 4. Run the agent
opencode  # or: claude

# 5. Tell it what to build
# "Create a simple Python script that prints 'Hello, world!'"

# 6. Review the output, then commit
git add . && git commit -m "feat: hello world script"
```

That's it. Read section 0 first, then proceed through the guide in order.

---

## Guide 📖

### [0. What is Vibe Coding?](sections/00-what-is-vibe-coding.md) 🔰

The mental model — what the AI can and can't do, the human-agent loop, common misconceptions.

### [1. Git & GitHub](sections/01-git-github.md) 📦

How to set up your repo, what to commit vs ignore, and why feature branches matter even when working solo.

### [2. Context Files](sections/02-context-files.md) 📄

The files to create before your first session — `AGENTS.md`, `PROJECT.md`, `TASKS.md` — what goes in them and how long they should be.

### [3. Best Practices](sections/03-best-practices.md) ⚡

Slash commands, agents, MCP servers, `CHANGELOG.md`, security hygiene, and the habits that separate effective vibe coders from frustrated ones.

### [4. Workflow](sections/04-workflow.md) 🔄

The per-session loop: plan first, work in small steps, commit frequently, clear context between tasks. Includes a quick-reference checklist.

### [5. OpenCode vs Claude Code](sections/05-opencode-vs-claude-code.md) ⚔️

Side-by-side feature comparison, tool-specific tips, and how to run both on the same project.

### [6. Resources](sections/06-resources.md) 🔗

Curated official docs, high-quality guides, and how to stay current as the tooling evolves quickly.

### [7. Prompt Engineering](sections/07-prompt-engineering.md) 💬

How to write effective prompts — the anatomy of good requests, plan-then-execute patterns, templates for common tasks.

### [8. Debugging with Agents](sections/08-debugging-with-agents.md) 🐛

What to do when things break — the explain-before-fix pattern, common failure modes, when to restart vs course-correct.

### [9. Project Types](sections/09-project-types.md) 🏗️

How to start different projects — web app, API, CLI tool, script, library. Starter checklists for each type.

### [10. Cost and Models](sections/10-cost-and-models.md) 💰

Managing API costs, choosing the right model for the task, local vs cloud trade-offs, cost-saving strategies.

### [11. Managing Sessions](sections/11-session-management.md) 🔁

Resume, fork, and revert sessions — when to continue, when to branch, and how to recover from a bad run.

---

## Starter Template 📂

The [`starter-template/`](starter-template/) directory is a generic project scaffold you can copy into any new vibe-coding project.

```text
starter-template/
├── AGENTS.md        ← main AI context file (fill in your project details)
├── CHANGELOG.md     ← change log stub (Keep a Changelog format)
├── .gitignore       ← sensible defaults for AI tools + common stacks
├── README.md        ← human-readable project overview
└── docs/
    ├── PROJECT.md   ← project goals, audience, constraints
    └── TASKS.md     ← task tracker with emoji states
```

**To use it:**

```bash
# Copy into your new project
cp -r starter-template/. /path/to/your/new-project/

# Edit the placeholders
# Every [FILL IN] or [brackets] item needs your content
```

---

## How to Contribute 🤝

Contributions are welcome. This guide should stay current as the tools evolve — sections need updating, new tools emerge, and real-world experience improves the advice.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for full guidelines, ways to help, and the PR workflow.

---

## Project structure 🗂️

```text
vibe-coding-playbook/
├── sections/           ← guide chapters (the published content)
├── starter-template/   ← copyable project scaffold
├── ai_answers/         ← raw answers from 10 LLMs (the source material)
├── FAQ.md              ← the original questions submitted to each LLM
├── docs/               ← AI instruction files (not guide content)
├── .ai/                ← AI agent behavior rules
├── .opencode/          ← OpenCode config and commands
├── AGENTS.md           ← agent playbook for working in this repo
├── CHANGELOG.md        ← change history for this playbook
└── README.md           ← this file
```

The `docs/` directory contains files for AI agents working on this repo — rules, conventions, tasks. The actual guide lives in `sections/`.
