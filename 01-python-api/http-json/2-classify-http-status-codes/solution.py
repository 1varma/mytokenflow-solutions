def classify(status):
    if 200 <= status < 300:
        kind = "success"
    elif 300 <= status < 400:
        kind = "redirect"
    elif 400 <= status < 500:
        kind = "client_error"
    elif 500 <= status < 600:
        kind = "server_error"
    else:
        kind = "unknown"
    retry = status in (408, 429) or (kind == "server_error" and status != 501)
    return {"ok": kind == "success", "kind": kind, "retry": retry}

