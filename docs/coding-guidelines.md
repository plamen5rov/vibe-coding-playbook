# General Coding Guidelines (for future examples)

- Keep code samples copy-paste ready and runnable.
- Use 2-space indentation for JS/TS/JSON and 4 spaces for Python.
- Prefer descriptive names over clever abbreviations.
- Add comments only when the intent is not obvious.
- Always include basic error checks even in snippets.

## 5.1 Code Examples: Bad vs Good

```javascript
// ❌ Bad: clever but cryptic
const f = (x) => x.reduce((a, b) => a + b, 0);

// ✅ Good: explicit and beginner-friendly
function calculateTotal(numbers) {
  let sum = 0;
  for (const number of numbers) {
    sum += number;
  }
  return sum;
}
```

```python
# ❌ Bad: swallows errors
data = json.loads(raw)

# ✅ Good: guards against invalid input
try:
    data = json.loads(raw)
except json.JSONDecodeError as exc:
    raise ValueError("Invalid JSON payload") from exc
```
