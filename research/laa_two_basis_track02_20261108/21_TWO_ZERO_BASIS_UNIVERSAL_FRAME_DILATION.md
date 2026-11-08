# Milestone 21 — a two-orthonormal-basis dilation for EVERY rank-one Parseval compiler, without any admissible ONB

Date 2026-11-08. This is a proved general construction for exact PSD feasible fibres using TWO bases and potentially ZERO observed entries. It removes the admissible-ONB obstruction of Milestone 03, at a controlled cost in noisy error exponents. It is **NOT** a full solution to universal near-quadratic stability-preserving two-basis normal forms with positive observations: the dimension of the underlying rank-one compiler still matters, and the general noisy upper bound may evaluate the source modulus at sqrt(delta).

## 1. Main theorem (double-zero Naimark dilation)

Let d>=1 and let G=[g_1 ... g_M] in R^{d x M} be a rank-one Parseval analysis frame:
  GG^T=I_d,
  span{g_j g_j^T}=W <= S^d,
  g_j !=0 and ||g_j||<1 for every j,
  M>d.
(The last two strict conditions can be enforced by replacing every frame vector g by two copies g/sqrt(2), without changing the span, tightness, or the associated inverse problem.)

Let M_G(Z)=(g_j^T Zg_j)_{j=1}^M. Fix any nonempty PSD fibre
  F={Z>=0: M_G(Z)=c},
and assume its residual-bounded PSD sets are compact; Parseval tightness already guarantees this because sum_j g_j^T Zg_j=tr Z.

Then there exist TWO real ONBs B1,B2 of R^N with
  N=2M-d,
and an isometric linear face embedding
  E(Z)=F_0^T Z F_0, F_0=[G,0_{d x(M-d)}],
such that the complete unrestricted-rank PSD fibre of their measured target data is EXACTLY E(F):
  {Y>=0: A_U(Y)=A_U(E(Z_*))}=E(F)
for any chosen Z_* in F.
The two measured lists on E(Z) are
  (M_G(Z),0_{M-d}) and (0_{M-d},M_G(Z))
in a suitable output ordering.
The transition matrix U may be chosen with ALL entries nonzero (despite some observations being zero), and is generically nontrivial/non-involutory.

The decoder D(Y)=F_0 Y F_0^T is globally positive and satisfies D(E(Z))=Z. For every source cost C, the ambient cost F_0^T C F_0 satisfies
  <F_0^T C F_0,Y>=<C,D(Y)>
for every symmetric ambient Y. Frobenius distances along E are exactly preserved, and rank E(Z)=rank Z.

## 2. Explicit bases and exact fibre proof

Complete the rows of G to an orthogonal M-by-M matrix:
  [G;K] in O(M), with K in R^{(M-d) x M}, KG^T=0.
Write z=M-d>0, N=M+z, and let
  P=G^T G (M-by-M projection),  Q0=K^T K=I_M-P.
Identify R^N=R^M direct-sum R^z. The embedded source support is
  V=ran(F_0^T)={(G^T x,0):x in R^d}.
Use the standard basis as B1. Its last z vectors lie in V^perp, and their target outcomes are zero.

Define the initial second ONB as the columns of the explicit N-by-N orthogonal matrix
  U_0 = [ [K^T, P],
          [0_(z x z), K] ],
where its first z columns span Z_2=ran(K^T) direct-sum {0} subset V^perp, and its remaining M columns are
  u_j=(P e_j,K e_j).
Check U_0^T U_0=I_N directly: P²=P, K K^T=I_z, KP=0 and P+K^T K=I_M. For j=1,...,M,
  F_0 u_j=G P e_j=Ge_j=g_j,
whereas F_0 U_0 e_a=0 for a<=z. Thus on E(Z), the second target list is (0_z,M_G(Z)), as claimed.

The first-basis zero outcomes force Y>=0 to have its range in
  E_1=R^M direct-sum {0};
the second-basis first z zero outcomes force its range to be orthogonal to
  E_2=ran(K^T) direct-sum{0}.
Their intersection is exactly V. (For any PSD matrix, a zero quadratic form along v implies Yv=0, by Y^{1/2}v=0.) Therefore every exact ambient competitor is E(Z) for a unique Z>=0. Both lists then force M_G(Z)=c, proving the complete fibre identity with NO fixed-rank or singleton assumptions.

## 3. Nonzero basis overlaps by rotation on the exterior

The initial U_0 has a structurally zero z-by-z lower-left block. We can eliminate every zero overlap without changing any compressed measurement or exact fibre.

Let Q=I_N-F_0^T F_0 be the orthogonal projector onto V^perp (dimension 2z), and let W_R=I_V direct-sum R be the orthogonal map acting as identity on V and as R in O(2z) on V^perp. Set U_R=W_R U_0.

Every compressed second basis vector is unchanged, since F_0 W_R=F_0. The second zero subspace becomes W_R E_2. The FIRST zero subspace remains E_0={0}_M direct-sum R^z. For R sufficiently close to the identity, the positive certificate
  S_R=P_(E_0)+P_(W_R E_2)
has kernel precisely V and satisfies
  S_R >= (1/2)Q.
At R=I, the two zero spaces are orthogonal and S_I=Q; the bound follows for small R by the operator norm continuity of projectors.

Every coordinate first-basis vector has nonzero V^perp component, because ||g_j||<1 for j<=M and the final z coordinates lie in V^perp. Every second-basis vector has nonzero V^perp component: for the first z it lies wholly there, while the last M have Q component (0,K e_j) of positive norm, again since ||g_j||<1. Consequently, for every fixed first and second basis column pair (i,j), the analytic function
  R -> <e_i,W_R U_0 e_j>
is not identically zero on any neighbourhood of I in SO(2z). It is a fixed scalar plus the inner product of two nonzero exterior vectors under R, and a nonconstant rotation varies the latter (2z>=2). Each zero set is thus a proper real-analytic subset; finitely many such zero sets cannot cover a neighbourhood of I. Choose R there. Then ALL entries of U_R are nonzero. Rational Cayley rotations give algebraic approximations, and exact finite polynomial avoidance gives a rational R whenever G is algebraic.

This proves the nonzero-overlap assertion without any admissible ONB inside W.


## 3b. Sharp ambient order for zero-only two-list exposure

Suppose a target support V of dimension d in R^N is exposed SOLELY by zero outcomes: the first basis has z_1 zero-outcome vectors and M_1=N-z_1 surviving vectors, while the second has z_2 zeros and M_2=N-z_2 survivors. If the spans of all zero-outcome vectors together equal V^perp (which is necessary for the zeros alone to force support V against arbitrary PSD competitors), then
  N-d=dim V^perp <=z_1+z_2=2N-M_1-M_2,
so
  N>=M_1+M_2-d.
Our more general construction, using any two allowed Parseval frames of sizes M_1 and M_2 (complete their row isometries independently), realizes equality N=M_1+M_2-d: put their orthogonal-complement directions in complementary, initially orthogonal subspaces of V^perp. The explicit symmetric case M_1=M_2=M from Section 2 has N=2M-d. Thus the dimension bound is EXACTLY optimal among zero-only exposing constructions with these two surviving-frame lengths. This statement does not constrain signed certificates with strictly positive observations.

## 4. Explicit full-ambient quantitative bound

Let delta=||A_(U_R)(Y)-A_(U_R)(E(Z_*))||_2 with Y>=0 and delta<=1. Write
  T=tr Z_*+sqrt(N).
The measured nonnegative zero-coordinate outcomes give
  <S_R,Y> <=sqrt(2z)delta.
Using S_R>=(1/2)Q, we obtain the explicit exterior-mass estimate
  tr(QYQ)<=kappa delta,  kappa=2sqrt(2z).
As trY<=T, PSD block Cauchy-Schwarz gives
  ||F_0^T F_0 Y Q||_F <=sqrt(T kappa delta).
Consequently
  ||Y-E(D(Y))||_F <=kappa delta+sqrt(2T kappa delta).      (1)
In particular D(Y)>=0.

The first-basis nonzero diagonal entries are M_G(D(Y)) plus the diagonal of Y-E(D(Y)). Therefore
  ||M_G(D(Y))-c||_2
   <= delta+kappa delta+sqrt(2T kappa delta).              (2)
Let omega_G be the worst-case PSD distance-to-fibre modulus for M_G and omega_lift for the two-basis fibre. Then
  omega_lift(delta)
   <= omega_G((1+kappa)delta+sqrt(2T kappa delta))
      +kappa delta+sqrt(2T kappa delta),                 (3)
with full-ambient arbitrary PSD competitors.
Conversely each embedded Z>=0 satisfies
  ||A_U(E(Z)-E(Z_*))||_2=sqrt(2)||M_G(Z)-c||_2,
  dist(E(Z),E(F))=dist(Z,F),
so
  omega_lift(delta)>=omega_G(delta/sqrt(2)).             (4)

Thus every source exponent alpha<=1 transfers to at least alpha/2 and at most alpha. For the zero datum, trace itself gives a Lipschitz bound, so the zero fibre retains exponent one. Formula (3) is NOT claimed sharp in general: unlike the earlier signed-reflection construction, the two noisy lists do not necessarily cancel source/exterior cross blocks to first order.

This is a precise tradeoff: it removes the orthonormal-basis existence obstruction at the cost of zero target observations and potentially an additional square-root conditioning loss.

## 5. Consequences for codimension-adaptive purification

In Milestone CODIMENSION_TWO_UNIVERSAL_THEOREM.md (previous dense_quadratic directory), Part 3 constructs for arbitrary measurement spaces L containing I a rank-one Parseval compiler in
  d=m r,  r=2r_0+1,  r_0=max{k>=1:k(k+1)/2<=s+1},
where s=codim L, with M<=2dim W_L and W_L={S:partial_trace S in L}.

Apply the double-zero dilation to that compiler (duplicating nonzero frame columns first if needed). One obtains for EVERY such real PSD problem an exact two-basis representation without having to construct a permissible ONB in the amplified tensor space. The resulting order is
  N <=4 dim W_L-d =4[d(d+1)/2-s]-d =2d²+d-4s
before optional frame duplication to guarantee strict column norms; after duplication a safe universal bound is N<=8dim W_L, hence
  N=O(m²(s+1)).
For each FIXED codimension s this is quadratic in m, even for arbitrarily dense, noncommuting constraints and without simultaneous hollowization.

These are exact-fibre statements with zero observed entries and the quantitative bounds of Section 4. They do NOT establish the sharp modulus-preserving O(m²) construction for generic s=Theta(m²), nor strict positivity of every target observation, nor polynomial uniform Turing bit complexity absent conditioning promises.

## 6. Hostile audit and novelty scope

- Both bases are honest complete real orthonormal bases, not two arbitrary POVMs or a hybrid with extra linear observables.
- First/second zero data expose complementary directions in the exterior. Rotating inside the exterior keeps their sum strictly positive there; hence no hidden off-face exact PSD solutions.
- Exposing with zero outcomes is LEGITIMATE for arbitrary ambient PSD competitors, even though a fixed positive-data requirement would disallow this construction.
- The decoder is the positive compression F_0 Y F_0^T. No Schur-complement subtraction or rank restriction is used.
- The source operator system need not contain a single admissible ONB. For instance the tetrahedral W={S in S³:S_11=S_22=S_33} of Milestone 03 has an exact two-basis rank-one frame dilation of order N=5, even though its four admissible rays contain no orthogonal pair.
- The all-nonzero overlap claim is about the basis transition matrix, NOT target outcomes: several target outcomes are exactly zero.
- Modulus equivalence from signed reflections must NOT be copied into this new construction without proving cross-term cancellation; only the explicit upper and lower bounds (3)-(4) are established.
- The more efficient codimension-adaptive compiler is invoked from an earlier separately committed proof; the present theorem is independently valid for ANY supplied Parseval frame and therefore does not depend on that earlier theorem's novelty or computational complexity.
