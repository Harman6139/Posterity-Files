# Milestone 27 — rate-neutral target-adapted frame augmentation recovers SHARP two-basis transfer without an admissible source ONB

Date 2026-11-08. Complete, self-audited real PSD theorem. This advances the sharpness programme after the explicit 1/2-to-1/4 loss in Milestone 26. It is target/certificate-dependent and does NOT solve the unrestricted O(m²+p) effective universality question.

## 1. Hypotheses and theorem

Let G=[g_1,...,g_M] in R^{d x M} satisfy GG^T=I_d, with every g_j nonzero. Let
  W=span{g_jg_j^T} <= S^d,
  M_G(Z)=(g_j^T Zg_j)_j,
and suppose a nonzero Z_*>=0 is uniquely determined by its M_G data among ALL PSD competitors.

Write P for the projector onto ran Z_* and Q=I-P. Assume a **strict measured stress certificate**
  S=sum_j a_j g_jg_j^T in W,
  S>=gamma Q, S P=0, gamma>0.
Assume EITHER
(A) rank Z_*=1; OR
(B) ran Z_* admits a real orthonormal basis u_1,...,u_r such that every support projector u_i u_i^T belongs to W.
No admissible orthonormal basis of the WHOLE original R^d is required.

**Theorem.** Choose any orthonormal basis of R^d extending the supplied support basis (in rank-one case use the unique support unit vector), and fix 0<epsilon<1. Let
  G'=[ sqrt(1-epsilon) G, sqrt(epsilon) U_basis ]
be the d-by-(M+d) frame obtained by appending all d basis vectors at common weight sqrt(epsilon). Then:
1. G' is Parseval and its rank-one projectors span W'=W+span{u_i u_i^T:1<=i<=d}. In particular W' contains an admissible ONB even if W does not.
2. The new source data are QUANTITATIVELY RATE EQUIVALENT to the old data against every PSD competitor:
   (1-epsilon)||M_G(Z-Z_*)||
   <=||M_G'(Z-Z_*)||
   <=sqrt((1-epsilon)^2+epsilon² C_B²)||M_G(Z-Z_*)||,
   for an explicit C_B depending only on the original stress gap gamma, coefficients a and the support-projector coefficient representations (or trace in rank one).
   Hence omega_G'(t) ~ omega_G(t) as t downarrow0, for the full feasible-set distance (here a singleton).
3. Applying the ONE-STAGE signed-anchor reflection dilation (with an optional equal-weight rotation) gives two real orthonormal bases of order
     N<=M+4d+4
   with every target observation strictly positive, every basis overlap nonzero, exact full-ambient PSD target uniqueness, and a globally positive linear decoder. Target rank is rank(Z_*)+1; Frobenius differences are preserved exactly along the embedding and source objectives are decoded identically for all ambient symmetric matrices.
4. The sharp two-basis modulus law is
     omega_final(t) ~ omega_G(t)+sqrt(t)
   for all sufficiently small t>0. In particular, if the original source recovery is non-Lipschitz, its entire worst-case modulus is preserved up to fixed multiplicative constants.
5. Under the strict-stress hypothesis, the source is at least 1/2-Hölder. Its attained optimal exponent is therefore either 1/2 or 1. The two-basis exponent is exactly 1/2, and **the exponent is preserved whenever the source was non-Lipschitz**.

The construction is effective in an algebraic arithmetic model when the target support and strict stress certificate are supplied. It is not an algorithm that discovers an unknown target from arbitrary rational A,b at uniform polynomial-bit cost.

## 2. Proof of rate-neutral basis augmentation

Write delta=||M_G(Z-Z_*)|| for Z>=0. Parseval gives
  |tr Z-tr Z_*| = |sum_j g_j^T(Z-Z_*)g_j| <=sqrt(M) delta.
Since S annihilates Z_* and is measured,
  0<=tr(SZ) =sum_j a_j g_j^T(Z-Z_*)g_j<=||a|| delta.
Thus
  0<=tr(QZ)<=kappa delta, kappa=||a||/gamma.
For ANY unit vector v in ran Q,
  0<=v^T Z v<=kappa delta.
In particular the d-r appended orthonormal kernel vectors have new residuals bounded by kappa delta each.

For rank r>=2 under (B), represent each support projector as
  u_i u_i^T=sum_j c_(i,j) g_jg_j^T, 1<=i<=r.
Then
  |u_i^T(Z-Z_*)u_i|<=||c_i|| delta.

For rank r=1 under (A), let u span ran Z_*. Since I=u u^T+Q,
  u^T Z u-tr Z_*=tr Z-tr Z_*-tr(QZ).
Hence
  |u^T(Z-Z_*)u|<= (sqrt(M)+kappa)delta.
This uses only measured trace plus strict stress, and does NOT require uu^T to lie in W.

Define bounds C_i=||c_i|| for support vectors in (B), C_1=sqrt(M)+kappa for rank one, and C_i=kappa for kernel vectors. Let C_B=(sum_i C_i²)^(1/2).
Then the appended ONB diagonal residual has norm <=C_B delta, and
  M_G'(Z-Z_*)=((1-epsilon)M_G(Z-Z_*),
               epsilon diag(U_basis^T(Z-Z_*)U_basis)).
The advertised two-sided estimates follow. Exact fibres remain identical because the original scaled measurements are retained. PSD residual-bounded sets are compact, as both frames are Parseval. Fixed rescalings of convex-fibre moduli are equivalent, so the worst-case source moduli are asymptotically equivalent. QED.

## 3. One-stage positive signed dilation and sharp transfer

The frame G' has M'=M+d columns and contains an explicit ONB in its projector span, namely the appended basis. Use it as the negative-weight coordinate family in the standard signed-frame construction:
 - three columns a u_i,b u_i,b u_i with signed weights -1,2,3 per basis vector u_i;
 - columns h g'_j with weight 4 for every g'_j, h=1/10, a²=(5+3h²)/7, b²=(1-5h²)/7;
 - a small nonzero anchor coordinate added to every column, with two or three pure-anchor columns restoring the identities FF^T=I and FDF^T=0.
With a duplicated weight-4 coordinate and three pure-anchor columns to permit a nonreflection rotation, the final order is
  N=3d+(M+d)+4=M+4d+4.
All coefficients are finite algebraic and a finite rational grid avoids zero overlaps.

Let P_1=F^T F, Q_1=I-P_1, R=P_1-Q_1 and let D be the signed diagonal weight matrix. Its negative inertia is d+1 with all negative weights -1, all positive weights >=2, and FDF^T=0. Therefore
  S_0=D+RDR=2Q_1 D Q_1>=2Q_1,
with kernel ran P_1. An optional sufficiently small rotation of two equal-weight coordinates commutes with D and preserves S_0; the retained duplicate preserves the compressed span. Every column has nonzero anchor coordinate, giving strictly positive target observations, and all overlaps can be kept nonzero.

The compressed measurement span is exactly the anchored extension of W', and the full ambient exact fibre is
  {F^T(Z direct-sum[1])F:Z>=0,M_G'(Z)=M_G'(Z_*)}
  ={F^T(Z_* direct-sum[1])F}.
The decoder is positive compression D_final(Y)=(F Y F^T)_(1:d,1:d), with D_final(E(Z))=Z. The encoder is isometric on differences, and for any source cost C, F^T(C direct-sum[0])F represents the decoded objective on ALL ambient matrices.

For arbitrary PSD Y with data residual delta, the exposing certificate bounds exterior mass O(delta) and cross-block Frobenius norm O(sqrt(delta)). The even part of the two reflection lists cancels cross terms EXACTLY, recovering compressed W' data with residual O(delta). This gives
  omega_final(delta)<=C omega_G'(C delta)+C sqrt(delta).
Embedded competitors give the reverse omega_final(delta)>=omega_G'(c delta).
Since rank of the anchored target is rank Z_*+1>=2 and the ambient exterior has sufficiently many dimensions, the support/exterior cross measurement map has a nontrivial invisible direction. Its same-rank Gram-corrected PSD curve yields a matching omega_final(delta)>=c sqrt(delta). Therefore
  omega_final(t) ~ omega_G'(t)+sqrt(t) ~omega_G(t)+sqrt(t).
No source-rank or ambient-rank restriction is used in the upper estimate. QED.

## 4. Why the source exponent is at least one half

Let Z>=0 have residual delta and tr Z<=T_*=tr Z_*+sqrt(M). The strict measured stress gives tr(QZ)<=kappa delta. PSD block inequalities imply
  ||PZQ||_F<=sqrt(T_* kappa delta)
and ||QZQ||_F<=kappa delta.

On the positive target support E=ran Z_* of dimension r, the restricted linear measurement map
  H in S(E) -> M_G(H)
is injective: if a supported H!=0 were unmeasured, then Z_*+/-tH would both be PSD for sufficiently small t because Z_* is positive definite on E, contradicting source uniqueness. Let sigma_E>0 be its smallest singular value.
For H=PZP-Z_*,
  sigma_E||H||_F<=||M_G(H)||
   <= delta+||M_G(PZQ+QZP+QZQ)||
   <=delta+C[sqrt(T_* kappa delta)+kappa delta].
Thus ||H||=O(sqrt(delta)). Combining blocks gives
  ||Z-Z_*||_F=O(sqrt(delta)).
The semialgebraic source modulus has an attained exponent alpha>=1/2. The PSD tangent-cone dichotomy (proved in previous Track 02 work) implies alpha is either 1 or at most 1/2; hence alpha in {1/2,1}. The lifted modulus t^alpha+sqrt(t) has sharp exponent 1/2, preserving the source exponent in the non-Lipschitz case.

## 4b. Dimension optimality up to a constant factor in the data-faithful class

Put q=dim W. The supplied Parseval frame may have M>>q columns, but the conic Caratheodory compression reduces it to at most 2q WITHOUT changing its projector span or tightness. Precisely: reserve epsilon>0 of each of q linearly independent frame projectors P_i (small enough that all original weights remain positive). Represent the residual identity as a positive combination of the original projectors. Whenever more than q residual coefficients are active, use a linear dependence of the projectors and move in one sign direction until one coefficient reaches zero. Since the trace of each nonzero rank-one projector is positive, every nonzero dependence has both signs, so the reduction preserves positivity. Continue to at most q residual terms. Adding the q reserved terms leaves at most 2q columns, preserves Parseval and spans all of W. The measured stress S retains a coefficient representation in the new frame, although its coefficient norm may deteriorate; the rate theorem remains valid with the updated explicit constants.

Also q>=d: to express I_d as a positive combination of q independent rank-one generators requires at least d nonzero generators because rank(I_d)=d and each generator has rank one.

Apply the rate-neutral ONB augmentation and signed-anchor lift to the compressed frame. The resulting final order obeys
  N<=2q+4d+4<=6q+4.
Thus the certified target-adapted sharp-transfer representation has size O(q), LINEAR in the number q of independent source rank-one measurements, not merely O(M).

For comparison, any two-basis encoding that faithfully retains q independent source measurements as linear functionals on the full embedded symmetric matrix space must satisfy
  q<=2N-1,
because the two complete basis diagonals have one shared trace linear relation. Therefore
  N>=(q+1)/2.
Our construction is within an absolute factor at most approximately 12 of this elementary information lower bound (ignoring the additive constant). This near-optimality comparison is for DATA-FAITHFUL encodings; target-specific exact singleton recovery without full measurement fidelity need not obey the same q-based lower bound.

## 5. Nontrivial example with NO admissible original ONB

Take d=3 and four tetrahedral unit vectors
  u1=(1,1,1)/sqrt3,
  u2=(1,-1,-1)/sqrt3,
  u3=(-1,1,-1)/sqrt3,
  u4=(-1,-1,1)/sqrt3.
Let g_j=sqrt(3/4)u_j. These are Parseval, and their rank-one projectors span
  W={H in S^3:H_11=H_22=H_33}.
No two distinct allowed rank-one lines are perpendicular (pairwise inner product absolute value 1/3), so W has NO admissible ONB. Nevertheless the rank-one target Z_*=u1u1^T is uniquely determined: the measured strict stress
  S=I-u1u1^T in W
is PSD with kernel exactly span u1, and trace fixes the coefficient on that support.
Our theorem appends the eigenbasis of Z_* at a small positive frame weight, without changing the source recovery modulus. It then yields a SINGLE positive-data signed two-basis lift of order
  N<=M+4d+4=4+12+4=20
with exact full-PSD target uniqueness and sharp modulus omega_final~omega_source+sqrt(t). This bypasses the tetrahedral ONB obstruction without the two-zero stage and without its possible alpha/2 loss.

## 5b. A genuinely NON-LIPSCHITZ example whose original frame has NO admissible ONB

To demonstrate that sharp preservation is not vacuous in the no-ONB class, take the orthogonal direct sum of the three-dimensional tetrahedral operator system and a two-dimensional diagonal system. Thus d=5, with
  W={A direct-sum diag(x,y): A in S^3, A_11=A_22=A_33}.
A rank-one Parseval frame consists of the four tetrahedral vectors (scaled by sqrt(3/4)) in the first three coordinates, together with e4 and e5. Hence M=6 and dimW=6. The rank-one allowable lines in W belong entirely to one of the two blocks, since a mixed vector would have nonzero forbidden cross-block entries. In the tetrahedral block, no two allowable rank-one lines are orthogonal. Therefore W admits NO full admissible orthonormal basis of R^5.

Choose
  Z_*=e4e4^T
of rank one. The measured PSD stress
  S=I_3 direct-sum diag(0,1)
belongs to W, has kernel span(e4) and satisfies S>=Q=I-Z_*.
Thus Z_* is unique among all PSD matrices with its data: the stress confines any exact competitor to span(e4), and measured trace fixes its coefficient.

The source optimal exponent is EXACTLY 1/2. For arbitrary PSD Z with data residual delta, the tetrahedral frame measures its upper 3-by-3 trace, and the last frame vector measures Z_55; both have target zero, so tr(QZ)=O(delta). Trace fixes Z_44=1+O(delta), and positivity gives ||PZQ||_F=O(sqrt(delta)). Hence ||Z-Z_*||_F=O(sqrt(delta)).
For sharpness take
  Z(t)=(sqrt(1-t²)e4+t e5)(sqrt(1-t²)e4+t e5)^T.
Its source data residual is Theta(t²) (only the e4/e5 diagonal outcomes change), while ||Z(t)-Z_*||_F=sqrt(2)t. Its rank remains one and its trace is exactly one.

The rate-neutral ONB augmentation in this theorem adds any eigenbasis of Z_* (e4 plus an orthonormal basis of its four-dimensional kernel). It changes every source measurement residual by at most a fixed factor because S controls kernel mass and trace controls the one support diagonal. Applying the ONE-STAGE signed-anchor lift gives
  N<=M+4d+4=6+20+4=30,
strictly positive two-basis target observations, no zero basis overlaps, full-PSD uniqueness, target rank two, and sharp exponent 1/2, exactly the original exponent.

This explicit construction demonstrates that an admissible source ONB is genuinely unnecessary for sharp transfer when a strict measured stress is available; the two-zero construction's quarter-root loss can be avoided in a nontrivially unstable source problem.

## 6. Scope and hostile audit

- The stress must be globally PSD on R^d with a POSITIVE GAPPED restriction to the target kernel. A merely compressed facial-reduction certificate after earlier steps is not enough.
- For rank r>=2, support basis projectors must be in W (a checkable linear-algebra condition). For rank one no such assumption is needed because trace and the strict stress control the one support diagonal.
- The added rank-one measurements do not change the data modulus at any order: each new residual coordinate is explicitly O(delta) over all original PSD competitors.
- The positive ONB augmentation and signed frame are target-dependent. Without a supplied target support/stress, the construction is not a uniform polynomial-time reduction of arbitrary SDP instances.
- This does NOT contradict Milestone 26: its original W already had an admissible ONB and a sharp one-stage reflection lift; Milestone 26 specifically used the inferior two-zero route.
- The final lift has rank amplification exactly one, versus the two-zero+anchor's same rank gain, and avoids its extra facial-depth step.
- All sharpness claims are against unrestricted ambient PSD competitors. The square-root lower curve is PSD by exact Gram factorization, not by assuming linear off-face perturbations remain PSD.
- No universal dimension-only condition-number bound is claimed; the source stress gap, coefficient norms and frame analysis singular values are explicit input-dependent parameters.
