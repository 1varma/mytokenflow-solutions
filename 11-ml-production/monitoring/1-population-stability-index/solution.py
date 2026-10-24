import numpy as np


def psi(expected, actual, bins=10):
    expected, actual = np.asarray(expected, float), np.asarray(actual, float)
    edges = np.unique(np.quantile(expected, np.linspace(0, 1, bins + 1)))
    edges[0], edges[-1] = -np.inf, np.inf
    e = np.clip(np.histogram(expected, edges)[0] / len(expected), 1e-4, None)
    a = np.clip(np.histogram(actual, edges)[0] / len(actual), 1e-4, None)
    value = round(float(np.sum((a - e) * np.log(a / e))), 4)
    level = "none" if value < 0.1 else "moderate" if value < 0.25 else "major"
    return {"psi": value, "level": level}
