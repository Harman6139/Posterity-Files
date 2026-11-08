# LAA Paper — Research Track 02: canonical GitHub index and status ledger

Last updated: 2026-11-08. Current working branch: **laa-track02-unrestricted-quadratic-20261108**.

**Share THIS document with the project lead**. It links the original research brief, earlier dense-quadratic branch, all subsequent milestones and the remaining unsolved question. The upstream main branch is NOT the current research branch. The link is stable by branch and path; each update has a separate immutable commit hash in Git history.

## Canonical locations

- Repository: https://github.com/Harman6139/Posterity-Files
- Current active research branch: https://github.com/Harman6139/Posterity-Files/tree/laa-track02-unrestricted-quadratic-20261108
- Current active milestone directory (00 archive plus 23 numbered milestones): https://github.com/Harman6139/Posterity-Files/tree/laa-track02-unrestricted-quadratic-20261108/research/laa_two_basis_track02_20261108
- Previous dense-quadratic research directory, inherited into this branch: https://github.com/Harman6139/Posterity-Files/tree/laa-track02-unrestricted-quadratic-20261108/research/laa_two_basis_track02_20261107/dense_quadratic
- Original pinned research brief, inherited into this branch: https://github.com/Harman6139/Posterity-Files/blob/laa-track02-unrestricted-quadratic-20261108/prompts/laa_two_basis_significance_20261107/02_UNIVERSAL_STABILITY_TRANSFER.md
- Earlier separate branch: https://github.com/Harman6139/Posterity-Files/tree/laa-track02-quadratic-dense-20261108
- Earlier brief branch: https://github.com/Harman6139/Posterity-Files/tree/laa-significance-three-pro-20261107
- Local canonical overview / update destination: MASTER_INDEX.md (THIS FILE).
- Local theorem ledger / newest work destination: numbered XX_*.md files in this folder.
- Code and audits: see the dense_quadratic folder and original conversation attachments; individual newer analytic no-go results do not require numerical evidence.

## The actual unresolved north star

For arbitrary rational trace-controlled A:S^m->R^p, prove or disprove a polynomial-conditioned reduction to TWO orthonormal-basis PSD measurements of order N=O(m^2+p), preserving arbitrary-rank approximate recovery, feasible-set geometry and SDP objectives under positive decoding.

**Status: OPEN in this research.** There is no unconditional near-quadratic construction or architecture-independent superquadratic impossibility theorem. Several strong CONDITIONAL lower bounds and explicit special-class quadratic constructions have been proved. Do not tell a referee or project lead that the unrestricted problem is solved.

## Chronology from beginning of Track 02

### Stage 0 — original sharp transfer and early constructive universality (chat + archival notes)

- **00_EARLY_GRAPH_TRANSFER_ARCHIVE.md:** self-contained reconstruction of the first all-ambient sharp graph-transfer theorem, including the PSD retraction, invisible cross-block lower bound, zero-target exception, and nonsingleton extension. This was added so the original mathematical result is not stranded solely in conversation text.
- Original Track 02 research starts from an exact graph-completion embedding in the 25-page LAA manuscript. The first research response established an all-ambient reflection modulus law: omega_lift(t) ~ omega_graph(t)+sqrt(t) for nonzero targets, with a rank-one zero-target exception. A cross-block injectivity criterion describes when the added square-root term vanishes.
- The next continuation developed general tensor-purification rank-one compilers with order O(m^4), positive partial-trace decoding and the same sharp non-Lipschitz modulus transfer. This was substantially more general than graph completion.
- A subsequent effort investigated explicit algebraic conditioning, non-reflection basis rotations and a deterministic O(m^4) compiler. The width-adaptive companion construction improved this to O(m^2(w+1)^2), where w is the diagonal-cover width, and to O(m^2) for bounded-width systems. The complete prior companion memorandum is summarized in the dense_quadratic directory on this branch.
- Historical scripts/artifacts available in the original conversation may not all have been committed individually; refer to the original ChatGPT conversation for exact early response prose. This index and the later committed memoranda preserve their mathematical results and provenance, not necessarily every sentence or artifact.

### Stage 1 — dense structured quadratic theorems (the dense_quadratic directory)

- QUADRATIC_DENSE_THEOREMS.md: exact rank-plus-one quadratic construction for arbitrary dense codimension-one measurement spaces; commuting annihilators; block-graph spaces with noncommuting dense constraints.
- RIGIDITY_OPEN_QUADRATIC_THEOREM.md: rank matrix criterion and nonempty open families of dense noncommuting spaces for s<=floor(m/2), with N roughly m²/2+O(m).
- CODIMENSION_TWO_UNIVERSAL_THEOREM.md: every codimension-two system has a fixed sixfold real purification and N<=36m²+24m, even with no allowed single-copy rank-one measurements.
- RATIONAL_OBSTRUCTION.md: rational trace control does not always imply a rational single-copy rank-one frame.
- AUDIT_NUMERICS.py, AUDIT_README.md and RESULTS.json: independent finite-dimensional consistency checks, which are NOT proofs.

### Stage 2 — unconditional versus architecture-restricted lower bounds (numbered files in this directory)

01. GENERIC_TENSOR_LOWER_BOUND — generic tensor ancilla Omega(m), hence N=Omega(m^4) in the tensor-face architecture.
02. DIAGONAL_COMPANION_LOWER_BOUND — a positive principal-block lift has forced XB cross blocks, and generic diagonal companions have quartic order.
03. PARSELVAL_VS_ADMISSIBLE_BASIS — exact positive rank-one Parseval cone criterion; a Parseval system may have no admissible ONB. The inertia statement explicitly requires nonsingular stress weights.
04. POSITIVE_RETRACT_JORDAN_RIGIDITY — faithful normalized positive left inverses force a Jordan matrix amplification.
05. FAITHFUL_DECODER_QUARTIC_LOWER_BOUND — generic quartic lower bound for faithful positive-linear decoders.
06. FULL_CLASSIFICATION_POSITIVE_LINEAR_RETRACTS — every globally positive linear retract is congruent to (X tensor I_t) direct-sum a positive matrix-valued companion.
07. GENERIC_SUPERQUADRATIC_LOWER_BOUND_POSITIVE_RETRACT — generic N=Omega(m^(8/3)) for exact full-fibre positive-linear retracts.
08. AFFINE_ANCHOR_NO_GO_EXTENSION — the same bound survives a fixed positive affine anchor.
09. SURJECTIVE_KRAUS_SLACK_TRADEOFF — generic many-to-one CP quotient representations satisfy a parameter/slack inequality; N=O(m²), Kraus t=O(m) forces Omega(m⁴) decoder-invisible auxiliary dimensions.
10. CP_ENCODER_KRAUS_LOWER_BOUND — generically CP data-faithful encoders need Kraus rank >=(1-1/sqrt(2)-o(1))m.
11. APPROXIMATE_TO_EXACT_CLOSURE_THEOREM — all-tolerance fixed-design sound and complete weak recovery implies exact surjectivity.
12. VARIABLE_DESIGN_COMPACTNESS_AND_CONDITIONING — uniformly controlled tolerance-varying designs have exact surjective accumulation points.
13. UNCONDITIONAL_QUADRATIC_AFFINE_ISOMORPHISM_LOWER_BOUND — generic exact affine isomorphisms of spectrahedra require N=Omega(m²) without positive-encoder assumptions.

### Stage 3 — new quadratic shadows and exact measurement-geometry obstructions

14. UNIVERSAL_SINGLE_BASIS_MARGINAL_SHADOW — every bounded PSD source fibre has an exact order-2m² POSITIVE marginal shadow with one maximally entangled basis and arbitrary extra source observables. This is a HYBRID normal form, NOT two bases.
15. SYMMETRIC_EXTENSION_ESCAPES_POSITIVE_RETRACT — order m(m+1)/2 symmetric-square marginal has positive CP decoder and exact surjectivity to ALL density matrices but provably NO globally positive linear right inverse.
16. SYMMETRIC_EXTENSION_NO_BASIS_DIAGONAL — that smallest symmetric-square shadow cannot even satisfy one full fixed-basis diagonal while surjecting onto all density matrices, because its pure-state lifts are unique.
17. TWO_MASA_COMMUTING_COMPLETION_CRITERION — an operator space lies in two MASA spans iff diagonal corrections make generators commute. **CORRECTION:** for FIXED first basis, these conditions are LINEAR, not quadratic; see Milestone 20.
18. PURE_STATE_LIFTS_MUST_BE_MIXED — any real fixed-diagonal PSD fibre mapping onto the entire density-body requires mixed input lifts for all but finitely many source pure states.
19. TWO_BASIS_TRACE_CONE_QUADRATIC_SHADOW — GENUINE two-basis order N=2m² trace-only universal quotient, both lists strictly positive, all basis overlaps nonzero, CP positive Lipschitz decoder and Theta(m⁴) auxiliary slack. Does not impose nontrivial source measurements.
20. TWO_MASA_LINEAR_TEST_AND_MAXENT_NO_GO — polynomial-time linear system deciding two-MASA inclusion for a fixed first basis; a dimension-independent commutator inequality proves that the maximally entangled first basis CANNOT be completed by any second basis to detect two noncommuting source observables via partial trace. The reproducible diagnostic TWO_MASA_LINEAR_TEST.py is in this directory.

### Stage 4 — universal two-basis dilation without an admissible orthonormal basis

21. TWO_ZERO_BASIS_UNIVERSAL_FRAME_DILATION — any supplied d-dimensional rank-one Parseval measurement compiler of M vectors admits an exact two-basis PSD dilation of order N=2M-d, with a positive isometric decoder and rank preservation, requiring NO admissible ONB in the original operator system. The two bases can have no zero overlaps. The exact support is exposed by complementary zero observations; N=2M-d is dimension-optimal within this zero-only exposing architecture for two M-vector frames. The full-ambient noisy bound is omega_lift(delta)<=omega_source(C sqrt(delta))+C sqrt(delta), not the previously sharp omega_source(delta)+sqrt(delta). It cannot be advertised as strictly-positive-observation or exponent-preserving universality. AUDIT_TWO_ZERO_NAIMARK.py tests the tetrahedral d=3,M=4,N=5 instance whose operator system has no admissible ONB.

### Stage 5 — newer stability and first-order obstruction results

22. TRANSVERSE_EXPOSING_DILATION_STABILITY — a finite-dimensional cross-image transversality condition for arbitrary PSD face-exposing measurements gives O(delta) recovery of compressed measurements from all ambient PSD competitors. If an invisible support-to-exterior cross block exists, a same-rank PSD quadratic curve gives the matching sqrt(delta) lower bound. A small audit correction was committed to the output projection used in the decoder.
23. DOUBLE_ZERO_FIRST_ORDER_NO_GO — the cross-image map of the two-zero Naimark dilation has rank M-c(P), where c(P) counts connected components of the Gram projector support graph. For a connected Gram graph, source trace-free data overlap the first-order cross image, so the linear transversality condition of Milestone 22 fails for all nontrivial source signals; a quadratic-residual cancellation curve shows the potential extra square-root instability is real.

**Status after Milestone 23:** Milestone 21 solves exact two-basis dilation of arbitrary Parseval frames without a permitted ONB but allows zero target measurements and does NOT generally preserve non-Lipschitz moduli sharply. Milestone 23 explains this loss. Unrestricted N=O(m^2+p) positive-data, condition-faithful two-basis universality remains UNSOLVED.

### Stage 5 — exact noise diagnosis and positive-data removal of the ONB obstruction

22. TRANSVERSE_EXPOSING_DILATION_STABILITY — an arbitrary exposed PSD face has sharp source-residual O(delta) transfer whenever its compressed-output and cross-block-output spaces have positive principal-angle separation. Under an invisible target-support cross direction the full ambient modulus is omega_source(t)+sqrt(t); no reflection assumption is needed. A corrected projection/inverse formula is recorded in commit history.
23. DOUBLE_ZERO_FIRST_ORDER_NO_GO — for a Parseval frame G, the cross-data map X -> diag(G^T X K) has exact rank M-c(Gamma), where Gamma is the graph of nonzero off-diagonal entries of P=G^T G. For connected Gamma, cross data fill the trace-zero source output in both bases, and the transversality margin in Milestone 22 vanishes whenever dim W>1. An explicit PSD Schur-repaired curve hides O(t) source variations behind O(t²) data, showing the first-stage square-root loss can be real.
24. POSITIVE_TWO_BASIS_UNIVERSAL_FRAME_COMPOSITION — compose the exact double-zero ONB dilation (Milestone 21) with a signed-anchor lift of its intermediate TWO-BASIS measurement space. This gives all STRICTLY POSITIVE final observations, no zero overlaps, positive decoding, exact all-rank PSD fibre equivalence, rank amplification exactly one, and genuine nonreflection design at order N<=10M-5d+4 for ANY supplied d-dimensional M-vector rank-one Parseval compiler, even with no admissible source ONB. Quantitative source modulus is bounded between omega_source(c t) and C omega_source(C sqrt(t))+C sqrt(t); it does NOT preserve all non-Lipschitz exponents. Numerical audit AUDIT_POSITIVE_FRAME_COMPOSITION.py verifies a d=3,M=4->n=5->N=29 example with positive lists and exposing gap >2.

### Stage 6 — a sharp quantitative no-go for the zero-exposure route

25. TWO_ZERO_TRANSVERSALITY_DIMENSION_BARRIER — for ANY minimal zero-only exposing two-basis realization of independent Parseval frames G,H, the source data separable from first-order off-face cross terms have dimension at most c(G)+c(H)-1<=2d-1, where c is the number of components of each frame's Gram-support graph. If dim of the source rank-one projector span exceeds this threshold, a Schur-complement-repaired PSD curve at every positive-definite source point has decoded source residual Theta(t) but two-basis measurement residual Theta(t²). Thus the O(sqrt(delta)) loss in Milestones 21/24 cannot generically be repaired by linear data processing. This no-go is restricted to zero-only exposure, not all two-basis designs.

### Stage 7 — sharpness breakthrough: universal stabilized Parseval-frame transfer

26. SHARP_UNIVERSAL_PARSEVAL_FRAME_TRANSFER — **SHARPNESS PROBLEM SOLVED** for any supplied finite real rank-one Parseval compiler. Given G of order d with M nonzero columns, its Naimark enlargement to n=M has a balanced Parseval frame consisting of coordinate vectors e_j, PURE-SOURCE vectors P e_j and PURE-EXTERIOR vectors h_a. These source-only projectors measure the original source data without FIRST-ORDER contamination from the Naimark exterior; the exterior-only projectors control the remaining PSD mass. Applying ONE signed-anchor two-basis dilation gives N<=6M-d+4, all observations strictly positive, all basis overlaps nonzero, positive linear decoding, objective identity, exact full feasible-set correspondence, rank amplification +1, and the exact full-ambient modulus law omega_final(t) ~ omega_source(t)+sqrt(t) for every nonzero source datum (zero source remains Lipschitz). In particular ALL non-Lipschitz moduli are preserved and attained exponents transform as min(alpha_source,1/2), with no alpha/2 degradation. This construction needs NO admissible ONB in the ORIGINAL operator system. For generic source SDP spaces, combine with the earlier codimension-adaptive tensor frame compiler to get sharp transfer at order O(m²(s+1))<=O(m^4). The generic O(m²+p) dimension conjecture is STILL FALSE in the strong exact positive-retract model and unresolved in weaker quotient models. Independent script AUDIT_SHARP_PARSEVAL.py and numeric results AUDIT_SHARP_PARSEVAL_RESULTS.json test the tetrahedral d=3,M=4,N=25 example.

The first-stage zero-only rate loss of Milestones 21/23/25 is a flaw of THAT particular measurement architecture, **not a universal cost of lacking an admissible ONB**. Milestone 26 replaces it by a source-only/exterior-only balanced compiler and repairs the loss. The second-stage composition of Milestone 24 is a valid but now superseded less-sharp construction.

## Current best mathematical understanding

- General O(m^4) exact positive-retract two-basis universality with sharp non-Lipschitz modulus transfer: established in earlier Track 02 work.
- Full O(m²) or N<=36m²+24m exact positive-retract lifts for broad structured or codimension-two spaces: established in committed dense_quadratic proofs.
- Genuine O(m²) surjective TWO-BASIS quotient with gigantic auxiliary slack: established for the TRACE-ONLY source case (Milestone 19). This proves the escape mechanism is geometrically realizable, but it does not encode arbitrary noncommuting source constraints.
- Symmetric-square quotient: exact universal PSD shadow without a positive linear section (Milestone 15), but impossible as a fixed-basis diagonal fibre even for trace-only data (Milestone 16).
- Maxent-first-basis hybrid: universally handles marginal source constraints as separate observables, but the two-MASA commutator no-go blocks replacing them by one second ONB whenever source operators fail to commute (Milestone 20).
- Unrestricted universal N=O(m²+p) two-basis quotient with efficient robust positive decoder: still UNSOLVED. Milestone 21 removes the admissible-ONB bottleneck at the price of zero observations and potentially slower recovery; Milestones 22-23 characterize a transversality route and prove why it fails generically in the two-zero construction. None evade the generic quartic lower bounds for strong positive retracts.
- Strong exact positive retract N=O(m²+p) universal theorem: FALSE for generic dense instances by Milestones 07-08, which show N=Omega(m^(8/3)).
- No claim of unconditional exact SDP feasibility polynomial time or generic rational ONBs without algebraic conditioning promises.

## Recommended reading sequence for the lead

1. This MASTER_INDEX.md.
2. CODIMENSION_TWO_UNIVERSAL_THEOREM.md and RIGIDITY_OPEN_QUADRATIC_THEOREM.md in dense_quadratic for positive quadratic constructions.
3. 06_FULL_CLASSIFICATION_POSITIVE_LINEAR_RETRACTS.md, then 07_GENERIC_SUPERQUADRATIC_LOWER_BOUND_POSITIVE_RETRACT.md and 09_SURJECTIVE_KRAUS_SLACK_TRADEOFF.md for sharp scope of negative results.
4. 15_SYMMETRIC_EXTENSION_ESCAPES_POSITIVE_RETRACT.md, 16_SYMMETRIC_EXTENSION_NO_BASIS_DIAGONAL.md, 19_TWO_BASIS_TRACE_CONE_QUADRATIC_SHADOW.md and 20_TWO_MASA_LINEAR_TEST_AND_MAXENT_NO_GO.md, and 21_TWO_ZERO_BASIS_UNIVERSAL_FRAME_DILATION.md, 22_TRANSVERSE_EXPOSING_DILATION_STABILITY.md and 23_DOUBLE_ZERO_FIRST_ORDER_NO_GO.md for the newest approach, stability criterion, and precise obstruction.
5. The original pinned brief and the LAA manuscript before making publication or novelty claims.

## Update convention for future research turns

Use the SAME active branch and THIS directory. Add sequentially numbered XX_DESCRIPTIVE_NAME.md (next free number: 24) for each newly verified milestone, amend older files when an audit finds a correction, and update this MASTER_INDEX.md with scope and remaining gaps. Use GitHub commit history for provenance and versioned changes. This plan is a path convention, not a claim that work will continue automatically in the background.

Every statement is self-audited rather than externally peer-reviewed; numerical checks are supporting diagnostics only. No manuscript-ready novelty or publication-priority certification is asserted.
