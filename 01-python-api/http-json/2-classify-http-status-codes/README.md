# Classify HTTP status codes

`python-api.http-json.2` · Easy · code

Implement `classify(status)` returning a dict `{"ok": bool, "kind": str, "retry": bool}` where kind is `"success"` (200-299), `"redirect"` (300-399), `"client_error"` (400-499) or `"server_error"` (500-599), and `"unknown"` otherwise. `ok` is True only for success. `retry` is True for 408, 429 and every 5xx except 501.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-21 | 0.1 ms | 39.6 MB | after viewing solution |

_Synced by MyTokenFlow._
