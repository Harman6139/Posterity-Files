# Submission readiness and journal strategy (2026-11-13)

**Status:** All mathematical research files 01–09 and their diagnostic source/results are on the named working branch. This is a *pre-submission editorial assessment*, not a new proof, prior-art certificate, or journal acceptance decision.

## Recommended target

**Primary: Mathematical Programming (Series A)**, conditional on a human-led independent mathematical audit and a serious novelty review.

The central result is a universal finite-dimensional reduction of bounded trace-controlled semidefinite programming to TWO complete real orthonormal-basis diagonal lists, with an explicit order (N=11m^2+8m+14+2p), an exact globally positive many-to-one feasible-fibre quotient, exact source-objective preservation, and rank-independent all-PSD residual control. Secondary theorems give CP amplifications, exact facial depth `max(1,k)`, dual attainment equivalence, dense nonreflection bases, and a sharp ambient leakage-modulus law. These subjects are native to conic optimization, spectrahedral representation, and stability.

Official scope: https://www.mathprog.org/sub/journal.htm . The scope covers theoretical mathematical programming, convexity, constrained optimization, and interfaces with computer science. The scope fit is strong; *editorial acceptance and originality are unverified*.

**Secondary:** Mathematics of Operations Research (Continuous Optimization), especially if framed as a structural theorem with computational relevance. Official scope and submission guidance:
https://pubsonline.informs.org/page/moor/editorial-statement
https://pubsonline.informs.org/page/moor/submission-guidelines
MOR currently asks for 35–45 pages in 1.5 spacing, including everything, unless approved otherwise; this encourages a careful single-paper theorem hierarchy.

**Alternative:** SIAM Journal on Optimization if the exposition can be made unusually compact. Official scope and instructions:
https://epubs.siam.org/siopt/editorial-policy
https://epubs.siam.org/journal/siopt/instructions-for-authors
SIOPT normally has a 25-page typeset limit, and unusually long submissions need special justification; the current proof corpus is too wide to submit unchanged as one SIAM paper.

## Proposed central paper

**Working title:** `A Quadratic-Size Two-Orthonormal-Basis Normal Form for Semidefinite Programming`

Alternate technical title: `Universal Positive Two-Basis Quotients of Semidefinite Feasible Sets`.

**Main theorem in abstract:** For each rational trace-controlled SDP on (mathbb S^m_+) with (p) affine measurements, construct in polynomial bit complexity (given a rational positive trace-control certificate) two real complete ONBs of order (O(m^2+p)), a globally CP affine encoder with a fixed PSD offset, a CP coisometric decoder, and affine target data. The two-basis PSD fibre maps *onto* the source fibre for every datum. Source residual and exact linear objectives are controlled globally. Positive observations (including zero data) and dense nonreflection basis transitions can be enforced. A second theorem shows exact facial-degree transformation, dual attainment equivalence, and sharp entire-lift stability via minimum-face leakage.

**Core novelty mechanism to make readable:** Four-character anchor-entry copying + conically positive free auxiliary covariance + special block-respecting Parseval completion + one signed exposing two-basis dilation. Explicitly explain why this is a many-to-one quotient and does not contradict positive-retract or two-MASA obstructions.

## Proposed manuscript structure

1. Introduction: precise universal claim, relevance to rank-one measurement models and SDP normal forms; contrast with known tensor/rank-one and two-MASA architectures.
2. Preliminaries and theorem: exact all-data fibre quotient, global residual, complexity and objectives.
3. Anchor-entry-copy gadget, positive lift, linear inverse certificate.
4. Frame completion and conversion to two complete orthonormal bases.
5. Strong form: all-positive dense nonreflection bases and CP.
6. Facial reduction and SDP duality.
7. Sharp source-leakage ambient stability with analytic separation family.
8. Related work, applications/limitations, precise complexity model, reproducibility.

The text should be drafted as one coherent paper, *not* a concatenation of milestones. A separate supplementary proof packet can remain in GitHub, subject to the target journal's policy.

## Non-negotiable verification before submission

- Independent human mathematical audit of the load-bearing identities and inequalities in 02, 06, 07, 08, including arbitrary-rank/singular fibres, the affine-anchor effects on duality, CP on full matrix algebras, exact facial depth, and matching ambient lower bounds. Finite tests are **not proofs**.
- Literature and novelty audit via MathSciNet/zbMATH/arXiv and reference-by-reference inspection. The preliminary targeted web search found related spectrahedral, semidefinite, rank-one sensing, and quantum measurement work but **did not establish novelty** or exhaust prior results.
- A fully runnable, human-reviewed rational/algebraic constructor and deterministic exact invariants; independent referee-style proof reproduction, especially the rational finite-grid nonreflection margin and the all-ancilla norm bounds.
- Explain why the theorem is useful for optimization beyond renaming the constraints: exact quotient universality, dual attainment, complete positivity, stability, and expressiveness boundaries. Distinguish mathematical reduction from a claim of faster SDP solution.
- Do not claim unconditional polynomial-time exact SDP feasibility from conditional trace-certificate discovery. No uniform source-face conditioning is asserted for the full-ambient distance law.
- Verify source authorship, appropriate AI-use disclosure, references, license and reproducibility. Springer Nature policies require human accountability and disclosure of material AI involvement; AI is not an author. See https://www.springernature.com/gp/policies/editorial-policies/ai-manuscript-preparation . SIAM's policy effective May 2026 explicitly requests disclosure and responsibility for all content: https://epubs.siam.org/artificial-intelligence .

## Research provenance and reproducibility

- Original immutable brief/corpus: `ff6117295c329dc88d5bc280ee18adfe64cda8b0`.
- Original positive quotient proof 01–05 on this branch.
- Strengthening proofs 06–08, audit 09; reproducible early and strengthening audit code and recorded outputs.
- GitHub branches and commits are research provenance, **not** substitutes for journal peer review or certified proof check.

**Readiness judgement:** A potentially strong Mathematical Programming (Series A) submission *can be developed from this material*, but the repository contains research manuscripts, not a polished and independently verified submission. Do not submit the milestone files verbatim. Validation and positioning are the gating steps.
