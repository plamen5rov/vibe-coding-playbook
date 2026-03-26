# Prompt Engineering

Your prompts are the interface between your brain and the AI. Write them well, and the agent delivers. Write them poorly, and you get guesswork.

This section teaches you to write prompts that get results.

---

## The anatomy of a good prompt

Every effective prompt has four parts:

| Part | What it does | Example |
| --- | --- | --- |
| **Context** | What the agent needs to know | "Read AGENTS.md and docs/TASKS.md" |
| **Goal** | What you want done | "Add user authentication" |
| **Constraints** | What to avoid or limit | "No external dependencies" |
| **Format** | How you want the output | "Write a plan in SPEC.md first" |

A prompt missing any of these parts is incomplete.

---

## Bad vs good prompts

### Adding a feature

```text
❌ Bad:
"Add authentication to the app."
```

```text
✅ Good:
"Read docs/PROJECT.md to understand our tech stack. Then add JWT-based authentication:
- Create a POST /api/auth/login endpoint
- Return a token on successful login
- Add the token to .env.example (no value)
- Update docs/API.md with the new endpoint
Write a plan to SPEC.md before touching any code."
```

The good version has context, goal, constraints, and format. The bad version leaves everything to guesswork.

### Fixing a bug

```text
❌ Bad:
"The login button isn't working."
```

```text
✅ Good:
"The login button on /login returns a 500 error. Steps to reproduce:
1. Go to /login
2. Enter valid credentials
3. Click the login button
Expected: redirect to /dashboard
Actual: 500 error in console
Check the server logs and fix the underlying issue."
```

Good bug reports include steps to reproduce, expected vs actual behavior, and a specific task.

### Refactoring

```text
❌ Bad:
"Clean up the codebase."
```

```text
✅ Good:
"Refactor the functions in src/services/payment/ to use async/await consistently.
Keep existing function signatures. Do not change business logic.
Run tests after to verify nothing broke."
```

---

## The plan-then-execute pattern

This is the single most effective prompt pattern in vibe coding.

```text
"Before touching any code, write a plan to docs/SPEC.md that covers:
1. What files need changing
2. The approach you'll take
3. Any risks or edge cases
Wait for my approval before implementing."
```

This forces the agent to think before acting. You catch misunderstandings in the plan phase — where they cost 30 seconds to fix, not hours in the debug phase.

Claude Code has a built-in Plan mode (Shift+Tab twice) that physically prevents the agent from writing code until you approve. OpenCode has a `plan` agent that is read-only by default.

---

## How to correct the agent without restarting

When the agent goes wrong, you don't need to start over. Guide it back:

### Point out the specific issue

```text
"That's not quite right — I need X, not Y. Please revise."
```

### Provide missing context

```text
"I forgot to mention: the API uses a Python Flask backend, not Express."
```

### Ask for explanation first

```text
"Before you fix it, explain why you chose this approach. I want to understand."
```

### Request a smaller step

```text
"Stop. Just do the first part — create the file and one function. Don't proceed further until I say."
```

---

## Prompt templates for common tasks

Copy these into your prompts or create slash commands from them.

### Add a feature

```text
Read AGENTS.md and docs/TASKS.md. Then:
1. Write a plan to docs/SPEC.md covering the approach and files involved
2. Wait for my approval
3. Implement the feature
4. Run tests to verify it works
5. Update CHANGELOG.md
```

### Fix a bug

```text
Fix the following bug:
[Describe the bug with steps to reproduce, expected vs actual behavior]
Check the relevant code files and identify the root cause.
Write the fix, then run tests to verify.
```

### Write tests

```text
Write tests for [file or function]:
- Cover the main use cases
- Include edge cases
- Use the same test framework as the existing tests
Run the test suite to confirm all tests pass.
```

### Refactor

```text
Refactor [what] to [what you want it to become]:
- Do not change function signatures
- Do not change business logic
- Do not add new dependencies
- Run tests after to verify nothing broke
```

---

## When prompts go wrong

### The agent ignores part of your prompt

If the agent skips something you asked for, be explicit:

```text
"Do all three things I asked: 1) create the file, 2) add tests, 3) update CHANGELOG.md."
```

### The agent keeps going off-track

Use the "one step at a time" pattern:

```text
"Only do step 1 from the plan. Do not proceed to step 2 until I tell you."
```

### The agent asks too many questions

Give it permission to make reasonable assumptions:

```text
"Make a reasonable choice for [X] if I haven't specified. Document your assumption in a comment."
```

---

## Pro tips

- **One task per prompt.** If you ask for three things, the agent may forget one. Break it up.
- **Use the agent's output.** If the agent writes something good, keep it. Don't rewrite unnecessarily.
- **Tell the agent what you liked.** "That approach worked well — use the same pattern for the next feature."
- **Be specific about file paths.** "Edit src/api/users.py, not just 'the user file'."
- **State constraints explicitly.** "Use only the dependencies already in package.json" is clearer than "keep it simple."
