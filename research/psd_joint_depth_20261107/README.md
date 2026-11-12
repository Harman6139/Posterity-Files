# Sharp PSD stability — master research index

**Research branch:** `research/psd-joint-depth-universal-20261107` in `Harman6139/Posterity-Files`.

## Current theorem package — 2026-11-12

[Milestone 128: one-switch interpolation at exact nullity](../psd_joint_depth_20261112/128_ONE_SWITCH_EXACT_NULLITY_INTERPOLATION.md) gives an explicit rational realization of every admissible harmonic half-weight at every integer depth between the canonical peeling bounds, with no extra null coordinates. The proof controls every ambient PSD competitor and establishes the **minimum** facial degree, including the leading-edge collision cases.

[Milestone 129: complete all-nullity arithmetic spectrum](../psd_joint_depth_20261112/129_COMPLETE_ALL_NULLITY_ARITHMETIC_SPECTRUM.md) reconstructs dense necessity and gives the finite integer necessary-and-sufficient formula for all `(n,r,d,alpha)`, together with a bounded arithmetic formula for the exact minimum nullity.

[Milestone 131: proof scope, audit, and handoff](../psd_joint_depth_20261112/131_FRONTIER_CLOSURE_AUDIT_AND_HANDOFF.md) distinguishes the closed tuple-existence frontier from the stronger rank-profile and individual-kernel questions. The [exact certificate program](../psd_joint_depth_20261112/130_EXACT_ONE_SWITCH_CERTIFICATE.py) and [recorded output](../psd_joint_depth_20261112/130_AUDIT_OUTPUT.txt) are supplementary checks, not finite-case substitutes for the general proof.

**Status:** complete research proof; independent specialist review and literature-priority audit remain outstanding.

## Complete historical record

The [chronological master index through milestone 127](README_THROUGH_127_20261109.md) is an exact preserved copy of the former README at commit `48bcfb75063cb8674f3505384cbcd5e8ddc8af75`. Its old open-problem statements describe the status at their dates. All linked milestone files and original chat-attachment archives remain unchanged.

The [original Opus 5.5 handoff](../psd_joint_depth_20261109/OPUS_5_5_SUCCESSOR_RESEARCH_HANDOFF.md) and [previous project-lead handoff](PROJECT_LEAD_START_HERE_THROUGH_127_20261109.md) are preserved. The old forbidden-schedule and cancellation examples remain valid; the new construction avoids their hypotheses rather than overturning them.

## Parallel one-switch proof and exact-rational certificates (2026-11-12)

A second, independently prepared research write-up is archived as [128 — fixed-nullity universal classification](../psd_joint_depth_20261112/128_ONE_SWITCH_FIXED_NULLITY_UNIVERSAL_CLASSIFICATION.md), with its [rational constructor/audit](../psd_joint_depth_20261112/129_ONE_SWITCH_EXACT_CERTIFICATE_AUDIT.py), [recorded results](../psd_joint_depth_20261112/130_ONE_SWITCH_EXACT_AUDIT_RESULTS.json), [manifest](../psd_joint_depth_20261112/SOURCE_AND_CHECKSUM_MANIFEST.json), and [original pre-push packet notes](../psd_joint_depth_20261112/README_PARALLEL_ONE_SWITCH_PROOF.md). Its internal milestone numbering overlaps the earlier Nov 12 package; filenames are intentionally distinct and no existing proofs or historical checkpoints were overwritten. The original auditor was rerun on 2026-11-12 and reported PASS on 225 constructions in 17 families. This is a research proof, not an independently refereed or validated journal result.

## Milestone 132 — one-paper geometric strengthening and significance (2026-11-12)

[132: rank universality, complete central spectra, and single-paper architecture](../psd_joint_depth_20261112/132_RANK_UNIVERSALITY_CENTRAL_SPECTRA_AND_SINGLE_PAPER.md) supplies research proofs that the attainable sharp affine-section exponent/minimum-depth spectrum is identical for all **irreducible symmetric cones of the same Jordan rank**, and that every admissible primal/dual maximum-determinant eigenvalue-order vector can be realized with arbitrary prescribed grade multiplicities and every compatible minimum degree. The proof includes a fixed graded Jordan chart, harmonic necessity, exact facial-depth preservation under a positive retraction, and a multiplicity lift of the one-switch construction. A gauge reduction covers general nonempty affine sections on bounded test regions.

The same file contains the adversarial primary-literature audit, proposed title and abstract, draft introduction, economical theorem/proof architecture, and recommendation to consolidate one Transactions AMS submission rather than pursue a separate rank-profile program. The [primary-source BibTeX bibliography](../psd_joint_depth_20261112/132_PRIMARY_SOURCES.bib) records the literature and current journal-policy sources.

**Scope:** Jordan rank is not ambient vector-space dimension; irreducibility is essential. The spectral result concerns external maximum-determinant regularization, not every SDP central path, full Puiseux ramification, or algorithmic iteration rates. No classification of all exposing rank profiles is claimed. The arguments assume Milestone 128 and standard Jordan algebra facts; they remain unrefereed research proofs, and worldwide bibliographic priority is not certified.

## Milestones 133–135 — uniform prefix profiles and a sharp boundary to rank universality

[133: two-channel prefix-profile theorem](../psd_joint_depth_20261112/133_TWO_CHANNEL_PREFIX_PROFILE_THEOREM.md) gives a uniform necessary-and-sufficient arithmetic criterion for **every prescribed grade-prefix greedy schedule over complex and quaternionic Hermitian PSD cones**, at exactly the original nullity, with arbitrary grade multiplicities and every admissible sharp exponent. Tight edges use real coordinates and releases use imaginary coordinates; blockers use the remaining coordinate. The only three-way collision is a redundant child-one blocker, which is deleted. The proof controls all ambient competitors and establishes the actual maximum-rank greedy faces and minimum depth.

[134: real/complex profile separation](../psd_joint_depth_20261112/134_REAL_COMPLEX_PROFILE_SEPARATION.md) proves that **prescribing the entire central spectrum together with the greedy rank-drop profile can detect the scalar field**. For the six simple null grades `(1/4,3/7,1/2,17/28,5/7,1)`, the profile `(1,2,2,1)` is impossible over real PSD at rank-one target, even for arbitrary dense kernels and rotated exposing subspaces, but has an explicit complex order-seven realization. For this datum its exact source/field threshold is `r dim_R(F)>=2`. The file gives the complete profile list for this separating spectrum, a real rank-two realization, and counterexamples to the endpoint-only and prefix-only shortcuts. The coarser rank-universality theorem of 132 is unchanged.

[135: exact audit code](../psd_joint_depth_20261112/135_PROFILE_CHANNEL_EXACT_AUDIT.py) and [recorded results](../psd_joint_depth_20261112/135_PROFILE_CHANNEL_EXACT_AUDIT_RESULTS.json) verify 999 exponent–schedule certificates using rational arithmetic, including 454 redundant-collision cases, the explicit real/complex witness pairings, and the scope counterexamples. These checks supplement, rather than establish, the all-dimensional theorem.

**Remaining gap:** a compact arithmetic iff for every real `(n,r,s_1,...,s_d,alpha)` with unrestricted canonical weights and arbitrary greedy flags is NOT proved. The prefix theorem must not be described as that full classification. All new mathematical arguments remain unrefereed research proofs.
