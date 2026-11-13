# Current results — unrestricted SDP universality and conic escape duality

Date: 2026-11-13.
Repository: Harman6139/Posterity-Files.
Branch: laa-track02-gptpro-analytic-frontier-20261112.

The previous MASTER_INDEX.md records the trace-controlled results through 09. This file indexes the continuation beyond trace control and the separate general conic theorem in 12. The statements below are supported by full algebraic proofs in the named manuscripts, not inferred from diagnostic examples.

## 1. Standalone theorem: exact conic escape-profile duality

**12_RECIPROCAL_ESCAPE_LAW_AND_SHARP_DIMENSIONAL_BOUNDS.md**
Proof commit: 2e2f8f75c99f49e4b6e51fad2a37b41891928901.

For a closed pointed full-dimensional convex cone K, e in int K*, and weakly infeasible b for A(K), define

    R_b(delta)=min{<e,x>:x in K, ||Ax-b||<=delta},
    d_b(R)=min{||Ax-b||:x in K, <e,x><=R},
    Q_b(epsilon)=min{||y||:b.y=-1, A*y+epsilon e in K*}.

The exact functional identity is

    d_b(R)=sup_(0<epsilon<1/R) (1-R epsilon)/Q_b(epsilon).

For semialgebraic K the attained positive power exponents of R_b and Q_b are RECIPROCALS. If R_b(delta)~p0 delta^(-a) and Q_b(epsilon)~q0 epsilon^(-beta), then

    a beta=1,
    p0^beta q0=beta^beta/(beta+1)^(beta+1).

For order-m semidefinite systems, m>=2, put E_m=2^(m-1)-1. Every weakly infeasible instance satisfies, for sufficiently small delta and instance-dependent c,C>0,

    c delta^(-1/E_m)<=R_b(delta)<=C delta^(-E_m).

Both exponents are attained by explicit rational bounded-coefficient families at EVERY m. The proof supplies the upper path by a quantitative Schur recurrence on a classical hyper-feasible partition, and obtains the universal lower envelope by applying that construction to the normalized Farkas-dual affine system. This is a sharp envelope, not a full classification of all attainable exponents at a fixed m. The qualitative partition and large-solution phenomena have established antecedents, cited in 12; comprehensive priority is not asserted.

## 2. All-rational two-basis construction

**10_ALL_RATIONAL_TWO_BASIS_COMPILER.md**
Proof commit: 31d40a5bf1100545564830bd70dc069ed4f118c8.

The two complete bases themselves, encoder/decoder coefficients, targets and rational objective pullbacks can ALL be rational, without changing the minimal quadratic matrix order. The new step is the rational Cayley frame

    G=[(I-Q)(I+Q)^(-1), 2(I+Q)^(-1)B], Q=BB^T,

combined with a block-respecting positive congruence of the source lift. It retains the exact source extraction identity. No square-root gates, eigenvectors, algebraic sign decisions or general PSD-completion solver are used in constructing the rational output.

This minimal rational construction uses a reflection pair; it does not also claim all overlaps nonzero, nonreflection, or positive zero-data outcomes. Those were separate features of 08.

## 3. Arbitrary rational SDPs: two bases and exactly one free scale

**11_OPTIMAL_ONE_SCALE_UNRESTRICTED_UNIVERSALITY.md**
Proof commit: cd97bc32a1febc3f37ad3803c7cd582d140cf04d.

For EVERY rational A:S^m->R^p, without trace control or a supplied certificate, construct in polynomial bit time two rational real bases of order

    N=9m^2+4m+5+2p,

and a fixed positive decoder D such that

    D({Y>=0:exists t in R, B_U(Y)=Wb+t v})
      ={X>=0:A(X)=b}

for every datum b. The vector v is strictly positive, and exact lifts have t=trY/c=trD(Y), with 1<=c<=10m^5. The encoder and decoder are completely positive. After explicitly centering and rescaling the two diagonal lists, forward source residuals are isometric and reverse residuals have an explicit polynomial bound valid on the full PSD cone.

The reduction preserves exact, weakly infeasible and strongly infeasible data; all primal and dual objective values; finite primal and dual attainment; unboundedness and recession cones; and the trace-escape exponents of 12. It also admits ancillary-matrix amplification, with the observations correctly interpreted as block-valued at higher levels. The normalized encoder gives a trace-preserving channel with heralded exact recovery probability 1/c>=1/(10m^5), not deterministic recovery.

Two bases and one free scale are necessary and sufficient in the specified datum-uniform positive-linear-decoder model. Fixed complete diagonal lists always give compact PSD fibres and a closed measurement cone, so deleting trace control WITHOUT freeing a scale is impossible. One basis is insufficient because dephasing would make full-PSD-cone singleton recovery factor through a finitely generated PSD cone. No matching lower bound for the quadratic matrix order is claimed.

This is a polynomial-time REDUCTION for exact SDP feasibility, not a polynomial-time DECISION algorithm or a solution to the exact-SDP complexity question.

## 4. Reproducible rational implementation

The unrestricted_rational/ directory contains:

- rational_two_basis.py: exact SymPy constructor and source/target/decoder functions.
- RATIONAL_RESULTS.json: passing exact order-two weak-infeasibility instance and order-one empty-measurement edge case.
- exact_escape_examples.py: exact symbolic endpoint Schur identities and residuals.
- ESCAPE_RESULTS.json: recorded checks at matrix orders 2 through 7.
- README.md: reproduction and input/output conventions.

The proof of every dimension and every rank is in the manuscripts. Finite checks are reproducibility material, not substitutes for those proofs. No historical scripts were rerun merely to generate these new results.

The entire earlier research history remains on the branch, including all original numbered milestones, corrections, proofs 01–09, construction code and recorded outputs.
