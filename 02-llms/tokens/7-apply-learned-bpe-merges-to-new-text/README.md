# Apply learned BPE merges to new text

`llms.tokens.7` · Medium · code

Byte-pair encoding learns an ordered list of merges like `("l", "o") -> "lo"`. To encode a word, start from its characters and repeatedly apply the highest-priority merge (earliest in the list) that occurs anywhere in the current sequence, merging every occurrence of that pair (left to right, non-overlapping), until no merge applies. Implement `bpe_encode(word, merges)` where `merges` is a list of `[a, b]` pairs.

Example: with merges `[["l","o"], ["lo","w"], ["e","r"]]`, `bpe_encode("lower", merges)` returns `["low", "er"]`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-21 | 0.1 ms | 39.6 MB | after viewing solution |

_Synced by MyTokenFlow._
