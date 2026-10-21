# Fill a prompt template

`python-basics.strings.7` · Medium · code

Implement `render(template, values)` for a tiny template language: every `{name}` in `template` is replaced by `str(values[name])`. If a placeholder's name is missing from `values`, raise `KeyError` with the missing name. Text without braces is copied as is. Placeholder names contain only letters, digits and underscores.

Example: `render("Summarise {doc} in {n} words", {"doc": "the report", "n": 20})` returns `"Summarise the report in 20 words"`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-21 | 0.0 ms | 39.5 MB | after viewing solution |

_Synced by MyTokenFlow._
