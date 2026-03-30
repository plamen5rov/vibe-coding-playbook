# OpenCode Commands

## Overview

Custom commands live in `.opencode/commands/`. The file name becomes the command name.

| Command | File | Description |
| --- | --- | --- |
| `/push` | `.opencode/commands/push.md` | Stage, commit, and push pending changes |

## Adding Custom Commands

Create a markdown file in `.opencode/commands/<name>.md`:

```markdown
---
description: Brief description of what the command does
---

The prompt template sent to the LLM when the command runs.

Use $ARGUMENTS for positional parameters.
Use !\`command\` to inject shell output.
Use @filename to include file content.
```

Options (frontmatter):

- `description` - Shown in TUI command list
- `agent` - Which agent should run it
- `model` - Override default model
- `subtask` - Force subagent invocation

Built-in commands: `/init`, `/undo`, `/redo`, `/share`, `/help`
