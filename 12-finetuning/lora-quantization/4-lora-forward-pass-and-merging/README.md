# LoRA forward pass and merging

`finetuning.lora-quantization.4` · Hard · code

Implement `lora_forward(x, W, A, B, alpha, r)`:

* `x` is n x d_in, `W` is d_out x d_in, `A` is r x d_in, `B` is d_out x r (lists of lists).
* Adapter output: `y = x @ W.T + (alpha / r) * (x @ A.T) @ B.T`.
* Merged weight: `W_merged = W + (alpha / r) * B @ A`; `y_merged = x @ W_merged.T`.

Return `{"y": y rounded to 6, "merged": W_merged rounded to 6, "max_diff": max |y - y_merged| as a float}`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-15 | 0.3 ms | 39.4 MB | after viewing solution |

_Synced by MyTokenFlow._
