# Workflow: Running a Vibe Coding Session

![Header](../pictures/04-workflow.png)

## Starting a new project

Do this once, before the first session:

```text
□ Create GitHub repo → clone locally
□ Write docs/PROJECT.md (goals, stack constraints, non-goals)
□ Run /init to generate AGENTS.md → review and refine
□ Add .gitignore (include .env, CLAUDE.local.md)
□ Create .opencode/commands/ with your core slash commands
□ Set up global ~/.config/opencode/opencode.json with personal preferences
□ Install gh CLI for GitHub integration
□ Connect MCP servers you use daily
```

---

## Per-session workflow

This is the loop you'll run for every coding session:

### 1. Start on a branch

```bash
git checkout -b feature/what-youre-building
```

### 2. Ask for a plan first

```text
"Read AGENTS.md and docs/TASKS.md. Then write a plan for [task] before touching any code."
```

Review the plan. If it looks right, approve it. If not, correct it before execution starts. This is faster than debugging after the fact.

### 3. Work in small steps

Don't let the agent run unattended for 20 minutes on a complex task. Check in every few steps:

```text
"Good. Now just do step 1 — don't touch anything else yet."
"That looks right. Now step 2."
```

### 4. Run the verification loop

After every significant change, run your check command:

```bash
npm run lint && npm run test && npm run build
```

Tell the agent in `AGENTS.md` to run this automatically:

```markdown
## Rules for This Agent
- After writing code, always run `npm run lint` and `npm run test`.
- If either fails, fix the errors before proceeding.
```

### 5. Commit as you go

```bash
git add . && git commit -m "feat: add login form with error handling"
```

Frequent small commits give you rollback points. The agent is good at writing commit messages — ask it to.

### 6. Clear context between tasks

When switching to a different feature or topic:

- **Claude Code:** `/clear`
- **OpenCode:** start a new session

Context accumulated from task A will confuse task B. Start clean.

### 7. Merge and push when done

```bash
git checkout main
git merge feature/what-you-built
git push
```

---

## The plan-then-code loop in detail

This pattern is the core of effective vibe coding:

```text
1. You describe the goal in plain language
2. Agent writes a plan to a file (SPEC.md or inline)
3. You review and correct the plan
4. Agent implements the plan
5. You review the diff
6. Agent fixes issues
7. You commit
```

Step 3 is where most time is saved. A wrong plan caught early costs 30 seconds to correct. A wrong implementation caught late costs hours to debug.

**Claude Code:** use Plan mode (Shift+Tab twice). The agent cannot write files until you approve.

**OpenCode:** use the `plan` agent (read-only), then switch to `build` for execution.

---

## Context window hygiene

Both tools have finite context. Quality degrades as it fills up. Signs you need to clear:

- The agent starts contradicting earlier instructions.
- It forgets what files it already modified.
- Responses become slower or less relevant.

**Preventing context overflow:**

- Use `@filename` references instead of pasting file contents.
- Use progressive disclosure in `AGENTS.md` (short root file, detailed docs loaded on demand).
- For deep investigation, ask the agent to use a subagent (Claude Code) so the main context stays clean.
- When context exceeds ~60%, consider clearing and resuming with a summary.

**Resuming after a clear:**

```text
"Read AGENTS.md and docs/TASKS.md. We were working on [feature].
The last completed step was [X]. Continue from step [Y]."
```

If sessions run long, keep a `docs/SESSION.md` scratch file where the agent logs what was done and what's next. Ask it to update this before you end the session.

---

## Working with local models

Both tools support running local models via Ollama or LM Studio.

### Why use local models?

- **Privacy:** Your code never leaves your machine
- **Cost:** Free after hardware investment (GPU needed)
- **Offline:** Works without internet
- **Custom:** Run fine-tuned models for specific domains

### Trade-offs

- Slower than cloud models
- Less capable for complex reasoning
- Need a decent GPU (8GB+ VRAM recommended)
- Context windows smaller on many local models

### OpenCode configuration

Configure in `~/.config/opencode/opencode.json`:

```json
{
  "model": "qwen2.5-coder:14b",
  "provider": {
    "ollama": {
      "url": "http://localhost:11434"
    }
  },
  "numCtx": 32768
}
```

Set `numCtx` to 32768 or higher — agentic coding with tool calls and long files needs the space.

### Claude Code configuration

```bash
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_BASE_URL="http://localhost:11434"
claude --model qwen3-coder:latest
```

### Recommended local models for vibe coding

| Model | Size | Performance |
| --- | --- | --- |
| Qwen2.5-Coder 14B | 14GB | Best all-around |
| CodeLlama 13B | 13GB | Good, slightly slower |
| DeepSeek Coder 6.7B | 6.7GB | Lightweight, decent |
| Qwen2.5-Coder 7B | 7GB | If VRAM is tight |

### When to use local vs cloud

**Use local when:**

- Working on sensitive code
- Offline or on a plane
- Doing simple tasks (file editing, searching)
- Want to experiment without cost

**Use cloud when:**

- Complex architecture decisions
- Debugging tricky issues
- Need the best code quality
- Speed matters

---

## Quick reference checklist

```text
New project:
□ Create GitHub repo → clone locally
□ Write docs/PROJECT.md
□ Run /init → refine AGENTS.md
□ Add .gitignore + .env.example
□ Create core slash commands

Per session:
□ git checkout -b feature/name
□ Ask agent to plan first → approve → execute
□ Work in small steps, check in frequently
□ Run lint + tests after changes
□ Commit frequently — git is your undo button
□ /clear between unrelated tasks
□ Update CHANGELOG.md after features

Before merging:
□ Review the full diff
□ Run the full test suite
□ Merge to main, push
```
