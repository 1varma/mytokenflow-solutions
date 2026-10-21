from collections import Counter


def bpe_train(text, num_merges):
    vocab = {tuple(w): c for w, c in Counter(text.split()).items()}
    merges = []
    for _ in range(num_merges):
        pairs = Counter()
        for toks, c in vocab.items():
            for a, b in zip(toks, toks[1:]):
                pairs[(a, b)] += c
        if not pairs:
            break
        best = min(pairs, key=lambda p: (-pairs[p], p))
        merges.append(best)
        new = {}
        for toks, c in vocab.items():
            out, i = [], 0
            while i < len(toks):
                if i < len(toks) - 1 and (toks[i], toks[i + 1]) == best:
                    out.append(toks[i] + toks[i + 1])
                    i += 2
                else:
                    out.append(toks[i])
                    i += 1
            new[tuple(out)] = new.get(tuple(out), 0) + c
        vocab = new
    return merges
