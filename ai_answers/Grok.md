<!-- markdownlint-disable-file -->

\*\*UPDATED FAQ: Vibe/Context Coding with OpenCode (VS Code) and Claude Code (Local Models) – March 2026 Edition\*\*

This is the complete, up-to-date answer to every question in your original FAQ.md. All advice is based on the current (March 2026) official documentation and best practices for \*\*OpenCode\*\* (the open-source AI coding agent at opencode.ai) and \*\*Claude Code\*\* (Anthropic’s agentic coding harness at code.claude.com). Both tools are fully compatible with vibe/context coding workflows: you provide high-level context (“vibe”) via dedicated files, and the agent plans, explores, edits, tests, and commits autonomously.

Vibe/context coding works best when the AI has persistent, project-specific instructions instead of starting from zero every session. Both tools auto-load key files at startup.

\---

\### Git/GitHub

\*\*Should I create a GitHub repo first and then clone it locally, or let OpenCode/Claude Code create it for me?\*\*  
Create the GitHub repo first (empty, with a README or .gitignore), then \`git clone\` it locally. This is the recommended workflow for both tools in 2026.  
\- It gives you immediate remote backup and easy future collaboration.  
\- Both OpenCode and Claude Code can then \`git init\` (if needed), add remotes, commit, push, and even open PRs via the \`gh\` CLI.  
\- Letting the AI create the repo from scratch works but is less reliable for authentication and initial setup.  
\*\*Specifics\*\*: In VS Code with the OpenCode extension, run \`opencode\` in the cloned folder. For Claude Code (terminal or local models), the agent handles \`git\` commands natively once \`gh\` is installed.

\*\*Should I include the OpenCode/Claude Code config directory (or any other specific files) in the .gitignore file?\*\*  
\*\*No\*\* for project-specific configs — commit them.  
\- Project-level directories (\`.claude/\`, \`.opencode/\`, \`.agents/\`) contain your \`CLAUDE.md\`, \`SKILL.md\` files, custom agents, \`opencode.json\`, and \`settings.json\`. These are \*\*core context\*\* and should be version-controlled (they travel with the repo).  
\- Global configs (\`~/.claude/\`, \`~/.config/opencode/\`) stay out of the repo — add them to a global \`.gitignore\` or never commit them.  
\- Standard language \`.gitignore\` (via \`git ignore\` templates) is fine. OpenCode’s built-in tools respect your \`.gitignore\` by default for searches/edits.  
\*\*Tip\*\*: Use the OpenCode plugin \`opencode-ignore\` if you want extra \`.ignore\` rules for the AI without affecting Git.

\*\*As a solo developer, should I create branches/PRs, or just commit and push every new feature?\*\*  
Use \*\*feature branches + PRs\*\* even as a solo dev — it is now the 2026 best practice.  
\- Branch name convention (put this in \`CLAUDE.md\`): \`feature/xxx\` or \`task/yyy\`.  
\- Let the agent create the branch, implement, commit, push, and open a PR (\`gh pr create\`).  
\- Merge via PR (self-review) or \`gh pr merge\`. This gives you a clean history, easy rollbacks, and trains the AI on your workflow.  
\- Direct \`main\` commits are acceptable only for tiny hotfixes. Both tools handle branching/PRs excellently via \`gh\` CLI.

\---

\### Preparatory Work

\*\*Before even starting OpenCode/Claude Code, should I create and upload files that explain the project itself?\*\*  
\*\*Yes — this is the single most important step for vibe/context coding.\*\* Do it before the first session. Both tools read these files automatically on startup.

\*\*Should it be one file or more?\*\*  
Start with \*\*one primary file\*\* (\`CLAUDE.md\` or the cross-tool \`AGENTS.md\`), then add supporting files as needed.

\*\*What to include? How long should it be?\*\*  
Keep it \*\*concise (100–300 lines max)\*\* — Claude/OpenCode treat every line as context.  
\*\*Recommended structure\*\* (copy-paste this as a starter, then run \`/init\` to let the AI flesh it out):

\`\`\`markdown  
\# PROJECT VIBE / CONTEXT (CLAUDE.md or AGENTS.md)

\## Project Overview  
One-sentence goal + success metrics.

\## Tech Stack  
\- Language: ...  
\- Framework: ...  
\- Key libraries: ... (list exact versions where critical)  
\- Architecture: (monolith / monorepo / etc.)

\## Code Style & Conventions  
\- Naming, formatting, linting rules.  
\- Do’s / Don’ts (most valuable section — add examples of past mistakes).

\## Repository Structure  
High-level map (do not list every file).

\## Common Commands & Workflows  
\- Build, test, dev server, deploy.  
\- Testing strategy.

\## Rules for This Agent  
\- Always run tests after edits.  
\- Branch/PR naming.  
\- Security / performance guardrails.

\## References  
@README.md  
@package.json (or equivalent)  
\`\`\`

\*\*Decide the technical stack yourself or let the AI suggest?\*\*  
Decide the \*\*high-level stack\*\* yourself (it’s part of the vibe). Let the AI suggest concrete libraries, versions, or alternatives once it has read \`CLAUDE.md\`. Prompt: “Review the stack in CLAUDE.md and propose any improvements with trade-offs.”

\*\*If more than one preliminary file — what are they?\*\*  
\- \`AGENTS.md\` (root) — universal, works with OpenCode + Claude Code + Cursor etc. (many people now use this as the single source of truth and \`@AGENTS.md\` from \`CLAUDE.md\`).  
\- \`.claude/skills/&lt;name&gt;/SKILL.md\` or \`.opencode/skills/&lt;name&gt;/SKILL.md\` or \`.agents/skills/&lt;name&gt;/SKILL.md\` — reusable behaviors.  
\- \`.claude/agents/&lt;name&gt;.md\` — custom sub-agents.  
\- \`.claude/settings.json\` — hooks (auto-lint, tests, etc.).  
\- \`opencode.json\` (root or \`~/.config/opencode/\`) — permissions, model defaults.

\*\*How should I name these files?\*\*  
\- Primary context: \`CLAUDE.md\` (Claude Code native) or \`AGENTS.md\` (cross-tool standard).  
\- Skills: \`&lt;kebab-case-name&gt;/SKILL.md\` (must match directory name).  
\- Agents: \`&lt;descriptive-name&gt;.md\` inside \`.claude/agents/\` or \`.agents/agents/\`.

\*\*Should I create these files in a separate directory? How to name it? Commit to GitHub or .gitignore?\*\*  
\- \`CLAUDE.md\` / \`AGENTS.md\` → \*\*project root\*\*.  
\- Skills, agents, settings → hidden dirs: \`.claude/\`, \`.opencode/\`, or \`.agents/\` (auto-discovered by both tools).  
\*\*Commit everything project-specific to Git.\*\* These are not secrets — they are your “vibe” and improve over time. Global files stay outside the repo.

\---

\### Best Practices

\*\*What other files do I need for a vibe/context coding project?\*\*  
\- \`README.md\` (always)  
\- \`CLAUDE.md\` / \`AGENTS.md\` (mandatory)  
\- \`.claude/skills/\` or equivalent (as needed)  
\- \`.claude/settings.json\` (hooks)  
\- \`opencode.json\` (project-level permissions/models)  
\- Standard project files (\`.gitignore\`, \`LICENSE\`, etc.)

\*\*Should I create skills, agents, MCP and tools in advance — or let OpenCode/Claude Code create them during coding?\*\*  
Create \*\*project-specific\*\* ones in advance if you already know the domain (e.g., “api-conventions”, “tailwind-best-practices”). For everything else, let the agent create them on-the-fly — it is excellent at this in 2026.  
\*\*MCP servers\*\* (external tool integrations like Notion, databases, Figma): add via \`claude mcp add\` or OpenCode’s tool system only when the project actually needs them.

\*\*Should I create them in an outside directory or inside the global configuration to be re-used?\*\*  
\- \*\*Project-specific\*\* → inside the project (\`.claude/skills/\`, \`.agents/skills/\`).  
\- \*\*Reusable across projects\*\* → global (\`~/.claude/skills/\`, \`~/.config/opencode/skills/\`).  
Both tools load global + project skills automatically.

\*\*Is there a standard file to be used as a log for all changes and tasks done?\*\*  
No single “standard” log file.  
\- Use conventional \`CHANGELOG.md\` (let the agent maintain it).  
\- Many people add a \`TASKS.md\` or \`ROADMAP.md\` that the agent updates.  
\- The agent’s own session history + Git commit messages + PR descriptions are usually sufficient.  
\- Claude Code/OpenCode can generate release notes automatically via skills.

\*\*Am I missing something else that is important?\*\*  
\- Use the \*\*Plan → Explore → Implement\*\* workflow (built-in sub-agents).  
\- Always reference files with \`@filename\` syntax.  
\- Install \`gh\` CLI for seamless GitHub integration.  
\- Use \`/init\`, \`/skill\`, sub-agents, and hooks aggressively.  
\- Prune \`CLAUDE.md\` regularly — context bloat kills quality.  
\- For local models: both tools work perfectly via Ollama / LM Studio (Anthropic-compatible endpoint) in 2026.

\---

\### Resources (Correct URLs – March 2026)

\*\*Official Documentation\*\*  
\- OpenCode main docs: https://opencode.ai/docs/  
\- OpenCode Skills: https://opencode.ai/docs/skills/  
\- OpenCode Config & Permissions: https://opencode.ai/docs/config/ and https://opencode.ai/docs/permissions/  
\- Claude Code full docs: https://code.claude.com/docs/  
\- Claude Code Best Practices: https://code.claude.com/docs/en/best-practices  
\- Claude Code Skills: https://code.claude.com/docs/en/skills

\*\*GitHub\*\*  
\- OpenCode: https://github.com/opencode-ai/opencode

\*\*Communities & News\*\*  
\- Reddit: r/ClaudeCode and r/opencodeCLI  
\- For real-time updates: follow @opencode_ai and Anthropic’s Claude announcements on X, GitHub releases, and the OpenCode Discord (linked from opencode.ai).  
\- Vibe coding tutorials: Search YouTube for “vibe coding OpenCode 2026” or “Claude Code CLAUDE.md best practices”.

Save this file as \`FAQ.md\` (or \`VIBE-CONTEXT-FAQ.md\`) in every project — the agents will read it too!

Happy vibe/context coding. With a solid \`CLAUDE.md\`/\`AGENTS.md\` + skills, both OpenCode in VS Code and Claude Code (local or cloud) become dramatically more powerful. Let the agents do the heavy lifting.