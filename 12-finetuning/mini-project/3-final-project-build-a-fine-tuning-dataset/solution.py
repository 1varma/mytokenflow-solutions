import json
import random
import re

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")

def to_line(system, prompt, completion):
    msgs = [{"role": "system", "content": system}, {"role": "user", "content": prompt}, {"role": "assistant", "content": completion}]
    return json.dumps({"messages": msgs}, ensure_ascii=False)

def build_dataset(rows, system, test_frac, seed=0):
    dropped = {"empty": 0, "pii": 0, "duplicate": 0}
    kept, seen = [], set()
    for row in rows:
        p, c = row["prompt"].strip(), row["completion"].strip()
        key = " ".join(p.lower().split())
        if not p or not c:
            dropped["empty"] += 1
        elif EMAIL.search(p) or EMAIL.search(c):
            dropped["pii"] += 1
        elif key in seen:
            dropped["duplicate"] += 1
        else:
            seen.add(key)
            kept.append((p, c, row["customer"]))
    keys = sorted({cust for _, _, cust in kept})
    random.Random(seed).shuffle(keys)
    target, test_keys, count = test_frac * len(kept), set(), 0
    for k in keys:
        if count >= target:
            break
        test_keys.add(k)
        count += sum(1 for _, _, cust in kept if cust == k)
    train = [to_line(system, p, c) for p, c, cust in kept if cust not in test_keys]
    test = [to_line(system, p, c) for p, c, cust in kept if cust in test_keys]
    return {"train": train, "test": test,
            "report": {"kept": len(kept), "dropped": dropped, "train_rows": len(train), "test_rows": len(test),
                       "test_customers": sorted(test_keys)}}
