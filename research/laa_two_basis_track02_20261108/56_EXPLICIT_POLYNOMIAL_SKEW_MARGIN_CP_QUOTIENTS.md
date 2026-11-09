# Milestone 56 — EXPLICIT POLYNOMIAL skew-sector conditioning for ALL real CP quotients of the PSD cone

Track 02, 2026-11-09. Substantial quantitative strengthening of Milestone 55. Its previously nonconstructive compactness conclusion is replaced by an explicit universal lower bound from Welch's spherical frame inequality and pure-state Stinespring fibres. The result is self-contained, holds with any finite Kraus rank, and remains meaningful for nontrace-preserving CP maps through the smallest positive Kraus-stack singular value. Combined with Milestone 54 it forces an EXPLICIT non-Jordan commutator defect for any CP quotient that makes a generically rich source measurement operator space readable from only two basis diagonals.

## 1. Sharp input assumptions and theorem

Let m>=2, N>=1, and let
  D:S^N→S^m,  D(Y)=sum_(a=1)^t B_a Y B_a^T
be a real COMPLETELY POSITIVE map with t>=1 Kraus operators, not necessarily trace preserving. Form the real stacked Kraus linear map
  V:R^N→R^m⊗R^t,
  Vx=sum_a B_a x⊗e_a,
and let s_V=sigma_min^+(V)>0 be its smallest NONZERO singular value.

Suppose D(S^N_+) contains EVERY real rank-one PSD output ray: for each nonzero u in R^m there is some PSD Y_u with D(Y_u)=uu^T.

Let Phi(T)=V^T(T⊗I_t)V be the canonical real Kraus adjoint extension to skew and all real matrices.

**Theorem 1 (explicit singular-value floor).** For EVERY real skew T,
  ||Phi(T)||_op
    >= s_V² * sin(pi/(t+2))/(t sqrt(m)) *||T||_F.   (1)
Therefore
  sigma_skew(Phi)
    >= s_V² * sin(pi/(t+2))/(t sqrt(m)) >0.          (2)

If D is TRACE PRESERVING on the entire symmetric cone, then V^T V=I_N, hence s_V=1 and
  sigma_skew(Phi)
    >=sin(pi/(t+2))/(t sqrt(m)).                     (3)

Using sin(pi/(t+2))>=2/(t+2) for t>=1 yields the elementary rational bound
  sigma_skew(Phi)>=2/[t(t+2)sqrt(m)]                 (4)
for every trace-preserving real CP cone quotient. All bounds hold for ANY choice of Kraus representation, with its corresponding t and s_V.

## 2. Proof by a rotation-plane packing and Welch bound

Fix a nonzero skew T, and normalize first to ||T||_F=1. By the real skew-symmetric spectral theorem, T has an invariant oriented two-plane with orthonormal e1,e2 and
  e1^T T e2=lambda!=0,
where lambda is the LARGEST positive rotation frequency. Since the nonzero frequencies occur as +/- i lambda_j,
  1=||T||_F²=2 sum_j lambda_j²
    <=m lambda².
Thus lambda>=1/sqrt(m).

Choose n=t+1 unit source vectors in this plane at angles
  theta_j=j*pi/(t+2), j=1,...,t+1,
  u_j=cos(theta_j)e1+sin(theta_j)e2.
For all i!=j the skew pairing is
  |u_i^T T u_j|=lambda |sin(theta_j-theta_i)|
             >=lambda sin(pi/(t+2)).
Indeed the angle difference is k*pi/(t+2) with integer 1<=k<=t and the minimum sine over those differences is sin(pi/(t+2)).

By pure-output surjectivity and positivity, the Stinespring product fibre
  K_u={w∈R^t:u⊗w∈ran V}
is NONZERO for every u, as proved in Milestone 55. Choose a UNIT vector w_j∈K_(u_j).

Apply the elementary Welch frame inequality to these t+1 unit vectors w_j in R^t. Their (t+1)-by-(t+1) Gram matrix G has rank<=t, diagonal entries one and trace t+1. By Cauchy–Schwarz on its nonzero eigenvalues,
  tr(G²)>=(trG)²/t=(t+1)²/t.
Writing tr(G²)=(t+1)+sum_(i!=j)|w_i^T w_j|² shows that some pair i!=j satisfies
  |w_i^T w_j|>=1/t.                                    (5)
(This is sharp for a regular simplex frame.)

For each j, the product vector u_j⊗w_j lies in ran V. Choose its minimal-norm preimage
  x_j=V^dagger(u_j⊗w_j).
Then Vx_j=u_j⊗w_j and
  ||x_j||<=1/s_V,
because ||u_j⊗w_j||=1.

For the pair i!=j from (5), using Phi(T)=V^T(T⊗I_t)V gives
  |x_i^T Phi(T)x_j|
   =|u_i^T T u_j| |w_i^T w_j|
   >=lambda sin(pi/(t+2))/t.
The operator norm inequality gives
  |x_i^T Phi(T)x_j|
    <=||Phi(T)||_op ||x_i|| ||x_j||
    <=||Phi(T)||_op/s_V².
Combining the two displays and lambda>=1/sqrt(m) proves (1) for normalized T. Homogeneity proves it for general T, and ||Phi(T)||_F>=||Phi(T)||_op proves (2).

If D is trace preserving, sum_a B_a^T B_a=I_N, hence V is an ISOMETRY and s_V=1, giving (3). The elementary sine inequality sin x>=2x/pi for 0<=x<=pi/2 gives sin(pi/(t+2))>=2/(t+2), proving (4). QED.

## 3. Quantitative consequence for two-basis SDP decoders

Let L⊂S^m satisfy gamma_4(L)>0 from Milestones 49/53 (generic source spaces containing I already with dimL>=m+3, m>=4). Let D:S^N→S^m be a real CP decoder whose PSD cone image contains every real PSD rank-one ray, and let Phi=D* be its real Kraus adjoint extension. Suppose two real ONB diagonal spaces D1,D2 satisfy
  Phi(L)⊂D1+D2.

The general channel commutator-defect inequality from Milestone 54 gives
  delta_comm(Phi;L)
    >=gamma_4(L)*sigma_skew(Phi)
         sqrt[(m(m−1)/2)/(N(N−1))].
Inserting (2) yields the FULLY EXPLICIT positive bound
  delta_comm(Phi;L)
    >= gamma_4(L)*s_V²*sin(pi/(t+2))/t
         *sqrt[(m−1)/(2N(N−1))].               (6)
For a CPTP cone quotient s_V=1, and the rational version is
  delta_comm(Phi;L)
    >= 2 gamma_4(L)/[t(t+2)]
         *sqrt[(m−1)/(2N(N−1))].               (7)

Every real CP map S^N→S^m admits a real Kraus form with t<=mN in a standard Choi decomposition. Therefore, at N=poly(m), (7) gives an inverse-POLYNOMIAL lower bound in m and N TIMES the original commutator margin gamma_4(L). It prevents a proposed polynomially conditioned universal two-basis CP quotient from approaching a Jordan-homomorphic decoder too closely while retaining full pure-state surjectivity.

This is a condition-controlled NONREVERSIBILITY obstruction, not a general impossibility for quadratic two-basis normal forms: a channel with sufficiently large commutator defect may satisfy the necessary bound, and a source F_b containing no pure states does not trigger the pure-cone-surjectivity hypothesis by itself.

## 4. Scope and hostile audit

- The proof selects t+1 source directions whose pairwise skew pairings are ALL nonzero and have a UNIFORM trigonometric lower bound; it does not merely use the finite-dimensional impossibility of t+1 pairwise orthogonal ancilla vectors.
- Welch's inequality is proved from the rank/trace of an explicit Gram matrix. Its constant 1/t is exact for t+1 unit vectors in R^t.
- The minimal-norm Kraus-stack preimage accounts for nontrace-preservation and any nontrivial kernel of V; its norm <=1/s_V is the ONLY additional conditioning loss.
- For CPTP maps V is an isometry, making the polynomial lower bound independent of the individual Kraus matrices, channel conditioning or any compactness constants.
- The bound on lambda_max(T)>=||T||_F/sqrt(m) is valid for real skew matrices because their nonzero singular values occur twice.
- The output norm is OPERATOR norm, so the Frobenius skew singular-value statement follows without additional dimension factors.
- The inverse-polynomial assertion holds as a function of t<=mN; gamma_4(L) may still be arbitrarily small for ill-conditioned rational source measurement spaces.
- Theorem 1 applies to each Kraus realization, not just the minimal Kraus rank one; choosing the minimal representation gives the strongest t-bound for CPTP maps.
- The channel need only hit ALL rank-one output rays as PSD cone points. No positive linear right inverse, nonlinear witness regularity, trace-one normalization or two-ONB hypothesis is used in the main theorem.
- The two-basis consequence requires exact operator inclusion of Phi(L) in the measured two-MASA span, as implied by soundness at a full-rank lifted feasible point. Singular lifted supports and more general positive non-CP decoders escape this argument.
