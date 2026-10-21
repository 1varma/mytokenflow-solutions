# Mask an API key for logs

`python-basics.strings.4` · Easy · code

Never log a full secret. Implement `mask_key(key)` that keeps the first 3 and last 4 characters and replaces everything in between with `...`. Keys of 10 characters or fewer are fully hidden as `"***"`.

Example: `mask_key("sk-abc123456789xyz")` returns `"sk-...9xyz"`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-21 | 0.0 ms | 39.5 MB | after viewing solution |

_Synced by MyTokenFlow._
