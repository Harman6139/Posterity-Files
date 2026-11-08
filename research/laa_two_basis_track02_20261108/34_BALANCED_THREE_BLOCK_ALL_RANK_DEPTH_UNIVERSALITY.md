# Milestone 34 — THREE-BLOCK BALANCED POSITIVE LIFT preserves SHARP moduli AND facial depth for ALL ranks

Date 2026-11-08. Complete real constructive theorem. This repairs the sole rank-one depth exception of Milestone 33 while retaining universal sharp non-Lipschitz modulus transfer, all-rank ambient PSD fidelity, positive decoding and strictly positive two-basis measurements. No source strict stress, admissible ONB, target, or facial chain is required. The unrestricted generic O(m²+p) size conjecture remains unresolved, but the SHARPNESS question and exact depth transformation are fully resolved within rank-one Parseval systems and, via the earlier codimension-adaptive compiler, for arbitrary finite-dimensional trace-controlled SDP systems with size O(m²(s+1)).

## Theorem 1 (all-rank, all-depth rank-one source representation)

Let G in R^(d x M), GG^T=I_d, be a real rank-one Parseval frame; W=span{g_jg_j^T} and q=dim W. For every nonempty PSD source fibre
  F_c={Z>=0:(g_j^T Zg_j)_j=c},
define its worst-case distance-to-fibre recovery modulus omega_c(t). Let k be its facial-reduction depth, computed using the measured operator system W and a maximal-rank feasible matrix. Then there is a finite algebraic two-real-orthonormal-basis construction on order
  N<=8d²+11d+2q+4 <=9d²+12d+4,              (1)
with positive affine encoding and positive linear decoding, exact full-ambient PSD fibre identity, exact objectives, no zero basis overlaps, and STRICTLY POSITIVE observed target data for every feasible source datum including zero.

Its sharp modulus and depth law are
  omega_final(t) ~ omega_c(t)+sqrt(t),   depth_final=max(1,k),  if c!=0;
  omega_final(t) ~ t,                   depth_final=1,         if c=0.
Here ~ is two-sided fixed-instance comparability and all ambient PSD competitor ranks are allowed. For c!=0 the entire non-Lipschitz source modulus (not merely exponent) is therefore preserved.

The encoder has the form
  E(Z)=F^T([J_3(Z)] direct-sum [1])F,
  J_3(Z)= Z direct-sum (trZ I_d - Z/2)
                 direct-sum (trZ I_d - Z/2).             (2)
The decoder is the leading original d-by-d principal block of FYF^T. For Z!=0 with rank r,
  rank E(Z)=r+2d+1,
while E(0) has rank one. All source linear objectives are represented EXACTLY as ambient linear objectives on every symmetric matrix. The Frobenius norm distortion is explicit:
  ||J_3(H)||_F²=3||H||_F²/2 +2(d-1)(trH)².                (3)

A version avoiding conic sparsification of the new compiler has
  N<=14d²+9d+3M+4,                                    (4)
and an analysis conditioning loss polynomial in d, the nonzero singular values of the original frame analysis and of a selected independent d-column submatrix.

## 2. Globally positive lift with STRICTLY positive auxiliary blocks

For Z>=0 with tau=trZ,
  tau I_d-Z/2 >=(tau/2)I_d.
Thus J_3 is linear and PSD-positive, with positive principal-block decoder D_0(Y)=Y_top. If tau>0, BOTH auxiliary blocks are positive definite for EVERY source rank, including rank ONE. This is the decisive improvement over J_2(Z)=Z direct-sum (trZ I-Z) from Milestones 31-33, where a rank-one source creates an auxiliary null direction.

The exact Frobenius norm formula (3) follows by expanding two copies of ||trH I-H/2||²:
  ||trH I-H/2||²=(d-1)(trH)²+||H||²/4.
The embedding is injective and source distances are comparable with explicit constants between sqrt(3/2) and sqrt(3/2+2d(d-1)).

On an arbitrary symmetric block matrix B in S^(3d), with diagonal d-by-d blocks A0,A1,A2 and arbitrary off-diagonal blocks, the dual source pullback is
  J_3*(B)=A0-(A1+A2)/2+(tr A1+tr A2)I_d.
Because I belongs to W, the allowed measurement operator system is exactly
  W_3={B in S^(3d):A0-(A1+A2)/2 in W}.                  (5)
It has dimension
  q_3=dim W_3=D_(3d)-(D_d-q)=4d²+d+q.                   (6)

## 3. EXPLICIT complete orthonormal basis of admissible rank-one vectors

Let alpha=(1,-1/2,-1/2). Define unit REAL vectors
  h(theta)=(1/sqrt(3), sqrt(2/3)cos(theta),
                        sqrt(2/3)sin(theta)) in R³.
They satisfy h(theta)^T diag(alpha) h(theta)=0.

The THREE vectors
  h(0),h(2pi/3),h(4pi/3)
are orthonormal, because their inner products are 1/3+(2/3)cos(2pi/3)=0 for distinct angles. Thus for every source coordinate e_i, the three vectors
  h(2pi j/3) tensor e_i, j=0,1,2
form an admissible complete ONB of R^(3d). Their rank-one projector source pullbacks are scalar multiples of I_d, by the alpha-isotropy identity. No knowledge of the original operator system beyond I in W is required.

For a second, spanning set of alpha-isotropic directions, take the FIVE vectors
  h(2pi j/5), j=0,...,4.
Their projectors sum to (5/3)I_3 and SPAN the five-dimensional space
  alpha^perp={H in S³:<H,diag(alpha)>=0}.
Proof of span: for any symmetric H, the function theta->h(theta)^T H h(theta) is a real trigonometric polynomial with frequencies 0,1,2. If it vanishes at all five fifth roots of unity, discrete Fourier inversion makes every Fourier coefficient zero, hence it vanishes identically. Its only possible H then is a scalar multiple of diag(alpha), as inspection of cos(theta),sin(theta),cos(2theta),sin(2theta) coefficients shows. Thus the projector span has codimension one and is exactly alpha^perp.

Combining the 3-vector orthonormal isotropic frame with the 5-vector isotropic frame scaled sqrt(3/5), each with an additional coefficient 1/sqrt(2), gives an explicit EIGHT-vector Parseval frame in R³. Every projector is alpha-isotropic, its projector span is alpha^perp, and it contains positive multiples of an entire admissible ONB.

## 4. Universal allowed Parseval compiler on 3d with EXACT projector span

Let I be a set of d independent source-frame columns; such a set exists. Put
  S_I=sum_{j in I}g_jg_j^T<=I_d,
  epsilon=1/(16d),
  w_j=3/4 if j in I, else w_j=1.
Construct THREE groups of real vectors in R³ tensor R^d, with block coordinates indexed 0,1,2.

(A) Cross-pair group: for every unordered pair of DISTINCT blocks a<b, each ordered pair j,k in I and each sign +/- take
  sqrt(epsilon)(e_a tensor g_j +/- e_b tensor g_k).
There are 3*(2d²)=6d² vectors. Every rank-one projector is allowed since its pullback is a linear combination of g_jg_j^T, g_kg_k^T and I.

(B) Separated source group: for each j=1,...,M and a=0,1,2 take
  sqrt(w_j) e_a tensor g_j.
There are 3M vectors, all allowed.

For each block a, the A covariance contribution is 4epsilon d S_I=S_I/4; the B contribution is I_d-S_I/4. Cross covariance cancels by pairing signs. Hence groups A+B form a Parseval frame on R^(3d).

(C) Isotropic tensor group: in R^d take the explicit d²-vector Parseval frame
  k_i=e_i/sqrt d,
  k_ij,+/-=(e_i +/-e_j)/sqrt(2d), i<j,
whose rank-one projectors span ALL S^d. Take all tensor products
  h_l tensor k_b
between the 8-vector alpha-isotropic Parseval frame of Section 3 and the d²-vector source frame. There are 8d² vectors; their covariance is I_3 tensor I_d=I_(3d).
Every rank-one projector in this group pulls back through J_3* to a scalar multiple of I_d, hence is allowed.

Finally scale ALL vectors in A+B and C by 1/sqrt2. The resulting frame K is Parseval, with
  M_raw=14d²+3M,                                      (7)
and every rank-one projector belongs to W_3.

**Exact span.** Group B spans separately the three diagonal measured blocks diag(W,0,0), diag(0,W,0), diag(0,0,W). Signed differences of group A vectors isolate arbitrary off-diagonal d-by-d cross blocks between EVERY pair of output blocks: the products g_j g_k^T for j,k in I form a basis of all real d-by-d matrices, including antisymmetric cross parts. Group C spans the tensor-product operator space S^d tensor alpha^perp, because the source k projectors span S^d and the isotropic h projectors span alpha^perp. In particular it spans ALL diagonal triples (A0,A1,A2) for which A0-(A1+A2)/2=0. Adding the independent W-valued diagonal blocks from group B gives EVERY diagonal triple satisfying A0-(A1+A2)/2 in W. Therefore the full projector span equals exactly W_3, with NO missing cross or scalar direction.

Use exact positive conic Caratheodory elimination: reserve positive portions of q_3 independent frame projectors, express the residual identity by at most q_3 frame projectors, and add the reserved terms back. This yields an allowed Parseval frame with
  M_comp<=2q_3=8d²+2d+2q,                              (8)
whose projectors still span W_3 and thus contain the admissible ONB projectors of Section 3 in their linear span. Its construction uses finitely many real algebraic operations and verified linear independence comparisons. Exact algebraic conditioning can be read from the resulting finite frame.

## 5. Exact PSD fibre and LINEAR noisy positive retraction

Let M_3 be the rank-one measurement map for the frame in Section 4, and let L be the original frame map. Since W_3=(J_3*)^(-1)(W) and J_3 is injective, duality and dimension give
  ker M_3 = W_3^perp=J_3(W^perp)=J_3(ker L).         (9)
For every source feasible datum c,
  {B>=0:M_3(B)=M_3(J_3(C))}=J_3(F_c),            (10)
because the kernel equality forces B=J_3(Z) with L(Z)=c, and positivity of the top principal block forces Z>=0; conversely J_3 is positive.

For ARBITRARY symmetric B, define the positive decoder D_0(B)=B_(top d-by-d) and the linear off-model map R_0(B)=B-J_3(D_0(B)). The two maps
  B->M_3(B)
and
  B->(R_0(B),L(D_0(B)))
have identical kernel J_3(ker L). Therefore there is a computable finite positive singular-value constant K such that, for arbitrary target C and every B,
  ||B-J_3(D_0(B))||_F+
    ||L(D_0(B))-c||_2
       <=K ||M_3(B)-M_3(J_3(C))||_2.               (11)
If B>=0 then D_0(B)>=0 and J_3(D_0(B))>=0, so this is a globally PSD-positive O(delta) retraction. Embedded source matrices give the converse residual comparison by the same kernel identity. Using (3), the compiled source and original recovery moduli are therefore equivalent at the same t scale:
  omega_comp(t)~omega_source(t),                    (12)
including NONSINGLETON fibres and arbitrarily high singularity degree. Crucially no extra sqrt arises in this first stage.

For the RAW frame (7), one may instead obtain a polynomial conditioning estimate analogous to Milestone 32, using the three independent data blocks: the separated g_j outcomes control the W-valued diagonal components via sigma_W^(-1); the eight isotropic Fourier directions combined with the d² source frame control alpha^perp-valued symmetric components with O(d) inverse; and the three cross-pair groups recover arbitrary cross blocks through the inverse selected source basis with factor O(d sigma_B^(-2)). Thus K can be bounded by a universal polynomial in d,sigma_W^(-1),sigma_B^(-2), with no unknown generic singular gap. The conically sparsified variant is more compact but may have smaller singular values, which remain computable.

## 6. EXACT facial depth preservation for every NONZERO feasible source fibre

Let C_* be a maximum-rank feasible source matrix, with E=ranC_* and tau=trC_*>0. By construction
  tau I-C_*/2 >=(tau/2)I>0.
Hence J_3(C_*) is positive definite on its minimal target support
  E direct-sum R^d direct-sum R^d.
Every compiled facial-reduction support is of the form E_i direct-sum R^d direct-sum R^d. Indeed if a measured compiled certificate S in W_3 has PSD compression to that support and zero target pairing, positivity and the STRICTLY POSITIVE bottom two target blocks force its compressed bottom rows and cross blocks to vanish. Thus its bottom diagonal blocks are zero, and its top block A0 belongs to W (the W_3 membership condition). Its top compression is exactly a legitimate original facial certificate on E_i. Every compiled reduction therefore induces one original reduction. Conversely any original compressed certificate A in W lifts as diag(A,0,0) in W_3, performing the same step on E_i and leaving the positive bottom support untouched. Thus
  depth_comp=depth_source=k.                           (13)
This holds for EVERY nonzero feasible C_* rank, including rank one, and for nonunique fibres (use their maximum-rank member).

For zero datum c=0, Parseval trace control forces F_c={0}. Both source and compiled zero targets are exposed by the measured identity in one step, so they both have depth one.

## 7. Single positive-data signed two-ONB lift: exact rate AND depth

The frame in Section 4 is Parseval on order 3d and its operator span W_3 contains the complete admissible ONB from Section 3. Apply the explicit signed-anchor reflection construction of Milestones 27–31 using three weighted columns per admissible ONB direction, the compiled frame columns at weight 4, and three additional pure-anchor columns. It yields
  F in R^((3d+1) x N), FF^T=I, F D F^T=0,
  N<=3(3d)+2q_3+4
    =8d²+11d+2q+4 <=9d²+12d+4.
The orthogonal reflection R=2F^TF-I and its optional equal-weight nonreflection variant U carry a measured PSD exposing certificate
  S0=D+UDU^T>=2(I-F^TF),
and every column has nonzero anchor coordinate. Therefore all target observations are STRICTLY positive and all transition entries can be made nonzero by finite algebraic parameter avoidance.

The exact full ambient fibre equals
  {F^T([J_3(Z)] direct-sum[1])F:Z in F_c}
for every feasible c, with no ambient PSD rank restriction. The positive decoder takes the original top d-by-d principal block of FYF^T. Embedded differences have norms exactly ||J_3(Z-Z')||, and source linear costs C lift to F^T((C direct-sum0_d direct-sum0_d) direct-sum[0])F, giving objective equality for ALL ambient symmetric Y.

The even part of the two reflection measurement lists cancels exterior cross blocks exactly. The exposing certificate controls exterior PSD mass O(delta), and PSD block positivity bounds exterior crosses by O(sqrt delta). The compressed W_3 data are therefore O(delta), and the positive retraction (11) recovers source residual O(delta). For all ambient PSD competitors,
  omega_final(t)<=C omega_source(Ct)+C sqrt(t).
Embedded competitors give omega_final(t)>=omega_source(c t). For any nonzero source fibre, rank of the final target is >=2; a support-to-exterior invisible cross direction exists by the same dimension argument as Milestones 22/31, with a PSD Gram-repaired curve giving omega_final(t)>=c sqrt(t). Hence
  omega_final(t)~omega_source(t)+sqrt(t).              (14)
At zero source data the final target is the rank-one anchor and has Lipschitz modulus Theta(t).

The facial-reduction depth of the signed-anchor lift is max(1,k_comp), because its exposing certificate removes the full outer face and can be merged with the first compressed facial reduction step; intersection of any ambient chain with the embedded support gives the reverse inequality. Thus, combining (13),
  depth_final=max(1,k_source).                        (15)
This proves Theorem 1 in its entirety.

## 8. General-linear SDP consequence and remaining size frontier

The independently committed codimension-adaptive tensor rank-one compiler takes ANY normalized trace-controlled real PSD measurement operator system L subset S^m of codimension s to a rank-one Parseval compiler on order d=O(m sqrt(s+1)), with positive partial-trace decoder and exact O(delta) source residual fidelity. Applying Theorem 1 produces a two-basis model of order
  N=O(d²)=O(m²(s+1))
with exact full feasible-set correspondence, source objective preservation, SHARP worst-case modulus transformation, and facial depth transformation max(1,k) for every feasible fibre. No strict stress and no source rank assumption are needed. For fixed codimension s this is quadratic in m, including dense noncommuting measurements and high facial depth.

This solves the SHARPNESS/FACIAL-DEPTH portion of the Track 02 universality programme for arbitrary trace-controlled PSD linear inverse problems in a polynomial-size, positive-decoder construction. It does NOT prove the requested N=O(m²+p) universal ORDER bound when s=Theta(m²), nor uniformly polynomial Turing bit complexity without explicit conditioning/separation promises. Those remain separate unresolved problems.

## 9. Audit

1. The two auxiliary complements are POSITIVE DEFINITE at every nonzero PSD source, so the rank-one exception of the two-block lift disappears. The zero source remains a separate rank-one anchored case.
2. The three alpha-isotropic vectors at angles 0, 120, 240 degrees form a genuine real orthonormal basis; the five equally spaced directions span alpha^perp by exact Fourier inversion. Both facts are load-bearing and independently checked.
3. The raw compiler's covariance identity uses 4epsilon d=1/4 for each of the THREE output blocks, since each block is incident to two source-pair groups. The separated weights 3/4 restore exactly the missing covariance.
4. The source-frame pullback of every tensor-isotropic projector is a scalar I, which belongs to W by Parseval. Cross-pair pullbacks are differences of original measured rank-one projectors plus scalar trace.
5. The spanning proof includes all skew cross blocks and the alpha-direction W-valued diagonal degrees of freedom; the projectors span EXACTLY W_3.
6. The linear noisy retraction kernel identity holds for ALL symmetric matrices and thus cannot conceal O(sqrt delta) cross-block pollution inside the compiler.
7. The facial-depth proof uses a maximum-rank feasible matrix; it is not restricted to singleton fibres or to full-rank source matrices.
8. The final two-basis matching sqrt curve is PSD by exact Gram factorization and competes against the entire ambient PSD cone.
9. Numerical examples for d=2 (diagonal input) and d=3 (tetrahedral input with no admissible source ONB) verify the full frame span ranks 20 and 43, respectively, and Parseval covariance errors below 2e-15. These are sanity checks, NOT proofs.
10. No assertion of global O(m²+p) SIZE universality, unconditional exact SDP feasibility polynomial time, or external novelty certification is made.
