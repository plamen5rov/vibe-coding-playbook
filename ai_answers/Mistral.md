<!-- markdownlint-disable-file -->


# Vibe/Context Coding FAQ Answers

## Git/GitHub

### Should I create a GitHub repo first and then clone it locally, or let OpenCode (Claude Code) create it for me?
**Answer:** Create a GitHub repo first, then clone it locally. This is the standard approach and ensures your repo is properly linked to GitHub from the start. Claude Code and OpenCode can also create a repo for you, but it's best to create it on GitHub first for better control and visibility.

**References:**
- [Collaborating with GitHub](https://oboe.com/learn/github-and-claude-code-collaboration-1l8ix0q/collaborating-with-github-2)
- [GitHub x Claude](https://www.reddit.com/r/ClaudeAI/comments/1khiw7e/github_x_claude_how_does_it_work/)
- [Claude Code GitHub Topics](https://github.com/topics/claude-code)

### Should I include OpenCode (Claude Code) config directory or any other specific OpenCode (Claude Code) files in the .gitignore file?
**Answer:** Include OpenCode/Claude Code config directories and files in your .gitignore to exclude them from version control. Use a dedicated `.claudeignore` file if you want Claude Code to access specific ignored files. For example, add `.claude` and `.opencode` directories to .gitignore, but create a `.claudeignore` file for Claude-specific exclusions.

**References:**
- [Need for dedicated .claudeignore file](https://github.com/anthropics/claude-code/issues/1304)
- [Allow Claude Code to access gitignored files](https://github.com/anthropics/claude-code/issues/2305)
- [How to tell claude CLI agent to ignore directories](https://github.com/anthropics/claude-code/issues/79)

### As a solo developer, should I create at all any branches/PRs, etc., or just commit and push every new feature?
**Answer:** Even as a solo developer, use branches and PRs for significant changes. This keeps your main branch clean and allows for better organization, review, and rollback if needed. For small or quick fixes, committing directly to main is acceptable.

**References:**
- [Do you commit to master on your solo projects?](https://dev.to/daveskull81/git-workflow-do-you-commit-to-master-on-your-solo-projects-hi4)
- [Do you use pull requests if you are the only developer?](https://www.reddit.com/r/learnprogramming/comments/16bl695/do_you_use_pull_requests_if_you_are_the_only/)
- [Why I always raise a pull request on solo projects](https://www.tempertemper.net/blog/why-i-always-raise-a-pull-request-on-solo-projects)

## Preparatory Work

### Before even starting OpenCode (Claude Code), should I create and upload in the project's directory files that will explain the project itself to OpenCode (Claude Code)?
**Answer:** Create a CLAUDE.md file (for Claude Code) or AGENTS.md (for OpenCode) in your project root. This file should describe your project, technical stack, coding standards, and any specific instructions for the AI. Keep it concise but detailed enough to provide context. Use the `/init` command to generate a starter file, then refine it.

**References:**
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
- [OpenCode Rules](https://opencode.ai/docs/rules/)
- [How to Write a Good CLAUDE.md File](https://www.builder.io/blog/claude-md-guide)

### Should it be one file or more?
**Answer:** Use one main file (e.g., CLAUDE.md or AGENTS.md) for general context. If your project is complex, split concerns into multiple files (e.g., one for coding standards, one for architecture).

**References:**
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
- [How to Write a Good CLAUDE.md File](https://www.builder.io/blog/claude-md-guide)

### What to include in this file? How long should it be?
**Answer:** Include project overview, technical stack, coding standards, and example commands. Be specific about your project structure, dependencies, and any unusual patterns.

**References:**
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
- [How to Write a Good CLAUDE.md File](https://www.builder.io/blog/claude-md-guide)

### Should I decide what technical stack to be used, or let OpenCode (Claude Code) suggest ones for me?
**Answer:** Decide the technical stack yourself. The AI can suggest stacks, but your expertise and project requirements should drive the decision. Use the AI to validate or refine your choices.

**References:**
- [AI Tech Stacks for 2025](https://smartdev.com/ai-tech-stacks-the-blueprint-for-2025/)
- [Ultimate AI Tech Stack Guide](https://www.tristatetechnology.com/blog/ultimate-ai-tech-stack-guide)

### If there should be more than one preliminary file, what are they?
**Answer:** The main file is CLAUDE.md/AGENTS.md. Additional files might include:
- `.gitignore` (and `.claudeignore`)
- `README.md` for human readers
- `CHANGELOG.md` for tracking changes
- A `docs/` directory for additional documentation

**References:**
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
- [OpenCode Rules](https://opencode.ai/docs/rules/)

### How should I name this file/s?
**Answer:** Name context files clearly, e.g., CLAUDE.md, AGENTS.md, or PROJECT_CONTEXT.md. Place them in the project root or a dedicated `.claude`/`.opencode` directory.

**References:**
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
- [OpenCode Rules](https://opencode.ai/docs/rules/)

### Should I create this file/s in a separate directory? How to name it? Should I commit it to GitHub, or include it in .gitignore?
**Answer:** Commit context files to your repo, but exclude sensitive or AI-specific config files (e.g., API keys) using .gitignore or .claudeignore.

**References:**
- [Need for dedicated .claudeignore file](https://github.com/anthropics/claude-code/issues/1304)
- [Allow Claude Code to access gitignored files](https://github.com/anthropics/claude-code/issues/2305)

## Best Practices

### What other files do I need for a vibe/context coding project with OpenCode (Claude Code)?
**Answer:** You will need a CLAUDE.md/AGENTS.md for context, a .gitignore (and possibly .claudeignore), and a README.md for humans. Consider a CHANGELOG.md for tracking changes and a docs/ directory for additional documentation.

**References:**
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
- [OpenCode Rules](https://opencode.ai/docs/rules/)

### Should I create in advance skills, agents, MCP, and tools for this specific project, or let OpenCode (Claude Code) create them for me during coding?
**Answer:** Create skills, agents, and MCP tools in advance if they are project-specific. For general or reusable tools, use global config or shared directories.

**References:**
- [Skills vs MCP tools for agents](https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what)
- [Spring AI Agentic Patterns](https://spring.io/blog/2026/01/13/spring-ai-generic-agent-skills/)

### Should I create skills, agents, MCP, and tools in an outside directory or inside OpenCode (Claude Code) global configuration to be reused when needed?
**Answer:** Store project-specific files inside the project directory (e.g., `.claude/skills/`). Store global files in user home directory (e.g., `~/.claude/skills/`).

**References:**
- [Skills vs MCP tools for agents](https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what)
- [Awesome Agent Skills](https://github.com/skillmatic-ai/awesome-agent-skills)

### Is there a standard file to be used as a log for all changes and tasks done?
**Answer:** Use a standard changelog or a custom log file (e.g., `logs/ai_actions.md`). Automate logging with tools like `vercel activity` or a simple timestamped file.

**References:**
- [Vercel Changelog](https://vercel.com/changelog)
- [Automated Decision Logs](https://addyosmani.com/blog/automated-decision-logs/)

### Am I missing something else that is important?
**Answer:** Ensure you have context files, a working .gitignore, and a process for updating documentation as the project evolves. Use community resources (e.g., GitHub discussions, Anthropic docs) for best practices.

**References:**
- [Need for dedicated .claudeignore file](https://github.com/anthropics/claude-code/issues/1304)
- [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)

