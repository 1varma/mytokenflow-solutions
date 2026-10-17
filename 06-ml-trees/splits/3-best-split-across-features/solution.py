import numpy as np

def _gini(labels):
    if len(labels) == 0:
        return 0.0
    p = np.bincount(labels) / len(labels)
    return 1 - (p ** 2).sum()

def best_split(X, y):
    X, y = np.asarray(X, dtype=float), np.asarray(y)
    best, best_score = [None, None, round(float(_gini(y)), 4)], None
    for j in range(X.shape[1]):
        u = np.unique(X[:, j])
        for t in (u[:-1] + u[1:]) / 2:
            m = X[:, j] <= t
            s = (m.sum() * _gini(y[m]) + (~m).sum() * _gini(y[~m])) / len(y)
            if best_score is None or s < best_score - 1e-12:
                best_score, best = s, [j, round(float(t), 4), round(float(s), 4)]
    return best
