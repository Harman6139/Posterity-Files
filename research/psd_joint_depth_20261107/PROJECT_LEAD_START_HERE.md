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


## NEW COMPLETE STRATUM (2026-11-08) — arbitrary dense ν=5, d=3

The arbitrary dense recovery spectrum at target nullity **five** and exact minimal singularity degree **three** has now been COMPLETELY classified: **51 rational exponent values**, independently of any conjectured dense-to-tied-game universality. [Checkpoint 97](../psd_joint_depth_20261108/97_COMPLETE_UNIVERSAL_DENSE_NULLITY_FIVE_DEGREE_THREE.md) contains the full list and proof; [checkpoint 98](../psd_joint_depth_20261108/98_NU5_D3_COMPLETE_EXACT_RATIONAL_AUDIT.py) contains exhaustive rational verification. Key prerequisite [95](../psd_joint_depth_20261108/95_DENSE_DUAL_CENTRAL_TWO_STEP_THRESHOLD.md) proves a universal two-step dual-center threshold. All 51 fractions are realized constructively: 49 independent-edge incidence systems and two tied-edge systems with α=3/22 and 3/20.

**Still open:** full all-nullity/all-depth joint classification, notably the ν=5,d=4 stratum and nonmaximal degrees in dimensions ≥6. No background research or automatic commits occur between active sessions.


## 2026-11-08 NEW: full arbitrary-DENSE spectrum at target nullity SIX

[Checkpoint 103](../psd_joint_depth_20261108/103_COMPLETE_DENSE_NULLITY_SIX_ALL_DEGREES.md) and its [exact rational certificate 104](../psd_joint_depth_20261108/104_NU6_ALL_DEGREES_EXACT_FRACTION_CERTIFICATE.py) now COMPLETE every exponent-versus-exact-singularity-degree set for **all arbitrary dense PSD problems with target nullity \(\nu=6\)**: number of distinct sharp exponents at d=1,..,6 is **2,81,206,174,107,46**. Dense necessity is independent of graph universality (canonical maxdet harmonic extraction + original-kernel primal/dual peeling recurrences), sufficiency comes from explicit globally PSD incidence constructions. The crucial new [13/64 degree-five 7×7 example](../psd_joint_depth_20261108/102_THREE_SLACK_ACTIONS_NEW_NU6_D5_13_OVER_64.md) uses THREE Bellman-slack actions and has exact exposing profile (1,1,1,2,1). All checkpoint files are on this SAME research branch.

**Still NOT proved:** a uniform closed all-nullity all-degree compact combinatorial theorem, or every possible exact rank-drop profile conditioned on a prescribed exponent. Specialist audit / priority checks remain required.


## NEW completed arbitrary-dense nullity SEVEN (2026-11-08)

The fixed-target-nullity ν=7 PSD sharp exponent spectrum has been completely classified at **every exact minimal facial degree d=1,...,7**, for arbitrary dense measurement maps and every positive target rank. The numbers of exponents for d=1,...,7 are **2, 325, 857, 817, 596, 321, 117**. See [Milestone 105](../psd_joint_depth_20261108/105_COMPLETE_DENSE_NULLITY_SEVEN_ALL_DEGREES.md) for the precise iff and proof, and [Milestone 106](../psd_joint_depth_20261108/106_NU7_ALL_DEGREES_EXACT_CPP_CERTIFICATE.cpp) for the exhaustive 518400-policy exact-rational reproducibility certificate. No use of unproved dense-to-game universality occurs in necessity; sufficiency is explicit PSD construction.

**Remaining:** the requested UNIFORM all-nullity compact joint combinatorial theorem (or a counterexample to the interval-filling principle), and all-value classification conditioned on every exact facial rank-drop profile. This handoff and master index remain the update lane.


## 2026-11-09 latest checkpoints: precise remaining fixed-dimension obstruction

Latest [Milestones 107–113](../psd_joint_depth_20261108/112_SHARED_RELEASE_EDGES_AT_EXACT_ORIGINAL_NULLITY.md) substantially advance the all-nullity interpolation mechanism. [Milestone 110](../psd_joint_depth_20261108/110_UNIFORM_INTERVAL_REALIZATION_WITH_LINEAR_NULLITY_OVERHEAD.md) proves a uniform construction for EVERY integer \(L(w)\le d\le U(w)\) associated with any strict rational harmonic w, with at most \(3h+1\) null coordinates instead of the original \(h+1\). [Milestone 112](../psd_joint_depth_20261108/112_SHARED_RELEASE_EDGES_AT_EXACT_ORIGINAL_NULLITY.md) removes all clones for the LOWER endpoint \(d=L(w)\) when the sharp exponent is the smallest harmonic diagonal weight \(w_1\); it also covers leading halfweights without a release-edge collision (and all leading halfweights with a second positive support coordinate). [Checkpoint 113](../psd_joint_depth_20261108/113_SHARED_RELEASE_FIXED_NULLITY_EXACT_AUDIT.py) checks exact rational stresses and full-weight support across the 2,099 strict h=5 graphs.

**NOT SOLVED:** universal fixed-nullity realization of all intermediate and upper depths, including some rank-one leading-edge collision cases. A single Bellman-neutral action can jump two facial steps (107), so induction by adding one edge and assuming one-step changes is invalid. The master README has the detailed chronology.


## NEW 2026-11-09 result — rank-one leading-edge collision fully repaired, no extra null directions

[Milestone 114](../psd_joint_depth_20261108/114_ALL_HALFWEIGHTS_LOWER_PEELING_EXACT_NULLITY_RANK_ONE.md) proves that for EVERY strict harmonic w and EVERY possible sharp leading halfweight α=w_v/2≤w1, the fastest *primal* exposing depth d=L(w) is attained by a full-PSD rational measurement construction at EXACT original nullity ν=h+1 and rank-one target; any higher positive target rank is obtained by fully measured padding. Earlier milestone112 handled α=w1 and noncolliding leading edges; the remaining collision is shown to occur only at the final exposing layer and repaired by a positive-definite harmonic-anchor stress. [Audit 115](../psd_joint_depth_20261108/115_ALL_HALFWEIGHT_COLLISION_REPAIR_EXACT_AUDIT.py) exactly checks 933 collisions among 5,269 tested halfweight cases.

**The requested FULL uniform fixed-nullity arithmetic classification is STILL OPEN.** The outstanding dimension-preserving sufficiency concerns all interior and upper exposing depths (the clone-assisted version is in Milestone110), not the lower peeling endpoint. Expert review remains needed.


## 2026-11-09 ACTIVE RESEARCH UPDATE — exact rank-one lower bound solved; new signed cancellation obstruction

[Milestone 114](../psd_joint_depth_20261108/114_ALL_HALFWEIGHTS_LOWER_PEELING_EXACT_NULLITY_RANK_ONE.md) now removes the LAST exception in the original-nullity fastest-exposure realization: for EVERY strict harmonic w and ANY valid sharp halfweight α≤w1, a rational rank-one PSD problem at EXACT original nullity realizes α and d=L(w). The independent leading-source-edge collision can only happen at the final exposing stage and is repaired using a PD harmonic-anchor stress. [Checkpoint 115](../psd_joint_depth_20261108/115_ALL_HALFWEIGHT_COLLISION_REPAIR_EXACT_AUDIT.py) checked all 933 source/release collision cases through h=5 exactly.

The NEXT attempt to eliminate clones at the upper endpoint exposed a genuine no-go: [Milestone 116](../psd_joint_depth_20261108/116_SAFE_TIGHT_EDGE_COLLISION_CHANGES_SHARP_EXPONENT.md) provides explicit rational 7×7 PSD measurements where adding a Bellman-safe parent action that physically SHARES another child's tight edge changes sharp exponent **1/6 → 1/7** while retaining four facial steps. [Checkpoint 117](../psd_joint_depth_20261108/117_SAFE_TIGHT_COLLISION_EXACT_SYMBOLIC_AUDIT.py) verifies all exposing stresses and a sharp monomial arc. [Milestone 118](../psd_joint_depth_20261108/118_SHARED_EDGE_LOCKS_DIKIN_VALUATION_GRADES.md) derives the universal stationarity mechanism: a shared edge forces canonical dual diagonal valuation grades to MERGE, independent of fixed coefficient tuning.

**Full classification remains OPEN:** dimension-free all-depth interpolation is proved with O(ν) clones (110); the original-nullity lower endpoint is now solved (114), but exact original-nullity upper/intermediate depths demand different harmonic policies or nontrivial signed/determinantal circuit designs. Do NOT claim this last sufficiency as proved. Prior results require independent specialist review.


## 2026-11-09 PROJECT-LEAD UPDATE — FULL effective all-n ANALYTIC membership classification (not a graph-only formula)

The latest [Milestone 120](../psd_joint_depth_20261109/120_UNIFORM_SIGNED_CONIC_MATROID_ALL_N_CLASSIFIER.md) states and proves a uniform **necessary-and-sufficient finite semialgebraic certificate** for every (matrix order n, target rank r, exact minimal facial depth d, sharp exponent α), including exact rank-drop profiles. It searches finitely many rational harmonic grade graphs and multiplicities, and then uses **real linear kernel coefficients, maximum-weight linear-matroid rank tests, graded positive-definite dual separation, primal first-coefficient witnesses and exact compressed facial stress towers**. Polynomial quantifier elimination decides the certificate for ALL finite n. This is a structured analytic upgrade over the earlier raw algebraic membership algorithm in checkpoints14/16, not a newly settled *purely arithmetic graph-only spectrum*.

[Milestone 119](../psd_joint_depth_20261109/119_INITIAL_CONIC_GRADED_KERNEL_LOEWNER_IFF.md) proves a graded-cone plus full-rank primal-witness criterion for a proposed monomial Loewner chart; [Milestone 121](../psd_joint_depth_20261109/121_SHARED_EDGE_GRADED_CONIC_CERTIFICATE.md) gives a self-contained exact positive-semidefinite initial-kernel direction that detects the rate-changing shared-edge collision of checkpoint116 without computing the center.

**DO NOT REPORT THE STRONGER FULL GRAPH-ONLY UNIVERSAL THEOREM AS PROVED.** The remaining open target is to eliminate the residual real-conic feasibility tests, producing a compact necessary-and-sufficient purely finite-integer/combinatorial list and optimum dimensions uniformly in n. Earlier maximal-depth, exponent-only, unrestricted-dimension and small-nullity spectra remain important proved subcases (subject to specialist proof audit). No background work or automatic commits happen between active research sessions.


## NEW 2026-11-09 — Exact-nullity UPPER peeling milestone, plus graded cone simplification

[Checkpoint 123](../psd_joint_depth_20261109/123_CLONE_FREE_UPPER_PEELING_BY_MULTICHILD_DIAGONAL_GENERATORS.md) proves that **EVERY** strict harmonic w and admissible halfweight alpha can be realized at the **original nullity** with singularity degree EXACTLY U(w) and all upper exposing layers. The construction avoids edge-sharing cancellation by assigning each physical parent edge to only one generator while allowing that generator to contain two diagonal child coordinates. [Exact C++ exhaustive audit 124](../psd_joint_depth_20261109/124_CLONE_FREE_UPPER_EXACT_RATIONAL_CPP_AUDIT.cpp) verifies 34,570 strict h=6 harmonic systems, 6,276 requiring diagonal coupling. [Checkpoint 122](../psd_joint_depth_20261109/122_GRADED_PSD_CONE_SPLITS_AND_SIMPLE_WEIGHT_RANK_CRITERION.md) independently proves the weighted initial PSD cone splits by valuation grade; for simple grades its strict separation reduces to ordinary rank tests, giving an alternative harmonic midpoint proof.

Together with the earlier [lower-bound checkpoint 114](../psd_joint_depth_20261108/114_ALL_HALFWEIGHTS_LOWER_PEELING_EXACT_NULLITY_RANK_ONE.md), **BOTH universal extremal depths L(w) and U(w) now have uniform dimension-preserving rank-one realizations in EVERY nullity**. What remains OPEN: all intermediate depths L(w)<d<U(w) at unchanged nullity, and the stronger full exposing rank-profile spectrum. The often-cited 7×7 shared-edge example checkpoint 116 still changes exponent, but its displayed harmonic vector has **L=U=4** (corrected); it is not evidence about depth interpolation.

This is significant constructive progress, but neither the complete pure-integer all-n joint spectrum nor proof of every intermediate depth has been achieved. Expert audit is outstanding.
