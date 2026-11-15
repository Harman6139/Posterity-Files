# Randomized nonattainment hard-family diagnostics

Proof: `../38_RANDOMIZED_AND_PARALLEL_MINIMAX_NONATTAINMENT.md`.

Run with Python 3, NumPy and SymPy:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_hard_family.py
```

`hard_family.py` implements the 3/2-power sparse maximum, its first two derivatives, the C2 two-function maximum, the radial exterior term, the nonattainment tail, and the conservative dimension formula. It leaves the additive core minimum symbolic. No floating-point minimizer is used as an exact normalization.

`check_hard_family.py` checks the scalar C2 matching identities and constants exactly, then tests 15 frame/scale cases and 30 multi-active sparse-smoothing cases. It checks local equality of truncated and full cores, exterior masking, explicit comparison values, and finite-difference derivatives. It writes `RESULTS.json`.

The constructor uses floating point. Small examples do not establish the arbitrary randomized-oracle lower bound: its fixed-distribution coupling, spherical concentration and all-scale escape bounds are proved analytically in the manuscript. The very large conservative theorem dimensions are recorded but not allocated or simulated. Observed local Hessians in the prefix tests can be zero because the sparse maximum is exactly affine when only one coordinate is active; the separate multi-active tests exercise nonzero Hessians.

`RESULTS_SUMMARY.json` summarizes the completed run. `SHA256.json` in the parent directory checks the delivered text files. Numerical values can differ slightly across linear-algebra libraries; proof constants and symbolic identities do not depend on those runs.
