# Checkpoint 008 — manuscript and independent verification

Project date: 2026-11-14.

The complete local manuscript, **Sharp Ryshkov margins and the binary complexity of copositive shadow paths**, has been written and compiled twice with pdflatex. It is 20 pages, with no overfull boxes or undefined-reference warnings. It contains self-contained proofs of the sharp norm exponent, all-order exponential paths, positive definite strictly entrywise-positive lower-bound inputs, the quantitative upper bound and heights, the finite neighbor cutoff, the exact support oracle, rational outward-rounded ellipsoids, and the total separator-or-nearby-factor alternative. The known 2023 shear construction and classical support/ellipsoid antecedents are explicitly credited.

The source and PDF are currently in the active runtime under /mnt/data/copositive_track_II/manuscript/. Their GitHub/source-package export and the venue report are being completed. This checkpoint does NOT pretend the PDF has already been committed.

## Completed exact tests

Original suite:
- 5 simplex-minimum cases, including singular and boundary cases.
- 200 seeded exact linear systems.
- 85 simple-family shadow normal identities.
- 4 complete Ryshkov neighbor computations.
- Binary separation in 13 rounded ellipsoid updates.
- Positive definite non-CP five-cycle separation in 84 updates; 2015 support systems in the trajectory.

Additional tests:
- A separate Gauss–Jordan verifier, importing neither the generator's Bareiss solver nor its support oracle, independently recomputed all 3 and 31 support cases for the saved binary and five-cycle separators. Both passed exact norm, target-gap and copositivity-margin checks.
- 42 strictly entrywise-positive perturbed DNN normal-cone decompositions, in dimensions 5 through 10, passed exact reconstruction, positivity and active-face checks.
- 20 sharp-margin perfect-vertex cases (orders 2 through 6, q=2,3,8,32) passed exact active-vector and full-rank tests, including the long minimal vector.
- A complete unsuccessful ellipsoid stage on the CP matrix J_2/4 ran all 960 prescribed updates; finite-cut-cone recovery then found an exact CP approximation after 3 subset solves. Its rational Gram conversion was reconstructed exactly. This tests the actual finite primal branch, not only its projection subroutine.

## Large compressed lower-bound certificate

For n=5 and N=2^128, the DNN construction and its strictly positive perturbation have a certified prefix of

    768614336404564649 adjacent pivots.

The certificate stores the rational input, inverse-congruence Horn separator, distance bound, and first/last normal-cone decompositions. The universal formulas prove every intermediate transition. No claim is made to have simulated that many pivots. All certificate entries are exact rationals; the Horn separator was also checked by the independent mathematical support criterion.

## Remaining publication gates

The 10-paper-per-venue sample was prespecified in 07_BENCHMARK_PROTOCOL.md. Primary issue pages and all Mathematical Programming DOIs have now been retrieved, but full-proof comparisons are not complete. Several LAA sample full texts remain inaccessible through the sources tried. They will not be counted as comparative passes on the strength of abstracts.

The new results are mathematical claims with supplied proofs, not a completed independent referee review. Historical priority of the quantitative lower bounds and sharp exponent is still being compared against the 2017, 2021, 2023 and 2026 primary literature. The 2026 generalized-perfect-matrix paper gives a qualitative Dirichlet argument, not the explicit sharp norm exponent proved here. No upper-quintile or acceptance-probability certification is claimed at this checkpoint.
