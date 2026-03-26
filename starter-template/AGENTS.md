# [PROJECT NAME] — Agent Context

> Replace everything in `[brackets]` with your project's specifics.
> Keep this file under 200 lines. Long files get skimmed, not read.

## Project Overview

**Goal:** [One sentence. What does this project do and for whom?]

**Status:** [e.g., Early prototype / Active development / Maintenance]

## Tech Stack

- **Language:** [e.g., TypeScript 5, Python 3.12]
- **Framework:** [e.g., Next.js 14 App Router, FastAPI]
- **Database:** [e.g., PostgreSQL via Prisma]
- **Styling:** [e.g., Tailwind CSS]
- **Package manager:** [e.g., pnpm, bun]
- **Tests:** [e.g., Vitest, pytest]

## Repository Structure

```text
[project-root]/
├── src/           # [describe main source]
├── docs/          # Project documentation and AI context files
├── tests/         # Test files
└── AGENTS.md      # This file — read every session
```

## Commands

```bash
# Install dependencies
[install command]

# Start dev server
[dev command]

# Run tests
[test command]

# Lint
[lint command]

# Build
[build command]
```

## Coding Conventions

- [e.g., Use named exports only, no default exports]
- [e.g., All functions must have TypeScript types — no `any`]
- [e.g., File names: kebab-case for utilities, PascalCase for components]
- [e.g., Prefer `async/await` over `.then()` chains]

## Rules for This Agent

- Read `docs/TASKS.md` before starting any session.
- Make minimal, scoped changes. Do not refactor unrelated code.
- Run [lint command] before finalizing any changes.
- Never commit `.env` or secrets.
- Always ask before changing the tech stack or adding new dependencies.
- When the user sends `/push`, stage all changes, commit with a descriptive message, and push — no further permission needed.

## Important Constraints

- [e.g., The database schema must stay backward compatible — use migrations]
- [e.g., No jQuery — vanilla JS only]
- [e.g., Mobile-first responsive design required]

## References

- See `docs/PROJECT.md` for full project goals and non-goals.
- See `docs/TASKS.md` for current work items.
