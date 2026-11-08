# Rigidity-certified quadratic universality on a full-dimensional open family

Track 02 mathematical research memorandum, 2026-11-07/08. Exact finite-dimensional proofs; not externally peer reviewed.

## A. Main theorem

Let A:S^m -> R^p be a real trace-controlled linear PSD measurement map, normalized so I_m lies in L=range(A*). Let s=codim(L) and choose linearly independent trace-zero symmetric matrices K_1,...,K_s spanning L^perp.

Assume there exists an orthogonal Q for which all Q^T K_a Q have zero diagonal. In this basis set k_ij=((K_1)_ij,...,(K_s)_ij) in R^s for i<j. Define the rigidity operator
  R_K:(R^s)^m -> R^{m choose 2},
  (R_K lambda)_ij = k_ij dot (lambda_i-lambda_j).
Assume
  ker R_K = {lambda_1=...=lambda_m}.
Equivalently, rank R_K=s(m-1). The condition is a finite linear-algebra rank test.

**Theorem.** Put q=dim L=m(m+1)/2-s. There exists a finite algebraic rank-one Parseval frame g_1,...,g_M in R^m with M<=q+m, whose projectors all lie in L and span L. In particular, the signed exposing construction yields a two-orthonormal-basis PSD representation of order
  N<=q+4m+4
with the following properties for every feasible datum b:
(i) the exact full ambient PSD fibre is E(F_b);
(ii) the positive decoder D satisfies D(E(X))=X, the encoding is Frobenius-isometric, and rank E(X)=rank X+1;
(iii) source objective <C,X> is represented exactly for all ambient matrices Y by <F^T(C direct-sum 0)F,Y>=<C,D(Y)>;
(iv) for arbitrary ambient PSD Y of any rank, its source residual is bounded linearly in its two-basis residual and its off-model distance is O(delta)+O(sqrt(delta)) with explicitly computable singular-value constants;
(v) the local worst-case moduli obey omega_tilde_b(t)~omega_b(t)+sqrt(t) for b!=0 and omega_tilde_0(t)~t;
(vi) the basis change has no zero entries, observations at all feasible sources are positive, and a small equal-weight coordinate rotation makes the basis change non-reflection (even under independent signed row/column permutations) with genuinely different source quadratic observations.

Every non-Lipschitz PSD modulus is therefore preserved up to multiplicative constants. No graph-completion, commutation, or sparsity hypothesis is needed.

## B. The linear-algebraic rigidity-to-spanning principle

Work in a hollow basis. Let Z={x in R^m:x^T K_a x=0 for all a}. The desired claim is
  span{xx^T:x in Z}=L.

At each coordinate vector e_i, the Jacobian of the defining quadratic system has rows 2(K_a e_i)^T. Its restriction to e_i^perp is the s-by-(m-1) matrix A_i with columns k_ij. Each A_i has row rank s: otherwise a nonzero lambda_i perpendicular to all k_ij, with all other vertex coefficients zero, would be a nonconstant element of ker R_K.

Consequently Z is a real-analytic manifold near e_i, and every tangent u in
 T_i={u:u_i=0, k_ij dot u_j summed over j != i equals 0}
is realized by a smooth isotropic curve x_i(t)=e_i+t u+O(t^2).

Let S be a symmetric matrix orthogonal to all xx^T, x in Z. Since e_i in Z, S_ii=0. Differentiating x_i(t)^T S x_i(t)=0 at t=0 gives u^T S e_i=0 for all u in T_i. Therefore the off-diagonal row (S_ij)_{j!=i} belongs to the row span of A_i, and there are unique lambda_i in R^s such that
  S_ij=lambda_i dot k_ij.
Symmetry implies (lambda_i-lambda_j) dot k_ij=0 for all i<j. Rigidity forces all lambda_i equal, hence S=sum_a lambda_a K_a. Thus the orthogonal complement of the rank-one projector span is L^perp. This proves the claim, including degenerate/rank-deficient K_a as long as the stated R_K rank holds.

Moreover, the finitely many projectors e_ie_i^T and their curve derivatives e_i u^T+u e_i^T already span L. Their number is at most m+m(m-1-s). Choose small nonzero algebraic curve parameters, and the actual isotropic projectors together with e_ie_i^T still span L by continuity of a nonzero maximal minor. Extract q independent projectors P_j=x_jx_j^T. This is a finite algebraic construction: choose independent tangent bases, use the implicit function theorem to isolate the unique small real root of the s quadratic equations for each curve, and verify the rank of the selected projectors. Certified Newton iteration gives weak approximations with complexity polynomial in the inverse Jacobian margins and logarithmic precision.

## C. A constructive strict Parseval completion using the same rigidity condition

The map H -> (diag(U^T H_a U))_a, with U in O(m), has at U=I derivative
  J_K(Omega)_{a,i}=2 sum_{j!=i} (K_a)_ij Omega_{ji}.
Its image is contained in s copies of the zero-sum subspace 1^perp. Its transpose is, up to a constant and signs, R_K. Hence rigidity implies J_K is surjective onto that target.

The finite-dimensional implicit function theorem consequently gives: for every trace-zero tuple H_a sufficiently close to K_a, there is an orthogonal U(H) near I such that diag(U(H)^T H_a U(H))=0 for all a. A local right inverse to J_K and a contraction/Newton scheme make this effective under an explicit positive smallest-singular-value margin.

Choose the q independent isotropic projectors P_j from Part B. For sufficiently small epsilon>0,
  B=I-epsilon sum_j P_j
is positive definite and belongs to L. Thus
  H_a=B^(1/2) K_a B^(1/2)
are traceless and close to K_a. Apply the preceding simultaneous-hollowization lemma to find an orthogonal U_B for H_a. Set v_i=B^(1/2) U_B e_i. Then
  v_i^T K_a v_i=0,  sum_i v_i v_i^T=B.
Therefore
  {sqrt(epsilon)x_1,...,sqrt(epsilon)x_q,v_1,...,v_m}
is a positive Parseval frame of length q+m with every projector in L. Its first q projectors are independent, so the full projector span is exactly L.

This argument proves a strict local cone statement as well: every positive definite B in L sufficiently close to I admits a decomposition B=sum_{i=1}^m v_iv_i^T with each v_iv_i^T in L. It avoids unverified claims that individual isotropic vectors extend to entire isotropic ONBs.

## D. Exact two-basis dilation and quantitative transfer

Use the admissible hollow basis u_i and the q+m-vector Parseval frame above. Assign at each u_i the three columns a u_i,c u_i,c u_i with weights -1,2,3, where h=1/10,
  a^2=(5+3h^2)/7, c^2=(1-5h^2)/7,
and assign each Parseval column h g_j weight 4. The resulting d=m by n_0=3m+M matrix A_0 satisfies A_0 A_0^T=I and A_0 D_0 A_0^T=0.

Let r_i=h sum_j <u_i,g_j>, let t=2 sqrt(M+1), assign anchor coefficients
  z_{i,-}=(2r_i+t)/(3a), z_{i,2}=-(5r_i+4t)/(3c), z_{i,3}=t/c,
and z=1 for every g column. Then A_0 z=A_0 D_0 z=0, all z entries are nonzero and bounded polynomially in M. Choose a sufficiently small epsilon_anchor>0 by a finite rational grid avoiding each of the finitely many inner-product cancellation values. Append three pure anchor columns with signed weights -1,2,4 and positive squared lengths x^2,y^2,v^2, with v^2=1/100 and
  x^2=[2+epsilon_anchor^2(q_0-2s_0)+2v^2]/3,
  y^2=[1-epsilon_anchor^2(s_0+q_0)-5v^2]/3,
where s_0=z^T z and q_0=z^T D_0 z.
The full (m+1)-by-N frame F then obeys
  FF^T=I, FDF^T=0.
Its column inner products are nonzero and none of its squared column norms equals 1/2.

Write P=F^T F, Q=I-P, R=P-Q. Since D has exactly m+1 entries -1 and all other entries >=2, the standard isotropic graph argument proves
  S_0=D+RDR=2QDQ >=2Q.
Thus every exact ambient PSD competitor has support in range(P).

The compressed projectors span exactly
 {Z=[B,z;z^T,s]:B in L, z arbitrary, s arbitrary}.
For the source model E(X)=F^T(X direct-sum [1])F, this gives the exact fibre identity for every b, including nonsingleton fibres and all ambient ranks. The source decoder is D(Y)=(F Y F^T)_{1:m,1:m}, which is positive and returns X on E(X). Frobenius distances and source ranks are preserved, except for the added rank-one anchor.

For arbitrary Y>=0 with residual delta from E(F_b), the measured certificate implies tr(QYQ)<=kappa delta for kappa=||diag D||_2/sqrt 2. Trace control bounds tr Y by T_b. Positivity then gives ||PYQ||_F<=sqrt(T_b kappa delta). On each unrotated coordinate, the average of first- and second-basis residuals cancels the off-support cross block exactly, leaving compressed residual O(delta). Let gamma_ret>0 be the explicitly computed least singular value of the retained compressed rank-one analysis map on the augmented measured subspace. Then
  ||A(D(Y))-b||<=c_2 delta,
  ||Y-E(D(Y))||<=c_1 delta+sqrt(2T_b kappa delta),
where c_1,c_2 are explicit polynomials in m,N,||A||,gamma_ret^(-1),kappa. Conversely embedded measurements satisfy upper and lower residual inequalities by equality of their kernels with A, with constants from sigma_min^+(A) and the frame analysis singular values.

For nonzero b, source feasible matrices have nonzero rank. In the ambient lift the target rank is at least 2; the cross-block space from any two positive target support directions into Q has dimension 2(N-m-1), whereas invisibility to the first diagonal and the single rotated coordinate imposes at most N constraints. Since N>2(m+1), there is a nonzero invisible cross block K. With G=K^T E(C)^dagger K, the exact same-rank PSD curve
  E(C)+t(K+K^T)+t^2G
has residual Theta(t^2) and distance at least sqrt(2)t||K|| from the entire lifted fibre. This gives the sharp sqrt(t) lower bound. For b=0, the original and embedded feasible sets are singletons and the rank-one anchor has every coordinate nonzero, so the ambient off-support cross block is linearly detected; its modulus is Theta(t).

The source PSD tangent-cone dichotomy (proved in the earlier Track 02 work) implies omega_b(t)=O(t) or omega_b(t)>=c sqrt(t); hence all non-Lipschitz moduli are preserved up to constants.

To avoid reflection symmetry, split one weight-4 g column into equal duplicates and rotate one of them with the pure anchor weight-4 coordinate. This leaves D invariant under the rotation and hence preserves S_0; the untouched duplicate preserves the compressed analysis span. A generic sufficiently small angle leaves all overlaps nonzero, yields genuinely different source measurements, and makes the row and column fourth-moment multisets unequal, ruling out independent signed-permutation equivalence to a symmetric reflection. The extra duplicate and third anchor are included in N<=q+4m+4.

## E. Full-dimensional open sets and sharp threshold

Let h_m be the real vector space of hollow symmetric m-by-m matrices (dimension E=m(m-1)/2) and t_m be the traceless symmetric space (dimension E+m-1). Consider the smooth map
  Psi:O(m) x h_m^s -> t_m^s,
  Psi(U,(H_a))=(U H_a U^T)_a.
At (I,K), the derivative spans all hollow perturbations plus the diagonal image of J_K; rigidity is exactly the surjectivity of this derivative onto t_m^s. The submersion theorem therefore implies that all sufficiently small traceless perturbations of K are simultaneously hollowizable and continue satisfying the rigidity test. The set of operator-system tuples admitted by the theorem contains a genuine open set, not just a thin common-conjugation orbit.

For every integer 1<=s<=floor(m/2), the complete graph K_m has s edge-disjoint spanning trees (classical Walecki/Nash-Williams-Tutte tree packing). Define K_a as the symmetric zero-diagonal adjacency matrix of tree a. Their edge supports are pairwise disjoint. The rigidity equation on each tree edge forces lambda_{a,i}=lambda_{a,j}; connectivity of each tree forces each coordinate lambda_a constant across all vertices. Thus rank R_K=s(m-1). All coordinate-row Jacobians have full rank as well. For m>=4 and s>=2 one can choose two trees whose adjacency matrices do not commute; arbitrary sufficiently small dense traceless perturbations remain in the open class.

The dimension threshold is sharp for the *robust simultaneous-hollowization mechanism*: the domain of Psi has dimension (s+1)E, while its target has dimension s(E+m-1). If s>m/2, the domain dimension is strictly smaller, so by Sard's theorem/semialgebraic dimension, its image has empty interior. Conversely the tree construction establishes nonempty interior for s<=floor(m/2). This does NOT rule out quadratic two-basis universality by other architectures at larger codimension.

## F. Effective computation and hostile audit

A regular hollowization witness U and the positive singular gaps of J_K and the finite tangent-projector analysis matrix are natural conditioning parameters. The null curves near e_i are solved by the implicit function theorem from s quadratic equations with a full-rank s-by-s dependent-variable Jacobian. Certified Newton iteration computes them to precision 2^-L in polynomially many operations in m,s,L and the reciprocal indicated gaps. A finite sample of such curves gives q independent projectors with a verifiable singular gap. The residual B=I-epsilon sum P_j is made close to I by a rational epsilon with polynomially bounded inverse in these gaps; a second certified Newton solve produces its admissible orthonormal diagonalization. The signed anchor parameters and finite grid have explicit polynomial separation margins. Exact coefficients can be specified by finite algebraic equations and isolating boxes. No claim of uniformly polynomial expanded minimal polynomial degrees is made.

The proof uses an actual positive decoder and holds for every ambient PSD competitor. The local cone Parseval completion, rather than individual ONB extension of arbitrary null vectors, closes a major potential gap. The open-family claim uses a surjective derivative, not merely a dimension count. For s>m/2 the impossibility is restricted to simultaneous hollowization, not to all PSD embeddings. All sharpness curves include their quadratic PSD repair. Normalization to trace one uses a fixed scalar, not competitor-dependent normalization.

Independent numerical tests are in RIGIDITY_OPEN_AUDIT.py and RIGIDITY_OPEN_RESULTS.json. They include m=4,s=2 and m=6,s=3 edge-disjoint tree examples; arbitrary dense traceless perturbations were successfully hollowized, the local null projectors attained rank dim L, and the completed frames had Parseval errors <=3e-15 and null-quadratic errors <=2e-15. These are diagnostic checks, not proofs.

Related established ingredients: Nash-Williams--Tutte edge-disjoint spanning-tree theorem; finite-dimensional implicit/submersion theorem; standard matrix-frame and conic conditioning estimates; the existing Track 02 reflection-exposure construction. The rigidity criterion, its dual spanning interpretation, the local Parseval completion, and the sharp robust codimension threshold are candidate new contributions pending comprehensive priority review.
