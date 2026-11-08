# Milestone 27 — SHARP exponent halving for EVERY dyadic source exponent, even after strictly-positive two-basis compilation

Date: 2026-11-08. This is a complete analytic theorem with an all-ambient upper bound and a matching fixed-rank PSD curve, extending the isolated 1/2 -> 1/4 example of Milestone 26 to EVERY k>=1. It proves that the square-root loss in the generic two-zero frame compilation can be genuinely optimal even when the original source recovery is already non-Lipschitz and arbitrarily ill-conditioned.

## Theorem A — edgewise Gram independence makes the target-support cross map surjective

Let G=(V,E) be a finite connected graph on m>=2 vertices. Choose h>0 with 2h² deg(i)<1 and put a_i=sqrt(1-2h²deg(i)). Form the m-by-M Parseval frame, M=m+2|E|, consisting of:
  g_i=a_i e_i for each vertex i;
  g_(ij,+)=h(e_i+e_j) and g_(ij,-)=h(e_i-e_j) for each edge {i,j}.
Then GG^T=I_m and the outer products span exactly the diagonal-and-edge subspace L_G<=S^m.

Let K in R^{(M-m) x M} complete [G;K] to an orthogonal M-by-M matrix. Let C>=0 have range projection R_C. Assume that for every edge {i,j}, the projected vectors R_C e_i and R_C e_j are linearly independent. Equivalently, in ANY Gram representation C_ij=<p_i,p_j>, the vectors p_i,p_j are linearly independent on every edge.

Define the restricted support-to-exterior cross analysis map
  T_C:X in R^{m x(M-m)}, ran X subset ran C,
      -> 2 diag(G^T X K) in R^M.
Then
  ran T_C = {v in R^M:sum_j v_j=0}.
Thus T_C is SURJECTIVE onto the entire trace-zero measurement output space. Its positive singular values are continuous under fixed-rank perturbations C(t) and remain bounded away from zero in a neighbourhood of C as long as all edgewise independence conditions persist.

**Proof.** Parseval tightness follows by adding the + and - edge projectors: their off-diagonal contributions cancel and each incident edge adds 2h²e_ie_i^T, which the vertex coefficient compensates. The same plus/minus pairs recover each measured edge and the vertex columns recover each diagonal, proving the span.

Every output of T_C has sum 2 tr(G^T X K)=2 tr(X K G^T)=0, so the range is contained in 1^perp. To compute the adjoint kernel, choose an orthonormal basis R in R^{m x r} of ran C. If lambda in R^M annihilates T_C, then
  R^T G diag(lambda) K^T=0.
Since the rows of K span ker G and GG^T=I, this means
  R^T G diag(lambda) = A G
for some r-by-m matrix A. At a vertex column g_i=a_i e_i (a_i>0), this gives A e_i=lambda_i R^T e_i. For the two edge columns g_(ij,+)=h(e_i+e_j), g_(ij,-)=h(e_i-e_j), it gives
  (lambda_i-lambda_(ij,+)) R^T e_i+
  (lambda_j-lambda_(ij,+)) R^T e_j=0,
and the analogous equation with a minus sign for the minus column. Since R^T e_i,R^T e_j are linearly independent, all four lambda values coincide for every edge. Connectedness forces every lambda_j to be the same scalar. Hence ker T_C*=span(1) and ran T_C=1^perp. QED.

## Theorem B — a general second-order cancellation mechanism

Under Theorem A, suppose Z_*>0 on its range and Z(t)>=0 is a continuous constant-rank PSD curve converging to Z_*, whose positive eigenvalues remain >=lambda>0. Assume:
(i) tr Z(t)=tr Z_* for all t;
(ii) edgewise Gram independence holds at Z_* (hence for small t);
(iii) e(t)=M_G(Z(t)-Z_*) is nonzero for t>0 and ||e(t)||->0.
Write e(t)=O(epsilon(t)) for a positive scale epsilon(t)->0.

Apply the exact two-zero frame-to-two-basis dilation of Milestone 21 (order n=2M-m), with an exterior rotation sufficiently close to identity chosen so that every basis overlap is nonzero. Then there is a PSD curve Y(t) of the SAME rank as Z(t), with compression F_0Y(t)F_0^T=Z(t), such that
  ||A_U(Y(t)-Y_*)||_2 = Theta(||e(t)||_2²),
  ||Y(t)-Y_*||_F >=||Z(t)-Z_*||_F.
The constants are fixed for the instance and the chosen exterior rotation.

**Proof.** Since both frames are the same G and Parseval holds, sum_j e_j(t)=tr[Z(t)-Z_*]=0. Theorem A supplies X_t of range in ran Z(t) with
  2 diag(G^T X_t K)=-e(t),  ||X_t||_F<=C||e(t)||_2,
where a uniformly bounded right inverse exists by the fixed-rank and independent-edge hypotheses.

Let P_t in R^{m x r} be a full-column-rank Gram factor Z(t)=P_tP_t^T with sigma_min(P_t)>=sqrt(lambda). Define B_t=P_t^dagger X_t in R^{r x(M-m)}. Then P_tB_t=X_t and ||B_t||=O(||e(t)||).

In the canonical two-zero ambient decomposition
  R^n = (source R^m) direct-sum Q1 direct-sum Q2,
with each Qj of order z=M-m, the source embedding is F_0^T and the first/second nonzero basis vectors have exterior components K e_j in Q1/Q2 respectively. Define the Gram factor
  L_t=[P_t; B_t^T; B_t^T] in R^{(m+2z) x r}.
Its Gram matrix, transported to ambient coordinates, is PSD of rank r and compresses exactly to Z(t). In each basis the source data change e_j(t) and the linear source-to-exterior cross contribution 2diag(G^T X_t K)=-e(t) cancel EXACTLY. Every remaining measured change comes from the quadratic exterior block B_tB_t^T and is O(||e(t)||²).

Choose a fixed exterior rotation Omega near identity so the two sets Q1 and Omega Q2 remain complementary and every basis overlap is nonzero. Let
  C_Omega=[J1,Omega J2] in R^{2z x 2z},
where J1=[I_z;0] and J2=[0;I_z].
It is invertible. Replace the lower Gram-factor block by
  ([B_t,B_t] C_Omega^(-1))^T.
Its source-to-Q1 and source-to-(Omega Q2) restrictions are exactly B_t, so the same cross cancellation occurs for both bases. The lower block stays O(||e(t)||), preserving PSD, rank, and the quadratic residual.

Finally the source trace is constant. The ambient trace defect equals the squared Frobenius norm of the nonzero lower Gram-factor block. Since the cross map is bounded and e(t)!=0, ||B_t||>=c||e(t)||, and the fixed exterior linear transformation has bounded inverse. Thus the ambient trace defect is Theta(||e(t)||²), so the FULL measured residual is not merely O but Theta(||e(t)||²). The Frobenius distance lower bound follows from isometric compression. QED.

## Theorem C — infinite family realizing the LOWER end of the universal exponent interval

For EVERY integer k>=1 there exists an explicit connected graph G_k, a uniquely recoverable real PSD graph target C_k, and a rank-one Parseval graph frame G, such that:

(i) C_k has graph/frame optimal attained recovery exponent
  alpha_source=2^(-k).
(ii) Its exact two-zero two-basis dilation, with all basis overlaps nonzero, has the sharp optimal attained exponent
  alpha_zero=2^(-(k+1)).
(iii) Its strictly-positive, no-zero-overlap, nonreflection second lift from Milestone 24 has sharp optimal attained exponent
  alpha_positive=2^(-(k+1)).
The final target has rank k+3, strictly positive two-basis data, and can be normalized to trace one.

The exact orders can be chosen
  m=2k+2,
  e=(k²+7k+2)/2,
  M=m+2e=k²+9k+4,
  n=2M-m=2k²+16k+6,
  N=5n+4=10k²+80k+34.

Hence the quantitative interval proved in Milestone 24,
  alpha_source/2 <= alpha_final <=min(alpha_source,1/2),
is SHARP at its LOWER END for EVERY dyadic alpha_source=2^(-k), not only for a Lipschitz source or the k=1 example.

### Construction of G_k and C_k

Take anchor vertices a_0,...,a_(k+1) forming a clique. Add descendants b_1,...,b_k; define b_0=a_0 and join b_i to b_(i-1) and a_i for each i>=1. All diagonal entries are measured and prescribed equal one; distinct anchor entries are zero; both parent entries for each b_i are s=1/sqrt(2).

Use the Gram representation in R^(k+2):
  p(a_j)=e_j,
  p(b_0)=e_0,
  p(b_i)=s[p(b_(i-1))+e_i], i=1,...,k.
Its Gram matrix C_k is PSD rank k+2 with trace m. At each step the two parents p(b_(i-1)) and e_i are orthogonal unit vectors, so the measured unit norm and inner products force p(b_i) to equal their normalized sum in ANY Gram realization. Thus the PSD completion is unique among all ranks.

Every measured edge joins two linearly independent target Gram vectors: anchor edges join distinct orthonormal vectors, and each descendant-parent edge joins a proper normalized sum of two independent parents to one of them. Therefore Theorems A/B apply. All graph-frame outcomes are strictly positive, since every vertex has norm one and no measured edge joins parallel or antiparallel vectors.

### Optimal source exponent

Let X>=0 be any graph competitor with graph residual delta. Choose Gram vectors q_v. Set
  r_i=q_(b_i)-s(q_(b_(i-1))+q_(a_i)).
For i=1, expansion of ||r_1||² uses only graph-measured entries and the anchor edge a_0a_1, giving ||r_1||²=O(delta) and ||r_1||=O(delta^(1/2)).
Inductively, on expressing q_(b_(i-1)) as the prescribed fixed linear combination of anchor Gram vectors plus an error O(delta^(2^(-(i-1)))), its inner product with the independent anchor q_(a_i) is O(delta^(2^(-(i-1))}). The expansion
  ||r_i||²=<q_(b_(i-1)),q_(a_i)>+O(delta)
therefore gives
  ||r_i||=O(delta^(2^(-i))).
Every Gram vector q_v is thus its target anchor linear combination plus an error of size O(delta^(2^(-k))), and the anchor Gram matrix differs from the identity by O(delta). All entries of X-C_k differ by O(delta^(2^(-k))), so
  ||X-C_k||_F <=C delta^(2^(-k))
for ALL PSD competitors.

For sharpness retain all anchors e_j and choose
  p_t(b_1)=s sqrt(1-t²)(e_0+e_1)+t e_2.
For i>=2 let
  beta_i=<p_t(b_(i-1)),e_i> >0,
  p_t(b_i)=s/(1+beta_i)(p_t(b_(i-1))+e_i)
           +sqrt(beta_i/(1+beta_i)) e_(i+1).
Every descendant remains unit norm; for i>=2 both parent inner products remain s. The only measured changes are the two first parent edges, by O(t²); every graph diagonal stays exactly one, so the trace is exactly m. Let
  u_1=t, u_i=sqrt(u_(i-1)/(1+u_(i-1))), i>=2.
Then the unmeasured Gram entry (b_k,a_(k+1)) is u_k~t^(2^(-(k-1))) while its target value is zero. Therefore
  ||C_k(t)-C_k||_F >=c t^(2^(-(k-1))),
  ||M_G(C_k(t)-C_k)||_2=Theta(t²).
This excludes every exponent larger than 2^(-k). The source upper bound proves attained alpha_source=2^(-k).

### Halving and final positive lift

The anchor Gram block of C_k(t) is the identity I_(k+2), and C_k(t)=P_tP_t^T with P_t containing those anchor rows. Hence rank C_k(t)=k+2 for all t, and its smallest positive eigenvalue is >=1. All measured-edge Gram pairs stay independent for small t. By Theorem B the two-zero lift admits a fixed-rank PSD competitor curve with
  data residual Theta(t^4),
  distance >=c t^(2^(-(k-1))).
Thus any valid lifted exponent must satisfy
  4 alpha <= 2^(-(k-1)),
i.e. alpha<=2^(-(k+1)).
Conversely the all-ambient error bound in Milestone 21 gives
  omega_zero(delta)
     <=omega_source(C sqrt(delta))+C sqrt(delta)
     =O(delta^(2^(-(k+1)))),
so the exponent is attained exactly.

Apply the signed-anchor positive-data lift from Milestone 24. Its exact all-ambient error comparison is
  omega_final(delta) <= C omega_zero(Cdelta)+C sqrt(delta),
while embedded curves preserve Frobenius distances and have comparable residuals. Since 2^(-(k+1))<=1/4, the sharp exponent of the FINAL all-positive two-basis problem is the same 2^(-(k+1)). The signed lift adds exactly one to rank and trace, gives nonzero overlaps and a nonreflection transition by a small equal-weight rotation, and all target outcomes are strictly positive. Divide by m+1 to obtain trace one.

## Corollary — fixed source geometry admits both SHARP and LOSSY two-basis embeddings

The same uniquely completable graph instances G_k also admit the original single-certificate reflection graph lift from Track 02 with exponent exactly 2^(-k), dimensions O(k²), rank k+3 and strictly positive observations. In contrast, the generic two-zero-plus-positive-compiler lift has exponent exactly 2^(-(k+1)). Thus exact fibre equivalence, rank, positive data and polynomial dimension DO NOT determine the recovery exponent. The exposure geometry of the EMBEDDING itself is an additional essential invariant.

## Hostile audit

1. The source graph upper bound is proved for every PSD competitor in arbitrary Gram dimension; it is not inferred from special curves or facial depth.
2. The source curve has EXACTLY fixed trace, so the trace constraint does not prevent cancellation of its leading measured error.
3. Edgewise linear independence is checked at the target on every graph edge, and remains under small fixed-rank perturbations.
4. The restricted cross-data map is onto the ENTIRE trace-free output space, with a locally bounded right inverse. The proof explicitly computes its adjoint nullspace and uses connectedness, not a generic-rank guess.
5. The PSD lifted curve is built as a Gram factor. It has unchanged rank and a quadratic exterior block; no unsupported PSD Schur-complement assumption appears.
6. Exterior rotations preserve cross-data cancellation through the explicit invertible complementary-subspace matrix C_Omega.
7. The residual is Theta(||e||²), not just O, because its trace defect is strictly positive of that order.
8. The all-ambient upper bound is separately proved by the two-zero positive certificate, and then the signed second-stage certificate; optimality is not inferred from a single curve.
9. The strict positive final data and nonzero basis overlaps arise only after the signed second stage; the zero-datum first stage is not mislabeled positive.
10. This is a sharp LOWER-END counterexample for a SPECIFIC universal compiler architecture, not a proof that all two-basis embeddings must halve exponents.
