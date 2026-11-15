# Manuscript II — exact status, 15 November 2026

## Mathematical result

The release contains complete internal proofs of a corrected universal theorem, centered on the **canonical arithmetic carrier** of a rational affine Gram fiber. The proofs do not rely on numerical experiments, the reported 2026 boundary counterexamples, or an inaccessible earlier project file.

PROVED IN THE MANUSCRIPT:

1. For any nonempty finite family of closed rational polyhedral column cones and any rational affine matrix fiber, the closure of viable rational column directions is a canonical finite union of closed rational polyhedral cones. At most d=n(n+1)/2 strict matrix-span reductions compute it or certify absence of a rational Gram completion. The reduced domain is unique, not just its feasible matrix slice.
2. Exact rational-fiber preservation, the closure identity, a universal rational reserve completion, rational direction-insertion certificates, and a criterion for every prescribed rational regularization direction.
3. Descent of polyhedrally constrained Gram factors from totally real number fields. Positive weights must be totally positive; positivity at one embedding alone is insufficient.
4. A deterministic exact fixed-dimensional algorithm, with explicitly separated reduction count, component count, bit height, algebraic degree, arithmetic time, and factor width. Standard real-algebraic sampling and elimination are charged algorithmic primitives.
5. Correct partial-observation alternatives, including arithmetic infeasibility, strong real infeasibility, weak infeasibility, and the extra observability condition necessary for observation-supported positive-margin separators.
6. The exact angular correction for every tensor grid of a bounded-moment cone; the optimal real grid, precise rational nonattainment, and rational stereographic grids with exact coefficient 1/(q^2+1).
7. In every n>=4, a fixed nonsimplicial cone with interior rational targets, constant-width rational factors, a fixed full arithmetic carrier, depth zero, and a uniquely forced shadow walk of exactly N-1 adjacent pivots on O_n(log N)-bit input. A fixed integral congruence makes every target entry strictly positive. The proof includes an inverse-polynomial interior radius.
8. Cone-relative lattice conditioning with sharp norm exponent r-1. This builds on the prior Manuscript II orthant theorem and known geometric ingredients; it is not presented as the new flagship contribution.

## What the corrected theorem refutes

The original hope that genuine arithmetic faces, short rational factors, binary interior conditioning, and observation coercivity should force a polynomial adjacent-shadow path is false for the specified rule. The new interior family keeps the carrier and observation condition fixed and still has exponential path length. This does not refute every conceivable invariant or every possible local rule.

An unconditional exact 'rational factor or strictly positive copositive separator' alternative under partial observations is also false. Three situations are kept separate: a real-feasible but arithmetically infeasible fiber; a strongly infeasible image with no observation-supported positive cone margin; and a weakly infeasible nonclosed image.

## Verification actually performed

The separately written verifier imports no generator code. A fresh exact run passed five angular-grid cases, eleven compressed facet certificates, and one arithmetic-obstruction example, and rejected three deliberately corrupted certificates. The complete generated JSON has SHA256:

`ed0b5405a54353b35eaaa65312e77d08d5f1ead1ae41f5a3207ef914fe103117`

The N=2^64 path certificate is not a simulation of its 2^64-1 pivots. Finite checks validate identities and implementation interfaces, not the universal proofs. No independent human review, proof-assistant formalization, or production implementation of arbitrary real-algebraic elimination has occurred.

## Gates not completed

Historical priority of the exact canonical-carrier theorem and its constrained descent consequence is NOT certified. Primary antecedents were inspected and distinguished; several relevant full texts and external 2026 certificates were not completely audited.

The registered twelve-paper LAA comparison remains incomplete and unscored. No upper-20% certification is made. No ten-paper higher-venue comparison, editorial acceptance probability, no-revision assurance, or eight-month decision guarantee is asserted.

The mathematical proof package is complete as a research draft. The broader assignment's historical-priority and publication-benchmark requirements are not declared complete. External expert proof review remains necessary before treating this as a vetted research breakthrough.
