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
- Run markdownlint before and after any substantial Markdown edits — no permission needed, execute immediately. Fix lint issues without asking: run `markdownlint-cli2 --fix` for auto-fixable issues, then manually edit any remaining violations.
- Proactively remind the user when a commit/push is appropriate (e.g., after a significant batch of changes). Do not commit without being asked.
- When the user sends `/push`, stage all changes, commit with a descriptive message, and push immediately — no further permission needed, no confirmation prompts.

## 3. Build / Lint / Test Commands

For markdownlint setup and commands, read @docs/markdownlint.md.

### 3.3 Git Hygiene

```bash
git status
git add path/to/file.md
git commit -m "Describe the actual change"
```

- Craft commit messages that are concise but informative: `"Clarify markdownlint setup"` beats `"updates"`.

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

For formatting rules, read @docs/markdown-formatting.md.

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

For code examples and guidelines, read @docs/coding-guidelines.md.

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
- When the user sends `/push`, stage all changes, commit with a descriptive message, and push — no further permission needed.

## 7. Anti-Patterns & Guardrails

```markdown
❌ Over-engineering simple docs
❌ Rewriting working sections without cause
❌ Expanding scope because "it feels right"
❌ Adding abstractions or templates prematurely
❌ Ignoring `.ai/RULES.md`

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

For custom command reference, read @docs/opencode-commands.md.
