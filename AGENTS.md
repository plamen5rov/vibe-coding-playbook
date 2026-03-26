# AGENT PLAYBOOK

## 1. Purpose & Reading Order

1. This file teaches AI coding agents and vibe-coding beginners how to work inside this repo.
2. Follow the mandatory reading chain before touching files:

   - `AI.md`
   - `.ai/RULES.md`
   - `docs/CONVENTIONS.md`
   - `docs/PROJECT.md`
   - `docs/TASKS.md`
3. If instructions conflict, `.ai/RULES.md` wins, followed by `docs/CONVENTIONS.md`, then task-specific asks.
4. Cursor- or Copilot-specific rules do not exist in this repo; default to the guidance here.

## 2. Quick Operating Checklist

- Scan `docs/TASKS.md` to confirm the current focus before you start.
- Read target files completely before editing anything.
- Make minimal, scoped changes; never refactor unrelated sections.
- Keep a log of commands you run so users can reproduce your steps.
- Always remind the user to commit and push; never do it without explicit permission.

## 3. Build / Lint / Test Commands

This repo currently holds Markdown documentation, so linting is the main enforcement mechanism.

### 3.1 Markdownlint Setup

```bash
npm install -g markdownlint-cli2

cat > .markdownlint.json <<'EOF'
{
  "default": true,
  "MD013": false,
  "MD033": false,
  "MD041": false
}
EOF
```

- `MD013` (line length) is off to keep snippets readable.
- `MD033` (inline HTML) is off for future embeds.
- `MD041` is off so files can start with comments or metadata.

### 3.2 Linting Commands

```bash
# Lint every Markdown file
markdownlint-cli2 '**/*.md' '!**/node_modules/**/*.md'

# Auto-fix what can be fixed safely
markdownlint-cli2 --fix '**/*.md' '!**/node_modules/**/*.md'

# Lint a single file when iterating
markdownlint-cli2 docs/CONVENTIONS.md
```

- Run linting before and after substantial edits.
- When a rule cannot be satisfied, explain why in your summary.

### 3.3 Git Hygiene

```bash
git status
git add path/to/file.md
git commit -m "Describe the actual change"
```

- Craft commit messages that are concise but informative: `"Clarify markdownlint setup"` beats `"updates"`.
- Never push without the user's go-ahead; explicitly wait for the `/push` command before running `git push origin <branch>`.

### 3.4 Validation

- Use `ls -R` to double-check file placement when creating new docs.
- Verify new sections link logically from `README.md` or `docs/` entry points.
- Preview Markdown where possible to ensure headings nest correctly.

## 4. Documentation Style Guide

### 4.1 Writing Voice

- Short, direct sentences.
- Practical examples only; no theory dumps.
- Prefer active voice and commands: `"Use short sentences"` not `"You might consider using short sentences"`.
- Keep paragraphs under four lines.

### 4.2 Good vs Bad Sentences

```markdown
❌ Bad: "This is a comprehensive and incredibly detailed document that aims to elucidate every nuance."
✅ Good: "Guide for building vibe-coding docs."

❌ Bad: "You could potentially consider maybe checking lint."
✅ Good: "Run markdownlint before committing."
```

### 4.3 File Naming & Structure

- System files (tasks, rules, guides) stay in uppercase: `TASKS.md`, `RULES.md`, `AGENTS.md`.
- Folder names stay kebab-case: `ai-examples/`, `starter-template/`.
- One idea per file; if a doc exceeds ~300 lines, split it.
- Maintain heading hierarchy (`#`, then `##`, then `###`).

### 4.4 Markdown Formatting

- Use fenced code blocks with language tags for every snippet.
- Bullets for lists, checkboxes for tasks (`- [ ] item`).
- Tables only when data benefits from grid layout.
- Emojis convey state: 🔥 current, 🚧 in-progress, ✅ done, 📌 queued, ❌ anti-pattern.

### 4.5 Example Blocks

```markdown
❌ Bad:
### Steps
1. do thing one two three four five

✅ Good:
### Steps
1. Run `markdownlint-cli2 "**/*.md"`.
2. Fix issues or justify exceptions.
3. Update SUMMARY section if navigation changed.
```

## 5. General Coding Guidelines (for future examples)

- Keep code samples copy-paste ready and runnable.
- Use 2-space indentation for JS/TS/JSON and 4 spaces for Python.
- Prefer descriptive names over clever abbreviations.
- Add comments only when the intent is not obvious.
- Always include basic error checks even in snippets.

### 5.1 Code Examples: Bad vs Good

```javascript
// ❌ Bad: clever but cryptic
const f = (x) => x.reduce((a, b) => a + b, 0);

// ✅ Good: explicit and beginner-friendly
function calculateTotal(numbers) {
  let sum = 0;
  for (const number of numbers) {
    sum += number;
  }
  return sum;
}
```

```python
# ❌ Bad: swallows errors
data = json.loads(raw)

# ✅ Good: guards against invalid input
try:
    data = json.loads(raw)
except json.JSONDecodeError as exc:
    raise ValueError("Invalid JSON payload") from exc
```

## 6. Workflow Rules

### 6.1 Before You Start

1. Re-read `AI.md` to refresh the workflow.
2. Check `docs/TASKS.md` and align with the 🔥 section.
3. Skim `.ai/RULES.md` and `docs/CONVENTIONS.md` to ensure compliance.
4. Confirm there are no Cursor or Copilot overrides (currently none).

### 6.2 While Working

- Stay within the explicit scope of the task request.
- Do not introduce new tools or dependencies without approval.
- Work step-by-step, summarizing progress after each logical chunk.
- Keep diffs tight; avoid opportunistic refactors.

### 6.3 Communication

- Be concise and factual; no filler.
- Surface blockers early and propose a default path forward.
- If a task seems risky or destructive, pause and ask.
- Always remind the user to run `git add`, `git commit`, and `git push` after verifying changes, and wait for the `/push` command before pushing yourself.

## 7. Anti-Patterns & Guardrails

```markdown
❌ Over-engineering simple docs
❌ Rewriting working sections without cause
❌ Expanding scope because "it feels right"
❌ Adding abstractions or templates prematurely
❌ Ignoring `.ai/RULES.md`
❌ Committing/pushing without permission

✅ Make the smallest change that solves the task
✅ Explain trade-offs when deviating from conventions
✅ Document assumptions in your summary
```

## 8. Project Context Recap

- **Audience:** Beginner and intermediate developers learning AI-assisted vibe coding.
- **Goal:** Deliver the most practical guide with real workflows, templates, and actionable advice.
- **Core Value:** No fluff, just tangible examples and checklists.
- **Non-Goals:** No deep theory, no outdated tools, no basic programming lessons.
- **Current Phase:** Write guide sections in `sections/`, complete `starter-template/`, and keep all docs in sync as the project grows.

## 9. When In Doubt

- Re-read the relevant section of this AGENT PLAYBOOK.
- Default to simpler wording, smaller diffs, and clearer explanations.
- Document your reasoning so future agents can follow your trail.
- If clarity is still lacking, stop and ask for direction with a proposed default.

## 10. OpenCode Commands

Custom commands live in `.opencode/commands/`. The file name becomes the command name.

| Command | File | Description |
| --- | --- | --- |
| `/push` | `.opencode/commands/push.md` | Stage, commit, and push pending changes |

### Adding Custom Commands

Create a markdown file in `.opencode/commands/<name>.md`:

```markdown
---
description: Brief description of what the command does
---

The prompt template sent to the LLM when the command runs.

Use $ARGUMENTS for positional parameters.
Use !\`command\` to inject shell output.
Use @filename to include file content.
```

Options (frontmatter):

- `description` - Shown in TUI command list
- `agent` - Which agent should run it
- `model` - Override default model
- `subtask` - Force subagent invocation

Built-in commands: `/init`, `/undo`, `/redo`, `/share`, `/help`
