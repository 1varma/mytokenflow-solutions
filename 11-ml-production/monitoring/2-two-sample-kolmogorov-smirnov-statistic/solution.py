import numpy as np


def ks_test(a, b, alpha_c=1.358):
    a, b = np.sort(np.asarray(a, float)), np.sort(np.asarray(b, float))
    n, m = len(a), len(b)
    pts = np.concatenate([a, b])
    fa = np.searchsorted(a, pts, side="right") / n
    fb = np.searchsorted(b, pts, side="right") / m
    D = float(np.max(np.abs(fa - fb)))
    c = alpha_c * np.sqrt((n + m) / (n * m))
    return {"D": round(D, 4), "critical": round(float(c), 4), "drift": bool(D > c)}
