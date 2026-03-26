\# Vibe/Context Coding FAQ - Updated Best Practices (March 2026)

\## Prerequisites

Create a GitHub repo first and clone it locally before starting with OpenCode or Claude Code. This gives you control over the initial structure and avoids tool-generated repos that might lack customization.\[web:10\]\[web:7\]

Include OpenCode/Claude Code config directories (e.g., \`.opencode/\`, \`claude-config/\`) in \`.gitignore\` to prevent committing sensitive API keys or local paths.\[web:7\]\[web:8\]

As a solo developer, skip branches/PRs initially—just commit and push features directly to \`main\`. Use them later for collaboration or releases.\[web:10\]

\## Git/GitHub Workflow

Yes, upload preliminary project explanation files before starting OpenCode/Claude Code to prime the AI with context, reducing hallucinations in vibe coding.\[web:6\]\[web:2\]

Use 1-3 focused files: a main \`README.md\` (project overview, goals), \`PROJECT_BRIEF.md\` (features, stack), and \`CONTEXT_GUIDE.md\` (vibe, tone, examples). Keep each under 1000 words.\[web:6\]\[web:10\]

Decide on core stack upfront (e.g., React + Node for web) but let tools suggest refinements. Preliminary files should outline it.\[web:10\]

Name files clearly as above, place in repo root or \`/docs/\` folder (commit to GitHub, not .gitignore).\[web:6\]

\## Preparatory Work

Essential files: \`README.md\`, \`PROJECT_BRIEF.md\`, \`.gitignore\`, \`package.json\` (if applicable), and a \`CHANGELOG.md\` for logging changes/tasks.\[web:10\]\[file:1\]

Let OpenCode/Claude Code create project-specific skills/agents/MCPs/tools during coding for iteration; pre-create reusable global ones outside (e.g., in \`~/.opencode/tools/\`).\[web:9\]\[web:7\]

Store reusables in global configs for cross-project use. Project-specific go in repo \`/agents/\` or \`/tools/\`, committed.\[web:9\]

Use \`CHANGELOG.md\` as standard log: append dated entries for tasks, decisions, AI prompts used.\[web:10\]

Add a \`SECURITY.md\` for auth/vuln notes, and \`PROMPT_TEMPLATES.md\` for reusable vibe/context prompts.\[web:6\]\[web:2\]

\## Best Practices

\- Provide rich context upfront: project brief, examples, constraints to evolve "vibe coding" into "context engineering".\[web:6\]\[web:4\]  
\- Break tasks into steps: plan > generate > review > test, using OpenCode TUI for iteration in VS Code.\[web:7\]\[web:10\]  
\- Review AI changes manually; test locally before commit. Use local models in Claude Code via LM Studio/Ollama for privacy.\[web:8\]\[web:10\]  
\- Maintain consistency: reference existing code/files in prompts.\[web:11\]  
\- For OpenCode in VS Code: Use TUI for planning/patches, VS Code for editing.\[web:7\]  
\- For Claude Code local: Route via claude-code-router to Ollama/LM Studio with large-context models like Qwen Coder.\[web:8\]

\## Resources

\- OpenCode Docs: https://opencode.ai/docs (VS Code integration, TUI workflow)\[web:7\]  
\- Claude Code Setup: https://code.claude.com/docs/en/setup (Local routing guide)\[web:8\]  
\- Vibe/Context Coding Guide: https://inferencebysequoia.substack.com/p/vibe-coding-needs-context-engineering (Context engineering pillars)\[web:6\]  
\- Best Practices 2026: https://www.softr.io/blog/vibe-coding-best-practices \[web:10\]  
\- Reddit Vibecoding: https://www.reddit.com/r/vibecoding/ (Community tips, OpenCode vs Claude)\[web:9\]  
\- Context Engineering Video: https://www.youtube.com/watch?v=Egeuql3Lrzg \[web:4\]

Monitor: r/vibecoding, OpenCode GitHub (https://github.com/opencode), Claude Code updates via Anthropic blog.