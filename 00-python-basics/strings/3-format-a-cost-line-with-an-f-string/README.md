# Format a cost line with an f-string

`python-basics.strings.3` · Easy · code

Implement `cost_line(model, tokens, price_per_1k)` that returns a string like `"gpt-mini: 1,500 tokens = $0.0030"`: the model name, the token count with thousands separators, and the cost (`tokens / 1000 * price_per_1k`) with exactly 4 decimal places.

Example: `cost_line("gpt-mini", 1500, 0.002)` returns `"gpt-mini: 1,500 tokens = $0.0030"`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-21 | 0.0 ms | 39.5 MB | after viewing solution |

_Synced by MyTokenFlow._
