# AI Entry Point

You are working in a structured vibe coding system.

If a request conflicts with .ai/RULES.md, ask for clarification instead of proceeding.

## Mandatory Reading Order

1. .ai/RULES.md
2. docs/CONVENTIONS.md
3. docs/PROJECT.md
4. docs/TASKS.md

## Workflow

Before starting:

- Read TASKS.md
- Identify current task

During work:

- Make minimal changes
- Stay within scope
- Run markdownlint before and after substantial Markdown edits without asking — use `markdownlint-cli2 '**/*.md' '!**/node_modules/**/*.md'`.
- Proactively remind the user when a commit/push is appropriate — do not commit without being asked.
- When the user sends `/push`, stage all changes, commit with a descriptive message, and push immediately — no further permission needed, no confirmation prompts.

Never:

- Rewrite large sections without request
- Add unnecessary complexity
