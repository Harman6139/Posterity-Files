# Consolidation audit and publication recommendation

**Date:** 2026-11-12.  
**Repository:** Harman6139/Posterity-Files.  
**Research branch:** research/psd-joint-depth-universal-20261107.  
**Source checkpoint:** b9237b13b0295c37dbe5a1b564d13837c2986a19, plus the uploaded Milestones 139–141 packet.  
**Deliverable:** one self-contained 22-page LaTeX research manuscript, not a new classification program.  
**Status:** internal adversarial proof audit and exact computational reruns. No external referee review, verified human authorship, or worldwide-priority certification is implied.

## 1. Editorial decision

Retain exactly three headline theorems under the title **Rank universality and field-dependent tangency of symmetric cones**.

**A — Rank-universal central and coarse spectra.** For every irreducible symmetric cone, classify central orders and multiplicities jointly with the sharp exponent and minimum facial depth. Extend the coarse statement to arbitrary nonempty affine sections on bounded sets. The fixed-rank real one-switch theorem, multiplicity lift, and positive retraction are one proof, not three unrelated papers.

**B — Complete Hermitian relative-flag spectrum.** For complex and quaternionic PSD cones, classify the central/facial relative-position table, including non-prefix schedules and split grades, with the exact sharp exponent and greedy profile at unchanged rank.

**C — Field dependence after central orders are forgotten.** For all m,r >= 1, exponent 5/27 and profile (m,1,2,2) at nullity m+5 are attainable over F=R,C,H exactly when r dim_R(F) >= 2. This is the sharp boundary to A, not a claim of a universal capacity rule for all data.

The conceptual arc is: coarse tangency is rank-universal; fine exposure can remember the scalar field and source rank; this memory cannot always be removed by changing the central certificate. There is no need to classify every remaining real profile to make these three claims complete.

## 2. Proof dependency audit

The consolidation reconstructs all load-bearing arguments in the manuscript instead of citing an unpublished milestone as a black box. Classical inputs are explicitly identified: Euclidean Jordan algebra identities and classification, finite-dimensional strict separation, semialgebraic Puiseux expansion, and the standard facial error-bound estimate used only in the minimum-rank appendix.

| Dependency | Adversarial issue | Resolution and location |
|---|---|---|
| Singleton compactness | Uniqueness does not imply general metric regularity. | Only K intersect C = {0} is used; strict positive separation bounds residual sublevels. Lemma 3.4. |
| Central path and envelope | A selected arc or center displacement need not control the sharp modulus. | The dual trace identity bounds every ambient competitor. Dikin radius, not center displacement, gives the modulus. Section 3.2. |
| Fixed chart | Eigenvectors can rotate with t. | Successive fixed positive compressions, coefficient rescaling, and the all-competitor envelope give Loewner comparison in a fixed decomposition. No frozen moving eigenbasis. |
| Harmonic necessity | A sparse construction does not prove dense necessity. | The actual central coefficient cannot be downshifted without violating the envelope. Works in arbitrary dense kernels and multiple grades. |
| Hessian comparison | Quadratic representation is not simply assumed order-monotone. | Differentiate determinant covariance and compare on a compact interior normalized chart. Proposition 3.7. |
| Facial lower bound | Chosen coordinate chains may not be minimum. | Actual positive kernel coefficients force survival inside any current face containing a prefix, including rotated ones. |
| Facial upper bound | A compressed separator cannot be freely zero-extended into K-perp. | Use actual full dual Puiseux coefficients and their finite linear combination. |
| Greedy minimum | Maximum rank at one step alone does not justify a shortest chain. | Monotonicity of common zero faces under face inclusion gives an induction against every alternative chain. Lemma 3.2. |
| Real interpolation | Arbitrary schedule interpolation and one-edge increments were false. | One-switch path lengths increase by zero or one; synchronized ownership prevents independent coefficient cancellation. Section 4. |
| Leading-edge collision | Optional pure leading direction may destroy the last stress. | Collision occurs only at the final lower layer; releases are omitted and a separately rescaled tight-anchor stress is proved positive. |
| Multiplicity lifting | Copying scalar stresses can destroy positive definiteness or permit partial exposure. | Use traces for necessity and scaled identity blocks for attainment; redo convex-square dominance with multiplicity factors. |
| Other simple cones | Extra Peirce directions might allow shorter facial reduction. | Positive retraction and orthogonality to the complement of the old maximum support force every new stress into that old support. |
| Gauge reduction | Distance to one solution differs from distance to the set. | Compare distance to the affine hull, repair by mixing with a relative-interior point, and prove the augmented stress component vanishes. The original ungauged central curve is not preserved or claimed preserved. |
| Flag normalization | Congruence changes the identity shift. | Compare both centers by their envelopes; only then use the flag-preserving triangular map. Lemma 5.1. |
| Survivor rules | Repeated grades and non-prefix flags can defeat scalar arguments. | Primal support and dual Schur-complement arguments apply to partial positive blocks; whole current top grade must disappear. |
| Two-component realization | Shared releases or blockers could couple different steps. | Self-release uniqueness, one-stage ownership of source releases, and exact deletion of the sole redundant triple collision. |
| Field separation | A fixed-spectrum obstruction does not exclude replacement spectra. | Determinant 27 forces two graph types; boundary equations give two spectra; all schedules are excluded or forced before invoking the cut obstruction. Section 6. |
| Sharp witness | Bounding a structured curve is not an upper recovery estimate. | Direct arbitrary-competitor inequalities include the necessary sum for b+f; a separate thick curve gives sharpness. |
| Infinite padding | Extra terminal multiplicity might enlarge the low-order cut. | At orders 8/27 and 10/27 all terminal-related entries remain forbidden; the first rank drop fixes the five-internal-grade budget. |

Numbered lemma/proposition references should be read against the compiled manuscript; section names are stable if numbering changes.

## 3. A real correction, not a stylistic change

The original weighted version of the off-face cut-rank lemma in Milestone 139 was overbroad at the terminal weight tau=1. Its proof used the actual central coefficient H_tau as an element of K. This is valid only below order one: at order one only H_1-I belongs to K.

A counterexample to the unrestricted statement is X*=E00 and K=span(R01) in S^2. The center is diag(1+t,t), and E11 is a valid first exposing stress. At the full face every off-face projection is zero, so both cut ranks are zero and no strict jump occurs.

**Repair:** restrict the weighted jump consequence to 0<tau<1. The unweighted positive-circuit lemma itself remains correct. The field-separation theorem uses the internal order 10/27 and is unchanged. The correction is stated in the main proof and Appendix C, and the independent checker records the counterexample. The original note remains in the historical project packet, and this explicit erratum supersedes that sentence. The four finite-minimality witnesses are extracted into the computational supplement; the unrelated product program is not included in the paper.

No additional unresolved logical gap was identified in the retained proof chain during this audit. That is an internal research assessment, not independent specialist certification.

## 4. Primary-literature novelty audit

The relevant comparison is simultaneous sharp realizability, not merely explicit formulas, universality language, or rational exponents. The following primary sources were checked through journal records, author manuscripts, or full-text primary versions. The audit does not certify absence of all worldwide overlap.

| Primary source | Established content that must be credited | Precise distinction in this manuscript |
|---|---|---|
| Borwein–Wolkowicz (1981), DOI 10.1017/S1446788700017250 | Facial reduction and minimal-cone regularization. | Greedy reduction is a tool. The new question is the exact attainable sharp analytic/facial spectrum at fixed rank. |
| Sturm (2000), DOI 10.1137/S1052623498338606 | Guaranteed semidefinite error exponent governed by singularity degree. | A guaranteed 2^-d estimate is not an exact sharp exponent for every instance; A classifies all possibilities and their realizations. |
| Lourenço (2021), DOI 10.1007/s10107-019-01439-3 | Amenable cones and facial residual functions; symmetric-cone error bounds without constraint qualifications. | Extending an error bound to symmetric cones alone is not novel. A identifies exact equality of spectra across simple cone types and unchanged-rank converses. |
| Sremac–Woerdeman–Wolkowicz (2021), DOI 10.1137/19M1289327, especially Theorems 4.4 and 4.7 | The external maximum-determinant family, eigenvalue decay, limiting ranks, and information about singularity degree. | The same family is used. The new assertions give exact harmonic central order lists and multiplicities, their full compatibility with facial tables, and sharp all-competitor error exponents. |
| Basu–Mohammad-Nezhad (2022), DOI 10.1137/21M1419933 | Algebraic description and degree/convergence bounds for SDP central paths. | Puiseux expansions and algebraicity are not claimed new; the path and invariants are specified rather than transferred indiscriminately. Bibliographic correction: this paper is in SIAM Journal on Applied Algebra and Geometry 6(2), 299–318, not SIAM Journal on Optimization. |
| Basu–Mohammad-Nezhad (2024), DOI 10.1017/fms.2024.66 | Effective Łojasiewicz inequalities and error-bound applications. | Rationality and finite real-algebraic decidability do not imply the midpoint restriction, same-rank realization, or field-sensitive profile exclusion. |
| Yu (2015), DOI 10.1090/S0002-9939-2014-12428-2, Theorem 1 | Tropical PSD entry inequalities and positive lifting. | The entry-order inequality is a precedent. The fixed measurement kernel, actual central coefficients, and all facial reductions must be compatible simultaneously here. |
| Allamigeon–Gaubert–Skomra (2018), DOI 10.1016/j.jsc.2017.07.002 | Generic tropical spectrahedra and stochastic games. | Graph/game formulations are not themselves new. The present dense, fixed-rank sharp-exponent/profile realization theorem has different hypotheses and conclusions. |
| Akian–Allamigeon–Gaubert–Sergeev (2025), DOI 10.1007/s10957-025-02732-2 | Signed tropical polar cones and compatibility with signed valuation. | Signed positivity matters, but this is not a ready-made classification of all nested original-real facial profiles with prescribed error order. |
| Wang (2024), DOI 10.1137/22M1531257 | Minimum mediated sets and optimal simple SOC representations of geometric means. | Midpoint networks and representation-size optimization have precedent. The optimized resource here is rank defect at specified sharp exponent and minimum facial depth, not the number of SOC constraints. |
| Blanco–Martínez-Antón (2026), DOI 10.1007/s10957-026-03048-5 | A general mediated-graph framework and extremal graph computation for conic representations. | Do not advertise the invention of mediated graphs. The new content is fixed-kernel tangency and facial synchronization, with an exclusion surviving every replacement central certificate. |
| Hu–Sotirov–Wolkowicz (2023), DOI 10.1007/s10107-022-01890-9 | Symmetry reduction and preservation of singularity degree. | Positive reduction is a precedent. The proof here establishes exactly the invariants needed for cone-type transfer, rather than claiming all geometric lifts preserve profiles. |

The introduction now includes tropical PSD and mediated-set literature. These are substantial omissions in a recovery-only positioning and should not be relegated to a token bibliography entry. The most defensible contribution is the joint arithmetic realization theory together with its sharp field-sensitive boundary.

## 5. Computational audit: actual runs and limits

All three supplied programs were rerun successfully in this session with exact arithmetic:

- One-switch: 225 construction certificates in 17 families.
- General Hermitian tables: 7,572 labelled exponent/schedule certificates, 1,590 split-grade cases, 404 non-prefix cases, and 247,749 generator/stress pairings.
- Field separation: two denominator-27 spectra, explicit complex and real rank-two witnesses, finite profile coverage through nullity five, and ancillary product checks.

A new independent program checks 3,125 anchored Hamiltonian graphs, finding exactly the two determinant-27 types (80 and 40 labelled cases); it solves the two boundary systems independently, checks all 24 witness pairings and all four compressed identity stresses, verifies the unique low-order cut pair, and records the terminal counterexample. It passes.

The all-dimensional theorems rely on their written proofs. The claim that nullity six is the *smallest* separating nullity is separately computer-assisted and confined to the appendix. The manuscript does not need this minimality claim to stand. The original field audit's unrelated product checks remain archival, not headline content.

## 6. What stays out of this paper

Do not add the unrestricted real-profile classification, a general product classification, a two-basis quotient bridge, a large KL-exponent catalogue, or an algorithmic-rate claim. The corresponding open problems do not invalidate A–C. The exact field/source threshold is for the displayed family, not a universal dimension-only criterion.

Long historical routes, finite catalogues, and additional witnesses remain in the repository or supplement. The manuscript uses one analytic foundation, one real interpolation argument, one two-component construction, and one separation proof.

## 7. Journal and submission recommendation

**Transactions AMS first; JLMS a strong alternative.** The contribution is a structural classification plus an exact boundary, rather than a list of examples. Transactions emphasizes correctness, novelty, significance, and substantial mathematical interest; JLMS explicitly makes a motivating introduction understandable outside the immediate specialty part of its criteria. The manuscript is long enough for either journal without artificial padding.

**Advances in Mathematics remains ambitious.** Its significance threshold cannot be inferred from the number of milestones or by attaching more applications. An independent expert assessment of the three-theorem package is the appropriate basis for an Advances decision.

Primary editorial sources checked November 12, 2026:
- Transactions AMS journal guidance, DOI 10.1090/TRAN/8986 and the AMS journal information page.
- JLMS submission page: https://www.lms.ac.uk/publications/jlms/submission
- LMS AI policy, updated October 2026: https://www.lms.ac.uk/publications/policies/AI
- Advances in Mathematics official aims and scope, Elsevier/ScienceDirect.

LMS requires an AI Declaration identifying tools/models and contributions to ideas, calculations, proofs and writing, and access to substantial computational materials. The draft includes a truthful provisional declaration but does not invent the complete model history or human verification. The submitting authors must finalize it and take responsibility for all claims. No submission has been made.

## 8. Publication-readiness assessment

The mathematical argument is consolidated, the internal cut-lemma gap is repaired, the primary comparisons are stated, the exact programs pass, and the PDF compiles without unresolved references or overfull boxes. This is the strongest coherent **pre-submission research manuscript** produced in this session.

The remaining gates are author verification, independent specialist proof review, final bibliographic/priority assessment, and final disclosure/metadata. These are not invitations to prolong an open-ended classification project. No claim of external acceptance, a completed referee audit, or guaranteed journal placement is made.
