# Project-lead handoff: Sharp PSD inverse-problem stability

**Private repository:** Harman6139/Posterity-Files

**Research branch:** research/psd-joint-depth-universal-20261107

**Master running index:** research/psd_joint_depth_20261107/README.md

**November 7 work:** research/psd_joint_depth_20261107/

**November 8 work and subsequent checkpoints:** research/psd_joint_depth_20261108/

## What this branch covers

This is the research record for the present thread on sharp Hölder recovery exponents of semidefinite inverse problems, facial-reduction singularity degree, arbitrary dense kernels, and combinatorial realizations. Numbered Markdown checkpoints contain statements, proofs, limitations, and open questions. Adjacent Python files are exact-arithmetic or symbolic reproducibility tests. Commit history preserves the order of work.

The project lead should first read this handoff, then the master README, then the linked numbered checkpoint proofs. The repository is private, so they must have GitHub permission to read it.

## Main landmarks, with exact file identifiers

- **Canonical instance-wise structural classifier**: 20261107/10_UNIVERSAL_DIKIN_HESSIAN_CLASSIFIER.md and 20261107/12_DETERMINANT_RATIO_INVARIANT.md. Related: 13 (symmetric cones), 15 (bounded nonsingleton fibres), 37 (exterior-minor valuations).
- **Exact all-degree algebraic membership/enumeration**: 20261107/14_ALL_DEGREE_JOINT_ALGEBRAIC_COMPATIBILITY.md and 16_FINITE_EXHAUSTIVE_ALL_DEGREE_SPECTRA.md. These provide an algorithmic criterion, not a compact arithmetic catalogue.
- **Sharp largest recovery exponent for every facial rank-drop profile**: 20261108/45_UNIVERSAL_SHARP_ALL_DEPTH_RANK_PROFILE_ENDPOINT.md; 49_POLYNOMIAL_DP_SHARP_FIXED_NULLITY_DEPTH_ENDPOINT.md gives the fixed-nullity/depth dynamic program; 50_PROFILE_ENDPOINT_EXACT_DP.py checks it.
- **Small-nullity exact joint tables / rigidity**: 20261107/20, 31, 33, 35 and 36, and 20261108/38–47 and 51. Some claimed exhaustive dense spectra depend on an earlier weighted-flag theorem and require independent specialist review.
- **Every rank profile has sharp lower and upper realizable endpoints**: 20261108/52_VERTEX_BLOWUP_PROFILE_PRESERVATION.md (classical lower exponent 2^(-d)) and checkpoint 45 (upper endpoint).
- **Original single-action network conjecture disproved**: 20261108/58_EXPLICIT_COUNTEREXAMPLE_SINGLE_ACTION_DEPTH_UNIVERSALITY.md gives an explicit rank-one 6x6 PSD example with nullity five, exponent 7/32 and degree four. Checkpoint 66_INFINITE_TWO_ACTION_SEPARATION_FAMILY.md gives an infinite family. The old single-action sparse classifier must NOT be presented as universally necessary.
- **Richer two-policy controlled midpoint family**: 20261108/57_MULTI_ACTION_BELLMAN_PSD_STABILITY_AND_EXACT_PEELING.md, 59_TROPICAL_MAXPLUS_FACIAL_TIME_THEOREM.md, 61_TWO_ACTIONS_SUFFICE_PSD_EXPONENT_AND_EXACT_FACIAL_PROFILE.md, 62_EXACT_TWO_POLICY_COMBINATORIAL_SPECTRUM.md. Exact exponents and exposing ranks are classified in that family, including all ambient PSD competitors.
- **Obstructions to simplistic invariants**: 20261108/63_IDENTICAL_SIGN_PATTERN_DIFFERENT_PSD_STABILITY_AND_DEPTH.md and 65_UNBOUNDED_DETERMINANTAL_ORDER_OBSTRUCTION.md.

In this list, the 20261107 and 20261108 prefixes abbreviate the folders research/psd_joint_depth_20261107/ and research/psd_joint_depth_20261108/ respectively.

## URGENT UPDATE — 2026-11-08: the former two-policy universality conjecture is DISPROVED

The previously open assertion that every arbitrary dense PSD exponent/depth pair can be realized by a strict independent-edge **two-policy** midpoint graph is now **FALSE**. The proof is [Milestone 75](../psd_joint_depth_20261108/75_SIX_BY_SIX_COUNTEREXAMPLE_TO_TWO_POLICY_UNIVERSALITY.md): an explicit rational **6x6** uniquely solvable PSD problem has target rank one, nullity five, exact minimal facial-reduction degree three, and sharp recovery exponent **3/22**, whereas every strict independent-edge Bellman graph at the same nullity and exponent requires at least four exposing steps. This is proved by a direct full-PSD modulus bound, matching PD curve, explicit dual stresses, and exhaustive exact enumeration of only **576** harmonic parent assignments. [Exact audit](../psd_joint_depth_20261108/76_TIED_EDGE_TWO_POLICY_COUNTEREXAMPLE_EXACT_AUDIT.py).

A new, stronger and still UNPROVED universal candidate is the [tied-edge MIN–MAX stochastic-game incidence model](../psd_joint_depth_20261108/74_TIED_EDGE_MINMAX_GAME_PSD_RECOVERY_AND_FACIAL_PEELING.md), which couples multiple parent edges to each scalar kernel generator. Its exact exponent and exposing-degree rules are proved **within that explicit class**; a reduction from every arbitrary dense PSD kernel is not established.

This correction supersedes older README sections and handoff statements referring to the independent-edge two-policy universality conjecture as merely open. Its **internal incidence-family compression theorem remains valid**, but that family is now known to be universally incomplete.

## Mathematical status — key distinction

**Proved within explicit construction families:** Bellman exponent/peeling theorem, two-action compression, finite two-policy spectrum, graph blow-ups and realization examples.

**Universal structural statements reported with full proofs:** Dikin–Hessian modulus comparison, sharp rank-profile endpoint theorem, and algorithmic all-degree compatibility criteria. These are research proofs, not externally refereed or independently priority-audited. Some finite dense exponent tables are conditional on earlier load-bearing weighted-flag arguments.

**Still NOT resolved:** whether every arbitrary dense PSD exponent/minimal-exposing-rank-profile pair has a two-policy incidence realization at the same nullity; equivalently, the reverse inclusion needed for a *complete compact combinatorial spectrum*. Nor is there a simple complete dimension-optimal arithmetic formula for every rational exponent at every prescribed degree. Do not communicate the full open conjecture as proved.

## Historical completeness: important caveat

The first portion of this chat generated separate **conversation attachments**, before the GitHub branch was established, including Sharp_PSD_Stability_Weighted_Flags_Memorandum.md, psd_exponent_catalogue.py, psd_exponents_nullity6.json, PSD_Facial_Peeling_Progress_2026-11-07.md and PSD_Universal_Dikin_Hessian_Classifier_2026-11-07.md. Numbered GitHub checkpoints incorporate and extend substantial content from this work, but the original chat attachments have **NOT all been verified as verbatim GitHub uploads**. Keep the original attachments too when exact historical archiving matters.

Other papers and historical project briefs referenced from additional GitHub branches or repositories are not automatically mirrored to this branch.

## Convention for future actively requested research sessions

On every verified milestone, save the next unused numbered NN_DESCRIPTIVE_TITLE.md in research/psd_joint_depth_20261108/ (or an explicitly adopted dated successor), save reproducibility code beside it, and append a concise result/status/link to research/psd_joint_depth_20261107/README.md. Preserve prior checkpoint files and mark proof assumptions, failed conjectures and unresolved gaps honestly.

There is no autonomous background activity or automatic GitHub synchronization between chat interactions; commits occur only when a research session is actively running and has permission to make them.

For immutable review or citation, use the commit SHA from GitHub history rather than a moving branch link.


## PROJECT-LEAD RESEARCH UPGRADE (2026-11-08): maximal-depth universality now PROVED

The fixed-dense-kernel-to-combinatorial gap is COMPLETELY CLOSED for the **entire maximal facial-reduction degree stratum \(d=\nu\)**, every matrix nullity \(\nu\ge2\) and positive target rank:

- [Checkpoint 89](../psd_joint_depth_20261108/89_UNIVERSAL_FIXED_MONOMIAL_DIKIN_CHART_DENSE.md) proves a fixed monomial Loewner chart for the canonical maxdet center of EVERY dense uniquely solvable PSD inverse problem, and gives a finite weighted linear-rank test for its exact recovery exponent.
- [Checkpoint 90](../psd_joint_depth_20261108/90_COMPLETE_DENSE_MAXIMAL_DEPTH_CONVEX_GAME_UNIVERSALITY.md) proves that at d=nu the valuation grades are all one-dimensional and aligned with the facial chain; the weights are genuine rational harmonic midpoints with nondecreasing gaps, and the sharp exponent is a qualifying half-weight. Thus the bounded primitive **INTEGER-GAP** finite combinatorial iff previously proved only for incidence constructions in [Checkpoint 72](../psd_joint_depth_20261108/72_INTEGER_GAP_DIOPHANTINE_MAXDEPTH_CLASSIFICATION.md) is now UNIVERSALLY exact for **all arbitrary dense measurement kernels** at maximal depth. This includes nonreciprocal values at nullity six.

**Still open:** the full necessary-and-sufficient combinatorial catalogue at NONMAXIMAL singularity degree d<nu, including all exact rank profiles. Do not interpret the maximal-depth theorem as a full solution of every (n,r,d,alpha) compatibility.

**Audit:** Checkpoints 89–90 have self-contained mathematical proofs; they have not yet undergone independent external referee review or novelty/priority verification.
