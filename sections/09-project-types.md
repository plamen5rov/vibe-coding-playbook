# Project Types

Different projects need different setups. This section shows you how to start each type correctly.

---

## How to use this section

| Project type | When to use |
| --- | --- |
| Web app | Full-stack applications with UI |
| API / backend | Headless services, microservices |
| CLI tool | Terminal utilities, scripts |
| Script / automation | One-off tasks, data processing |
| Library / package | Reusable code for other projects |

Each type has a starter checklist. Copy the pattern that fits your project.

---

## Web app

**Characteristics:** User interface, routing, server-side logic, database

### Web app stack

| Use case | Stack |
| --- | --- |
| Quick prototype | Next.js, Vercel |
| React + backend control | Next.js (App Router), Node.js |
| Python web app | Django or Flask |
| Simple static site | Astro |
| Full custom | Vite + any backend |

### Web app checklist

```text
□ Create GitHub repo
□ Clone locally
□ Choose stack based on your constraints (not defaults)
□ Write docs/PROJECT.md with:
  - What the app does
  - Target users
  - Tech stack + why
  - Hosting plan (Vercel, Railway, VPS?)
□ Create AGENTS.md with stack details
□ Add .gitignore (node_modules, .env)
□ Create .env.example with all env vars (empty values)
□ Initialize the framework
□ Run the dev server to verify it works
□ Make one trivial commit to confirm the flow
```

### Useful MCPs for web apps

- GitHub (issues, PRs)
- Puppeteer or Playwright (if testing)
- Vercel (deployment)

---

## API / backend

**Characteristics:** No UI, business logic, data processing, REST/GraphQL endpoints

### API stack

| Use case | Stack |
| --- | --- |
| Node.js API | Express, Fastify |
| Python API | FastAPI (modern, auto-docs) |
| Go API | Gin, Echo |
| Simple | Python Flask |
| Microservices | Depends on team |

### API checklist

```text
□ Create GitHub repo
□ Clone locally
□ Define the API surface first:
  - What endpoints?
  - What data format?
  - What database?
□ Write docs/PROJECT.md with API spec
□ Create AGENTS.md with:
  - The endpoints you'll build
  - Error handling pattern
  - Auth approach (if any)
□ Add .gitignore and .env.example
□ Initialize the project
□ Add a health check endpoint first
□ Verify it runs
```

### Useful MCPs for APIs

- GitHub
- Database (PostgreSQL, MongoDB)
- Docker (if containerizing)

---

## CLI tool

**Characteristics:** Terminal-based, no UI, often single-purpose

### CLI tool stack

| Use case | Stack |
| --- | --- |
| Cross-platform | Node.js (commander), Python (click) |
| Shell script | Bash (simple), Go (compiled) |
| Quick script | Python |
| Performance critical | Go, Rust |

### CLI tool checklist

```text
□ Create GitHub repo
□ Clone locally
□ Define what the CLI does:
  - What commands?
  - What arguments?
  - What output?
□ Write docs/PROJECT.md with command spec
□ Create AGENTS.md
□ Decide: single script or proper package?
  - Script: just files
  - Package: proper project structure with tests
□ Add .gitignore
□ Implement --help and --version first
□ Verify with: node tool.js --help
```

### Useful MCPs for CLI tools

- GitHub
- npm (if publishing)

---

## Script / automation

**Characteristics:** One-off, run and done, data processing

**Note:** Don't over-engineer a script into a project. If it's truly one-off, use a simple file.

### When to use a script vs a project

| Script | Project |
| --- | --- |
| Run once or rarely | Run frequently |
| Simple, few files | Complex, many files |
| No tests needed | Tests are valuable |
| No dependencies or few | Multiple dependencies |

### Script checklist

```text
□ Decide: script or project?
  - Script: just one .py, .js, or .sh file
  - Project: use project checklist instead
□ For a script:
  - Just create the file in your project
  - Add a brief comment explaining what it does
  - Make it executable if needed
  - Commit it if it might be useful later
□ For automation that runs regularly:
  - Create a proper project
  - Add scheduling (cron, systemd)
  - Consider logging
□ Document the inputs and outputs
□ Test with sample data
```

---

## Library / package

**Characteristics:** Reusable code, published to npm/pip/crate, used by other projects

### Tech stack recommendations

| Language | Package manager |
| --- | --- |
| JavaScript/TypeScript | npm, pnpm |
| Python | pip, pyproject.toml |
| Go | go modules |
| Rust | Cargo |

### Starter checklist

```text
□ Create GitHub repo
□ Clone locally
□ Decide: open source or internal?
  - Open source: add LICENSE, CONTRIBUTING.md
  - Internal: skip public docs
□ Write docs/PROJECT.md:
  - What the library does
  - API surface (main exports)
  - Versioning strategy
□ Create AGENTS.md with:
  - How to use the library
  - Build/publish commands
  - Test requirements
□ Set up:
  - Package.json / pyproject.toml / Cargo.toml
  - Tests (Vitest, pytest, Cargo test)
  - Linter
□ First commit: working empty skeleton
```

### Useful MCPs for libraries

- GitHub
- npm / PyPI (if publishing)

---

## How to choose your stack

Don't let the agent choose for you. The agent suggests whatever is popular in its training data — it has no knowledge of your constraints.

### Questions to answer first

1. **What does this project need to do?** (features, scale)
2. **Where will it run?** (VPS, cloud, local, browser)
3. **What do you already know?** (don't learn a new stack + vibe coding at once)
4. **What are your constraints?** (budget, hosting, team size)
5. **Will it need to scale?** (start simple, refactor later)

### The workflow

1. Write constraints in `docs/PROJECT.md`
2. Ask the agent: "Given these constraints, suggest a stack and explain tradeoffs"
3. Discuss, decide, then document in `AGENTS.md`

This is covered in detail in section 02.

---

## Quick reference: MCPs by project type

| Project type | Useful MCPs |
| --- | --- |
| Web app | GitHub, Vercel, browser automation |
| API / backend | GitHub, database, Docker |
| CLI tool | GitHub, npm/pip |
| Script | (usually none needed) |
| Library | GitHub, package registry |
