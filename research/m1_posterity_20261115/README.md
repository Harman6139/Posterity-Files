# Manuscript I — Posterity archive and verification map

**Archive date:** 2026-11-15 (America/Toronto).  
**Repository:** `Harman6139/Posterity-Files`  
**Results branch:** `research/pro-m1-posterity-and-journal-benchmark-20261115`  
**Parent research snapshot:** `0be40beea703afbd07807028ee34ed8ee82b9ee6`  
**Integrity:** Source files under `ORIGINAL_HANDOFFS`, `FOUNDATIONS`, `PROOFS` and `PARALLEL_RESONANCE_AUDIT` were copied by referencing their existing Git *blob SHA*, retaining their bytes, not by generative rewriting. The branch also contains the unchanged source-tree originals.

## Read this first

1. [Research conclusions and exact limitations](STATUS_AND_PROOF_DEPENDENCIES.md).
2. [Journal and upper-quintile audit](80TH_PERCENTILE_VENUE_AUDIT.md).
3. [Original 2026-11-14 plain-DRS handoff](ORIGINAL_HANDOFFS/01_ALLORDER_PLAIN_DRS_HANDOFF.md).
4. [Original 2026-11-15 grand spectral-transport handoff](ORIGINAL_HANDOFFS/02_GRAND_THEOREM_COMPLETE_HANDOFF.md).
5. [Current consolidated manuscript](PROOFS/02_GRAND_SPECTRAL/manuscript/spectral_transport.tex), a *working draft*, not a cleared submission.
6. [Evidence, sources, numerical limitations and future audit](SOURCE_AND_DATA_PROVENANCE.md).

**Principal mathematical status:** The sourced proofs propose a rational affine–PSD `7 × 7` counterexample for `gamma=2` (and a rational gamma interval) to the universal scaled last-iterate law, together with a universal static-excess/kinetic-defect replacement for semialgebraic convex cones. An independent final referee-level audit of quantitative nonlinear trapping and the claimed exceptionally large explicit rational witness has **not** been completed in this archival exercise. No unconditional original `gamma=1` switching-orbit theorem is claimed. No publication-quality/priority certification is claimed.

## Organization and where the *full proofs* live

### ORIGINAL_HANDOFFS/
Both original user research briefs, byte-identical to their GitHub source blobs. Their success definitions, restrictions against alternating-projection substitution, and journal-percentile methodology are preserved.

### FOUNDATIONS/
The full original manuscript/milestone proofs:
- `12_` reciprocal escape law and sharp dimension bounds;
- `26_` escape-controlled projection dynamics;
- `28_` anchored/Halpern splitting;
- `30_` tame cosmic convergence and common state power;
- `31_` common leading state for monotone methods and **plain DRS**;
- `35_` analytic firmly nonexpansive counterexample (NOT affine–PSD DRS);
- `36_` exact one-Lorentz last iterates (NOT arbitrary-order PSD);
- `40_` exact convex forward–backward velocities (NOT plain DRS);
- manuscript status notes, including the historical unresolved status.
These provide complete arguments as originally committed; they are not reduced to summaries.

### PROOFS/01_ORIGINAL_DRS/
All 00–06 original DRS research checkpoints and available diagnostic scripts, including failed routes, scalar profile saturation equivalence, matrix virial identities, projective duality and the one-good-orbit transfer lemma.

### PROOFS/02_GRAND_SPECTRAL/
All 00–18 spectral-transport checkpoints, exact PSD cut energy, regular-spectrum positive theorem, saddle potential, gamma-2 weighted chart, nonlinear trapping, rational limit-set calculation, explicit witness bounds, universal excess and angular laws, gamma-family extension, switching regime and literature sample; the full `.tex` manuscript and diagnostic scripts.

### PARALLEL_RESONANCE_AUDIT/
Parallel independently written 06–09 trapping, normalized-map, rational counterexample and hostile-audit files, plus algebraic scripts. The alternative `09` files are intentionally kept distinct: their differing scopes and assumptions must never be merged silently.

### LOCAL_20261115/
Textual recovery of the original unpushed balanced-variant checkpoint and its NumPy/Numba driver, as distinct from the *proved-in-manuscript* gamma-2 construction. The original binary NumPy datasets were in the user-provided ZIP `DRS_progress_checkpoint_20261115.zip`; this GitHub connector supports UTF-8 source writes and archival Git blobs but did not ingest those binary `.npz` files here. Numerical aggregates, deterministic code, run details and hashes are recorded in the provenance file; original binary ZIP remains a separate conversation attachment.

## Dependencies and proof-status discipline

* The state law `Z_k=V k^p+o(k^p)` and `p=alpha/(1+alpha)` is obtained from the inherited tame fixed-point and conic radius results, NOT from differentiating the error.
* The counterexample claim depends critically on a uniform nonlinear spectral-inertia chart, all-time trapping, rational entry, amplitude averaging and phase winding; **not** on the six-million-step experiment.
* The general replacement is conditional on the natural-scale excess budget when deriving sharp pointwise norm coefficients; statements unconditional in the theorem are distinguished in its proofs.
* The original gamma=1 switching orbit does not follow from the gamma=2 separated spectral chart.
* Neither the originality review nor the 80th-percentile published-paper comparison is certified until proof and priority gates pass.

## Preservation policy

All prior proof versions remain available; no failed route was deleted or rewritten. Branch ancestry inherits the complete `research/laa_two_basis_track02_20261112` research tree even where off-topic milestones are not duplicated inside the curated archive. Any subsequent correction should add a numbered ERRATA or AUDIT file, with a pointer to the exact old blob and the corrected statement, rather than silently editing history.

**Do not cite this directory as a published paper or as a verified claim of acceptance odds.** It is a reproducible research archive and journal-screen record.
