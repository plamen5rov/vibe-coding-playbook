# Markdownlint Setup and Commands

## 3.1 Markdownlint Setup

```bash
npm install -g markdownlint-cli2

cat > .markdownlint.json <<'EOF'
{
  "default": true,
  "MD013": false,
  "MD033": false,
  "MD041": false
}
EOF
```

- `MD013` (line length) is off to keep snippets readable.
- `MD033` (inline HTML) is off for future embeds.
- `MD041` is off so files can start with comments or metadata.

## 3.2 Linting Commands

```bash
# Lint every Markdown file
markdownlint-cli2 '**/*.md' '!**/node_modules/**/*.md'

# Auto-fix what can be fixed safely
markdownlint-cli2 --fix '**/*.md' '!**/node_modules/**/*.md'

# Lint a single file when iterating
markdownlint-cli2 docs/CONVENTIONS.md
```

- Run linting before and after substantial edits.
- When a rule cannot be satisfied, explain why in your summary.
