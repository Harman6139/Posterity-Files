# Milestone 33 — exact facial-reduction-depth preservation by complement-twin compilation for rank >=2

Date 2026-11-08. This strengthens Milestone 31 beyond sharp recovery moduli: on source fibres whose maximum feasible rank is at least TWO, the positive complement-twin rank-one compiler preserves singularity degree EXACTLY. Its subsequent signed-anchor two-basis lift changes depth only by the familiar k -> max(1,k). This is an all-ambient PSD statement, independent of nonuniqueness of the source fibre.

## 1. Definitions and theorem

Let G be a rank-one Parseval frame on R^d with measured operator system W=span{g_jg_j^T} containing I_d and feasible PSD fibre
  F_c={Z>=0:L(Z)=c}.
Let E_* be the range of a maximum-rank source feasible matrix C_*. Suppose rank C_*>=2. Define the facial-reduction depth k of F_c to be the minimal length of a standard W-certificate chain from R^d to E_*, with each compressed certificate positive semidefinite on the current support and annihilating the target C_*.

Let
  J(Z)=Z direct-sum(trZ I_d-Z),
  Wtilde={ [A,C;C^T,B] in S^(2d): A-B in W }.
(The equivalence follows from the exact dual J* and the presence of I in W.)
The compressed compiler fibre is
  Ftilde_c=J(F_c), exactly, by Milestone 31.

**Theorem.** The facial-reduction depth of Ftilde_c, relative to Wtilde, equals k. After the one-stage signed-anchor reflection / nonreflection two-basis dilation of Milestone 31, the full ambient two-basis fibre has depth EXACTLY
  k_final=max(1,k).
This holds for singleton and nonsingleton source fibres, all possible ambient PSD competitor ranks, and arbitrary source singularity degree k.

## 2. Why rank(C_*)>=2 is the decisive hypothesis

Let tau=tr C_*>0. If rank C_*>=2, then lambda_max(C_*)<tau, so
  T_*:=tau I_d-C_* >0
on ALL R^d. Thus
  J(C_*)=C_* direct-sum T_*
is positive definite on the support
  E_* direct-sum R^d.
Because C_* has maximum feasible rank and every feasible C has range contained in E_*, this is precisely the minimal PSD face containing Ftilde_c.

(The inclusion of source feasible ranges in E_* follows by averaging C_* with any feasible C: if C has a positive component outside E_*, the average increases rank, contradicting maximality.)

If rank C_*=1, T_* has a one-dimensional nullspace and the simple depth correspondence below need not hold; NO claim is made for that edge case.

## 3. Every compiled facial-reduction step is an original step

Take any compiled facial chain. Initially its current support is R^d direct-sum R^d. We prove inductively that every support has the form
  E_i direct-sum R^d
for some E_i containing E_*.

Let a compressed measured certificate S=[A,C;C^T,B] in Wtilde be positive semidefinite on the current support E_i direct-sum R^d and satisfy <S,J(C_*)>=0. Because J(C_*) is positive definite on E_* direct-sum R^d, a PSD compressed matrix with zero pairing annihilates all of E_* direct-sum R^d. In particular it annihilates every vector in the entire lower R^d block.

Consequently the compressed lower block B=0 and the compressed cross block P_(E_i) C=0. Since S belongs to Wtilde, A-B=A belongs to W. Its top compression P_(E_i) A P_(E_i)>=0 and its source pairing <A,C_*>=0. The next compiled support is therefore
  [ker(P_(E_i)A P_(E_i)) within E_i] direct-sum R^d,
and this is EXACTLY one valid original facial reduction step. Hence every compiled chain pulls back to an original chain of equal length after unchanged supports are deleted, proving k_comp>=k.

Conversely, let A_1,...,A_k in W be a shortest original facial chain. The block-diagonal lifted certificates
  S_i=A_i direct-sum 0_d
belong to Wtilde, are positive semidefinite on E_(i-1) direct-sum R^d, annihilate J(C_*), and cut that support to E_i direct-sum R^d. Hence k_comp<=k. Therefore k_comp=k. QED.

## 4. Signed anchored lift changes depth by max(1,k)

Let F in R^((2d+1) x N) be the signed-anchor isometry of Milestone 31, with P=F^TF, Q=I-P and two-basis measured exposing certificate S0>=2Q, ker S0=ran P. Its compression to P has measurement span exactly the *anchored extension* of Wtilde:
  W_aug={ [A,z;z^T,s]: A in Wtilde, z arbitrary, s arbitrary }.
The anchored target is J(C_*) direct-sum[1]. Since its last coordinate is positive definite and its cross entries are zero, the anchored problem has the SAME depth k as Wtilde: any compressed PSD zero-pairing certificate annihilates the anchor direction, and every old certificate extends by zero on it.

Upper depth: for k>=1, represent the first compressed certificate by a diagonal measured coefficient Lambda on the frame. Average its first/second-basis measurements to eliminate the off-P cross blocks; add a sufficiently large multiple of S0 to make the exterior Q block strictly positive. This first ambient certificate simultaneously cuts away Q and performs the first compressed facial step. The remaining k-1 certificates work on the now-embedded support. Thus depth<=k. For k=0, S0 exposes the full target face in one step, so depth<=1.

Lower depth: intersect any ambient certificate chain's supports with ran P. The pullback of every measured ambient certificate belongs to W_aug (including the optional equal-weight nonreflection rotation; its compressed frame projectors remain in W_aug), and positivity makes the successive intersected kernels exactly the kernels of the compressed certificates. Removing unchanged steps yields an anchored compressed chain no longer than the ambient chain, so depth>=k. If k=0, the target has rank <N because the exposing dilation has nontrivial Q, so depth cannot be zero. Combining bounds gives depth_final=max(1,k). QED.

## 5. Concrete interpretation of the sharp 1/2-versus-1/4 example

The original 4x4 rank-two source in Milestone 26 has source graph operator system W={H:H_(1,3)=0}, source facial depth k=1 and sharp exponent 1/2. Its complement-twin target J(Z_*) has a POSITIVE DEFINITE bottom 4x4 block because tr Z_*=2 and rank Z_*=2, hence compiled depth remains exactly ONE. The signed-anchor final two-basis problem retains depth one and sharp exponent 1/2.

By contrast the two-zero Naimark route in Milestone 26 raises source depth one to two and sharp exponent 1/2 to 1/4. The complement-twin construction therefore repairs BOTH the facial-depth defect and the Hölder exponent defect for this explicit source.

For any source graph family with rank>=2, depth k and optimal exponent 2^(-k), the new universally admissible complement-twin compiler and one signed stage preserve both k (when k>=1) and 2^(-k). This provides a systematic all-depth two-basis transfer without choosing a target-dependent chain or individual exposing stresses.

## 6. Scope and hostile audit

- The proof uses strict positive definiteness of trC_* I-C_*; it fails for rank-one source matrices where the complement block has an additional null direction.
- It treats the MINIMAL FACE OF THE ENTIRE SOURCE FIBRE, using a maximal-rank feasible matrix, not a possibly lower-rank arbitrary point.
- The lower-block cancellation in a compressed PSD certificate follows from POSITIVITY plus zero pairing against a positive-definite target block; it is not an unjustified block algebra shortcut.
- A diagonal block S_i=A_i direct-sum0 belongs to Wtilde because A_i in W; this is why every original reduction extends.
- The final signed-anchor formula k->max(1,k) uses exactly the same support-intersection argument as the graph embedding and does not assume source uniqueness.
- The optional nonreflection rotation retains the compressed frame span and signed exposing certificate; no original source admissible ONB or strict stress is required.
- This is a depth theorem for rank>=2 source feasible fibres; it does not establish a complete depth classification of the rank-one edge case.
