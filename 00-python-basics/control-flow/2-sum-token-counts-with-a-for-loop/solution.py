def total_tokens(messages):
    total = 0
    for m in messages:
        if m["role"] == "system":
            continue
        total += m["tokens"]
    return total
