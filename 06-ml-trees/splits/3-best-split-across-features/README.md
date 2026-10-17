# Best split across features

`ml-trees.splits.3` · Medium · code

Implement `best_split(X, y)` that searches every feature and every candidate threshold (midpoints of distinct sorted values), scoring by weighted child Gini. Return `[feature, threshold, score]` (threshold and score rounded to 4) for the best split, preferring the lower feature index, then the smaller threshold on ties. If no feature can split, return `[None, None, gini(y)]`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-17 | 0.9 ms | 39.5 MB | after viewing solution |

_Synced by MyTokenFlow._
