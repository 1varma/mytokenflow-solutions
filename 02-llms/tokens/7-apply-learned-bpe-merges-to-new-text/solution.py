def bpe_encode(word, merges):
    rank = {tuple(m): i for i, m in enumerate(merges)}
    parts = list(word)
    while len(parts) > 1:
        pairs = [(rank[p], p) for p in zip(parts, parts[1:]) if p in rank]
        if not pairs:
            break
        _, (a, b) = min(pairs)
        merged, i = [], 0
        while i < len(parts):
            if i + 1 < len(parts) and parts[i] == a and parts[i + 1] == b:
                merged.append(a + b)
                i += 2
            else:
                merged.append(parts[i])
                i += 1
        parts = merged
    return parts
