# Milestone 28 — EXACT FUNCTIONAL MODULUS TRANSFORMATION for support-cross-surjective two-basis frame compilers

Date 2026-11-08. This is a complete sharp two-sided local modulus theorem for a broad, checkably defined class of real PSD rank-one inverse problems. It resolves the "is alpha/2 loss sharp?" question at the FUNCTION level, not just along dyadic examples, while explicitly restricting the result to the TWO-ZERO / POSITIVE-COMPOSITION compiler architecture. The original sharp single-certificate reflection graph lift can preserve the source modulus and is NOT contradicted.

## 1. Hypotheses and computable surjectivity test

Let G=[g_1,...,g_M] in R^{d x M} be a Parseval frame GG^T=I_d, with 0<||g_j||<1, M>d, and rank-one measurement map
  M_G(Z)=(g_j^T Zg_j)_{j=1}^M.
Let Z_*>=0 be pointwise uniquely recoverable among ALL PSD competitors, with positive trace tau and rank r>=2. Write R_* for the orthogonal projection onto ran Z_*. Complete G to [G;K] in O(M), with K in R^{(M-d) x M}.

For any rank-r orthogonal projector R on R^d define
  T_R(X)=2diag(G^T X K),
  X in R^{d x(M-d)}, R X=X.
The **uniform cross-surjectivity test** is
  rank T_(R_*) = M-1,
equivalently
  ker[(R_*G diag(lambda) K^T) as a function of lambda in R^M]
       =span{1_M}.
All outputs of T_R have zero sum because G K^T=0, so M-1 is the maximal possible rank. This is a finite singular-value calculation. Full rank M-1 is OPEN under small perturbations of R, with a locally bounded right inverse; no genericity assumption is hidden.

Let omega_src(t)=max{||Z-Z_*||_F:Z>=0,||M_G(Z-Z_*)||<=t}, and let omega_zero, omega_pos be the full arbitrary-ambient PSD moduli of respectively (a) the minimal two-zero two-basis dilation of order 2M-d (Milestone 21) with a sufficiently small generic exterior rotation removing all zero basis overlaps; and (b) its strictly-positive signed-anchor two-basis composition of order at most 10M-5d+4 (Milestone 24).

## Theorem 1 (complete functional law)

Under the hypotheses above, for all sufficiently small delta>0,
  c omega_src(sqrt(delta)) <= omega_zero(delta)
      <= C omega_src(sqrt(delta)),
  c' omega_src(sqrt(delta)) <= omega_pos(delta)
      <= C' omega_src(sqrt(delta)),
for fixed finite positive constants c,C,c',C' depending only on the instance and selected bases.

Both compiled inverse problems are pointwise uniquely solvable over ALL ambient PSD ranks. The second has a rank-(r+1) target, ALL target observations strictly positive, no zero basis overlaps, and can be chosen nonreflection. Both have a globally positive decoder, exact fibre correspondence, and exact objective pullback.

In particular, because finite-dimensional PSD worst-case moduli are semialgebraic and have attained rational power exponents, if
  omega_src(t) asymp t^alpha,
then
  omega_zero(delta) asymp delta^(alpha/2),
  omega_pos(delta) asymp delta^(alpha/2).
Thus alpha_compiled=alpha_source/2 EXACTLY; the modulus transformation is stronger than exponent identity.

## 2. Lemma: trace-fixed source competitors capture the full local modulus

Define
  omega_tau(t)=max{||Z-Z_*||:Z>=0,trZ=tau,
                             ||M_G(Z-Z_*)||<=t}.
Then omega_tau(t) asymp omega_src(t).

Proof. The upper omega_tau<=omega_src is immediate.

For arbitrary Z>=0 with residual e<=t, Parseval gives
  |trZ-tau|=|1^T M_G(Z-Z_*)|<=sqrt(M)t.
For t small, s=trZ>=tau/2>0. Normalize Z'=(tau/s)Z. It remains PSD and has trace tau, and
  ||Z'-Z||_F<=|tau-s|<=sqrt(M)t.
Its residual is <=C_0t because M_G(Z'-Z_*)=(tau/s)M_G(Z-Z_*)+(tau/s-1)M_G(Z_*). Consequently
  omega_src(t)<=omega_tau(C_0t)+sqrt(M)t.        (1)

Since rank Z_*>=2, choose a nonzero symmetric trace-zero H supported on ran Z_*; then Z_*+uH>=0 for all sufficiently small |u|. Unique PSD recovery implies M_G(H)!=0; otherwise the two signs give distinct exact solutions. Thus omega_tau(t)>=c_0 t for small t. By convexity of the fixed-trace PSD competitor set,
  omega_tau(C_0t)<=C_0 omega_tau(t) (C_0>=1).
Use (1) to obtain omega_src(t)<=C_1 omega_tau(t), proving equivalence. This proof covers even Lipschitz sources and does not assume a special sharpness curve.

## 3. Uniform second-order exact lifting of EVERY trace-fixed nearby PSD competitor

Fix Z>=0 with trZ=tau and small source measurement residual e=M_G(Z-Z_*). Uniqueness and measured-trace compactness imply Z->Z_* uniformly as ||e||->0. Let R_Z be the spectral projection onto its r largest eigenvalues. For e small, these eigenvalues are >=lambda_*/2 where lambda_*>0 is the smallest positive eigenvalue of Z_*, while R_Z->R_*.

Because rank T_(R_*)=M-1, the same holds at R_Z for all sufficiently small residuals, and its least positive singular value is bounded below by some sigma>0. Since trZ=tau, Parseval implies 1^T e=0. Choose an off-source correction X_Z with R_Z X_Z=X_Z and
  2diag(G^T X_Z K)=-e,
  ||X_Z||_F<=sigma^(-1)||e||_2.                       (2)
The columns of X_Z belong to a stable positive-eigenvalue subspace of Z, so
  tr(X_Z^T Z^dagger X_Z)<=2lambda_*^(-1)||X_Z||_F²
  =O(||e||²).                                       (3)

For the unrotated minimal two-zero dilation use the orthogonal ambient decomposition (source R^d) direct-sum Q_1 direct-sum Q_2, with each Q_i of order z=M-d and the two surviving basis vectors having exterior projection K e_j in Q_1 or Q_2 respectively. Define cross blocks X_1=X_Z, X_2=X_Z. Then the ambient block matrix
  Y=[I_d; X_1^T Z^dagger; X_2^T Z^dagger]
       Z
     [I_d, Z^dagger X_1, Z^dagger X_2]
is PSD, compresses exactly to Z, and has the SAME rank as Z. The first-order source measurement e is canceled exactly in BOTH lists by (2). All remaining measurement error comes from exterior PSD blocks, and (3) gives
  ||A_U(Y)-A_U(Y_*)|| <=C_2||e||².                 (4)
When e!=0, its trace defect equals
  2tr(X_Z^T Z^dagger X_Z)>0
and is comparable to ||e||² because the cross analysis map is bounded and the stable eigenvalues of Z are also bounded above by tau; hence the residual is in fact Theta(||e||²).

To eliminate all zero transition overlaps, choose an exterior rotation Omega close to I in O(2z) such that the z-dimensional subspaces Q_1 and Omega Q_2 remain complementary. Define
  C_Omega=[J_1,Omega J_2] in R^{2z x2z},
J_1=[I_z;0], J_2=[0;I_z].
It is invertible near the identity. Replace the pair of cross blocks by the unique linear map on Q whose restrictions to Q_1 and Omega Q_2 are both X_Z, i.e. take [X_Z,X_Z] C_Omega^(-1). This map remains O(||e||), its range stays in ran R_Z, and the same positive Gram factorization and residual estimate (4) hold with constants depending continuously on C_Omega^(-1). Milestone 21 proves that an Omega arbitrarily close to I makes EVERY transition entry nonzero.

Consequently, every trace-fixed source competitor Z with residual <=t has an actual ambient PSD lift with residual <=C_2 t² and distance at least ||Z-Z_*||. Taking suprema yields
  omega_zero(C_2t²)>=omega_tau(t).                 (5)

For delta sufficiently small set t=sqrt(delta/C_2). Lemma 2 and fixed-argument scaling of convex PSD moduli give
  omega_zero(delta)>=c omega_src(sqrt(delta)).    (6)

## 4. Matching upper bound for ALL ambient PSD competitors

The double-zero exposing certificate of Milestone 21 bounds exterior PSD mass by O(delta) and its cross blocks by O(sqrt(delta)), uniformly over ALL PSD matrices of unrestricted rank. Compression therefore has source measurement residual at most C_3 sqrt(delta), giving
  omega_zero(delta)<=omega_src(C_3sqrt(delta))+C_4sqrt(delta).
Because omega_src(t)>=c_5t, the last term is absorbed by omega_src(sqrt(delta)). Fixed argument rescaling changes a PSD distance modulus by at most fixed multiplicative factors, proving
  omega_zero(delta)<=C omega_src(sqrt(delta)).
Combined with (6), this proves the first two-sided functional equivalence.

## 5. Strictly positive two-basis composition

Milestone 24's signed-anchor lift of the entire intermediate two-basis problem has exact full-PSD fibre correspondence and an exposing certificate S>=2Q. Its even/odd reflection decomposition gives, for all ambient PSD competitors, the upper estimate
  omega_pos(delta)<=C_6 omega_zero(C_7delta)+C_8sqrt(delta).
Embedded intermediate competitors give the lower
  omega_pos(delta)>=c_6 omega_zero(c_7delta).
Since omega_zero(delta) asymp omega_src(sqrt(delta)) and omega_src(t)>=ct, the extra sqrt(delta) term is dominated. Fixed-argument convexity gives the complete second equivalence.

The final two measured lists are strictly positive because each signed-anchor frame vector has nonzero anchor coordinate, all overlaps can be chosen nonzero by finite algebraic avoidance, and the equal-weight rotation can make the bases nonreflection without affecting the exposing certificate or compressed span. The rank increases by exactly one, and original costs pull back through the positive composite decoder.

## 6. Broad graph-completion corollary

Let G=(V,E) be a CONNECTED finite graph, and let C_*>=0 be a uniquely completable graph target such that in any Gram realization all measured-edge endpoint vectors p_i,p_j are linearly independent. This implies rank C_*>=2 and every vertex Gram vector is nonzero. Choose the explicit vertex-plus-paired-edge Parseval frame from Milestone 27:
  g_i=sqrt(1-2h²deg i)e_i,
  g_(ij,+/-)=h(e_i+/- e_j),
with h>0 sufficiently small. Its projector span equals the graph measurement space, and all target frame outcomes are strictly positive.

By the EXACT adjoint-kernel calculation of Milestone 27, connectedness and edgewise independence imply
  rank T_(R_*)=M-1.
The original frame and graph data are equivalent via a fixed invertible linear map on their ranges, so omega_src(t) asymp omega_graph(t).

Therefore, for EVERY such uniquely completable graph instance, irrespective of facial-reduction depth and irrespective of whether its source modulus is Lipschitz or non-Lipschitz,
  omega_compiled(delta) asymp omega_graph(sqrt(delta))
for both the zero-exposure and strictly-positive composed two-basis constructions.

In particular the attained optimal exponent ALWAYS transforms as
  alpha_compiled=alpha_graph/2.
This is an exact functional classification for a BROAD checkably defined graph class, not merely the cascade examples. It is consistent with the separate original single-certificate graph lift (which has exponent alpha_graph), demonstrating that the choice of embedding genuinely changes inverse-problem conditioning.

The positive composed dimension is
  N=5(m+4|E|)+4=5m+20|E|+4,
and the target rank is rank(C_*)+1. Every final observation is strictly positive and the basis transition has no zero entries.

## 7. Hostile audit

- The source-to-trace-fixed comparison handles Lipschitz targets as well as non-Lipschitz ones; rank>=2 gives a supported trace-free tangent, and uniqueness makes its measurement nonzero.
- The lower lifting mechanism applies to EVERY trace-fixed PSD competitor near Z_*, not only a distinguished sharpness curve. Its source support may have rank >r; the top-r spectral projection stays separated and guarantees a bounded PSD pseudoinverse on the cross-block range.
- All constructed ambient matrices are PSD by exact product factorization, with arbitrary source competitor rank. No fixed-rank assumption is hidden.
- The trace defect is quadratic in e and nonzero whenever e!=0; the full residual is Theta(||e||²), not only O.
- The exterior rotation is handled by a bounded explicit complementary-subspace inverse C_Omega. It does not silently assert that cross-data solvability survives an arbitrary unrelated basis perturbation.
- The graph independence hypothesis is checked on EVERY measured edge and is stronger than mere graph connectivity. Neither condition alone suffices for the surjectivity theorem.
- The final signed-anchor rate uses the first-order even/odd cancellation, not the unsharp alpha/2 estimate of the first stage a second time. Therefore only ONE square-root loss occurs.
- The positive frame-compiler rate is sharp exactly as claimed under the stated cross-surjectivity condition; there is no claim of universally sharp rate loss or universally preserved rates across all source operator systems.
- No claim of unconditional polynomial Turing bit complexity for degenerate algebraic inputs is made. Cross-surjectivity has a computable positive singular margin; constants can deteriorate as measured edge Gram vectors approach linear dependence.
