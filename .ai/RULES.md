# AI Rules (Project-Level)

## Priority

These rules override default AI behavior.

## Core Principles

- Make minimal, precise changes
- Never refactor unrelated code
- Do not introduce new tools or dependencies without approval

## Scope Control

- Only do what is explicitly requested
- Do not expand features automatically

## Code Style

- Follow docs/CONVENTIONS.md strictly
- Prefer simple solutions

## Workflow

- Always check docs/TASKS.md before starting
- Work step-by-step
- Run `markdownlint-cli2 '**/*.md' '!**/node_modules/**/*.md'` before and after any substantial Markdown edits — no permission needed, execute immediately.
- Fix lint issues without asking: run `markdownlint-cli2 --fix` for auto-fixable issues, then manually edit any remaining violations — all without requesting permission.
- Proactively remind the user when a commit/push is appropriate — do not commit without being asked.
- When the user sends `/push`, stage all changes, commit with a descriptive message, and push immediately — no further permission needed, no confirmation prompts.

## Communication

- Be concise
- Ask before major changes

## Anti-Patterns

- Over-engineering
- Rewriting working code
- Adding abstractions too early
