# Milestone 31 — UNIVERSAL SHARP two-basis transfer for every rank-one PSD inverse problem, of EVERY facial depth

2026-11-08, Research Track 02. This is a complete real finite-dimensional construction, with all-ambient noisy estimates. The central new positive "complement-twin" lift removes the admissible-orthonormal-basis obstruction WITHOUT losing any original PSD recovery modulus. It proves sharp transfer for ALL rank-one Parseval measurement spaces, including arbitrarily high singularity depth, non-singleton fibres and arbitrary competitor ranks. This is a substantive strengthening of Milestones 21–30. It does NOT prove unrestricted O(m²+p) representation for arbitrary dense measurement spaces; generic lower bounds in Milestones 07–09 remain applicable to strong positive retracts.

## Theorem 1 (universal O(d²) sharp rank-one two-basis normal form)

Let d>=1. Let G=[g_1 ... g_M] in R^(d x M) be a nonzero-column Parseval frame, GG^T=I_d, and let
  W=span{g_jg_j^T}, q=dim W (necessarily I_d in W);
  L(Z)=(g_j^T Zg_j)_j.
For every PSD feasible datum c, define
  F_c={Z>=0:L(Z)=c},
  omega_c(t)=max{dist_F(Z,F_c):Z>=0,||L(Z)-c||_2<=t}.
The target need NOT be uniquely recovered; assume only F_c nonempty.

There is a finite explicit REAL algebraic construction of a two-orthonormal-basis problem on order
  N<=3d²+7d+2q+4 <=4d²+8d+4,                 (1)
with an affine globally PSD-positive encoder E:S^d_+ ->S^N_+, a globally PSD-positive LINEAR decoder D:S^N ->S^d, and an affine data map Phi such that
  {Y>=0:A_U(Y)=Phi(c)}=E(F_c),                (2)
  D(E(Z))=Z for every Z>=0,
  <C_tilde,Y>=<C,D(Y)> for EVERY symmetric ambient Y,
and every entry of Phi(c) is strictly positive, every entry of the orthogonal basis transition U is nonzero, and U may be chosen not signed-permutation equivalent to a symmetric reflection. For a non-scalar W the two bases can have genuinely different source-dependent quadratic observations.

For every feasible c with c!=0, the full-ambient worst-case recovery modulus satisfies
  omega_final(t) ~ omega_c(t)+sqrt(t)   (t downarrow0),          (3)
where ~ denotes two-sided fixed-instance comparability at the SAME residual scale up to multiplicative constants. If c=0, F_c={0} and omega_final(t)~t. The result holds for all ambient PSD competitors of unrestricted rank.

The encoding is
  E(Z)=F^T([J(Z)] direct-sum [1])F,
  J(Z)=Z direct-sum (tr Z I_d -Z),                               (4)
with F in R^((2d+1) x N), FF^T=I_(2d+1). The positive decoder is the leading original d-by-d principal block of FYF^T. The embedded Frobenius distance satisfies
  ||Z-Z'||_F <=||E(Z)-E(Z')||_F
   <=sqrt(d²-2d+2)||Z-Z'||_F            (d>=2),               (5)
with sqrt(2) instead of the displayed upper bound for d=1.
The final target rank is
  rank E(Z)=rank Z +rank(trZ I_d-Z)+1:
for Z=0 it is 1; for nonzero rank-one Z and d>=2 it is d+1; for rank Z>=2 it is rankZ+d+1.

All numerical conditioning constants are explicitly computable as reciprocal positive singular values of the finite frame-analysis maps, and the exposing certificate has a uniform gap 2. No dimension-only guarantee for the frame-analysis singular gaps or Turing-bit complexity under arbitrary degeneracy is claimed.

**Consequences.** Every non-Lipschitz PSD recovery modulus, including exponents below 1/2 arising from arbitrarily high facial-reduction depth, is preserved EXACTLY up to fixed comparison constants. A nonzero Lipschitz source necessarily acquires sharp square-root behavior in the final rank>=2 two-basis problem. Crucially this theorem does not require a strict source stress, any source target, or any admissible source orthonormal basis.

## 2. The complement-twin positivity and exact norm identity

For symmetric Z in S^d put
  T(Z)=tr(Z) I_d-Z, J(Z)=Z direct-sum T(Z).
If Z>=0, every eigenvalue lambda_i(Z) satisfies 0<=lambda_i<=trZ, so T(Z)>=0. Thus J is linear, PSD-positive and injective, and
  D0(B)=B_(top d-by-d)
is a PSD-positive linear left inverse on ALL S^(2d)_+.

For any symmetric H,
  ||J(H)||_F²
   =||H||_F²+||tr(H)I-H||_F²
   =2||H||_F²+(d-2)(trH)².                (6)
For d>=2 this lies between 2||H||² and (d²-2d+2)||H||²; for d=1 it equals ||H||² because T(H)=0. The rank formulas in (1) follow by inspecting the eigenvalues of T(Z).

The dual action on a symmetric block matrix
  B=[A,C;C^T,D] in S^(2d)
is
  J*(B)=A-D+(tr D)I_d.                  (7)

## 3. A UNIVERSAL allowed Parseval frame and admissible ONB in dimension 2d

Let
  Wtilde={B in S^(2d):J*(B) in W}.        (8)
Because I_d belongs to W, (7) shows B belongs to Wtilde iff A-D belongs to W; its cross block C is arbitrary. Hence
  dim Wtilde=D_d+d²+q=(3d²+d)/2+q.      (9)

We explicitly construct THREE real Parseval frames in R^(2d), each of whose rank-one projectors belongs to Wtilde.

Family A (ordered source-pairs): for j,k=1,...,M, take
  a_(jk,+)=(g_j,g_k)/sqrt(2M),
  a_(jk,-)=(g_j,-g_k)/sqrt(2M).
Each pullback is
  J*(a a^T)=[g_jg_j^T-g_kg_k^T+||g_k||²I]/(2M) in W.
Summing the two projectors over all ordered j,k gives I_(2d), since GG^T=I_d and cross terms cancel.

Family B (separated copies): for j=1,...,M take
  b_(j,1)=(g_j,0), b_(j,2)=(0,g_j).
Their pullbacks are g_jg_j^T and ||g_j||² I-g_jg_j^T, respectively, both in W. The projectors sum to I_(2d).

Family C (paired arbitrary symmetric generators): define a d-dimensional Parseval frame H with d² columns:
  h_i=e_i/sqrt(d), i=1,...,d;
  h_(i,k,+)=(e_i+e_k)/sqrt(2d),
  h_(i,k,-)=(e_i-e_k)/sqrt(2d), i<k.
Its projectors span ALL S^d, and sum to I_d: the pair projectors contribute (d-1)I/d and the coordinate projectors contribute I/d.
For every column h of H take
  c_(h,+)=(h,h)/sqrt2, c_(h,-)=(h,-h)/sqrt2.
Each has pullback (||h||²/2)I in W. Their projectors sum to I_(2d).
In particular, Family C contains a positive multiple of every projector onto the COMPLETE ONB
  u_i^+=(e_i,e_i)/sqrt2, u_i^-=(e_i,-e_i)/sqrt2, i=1,...,d.
Thus Wtilde has an admissible ONB regardless of whether W has one.

Combine Families A,B,C after scaling each column by 1/sqrt3. Their union is Parseval and every projector lies in Wtilde.

**EXACT SPAN.** The B projectors span diag(W,0) and diag(0,W). The signed difference of Family C projectors for a fixed h spans a symmetric off-diagonal cross block with matrix hh^T, and their sum spans diag(hh^T,hh^T); since {hh^T} spans S^d, all common diagonal pairs diag(A,A) and all symmetric cross blocks occur. The signed difference of Family A projectors for j,k is a pure cross block with upper-right matrix g_j g_k^T (up to positive scaling). Since G has full row rank, {g_jg_k^T} spans ALL real d-by-d matrices, including skew parts. Therefore the union spans every cross block and every diagonal pair diag(A,B) with A-B in W, namely EXACTLY Wtilde.

The raw frame has 2M²+2M+2d² columns. The following elementary conic elimination reduces its length to
  Mtilde<=2 dim Wtilde=3d²+d+2q.         (10)
Choose dim Wtilde independent projectors from the original positive frame, reserve HALF of the original coefficient of each, and use conic Caratheodory elimination on the remaining positive identity representation. Whenever more than dim Wtilde positive terms remain, a linear dependence among their rank-one projectors has both signs (because every projector has positive trace); move along the dependence until one coefficient reaches zero. This preserves PSD coefficients and the represented identity. At most dim Wtilde residual terms remain. Adding the reserved independent projectors produces a positive Parseval frame with <=2dim Wtilde columns and full projector span Wtilde. It continues to contain the ONB PROJECTORS IN ITS LINEAR SPAN (not necessarily as literal retained columns), which is exactly what the signed-anchor construction requires.

This proves the new universal **admissible-basis rank-one compiler** with only a factor-two increase in compressed matrix order and O(d²) final frame columns.

## 4. Exact correspondence and a globally Lipschitz POSITIVE retraction

Let Mtilde:S^(2d)->R^(Mtilde) be the rank-one measurement map for the compressed frame. Because its projector span is Wtilde,
  ker Mtilde = Wtilde^perp=J(W^perp)=J(ker L).            (11)
The second equality follows directly from the adjoint identity (7) and dimension counting: J is injective, J* is surjective, and
  dim Wtilde^perp=D_d-q=dim J(W^perp).

Thus for every nonempty feasible source fibre F_c,
  {Y>=0:Mtilde(Y)=Mtilde(J(Z_*))}
     =J(F_c).                                           (12)
Indeed linearity and (11) force Y=J(Z_*+H) for some H in ker L, and Y>=0 forces its top block Z_*+H>=0; conversely J(Z)>=0 whenever Z>=0.

The map D0(Y)=Y_(top d-by-d) is PSD-positive. More strongly, the retraction
  R0(Y)=J(D0(Y))
is PSD-positive on all Y>=0, fixes J(S^d_+), and is LINEAR and uniformly Lipschitz:
  ||R0(Y)-R0(Y')||<=||J|| ||Y-Y'||.

To make explicit the DATA residual estimates, on S^(2d) define linear maps
  A0(H)=(H-J(D0(H)), L(D0(H))).
Both A0 and Mtilde have the SAME kernel J(kerL). Hence their quotient norms are equivalent: for a computable constant
  K0=||A0 Mtilde^dagger||_(2->F⊕2)<infinity,
  ||Y-J(D0(Y))||_F+||L(D0(Y))-c||_2
    <=sqrt2 K0||Mtilde(Y)-Mtilde(J(Z_*))||_2.           (13)
The Moore-Penrose pseudoinverse is computed on the positive singular-value subspace; this is an explicit finite-dimensional conditioning constant, not an unspecified equivalence assertion.

Conversely there is a computable C0>0 such that
  ||Mtilde(J(Z-Z_*))||<=C0||L(Z-Z_*)||
for all symmetric source perturbations, because both maps have the same source kernel. In particular the source and compiled worst-case PSD feasible-set moduli satisfy
  omega_comp(t)~omega_source(t)                         (14)
for all sufficiently small t, including NONSINGLETON fibres. An explicit pair of inequalities follows from (13), (6), and the embedded competitor curves:
  omega_comp(t)<= ||J|| omega_source(sqrt2 K0 t)+sqrt2 K0 t,
  omega_comp(t)>=omega_source(t/C0).
Fixed rescalings of a convex PSD recovery modulus change it only by multiplicative constants, by interpolating competitors toward their nearest feasible points.

**The key distinction from the two-zero Naimark construction:** here the retraction and SOURCE RESIDUAL are both O(t), not O(sqrt t). No additional square-root loss occurs during rank-one compilation, even for singular or high-facial-depth source fibres.

## 5. A SINGLE signed-anchor two-basis dilation and full-ambient rates

Apply the signed-anchor construction of Milestones 27 and 30 to this NEW d'=2d-dimensional Parseval frame. The necessary admissible ONB is the explicit paired basis u_i^± in Wtilde, so NO target/stress/face or tangent-curve information is required.

Take three columns per u_i with weights -1,2,3, all compressed-frame columns at positive weight 4, h=1/10 and the standard coefficients a²=(5+3h²)/7, b²=(1-5h²)/7; solve the two tightness/signed identities by nonzero small anchor coordinates and three pure-anchor columns with weights -1,2,4. Duplicate one weight-4 frame column for the optional two-coordinate equal-weight rotation. This produces an algebraic Parseval frame F in R^((2d+1) x N), with
  FF^T=I_(2d+1), FDF^T=0,
and
  N<=3(2d)+Mtilde+4<=3d²+7d+2q+4
as in (1).

Let P=F^T F, Q=I-P, R=P-Q. D has exactly 2d+1 negative entries -1 and all positive entries >=2; the isotropic-graph argument yields
  S0=D+RDR=2QDQ>=2Q,
with kernel ran P. The exposing certificate is a measured signed combination of the two diagonal lists. Rotating a selected weight-4 duplicate with the pure-anchor weight-4 coordinate leaves S0 unchanged because the rotation commutes with D; retain the other duplicate to preserve compressed analysis. Generic sufficiently small nonzero rotation preserves strictly positive observations and nonzero overlaps and makes the row/column fourth-moment multisets unequal, proving the transition not signed-permutation equivalent to a reflection.

The compressed projectors span exactly the anchored extension of Wtilde:
  W_aug={ [H,z;z^T,s]:H in Wtilde,z in R^(2d),s in R}.
Therefore the full-ambient exact PSD fibre is E(F_c), and for every PSD ambient competitor with two-basis residual delta<=1, the exposing certificate controls exterior PSD mass by kappa delta and the exterior cross blocks by O(sqrt delta). Averaging the two unrotated basis lists cancels all cross blocks EXACTLY, recovering the compressed W_aug data with O(delta) error. The retained duplicate controls the at-most-two rotated outputs with a fixed finite analysis constant. Combined with the linear PSD retraction (13),
  dist(Y,E(F_c))
    <= C_1 omega_source(C_2 delta)+C_3 sqrt delta+C_4 delta.
Embedded curves yield the lower omega_final(delta)>=omega_source(c delta).

For any nonzero feasible source C, the final encoded target E(C) has rank >=2, and the large exterior dimension guarantees a nonzero invisible support-to-exterior cross block K: the domain dimension is at least 2(N-2d-1)>N, whereas first-basis diagonal invisibility and the one rotated pair impose at most N independent equations. The PSD same-rank curve
  Y(t)=E(C)+t(K+K^T)+t²K^T E(C)^dagger K
has data residual Theta(t²) and distance Omega(t) from the WHOLE embedded feasible fibre (which is supported on ran P). Hence omega_final(t)>=c sqrt t, proving (3).

When c=0, Parseval trace control forces F_c={0}. The final encoded target is the positive-anchor rank-one matrix. The compressed positive source and lower support blocks are O(delta); positivity makes cross blocks between the two small-mass subspaces O(delta), while the first diagonal detects the anchor-to-exterior cross block LINEARLY because every anchor coordinate is nonzero. Thus omega_final(t)=Theta(t), rather than sqrt t.

Every source linear cost C is lifted to F^T[(C direct-sum 0_d) direct-sum [0]]F. Its objective on ANY symmetric Y equals <C,D(Y)> for D(Y)=the original d-by-d leading principal block of FYF^T, a PSD-positive decoder with D(E(Z))=Z. All competitors are arbitrary rank.

## 6. Sharp non-Lipschitz preservation and arbitrary facial depth

For any bounded real PSD linear inverse problem, its local set-valued modulus is either Lipschitz, omega(t)=O(t), or dominates sqrt(t), omega(t)>=c sqrt(t). For clarity this PSD tangent-cone dichotomy is proved directly in the preceding Track 02 work: choose a maximal-rank feasible C, let E=ran C. If ker L has a nonzero direction with PSD kernel-kernel block not supported entirely in E, a Schur-complement quadratic repair yields distance Omega(t) at residual O(t²). Otherwise a uniform angle between the tangent cone {H:QHQ>=0} modulo supported kernel directions and ker L gives a Lipschitz retraction to the face using mixing with C. Both alternatives include nonsingleton fibres.

Consequently (3) implies
  omega_final(t)~omega_source(t)
whenever the original source is NON-LIPSCHITZ. This is a FULL-MODULUS comparison, not just preservation of the optimal rational exponent. The argument makes NO assumption about strict exposing stress, facial reduction depth, target rank, or a pre-existing admissible ONB.

For example, applying this construction to any rank-one Parseval representation of a high-depth graph-completion instance with exponent 2^(-k) gives a positive-data all-overlap-nonzero two-basis problem of order O(d²) with EXACT optimal exponent 2^(-k), for all k>=1. This contrasts with the loss demonstrated in Milestone 26's two-zero first stage.

## 7. General linear PSD inverse problems via an arbitrary rank-one compiler

The codimension-adaptive purification lemma proved in the earlier CODIMENSION_TWO_UNIVERSAL_THEOREM.md produces for every trace-normalized real PSD measurement space L subset S^m of codimension s a rank-one Parseval compiler on order
  d=m r, r=2r0+1=O(sqrt(s+1)),
  r0=max{k:k(k+1)/2<=s+1},
whose projector span has kernel J_old(ker A), with J_old(X)=X tensor I_r. Its positive partial-trace decoder preserves original moduli at linear residual scale and has all-rank exact fibres.

Applying Theorem 1 to that compiler gives, WITHOUT any strict source stress or target-dependent procedure,
  N=O(d²)=O(m²(s+1)),                         (15)
a fully explicit algebraic two-ONB representation with positive observations, nonzero overlaps and SHARP
  omega_final(t)~omega_A(t)+sqrt(t)
for nonzero feasible data, and Lipschitz zero-fibre behavior. Thus for every FIXED codimension s, ANY bounded real PSD linear inverse problem, of any singularity depth and including dense noncommuting constraints, has a SHARP quadratic-size O_s(m²) two-basis normal form. For unrestricted s=Theta(m²), the dimension remains O(m^4); the generic superquadratic lower bounds under positive retracts remain consistent with this.

The proof above of the rank-one-to-ONB conversion is SELF-CONTAINED and does not rely on the correctness of the previous codimension-adaptive compiler; equation (15) uses that separately committed input theorem. One may alternatively use the older fully universal r=2m tensor compiler if one wishes to avoid optimizing s, still obtaining sharp O(m^4) transfer for arbitrary trace-controlled PSD inverse problems.

## 8. Hostile audit

1. Complement positivity is global: trZ I-Z>=0 for EVERY PSD Z, not only for a fixed trace-one fibre. The decoder is a positive principal-block compression, not a Schur-complement subtraction.
2. The exact frame span includes BOTH antisymmetric cross blocks and the missing diagonal-difference scalar direction. Families A,B,C are all essential; just paired (u,u)/(u,-u) vectors would FAIL to span the desired operator space.
3. The allowed ONB u_i^± is present in the linear span of projector generators even after conic sparsification, which suffices for the signed-anchor dilation.
4. Exact kernel equality (11) is proved by adjoints and dimension, not inferred from numerical rank tests.
5. The noisy PSD retraction has the SAME kernel as the rank-one analysis map and so has an O(delta) linear inverse constant for all symmetric perturbations. This closes precisely the first-order cancellation problem of Milestone 23.
6. The final square-root lower bound is taken against the ENTIRE embedded feasible fibre, so it is valid for nonsingleton source sets, not only isolated targets.
7. At zero data, the final anchor is rank one and the modulus is Lipschitz; adding a fixed positive complement block would have incorrectly destroyed this exception, but the chosen complement vanishes at Z=0.
8. All projectors, positive Parseval weights, and admissible ONB are real; no complex tensor identities are needed in the new compiler.
9. The O(d²) dimension follows from explicit positive conic frame sparsification. It requires exact algebraic arithmetic and conditioning-dependent bit complexity; no unjustified uniform polynomial bit claim is made.
10. The general O(m²+p) near-quadratic SIZE conjecture for arbitrary dense noncommuting SDPs is not solved. What IS solved here is unrestricted SHARPNESS for all rank-one source systems, and sharp fixed-codimension universality for general linear SDP systems.
