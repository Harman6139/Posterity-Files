# Project lead — all-nullity PSD spectrum theorem

**Branch:** `research/psd-joint-depth-universal-20261107`.
**Repository:** `Harman6139/Posterity-Files`.
**New research directory:** `research/psd_joint_depth_20261112/`.

Start with [the closure/audit handoff](../psd_joint_depth_20261112/131_FRONTIER_CLOSURE_AUDIT_AND_HANDOFF.md). The proof is in [128: exact-nullity interpolation](../psd_joint_depth_20261112/128_ONE_SWITCH_EXACT_NULLITY_INTERPOLATION.md) and [129: complete arithmetic spectrum](../psd_joint_depth_20261112/129_COMPLETE_ALL_NULLITY_ARITHMETIC_SPECTRUM.md).

The new insight is a single switch from upper to lower peeling. Such schedules cover every admissible integer depth; their blocking-edge collisions synchronize within one layer and can be absorbed into positive multi-child generators without cloning.

The result supplies the missing uniform sufficiency for all `(n,r,d,alpha)` and a bounded integer formula for minimum nullity. It does not claim every individual flag or rank-drop profile is realizable. It is a complete research proof, not independently refereed or priority-certified.

The [prior project-lead document](PROJECT_LEAD_START_HERE_THROUGH_127_20261109.md), [full chronological index](README_THROUGH_127_20261109.md), and [Opus handoff](../psd_joint_depth_20261109/OPUS_5_5_SUCCESSOR_RESEARCH_HANDOFF.md) remain available. All numbered predecessor files are unchanged. No repository visibility change has been made.

## Additional 2026-11-12 proof packet (preserved separately)

An independently authored [one-switch full-classification manuscript](../psd_joint_depth_20261112/128_ONE_SWITCH_FIXED_NULLITY_UNIVERSAL_CLASSIFICATION.md) and [exact rational construction/audit](../psd_joint_depth_20261112/129_ONE_SWITCH_EXACT_CERTIFICATE_AUDIT.py) have been pushed alongside the pre-existing Nov 12 theorem package, with [recorded certificates](../psd_joint_depth_20261112/130_ONE_SWITCH_EXACT_AUDIT_RESULTS.json). The auditor was rerun locally and passed 225 checks across 17 target families. These materials do not overwrite the original Nov 12 milestone 128–131 files. Both remain research proofs pending independent mathematical review.

## Single-paper generalist recommendation — Milestone 132

Read [132: rank universality, central spectra, and the single-paper architecture](../psd_joint_depth_20261112/132_RANK_UNIVERSALITY_CENTRAL_SPECTRA_AND_SINGLE_PAPER.md), with its [primary-source bibliography](../psd_joint_depth_20261112/132_PRIMARY_SOURCES.bib).

Proposed title: **Sharp error exponents and facial depth in irreducible symmetric cones**. The stronger central statement is that the exact attainable exponent/minimum-depth spectrum depends only on Jordan rank and feasible rank, not on irreducible cone type. The substantial optimization consequence is the complete joint primal/dual eigenvalue-order spectrum for external maximum-determinant regularization, including arbitrary grade multiplicities and the exact interval of compatible minimum facial degrees. The file supplies complete research proofs relative to established Milestone 128 and standard Jordan facts, as well as an abstract and draft introduction.

**Recommendation:** incorporate these compact structural strengthenings into the SAME paper, target Transactions AMS first (JLMS a strong alternative), and stop expanding into a full rank-profile classification or unrelated applications. The next priority is independent hostile proof review and manuscript consolidation. Advances in Mathematics is an ambitious editorial possibility, not a promised outcome.

**Scope to preserve:** irreducible cones only for rank-universal equality; bounded-set error exponents for possibly unbounded feasible sets; Jordan rank rather than ambient dimension; this particular maximum-determinant path rather than all central paths or algorithmic complexity. The full facial-profile problem is not claimed solved. None of the new proofs has been independently refereed, and the primary-literature comparison is not a guarantee of worldwide novelty.

## Requested profile continuation — Milestones 133–135

The follow-on request to solve the profile problem produced a uniform positive theorem and a sharp obstruction, not a full real-profile classification.

[133: two-channel prefix-profile theorem](../psd_joint_depth_20261112/133_TWO_CHANNEL_PREFIX_PROFILE_THEOREM.md) proves that every arithmetically admissible sorted-grade-prefix greedy schedule is realizable over complex and quaternionic Hermitian PSD at unchanged nullity, with arbitrary grade multiplicities and every admissible exponent. It uses the real and imaginary components of each offdiagonal entry separately, with one rigorously redundant blocker deleted. Both the global recovery bound and exact greedy maximality are proved.

[134: real/complex profile separation](../psd_joint_depth_20261112/134_REAL_COMPLEX_PROFILE_SEPARATION.md) proves that the refined **central-spectrum plus greedy-profile** data need not be cone-type universal. For null grades `(1/4,3/7,1/2,17/28,5/7,1)`, the profile `(1,2,2,1)` is impossible over real PSD with rank-one target, even allowing arbitrary dense kernels and rotated intermediate faces. An explicit complex order-seven pencil realizes it. The proof also gives a real rank-two realization and the exact threshold `r dim_R(F)>=2` for this datum. It classifies all profiles for that separating spectrum and disproves the tempting endpoint-only profile rule.

[135: audit program](../psd_joint_depth_20261112/135_PROFILE_CHANNEL_EXACT_AUDIT.py) and [results](../psd_joint_depth_20261112/135_PROFILE_CHANNEL_EXACT_AUDIT_RESULTS.json) record 999 exact exponent–schedule checks, including 454 redundant-collision checks, plus the explicit witness and scope-counterexample certificates. The finite audit is supplementary, not a substitute for the general proofs.

**Paper implication:** the field-sensitive obstruction supplies a sharp, compact boundary to the rank-universality theorem. The two-channel theorem is a related structural extension, not a separate application program. The earlier theorem 132 is not retracted or contradicted.

**Precisely still unproved:** a compact arithmetic necessary-and-sufficient formula for every real `(n,r,s_1,...,s_d,alpha)` with unrestricted central weights and arbitrary greedy flags. Genuine non-prefix flags occur, so the prefix theorem cannot be advertised as that full solution. All new manuscripts are research proofs pending independent review.
