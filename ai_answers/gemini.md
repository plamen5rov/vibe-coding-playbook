<!-- markdownlint-disable-file -->

This guide provides expert advice on vibe and context coding using OpenCode (in VS Code) and Claude Code, based on current 2026 best practices.

# Vibe Coding FAQ: Expert Solutions (2026 Edition)

## 1\. Git & GitHub Workflow

- **Repo Initialization**: Always create your GitHub repo first and clone it locally. This ensures a clean origin and allows you to initialize specific AI configuration files (like `.cursorrules` or `CLAUDE.md`) immediately upon cloning.
    
- **Gitignore for AI Files**: You should generally **commit** your AI instruction files (`.cursorrules`, `CLAUDE.md`, `.clauderules`) to your repository so the AI has consistent context across different machines. However, **exclude** local configuration directories like `.claude/config` or `.opencode/` if they contain session-specific history or local paths.
    
- **Solo Developer Branching**: Even as a solo developer, use **feature branches**. This allows you to use "Plan Mode" in one branch while keeping your "Main" branch stable. It also prevents the AI from making sweeping, unrecoverable changes to your primary codebase.
    

## 2\. Preparatory Work & Project Context

- **Context Files**: Before starting, create a **single source of truth** file. For OpenCode/Cursor, use `.cursorrules` or `instructions.md`. For Claude Code, use `CLAUDE.md`.
    
- **What to Include**:
    
    - **Project Overview**: High-level goal of the app.
        
    - **Tech Stack**: Explicitly list frameworks (e.g., "Next.js 15, Tailwind, Supabase") to prevent the AI from suggesting incompatible libraries.
        
    - **Naming Conventions**: Your preference for exports (named vs. default) and file structure.
        
- **Technical Stack**: You should **decide the core stack** yourself based on your goals (e.g., Next.js for web, Flutter for mobile) but let the AI suggest specific helper libraries or implementation patterns.
    

## 3\. Best Practices for Vibe Coding

- **Vibe Coding Loop**: Describe the goal \$\\rightarrow\$ AI generates \$\\rightarrow\$ You test/observe \$\\rightarrow\$ Provide feedback.
    
- **Modular Skills & Agents**: Do not create all tools in advance. Let the AI generate specialized "Skills" (saved as `SKILL.md` in `.claude/skills/`) as the project evolves.
    
- **MCP (Model Context Protocol)**: Use MCP to connect your AI to live data (GitHub, Google Search, Databases). Store universal MCP servers in your global config and project-specific ones in your local `.clauderules`.
    
- **Logging Changes**: Maintain a `PROGRESS.md` or use the built-in `/history` and checkpoint features in Claude Code to track task completion and facilitate rollbacks.
    

## 4\. Recommended Resources (2026)

| **Resource** | **URL** | **Purpose** |
| --- | --- | --- |
| **Claude Code Docs** | [code.claude.com/docs](https://code.claude.com/docs) | Official best practices and CLI commands. |
| **OpenCode Guide** | [github.com/opencode/docs](https://www.google.com/search?q=https://github.com/opencode/docs) | Configuration for open-source LLM integration. |
| **MCP Servers** | [modelcontextprotocol.io](https://modelcontextprotocol.io/) | Catalog of tools for AI context expansion. |
| **Cursor Rules Hub** | [cursor.directory](https://cursor.directory/) | Community-shared `.cursorrules` for different stacks. |

## Important Security Note

**Never** let your AI read your `.env` files. Even if listed in `.gitignore`, some agents may still access them. Use explicit permission settings in your AI config to block access to secrets.