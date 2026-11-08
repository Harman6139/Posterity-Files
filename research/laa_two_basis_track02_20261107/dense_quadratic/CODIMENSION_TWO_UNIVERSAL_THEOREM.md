# Complete quadratic-size two-basis universality for EVERY codimension-two PSD measurement space

Track 02 new theorem, 2026-11-07/08. Complete analytic proof in real symmetric setting; independent external refereeing and exhaustive priority audit have not occurred.

## 1. The theorem

Let A:S^m -> R^p be a real trace-controlled linear measurement map with m>=2. Normalize by a fixed positive-definite congruence so I_m belongs to L=range(A*), and assume codim(L)=2. Thus L^perp=span{K_1,K_2}, with K_a real symmetric, linearly independent, and traceless.

**Theorem.** There exist finite algebraic matrices F in R^{(6m+1) x N} and U in O(N), and positive linear encoding and decoding maps, such that
  N <= 36m^2+24m,
  E(X)=F^T((X tensor I_6) direct-sum [1])F,
  D(Y)=(1/6) partial_trace_ancilla((FYF^T)_{1:6m,1:6m}),
and for every feasible b,
  {Y>=0:A_U(Y)=Phi(b)}=E({X>=0:A(X)=b}),
  D(E(X))=X,
  rank E(X)=6 rank(X)+1,
  ||E(X)-E(Z)||_F=sqrt(6)||X-Z||_F.
Every entry of U is nonzero and every encoded observation is strictly positive. The bases can be made genuinely different, with U not equivalent to a symmetric reflection under independent signed permutations.

Every original linear cost C is represented exactly by
  C_tilde=F^T(((C tensor I_6)/6) direct-sum [0])F,
giving <C_tilde,Y>=<C,D(Y)> for EVERY symmetric ambient Y.

For every feasible b, including nonsingleton fibres, the worst-case PSD recovery moduli satisfy, with finite explicitly computable fixed-instance constants,
  omega_tilde_b(t) ~ omega_b(t)+sqrt(t)  if b != 0;
  omega_tilde_0(t) ~ t.
In particular every non-Lipschitz recovery modulus is preserved up to positive constant factors, and any nonzero Lipschitz source acquires exactly a square-root ambient modulus. All estimates hold against unrestricted-rank ambient PSD matrices.

The construction uses at most polynomially many algebraic matrix operations and finite rational orthogonal rotations. The orbit-search algorithm below is randomized Las Vegas with expected polynomial arithmetic-operation complexity, provided exact algebraic rank/equality tests are available. This is NOT an unconditional polynomial Turing bit-complexity theorem: uniform numerical conditioning requires explicit singular-value, algebraic separation and trace-normalization promises.

The theorem includes the Pauli-type codimension-two obstruction, where NO nonzero original-coordinate rank-one projectors have measured pullbacks. Six-dimensional real purification repairs that obstruction without requiring commutativity, graph structure, or a simultaneous real hollowizing basis.

## 2. The rectangular Stiefel rank-one span lemma

Write V=R^m tensor R^r and let T:S^{mr}->S^m be the unnormalized partial trace. For B>=0 with support E of dimension k<r, consider the compact orbit of rank-one projectors
  P_B={ vec(V)vec(V)^T : V in R^{m x r}, V V^T=B }.

**Lemma.** If a symmetric W in S^{mr} annihilates every projector in P_B, then its compression to E tensor R^r equals H_E tensor I_r, for a symmetric H_E on E with <H_E,B>=0.

Proof. Choose a factorization B=A A^T with A:E -> R^k invertible. Every V with VV^T=B has the form V=A Q where Q in R^{k x r}, QQ^T=I_k. Replace W by its congruent compression to R^k tensor R^r. Decompose it into r-by-r blocks W_ij. If
  sum_{i,j} q_i^T W_ij q_j=0
for every ordered orthonormal k-frame of row vectors q_i, independently reversing signs of rows i,j shows q_i^T W_ij q_j=0 for every q_i perpendicular to q_j. Therefore W_ij is scalar I_r for i!=j.

For a diagonal block W_ii, fix the other k-1 rows orthogonal to an arbitrary two-plane in R^r, possible because r>=k+1, and vary q_i in that plane. Its quadratic form is constant on the unit circle in every two-plane, so W_ii is scalar I_r. The coefficients h_ij constitute a symmetric H with tr H=0. Undoing the congruence produces H_E tensor I_r and <H_E,B>=0. This proves the lemma. For k=1 the same diagonal-block argument applies.

## 3. A general codimension-adaptive purification theorem

The following intermediate lemma applies to ANY codimension, not just two.

Let L subset S^m contain I and have codimension s. Put
  r_0 = max{k>=1:k(k+1)/2 <= s+1},
  r=2r_0+1,
  d=mr,
  W_L={S in S^d:T(S) in L}.
Then there exists a positive Parseval rank-one frame G=(g_j) in R^d whose projectors span EXACTLY W_L.

**Extreme-rank reduction.** The compact base C={X>=0:X in L,tr X=1} has an interior point I/m relative to L. Every extreme point A of C has rank <=r_0: if its support has rank k and k(k+1)/2>s+1, a nonzero supported symmetric perturbation lies in L and has trace zero, so A+/-epsilon H both lie in C. This is the elementary Barvinok--Pataki rank argument.

Moreover a PSD B in L can be expressed as a positive sum of <=m PSD matrices of rank <=r_0 by a finite rank-reducing algorithm. To construct one low-rank A supported inside B, repeatedly move along a nonzero supported traceless H in L to a PSD singular endpoint; rank strictly decreases, so after at most m steps A has rank <=r_0. Subtract from B the largest scalar multiple c A preserving PSD. The residual is still in L and has strictly smaller rank. Repeating at most m times gives B=sum_i c_i A_i. All steps are nullspace solves and generalized eigenvalue endpoints in a fixed real algebraic field.

Choose a basis I,H_1,...,H_h of L, h=dim L-1, and small eta>0 such that I+/-eta H_j are PSD. Decompose these matrices into low-rank pieces. The resulting finite collection C_1,...,C_t of rank<=r_0 PSD matrices spans L. Choose epsilon>0 small so
  B_0=I-epsilon sum_{j=1}^t C_j
is positive definite and belongs to L. Decompose B_0=sum_{i=1}^{u} p_i A_i into rank<=r_0 pieces, u<=m. The supports E_i=range(A_i) span R^m because B_0 is positive definite.

For every i include the singleton A_i; for every i<j include the pair sum A_i+A_j (rank<=2r_0<r); include the supplementary C_j singles. Give the pairs small positive coefficients zeta and reduce each A_i coefficient by (u-1)zeta, retaining positivity. The resulting weighted list {B_v,c_v} has:
  c_v>0, rank(B_v)<r, sum_v c_v B_v=I,
  the singleton B_v span L,
  the supports of the initial A_i span R^m,
  and every pair sum A_i+A_j appears with positive coefficient.

For each B_v choose a purification V_v in R^{m x r}, V_v V_v^T=B_v. Consider all its right-orthogonal orbits vec(V_v O)vec(V_v O)^T. The total span across these orbits equals W_L.

To prove the last assertion, let W annihilate every orbit. By the rectangular lemma its compression to (E_i+E_j) tensor R^r has only an ancilla-scalar part, for every initial support pair i,j. Let H=T(W)/r and W_0=W-H tensor I_r. Every compression of W_0 to these paired supports is zero. Since the initial E_i span R^m, bilinearity gives W_0=0 globally. Thus W=H tensor I_r. Singleton orbit annihilation now gives <H,C_j>=0 and <H,A_i>=0 for all i,j, so H in L^perp. Conversely every H tensor I with H in L^perp annihilates the orbits. Therefore their projector span is (L^perp tensor I_r)^perp=W_L.

**Positive Parseval realization.** For a fixed purification V and Haar O in O(r),
 E[vec(V O)vec(V O)^T]=(B tensor I_r)/r.
A finite exact second-moment twirl is obtained from cyclic coordinate permutations and rows of a Sylvester Hadamard sign matrix (include a reflected copy if needed): a set G of <=4r^2 rational orthogonal matrices satisfies the identical average formula for every V.

For each B_v, choose finitely many base rotations R_1,...,R_h and include the entire twirl orbit {V_v R_t G:G in G}. Each twirl block has covariance (B_v tensor I)/r. Positive weights c_v r/(h |G|) make their combined covariance c_v B_v tensor I, independent of which rotations were chosen. Consequently the union over v is exactly Parseval. Its projector span is W_L once sufficiently many base rotations have been selected, by the proved full-orbit span identity.

**Effective finite rotation selection.** Take a rational planar rotation with cos(theta)=3/5, sin(theta)=4/5. Its powers are dense in SO(2), since theta/pi is irrational; its conjugates in all coordinate planes generate a dense subgroup of SO(r). Together with a reflected twirl element this is dense in O(r), so an enumeration of rational rotation words must eventually span every full orbit. The stopping criterion rank=dim W_L is exact finite linear algebra.

One can also obtain an expected-polynomial algebraic-arithmetic algorithm: sample rational Cayley rotations R(T)=(I-T)(I+T)^(-1), with independent skew entries uniform in {0,...,8r}. If the current projector span is deficient, some B_v and some annihilator H have a nonzero quadratic orbit coefficient <H,vec(V_v R(T)G)vec(...)^T>. After multiplication by det(I+T)^2 its numerator is a nonzero polynomial of degree <=2r. By Schwartz--Zippel, each trial for that B_v increases the span with probability >=3/4. Cycle through all polynomially many B_v types until rank dim W_L; expected number of accepted blocks is O(dim W_L), and expected total trial count polynomial in m,s. Each accepted whole twirl block preserves exact covariance, and discarded non-increasing blocks need not be kept.

Finally, apply conic Caratheodory sparsification: reserve half the weight of dim W_L independent projector columns, and conically reduce the remaining positive identity representation to at most dim W_L columns. This leaves at most
  M<=2 dim W_L = 2[d(d+1)/2-s]
Parseval columns with full projector span.

This gives a general positive rank-one POVM compiler with amplification r=O(sqrt(s+1)), one-sided positive decoder rho(W)=T(W)/r, and quantitative residual equivalence controlled by the positive singular values of its finite analysis matrix. It is NOT, by itself, a two-basis dilation for arbitrary s: existence of an admissible orthonormal basis in the amplified space is a separate step.

## 4. The special codimension-two admissible orthonormal basis

For s=2, the extreme-rank bound gives r_0=2. The span theorem therefore holds for r=5, and hence also r=6. We take r=6 specifically to construct an admissible real orthonormal basis.

Let A=K_1+i K_2 be the traceless complex m-by-m matrix. The Toeplitz--Hausdorff convexity theorem implies the numerical range W(A) is convex and contains the average of its eigenvalues, 0. Therefore some complex unit vector psi has psi* A psi=0. Compress A to psi^perp; its trace is still zero. Induction produces a complex orthonormal basis psi_1,...,psi_m with
  psi_j* K_1 psi_j=psi_j* K_2 psi_j=0.
This is the classical unitary zero-diagonal theorem (not an originality claim).

Write psi_j=a_j+i b_j with real vectors a_j,b_j. The 2m real vectors
  vec([a_j,b_j]), vec([-b_j,a_j])  (j=1,...,m)
form an orthonormal basis of R^{m x 2}. Their rank-one partial traces are a_j a_j^T+b_j b_j^T, orthogonal to K_1,K_2. Make three disjoint copies in the six auxiliary coordinates, yielding 6m real orthonormal vectors, every one of whose projectors belongs to W_L.

Thus BOTH prerequisites for the signed anchored two-basis dilation are available: a rank-one Parseval frame of length <=2dim W_L spanning W_L and a complete admissible orthonormal basis of R^{6m}.

## 5. Signed anchoring and exact two-basis fibres

Set d=6m, q=dim W_L=d(d+1)/2-2. Apply the explicit signed anchored dilation in the preceding Track 02 memorandum:

- three columns a u_i,c u_i,c u_i of signed weights -1,2,3 for each admissible basis vector u_i;
- one h g_j column of signed weight 4 for each Parseval frame vector;
- nonzero small anchor entries solving both FF^T=I and FDF^T=0;
- three pure-anchor columns of weights -1,2,4 and one duplicated weight-4 frame column.

Here h=1/10, a^2=(5+3h^2)/7 and c^2=(1-5h^2)/7. The dyadic/rational-grid anchor choice avoids every off-diagonal inner-product cancellation and every diagonal column norm squared equal to 1/2. All target observations are positive because the source tensor is PSD and the anchor contributes positively.

The reflection R=2F^TF-I has the explicit measured positive exposing certificate
  S_0=D+RDR=2QDQ>=2Q,  Q=I-F^TF,
since the D-isotropic compressed subspace has dimension d+1, exactly the negative inertia of D, and positive weights are at least 2. Rotate one weight-4 duplicate against the pure-anchor weight-4 coordinate, setting U=R O_phi. Since O_phi D O_phi^T=D, the certificate is unchanged. The retained duplicate preserves the compressed projector span. A sufficiently small generic phi makes U nonreflection under independent signed permutations while maintaining strictly positive data and no zero overlaps.

The compressed measurement span is exactly the anchored extension of W_L (all arbitrary source-anchor crosses and anchor scalar, with top matrix in W_L). The exposing certificate forces every exact PSD competitor into range(F^T), and the span identity then forces its compressed matrix to be
  (X tensor I_6) direct-sum [1], X in F_b.
Thus the complete ambient fibre equals E(F_b), for feasible singleton or nonsingleton fibres and arbitrary ambient competitor rank.

The rank, Frobenius and objective formulas in the theorem follow from FF^T=I, partial-trace positivity, and the direct calculations
 ||X tensor I_6||_F=sqrt(6)||X||_F,
 rank[(X tensor I_6) direct-sum 1]=6 rank X+1,
 <(C tensor I_6)/6,W>=<C,T(W)/6>.

The dimension is
  N<=3d+2q+4 = d^2+4d = 36m^2+24m.

## 6. Full-ambient sharp modulus law

Let Y>=0, delta=||A_U(Y)-Phi(b)||. Put P=F^TF and Q=I-P. The certificate forces tr(QYQ)<=kappa delta, kappa=||diag D||_2/sqrt(2). Trace measurement bounds tr Y by T_b, so ||PYQ||_F<=sqrt(kappa T_b delta). For every coordinate untouched by the two-coordinate rotation, the average of the first- and second-basis residuals cancels PYQ and QYP EXACTLY; the retained duplicate restores the lost source measurement. Consequently the compressed rank-one residual is bounded linearly in delta.

Let B=(FYF^T)_{1:d,1:d}>=0, and define X=rho(B)=T(B)/6>=0. Since the compressed frame projectors span W_L, the map B -> (B-J(X), A(X)-b) has the same kernel as the frame residual. Finite-dimensional linear inversion therefore supplies explicit computable constants c_1,c_2 (using the least positive singular value gamma_ret of the retained analysis matrix), with
 ||B-J(X)||_F<=c_1 delta, ||A(X)-b||_2<=c_2 delta.
Anchor cross and anchor scalar discrepancies are O(delta). Thus
 ||Y-E(X)||_F<=C_1 delta+sqrt(2kappa T_b delta),
 dist(Y,E(F_b))<=sqrt(6) omega_b(c_2 delta)+C_1 delta+sqrt(2kappa T_b delta).
Embedded competitors supply omega_tilde_b(t)>=sqrt(6) omega_b(t/C_2) for a fixed computable C_2.

For b!=0, every source feasible C has rank>=1 and E(C) has rank>=7. Select two positive support eigenvectors; their cross blocks into Q have dimension 2(N-d-1), exceeding N constraints (the first diagonal's zero-sum equations and one additional rotated equation) since N>2(d+1). Hence a nonzero K=R_*KQ exists whose linear variation has zero measurements in BOTH bases. The curve
 Y(t)=E(C)+t(K+K^T)+t^2 K^T E(C)^dagger K
is PSD and has the same rank as E(C), since it admits an exact Gram factorization. Its measurement residual is Theta(t^2) and its distance from every encoded feasible matrix (supported on P) is >=sqrt(2)t||K||. Therefore omega_tilde_b(t)>=c sqrt(t).

At b=0, the source fibre is {0}. The encoded target is the rank-one positive anchor, whose coordinate vector has no zero entries. The compressed error and exterior mass are O(delta); PSD block inequalities control all non-anchor cross blocks by O(delta), and the first diagonal detects the remaining anchor-to-exterior cross block linearly through entrywise multiplication by the nonzero anchor vector. Thus omega_tilde_0(t)=Theta(t).

The standard PSD tangent-cone dichotomy shows that each source modulus is either Lipschitz or at least square-root. Therefore omega_tilde_b(t)~omega_b(t) for every non-Lipschitz source fibre, with all estimates valid against arbitrary ambient PSD competitors.

## 7. Scope, computation, and hostile audit

This theorem removes the codimension-two obstruction COMPLETELY for dimension: every dense/noncommuting two-constraint missing-measurement space admits a quadratic-size two-basis lift. It does not extend unrestricted quadratic universality to arbitrary codimension s. Part 3 supplies a new general rank-one compiler with ancilla r=O(sqrt(s+1)), but there is not yet a universally justified admissible ONB and exposing certificate for s>=3 at that amplification.

The finite frame is explicitly computable in the exact algebraic arithmetic model: low-rank PSD decomposition by supported nullspace/eigenvalue endpoints, exact rational Cayley samples, rational finite twirls, verifiable rank stopping, and conic sparsification. With supplied positive conditioning gaps, weak numerical approximations and decoding have polynomial cost. The polynomial arithmetic-operation count is NOT a claim of uniformly polynomial Turing bit complexity for rational input without algebraic separation and trace-conditioning promises.

Audit conditions: all-rank ambient competitors handled; all auxiliary surrogates stay PSD by partial trace; no hidden alpha/2 loss because the even residual cancels cross blocks; no assumption that all C=L intersect PSD is rank-one-generated (rank-two extreme points are permitted); the rectangular lemma requires r strictly larger than every pair rank; r=6 satisfies this uniformly; realification of complex hollowization yields actual REAL orthonormal vectors; the positive twirl frame and its span are independently verified; and zero data are treated separately because a fixed positive auxiliary anchor alone has rank one.

Small-case tests in CODIM2_PURIFICATION_AUDIT.py demonstrate the complete rank-one span for the Pauli case m=2 (rank 76=dim W_L) and for m=3 Pauli constraints with coupled free coordinates (rank 169=dim W_L). Parseval errors are <=7e-15 before sparsification. These checks do not replace the analytic proofs.

Priority inputs: the Toeplitz--Hausdorff numerical-range theorem, elementary Barvinok--Pataki extreme-point rank bounds, real Stiefel frame identities, finite signed Hadamard twirling and the previous Track 02 signed exposing reflection. The new combined codimension-two full-cone transfer theorem and codimension-adaptive rank-one compiler are candidate original contributions subject to external literature review.
