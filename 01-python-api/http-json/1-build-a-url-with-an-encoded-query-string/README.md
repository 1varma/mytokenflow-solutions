# Build a URL with an encoded query string

`python-api.http-json.1` · Easy · code

Implement `build_url(base, path, params=None)` that returns a full URL string.

* Join `base` and `path` with exactly one `/` between them, whatever slashes either one already has.
* Append `?` and the query string only when at least one parameter remains. Parameters whose value is `None` are dropped.
* Percent-encode keys and values (spaces become `+`, as `urllib.parse.urlencode` does) and keep the dict order.
* A list value produces one `key=value` pair per element, in order.

```python
build_url("https://api.example.com/", "/v1/items", {"q": "a b&c", "limit": 10})
# "https://api.example.com/v1/items?q=a+b%26c&limit=10"
```

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-21 | 0.1 ms | 39.6 MB | after viewing solution |

_Synced by MyTokenFlow._
