# Two-sample Kolmogorov-Smirnov statistic

`ml-production.monitoring.2` · Easy · code

Implement `ks_test(a, b, alpha_c=1.358)`. The statistic `D` is the largest absolute difference between the empirical CDFs of `a` and `b`, evaluated at every observed value (use `np.searchsorted(sorted_x, v, side="right") / n`). The critical value is `alpha_c * sqrt((n + m) / (n * m))` (1.358 corresponds to a 5% test). Return `{"D": round(D, 4), "critical": round(c, 4), "drift": D > c}`.

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-17 | 0.2 ms | 39.4 MB | after viewing solution |

_Synced by MyTokenFlow._
