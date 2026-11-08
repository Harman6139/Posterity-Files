# Milestone 24 — STRICTLY POSITIVE two-basis dilation for EVERY rank-one Parseval PSD compiler, without an admissible ONB

Date 2026-11-08. Proved finite-dimensional construction with two real orthonormal bases, all strictly positive target observations, every overlap nonzero, positive decoding, exact full feasible-fibre correspondence and rank amplification exactly one. It extends Milestone 21 by removing zero target outcomes at **constant-factor ambient order**, using a signed anchor lift of the two-zero intermediate problem. The resulting modulus bound is weaker than the earlier sharp reflection transfer from the ORIGINAL source: the two-zero intermediate may lose a square root.

## Theorem A — positive nonreflection two-basis realization of any rank-one compiler

Let G=[g_1,...,g_M] in R^{d x M} be a Parseval frame, GG^T=I_d, whose projectors span a trace-controlled real PSD inverse measurement operator system W=span{g_jg_j^T}. Suppose M>d and 0<||g_j||<1 for all j; duplicate/rescale every frame column if needed. Let
  F_c={Z>=0: (g_j^T Zg_j)_j=c}
be any nonempty fibre (singleton or not).

There is an explicit finite algebraic construction of TWO complete real orthonormal bases on R^N with
  N <= 10M-5d+4
and an affine positive encoding E:S^d_+ -> S^N_+, a globally positive linear decoder D:S^N -> S^d satisfying D(E(Z))=Z for every Z>=0, such that
  {Y>=0: A_U(Y)=Phi(c)} = E(F_c)
for EVERY feasible c, with no restriction on ambient competitor ranks.

The source-to-target map preserves Frobenius distances exactly,
  ||E(Z)-E(Z')||_F=||Z-Z'||_F,
and
  rank E(Z)=rank Z+1.
Every encoded observation is strictly positive for EVERY Z>=0, including Z=0. The basis transition U has no zero entries and may be chosen not signed-permutation equivalent to a symmetric reflection. For an original measurement space dim W>=2 the two measured lists can be made genuinely different on encoded nonzero sources.

For every source cost C there is an explicit ambient matrix C_tilde with
  <C_tilde,Y>=<C,D(Y)>
for ALL symmetric ambient Y (not just feasible points). Thus exact objective values and arbitrary-ambient approximate objective errors decode without loss.

Let omega_source be the PSD source distance-to-fibre modulus and omega_final the full-ambient two-basis modulus. There are fixed-instance effectively computable c,C>0 such that for sufficiently small t>0,
  omega_source(c t) <= omega_final(t)
    <= C omega_source(C sqrt(t))+C sqrt(t).               (1)
If c!=0 (nonzero trace data), also
  omega_final(t)>=c sqrt(t).
If c=0 then F_c={0} and omega_final(t)=Theta(t) (rank-one anchored target).

For any attained source exponent alpha in (0,1] and nonzero source datum,
  alpha/2 <= alpha_final <= min(alpha,1/2).
In particular a Lipschitz source (alpha=1) yields EXACT final exponent 1/2. The theorem does NOT claim that every non-Lipschitz source exponent is preserved: sharp rate preservation for arbitrary W still requires another mechanism.

## Proof: first stage, exact two-zero basis representation

Apply Milestone 21 to G. It produces order
  n=2M-d
and two ONBs B_1,B_2 on R^n, with transition V in O(n), together with F_0=[G,0_{d x(M-d)}] satisfying F_0 F_0^T=I_d. Its exact PSD fibre at datum a(c) is
  T_c={Y>=0:A_V(Y)=a(c)}={F_0^T ZF_0:Z in F_c}.
Both first and second measurement lists contain M original frame values and M-d zeros, in complementary positions. A generic rotation on their shared exterior support makes every transition entry nonzero without changing exact fibres.

The positive compression D_0(Y)=F_0 Y F_0^T left-inverts E_0(Z)=F_0^T ZF_0; distances and ranks are preserved. Its all-ambient modulus satisfies
  omega_zero(t)>=omega_source(t/sqrt(2))
and
  omega_zero(t)<=omega_source(C_0 sqrt(t))+C_0 sqrt(t)
for computable C_0 and sufficiently small t. This is proved by the explicit zero-outcome exposing certificate S_0>=gamma Q_0 in Milestone 21.

## Proof: second stage, signed-anchored reflection of the ENTIRE two-basis problem

The original intermediate two-basis measurement span
  W_0=span{e_ie_i^T, V e_i e_i^T V^T :1<=i<=n}
contains the first standard ONB projectors. It has an explicit rank-one Parseval frame of 2n columns:
  g'_i=e_i/sqrt(2),  g'_{n+i}=V e_i/sqrt(2).
Duplicate ONE of the weight-4 frame vectors into two equal halves, retaining the same outer-projector sum and measurement span. The resulting frame has M'=2n+1 columns and still satisfies sum_j g'_j g'_j^T=I_n.

Use h=1/10, a^2=(5+3h²)/7, b²=(1-5h²)/7. At each standard source basis vector e_i take
  a e_i, b e_i, b e_i
with signed weights -1,2,3; at each g'_j take h g'_j of signed weight 4.
Let A be the n-by-(3n+M') matrix of these columns and D_old their diagonal weights. Since a²+2b²+h²=1 and -a²+5b²+4h²=0,
  AA^T=I_n,   A D_old A^T=0.

Put r_i=h sum_j <e_i,g'_j>, t_0=2sqrt(M'+1). Assign anchor coefficients to the three columns at e_i:
  z_(i,-)=(2r_i+t_0)/(3a),
  z_(i,2)=-(5r_i+4t_0)/(3b),
  z_(i,3)=t_0/b,
and put z_j=1 at each g'_j column. Every z_j is nonzero and a direct substitution gives
  A z=0, A D_old z=0.

Choose a sufficiently small positive algebraic epsilon with no cancellation among the finitely many quantities
  <A_j,A_k>+epsilon² z_j z_k, j!=k,
and avoiding squared new-column norms 1/2. One can search a finite rational grid; each forbidden cross equation eliminates at most one parameter value, and a sufficiently small grid interval preserves all strict positivity constraints.

Write s=z^Tz, q=z^T D_old z, fix v²=1/100 and define
  x²=(2+epsilon²(q-2s)+2v²)/3,
  y²=(1-epsilon²(s+q)-5v²)/3.
These are strictly positive for small epsilon. Append the anchor coordinate epsilon z_j to every old column, and append three pure-anchor columns x e_c,y e_c,v e_c with signed weights -1,2,4. The final (n+1)-by-(5n+4) matrix F_1 and diagonal D satisfy
  F_1 F_1^T=I_(n+1), F_1 D F_1^T=0.
D has exactly n+1 negative entries -1 and all positive entries at least 2.

Let P=F_1^T F_1, Q=I-P, R=P-Q. The signed certificate
  S=D+R D R=2Q D Q >=2Q
is positive semidefinite with kernel ran P. The inequality is proved by writing the D-isotropic n+1-dimensional subspace ran P as a graph over the n+1 negative-weight coordinates and using D_+>=2I to show Q D Q>=Q (identical to the explicit proof in Milestones 06/22).

Every column of F_1 has a nonzero anchor coordinate, and all pairwise inner products and all diagonal numbers 2||f_j||²-1 are nonzero. Thus R has no zero entry. For any intermediate PSD Y_0, define
  E_1(Y_0)=F_1^T (Y_0 direct-sum [1])F_1.
Every first-basis and second-basis measurement of E_1(Y_0) is STRICTLY POSITIVE: for every column f_j=(v_j,eta_j) with eta_j!=0,
  f_j^T(Y_0 direct-sum [1])f_j=v_j^T Y_0 v_j+eta_j²>0,
and R acts as identity on ran F_1^T.

The compressed source projectors span exactly the augmented operator system
  W_aug={ [H,z;z^T,s] : H in W_0, z in R^n,s in R}.
The vertex triplet projectors recover each e_ie_i^T and anchor-to-e_i cross direction by independent 2-by-2 coefficient pairs; pure-anchor projectors recover e_ce_c^T; subtracting these terms from each g'_j projector recovers g'_jg'_j^T. Therefore the S-certificate forces every exact ambient PSD competitor into ran F_1^T, and compression forces its matrix to have form Y_0 direct-sum [1] with Y_0 in the original intermediate two-basis fibre T_c. This proves
  {Y>=0:A_R(Y)=Phi(a(c))}=E_1(T_c).

For genuine nonreflection designs, rotate one selected weight-4 duplicated g'_j coordinate with the weight-4 pure-anchor coordinate through a sufficiently small nonzero angle phi, setting U=R O_phi. The rotation commutes with D and leaves S unchanged; the untouched duplicate preserves the compressed measurement span. Generic small angles preserve strict positive measurements, avoid zero overlaps and make row/column fourth-moment multisets unequal, excluding independent signed-permutation equivalence to a symmetric reflection. They also produce genuinely different compressed quadratic lists when W_0 contains nonscalar forms.

## Positive decoder, rank, and dimension

Define the composite encoder
  E(Z)=F_1^T((F_0^T Z F_0) direct-sum [1])F_1.
For an ambient Y, set
  D(Y)=F_0 [F_1 Y F_1^T]_(1:n,1:n) F_0^T.
Both operations are PSD-positive (congruence and principal compression). D E=id. Since F_0,F_1 have orthonormal rows,
  ||E(Z)-E(Z')||_F=||Z-Z'||_F,
  rank E(Z)=rank Z+1,
and for any cost C,
  C_tilde=F_1^T((F_0^T C F_0) direct-sum [0])F_1
satisfies <C_tilde,Y>=<C,D(Y)> identically.

The final order is
  N=5n+4=5(2M-d)+4=10M-5d+4.
Every claim concerns ALL ambient PSD ranks.

## Quantitative transfer and honest gap

The signed exposing certificate confines exterior PSD mass to O(delta) and cross blocks to O(sqrt(delta)). The reflection-even average of the unrotated measurements exactly cancels cross blocks, so the intermediate two-basis measurement residual is O(delta); the single rotated frame measurement is reconstructed from its retained duplicate. Consequently the signed second stage has, for fixed-instance computable positive constants,
  omega_final(t) <= C omega_zero(Ct)+C sqrt(t),
  omega_final(t) >= c omega_zero(ct).
For nonzero intermediate source target, an invisible support-to-exterior cross block exists by dimension (the target after anchoring has rank at least 2 and the exterior has dimension 4n+3), yielding omega_final(t)>=c sqrt(t). The zero target is rank one after anchoring and gives a Lipschitz modulus by linear detection of all anchor/exterior cross blocks; this is proved in the earlier abstract reflection theorem.

Substitute Milestone 21's omega_zero upper and lower bounds. Fixed rescalings of a PSD modulus change it only by fixed factors by convexity of feasible sets, giving
  omega_source(ct) <= omega_final(t) <= C omega_source(C sqrt(t))+C sqrt(t).
This proves the theorem and the claimed exponent interval. A source Lipschitz modulus is mapped to EXACT square-root in the nonzero case, whereas source exponents below 1/2 may degrade; there is NO claim that the original source non-Lipschitz exponent is universally preserved.

## Corollary — all fixed-codimension dense systems admit positive quadratic-size two-basis representations

Let the original trace-controlled operator space L<=S^m have codimension s. The codimension-adaptive purification theorem in the earlier CODIMENSION_TWO_UNIVERSAL_THEOREM.md constructs a rank-one Parseval compiler on order
  d=m r, r=2r_0+1, r_0=max{k:k(k+1)/2<=s+1}
with M=O(d²) frame columns. Combining it with this theorem yields order
  N=O(d²)=O(m²(s+1)).
For each fixed s (including every arbitrary dense noncommuting s>=3) this is O_s(m²). Every target observation can be made strictly positive, all basis overlaps nonzero, exact fibres and objectives preserved, and the positive decoder is explicit. The rate guarantee is the stated alpha/2 <=alpha_final<=min(alpha,1/2), not exact non-Lipschitz exponent preservation. When s=Theta(m²) this construction remains quartic and does NOT resolve unrestricted O(m²+p) universality.

## Hostile audit

1. The second stage is a signed frame dilation of the ENTIRE first-stage two-basis inverse problem, not an attempt to assume the original operator space has an admissible ONB.
2. The first-stage zero observations disappear in the final target: the nonzero anchor contribution makes EVERY final basis outcome positive.
3. Each final output has the prescribed positive source-anchor block; all-rank ambient competitors are forced there by the measured PSD stress. No rank-restricted reasoning occurs.
4. Nonzero overlaps are verified by finite avoidance, not inferred from genericity without a nonidentity argument.
5. A single duplicated weight-4 frame column is retained after basis rotation, preventing the rotation from destroying compressed measurement-spanning.
6. Composition changes dimension only by a factor <=5 plus four; it does NOT square the earlier O(d²) dimension.
7. The first-stage first-order cross map generically cancels all trace-free source data (Milestone 23). Therefore the composed positive construction is not falsely advertised as sharp modulus preserving.
8. Algebraic arithmetic construction is finite and polynomial in frame size, with numerical conditioning controlled by explicitly measured frame analysis gaps and anchor separation. No uniform polynomial Turing bit bound for arbitrary degeneracy is claimed.
9. The theorem is mathematically independent of the novelty claims in the preceding manuscripts; all results remain self-audited, not externally refereed.
