# Fix the off-by-one in a batch counter

`python-basics.control-flow.5` · Easy · code

`num_batches(n_items, batch_size)` should return how many batches are needed to process `n_items` items when each batch holds at most `batch_size` items (`batch_size >= 1`). The starter code has a bug. Find and fix it.

Example: 10 items in batches of 4 need `3` batches; 8 items need `2`; 0 items need `0`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-21 | 0.0 ms | 39.5 MB | after viewing solution |

_Synced by MyTokenFlow._
