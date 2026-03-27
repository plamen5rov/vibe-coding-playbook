# Contributing to the Vibe Coding Playbook

Contributions are welcome. This guide should stay current as the tools evolve — sections need updating, new tools emerge, and real-world experience improves the advice.

---

## Ways to contribute

- **Fix something wrong** — outdated URL, incorrect advice, broken command.
- **Improve a section** — better examples, clearer explanation, missing edge case.
- **Add a new section** — a topic not covered yet (e.g., Claude Code hooks, specific MCP setups).
- **Share your workflow** — if you have a battle-tested pattern, open an issue or PR.

---

## Via pull request

```bash
# 1. Fork the repo on GitHub
# 2. Clone your fork
git clone https://github.com/plamen5rov/vibe-coding-playbook.git
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

---

## Via issue

If you spot something wrong or have a suggestion but don't want to write the fix yourself, [open an issue](https://github.com/plamen5rov/vibe-coding-playbook/issues){target="_blank" rel="noopener"}. Describe what's wrong or what's missing.

---

## Style guidelines

- Short, direct sentences. Active voice. No filler.
- Keep paragraphs under four lines.
- Include a bad/good example when introducing a new practice.
- One idea per PR — small, focused changes are easier to review.
- Run markdownlint before submitting — zero errors expected.

See [`docs/CONVENTIONS.md`](docs/CONVENTIONS.md) for the full style guide.

---

## What belongs where

| Content type | Location |
| --- | --- |
| Guide chapters | `sections/` |
| Starter template files | `starter-template/` |
| Agent/AI instructions for this repo | `docs/`, `.ai/`, `AGENTS.md` |
| Raw LLM survey answers | `ai_answers/` (read-only, do not edit) |

---

## Markdownlint setup

```bash
npm install -g markdownlint-cli2

# Lint all files
markdownlint-cli2 '**/*.md' '!**/node_modules/**/*.md'

# Auto-fix safe issues
markdownlint-cli2 --fix '**/*.md' '!**/node_modules/**/*.md'
```

The `.markdownlint.json` in the repo root disables MD013 (line length), MD033 (inline HTML), and MD041 (first-line heading).
