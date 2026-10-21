# Deterministic train/test split by id

`python-api.files-json.8` · Medium · code

Implement `split(records, test_fraction)` that assigns each record (a dict with an `"id"`) to `"train"` or `"test"` deterministically: compute the SHA-256 of the id string, take the first 8 hex digits as an integer, divide by `16**8` to get a number in [0, 1), and put the record in test if that number is below `test_fraction`. Return `{"train": [...], "test": [...]}` keeping input order.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-21 | 0.2 ms | 39.5 MB | after viewing solution |

_Synced by MyTokenFlow._
