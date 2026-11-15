# Recovery and audit status — 2026-11-15

This checkpoint records the state recovered after the interrupted response. It does not claim a new theorem proved in the recovery turn, a completed historical-priority audit, or a finished flagship manuscript.

## Verified preservation

Authenticated GitHub reads recovered checkpoints 00–05 and the complete file `code/build_certificates.py`. The recovered branch head before this checkpoint was `8568e3c1b90811d2f1729977da71abcb187e83fc`. The results branch is `research/pro-m2-grand-arithmetic-matrix-cones-20261115`, based on the quantitative M2 snapshot specified by the handoff. Original milestones remain unchanged.

The recovery turn read the complete new handoff and the complete contents of checkpoints 00, 01, 02, 03 and 05. It inspected the directory and commit metadata. It did not repeat the full earlier-paper audit or rerun the exact-certificate suite.

## Main structural result with a written internal proof

Checkpoint 01 gives an arithmetic facial-reduction procedure for a finite union P of closed rational polyhedral vector cones and a rational affine matrix slice H. Writing C(P) for its real Gram cone and R(P) for the matrices admitting rational permitted Gram columns, the claimed terminal identity is

    closure(R(P) intersect H) = C(P_*) intersect H,

or the rational-completion set is empty. At a nonempty terminal stage H meets the relative interior of C(P_*). There are at most d=n(n+1)/2 strict matrix-span reductions. The proof uses algebraic nonnegative exposers, stationarity on the minimal polyhedral face of each zero vector, and rational coefficient kernels. It does not assume every matrix-cone face is exposed.

The central qualitative proof has been reread in this recovery turn. Its scope is substantially broader than an orthant change of variables: it concerns exact affine measurements and distinguishes real feasibility, rational factorability and limits of rational factorizations. It remains subject to adversarial checking and historical comparison before a novelty or flagship claim.

Consequences stated and proved internally in checkpoint 01 include a criterion for fixed-direction measurement-preserving rational regularization and descent from permitted Gram factors over a totally real number field. The latter is not a claim that arbitrary real algebraic factors descend, or that all rational boundary CP matrices admit rational factors.

## Other recovered analytic results

Checkpoint 02 gives an exact 1/q correction for bounded cube moments on a tensor grid, preserving mass, first moments and all cross moments. It also gives exponential unmodified shadow paths on a genuinely nonsimplicial cone for n>=7. The nonsimplicial path result is for the specified shadow rule: it is not an every-local-rule result, and generalized corrected-grid early termination is not excluded.

Checkpoint 03 gives fixed-dimensional algorithmic complexity accounting based on real-algebraic primitives, rational reset between reductions, exact terminal measurement repair, and cone-relative lattice conditioning with sharp norm exponent r-1. The displayed complexity exponent and height bounds need expansion with precise primitive theorem references and full input accounting in the submission proof; a production implementation of arbitrary real-algebraic elimination is not supplied.

## Exact alternatives must remain distinct

A real-feasible but rationally unfactorable fiber cannot be separated from the original real cone. Its arithmetic obstruction uses the reduction chain, not a false copositive separator. A weakly infeasible linear image may also lack a strict separator. These two different obstructions are explicitly preserved in the corrected statement.

## Verification and packaging limitation

Checkpoint 05 records six exact test groups and six deliberately corrupted certificate rejections. Those are prior-run records, not a new run during recovery. The currently inspected remote `code/` directory contains the generator only. The independently written verifier and six JSON certificate files are not present in that directory or in the recovered grand-results directory. Their earlier hashes remain in checkpoint 05. The earlier `/mnt/data/grand_matrix_cones` working directory is not present at its recorded location in the resumed runtime. Do not link nonexistent local files or call the full verification package uploaded.

## Unfinished gates

1. Expand and adversarially audit the master theorem and quantitative proof, including all degenerate affine-slice cases.
2. Determine whether the local/global complexity claims are genuinely consequences of the same arithmetic facial mechanism, rather than an associated lower-bound construction. Current notes do not establish a numerical equivalence controlling every local pivot rule.
3. Complete primary-literature comparison; no historical novelty certificate is established by these notes alone.
4. Restore or reconstruct and rerun the independent verifier, regenerate the certificates, and upload the full source/data package.
5. Finish the submission manuscript and all required source files.
6. Complete the registered full-paper venue comparison. The twelve-paper LAA cohort remains unscored in the last recovered benchmark checkpoint. No upper-20% or editorial-probability claim is warranted.

## Overall status

Substantial structural research and explicit proofs survived the interruption. This is not merely the old specialist pivot theorem. Nevertheless, the complete Grand Theorem U package, independent verification release, historical novelty audit, and upper-quintile publication gate are NOT declared complete.
