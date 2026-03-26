<!-- markdownlint-disable-file -->

Here is a detailed FAQ response based on your questions, incorporating the latest best practices for vibe/context coding as of early 2026, with specifics for \*\*OpenCode\*\* (the VS Code extension) and \*\*Claude Code\*\* (the terminal-based agent).

\---

\# ANSWERS: VIBE/CONTEXT CODING FAQ

\## Prerequisites  
\*\*General:\*\* Vibe coding relies on giving the AI a rich context. Both OpenCode and Claude Code work best when you treat them as pair programmers who need a clear "brief" before touching code.

\*\*OpenCode (VS Code):\*\* Best for tight integration with your editor, file watching, and inline diffs.  
\*\*Claude Code (Terminal):\*\* Best for agentic workflows (it can run commands, search the web, create files autonomously). It requires a good setup in \`~/.claude/settings.json\`.

\---

\## Git/GitHub

\### Should I create a GitHub repo first or let the tool create it?  
\*\*General:\*\* Create the repo first on GitHub (empty, no README) and then clone it locally.  
\- \*\*Why:\*\* This gives you control over visibility (public/private), org access, and ensures your remote origin is set correctly before the AI starts generating code.  
\- \*\*OpenCode:\*\* Does not create remote repos. You must clone first.  
\- \*\*Claude Code:\*\* It \*can\* initialize a repo and push, but this often leads to commit message friction. \*\*Best practice:\*\* Clone manually, then run \`claude\` inside the directory.

\### Should I include the tool’s config directory in \`.gitignore\`?  
\*\*Yes, absolutely.\*\*  
Add these to your \`.gitignore\`:  
\`\`\`gitignore  
\# OpenCode (VS Code extension)  
.opencode/  
.opencoderc.json  
.opencode-rules/

\# Claude Code (Terminal)  
.claude/  
.claude.json  
.claudeignore

\# General  
.DS_Store  
node_modules/  
dist/  
.env  
\`\`\`  
\*\*Why:\*\* These files contain session history, tokens, and local preferences. Committing them creates merge conflicts and exposes system prompts. \*Never\* commit them.

\### Solo developer: Branches & PRs?  
\*\*Yes, use branches.\*\*  
Even as a solo dev, you should create a \`main\` branch (protected) and a \`dev\` branch.  
\- \*\*Workflow:\*\* Let Claude Code create a branch per feature (e.g., \`feature/add-auth\`) and commit there. Merge via CLI or GitHub UI.  
\- \*\*Why:\*\* It allows you to use \`git reset\` to undo AI mistakes without affecting \`main\`. It also creates a safety net: if the AI goes into a "vibe loop" and breaks everything, you can just delete the feature branch and start over.

\---

\## Preparatory Work

\### Before starting the tool, should I create project explanation files?  
\*\*Yes. This is the most critical step for vibe coding.\*\*

\### Should it be one file or more?  
\*\*Two files.\*\* One for the \*technical blueprint\* and one for the \*active context/log\*.

\### What to include and how long?  
1\. \*\*\`PROJECT.md\` (Blueprint)\*\*  
    - \*\*Length:\*\* 100-300 lines. Be specific.  
    - \*\*Content:\*\*  
        - \*\*Core Goal:\*\* One sentence.  
        - \*\*Tech Stack:\*\* \*You\* decide this. Do not let the AI choose unless you are prototyping. (e.g., "Next.js 15 App Router, Tailwind CSS, Prisma with PostgreSQL, shadcn/ui").  
        - \*\*Database Schema:\*\* Entity Relationship Diagram in text or Mermaid.  
        - \*\*Folder Structure:\*\* Enforce a structure (e.g., \`src/app\`, \`src/lib\`, \`src/components/ui\`).  
        - \*\*API Contracts:\*\* If applicable, define the endpoints.  
        - \*\*Styling Constraints:\*\* "Use Tailwind classes. No custom CSS files."

2\. \*\*\`CONTEXT.md\` (or \`AGENTS.md\`)\*\*  
    - \*\*Length:\*\* Dynamic.  
    - \*\*Content:\*\*  
        - \*\*Current Phase:\*\* "Implementing authentication."  
        - \*\*Recent Changes:\*\* A running log of what the AI just did.  
        - \*\*Next Tasks:\*\* A checklist for the current session.

\### Should I decide the tech stack or let the tool suggest?  
\*\*You decide.\*\* If you let Claude Code or OpenCode choose, they will pick what they are most comfortable with (often outdated or specific to their training data). If you have preferences for 2026 (e.g., \`bun\` instead of \`npm\`, \`shadcn/ui\`, \`Drizzle\` instead of Prisma), specify them in \`PROJECT.md\`. If you have no preferences, ask them to suggest, but review the suggestions before approving.

\### How should I name these files?  
\- \`PROJECT.md\` (or \`README.md\` but keep README for user documentation)  
\- \`CONTEXT.md\` (or \`AGENTS.md\` — this is a standard that many AI agents recognize)  
\- Place them in the \*\*root directory\*\*.

\### Should I commit these files?  
\*\*Commit \`PROJECT.md\`.\*\* Do \*\*not\*\* commit \`CONTEXT.md\` initially if it contains specific API keys or temporary session notes, but you can commit a template version. Generally, it’s safe to commit \`CONTEXT.md\` as it helps you track progress.

\---

\## Best Practices

\### What other files do I need?  
\- \*\*\`.claudeignore\` / \`.opencodeignore\`:\*\* Prevents the AI from reading sensitive files (like \`node_modules\`, \`.env\`, or your \`CONTEXT.md\` if you want it to stay out of the context window).  
\- \*\*\`rules/\` directory:\*\* OpenCode supports "rules" files (\`.opencode-rules\`). You can store persistent instructions here (e.g., "always use TypeScript strict mode").

\### Skills, Agents, MCP, Tools: Create in advance or let the AI create?  
\- \*\*For Generic Needs (MCP Servers):\*\* Set these up \*\*globally\*\* in advance.  
    - \*Example:\* Install the \*\*GitHub MCP server\*\* so Claude can read/write PRs, or the \*\*Filesystem MCP\*\*.  
    - For OpenCode, install extensions that act as MCP clients.  
\- \*\*For Project-Specific Logic (Skills/Agents):\*\* Let the AI create them \*\*during coding\*\*.  
    - \*Example:\* If you are building a React app, let Claude Code generate a "component-generator" skill when it realizes you are repeating the same pattern.

\### Where to store skills, agents, MCP?  
\- \*\*Global Configuration:\*\* Use \`~/.claude/settings.json\` for MCP servers you use across all projects (e.g., \`github.com\`, \`brave-search\`).  
\- \*\*Project Directory:\*\* Store project-specific skills and agents in \`.claude/skills/\` or \`.opencode/skills/\`. This allows you to version control the \*logic\* of how you want the AI to work for that specific codebase without polluting your global config.

\### Is there a standard log file?  
There is no universal standard, but \*\*\`CONTEXT.md\`\*\* has become the de facto standard for "vibe coding."  
\- \*\*Alternative:\*\* Use \`CLAUDE.md\` (Anthropic's suggested naming) or \`AGENTS.md\`.  
\- \*\*Content:\*\* Update it manually or via a script to log:  
    - \`\[2026-03-26 10:00\]\` - Implemented login flow.  
    - \`\[2026-03-26 11:30\]\` - Fixed Prisma migration error.

\### Am I missing something?  
\*\*Memory Management:\*\*  
The biggest pitfall in vibe coding is \*\*context overflow\*\*. After 2-3 hours of coding, the AI forgets the initial \`PROJECT.md\`.  
\- \*\*Fix:\*\* Periodically open a new session and feed it the current \`CONTEXT.md\` and \`PROJECT.md\`. Say: "Read these two files. This is our project. Resume from the last task."

\---

\## Resources

Here are the best online resources for staying current with vibe/context coding as of 2026.

\### Official Documentation  
1\. \*\*Claude Code (Anthropic)\*\*  
    - URL: \[https://docs.anthropic.com/en/docs/claude-code\](https://docs.anthropic.com/en/docs/claude-code)  
    - \*Note:\* Check for \`settings.json\` updates and MCP (Model Context Protocol) integration.

2\. \*\*OpenCode (VS Code Extension)\*\*  
    - URL: \[https://github.com/OpenCode/opencode\](https://github.com/OpenCode/opencode) (Check for the official docs link within the repo)  
    - \*Note:\* The landscape for VS Code AI extensions changes rapidly. Look for "OpenCode" specific release notes.

3\. \*\*Model Context Protocol (MCP)\*\*  
    - URL: \[https://modelcontextprotocol.io\](https://modelcontextprotocol.io)  
    - \*Note:\* Essential for understanding how to connect Claude Code to databases, GitHub, and local servers.

\### Community & News  
4\. \*\*r/ClaudeAI (Reddit)\*\*  
    - URL: \[https://www.reddit.com/r/ClaudeAI/\](https://www.reddit.com/r/ClaudeAI/)  
    - \*Filter:\* Look for "Claude Code" or "Vibe Coding" flairs.

5\. \*\*Anthropic News / Discord\*\*  
    - URL: \[https://www.anthropic.com/news\](https://www.anthropic.com/news)  
    - URL: \[https://discord.gg/anthropic\](https://discord.gg/anthropic) (Official Discord for real-time changes)

6\. \*\*GitHub MCP Servers List\*\*  
    - URL: \[https://github.com/modelcontextprotocol/servers\](https://github.com/modelcontextprotocol/servers)  
    - \*Why:\* The "servers" repo is where new MCP integrations are listed first. Check this weekly to see new tools (e.g., Puppeteer, Slack, etc.) you can give to Claude Code.

\### Learning & Patterns  
7\. \*\*Vibe Coding Patterns (Blogs)\*\*  
    - Follow \*\*Simon Willison\*\* (often blogs about LLM coding patterns) and \*\*Anthropic Engineering\*\* blog for deep dives on context management.

- \*Pro Tip:\*\* To monitor changes, set up a \*\*GitHub Watch\*\* on the \`modelcontextprotocol/servers\` and \`opencode/opencode\` repositories. Set it to "Releases only" to get notified when new features drop.