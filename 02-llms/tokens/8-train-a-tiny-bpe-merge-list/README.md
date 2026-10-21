# Train a tiny BPE merge list

`llms.tokens.8` · Hard · code

Implement `bpe_train(text, num_merges)` for a toy tokenizer.

* Split `text` on whitespace into words; every word starts as a tuple of its characters (no end-of-word marker).
* Each round, count every adjacent pair of symbols inside words, weighting by how many times the word occurs. Overlapping positions all count (in `"aaa"` the pair `("a","a")` counts twice).
* Pick the pair with the highest count; break ties by the lexicographically smallest pair tuple.
* Merge that pair into one symbol everywhere, scanning each word left to right without overlap (`"aaa"` becomes `["aa","a"]`).
* Return the list of merged pairs in order, each as a `(left, right)` tuple (a 2-item list is judged the same). Stop early if no adjacent pairs remain.

Example: `bpe_train("low low low lower", 3)` returns `[("l","o"), ("lo","w"), ("e","r")]`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-21 | 0.2 ms | 39.6 MB | after viewing solution |

_Synced by MyTokenFlow._
