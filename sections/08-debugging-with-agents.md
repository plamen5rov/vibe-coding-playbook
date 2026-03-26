# Debugging with Agents

The agent will produce bugs. So will you. This section shows you how to debug effectively when working with an AI.

---

## The debugging mindset

When something breaks, you have two possible sources:

1. Code the agent wrote (wrong implementation or logic)
2. Instructions you gave (unclear or missing context)

Most beginners blame the agent. Usually, the issue is in how they asked.

**Before you debug the code, ask:**

- Did I clearly describe what I wanted?
- Did I provide enough context?
- Did I mention constraints the agent might have missed?

---

## The explain-before-fix pattern

When the agent produces wrong output, don't just say "fix it." Ask it to explain first.

```text
"This output isn't what I expected. Before you fix it, explain:
1. What your code does, step by step
2. Why you chose this approach
3. Where the bug likely is"
```

This reveals the agent's reasoning. Often the bug is a wrong assumption you can correct directly.

---

## Common failure modes

### 1. Hallucinated APIs

The agent invents library functions that don't exist.

**Symptoms:** Import errors, "function not found" in runtime.

**Fix:** Tell the agent exactly which libraries and versions you're using. Include a link to real docs.

```text
"I'm using Python 3.11 with the standard library only. Do not import external packages."
```

### 2. Wrong assumptions about your stack

The agent assumes a different framework, language version, or tool.

**Fix:** State your stack explicitly in every prompt:

```text
"This is a Next.js 14 app with App Router, using TypeScript and Prisma with PostgreSQL."
```

### 3. Overengineering

The agent builds a complex solution for a simple problem.

**Fix:** Set scope explicitly:

```text
"Keep this simple — just a basic script, no config files, no database."
```

### 4. Conflating tasks

The agent mixes requirements from a previous task with the current one.

**Fix:** Clear the session between unrelated tasks (section 04), or explicitly reset:

```text
"Forget the previous task. We're now working on [new task]. Here's what I need:"
```

### 5. Ignoring error messages

The agent sometimes ignores or misinterprets error output.

**Fix:** Paste the exact error into your prompt:

```text
"I'm getting this error:
[PASTE ERROR HERE]
Fix it."
```

---

## The diagnostic loop

When something breaks, run this loop:

1. **Run the code** — see the actual error
2. **Read the error message** — understand what happened
3. **Ask the agent to explain** — "What does this error mean?"
4. **Fix or guide** — either let the agent fix it, or direct it specifically
5. **Verify** — run again to confirm the fix

Never accept "it should work now" without running the code.

---

## Using git to recover

Git is your safety net. When the agent produces something unusable:

### Discard all changes

```bash
git checkout .
```

This resets to the last commit. Start fresh with a better prompt.

### See what changed

```bash
git diff
```

Review every line the agent modified. You might find it did something unexpected.

### Go back to a specific commit

```bash
git log --oneline -10
git checkout <commit-hash> -- .
```

Useful when you want to keep some changes but not others.

---

## When to restart vs course-correct

| Situation | Action |
| --- | --- |
| Agent misunderstood the goal | Course-correct — explain the goal differently |
| Agent keeps going in circles | Course-correct — narrow the scope |
| Agent produced completely wrong code | Course-correct — ask it to explain first |
| Agent is confused about the project state | Restart — clear context and re-explain |
| You've made multiple fixes that didn't help | Restart — `git checkout .` and start over |

The nuclear option:

```text
"Let's start over. Run git checkout . to reset, then I'll give you a clearer prompt."
```

---

## Debugging checklist

```text
□ Run the code and see the actual error
□ Read the error message carefully
□ Ask: did I give the agent enough context?
□ Ask the agent to explain its reasoning
□ Fix at the right level (prompt vs code)
□ Verify the fix by running again
□ Commit the working state
□ If it broke again, document what changed
```

---

## Preventing bugs in the first place

The best debugging is not needing to debug. These habits prevent issues:

- **Plan-first** (section 04) — catch misunderstandings before code is written
- **Small steps** — don't let the agent run for 20 minutes unattended
- **Run tests after every change** — tell the agent to do this automatically
- **Review every file** — don't accept code you haven't read
- **Keep AGENTS.md accurate** — outdated context causes wrong assumptions
