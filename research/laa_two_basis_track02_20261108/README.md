# Track 02: unrestricted two-basis SDP normal form — new rigorous bounds and exact scope

Updated: 2026-11-08. Branch: laa-track02-unrestricted-quadratic-20261108.

The unrestricted target "construct N=O(m^2+p) for EVERY rational trace-controlled SDP with a quantitatively faithful two-basis recovery normal form" remains **UNRESOLVED** when one permits nonunique auxiliary feasible points, positive decoders of unbounded complexity, or nonlinear/tolerance-dependent encodings. An architecture-independent impossibility theorem is also not established.

This branch contains 13 mathematical milestones. Below, m is the original PSD matrix order, p the number of independent measurements, and N the two-basis order. s denotes the original affine fibre dimension, not the number of measurements.

| File | Verified conclusion | Scope |
| --- | --- | --- |
| 01_GENERIC_TENSOR_LOWER_BOUND.md | Generic tensor-purification frames require ancilla Omega(m), N=Omega(m^4) | Tensor-face class only |
| 02_DIAGONAL_COMPANION_LOWER_BOUND.md | Positive principal-block encoders have forced XB cross blocks; generic diagonal companions yield N=Omega(m^4) | Diagonal companion |
| 03_PARSELVAL_VS_ADMISSIBLE_BASIS.md | Exact rank-one POVM cone criterion; positive Parseval frame may have no admissible ONB | Real operator systems |
| 04_POSITIVE_RETRACT_JORDAN_RIGIDITY.md | Faithful decoder portion is a Jordan amplification | Positive linear retracts |
| 05_FAITHFUL_DECODER_QUARTIC_LOWER_BOUND.md | Generic faithful positive retracts require N=Omega(m^4) | Faithful positive decoder |
| 06_FULL_CLASSIFICATION_POSITIVE_LINEAR_RETRACTS.md | Every positive linear retract is congruent to (X tensor I_t) direct sum T(X), T positive | All globally positive linear retracts |
| 07_GENERIC_SUPERQUADRATIC_LOWER_BOUND_POSITIVE_RETRACT.md | Generic N=Omega(m^(8/3)) | Exact full-fibre positive-linear retract |
| 08_AFFINE_ANCHOR_NO_GO_EXTENSION.md | Same lower bound with PSD affine anchor | Positive affine retract |
| 09_SURJECTIVE_KRAUS_SLACK_TRADEOFF.md | Generic many-to-one projections satisfy (D_d-s-a)(d-1)+tmd >=g; N=O(m^2), t=O(m) implies a=Omega(m^4) | Surjective exact CP decoder of rank t |
| 10_CP_ENCODER_KRAUS_LOWER_BOUND.md | Generic data-faithful CP encoder must have Kraus rank at least ~0.2929m | Completely positive encoding |
| 11_APPROXIMATE_TO_EXACT_CLOSURE_THEOREM.md | Fixed-design all-tolerance weak recovery implies exact surjective fibre | Fixed design/decoder |
| 12_VARIABLE_DESIGN_COMPACTNESS_AND_CONDITIONING.md | Uniformly sound tolerance-varying designs have exact surjective limit; inherits big slack requirement | Bounded data/decoder, CP rank |
| 13_UNCONDITIONAL_QUADRATIC_AFFINE_ISOMORPHISM_LOWER_BOUND.md | Generic exact affine-isomorphic two-basis representation requires N=Omega(m^2) | Arbitrary affine isomorphisms |

## Central strict-feasibility and dimension formulae

Let D_m=m(m+1)/2, choose s=floor(D_m/2), ell=D_m-s, and take generic L=range(A*) of dimension ell containing I_m. The source fibre F_b at b=A(I_m) has dimension s and a positive-definite point.

The input Grassmannian has dimension
  g=(ell-1)s=Theta(m^4).

For an ambient two-basis fibre T with minimal face order d, q-dimensional compressed measurement span W, and CP decoder D(Y)=sum_{a=1}^t B_a Y B_a^T satisfying D(T)=F_b, let
  a=dim(ker M intersect ker D)=D_d-q-s
be auxiliary-fibre dimension. Then generic exact surjective representations with fixed parameter bounds require
  (D_d-s-a)(d-1)+tmd >=g,
  D_d-s-a=q<=2N-1.
This is the strongest *general many-to-one* tradeoff proved in the branch. It excludes quadratic-size systems with both low Kraus rank and small auxiliary slack, but not all quadratic-size systems.

For globally positive affine exact retracts, the positive map classification removes encoder/decoder parameters and strengthens the generic lower bound to N=Omega(m^(8/3)). With a faithful decoder the stronger Omega(m^4) lower bound applies.

Even without any positive encoder or decoder, exact affine ISOMORPHISM of the full source and target feasible sets implies compressed LMI order d>=m from the irreducible degree-m determinantal algebraic boundary, and hence N>=Omega(m^2).

## Why this does not solve the unrestricted quadratic question

There remain three qualitatively different possible escapes:

1. A many-to-one exact projection with **Omega(m^4) decoder-invisible affine auxiliary dimensions** inside a compressed PSD face of order Omega(m^2), and a low-Kraus-rank decoder.
2. A compact order-O(m) compressed fibre with an essentially maximal-Kraus-rank CP decoder (or a positive but non-CP decoder).
3. A nonlinear, b-dependent, non-face or tolerance-dependent construction lacking a uniform positive linear right inverse.

The above lower bounds do not eliminate these regimes. Nor has a construction been proved for them.

## Mathematical standards / corrections

- Theorem 03's inertia obstruction explicitly requires NONSINGULAR diagonal weights; a zero-weight counterexample is recorded.
- All lower bounds distinguish affine full-fibre bijections from many-to-one projections, and globally positive maps from positivity only on a given feasible fibre.
- Source and target relative interior are used to justify tangent identities; no fixed-rank competitor restriction is hidden.
- No new theorem claims polynomial-time solvability of exact SDP feasibility or unconditional polynomial-bit algebraic coefficient separation.
- Theorems rely on elementary projective determinantal incidence, positive-map Jordan rigidity (proved directly), semialgebraic parameter counting, and in Theorem 13 classical Bertini irreducibility (hypotheses checked).
- Proofs are self-audited and committed. External referee verification, comprehensive novelty audit, and a universal O(m^2+p) construction have not been completed.

Recommended next independent target: test whether a high-Kraus-rank CP quotient of two-basis fibres of order O(m^2) can realize generic dense operator systems with a polynomially controlled decoder; in parallel, seek a lower bound on auxiliary slack that is architecture-independent.
