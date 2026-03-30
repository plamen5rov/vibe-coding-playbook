# Sessions forking

Sessions forking in AI coding tools like Claude Code or OpenCode is like creating a "branch" in your chat history with the AI, letting you experiment safely without messing up your main work.

## What Forking Does
Forking copies the entire session history up to that moment—your chats, code changes, tool uses, and context—then starts a brand-new, independent session from there. The original session stays frozen and unchanged, while the fork diverges on its own path with a fresh session ID. It's exactly like `git branch` for code: same starting point, parallel paths ahead. [code.claude](https://code.claude.com/docs/en/sdk/sdk-sessions)

## When to Use It
- **Testing ideas**: Try risky changes (like a wild new architecture) without polluting your main session—perfect for A/B testing approaches. [reddit](https://www.reddit.com/r/PromptEngineering/comments/1kwbmad/built_a_claude_code_js_sdk_with_session/)
- **Parallel experiments**: Run multiple "what if" scenarios from the same checkpoint, like JWT vs. OAuth auth in separate forks. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/sessions)
- **Multi-terminal work**: Avoid context corruption when resuming across terminals or delegating subtasks to subagents. [mcpmarket](https://mcpmarket.com/tools/skills/claude-session-fork)
- **Keeping main clean**: Explore tangents (e.g., a feature prototype) while your primary session stays laser-focused. [kau](https://kau.sh/blog/agent-forking/)

## When Not to Use It
- **Simple continuations**: Don't fork for routine next steps—stick to resuming the original to build deeper, linear context. [code.claude](https://code.claude.com/docs/en/sdk/sdk-sessions)
- **File-heavy main work**: Forks share the same filesystem, so file edits in one affect all; use checkpoints or Git for true isolation. [platform.claude](https://platform.claude.com/docs/en/agent-sdk/sessions)
- **Over-forking beginners**: As a newbie, it adds session-tracking overhead—master single sessions first before branching. [wmedia](https://wmedia.es/en/tips/claude-code-fork-session-branch-conversations)
- **Token limits**: Each fork duplicates history, burning more compute; reserve for genuine divergences, not every tweak. [trigger](https://trigger.dev/blog/10-claude-code-tips-you-did-not-know)

## What is the difference between fork and resume
Forking and resuming are two ways to pick up AI coding sessions in tools like Claude Code or OpenCode, but they handle your chat history differently—like branches vs. a straight road in Git.

### Key Differences
Resume loads your exact existing session and adds new messages right to the end of that same history and session ID. It keeps everything linear: past chats, code edits, tool results, and learnings build on each other seamlessly.

Fork copies the session history up to now, creates a brand-new session ID, and lets the copy diverge independently. Your original session stays untouched and frozen at the fork point, while the new one goes off on its own path.

### Comparison Table

| Aspect       | Resume                         | Fork                            |
| ------------ | ------------------------------ | ------------------------------- |
| History      | Appends to original            | Copies then branches separately |
| Session ID   | Same as before                 | New, unique ID                  |
| Original     | Continues evolving             | Unchanged, like a snapshot      |
| File Changes | Shared across same project dir | Shared (no isolation)           |
| Use Case     | Steady progress on main work   | Safe experiments                |

### Resume Pros/Cons
Perfect for daily work: deeper context means smarter AI responses over time. But if you mess up, you pollute the main history (use undos or CLAUDE.md for fixes).

### Fork Pros/Cons
Great for "what if" tests without risk. Downside: duplicate history eats tokens, and tracking multiple sessions gets confusing for newbies—merge insights back manually if needed.

## When to use revert with forking

**Reverting** in AI coding sessions (like Claude Code or OpenCode) rolls back your chat history, code, or tool state to an earlier checkpoint, undoing changes without losing the full log. Pair it with forking to safely rewind experiments before branching.

### What Revert Does
It jumps the session back to a prior "checkpoint" (like a past message, user input, or tool call), erasing everything after that point in the active session. Your original history stays intact as a record, but the session resets to that clean state—great for scrapping bad AI suggestions or buggy code edits.[ from prior]

### When to Use Revert *With* Forking
- **Failed experiments first**: If a fork goes wrong (e.g., AI adds broken logic), revert *inside* the fork to a good point, then fork again from there—keeps your main session pristine.
- **Checkpoint recovery**: Revert to a stable user message or decision point in the fork, then diverge safely (e.g., test auth method A vs. B from the same clean base). [reddit](https://www.reddit.com/r/opencodeCLI/comments/1s30y0e/is_it_fundamentally_impossible_to_revert_to_fork/)
- **Question tool fixes**: When AI asks a question and your reply leads astray, revert to pre-question, fork, and retry answers without polluting the trunk.
- **Multi-agent handoffs**: Revert sub-agent results in a fork if they mess up, preserving the parent session.

### When *Not* to Use Revert with Forking
- **Main session tweaks**: Don't revert your primary work—use undos or CLAUDE.md instructions instead; forks are for side quests only.
- **File-shared projects**: Revert doesn't snapshot files uniquely, so changes might linger across forks—commit to Git first.
- **Newbie overload**: Skip if tracking checkpoints feels fuzzy; resume linearly until comfy.

### Quick Workflow
1. Spot trouble in fork.
2. `/revert <checkpoint-id>` (or UI pick).
3. `/fork` from cleaned fork if needed.
Main session? Untouched.

