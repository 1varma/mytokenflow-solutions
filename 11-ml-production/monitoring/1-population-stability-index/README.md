# Population stability index

`ml-production.monitoring.1` · Easy · code

Your credit model was trained a year ago, and the risk team asks whether applicants' incomes look different now. Compute the population stability index. Take bin edges from the training values' quantiles (`np.quantile` at 0, 1/bins, …, 1), remove duplicates with `np.unique`, and replace the outer edges with ±∞. Floor the shares at 0.0001, and PSI = Σ(actual − expected) × ln(actual ÷ expected). Return "psi" (rounded to 4) and "level" ("none" below 0.1, "moderate" below 0.25, otherwise "major").

**How would you compute the PSI and its level?**

## Versions

| Version | Date | Runtime | Memory | Notes |
|---|---|---|---|---|
| v1 | 2026-10-23 | 541.1 ms | 71.7 MB |  |

_Synced by MyTokenFlow._
