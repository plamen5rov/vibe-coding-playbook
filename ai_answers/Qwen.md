\# Comprehensive Guide to Vibe/Context Coding with Claude Code & VS Code AI

\## Introduction  
\*\*Vibe Coding\*\* (or Context Coding) is a development methodology where the developer focuses on high-level intent, architecture, and review, while AI agents handle the implementation details. Success depends heavily on \*\*context management\*\*—ensuring the AI understands your project goals, constraints, and standards without constant hand-holding.

This guide answers your FAQ based on the latest workflows (early 2025 standards), specifically tailored for \*\*Claude Code\*\* (Anthropic's CLI) and \*\*VS Code AI Extensions\*\* (such as \*\*Continue.dev\*\* for local/open models, as "OpenCode" is primarily a CLI tool by SST, though the principles apply universally).

\---

\## 1. Git/GitHub Strategy

\### Should I create a GitHub repo first, or let the AI create it?  
\*\*Advice:\*\* \*\*Create the GitHub repo first.\*\*  
\* \*\*Why:\*\* AI coding agents (Claude Code, OpenCode, Continue) rely heavily on Git history to understand context and revert changes. Initializing the repo yourself ensures you control the license, visibility, and initial \`.gitignore\`.  
\* \*\*Workflow:\*\*  
    1. Create repo on GitHub.  
    2. Clone locally.  
    3. Initialize your context files (see Section 2).  
    4. Let the AI start coding within that structure.

\### Should I include AI config directories in \`.gitignore\`?  
\*\*Advice:\*\* \*\*It depends on the file type.\*\*  
\* \*\*Ignore:\*\* Secret keys, local logs, and temporary agent scratchpads.  
\* \*\*Commit:\*\* Configuration files that define \*how\* the AI behaves (e.g., \`CLAUDE.md\`, \`.cursorrules\`, \`continue.config.json\`). These are part of your project's "source of truth."  
\* \*\*Specifics:\*\*  
    \* \*\*Claude Code:\*\* Commit \`CLAUDE.md\` (root). Ignore \`.claude/\` if it contains local session logs.  
    \* \*\*Continue.dev (VS Code):\*\* Commit \`.continue/config.json\` if it contains project-specific model rules. Ignore \`.continue/sessions/\`.  
    \* \*\*OpenCode (SST):\*\* Commit \`opencode.config.json\` if used for project rules.

\### As a solo developer, should I use branches/PRs or just commit to main?  
\*\*Advice:\*\* \*\*Use Feature Branches, even as a solo dev.\*\*  
\* \*\*Why:\*\* AI agents can be overly confident and introduce breaking changes. Branches allow you to isolate AI experiments.  
\* \*\*Workflow:\*\*  
    1. \`git checkout -b feature/ai-login-system\`  
    2. Let Claude Code/OpenCode work on the branch.  
    3. Review the code manually.  
    4. Merge to \`main\` only after tests pass.  
\* \*\*PRs:\*\* Create a Pull Request to yourself. It forces a "review mode" where you read the AI's diff before merging. This is critical for maintaining code quality in vibe coding.

\---

\## 2. Preparatory Work (Context Files)

\### Should I create files to explain the project before starting?  
\*\*Advice:\*\* \*\*Yes, this is the most critical step.\*\*  
AI models are only as good as the context you provide. Without this, you get generic code. With it, you get "vibe coding."

\### Should it be one file or more?  
\*\*Advice:\*\* \*\*Modular is better.\*\*  
Start with one master file, but split as the project grows.  
\* \*\*Small Project:\*\* Single \`CLAUDE.md\` or \`PROJECT_CONTEXT.md\` in the root.  
\* \*\*Large Project:\*\* Create a \`.ai/\` or \`docs/ai/\` directory.  
    \* \`docs/ai/overview.md\` (Goal & Vision)  
    \* \`docs/ai/tech-stack.md\` (Languages, Libraries)  
    \* \`docs/ai/coding-standards.md\` (Linting, Naming conventions)

\### What to include and how long should it be?  
\*\*Advice:\*\* \*\*Be concise but specific.\*\*  
\* \*\*Length:\*\* 1–3 pages max per file. AI context windows are large, but clarity matters more than volume.  
\* \*\*Include:\*\*  
    \* \*\*Project Goal:\*\* One sentence summary.  
    \* \*\*Tech Stack:\*\* Specific versions (e.g., "Python 3.11", "React 18", "Tailwind CSS").  
    \* \*\*Constraints:\*\* "No class-based components," "Use async/await," "Mobile-first design."  
    \* \*\*Directory Structure:\*\* Expected layout.  
    \* \*\*Testing:\*\* "Write Jest tests for every new function."

\### Should I decide the tech stack or let the AI suggest?  
\*\*Advice:\*\* \*\*Hybrid Approach.\*\*  
\* \*\*You Decide:\*\* Core framework (e.g., "We are using Next.js").  
\* \*\*AI Suggest:\*\* Libraries and implementation details (e.g., "Which state management library fits best?").  
\* \*\*Why:\*\* Changing the core stack mid-project is expensive. Lock the foundation, let the AI optimize the bricks.

\### Naming and Directory Structure for Context Files  
\*\*Advice:\*\* \*\*Follow emerging standards.\*\*  
\* \*\*Claude Code:\*\* Use \`CLAUDE.md\` in the root directory. This is automatically picked up by the CLI.  
\* \*\*VS Code (Continue/Cursor):\*\* Use \`.cursorrules\` (if using Cursor) or \`.continue/rules.md\`.  
\* \*\*General:\*\* \`README_AI.md\` or \`.ai/INSTRUCTIONS.md\`.  
\* \*\*Commit?\*\* \*\*Yes.\*\* These files must be versioned so the AI context evolves with the code.

\---

\## 3. Best Practices

\### What other files do I need for a vibe/context coding project?  
\*\*Advice:\*\* \*\*Standardize your AI interaction.\*\*  
1\. \*\*\`CLAUDE.md\`\*\*: (For Claude Code) Project-specific instructions.  
2\. \*\*\`.env.example\`\*\*: Never commit secrets, but show the AI what env vars are expected.  
3\. \*\*\`TODO.md\` or \`AI_TASKS.md\`\*\*: A living document where you list high-level tasks for the AI to pick up.  
4\. \*\*\`ARCHITECTURE.md\`\*\*: Diagrams or text explaining how components interact.

\### Should I create skills, agents, MCP, and tools in advance?  
\*\*Advice:\*\* \*\*Leverage MCP (Model Context Protocol).\*\*  
\* \*\*MCP:\*\* This is the new standard (2025) for connecting AI to tools.  
    \* \*\*Global:\*\* Install common MCP servers globally (e.g., Filesystem, GitHub, Postgres) in your AI client's global config.  
    \* \*\*Project-Specific:\*\* Define custom MCP tools in the project repo if they are unique to this business logic.  
\* \*\*Agents/Skills:\*\* Do not over-engineer this initially. Let Claude Code/OpenCode use its built-in reasoning. Only create custom "skills" (prompts/templates) if you find yourself repeating the same instruction 10+ times.  
\* \*\*Directory:\*\* Store custom MCP configurations in \`.mcp/\` or within the AI config directory.

\### Is there a standard file for logging changes and tasks?  
\*\*Advice:\*\* \*\*Use a hybrid approach.\*\*  
\* \*\*Git Commits:\*\* Let the AI write commit messages. Enforce a standard (e.g., Conventional Commits).  
\* \*\*\`CHANGELOG.md\`\*\*: Have the AI update this for significant version changes.  
\* \*\*\`AI_SESSION_LOG.md\`\*\*: (Optional) For complex debugging sessions, ask the AI to summarize what was tried and failed in a temporary log file, then delete it when resolved.

\### Am I missing something else important?  
\*\*Advice:\*\* \*\*Security and Testing.\*\*  
\* \*\*Security:\*\* Never paste API keys into chat. Use \`.env\` files. Add a rule in \`CLAUDE.md\`: "NEVER commit secrets or .env files."  
\* \*\*Testing:\*\* Vibe coding can generate code that looks right but fails edge cases. Mandate: "No feature is complete without passing tests."  
\* \*\*Human Review:\*\* You are the Pilot, AI is the Copilot. Never push to production without reading the diff.

\---

\## 4. Resources & Monitoring

\### Best Online Resources for Vibe/Context Coding  
Here are the authoritative sources for the tools and methodologies mentioned:

| Topic | Resource Name | URL | Description |  
| :--- | :--- | :--- | :--- |  
| \*\*Claude Code\*\* | Anthropic Claude Code Docs | \`https://docs.anthropic.com/claude-code\` | Official documentation for the CLI tool. |  
| \*\*OpenCode\*\* | SST OpenCode | \`https://opencode.ai/\` | Open-source alternative CLI agent (by SST). |  
| \*\*VS Code AI\*\* | Continue.dev | \`https://continue.dev/\` | Leading open-source AI extension for VS Code (supports local models). |  
| \*\*Protocol\*\* | Model Context Protocol (MCP) | \`https://modelcontextprotocol.io/\` | Standard for connecting AI to data/tools. |  
| \*\*Methodology\*\* | "Vibe Coding" Concept | \`https://twitter.com/karpathy\` (Search "Vibe Coding") | Andrej Karpathy's original posts on the methodology. |  
| \*\*Prompts\*\* | Awesome AI Agents | \`https://github.com/awesome-ai-agents\` | Community resources for agent configurations. |

\### How to Monitor News and Changes  
The AI coding landscape changes weekly. To stay updated:  
1\. \*\*Twitter/X:\*\* Follow \*\*@karpathy\*\*, \*\*@anthropic\*\*, and \*\*@sst_dev\*\*.  
2\. \*\*Newsletters:\*\* Subscribe to \*\*The Batch (DeepLearning.AI)\*\* or \*\*Import AI\*\*.  
3\. \*\*GitHub Trends:\*\* Watch the \*\*\`awesome-ai-agents\`\*\* repository for new tools.  
4\. \*\*Discord:\*\* Join the \*\*Continue.dev\*\* and \*\*Anthropic\*\* Discords for real-time troubleshooting.

\---

\## Summary Checklist for Starting Your Project

1\. \[ \] \*\*Initialize Git:\*\* \`git init\`, create GitHub repo, push initial commit.  
2\. \[ \] \*\*Create Context:\*\* Add \`CLAUDE.md\` (root) with stack, goals, and constraints.  
3\. \[ \] \*\*Configure AI:\*\* Set up Continue.dev (VS Code) or Claude Code (CLI) to read your context files.  
4\. \[ \] \*\*Setup MCP:\*\* Install necessary MCP servers (Filesystem, Git) globally.  
5\. \[ \] \*\*Define Workflow:\*\* Create a \`TASKS.md\` for the AI to pick up work.  
6\. \[ \] \*\*Safety:\*\* Add \`.env\` to \`.gitignore\` and instruct AI never to commit secrets.  
7\. \[ \] \*\*Branching:\*\* Create a \`dev\` or \`feature\` branch before asking AI to code.

\*Happy Vibe Coding!\*