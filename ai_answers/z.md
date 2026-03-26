<!-- markdownlint-disable-file -->

Here is a comprehensive guide tailored to the latest practices in Vibe/Context Coding, specifically addressing your questions regarding OpenCode, Claude Code, and the agentic workflow.

\`\`\`markdown  
\# THE DEFINITIVE GUIDE TO VIBE/CONTEXT CODING  
\### Updated for 2025 Standards | OpenCode & Claude Code Edition

This document provides a curated FAQ based on the latest "Agentic" coding workflows. The philosophy here is \*\*Context is King\*\*. The goal is to reduce hallucination and friction by providing the AI with a rich, structured environment before you even write the first prompt.

\---

\## 1. GIT & GITHUB

\### Should I create a Github repo first or let the AI create it?  
\*\*Advice:\*\* \*\*Create it yourself first.\*\*  
While tools like Claude Code and OpenCode are capable of initializing git repos, the "Vibe Coding" workflow thrives on stability.  
\- \*\*The Problem:\*\* If an agent initializes the repo, it might miss setting the correct upstream branch, remote origin, or specific \`.gitignore\` templates (like Node, Python, Rust).  
\- \*\*The Solution:\*\*  
  1. Create the repo on GitHub (with README and .gitignore).  
  2. Clone it locally.  
  3. Initialize your AI tools \*inside\* that directory.  
  This ensures the remote is set, the initial commit is clean, and the agent understands it is working in a tracked environment immediately.

\### Should I include OpenCode/Claude Code config directories in .gitignore?  
\*\*Advice:\*\* \*\*Generally, NO (Commit them).\*\*  
In the modern "Context Coding" era, configuration is part of the source code.  
\- \*\*Commit these:\*\* \`.claude/\`, \`.opencode/\`, \`.cursorrules\`, \`CLAUDE.md\`.  
  - \*Why?\* If you switch machines or work with other humans/AIs, the "vibe" (rules, memory, context) travels with the code. Claude Code specifically uses local files to remember project instructions.  
\- \*\*Ignore these:\*\* Any config files containing API keys. However, modern tools usually read keys from environment variables (\`.env\`), which \*must\* be in \`.gitignore\`.  
\- \*\*Specifics for Claude Code:\*\* It creates a \`CLAUDE.md\` (or \`.claude/\` directory) in the root. Commit this. It is your project's "brain".

\### As a solo developer, should I create branches/PRs?  
\*\*Advice:\*\* \*\*Yes, but use "Atomic Branching".\*\*  
Working on \`main\` is tempting for speed, but AI agents can generate massive amounts of code. If the agent hallucinates a feature that breaks your app, reverting a \`main\` branch commit is messy.  
\- \*\*The Strategy:\*\*  
  - Work on \`feature/your-feature-name\`.  
  - Let the AI commit aggressively (AI loves to commit).  
  - Test the feature.  
  - Merge to \`main\`.  
\- \*\*Pro-Tip:\*\* Claude Code and OpenCode excel at writing conventional commit messages. Let them handle the choreography of commits, but you handle the merge.

\---

\## 2. PREPARATORY WORK (The "Context" in Context Coding)

\### Before starting, should I create files to explain the project?  
\*\*Advice:\*\* \*\*Absolutely. This is the most critical step.\*\*  
Do not start with a blank slate. The AI needs a "Memory Anchor".

\### Should it be one file or more?  
\*\*Advice:\*\* \*\*Two specific files are the gold standard.\*\*  
1\. \*\*\`README.md\`\*\*: The human-readable overview.  
2\. \*\*\`CLAUDE.md\` (or \`AGENTS.md\`)\*\*: The machine-readable "System Prompt". (Claude Code automatically looks for \`CLAUDE.md\` in the root).

\### What to include in this file? How long should it be?  
\*\*Advice:\*\* \*\*Structure over length.\*\*  
It shouldn't be a novel, but it must be dense.

\*\*Template for \`CLAUDE.md\`:\*\*  
\`\`\`markdown  
\# PROJECT CONTEXT  
\## Tech Stack  
\- Frontend: React + Vite + TailwindCSS  
\- Backend: Supabase (Postgres)  
\- Language: TypeScript (Strict mode)

\## Architecture  
\- Feature-based folder structure (src/features/...)  
\- Services layer for API calls

\## Coding Conventions  
\- Use functional components.  
\- Use Lucide React for icons.  
\- Never hardcode colors; use Tailwind classes.  
\- Run \`npm run lint\` before committing.

\## Current Goal  
\- Implementing the User Authentication flow.  
\`\`\`

\### Should I decide the tech stack or let the AI suggest it?  
\*\*Advice:\*\* \*\*You decide the stack; the AI executes it.\*\*  
If you let the AI decide, it might choose a stack it is comfortable with (often outdated or generic). If you mandate the stack (e.g., "Use SvelteKit and Supabase"), the AI acts as an expert in \*your\* chosen domain, reducing conflicts.

\### How should I name this file/s?  
\- \*\*Claude Code:\*\* \`CLAUDE.md\` (Root directory).  
\- \*\*General:\*\* \`AGENTS.md\` or \`.context.md\`.  
\- \*\*OpenCode:\*\* Check if it supports a specific instruction file. If unsure, \`README.md\` is the default fallback for most agents.

\### Should I commit these files?  
\*\*Advice:\*\* \*\*Yes.\*\* These are your source of truth. If you don't commit them, you lose the "Vibe" when you clone the repo elsewhere.

\---

\## 3. BEST PRACTICES

\### What other files do I need?  
\*\*Advice:\*\* Create a standardized environment for the AI.  
1\. \*\*\`.editorconfig\`\*\*: Forces consistent formatting (tabs/spaces). This stops the AI from fighting your linting rules.  
2\. \*\*\`package.json\` (or equivalent)\*\*: Lock your dependencies early. If you don't, the AI might try to install conflicting versions.  
3\. \*\*\`TASKS.md\` (Optional but recommended)\*\*: A file where the AI logs what it has done and what is pending.

\### Should I create skills, agents, MCP, and tools in advance?  
\*\*Advice:\*\* \*\*Setup MCP in advance; let Agents emerge naturally.\*\*  
\- \*\*MCP (Model Context Protocol):\*\* This is the new standard for giving AI access to tools (like filesystems, databases, web search). Configure your \`mcp_config.json\` \*before\* coding so the AI can read your database schema or browse documentation.  
\- \*\*Agents/Skills:\*\* Do not hardcode complex "skills" upfront. In tools like Claude Code, the "Agent" is the model itself. Use "Custom Instructions" (in \`CLAUDE.md\`) instead of creating rigid agent definitions.

\### Should I create tools in an outside directory (global) or inside the project?  
\*\*Advice:\*\* \*\*Project-local for code, Global for data.\*\*  
\- \*\*Local:\*\* Project-specific scripts (e.g., a script to seed the database). Commit these to the repo.  
\- \*\*Global:\*\* Connections to things like your Linear account, specific web search tools, or general utility scripts.  
\- \*\*Reasoning:\*\* Vibe coding relies on the project being self-contained. If you clone the repo on a new machine, it should work without copying global config files.

\### Is there a standard file to be used as a log?  
\*\*Advice:\*\* \*\*Yes, \`CHANGELOG.md\` or \`TASKS.md\`.\*\*  
Instruct the AI (via \`CLAUDE.md\`) to update a \`CHANGELOG.md\` after every significant feature.  
\*Prompt:\* "After completing a feature, append a summary to CHANGELOG.md following Keep a Changelog format."

\### Am I missing something important?  
\*\*Advice:\*\* \*\*You are missing the "Verification Loop".\*\*  
AI generates code, but it often fails to run it correctly the first time.  
\- \*\*Setup:\*\* Ensure you have a \`package.json\` script or a \`Makefile\` command (e.g., \`npm run check\`) that lints, builds, and tests.  
\- \*\*Instruction:\*\* Tell the AI: "Always run \`npm run check\` after writing code. If it fails, fix the errors and repeat."

\---

\## 4. RESOURCES

\### Best Online Resources (Correct URLs)

\*\*Official Documentation & Tools:\*\*  
\* \*\*Claude Code (Official Anthropic CLI):\*\*  
    \* \[Claude Code Docs\](https://docs.anthropic.com/en/docs/claude-code) - \*The primary source for the \`claude\` CLI tool.\*  
    \* \[Anthropic Prompt Engineering Guide\](https://docs.anthropic.com/en/docs/prompt-engineering)  
\* \*\*Model Context Protocol (MCP):\*\*  
    \* \[ModelContextProtocol.io\](https://modelcontextprotocol.io/) - \*The standard for connecting AI agents to data.\*  
    \* \[MCP Server Directory\](https://github.com/modelcontextprotocol/servers) - \*Pre-built tools for filesystem, github, postgres, etc.\*

\*\*Community & News:\*\*  
\* \*\*r/ClaudeAI (Reddit):\*\* Active community discussing Claude Code workflows.  
    \* \[r/ClaudeAI\](https://www.reddit.com/r/ClaudeAI/)  
\* \*\*Hacker News:\*\* Search for "LLM Coding Agents" or "MCP" for cutting-edge discussions.  
\* \*\*OpenCode (Open Source Initiative):\*\*  
    \* If you are using the open-source \*\*OpenCode\*\* interpreter or similar agent: \[OpenCode GitHub Topic\](https://github.com/topics/opencode) (Verify the specific repo you are using, as "OpenCode" is a common name. For example, \`opencode-ai\` or \`opencodeinterpreter\`).

\*\*News Monitoring:\*\*  
\* Monitor the \*\*Anthropic Changelog\*\* or their Developer Discord for updates on Claude Code features (like new MCP support).  
\`\`\`