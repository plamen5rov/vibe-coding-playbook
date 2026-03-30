# Conventions

## Writing Style

- Short, direct sentences
- No fluff
- Practical examples only

## File Naming

- UPPERCASE for system files (TASKS.md, RULES.md)
- kebab-case for folders

## Structure Rules

- One idea per file
- Keep files under ~300 lines

## AI Interaction Rules

- Always give explicit instructions
- Never use vague prompts
- Prefer step-by-step tasks

## Code Philosophy

- Simple > clever
- Explicit > abstract
- Small changes > big rewrites

## New Section Checklist

When adding a new section to the guide, follow this checklist:

### Required structure

Every section file in `sections/` must follow this pattern:

```markdown
# Section Title

![Header](../pictures/NN-section-name.png)

<One-sentence intro paragraph.>

---

## Content sections...

---

← [Previous: Previous Title](NN-previous.md) | [Next: Next Title →](NN+1-next.md)
```

### Header image

- Generate via `pictures/generate_headers.py` — same size, colors, and style
- Save as `pictures/NN-section-name.png`
- Do **not** change `pictures/README.png`

### Navigation

- Last line must be a `← Previous | Next →` footer
- If the section is now the last one, link `Next` to `[Back to README →](../README.md)`
- Update the **previous** section's footer to point forward to the new section

### README.md

- Add an entry in the `## Guide` section with: link, emoji, one-line description
- Do **not** change the README header image (`pictures/README.png`)

### TASKS.md

- Add the new section to the `## ✅ Done` list

### Tone

- Short, direct sentences — no "you might consider" or "it's important to note"
- No inline citations (e.g., `[code.claude]`) — this is a guide, not an academic paper
- No condescending "beginner/newbie" framing — address the reader directly

### Validation

- Run `markdownlint-cli2 '**/*.md' '!**/node_modules/**/*.md'` before and after
