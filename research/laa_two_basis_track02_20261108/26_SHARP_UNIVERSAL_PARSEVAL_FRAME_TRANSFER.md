# Milestone 26 — SHARP positive two-basis transfer for ANY rank-one Parseval compiler, no admissible source ONB

Date 2026-11-08. New substantive theorem resolving the **sharp-modulus preservation problem for rank-one Parseval-compiled PSD inverse problems**. This repairs the alpha/2 defect of Milestones 21/24 and avoids the first-order cancellation obstruction of Milestones 23/25. It does NOT prove unrestricted N=O(m²+p) for arbitrary dense source SDP inputs; Milestones 07/08 already show that impossible in the global positive exact-retract model.

## 1. Main theorem

Let G=[g_1 ... g_M] be a REAL d-by-M Parseval frame, GG^T=I_d, with every g_j !=0. Let
  M_G(X)=(g_j^T X g_j)_j,
  C_c={X>=0:M_G(X)=c},
  omega_G(t)=sup{dist_F(X,C_c):X>=0,||M_G(X)-c||_2<=t}.
The source fibre may be nonsingleton; positive input target ranks are unrestricted.

There is a finite algebraically explicit real two-orthonormal-basis PSD problem of order
  N<=6M-d+4
with an affine positive encoder E:S^d_+ -> S^N_+, a globally positive linear decoder D:S^N ->S^d, an affine data encoder Phi, and an orthogonal change-of-basis U satisfying the following simultaneously for EVERY feasible datum c:

(a) {Y>=0:A_U(Y)=Phi(c)}=E(C_c), with arbitrary ambient PSD competitor ranks.

(b) D E=id, ||E(X)-E(X')||_F=||X-X'||_F, rank E(X)=rank X+1, and every source linear objective C has an explicit ambient cost C_tilde with <C_tilde,Y>=<C,D(Y)> for ALL symmetric ambient Y.

(c) Every entry of U is nonzero, and both lists of every encoded target's measurements are strictly positive, including the zero source. U may be made nonreflection under independent signed permutations of its two bases by a redundant equal-weight two-coordinate rotation; if the source operator span has dimension >=2 the compressed lists can be genuinely different on encoded sources.

(d) For fixed-instance explicitly computable positive constants a,b,kappa, and all sufficiently small t>0,
  omega_G(a t)<=omega_final(t)
       <=omega_G(b t)+kappa sqrt(t).
For c!=0,
  omega_final(t)>=a sqrt(t),
so
  omega_final(t) ~ omega_G(t)+sqrt(t).                     (1)
For c=0, omega_final(t)~t. The same is true after a fixed trace-one normalization for nonzero targets.

(e) Every non-Lipschitz PSD source modulus is therefore preserved up to multiplicative constants, and every nonzero Lipschitz source has exact final exponent 1/2. All attained source error exponents alpha_G transfer as
  alpha_final=min(alpha_G,1/2)
for c!=0, and alpha_final=1 for c=0. Semialgebraicity of fixed-dimensional PSD moduli gives attainment of the optimal exponent.

A crucial novelty is that the construction needs NO admissible orthonormal basis in the original rank-one operator system span{g_jg_j^T}. In particular it applies to the tetrahedral W={X in S³:X_11=X_22=X_33}, for which Milestone 03 proves no pair of allowed rank-one vectors can be orthogonal.

## 2. The "source-only / exterior-only" Naimark enrichment

Set n=M, P=G^T G (rank-d projection on R^M), Q=I_M-P (rank q=M-d). Choose an orthonormal matrix H in R^{M x q} with HH^T=Q, H^T H=I_q. (When q=0 omit exterior columns.) Let x_j=P e_j=G^T g_j, j=1,...,M, and h_a=H e_a, a=1,...,q. Since every g_j!=0, every x_j!=0.

Build the explicit n-by-L Parseval frame
  T=[ e_1/sqrt2,...,e_M/sqrt2,
      x_1/sqrt2,...,x_M/sqrt2,
      h_1/sqrt2,...,h_q/sqrt2],
  L=2M+q=3M-d.                                         (2)
Indeed
  TT^T=(I_M+P+Q)/2=I_M.

The FIRST M columns of T are a complete standard ONB (up to the same scaling) and are permissible rank-one source measurements after embedding x ->G^T x G: G e_j=g_j. Every T column pulls back under G to g_j/sqrt2 or zero:
  G(e_j/sqrt2)=g_j/sqrt2,
  G(x_j/sqrt2)=g_j/sqrt2,
  G(h_a/sqrt2)=0.

The frame T does MORE than provide an admissible ONB: its projector span includes the explicit pure-source projectors x_jx_j^T and pure-exterior projectors h_a h_a^T. These two types respectively (i) measure the original source quadratic outcomes without any V/Q cross-contamination, and (ii) expose/quantitatively control every exterior PSD direction through their positive sum:
  sum_a h_a h_a^T=Q.                                 (3)
This is precisely the missing information in Milestone 21. No two-zero intermediate dilation or extra square-root composition is needed.

## 3. Strictly positive signed two-basis dilation

Apply the explicit signed-anchor construction, now to dimension n=M, using (2) as the rank-one Parseval frame and the standard e_i ONB as the admissible basis.

Let h=1/10,
  a²=(5+3h²)/7,  b²=(1-5h²)/7.
At every e_i take columns a e_i, b e_i,b e_i with signed diagonal weights -1,2,3; at every T frame column t_j take h t_j with signed weight 4. Their matrix A_0 in R^{n x (3n+L)} and diagonal D_0 satisfy
  A_0 A_0^T=I_n, A_0 D_0 A_0^T=0,
because a²+2b²+h²=1 and -a²+5b²+4h²=0.

Set r_i=h sum_j <e_i,t_j>, t0=2 sqrt(L+1), and let z for the vertex triplets be
  z_(i,-)=(2r_i+t0)/(3a),
  z_(i,2)=-(5r_i+4t0)/(3b),
  z_(i,3)=t0/b;
for all T columns use z_j=1. Then z_j!=0 and
  A_0 z=0, A_0 D_0 z=0.
Choose epsilon>0 sufficiently small and avoiding the finitely many forbidden cancellation roots
  <A_0[:,i],A_0[:,j]>+epsilon² z_i z_j=0 (i<j).
Also prevent the squared column norms from crossing 1/2. This can be done by exact finite rational-grid avoidance, with a polynomial bound on the grid denominator in the frame order and norms, if coefficients have an algebraic separation promise.

Fix v²=1/100. Put s0=z^T z, q0=z^T D_0 z and
  x²=[2+epsilon²(q0-2s0)+2v²]/3,
  y²=[1-epsilon²(s0+q0)-5v²]/3.
For sufficiently small epsilon these are positive. Define F in R^{(n+1) x N} using columns (A_0[:,j],epsilon z_j) and three pure-anchor columns x e_c,y e_c,v e_c with signed weights -1,2,4. Then
  FF^T=I_(n+1), F D F^T=0.
D has exactly n+1 negative entries -1 and all positive entries >=2. The total order is
  N=3n+L+3=6M-d+3.
For a selected g/T column one can split it into two equal columns before this construction, increasing the order by one, to reserve one duplicate for the nonreflection rotation:
  N<=6M-d+4.

Set P_1=F^T F, Q_1=I-P_1 and R=P_1-Q_1=2P_1-I. Then R is orthogonal with every entry nonzero. The signed measured certificate
  S_0=D+RDR=2Q_1 D Q_1 >=2Q_1
has kernel ran F^T. The gap proof is elementary: because FDF^T=0 and D=-I_(n+1) direct-sum D_+, D_+>=2I, the D-isotropic subspace ran F^T is a graph over the negative coordinate space, and D has quadratic form >=||w||² on its Euclidean orthogonal complement.

The compressed outer rank-one projectors span the augmented space
  W_aug={ [B,z;z^T,s]: B in span{t_jt_j^T}, z in R^n,s in R}.
Pure anchor columns give e_ce_c^T; two vertex triplet columns recover each e_ie_i^T and e_ie_c^T+e_ce_i^T; T columns recover their old projector after subtracting those terms. In particular pure-inner-source x_jx_j^T and pure-inner-exterior h_a h_a^T are measured linearly by this final two-basis map.

The embedded source map is
  E(X)=F^T[(G^T XG) direct-sum [1]]F.                 (4)
The positive decoder is
  D(Y)=G [F Y F^T]_(1:n,1:n) G^T.                   (5)
Because GG^T=I_d and FF^T=I_(n+1), D E=id; E is Frobenius isometric, rank E(X)=rank X+1, and source objectives lift exactly by the adjoint of D.

Each final frame column has nonzero anchor coordinate; hence its target outcome on every PSD X is
  v_j^T(G^T XG)v_j + eta_j² >0.
The second list agrees with the first for R. A small equal-weight two-coordinate rotation (one selected duplicated weight-4 T column against the pure-anchor weight-4 column) leaves D invariant and thus preserves the certificate; a remaining duplicate preserves the compressed span. Generic sufficiently small angles avoid all zero overlaps, change the lists on nonzero encoded source matrices when dim source measurement span>=2, and are not signed-permutation equivalent to a symmetric reflection by the row/column fourth-moment invariant.

## 4. Exact fibre proof

Let c=M_G(X_*) with X_*>=0. Any ambient Y>=0 with the same FINAL data has <S_0,Y>=0, so ran Y subset ran F^T. Thus Y=F^T Z F for Z>=0 on R^{n+1}. Its compressed measured data force anchor diagonal 1, anchor cross terms 0, and
  t_j^T W t_j=t_j^T(G^T X_*G)t_j
for every T column, where W is the upper n-by-n principal block of Z.

In particular the measured pure-exterior columns h_a/sqrt2 have target quadratic outcome zero. PSD then forces W h_a=0 for each a. Their span equals ran Q, so ran W subset ran P=ran G^T. Consequently W=G^T X G for X=G W G^T>=0.

The pure-source frame columns x_j/sqrt2 yield
  (x_j)^T W x_j=g_j^T X g_j=c_j.
Thus X belongs C_c. Conversely E(X) has the required data for every X in C_c, because every T projector on E(X) pulls back to a multiple of g_jg_j^T or zero. Hence
  {Y>=0:A_U(Y)=Phi(c)}=E(C_c)
with NO ambient rank restrictions.

## 5. Quantitative ALL-AMBIENT sharp modulus transfer

Let delta=||A_U(Y)-Phi(c)||<=1 for arbitrary Y>=0. Work first with the reflection U=R; the small two-coordinate rotation is treated afterwards by retaining an unrotated duplicate.

Write Y in outer P_1/Q_1 blocks. Let
  kappa_1=||diag D||_2/sqrt2,
  T=tr E(X_*)+sqrt(N).
The measured certificate gives
  tr(Q_1YQ_1)<=kappa_1 delta.
Positivity gives
  ||P_1YQ_1||_F²<=T kappa_1 delta.
Hence, with Z=FYF^T>=0,
  ||Y-F^T ZF||_F
    <=kappa_1 delta+sqrt(2T kappa_1 delta).         (6)

Averaging the TWO measured lists annihilates the outer cross block exactly:
  (r_1+r_2)/2=diag(F^T (Z-Z_*) F+Q_1 Y Q_1).
Thus the compressed frame residual satisfies
  ||diag(F^T(Z-Z_*)F)||_2
    <=(1/sqrt2+kappa_1)delta.                       (7)
For the nonreflection angle, let J be all output coordinates except the rotated selected weight-4 frame coordinate i and the rotated weight-4 pure-anchor coordinate k. The split weight-4 columns have EXACTLY identical full compressed vectors f_i=f_j (the old T vector was split equally and both assigned anchor coefficient z=1); coordinate j remains in J. Removing i therefore does not reduce the compressed span. Removing k does not reduce it either because the other two pure-anchor columns have nonzero anchor coordinates and already give e_ce_c^T. Hence the unrotated compressed projectors {f_l f_l^T:l in J} still span W_aug.

For every l in J, U e_l=R e_l and the measured even residual obeys
  (r_first,l+r_second,l)/2 = f_l^T (Z-Z_*) f_l +(Q_1 Y Q_1)_(l,l).
Let gamma_ret>0 be the least positive singular value of the retained analysis map
  Z ->(f_l^T Z f_l)_(l in J)
restricted to W_aug. Then, WITHOUT assuming anything about the other two rotated outcomes,
  ||P_(W_aug)(Z-Z_*)||_F
    <=gamma_ret^(-1)(delta/sqrt(2)+kappa_1 delta).   (7a)
This is the promised explicit inversion constant for the rotated nonreflection case; the full-rank retained-map verification is exact, not based on numerical genericity.

Let gamma_aug>0 be the least positive singular value of the compressed frame analysis map on W_aug. Because W_aug contains every pure-source x_jx_j^T, pure-exterior h_a h_a^T, anchor cross and anchor scalar functional, finite-dimensional inversion gives a computable C_aug>0 such that
  ||M_G(G W G^T)-c||_2 <= C_aug delta,             (8)
  tr(QWQ)<=C_aug delta,                            (9)
  ||anchor_cross(Z)||+|Z_cc-1|<=C_aug delta.      (10)
Here W=Z_(1:n,1:n)>=0. In particular the source decoder X=G W G^T is PSD and has original frame residual O(delta), WITHOUT any additional square-root loss.

Since tr W<=T and W>=0,
  ||W-PWP||_F <=C_aug delta+sqrt(2T C_aug delta).
Because PWP=G^T XG, (10) yields
  ||Z-[(G^T XG) direct-sum [1]]||_F
    <=C'_aug delta+sqrt(2T C_aug delta).           (11)
Combine (6), (11), the source distance-to-fibre modulus and the isometric embedding to get
  dist(Y,E(C_c))
     <=omega_G(C_aug delta)+C_1 delta+C_2 sqrt(delta)
     <=omega_G(C delta)+C sqrt(delta).             (12)

For the reverse source term, embedded competitors Y=E(X) have Frobenius distances exactly dist(X,C_c). Every final compressed projector restricted to E(X) is a known scalar multiple of an original g_jg_j^T (or zero), hence
  ||A_U(E(X)-E(X_*))||_2<=C_E ||M_G(X)-c||_2.
Thus
  omega_final(delta)>=omega_G(delta/C_E).        (13)

For c!=0, E(X_*) has rank rank(X_*)+1>=2. The outer exterior dimension is Q_1-rank =N-(n+1)>=5M-d+2. The space of cross blocks from any two positive target support eigenvectors into Q_1 has dimension 2[N-(n+1)]>N-1. Its first-basis diagonal variation has trace zero, so a nonzero cross block K exists with diag(K+K^T)=0. Under the reflection R, the second-basis variation is its negative, hence also zero. The same dimension statement survives a rotation of one output coordinate by adding at most one independent linear constraint. Put
  G_0=K^T E(X_*)^dagger K>=0.
Then
  Y(t)=E(X_*)+t(K+K^T)+t²G_0
      =(I+tK^T E(X_*)^dagger)E(X_*)(I+tE(X_*)^dagger K)
is PSD of the SAME target rank. Its data residual is Theta(t²), because trace is measured and G_0!=0, while dist(Y(t),E(C_c))>=sqrt2 t||K||. Hence
  omega_final(delta)>=c sqrt(delta).              (14)
Combining (12)-(14) gives the sharp law (1).

For c=0, since G is Parseval, c=0 forces X_*=0. In the final lift E(0)=v v^T is rank one, v=F^T e_c has every coordinate nonzero. Equations (7)-(10) control the source compressed block W and its trace by O(delta), and the outer exposing certificate controls Q_1 exterior trace by O(delta). Therefore in the decomposition of Y relative to v and v^perp, the v^perp PSD principal block has trace O(delta). The trace residual controls its scalar vv^T coefficient to O(delta), while the first-basis diagonal equations
  r_j=(a-1)v_j²+2v_j z_j+(Y_(v^perp))_jj
control each anchor-to-orthogonal coordinate z_j linearly, because every v_j!=0. Thus ||Y-E(0)||_F=O(delta); the reverse linear lower bound follows from scaling E(0). This proves omega_final(t)~t at zero source.

Semialgebraic one-variable growth for compact PSD residual sublevels gives attained rational error exponents. The standard source PSD tangent-cone dichotomy gives omega_G(t)=O(t) or omega_G(t)>=c sqrt(t); hence the sharp non-Lipschitz modulus preservation follows from (1).

## 6. Immediate corollary: sharp general SDP universality at polynomial order

Let A:S^m->R^p be ANY real trace-controlled PSD inverse map. The earlier codimension-adaptive tensor compiler (CODIMENSION_TWO_UNIVERSAL_THEOREM.md, Part 3 on the inherited branch) gives a PSD-positive partial-trace retraction and a rank-one Parseval frame G in dimension d=mr, where
  s=codim range A*, r=2r_0+1, r_0=max{k:k(k+1)/2<=s+1},
and M<=2[ d(d+1)/2-s]. Its rank-one frame measurement modulus is equivalent to the original source modulus, because partial-trace compression is PSD-positive and its measurement kernel is exactly the tensor embedding of ker A.

Composing that compiler with Theorem 1 gives an explicit real two-basis normal form of order
  N<=6M-d+4=O(m²(s+1))<=O(m^4),
with ALL observations strictly positive, ALL basis overlaps nonzero, arbitrary-rank ambient exact recovery, globally positive decoding, exact objective identity, and the SHARP original-source modulus law
  omega_final(t)~omega_original(t)+sqrt(t)  for nonzero feasible source datum,
  omega_final(t)~t  at the zero source.
In particular EVERY non-Lipschitz PSD recovery modulus is preserved, with no alpha/2 degradation.

For fixed codimension s, N=O_s(m²) uniformly over arbitrarily dense noncommuting source measurement spaces. This is a genuinely universal sharp transfer theorem with polynomial order, not the still-impossible-within-strong-model unrestricted quadratic order N=O(m²+p).

## 7. Hostile audit

- Previous false shortcut: a source-only rank-one projector cannot generally be recovered from the two-zero frame's measured span; HERE it is explicitly inserted as a measured projector in a NEW outer Parseval compiler, in a balanced additional tight-frame group.
- The external ONB is the standard coordinate basis in R^M. It is admissible because its pullback through G is the original Parseval frame, even if the original d-dimensional W has no admissible ONB.
- Balanced tightness is exact: sum e_j e_j^T/2 + sum (Pe_j)(Pe_j)^T/2 +sum h_a h_a^T/2=I_M. No unproved whitening or tiny cone-interiority lemma is used.
- The source-only outputs cancel INNER cross blocks by construction, before using any PSD square-root estimate; outer reflection averaging cancels OUTER cross blocks. This is precisely why the source residual is O(delta).
- The pure-exterior frame outputs have target zero ONLY in the compressed intermediate model; the final measured two-basis data are STRICTLY POSITIVE because of the added anchor.
- The construction covers nonsingleton feasible sets; exact fibre identity is proved against all ambient PSD matrices.
- The upper modulus uses PSD compression, positive exterior mass and Frobenius block Cauchy-Schwarz with explicit, computable singular-value constants. It never assumes a rank bound on Y.
- Matching sqrt lower curves are PSD by an exact Gram factorization and preserve target rank. The zero target is separately handled.
- The dimension is LINEAR in M, not O(M²): n=M and the enriched frame length is only 3M-d.
- The theorem does NOT defeat the generic N=Omega(m^(8/3)) lower bound for globally positive exact source retracts. It transforms an existing rank-one compiler of M=Omega(m^(8/3)) or larger; it does not construct a universally small compiler.
- Output coefficients can be defined by finite algebraic operations and grid avoidance. Uniform Turing polynomial bit complexity needs finite positive condition/separation promises; none is invented.
- This is a self-audited proof requiring external referee validation and a comprehensive novelty check before publication claims.
