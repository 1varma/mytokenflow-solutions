import numpy as np

def lora_forward(x, W, A, B, alpha, r):
    x, W, A, B = (np.asarray(m, dtype=float) for m in (x, W, A, B))
    s = alpha / r
    y = x @ W.T + s * (x @ A.T) @ B.T
    merged = W + s * B @ A
    y2 = x @ merged.T
    return {"y": np.round(y, 6).tolist(), "merged": np.round(merged, 6).tolist(), "max_diff": float(np.abs(y - y2).max())}
