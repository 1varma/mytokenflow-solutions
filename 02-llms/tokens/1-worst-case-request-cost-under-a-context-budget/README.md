# Worst-case request cost under a context budget

`llms.tokens.1` · Easy · code

Token counts drive both what fits in the context window and the price. Implement `max_request_cost(context_window, prompt_tokens, max_output, price_in_per_m, price_out_per_m)`.

* The model may generate `budget = min(max_output, context_window - prompt_tokens)` tokens: the prompt and the output share the window.
* Return a dict `{"output_budget": budget, "max_cost": dollars}` where `dollars` is the cost if the model uses its whole budget. Prices are dollars per **million** tokens, input and output priced separately.
* If the prompt leaves no room for even one output token, raise `ValueError`.

Example: `max_request_cost(8000, 7500, 1024, 3.0, 15.0)` returns `{"output_budget": 500, "max_cost": 0.03}` because `(7500 * 3 + 500 * 15) / 1_000_000 = 0.03`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-21 | 0.1 ms | 39.6 MB | after viewing solution |

_Synced by MyTokenFlow._
