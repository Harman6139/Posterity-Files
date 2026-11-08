# Milestone 35 — FINAL BALANCED TWO-BLOCK compiler: UNIVERSAL sharp PSD moduli AND depth, including rank one, in O(d²)

Date 2026-11-08. A crucial simplification discovered while auditing Milestones 31-34. The two-block complement compiler already has a full admissible ONB and exact rank-one span. Its only depth defect at rank-one targets is eliminated by MATCHING THE SOURCE AND NEGATIVE-COMPANION COEFFICIENTS. There is NO NEED for a third block. This theorem supersedes the three-block depth repair of Milestone 34 with smaller order and better constants. It is proved for all real rank-one Parseval source measurement systems, every nonempty feasible PSD fibre, all competitor ranks, all facial depths, and no strict-stress hypothesis.

## Theorem A — optimal two-block structure and sharp universal recovery

Let G=[g_1,...,g_M] in R^(d x M) be a nonzero-column Parseval frame, GG^T=I_d. Let W=span{g_jg_j^T}, q=dim W, L(Z)=(g_j^T Zg_j)_j and F_c={Z>=0:L(Z)=c}, with c any nonempty feasible datum. Let k be the facial-reduction depth of the source fibre relative to W, and omega_c its full-cone worst-case distance-to-fibre recovery modulus.

Fix the GLOBAL cone-positive real-linear embedding
  J(Z)=(Z/2) direct-sum (trZ I_d-Z/2)                 (1)
from S^d into S^(2d). Its positive linear decoder is
  D0(Y)=2 Y_(top d-by-d).                            (2)
There is an explicit algebraic rank-one Parseval frame on R^(2d), whose projectors span exactly
  Wtilde={ [A,C;C^T,B] in S^(2d): A-B in W },
and whose span contains a COMPLETE orthonormal basis of admissible rank-one projectors. A frame with at most
  Mtilde<=2 dim Wtilde=3d²+d+2q
vectors exists by exact conic elimination. Alternatively an explicitly indexed frame of
  Mtilde=4d²+2M
vectors is given in Milestone 32, with a polynomial analysis inverse bound in source conditioning parameters.

For every original feasible datum c, the compiled PSD fibre equals J(F_c), exactly, including NONSINGLETON F_c and unrestricted PSD competitor rank. Its source and compiled recovery moduli are equivalent at the SAME residual scale:
  omega_comp(t)~omega_c(t).                          (3)

**NEW RANK-ONE DEPTH CLAIM.** For EVERY nonzero feasible c, including fibres whose maximum feasible rank is exactly ONE, the compiled facial-reduction depth is EXACTLY k. For c=0, both source and compiled zero-fibre depths are one.

Applying a SINGLE signed-anchor two-orthonormal-basis dilation to the compiled frame gives order
  N<=3d²+7d+2q+4<=4d²+8d+4,                      (4)
with strictly positive observations, all basis overlaps nonzero, optional nonreflection transition, positive linear decoder, full-rank-unrestricted exact PSD fibre correspondence, and exact linear objective preservation. Its sharp worst-case recovery modulus and facial depth satisfy
  omega_final(t)~omega_c(t)+sqrt(t),
  depth_final=max(1,k)                             (5)
for c!=0; at c=0 the modulus is Theta(t) and the final depth is one.

Every source non-Lipschitz PSD recovery modulus is therefore preserved up to multiplicative constants, including arbitrary exponents below 1/2 and arbitrarily high singularity degree, without any source stress, target rank or admissible source ONB assumptions. This finishes the SHARP UNIVERSAL TRANSFER problem at quadratic order relative to any rank-one Parseval source matrix dimension.

The source positive decoder for the FINAL ambient system is
  D(Y)=2 (F Y F^T)_(1:d,1:d),                        (6)
and the positive encoding is
  E(Z)=F^T([J(Z)] direct-sum[1])F.
Every source cost C is represented by the ambient matrix
  C_tilde=F^T([(2C) direct-sum0_d] direct-sum[0])F,
which obeys <C_tilde,Y>=<C,D(Y)> for EVERY symmetric ambient Y.

For a nonzero source matrix Z of rank r, the final encoded rank is r+d+1; for Z=0 it is one.

## 1. Why this is a two-block breakthrough

The unbalanced complement from Milestone 31 was
  J_old(Z)=Z direct-sum(trZ I-Z).
It had a full admissible ONB, exact measurement span and O(delta) retraction, but at rank-one Z its bottom block trZ I-Z had one zero eigenvalue. This prevented an immediate universal facial-depth correspondence.

A tempting repair is J_eta(Z)=Z direct-sum(trZ I-eta Z), with 0<eta<1. It makes the bottom positive definite but DESTROYS the universal paired admissible ONB unless the source measurement space contains special rank-one projectors. The reason is the mismatch between the coefficients +1 and -eta.

The correct repair is to scale the TOP block too:
  J(Z)=eta Z direct-sum(trZ I-eta Z), eta=1/2.
Now the rank-one pullback of a paired vector (u,+/-u) has the unequal source terms canceled EXACTLY. At the same time, for every nonzero Z>=0,
  trZ I-Z/2 >=(trZ/2) I>0.                 (7)
Thus BOTH requirements are satisfied: an admissible ONB and a STRICTLY POSITIVE auxiliary block at every positive source rank. This needs only two d-by-d blocks, not three.

The exact norm identity for symmetric H is
  ||J(H)||_F² = (1/2)||H||_F²+(d-1)(trH)².           (8)
Hence
  ||H||/sqrt2<=||J(H)||
    <=sqrt(1/2+d(d-1))||H||.
The decoder (2) is globally positive, not merely positive on the solution fibre.

## 2. The rank-one compiler and exact kernel

For a symmetric 2d-by-2d block matrix S=[A,C;C^T,B], the dual action of (1) is
  J*(S)=(A-B)/2+(trB) I_d.                            (9)
Since I in W, membership in (J*)^(-1)(W) is equivalent to A-B in W. Thus the allowed rank-one projector subspace Wtilde in Theorem A is EXACTLY the same one as in Milestones 31-32, with dimension
  qtilde=dim Wtilde=D_d+d²+q=(3d²+d)/2+q.

We recall the EXPLICIT allowed Parseval generators (Milestone 31, Section 3):
 (A) for all ordered frame-column pairs j,k and both signs, (g_j,+/-g_k)/sqrt(2M);
 (B) the two separated vectors (g_j,0),(0,g_j) for every j;
 (C) for the explicit d²-vector Parseval source frame h_i=e_i/sqrt(d) and h_ij,+/-=(e_i+/-e_j)/sqrt(2d), the paired vectors (h,+/-h)/sqrt2.

Each of A, B, C separately has covariance I_(2d); scaling their union by 1/sqrt3 yields a Parseval frame. Every rank-one projector belongs to Wtilde: under (9), the respective pullbacks are
  [g_jg_j^T-g_kg_k^T]/(4M) + ||g_k||² I/(2M),
  g_jg_j^T/2 or ||g_j||²I-g_jg_j^T/2,
  ||h||² I/2,
all in W. The B projectors span independent W-valued top/bottom diagonal blocks; the C projectors span common arbitrary symmetric diagonal blocks and symmetric cross blocks; signed differences of A projectors span EVERY cross matrix g_jg_k^T, and products of full-row-rank source columns span all d-by-d matrices. Thus the projector span is exactly Wtilde.

The vectors u_i,+/-=(e_i,+/-e_i)/sqrt2 (i=1,...,d) are a COMPLETE real orthonormal basis of R^(2d), with
  J*(u_i,+/- u_i,+/-^T)=I_d/2.
Their projectors belong to Wtilde even when the ORIGINAL W has no admissible ONB. Exact conic sparsification (retain qtilde independent projectors, reduce the residual identity to qtilde positive terms) gives Mtilde<=2qtilde without changing tightness or span.

The compiler measurement map Mtilde has exact kernel
  ker Mtilde=Wtilde^perp=J(W^perp)=J(ker L).           (10)
The equality follows from J* surjective and J injective, by duality and the dimension qtilde. It implies that every exact compressed PSD competitor is J(Z) with L(Z)=c and Z>=0, since its top block equals Z/2>=0. Conversely J is globally PSD-positive. This proves exact fibre correspondence WITHOUT assuming source uniqueness or target rank.

For arbitrary symmetric compressed competitor B, the maps
  B -> Mtilde(B)
and
  B -> (B-J(D0(B)), L(D0(B)))
have exactly the same kernel J(ker L). Finite linear inversion therefore supplies explicit computable constants (using the least nonzero singular value of the returned frame analysis map) such that
  ||B-J(D0(B))||+||L(D0(B))-c||
   <=K ||Mtilde(B)-Mtilde(J(Z_*))||.                 (11)
If B>=0 then D0(B)>=0, so J(D0(B))>=0 is a genuine O(delta) PSD retraction onto the encoded source model. Embedded source curves provide the reverse residual and distance comparison. Thus omega_comp~omega_source, with NO extra square root at this stage, even at high facial depth.

## 3. Exact facial-depth preservation for ALL NONZERO source fibres

Fix c!=0 and choose C_* in F_c of maximum rank r>=1, with E=ran C_*. Let tau=tr C_*>0; trace is fixed throughout the fibre because G is Parseval. By (7) the lower d-by-d block of J(C_*) is POSITIVE DEFINITE even when r=1. Consequently the minimal face of J(F_c) is exactly
  E direct-sum R^d,
and the target J(C_*) is positive definite on that support.

Let S=[A,C;C^T,B] in Wtilde be a compressed measured facial-reduction certificate, positive semidefinite on a current support E_i direct-sum R^d containing the target support and with zero pairing against J(C_*). Positivity and zero pairing against a target positive definite on E direct-sum R^d force S to annihilate the ENTIRE lower R^d block. Hence B=0 globally and the cross block vanishes upon restriction to E_i. Since A-B=A belongs to W, the top-left compressed block P_(E_i) A P_(E_i) is a valid source facial certificate with zero source pairing. Its kernel cuts E_i to the next original support. Thus every compiled facial chain induces an original chain of no greater length: depth_comp>=k.

Conversely every original compressed certificate A_i in W lifts to diag(A_i,0) in Wtilde, PSD on the corresponding E_i direct-sum R^d and annihilating J(C_*). It performs the same reduction, proving depth_comp<=k. Therefore
  depth_comp=k                                           (12)
for EVERY nonzero source fibre, including rank-one maximal feasible matrices and non-singleton fibres.

At c=0, trace control forces F_0={0}. The measured identity exposes {0} in ONE step in both source and compiler, giving k=k_comp=1.

## 4. One signed-anchor stage and sharp full-ambient modulus

The compiled frame is Parseval on order d'=2d and Wtilde contains the paired admissible ONB. Apply the explicit signed anchor construction of the prior Track 02 work:
- three columns per admissible ONB vector, with weights -1,2,3 chosen to ensure tightness and zero signed compression;
- the compiler frame columns with weight 4;
- small nonzero anchor coordinates and three pure anchor columns of weights -1,2,4;
- one duplicated equal-weight column for optional nonreflection rotation.

The resulting F in R^((2d+1) x N) satisfies FF^T=I and F D_signed F^T=0, with
  N<=3(2d)+2qtilde+4
    =3d²+7d+2q+4<=4d²+8d+4.
The two-basis orthogonal reflection R=2F^TF-I and equal-weight rotated version U carry a measured PSD certificate
  S0=D_signed+U D_signed U^T>=2(I-F^TF),
with kernel ran F^T. It quantitatively controls all off-face PSD competitors. The compressed projectors span the anchored extension of Wtilde, hence the full exact ambient PSD fibre is E(F_c), with no rank restrictions. The anchor contribution makes EVERY observed datum strictly positive and finite algebraic parameter avoidance makes every basis overlap nonzero.

The even part of the two basis lists cancels off-face cross data exactly, so arbitrary-ambient compressed residuals are O(delta), not O(sqrt(delta)). The positive O(delta) retraction (11) then bounds the decoded ORIGINAL source residual by O(delta), and the full ambient PSD error by
  omega_final(delta)<=C omega_c(C delta)+C sqrt(delta).
Embedded competitors give omega_final(delta)>=omega_c(c delta). For any nonzero source C_*, rank E(C_*)=r+d+1>=2. The ambient exterior is sufficiently large that a nonzero support-to-exterior cross block invisible in both basis diagonals exists (the first diagonal imposes at most N-1 equations, the single equal-weight rotated pair adds at most one). Its Gram-repaired same-rank PSD curve has residual Theta(t²) and distance Omega(t) from the ENTIRE embedded source fibre. Thus omega_final(delta)>=c sqrt(delta), proving (5).

For c=0, the final target is a rank-one anchor with no zero coordinate. Its compressed positive source mass and exterior PSD mass are O(delta), and the remaining anchor-to-exterior cross vector is linearly determined by the first diagonal through coordinatewise multiplication by the nonzero anchor entries. Thus omega_final(delta)=Theta(delta).

The compiled facial depth equals k by Section 3. The signed anchor has one exposing certificate for its exterior face that can be merged with the first compressed facial reduction step, and any ambient chain restricts to a compiled chain. Therefore depth_final=max(1,k), completing the proof.

## 5. Quantitative explicitly conditioned version

Use the RAW no-sparsification frame from Milestone 32 of length
  Mtilde=4d²+2M;
it has exactly the SAME allowed projector space Wtilde because the coefficient factor 1/2 in (9) does not change any membership condition. A single signed lift then has
  N<=4d²+6d+2M+4.                            (13)

Let
  sigma_W=smallest positive singular value of L restricted to W,
  sigma_B=smallest singular value of d selected independent source frame columns,
  K_an=10d(1+sigma_W^(-1)+sigma_B^(-2)).
Milestone 32 proves for all symmetric B,
  ||Pi_Wtilde B||_F<=K_an ||Mtilde(B)||.
The positive decoder here is D0(B)=2 Top(B), so for all symmetric B and source Z_*,
  ||L(D0(B)-Z_*)||
     <=2 K_an ||Mtilde(B-J(Z_*))||,
  ||B-J(D0(B))||
     <=(1+2||J||)K_an ||Mtilde(B-J(Z_*))||.
By (8), ||J||<=sqrt(1/2+d(d-1))<=d for d>=1. Therefore the compiler's numerical conditioning loss is EXPLICITLY polynomial in d,sigma_W^(-1),sigma_B^(-1), independent of any unproved positive cone retraction. The final signed-anchor analysis constants are likewise computable and polynomial in their actual positive singular/exposing gaps.

All coefficients are real algebraic given an algebraic source frame; selecting d independent source vectors and the explicit three frame families uses polynomially many arithmetic operations. Uniform Turing-bit complexity without separation/conditioning promises is NOT claimed.

## 6. Sharp general-linear SDP corollary

Let A:S^m->R^p be any real trace-controlled PSD linear inverse problem. After a fixed positive-definite congruence normalize I_m into range A*. Let s be the codimension of that measurement operator space. The earlier codimension-adaptive tensor rank-one compiler gives order
  d=m(2r0+1)=O(m sqrt(s+1)), where
  r0=max{k:k(k+1)/2<=s+1},
with positive partial-trace decoding, exact PSD fibres and O(delta) original residual equivalence. Its rank-one frame is Parseval but may have NO admissible ONB. Apply Theorem A to it. This yields
  N=O(d²)=O(m²(s+1)),                            (14)
a fully algebraic two-ONB normal form with exact fibres, positive decoding, strict-positive observations, no zero overlaps, arbitrary-rank ambient control, exact linear objective preservation, SHARP modulus
  omega_two_basis(t)~omega_A(t)+sqrt(t) for nonzero feasible data,
and exact facial depth transform max(1,k). For zero data the modulus is Lipschitz.

No strict exposing stress, known target support, target rank hypothesis, singularity-degree bound, commuting condition, sparsity or graph-completion assumption is required. For every FIXED codimension s, the construction has quadratic size O_s(m²), including arbitrarily high facial depth and noncommuting dense measurements. For generic s=Theta(m²), its order remains O(m^4) and the independent generic Omega(m^(8/3)) positive-retract lower bound remains applicable. The unrestricted quadratic-size computational normal-form question therefore remains OPEN, despite full SHARP stability/depth transfer.

## 7. Scope and adversarial audit

1. The single crucial correction from Milestone 31 is BOTH coefficient changes +1->+1/2 and -1->-1/2. Changing only the negative coefficient breaks the paired admissible ONB.
2. The auxiliary block is >=(trZ/2)I for every NONZERO PSD Z, solving the rank-one facial-depth exception exactly.
3. The allowed projector space and its explicit Parseval frame are unchanged from Milestones 31-32 because I in W and the nonzero common factor 1/2 does not change membership conditions.
4. The positive decoder carries factor 2; the explicit conditioning bounds in Section 5 account for it, rather than silently using the former top-block decoder.
5. The exact full-fibre kernel identity follows from the dual of THIS balanced J, not from a rank-restricted Gram argument.
6. The zero source remains zero in every companion block; a fixed positive companion would incorrectly destroy the Lipschitz exception.
7. The whole chain of facial-depth restrictions uses positive definiteness of the bottom target block, and is valid for rank-one C_* as well as higher rank.
8. No claim of unrestricted O(m²+p) size, uniform bit-polynomial conditioning under degeneracy, or external novelty priority certification is made.
