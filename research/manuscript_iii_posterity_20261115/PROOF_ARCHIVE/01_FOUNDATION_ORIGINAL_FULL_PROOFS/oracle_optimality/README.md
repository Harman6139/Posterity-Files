# Optimal first-order complexity without minimizers — proof and reproduction packet

Date: 2026-11-13. Repository: Harman6139/Posterity-Files.
Branch: laa-track02-gptpro-analytic-frontier-20261112.

## Mathematical results

- `27_MINIMAX_ORACLE_COMPLEXITY_WITHOUT_MINIMIZERS.md`: for uniformly normalized smooth convex classes with minimum near-optimal radius rho(s) comparable to s^(-beta), the deterministic dimension-uniform value-and-gradient query complexity is Theta(epsilon^(-beta-1/2)). The all-query lower bound uses dimension 2T+3, permits an unqueried output, and uses constants independent of dimension and horizon. Proof commit: 5670a71c4cb270b558acc74be65533da0ec79f56.
- `28_HALPERN_SPLITTING_RATES_AT_INFINITY.md`: exact residual and growth powers for anchored nonexpansive iteration with a power escape profile. The Douglas–Rachford operator profile equals the primal affine/cone radius profile. Proof commit: 5af0e7dc9d9674786b19aec498d958b42a481d95.

The proof files are at the parent research-directory level in GitHub; the downloadable bundle places them next to the scripts for convenience. Neither proof requires the numerical results.

## Run

Python 3 and NumPy are sufficient. From this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python test_weighted_chain.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python test_halpern_splitting.py
```

Each script writes its corresponding JSON next to itself. Floating-point tail slopes may vary slightly by platform.

`test_weighted_chain.py` checks 35 exact Fraction prefix minima and coordinate-stationarity identities, dyadic coupling membership, a numerical Hessian bound, and consistency of an arbitrary dense-query resisting-rotation transcript. The final transcript discrepancy was below 4e-15. The simulator enforces theoretically zero unrevealed coordinates exactly; it is not using roundoff to infer a zero-chain proof.

`test_halpern_splitting.py` runs 60,000 anchored Douglas–Rachford iterations on each of three SDP systems. It checks the classical potential inequality and records fixed-point residual, state growth, primal shadow residual, and original equation residual. Scalar examples visibly retain transients, especially at exponent a=1/4. No numerical slope establishes an asymptotic theorem.

An initial transcript diagnostic treated a floating-point orthogonality residual as an exact zero; the test was corrected to encode the known mathematical zero before producing the recorded passing results. No theorem statement depended on that numerical failure.

## Exact scope

The oracle lower bound is deterministic, permits dimension to grow with the call budget, and uses a value-and-gradient black box. It is not a randomized lower bound, fixed-dimension lower bound, explicit-input SDP lower bound, or a lower bound for proximal/second-derivative oracles. Rational beta permits semialgebraic examples; the adversarial orthogonal rotation need not have bounded-height rational coefficients.

The splitting theorem is for the stated Halpern-anchored map, not plain Douglas–Rachford, arbitrary ADMM variants, inexact projections, or stochastic perturbations. The general rate result is self-contained; the sharp SDP dimension-only endpoints invoke the earlier manuscript 12 explicitly.

Classical acceleration, zero-chains, resisting oracles, and the Halpern potential are attributed in the manuscripts. Historical priority for the combined results has not been exhaustively established. No named conjecture resolution, efficient exact infeasibility detector, or editorial acceptance prediction is claimed.
