# Milestone 32 — explicit O(d²+M) complement-twin compiler with POLYNOMIAL CONDITIONING constants

2026-11-08. Strengthens the universal sharp construction in Milestone 31. No conic Caratheodory sparsification is required in this version: a source frame with M columns gives an explicitly indexed rank-one Parseval frame of 4d²+2M vectors, with an explicit inverse-analysis bound POLYNOMIAL in natural source conditioning parameters. The source PSD inverse problem and its feasible-set recovery modulus are preserved at linear residual scale, for all ambient PSD competitors of unrestricted rank. The subsequent single signed-anchor two-basis dilation has order N<=4d²+6d+2M+4.

## 1. Statement

Let G=[g_1,...,g_M] in R^(d x M) be real Parseval, GG^T=I_d, with nonzero columns. Let W=span{g_jg_j^T} and L:S^d->R^M be its quadratic-frame analysis map. Define the strictly positive finite-dimensional constants
  sigma_W=inf{||L(H)||_2:H in W,||H||_F=1},
  sigma_B=sigma_min([g_{i_1},...,g_{i_d}]),
where I={i_1,...,i_d} is ANY choice of d linearly independent frame columns. Such I exists since G has full row rank. For d>=1 put
  K_an=10 d(1+sigma_W^(-1)+sigma_B^(-2)).             (1)

Let
  J(Z)=Z direct-sum(trZ I_d-Z).
Then there is an explicitly listed REAL Parseval frame K in R^(2d x M') with
  M'=4d²+2M,                                         (2)
whose rank-one projectors span EXACTLY
  Wtilde={S in S^(2d):J*(S) in W}.                    (3)
In particular Wtilde contains a full ONB of admissible rank-one projectors.

Writing Ltilde(Y)=(k_j^T Y k_j) for the new frame, and D0(Y)=Y_(top d-by-d), the following hold for EVERY symmetric Y and every source target Z_*:
  ||L(D0(Y)-Z_*)||_2 <=K_an ||Ltilde(Y-J(Z_*))||_2,  (4)
  ||Y-J(D0(Y))||_F
      <=(1+d)K_an ||Ltilde(Y-J(Z_*))||_2.             (5)
The second formula uses ||J||_(F->F)<=d. All constants are explicit and no positivity or small-noise assumption is needed in (4)-(5).

For every H in S^d,
  K_an^(-1)||L(H)||_2
    <=||Ltilde(J(H))||_2
    <=(d/sigma_W)||L(H)||_2.                         (6)
Thus the compressed/source PSD recovery moduli satisfy the explicit two-sided inequalities
  omega_comp(t) <= d omega_source(K_an t)+(d+1)K_an t,
  omega_comp(t) >= omega_source((sigma_W/d)t).        (7)
They apply to NONSINGLETON fibres and all unrestricted-rank PSD competitors.

A single signed-anchored two-ONB lift of the resulting explicit frame has order
  N<=3(2d)+M'+4=4d²+6d+2M+4.                        (8)
For all nonzero source feasible data its full ambient worst-case modulus is
  omega_final(t)~omega_source(t)+sqrt(t);
at zero source data it is Theta(t). Strictly positive measurements, nonzero basis overlaps, globally positive source decoding, exact full-fibre correspondence and objective equality are retained. The final signed-exposure constants are polynomial in N, the explicit anchor nonzero-gap reciprocal, sigma_W^(-1), sigma_B^(-2), and the resulting frame analysis gap.

If the original source frame has first been conically sparsified to M<=2q<=d(d+1), equation (8) gives
  N<=6d²+8d+4,
while the tighter existential/singular-value-certified variant in Milestone 31 gives N<=4d²+8d+4.

## 2. Four explicitly indexed frame families

Fix I of d independent source columns, set
  S_I=sum_{i in I}g_i g_i^T <=I_d,
  epsilon=1/(8d),
  w_j=3/4 if j in I, otherwise w_j=1.
The following TWO groups together form a Parseval frame of R^(2d):

(A) for each ordered i,k in I and each sign s=+/-1, take
  a_(i,k,s)=sqrt(epsilon)(g_i,s g_k).
There are 2d² such columns. Summing the plus/minus projectors gives the covariance
  (2epsilon d) diag(S_I,S_I)=diag(S_I/4,S_I/4).

(B) for every j=1,...,M take
  b_(j,1)=(sqrt(w_j)g_j,0),
  b_(j,2)=(0,sqrt(w_j)g_j).
There are 2M such columns. Their covariance is
  diag(I-S_I/4,I-S_I/4).
Hence groups A+B have covariance I_(2d).

Independently, let H be the d-dimensional Parseval frame with d² vectors
  h_i=e_i/sqrt(d) (i=1,...,d),
  h_(i,j,+)=(e_i+e_j)/sqrt(2d),
  h_(i,j,-)=(e_i-e_j)/sqrt(2d) (i<j).
Indeed sum_h hh^T=I_d and span{hh^T}=S^d.
Define group (C) for every h by
  c_(h,+)=(h,h)/sqrt2, c_(h,-)=(h,-h)/sqrt2.
This group has 2d² vectors and covariance I_(2d). Every c rank-one projector has source pullback (||h||²/2)I in W.

Scale ALL columns of A+B and of C by 1/sqrt2. Their union K is Parseval and has the claimed M'=4d²+2M columns. No numerical optimization or hidden root solving is involved beyond explicitly listed positive square roots.

**Allowed pullbacks.** With J*( [A,C;C^T,B])=A-B+tr(B)I, the pullbacks are, respectively:
  A: proportional to g_i g_i^T-g_k g_k^T+||g_k||² I;
  B: proportional to g_jg_j^T or ||g_j||² I-g_jg_j^T;
  C: proportional to ||h||² I.
All belong to W. Therefore every new projector belongs to Wtilde.

**Exact span.** Group B spans diag(W,0) and diag(0,W). Group C spans all diag(T,T), T in S^d, as well as all symmetric cross blocks (T,T). Signed differences of the + and - ordered pair columns in A isolate pure cross blocks with upper-right g_i g_k^T; since the selected d columns G_I form a BASIS of R^d, these d² products span ALL d-by-d real cross matrices, including antisymmetric parts. Hence the projectors span every block matrix with A-B in W and arbitrary cross C, exactly Wtilde. The paired coordinate vectors
  (e_i,e_i)/sqrt2, (e_i,-e_i)/sqrt2
form a full admissible ONB; their projectors are proportional to existing C family projectors, so the signed frame theorem applies.

## 3. Explicit inverse-analysis conditioning

Let Y=[A,C;C^T,B] be an arbitrary real symmetric 2d-by-2d matrix. Write S=A+B, H=(A-B)/2. Its orthogonal projection onto Wtilde is
  Pi_Wtilde(Y)
   =[ S/2+Pi_W(H), C;
      C^T,        S/2-Pi_W(H) ],
where Pi_W is Frobenius-orthogonal projection onto W. Thus
  ||Pi_Wtilde(Y)||_F²
   =2||S/2||_F²+2||Pi_W H||_F²+2||C||_F².          (9)

Partition the frame output vector as y=(y_A,y_B,y_C) for the three groups in Section 2, AFTER the global 1/sqrt2 scaling.

(a) Group B measures (w_j/2)g_j^T A g_j and (w_j/2)g_j^T B g_j, with w_j>=3/4. Therefore
  ||Pi_W H||_F <=(4sqrt2)/(3sigma_W) ||y_B||_2.    (10)

(b) Group C outputs, for each h, the two numbers
  y_(h,+)= [h^T S h+2h^T C h]/4,
  y_(h,-)= [h^T S h-2h^T C h]/4.
Their sum s_h=(1/2)h^T S h. For h_i=e_i/sqrt d,
  S_ii=2d s_(h_i).
For h_(i,j,+/-),
  S_ij=d[s_(h_ij,+)-s_(h_ij,-)].
Summing squares and applying the inequality (u+v)^2<=2(u²+v²) gives
  ||S||_F<=4d ||y_C||_2.                            (11)

(c) Group A outputs
  y_(i,k,+/-)=(epsilon/2)[g_i^T A g_i+g_k^T B g_k
                         +/-2 g_i^T C g_k].
Hence
  g_i^T C g_k=[y_(i,k,+)-y_(i,k,-)]/(2epsilon).
Writing G_I=[g_i]_(i in I), we have
  ||G_I^T C G_I||_F <= ||y_A||_2/(sqrt2 epsilon).
Since G_I invertible,
  ||C||_F <= ||y_A||_2/(sqrt2 epsilon sigma_B²).    (12)

Combining (9)-(12), epsilon^(-1)=8d and
  ||Pi_Wtilde(Y)||_F<=K_an ||Ltilde(Y)||_2
with K_an in (1). This proves a global positive singular-gap estimate for the compiler, not just an exact span claim.

## 4. Derive the source residual and PSD retraction bounds

Since Wtilde=(J*)^(-1)(W), the analysis kernel is
  ker Ltilde=Wtilde^perp=J(W^perp)=J(ker L).          (13)
This equality holds over the entire REAL symmetric matrix space, not only over PSD matrices.

For T=Y-J(Z_*), decompose
  T=S0+J(H0),  S0=Pi_Wtilde(T), H0 in W^perp.
Taking top blocks gives
  D0(Y)-Z_*=D0(S0)+H0.
Thus
  L(D0(Y)-Z_*)=L(D0(S0)),
and Parseval tightness implies ||L||_(F->2)<=1. From Section 3,
  ||L(D0(Y)-Z_*)||<=||S0||<=K_an ||Ltilde(T)||,
proving (4). Also
  Y-J(D0(Y))=S0-J(D0(S0)),
so
  ||Y-J(D0(Y))||<=(1+||J||)||S0||
                  <=(1+d)K_an||Ltilde(T)||,
proving (5).

For source H, use (4) with Y=J(H),Z_*=0 to derive the first inequality (6). For the second, write H=Pi_W H+H_perp; then L(H)=L(Pi_W H), and J(H_perp) belongs ker Ltilde. Parseval gives ||Ltilde||<=1 and ||J||<=d, so
  ||Ltilde(J(H))||<=d||Pi_W H||<=d sigma_W^(-1)||L(H)||.
This proves (6).

For PSD Y, its top block D0(Y) is PSD and J(D0(Y)) is PSD. Hence (4)-(5) imply (7) by taking nearest source feasible points and using linear embedded-map comparisons. The claim is valid for all PSD ranks, any feasible c, and no local rank constraint.

## 5. Effective construction and scope

Selecting I is a finite rank-revealing pivot operation on G. Since GG^T=I, the Cauchy--Binet identity gives
  sum_|I|=d det(G_I)^2=1,
so there exists I with |det G_I|>=binom(M,d)^(-1/2). Since ||G_I||_op<=1, its least singular value obeys
  sigma_B>=binom(M,d)^(-1/2)
for such a selected maximum-volume subset. This worst-case lower bound can be exponentially small; sigma_B^(-1) is therefore retained as an explicit natural condition parameter, not falsely bounded by a polynomial in d alone.

All new frame coefficients use only source algebraic coefficients and rational square roots. The raw frame has O(M+d²) columns; its conditioning loss (1) is POLYNOMIAL in d,sigma_W^(-1),sigma_B^(-1), with no hidden dependence on exponentially tiny conic sparsification weights.

The signed final two-basis stage still introduces its own exposing gap (exactly >=2) and finite anchor/analysis singular-gap constants. These are computable on the returned finite matrices. The uniform polynomial-Turing-bit construction question for arbitrary rational SDP inputs is not solved by this milestone; only conditional algebraic-arithmetic and well-conditioned weak numerical reductions are claimed.

## Hostile audit

1. Using all M² source column pairs is NOT required: d independent source columns already span all cross blocks. The covariance loss is repaired by weakening those d separated source columns from weight 1 to weight 3/4; no indefinite subtraction is used.
2. Group C is essential to measure arbitrary common diagonal matrix blocks. Group B is essential for original W source information and the independent diagonal differences; without it the span may miss scalar diagonal differences.
3. Every group is separately or jointly tight by EXPLICIT sums. No random genericity, determinant avoidance or conic convexity is hidden in the new compiler.
4. The polynomial inverse constant is proved by direct recovery of the three independent block components, not simply asserted by finite-dimensional norm equivalence.
5. The exact kernel identity and positive retraction are unchanged from Milestone 31, so all source singularity depths and moduli are retained.
6. The final strictly-positive two-basis lift requires the standard small-anchor signed construction; its coefficients are finite algebraic, and it does not use any admissible source ONB or strict stress.
