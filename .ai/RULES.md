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
- When the user sends `/push`, stage all changes, commit with a descriptive message, and push — no further permission needed.
- Run `markdownlint-cli2 '**/*.md' '!**/node_modules/**/*.md'` before and after any substantial Markdown edits — no permission needed, just do it.
- Auto-fix lint issues with `markdownlint-cli2 --fix` when safe; explain any that cannot be auto-fixed.

## Communication

- Be concise
- Ask before major changes

## Anti-Patterns

- Over-engineering
- Rewriting working code
- Adding abstractions too early
