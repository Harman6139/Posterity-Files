# Reproducibility and hostile audit

Run AUDIT_NUMERICS.py with Python, NumPy and SciPy. It constructs finite-field sign patterns, verifies pair-character orthogonality, builds exact-covariance positive Parseval frames for commuting annihilators, performs numerical conic support reduction, and checks the signed dilation and its exposing gap.

Small-case results from the fuller independent local audits:

- Hyperplane m=3, K=diag(1,-1,0): five-dimensional measurement span, signed lift N=19 (before symmetry-breaking duplicate and extra pure anchor), frame error 1.6e-16, minimum positive certificate eigenvalue above 2.
- Rationally conjugated dense m=3 hyperplane K=[[32,-6,-30],[-6,-5,24],[-30,24,-27]]/49: span rank 5, signed lift N=20, frame error 3.5e-16.
- Two disjoint m=2 local constraints in m=4: span rank 8, signed lift N=30, frame error 6.7e-16.
- Commuting m=3 with one extra diagonal direction: pre-sparsification 55 columns, 16 retained, compressed span rank 9, signed lift N=31, frame error 8.1e-16, exposing gap above 2.06; a nontrivial pair of positive definite source matrices in the same fibre has encoded residual approximately 2.2e-16.
- Commuting m=5 with two extra diagonal directions: 359 columns before and 64 after sparsification, span rank 34, signed lift N=91, frame error 6.3e-16, exposing gap above 2.06; matching-fibre residual approximately 1.2e-17.
- Commuting m=4, equal diagonal: 48 columns before and 13 after sparsification, span rank 7, signed lift N=28.
- Two-constraint Pauli-type obstruction: K1=diag(1,-1,0,0), K2=e1e2^T+e2e1^T. The allowable projectors lie in a two-dimensional support and span at most three dimensions rather than the eight-dimensional L.

The numerical values test the formulas, not theorem correctness. The formulas in QUADRATIC_DENSE_THEOREMS.md are analytic and independent of these computations.

Specific pitfalls audited:
(1) A shared orthogonal conjugation cannot turn commuting matrices into noncommuting ones. The new block-graph theorem includes noncommutation from missing cross-block edges; the commuting theorem is separate.
(2) Fixed positive auxiliary identity blocks would make the zero target rank >=2 and create square-root instability. We instead use (tr X)I_r, which vanishes at X=0.
(3) A Naimark completion of a short sign frame is not by itself an exact compiler. The proof independently spans all original, cross, and auxiliary matrix directions.
(4) The full-ambient PSD retraction keeps a PSD principal block and never subtracts a Schur complement.
(5) The matched rank-one obstruction only invalidates *bare single-copy rank-one pullbacks*, not arbitrary positive SDP lifts.
(6) Conic sparsification is exact in the algebraic-arithmetic proof; the test script uses floating-point singular vectors and verifies identities only to numerical precision.
(7) Exact polynomial arithmetic-operation counts do not imply uniform Turing bit polynomial complexity for arbitrary nested radical comparisons. Weak approximations need explicit conditioning/separation promises.

For the source mathematical definition, see the pinned brief at prompts/laa_two_basis_significance_20261107/02_UNIVERSAL_STABILITY_TRANSFER.md. The general unrestricted near-quadratic theorem remains unresolved.
