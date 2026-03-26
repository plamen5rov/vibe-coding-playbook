# Cost and Models

API costs add up fast if you're not paying attention. This section shows you how to manage costs while getting good results.

---

## How pricing works

### Cloud models (API-based)

Most models use token-based pricing:

| Component | What it is | Cost |
| --- | --- | --- |
| Input tokens | Your prompts, context files | $1-15 per million |
| Output tokens | Model responses | $3-75 per million |
| Context tokens | Files the model reads | Often free up to limit |

Prices vary by model. Claude 3.5 Sonnet is roughly $3/million input, $15/million output. GPT-4o is around $5/million input, $15/million output.

### Local models (Ollama, LM Studio)

- Free after initial hardware investment
- GPU required for decent performance
- Slower than cloud models
- Quality varies significantly by model

---

## Cost estimates for a vibe coding session

A typical session:

- **Prompt tokens:** ~5K (your instructions + context)
- **Context tokens:** ~50K (reading files, existing code)
- **Output tokens:** ~10K (code + explanations)

**Approximate cost for a 30-minute session:**

- Claude 3.5 Sonnet: $0.30-0.50
- GPT-4o: $0.40-0.70
- Claude 4 Opus: $1.00-2.00

**Monthly estimate (10 sessions/week):**

- Cloud: $15-40/month
- With local models: $0 (after GPU investment)

---

## Which model to use when

Not every task needs the most expensive model.

| Task | Recommended model |
| --- | --- |
| Planning, exploration | Cheap model (Haiku, GPT-3.5) |
| Writing simple code | Mid-tier (Sonnet, GPT-4o) |
| Complex architecture, debugging | Premium (Opus, GPT-4) |
| Writing tests | Mid-tier |
| Refactoring | Mid-tier |
| Reading and explaining code | Mid-tier |
| Debugging tricky issues | Premium |

**Pattern:** Use a cheap model to plan, then switch to a capable model to implement.

---

## OpenCode model options

### OpenCode Zen (recommended for beginners)

OpenCode maintains a curated list of models tested for agentic coding. Access via `/connect` → `OpenCode Zen`.

Benefits:

- No need to manage API keys
- Optimized for coding tasks
- Competitive pricing

### Bring your own model

In `opencode.json`:

```json
{
  "model": "anthropic/claude-sonnet-4-5",
  "provider": {
    "anthropic": {
      "apiKey": "$ANTHROPIC_API_KEY"
    }
  }
}
```

Or use OpenAI, Google, Cohere, or any OpenRouter-compatible provider.

### Local models (Ollama)

```json
{
  "model": "qwen2.5-coder:14b",
  "provider": {
    "ollama": {
      "url": "http://localhost:11434"
    }
  }
}
```

Set `numCtx: 32768` or higher — agentic coding needs large context.

---

## Claude Code model options

### Cloud models

Claude Code uses your API key or subscription:

- **API key:** Pay per use
- **Subscription:** Use existing ChatGPT Plus, GitHub Copilot, or GitLab Duo — zero additional cost

### Local models via Ollama

```bash
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_BASE_URL="http://localhost:11434"
claude --model qwen3-coder:latest
```

---

## Cost-saving strategies

### 1. Use context efficiently

Don't paste file contents. Use `@filename` references:

```text
❌ Bad: "Here's the file contents: [pastes 500 lines]"

✅ Good: "Read @src/auth/login.ts and fix the issue."
```

### 2. Clear context between tasks

Context you don't need costs money. Clear sessions when switching topics (section 04).

### 3. Use the right model for the task

Don't use Opus for something Haiku can do.

### 4. Set budget alerts

Most providers have usage dashboards. Check weekly.

### 5. Try local models for simple tasks

Ollama is free after setup. Use it for exploration, simple edits, file searching.

---

## Model recommendations by use case

### For beginners

Start with OpenCode Zen or Claude Sonnet. Good balance of capability and cost.

### For cost-conscious

Use local models (Ollama) with Qwen2.5-Coder or CodeLlama. Quality is decent for most tasks.

### For maximum capability

Claude 4 Opus or GPT-4. Use for complex architecture, debugging, or when the task is high-value.

### For speed

Use Haiku or GPT-3.5 for quick tasks where capability matters less than response time.

---

## When to upgrade

Signs you need a more capable model:

- The cheap model keeps making the same mistakes
- It can't follow complex instructions
- It produces code that doesn't compile

Signs you can downgrade:

- The task is straightforward (simple edits, file reading)
- You're getting consistent results with a cheaper model
- You're trying to reduce costs

---

## Quick reference

| Model tier | Examples | Best for |
| --- | --- | --- |
| Cheap | Haiku, GPT-3.5, Qwen2.5-Coder 7B | Planning, simple tasks |
| Mid-tier | Sonnet, GPT-4o, GPT-4o-mini | Most coding tasks |
| Premium | Opus, GPT-4 | Complex architecture, debugging |

**Rule of thumb:** Start with mid-tier. Upgrade when you hit limitations. Downgrade when the task is simple.
