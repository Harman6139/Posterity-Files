# Checkpoint 00 — from asymptotic descriptions to finite certificates

Date: 2026-11-15. Branch: research/pro-m1-static-velocity-certificate-20261115. Parent: 5aef0dda7d2280214d6a011116c26bd7988b53c8.

## Mathematical objective

Develop the missing optimization-facing advance, not another venue recommendation. Two routes are being pursued:

1. A finite convex semidefinite program, built from the affine data, whose optimizer determines whether the common DRS escape direction is positive definite and, when it is, computes the exact leading state and last velocity. The intended strengthening is a primal–dual gap certificate, not an assumption about an unknown infinite orbit.
2. A parameter-free averaging of genuine cone shadows along the ORIGINAL plain DRS orbit, on windows whose relative length tends to zero. It should recover optimal size-versus-feasibility constants even when individual last steps oscillate or lack a natural-scale bound. This is a postprocessing theorem, not an attempt to rename an averaged result as the original pointwise conjecture.

## Source dependencies

The baseline files are under research/pro_m1_grand_spectral_transport_20261115 at commit 0be40beea703afbd07807028ee34ed8ee82b9ee6. In particular 02 supplies the regular-spectrum local expansion, 03 the quadratic cross-block saddle potential, and 10/12 the common-state, balance and exact static profile. This continuation will rederive the ingredients needed for the finite certificate rather than assume that an orbit is already regular.

The new finite-certificate route is independent of the gamma=2 resonance proof and of its exceptionally large rational-start bound. The averaging theorem uses the inherited quantitative common-state theorem; this dependence is explicit. Any use of the gamma=2 example to prove an averaging lower obstruction will be marked separately.

## Current boundaries

No universal unaveraged bound ||d_k||=O(k^(p-1)) is asserted here. No resolution of the original gamma=1 switching orbit is asserted. No upper-quintile or acceptance probability is inferred from a new lemma. New proofs, computations and failed routes will be saved separately.
