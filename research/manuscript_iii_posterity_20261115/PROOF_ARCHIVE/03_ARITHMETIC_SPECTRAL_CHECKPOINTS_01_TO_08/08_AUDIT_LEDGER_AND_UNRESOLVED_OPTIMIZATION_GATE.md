# Checkpoint 08 — proof audit and the exact unresolved gate

Date: 2026-11-15. Parent checkpoint-07 correction: 1e0d70c38fa9ff29f6b496160d52dffa90967356. Verification code: 10c3cb3f9541429090b7c2d07260a84d5f8f9ac5.

## Corrections and interpretation controls

1. In checkpoint 07, the extreme-mixed-inertia recovery theorem is for m>=2. This is automatic for weakly infeasible PSD systems, but must be explicit in its broader matrix-identification formulation. At m=1, the alternative k=m-1 is zero and cannot recover an inactive scalar inequality. The standalone manuscript states m>=2.
2. The first version of checkpoint 07 misstated the illustrative order-three determinant as -t_2. The corrected file proves det X=-t_2-4t_1^3, crossing at t_2=-4 when t_1=1, with null vector (2,-2,1) and crossing derivative 1/9. The incorrect version is retained only in Git history. The general irreducibility and escape proofs did not use it.
3. The oracle coordinates, not only the underlying affine matrix image, count as rational input data. No real hidden chart is relabeled rational.
4. The algebraic probe has bounded Euclidean norm but potentially enormous algebraic degree. Its construction is effective and height-independent; it is not a polynomial-bit or polynomial-time algorithm. Exact real comparisons and unlimited offline computation are essential.
5. Spectral recovery means recovery of the ordinary characteristic polynomial and the natural objective, not unique recovery of an isospectral coefficient representation.
6. Theorem 07B needs a common probe with one negative or one positive eigenvalue. A known small index-one ball is explicitly supplied for the arrow examples. No such ball is assumed to be known for every weakly infeasible pencil.
7. Theorem 07C is a sufficient spectral/Galois criterion. The Moser coefficients can vanish; neither all intermediate inertias nor all reducible squared spectra are classified. Matrix-algebra irreducibility is not a substitute for irreducibility over Q(x).

## Exact finite verification

The local run of verification/verify_results.py used SymPy 1.14.0 and passed 286 exact checks: rational direction Gram matrices, characteristic/determinant identities, small irreducibility checks, all displayed finite Schur certificates, the corrected crossing, Moser coefficient/generating identities, a subset-sum ambiguity, and positional-code separations. No numerical eigenvalue threshold is used to certify a theorem.

These are finite diagnostics, not a proof of the quantified general statements and not independent external peer review. The general proofs are written separately. No second independent researcher or theorem prover has certified the manuscript.

## Historical audit already changes attribution

The subset-sum inversion in checkpoint 07 is classical. Fomin's primary surveys arXiv:1709.06046 and arXiv:1903.04062 explicitly attribute the coefficient formula and nonvanishing recovery criterion to the classical multiset-recovery literature, including Gordon--Fraenkel--Straus (1962). That formula and its Newton-identity proof are not claimed as new.

Effective real quantifier elimination, Kronecker substitution, Eisenstein irreducibility, Riesz spectral projectors, Galois field traces and the analytic identity theorem are also established tools. The candidate contribution is their specific combination into natural-PSD-distance germ decoding, isometric inertia extraction, and spectral recovery across inactive branches, together with the conic examples and sharp identification separations. Historical priority for that combination remains provisional pending a fuller literature audit.

The prior arbitrary-query-to-block-Krylov argument is established methodology, as the 2026 matrix-vector-complexity paper by Derezinski, Epperly and Meyer explicitly credits Chewi et al. It is not rebranded as a new matrix-information invariant here.

## Why the main theorem has not been closed

The new results establish important subclasses in which rational exact information is much stronger than ordinary iterative progress. They do not supply a universal optimizer for arbitrary rank-changing rational pencils. Conversely, the n-bit construction gives a sharp GLOBAL IDENTIFICATION lower bound but has a common zero-query approximate solution. It therefore cannot prove the requested OPTIMIZATION lower bound.

A positive full solution still needs a single polynomial-encoding rational prior whose optimization-relevant inactive branches remain concealed for T arbitrary exact queries and an arbitrary final output, with the common all-scale escape bounds. It must evade both the connected-regular-locus mechanism and the algebraic spectral-reconstruction mechanisms.

A negative full solution still needs a uniformly budgeted algorithm for the residual cases: reducible spectra, unrecovered intermediate subset sums, and separating rank barriers whose ambiguity affects small-objective locations. Enumeration of all candidates is not by itself a query bound, and the chamber-count bound can be too large to defeat the proposed minimax rate.

No tested construction or proof in this branch meets either obligation yet. The full exact-rational minimax frontier is neither proved nor disproved.

## Publication gate

The fixed sample is twelve SIOPT articles (first six research articles from each of 35(3),35(4), 2025) and ten MOR articles (first five from each of 50(3),50(4), 2025). Main results and accessible proof sections are being compared with explicit access/version labels. Abstract-only inspection is not full-proof review.

Regardless of those comparisons, the essential requested theorem is missing. No upper-quintile classification, acceptance probability, submission-readiness, or eight-month publication assurance is justified. The manuscript being prepared is a standalone research draft of the structural partial results, with the original frontier displayed as unresolved.