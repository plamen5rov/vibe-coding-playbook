# Vibe Coding Playbook

A practical guide to building software with AI coding agents — specifically OpenCode and Claude Code.

No theory. No fluff. Just workflows, templates, and checklists you can use today.

---

## What is vibe coding?

Vibe coding (also called context coding or agentic engineering) is a development workflow where you work with an AI agent as a fast, capable junior developer. You describe goals, review output, and own the result. The agent writes code, runs commands, edits files, and commits changes.

The quality of the output depends almost entirely on the quality of the context you provide. This playbook shows you how to set that up.

---

## Guide

### [1. Git & GitHub](sections/01-git-github.md)

How to set up your repo, what to commit vs ignore, and why feature branches matter even when working solo.

### [2. Context Files](sections/02-context-files.md)

The files to create before your first session — `AGENTS.md`, `PROJECT.md`, `TASKS.md` — what goes in them and how long they should be.

### [3. Best Practices](sections/03-best-practices.md)

Slash commands, agents, MCP servers, `CHANGELOG.md`, security hygiene, and the habits that separate effective vibe coders from frustrated ones.

### [4. Workflow](sections/04-workflow.md)

The per-session loop: plan first, work in small steps, commit frequently, clear context between tasks. Includes a quick-reference checklist.

### [5. OpenCode vs Claude Code](sections/05-opencode-vs-claude-code.md)

Side-by-side feature comparison, tool-specific tips, and how to run both on the same project.

### [6. Resources](sections/06-resources.md)

Curated official docs, high-quality guides, and how to stay current as the tooling evolves quickly.

---

## Starter Template

The [`starter-template/`](starter-template/) directory is a generic project scaffold you can copy into any new vibe-coding project.

```text
starter-template/
├── AGENTS.md        ← main AI context file (fill in your project details)
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

## How to Contribute

Contributions are welcome. This guide should stay current as the tools evolve — sections need updating, new tools emerge, and real-world experience improves the advice.

### Ways to contribute

- **Fix something wrong** — outdated URL, incorrect advice, broken command.
- **Improve a section** — better examples, clearer explanation, missing edge case.
- **Add a new section** — a topic not covered yet (e.g., Claude Code hooks, specific MCP setups, common mistakes).
- **Share your workflow** — if you have a battle-tested pattern, open an issue or PR.

### Via pull request

```bash
# 1. Fork the repo on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/vibe-coding-playbook.git
cd vibe-coding-playbook

# 3. Create a branch
git checkout -b improve/section-name

# 4. Make your changes
# Sections live in sections/
# Starter template lives in starter-template/
# Run markdownlint before submitting:
markdownlint-cli2 '**/*.md' '!**/node_modules/**/*.md'

# 5. Commit and push
git add . && git commit -m "Improve git workflow section with worktree example"
git push -u origin improve/section-name

# 6. Open a PR on GitHub
gh pr create --base main
```

### Via issue

If you spot something wrong or have a suggestion but don't want to write the fix yourself, [open an issue](https://github.com/YOUR_USERNAME/vibe-coding-playbook/issues). Describe what's wrong or what's missing.

### Guidelines

- Keep the style consistent: short sentences, practical examples, no fluff. See [`docs/CONVENTIONS.md`](docs/CONVENTIONS.md).
- One idea per PR. Small, focused changes are easier to review.
- Include a bad/good example when introducing a new practice.
- Run markdownlint before submitting — zero errors expected.

---

## Project structure

```text
vibe-coding-playbook/
├── sections/           ← guide chapters (the published content)
├── starter-template/   ← copyable project scaffold
├── docs/               ← AI instruction files (not guide content)
├── .ai/                ← AI agent behavior rules
├── .opencode/          ← OpenCode config and commands
├── AGENTS.md           ← agent playbook for working in this repo
└── README.md           ← this file
```

The `docs/` directory contains files for AI agents working on this repo — rules, conventions, tasks. The actual guide lives in `sections/`.
