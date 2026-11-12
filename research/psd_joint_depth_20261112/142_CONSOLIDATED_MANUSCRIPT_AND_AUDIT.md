# 142 — One consolidated manuscript: rank universality versus field-dependent tangency

**Date:** 2026-11-12.  
**Branch:** `research/psd-joint-depth-universal-20261107`.  
**Inputs:** branch head `b9237b13b0295c37dbe5a1b564d13837c2986a19` and the uploaded Milestones 139–141 field-obstruction packet.  
**Status:** internally audited pre-submission research manuscript; no independent referee certification or journal submission.

## Deliverable

The complete source is in [manuscript/](manuscript/README.md), with [main LaTeX](manuscript/manuscript.tex), [bibliography](manuscript/references.bib), [proof and novelty audit](manuscript/AUDIT_AND_PUBLICATION_MEMO.md), and [exact reproducibility supplement](manuscript/supplement/README.md). The source compiles to a 22-page PDF; run `python3 build.py`. The compiled PDF is included in the conversation publication package, not tracked as a binary in the branch.

Title: **Rank universality and field-dependent tangency of symmetric cones**.

The manuscript has exactly three headline theorems:

1. Rank-universal central-order/multiplicity, sharp-exponent, and minimum-depth spectra for irreducible symmetric cones, with a coarse bounded-set affine-section extension.
2. The complete complex/quaternionic survivor-table classification, including non-prefix flags and split grades at unchanged rank.
3. For every m,r >= 1, exponent 5/27 and greedy profile (m,1,2,2) at nullity m+5 are attainable over F=R,C,H exactly when r dim_R(F) >= 2, even when all alternative central certificates are allowed.

The common central-chart argument, real one-switch realization, multiplicity and cone-type transfers, flag congruence, two-component construction, denominator-27 restriction, and explicit six-generator separation are proved in the manuscript. Unpublished milestones are not used as black-box proofs. The unrelated product and quotient-encoding programs are omitted.

## Explicit erratum to the original Milestone 139 note

The weighted off-face cut-rank jump requires an internal grade `0 < tau < 1`. At terminal order one, the actual central coefficient need not belong to K; only its difference from the identity does. The example `X*=E00, K=span(R01)` in S^2 has center diag(1+t,t), a valid first exposure E11, and zero off-face cut ranks on the full face. It disproves the unrestricted terminal formulation.

The unweighted positive-circuit lemma is unchanged, and the separation theorem uses the internal order 10/27, so its proof is unaffected. The correction is explicit in Section 6, Appendix C, the audit memo, and the independent checker. It is not silently concealed by editing an old proof.

## Verification and remaining gates

The supplied one-switch, general-table, and field audits were rerun with exact arithmetic. A newly written independent checker verifies the two determinant-27 graph types, their boundary systems, all explicit complex witness pairings and compressions, the unique obstructed cut, and the terminal counterexample. All pass. The finite claim that six is the smallest separating nullity is isolated as optional computer-assisted material; no main theorem depends on it.

The bibliography and introduction now explicitly compare tropical PSD cones, mediated sets, stochastic-game formulations, symmetric-cone error bounds, external maximum-determinant asymptotics, and symmetry reduction. No worldwide-priority certification is claimed.

Recommendation: consolidate this paper for Transactions AMS first, with JLMS a strong alternative. Advances is an ambitious editorial possibility requiring independent expert assessment, not additional peripheral classifications. Before submission the responsible authors must complete specialist proof review, authorship/affiliation metadata, final priority checking, and the accurate AI declaration. The unrestricted real-profile classification remains outside the stated theorems, not a missing dependency.
