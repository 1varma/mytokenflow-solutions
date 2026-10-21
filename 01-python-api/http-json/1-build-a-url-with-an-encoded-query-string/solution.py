from urllib.parse import urlencode

def build_url(base, path, params=None):
    url = base.rstrip("/") + "/" + path.lstrip("/")
    items = [(k, v) for k, v in (params or {}).items() if v is not None]
    if items:
        url += "?" + urlencode(items, doseq=True)
    return url
