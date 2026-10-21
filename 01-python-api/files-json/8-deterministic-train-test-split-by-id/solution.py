import hashlib

def bucket(id_):
    h = hashlib.sha256(str(id_).encode("utf-8")).hexdigest()
    return int(h[:8], 16) / 16 ** 8

def split(records, test_fraction):
    out = {"train": [], "test": []}
    for r in records:
        out["test" if bucket(r["id"]) < test_fraction else "train"].append(r)
    return out
