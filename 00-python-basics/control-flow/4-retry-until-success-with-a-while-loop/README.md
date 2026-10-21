# Retry until success with a while loop

`python-basics.control-flow.4` · Easy · code

`attempts` is a list of booleans: `attempts[i]` says whether call number `i` succeeds. Implement `calls_needed(attempts, max_calls)` that simulates calling until the first success, but never more than `max_calls` times. Return the number of calls made if one succeeded, or `-1` if none of the allowed calls did. Calls beyond the end of `attempts` fail.

Example: `calls_needed([False, False, True], 5)` returns `3`; `calls_needed([False, False, True], 2)` returns `-1`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-21 | 0.1 ms | 39.5 MB | after viewing solution |

_Synced by MyTokenFlow._
