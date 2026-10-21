# Final project: build a fine-tuning dataset

`finetuning.mini-project.3` · Hard · code

**Final project.** Raw support logs (`{"prompt", "completion", "customer"}`) become train and test JSONL files. Implement `build_dataset(rows, system, test_frac, seed=0)` (the starter gives you `to_line` and `EMAIL`):

1. **Clean**, in row order, with the first matching reason: strip both texts; `"empty"` if either is empty; `"pii"` if either contains an email; `"duplicate"` if the normalised prompt (lowercase, whitespace collapsed) was already kept. Count drops per reason.
2. **Split by customer** among the kept rows: `keys = sorted(set(customers))`, shuffle with `random.Random(seed)`, then move whole customers into test until test rows `>= test_frac * kept rows`.
3. **Emit** `to_line(system, prompt, completion)` for each kept row, preserving row order within train and within test.

Return `{"train": [...], "test": [...], "report": {"kept", "dropped": {"empty", "pii", "duplicate"}, "train_rows", "test_rows", "test_customers": sorted list}}`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-15 | 0.3 ms | 39.4 MB | after viewing solution |

_Synced by MyTokenFlow._
