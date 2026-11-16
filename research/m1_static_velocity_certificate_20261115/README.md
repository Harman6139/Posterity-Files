# Static certificates and implicit norm selection for diverging Douglas–Rachford iterations

**Research continuation:** 2026-11-15.  
**Branch:** `research/pro-m1-static-velocity-certificate-20261115`.  
**Parent:** `5aef0dda7d2280214d6a011116c26bd7988b53c8`.  
**Purpose:** supply a genuine optimization-facing theorem, not a repackaging of the older numerical resonance experiment.

## The main advance in plain language

When an affine space and the positive semidefinite cone never meet but come arbitrarily close, Douglas–Rachford can run to infinity. The new results identify a finite convex optimization problem that predicts its exact speed and the bounded matrix block it selects. A primal–dual gap gives a rigorous error bar for that prediction. Depending on the affine geometry, the selected block minimizes a Frobenius, Schatten-four or l^(4/3) norm, even though the algorithm uses Euclidean projections throughout.

A separate output theorem provides a low-memory averaging rule that recovers asymptotically best size-versus-residual points along the original algorithm. It remains valid for singular leading spectra and, more generally, arbitrary closed convex semialgebraic sets paired with an affine space. Averaging is explicitly postprocessing, not a substitute claim about unaveraged last steps.

## New theorems and their full proofs

| File | Result and exact scope |
|---|---|
| [00 — Scope](00_SCOPE_AND_DEPENDENCIES.md) | Research objective, inherited inputs and proof boundaries. |
| [01 — Local averaging](01_UNIVERSAL_LOCAL_AVERAGING_AND_SHARP_EFFICIENCY.md) | Universal cone-shadow recovery on windows h/n~1/log n, exact residual vector, and sharp efficiency loss (1-p)/(6 log^2 n); no bounded-excess assumption. |
| [02 — Finite convex program](02_FINITE_CONVEX_PROGRAM_AND_GAP_CERTIFICATE.md) | Attained strictly feasible quadratic SDP, explicit dual, exact gap identity, coefficient error <=2sqrt(gap), and finite positivity certificate. |
| [03 — Actual last velocities](03_DATA_ONLY_EXACT_VELOCITY_THEOREM.md) | Equivalence of a positive optimizer and an interior leading state. Every start obeys Z_k=V sqrt(k)+O(log k), d_k=V/(2sqrt(k))+O(log k/k). Coupled real/complex PSD products are included. |
| [04 — l^(4/3) selection](04_IMPLICIT_FOUR_THIRDS_NORM_SELECTION.md) | All-order diagonal-arrow problems select the minimum-l^(4/3)-norm cross vector. Exact formulas and a small rational zero-gap certificate. |
| [05 — Escape norms](05_ESCAPE_NORMS_DUALITY_AND_SENSITIVITY.md) | The general norm selected by the algorithm, its dual representation, three explicit norm identities, and analytic coefficient sensitivity. |
| [06 — ADMM and filters](06_ADMM_RESIDUALS_AND_RESONANCE_FILTERING.md) | Exact feasibility-ADMM residual constants and local recovery. The final resonance-filter application is explicitly conditional on the earlier resonance theorem. |
| [07 — Arbitrary coupling](07_COUPLING_INVARIANCE_AND_PRECISE_BOUNDARIES.md) | Exact speed invariant under arbitrary-strength affine couplings; failed routes and still-open singular cases are recorded. |
| [08 — Singular leading spectra](08_EXACT_VELOCITY_WITH_SINGULAR_LEADING_SPECTRA.md) | A broad all-order free-upper-block family is solved for every start even when the leading matrix has zero eigenvalues; ordinary affine least squares determines the coefficient. |
| [09 — General convex sets](09_LOCAL_RECOVERY_FOR_GENERAL_CONVEX_SETS.md) | Extends the sharp local output theorem from cones to arbitrary closed convex semialgebraic sets; also solves raw velocities for every inverse-power epigraph. |
| [10 — Literature and scope](10_PRIMARY_CONTEXT_AND_CONTRIBUTION_BOUNDARIES.md) | Primary-source comparisons, exact novelty boundaries, and the substantive optimization target addressed by this continuation. |

## The finite certificate

On the complementary support spaces determined by the affine data, let A and B be the supported primal and normal matrix subspaces, and let C0+Cdir be the affine cross-block slice. Solve

```
minimize   ||H||_F^2/4 + ||R||_F^2
subject to [[H,C],[C*,S]] >= 0,
           Q >= 0,
           R = S+Q-Z,
           H in A, C in C0+Cdir, Z in B^perp.
```

Here Q is an auxiliary PSD matrix, not the affine normal projector. The optimizer's relevant pair (H_*,R_*) is unique. Put G_*=2R_*. If H_* and G_* are positive on their respective supports, V=H_*+G_* is the exact coefficient of every DRS orbit. The optimum kappa_* satisfies

```
lim sqrt(k)||Z_(k+1)-Z_k|| = sqrt(kappa_*),
lim r D(r) = kappa_*.
```

A verified primal–dual pair of gap epsilon produces an approximation Vhat with

```
||Vhat-V||_F <= 2sqrt(epsilon).
```

Strict lower bounds for the two candidate minimum eigenvalues, exceeding 2sqrt(epsilon), certify the positive-optimizer condition. This is a finite certificate based on the problem data, not the observation of an infinite trajectory. Computing the support decomposition is not claimed to have polynomial bit complexity. A boundary optimizer does not by itself prove oscillation.

## A simple example of the implicit selection

For

```
U={[[diag(t),c],[c^T,0]] : t arbitrary, c in an affine space C},
```

let c_* minimize ||c||_(4/3) over C. When it has full support, the bounded cross block of both projected shadows converges to c_*, and

```
lim sqrt(k)||Z_(k+1)-Z_k||_F = ||c_*||_(4/3).
```

For C={c : (1,2,3)^T c=1}, the selected point is (1,8,27)/98, whereas the Euclidean projection of zero onto C is (1,2,3)/14. No l^(4/3) penalty was added to the iteration. It is selected by the affine–PSD geometry.

For the free symmetric upper-block family in Checkpoint 08, the selected norm is instead Frobenius and no full-rank condition is needed. These changes occur with the SAME original Frobenius projection metric.

## Universal output recovery

For the original DRS shadows v_j, average a centered block of 2h successive points with h/n~1/log n. Their positive average remains in the original closed convex constraint set. Its equation residual has the exact leading vector, and its residual divided by the optimal residual at the same permitted primal radius is

```
1 + (1-p)/(6 log^2 n) + o(1/log^2 n).
```

The block implementation stores only a fixed number of matrices and adds no projections. It does not need p, a spectral phase or the static profile. This output theorem is unconditional within the stated affine–convex semialgebraic class; it does NOT say that the original unaveraged velocity always converges.

## Reproducible checks

The [diagnostics directory](diagnostics) contains four runnable scripts and recorded outputs. The exact rational certificate uses Python Fraction arithmetic and verifies a zero primal–dual gap; its PSD claims have explicit Schur/factorization certificates. All trajectory experiments use double-precision eigendecompositions and are supporting checks only.

Run from that directory with Python, NumPy and Numba installed:

```
python certificate_and_drs_check.py
python averaging_admm_check.py
python coupled_four_by_four_check.py
python singular_leading_spectrum_check.py
```

The original run environment was Python 3.13.5, NumPy 2.3.5 and Numba 0.65.1. Numerical roundoff and library versions can change last digits. The proofs do not rely on those digits. The recorded outputs distinguish exact rational assertions from floating-point observations.

## Dependency and preservation discipline

- The finite coefficient/raw-velocity theorem 02–03 and explicit norm-selection applications do NOT depend on the seven-by-seven resonance proof.
- The general output-recovery theorem depends on the prior quantitative tame common-state result. Checkpoint 09 rederives the needed central-profile balance for nonconic sets.
- The one-good-orbit transfer in 08 is inherited from original DRS Checkpoint 06 and is reproved in full; it is not claimed as newly discovered here.
- The previous work and original briefs remain inherited under `research/m1_posterity_20261115`, `research/pro_m1_grand_spectral_transport_20261115` and the older foundation directories. Nothing there was overwritten.
- The unrestricted raw natural-scale upper bound in every singular SDP and the original gamma=1 switching orbit remain unresolved. No general resonance classification, journal acceptance probability or measured upper-quintile ranking is claimed.

## Manuscript implication

The organizing contribution can now be a finite predictive theory: a convex certificate computes the escape coefficient and reveals which norm the divergent algorithm implicitly minimizes. The earlier counterexample can motivate the need for conditions, but its delicate proof is not a dependency of this positive result. This directly addresses the previously identified SIOPT-facing gap. It does not automatically satisfy a separate JNS requirement for a robust resonance theorem beyond the original conic setting.
