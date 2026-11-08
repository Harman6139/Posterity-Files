# Quadratic-size two-basis recovery for dense structured SDP measurement spaces

Date: 2026-11-07/08. Track 02. Self-audited mathematical memorandum; external priority and refereeing have not occurred.

## 0. Main results and exact scope

For real symmetric matrices, let A:S^m -> R^p be trace-controlled, normalize so I_m belongs to L=range(A*), and write F_b={X>=0:A(X)=b}. The local worst-case modulus is omega_b(t)=max{dist(X,F_b):X>=0, ||A(X)-b||<=t}. The map between two orthonormal bases is A_U(Y)=(diag Y,diag(U^T Y U)).

**Theorem A (dense hyperplanes, rank +1).** If L has codimension one in S^m, then a finite deterministic algebraic construction gives N<=m^2+4m+2, an orthogonal U with all entries nonzero, a positive encoder E and positive decoder D, and an affine data map Phi with
 {Y>=0:A_U(Y)=Phi(b)}=E(F_b).
For every X>=0, D(E(X))=X, rank E(X)=rank X+1, and ||E(X)-E(X')||_F=||X-X'||_F. Every target datum is strictly positive. The design may be chosen non-reflection even under independent signed row/column permutations. Costs are exactly preserved by pullback of D.

**Theorem B (many noncommuting constraints, rank +1).** The same dimension bound holds if L^perp has a basis K_1,...,K_s of nonzero traceless quadratic forms, each supported on its own member of a family of mutually orthogonal coordinate subspaces. Arbitrary simultaneous orthogonal conjugation is permitted; the transformed constraints are typically dense and need not commute. One may have s as large as floor(m/2).

**Theorem C (all commuting annihilators, quadratic order).** If all elements of L^perp commute, set k=2^ceil(log2 m), r=k-m (for m=1 take k=1). Then there is a deterministic algebraic construction with
 N<=k^2+4k+5 <= 4m^2+8m+5.
It has the same full-fibre, positive-decoder and objective properties, with
 E(X)=F^T((X direct-sum (tr X)I_r) direct-sum [1])F.
For X!=0, rank E(X)=rank X+r+1; at X=0 rank E(0)=1. Distances on the embedded model satisfy
 ||X-X'|| <= ||E(X)-E(X')|| <= sqrt(1+rm)||X-X'||.
The bases can again be made non-reflection and genuinely different on the embedded source family.

**Sharp full-ambient modulus.** In all three theorems, for every feasible b and every ambient PSD competitor (arbitrary rank),
  omega_tilde_b(t) ~ omega_b(t)+sqrt(t) if b!=0,
  omega_tilde_0(t) ~ t if b=0.
Here ~ denotes two-sided fixed-instance comparison for small positive t. The upper bound has an explicit source residual constant linear in the inverse minimum singular value of a finite compressed frame analysis map; a more detailed bound appears below. Consequently every non-Lipschitz PSD recovery modulus is preserved up to constants. This is stronger than preserving the optimal exponent alone.

These results do NOT prove N=O(m^2+p) for arbitrary noncommuting L^perp. The earlier deterministic width-adaptive O(m^4) theorem is the general fallback. Our codimension-two no-go theorem below applies only to direct/unassisted rank-one compression, not to all possible positive lifts.

## 1. A universal anchored-reflection compiler lemma

Let d>=m and let J:S^m->S^d be a positive linear injection with a positive linear decoder D_0:S^d->S^m, D_0(J(X))=X. Assume a measured rank-one Parseval frame g_1,...,g_M of R^d satisfies
  sum_j g_j g_j^T=I_d,
  span{g_j g_j^T}=W,
where W is a subspace containing I_d. Assume (a) for each j, J*(g_jg_j^T) belongs to L; (b) the compressed measurement kernel is J(ker A), possibly after adjoining measured auxiliary equations that determine J(X) from A(X); and (c) there is an orthonormal basis u_1,...,u_d with J*(u_i u_i^T) in L.

In the applications, W is exactly the set of symmetric d-by-d matrices whose original m-by-m block belongs to L, with all other blocks unrestricted. Then the kernel condition is immediate for the direct lift J(X)=X, and for J(X)=X direct-sum (tr X)I_r it follows from trace belonging to L.

**Conic reduction.** Put q=dim W. Select q independent projectors among the Parseval columns. Reserve half the coefficient of each. The remaining positive combination is still a representation of I minus the reserved combination, using the original projectors. Whenever more than q coefficients are active, use a linear dependence of the active projectors, subtract the largest permissible positive multiple, and eliminate one coefficient. The trace of a zero linear combination of nonzero PSD projectors is zero, so a dependence has both signs. At termination at most q remain. Adding the reserved columns back gives a Parseval frame of at most 2q vectors with the full original span; every selected independent projector retains at least half its original positive coefficient. This is a finite exact-arithmetic algorithm and uses O(poly(M,q,d)) arithmetic operations. Its bit complexity depends on exact-algebraic comparison/separation margins, and is not asserted to be uniform without such a conditioning promise.

**Signed frame.** Let h=1/10, a^2=(5+3h^2)/7, c^2=(1-5h^2)/7. At each u_i take a u_i,c u_i,c u_i with signed weights -1,2,3, and at every g_j take h g_j with weight 4. Their matrix A_0 and diagonal D_0 obey
 A_0 A_0^T=I_d and A_0 D_0 A_0^T=0.
Indeed a^2+2c^2+h^2=1 and -a^2+5c^2+4h^2=0.

Let R_i=h sum_j <u_i,g_j>, and t=2 sqrt(M+1). Assign to the three u_i columns the anchor coefficients
 z_{i,-}=(2R_i+t)/(3a), z_{i,2}=-(5R_i+4t)/(3c), z_{i,3}=t/c,
and to each g_j column coefficient 1. All are nonzero, because |R_i|<=h sqrt M<t/2. Direct substitution gives A_0 z=A_0D_0 z=0.

Choose epsilon>0 sufficiently small and off finitely many roots of the linear equations
 <v_i,v_j>+epsilon^2 z_i z_j=0, for i<j.
One quantitative exact grid is epsilon^2=theta(1+j/L_0), with theta=[10^8(n_0+1)(M+1)]^{-1}, n_0=3d+M, L_0=2n_0^2+2, and 1<=j<L_0. At most one grid point per pair can be within theta/(4L_0) of its forbidden root. Therefore a grid point avoids all off-diagonal zeros, with separation at least a fixed inverse polynomial in n_0,M. The small theta also controls anchor mass and prevents column norms from crossing 1/2.

Set s=z^Tz, q_0=z^T D_0z, and insert THREE pure-anchor columns with weights -1,2,4. Fix their final squared length v^2=1/100, and solve
 x^2=(2+epsilon^2(q_0-2s)+2v^2)/3,
 y^2=(1-epsilon^2(s+q_0)-5v^2)/3.
These are positive and differ from 1/2. Define F by columns (v_j,epsilon z_j), xe_c,ye_c,ve_c, and extend D by -1,2,4. Then
 FF^T=I_(d+1), FDF^T=0.
The ambient order is N=3d+M+3, before one extra duplicate used for asymmetry.

Let P=F^T F, Q=I-P, R=P-Q=2P-I. The orthogonal reflection R has no zero entry: off-diagonal entries are twice the nonzero column inner products, and diagonal entries are twice squared norms minus one. Its two-basis span contains the signed exposing certificate
 S_0=D+RDR=2QDQ >= 2Q.
For the gap: D has exactly d+1 negative entries equal to -1, and all other entries at least 2. Since PDP=0, the isotropic subspace range(P) is a graph {(x,Tx)} over the negative coordinate subspace, with T^T D_+ T=I and ||T||^2<=1/2. Every perpendicular vector is (-T^T w,w), whose D-quadratic form is at least its Euclidean squared norm. Hence QDQ>=Q.

**Non-reflection without losing the certificate.** Duplicate a selected weight-4 g column into two equal halves before making F; use only one duplicate in the following rotation and retain the other. Rotate this selected weight-4 coordinate with the pure-anchor weight-4 coordinate through a small nonzero angle phi, writing U=R O_phi. Since O_phi commutes with D,
 D+UDU^T=D+RDR=S_0>=2Q.
The rotated compressed projectors remain in W: their old top block is a multiple of the selected g_jg_j^T, and all additional terms are measured anchor cross/diagonal terms. The untouched duplicate retains the original compressed span. A small angle retains strict overlap and data positivity.

To prove U is not equivalent to a reflection under independent signed permutations, compare multisets of row and column fourth moments. An unrotated column has constant fourth moment. The fourth moment of every row is a nonconstant trigonometric polynomial in 4phi, because both selected columns of R have nonzero entries in that row. Outside finitely many angles no row fourth moment equals the chosen fixed column moment, whereas a signed-permutation-equivalent symmetric matrix necessarily has equal row and column moment multisets. Rational tangent-half-angle sampling avoids these finitely many roots constructively. If dim L>=2, select a non-scalar original g_j projector; the rotated columns then produce different nonconstant source quadratic observations.

The outer anchor makes every target observation positive, including the zero source, and the old projectors are exactly the desired W projections. The certificate confines every exact ambient PSD solution to range(P). Compressing then proves the claimed complete fibre identity among unrestricted-rank competitors.

## 2. Arbitrary ambient noise and sharp rates

Write Y>=0 in P,Q blocks as PYP, QYQ, and K=PYQ. Put delta=||A_U(Y)-Phi(b)||. The exposing certificate implies
 tr(QYQ)<=kappa delta, kappa=||diag(D)||_2/sqrt(2).
Since diagonal measurements include the trace, for delta<=1,
 tr Y <= T_b:=tr(E(C))+sqrt N, for any C in F_b.
Block PSD Cauchy-Schwarz gives
 ||K||_F^2 <= T_b kappa delta.
Thus ||Y-PYP||_F<=kappa delta+sqrt(2T_b kappa delta).

For every unrotated coordinate, the average of its two basis residuals cancels K exactly, leaving a compressed frame residual bounded by (1/sqrt(2)+kappa)delta. The one selected g measurement removed by the rotation is recovered from its untouched duplicate, while the other unrotated projectors still span the full compressed W. Let gamma_ret>0 denote the smallest singular value of this explicitly given retained analysis map restricted to W; it is computable by finite linear algebra. Then
 ||P_W(FYF^T-Z_*)||_F <= (1/sqrt(2)+kappa)delta/gamma_ret.
The top source block B=(FYF^T)_{1:m,1:m} is PSD. In Theorem A/B, the compressed model is B direct-sum [1]. In Theorem C it is B direct-sum (tr B)I_r direct-sum [1]. All off-model blocks lie in W; trace is measured because I in L. Thus the positive retraction E(B) obeys
 ||Y-E(B)||_F <= c_1 delta +sqrt(2T_b kappa delta),
 ||A(B)-b||_2 <= c_2 delta,
with c_1,c_2 bounded by explicit polynomials in m,N,||A||,kappa,gamma_ret^{-1}. One valid structural choice is
 c_2=||A||(1/sqrt(2)+kappa)/gamma_ret,
 c_1=4(1+sqrt(r)+sqrt(d))(1/sqrt(2)+kappa)/gamma_ret+kappa,
where r=0 in A/B and r=k-m in C. This is a normalized condition-dependent bound; no uniform lower bound on gamma_ret is claimed.

The decoder is positive, D(Y)=B. Every source cost C has an ambient cost F^T(C direct-sum 0)F, giving exactly <C,D(Y)> for all symmetric Y. The embedding changes distances by factor 1 in A/B and by a factor in [1,sqrt(1+rm)] in C. Forward and reverse encoded residuals are linearly comparable using the nonzero singular values of A and the retained frame analysis. Hence
 omega_tilde_b(t) <= L_E omega_b(c_2t)+c_1t+sqrt(2T_b kappa t),
 with L_E=1 in A/B and sqrt(1+rm) in C,
and omega_tilde_b(t)>=omega_b(t/c_3) for an explicit finite c_3.

If b!=0, choose a nonzero C in F_b; the lifted target has rank at least two. With source support projector R_*, support-to-exterior cross blocks K=R_*KQ have dimension at least 2(N-d-1), while first diagonal invisibility imposes at most N-1 independent constraints and the selected two-coordinate rotation adds at most one. Since N>2(d+1), a nonzero invisible K exists. Setting G=K^T E(C)^dagger K gives a PSD same-rank curve
 Y(s)=E(C)+s(K+K^T)+s^2G
     =(I+sK^T E(C)^dagger)E(C)(I+s E(C)^dagger K).
Its residual is O(s^2) and its distance from the entire lifted fibre is at least sqrt(2)s||K||. This proves omega_tilde_b(t)>=c sqrt t.

If b=0, trace control forces F_0={0}. Crucially in Theorem C the auxiliary block is (tr X)I_r, NOT a fixed identity. Thus E(0) has rank one in all three constructions. The anchor vector has no zero coordinate. The retained compressed measurements control the source, auxiliary and anchor errors linearly; positivity controls all non-anchor cross blocks linearly, and the first diagonal then detects anchor-to-exterior cross blocks via entrywise multiplication by the nonzero anchor vector. Hence omega_tilde_0(t)=Theta(t).

Finally the PSD tangent-cone dichotomy (established in the preceding Track 02 work) says omega_b(t)=O(t) or omega_b(t)>=c sqrt t. Thus every non-Lipschitz source modulus is preserved, as a function, up to multiplicative constants. For b!=0, a Lipschitz source acquires the sharp square-root modulus. The bounds are full-cone, not fixed-rank statements.

## 3. Proof of Theorem A: sparse-grid parametrization of every isotropic hyperplane

Write L=K^perp with K!=0 and tr K=0. Thus K is indefinite. Choose rational p,n with p^T Kp>0>n^TKn. If a diagonal element of K is nonzero, trace zero supplies opposite-sign coordinate directions; otherwise an off-diagonal nonzero entry supplies e_i+e_j and e_i-e_j. Make the negative vector K-orthogonal to p:
 n_0=n-(p^TKn)/(p^TKp) p.
Then q_K(n_0)<0. Set v_+=sqrt(-q_K(n_0))p+sqrt(q_K(p))n_0 and v_-=sqrt(-q_K(n_0))p-sqrt(q_K(p))n_0. Both are isotropic and B_K(v_+,v_-)!=0.

For either isotropic base v define the quadratic polynomial map
 f_v(u)=q_K(u)v-2B_K(v,u)u.
Then q_K(f_v(u))=0. For any isotropic x with B_K(v,x)!=0, choosing u=x+v yields f_v(u)=-2B_K(v,x)x. The two patches using v_+,v_- are dense in the full real null cone: if an isotropic x is orthogonal to both, x+t v_+ stays isotropic and has nonzero pairing with v_- for t!=0, approaching x.

Evaluate f_v on integer vectors u with at most four nonzero entries, each from {1,2,3,4}. There are O(m^4) candidates. If a symmetric H is orthogonal to every candidate projector f_v(u)f_v(u)^T, the homogeneous quartic polynomial f_v(u)^T H f_v(u) vanishes on this sparse degree-four interpolation grid and therefore vanishes identically. By the two-patch density just proved, x^THx vanishes on every K-null x.

The elementary null-cone lemma states that if K is indefinite and a quadratic form H vanishes on the entire zero set of K, then H=cK. To see this, make a real congruence taking K to diag(I_p,-I_q,0). Testing e_i+/-e_j across the positive and negative blocks kills all opposite-sign off-diagonal entries and equates positive and negative diagonal coefficients with opposite signs. Adding arbitrary nullspace components kills the null block and its cross terms. Testing e_i+e_k+sqrt(2)e_j, with i,k positive and j negative, kills same-sign off-diagonals; similarly for negative pairs. Thus H=cK.

Therefore the finite candidate projectors span L=K^perp. Select q=dim L=m(m+1)/2-1 independent candidates. Normalize their underlying isotropic vectors. Any isotropic unit vector extends to an orthonormal basis of isotropic vectors: its orthogonal complement has trace-zero compressed K, so one may repeat the indefinite/zero case inductively. Extend each selected vector to such a basis. The union of q bases, scaled by 1/sqrt q, is Parseval and its projectors span L. The conic reduction in Section 1 produces at most 2q columns. The signed dilation therefore has
 N<=3m+2q+4=m^2+4m+2
after duplication and the third pure anchor. All steps are finite explicit algebraic operations and exact comparisons. The source encoding is X->F^T((X direct-sum [1]))F, hence rank amplification one.

## 4. Proof of Theorem B: independent block-isotropic constraints

After an orthogonal change of coordinates, let the annihilator be spanned by nonzero trace-zero K_i, each supported on a distinct mutually orthogonal block E_i. Include an unconstrained complementary block E_0 when present.

Within each E_i the preceding hyperplane theorem gives an isotropic orthonormal basis and a spanning family of isotropic projectors; E_0 is unrestricted. For two different blocks, take isotropic vectors u in one and v in the other. Both u+v and u-v are null for every K_i, and subtracting their rank-one projectors recovers the cross block uv^T+vu^T. Isotropic vectors span each block, so these cross blocks span every off-diagonal block. Together with the within-block projectors they span precisely L.

Every selected within-block vector extends to a global admissible ONB. Every selected cross vector (u+v)/sqrt2 does also: extend u and v separately to admissible bases in their blocks, and rotate the two basis vectors u,v through 45 degrees, leaving all other vectors fixed. The rotation remains isotropic for all block constraints. Thus a finite set of q=dimL independent projectors, each extendable to a global admissible ONB, exists. The union of q such ONBs is a spanning Parseval frame. Conic reduction plus signed dilation gives N<=m^2+4m+2, rank +1, and the general modulus theorem. The K_i may become dense and noncommuting after a common generic orthogonal conjugation.

## 5. Proof of Theorem C: commuting annihilators in quadratic order

Simultaneously diagonalize L^perp. In the resulting coordinates, L consists of arbitrary off-diagonal entries and a diagonal vector lying in a subspace V of R^m containing 1. Let h=dim V-1, and choose traceless independent vectors a_1,...,a_h in V with ||a_i||_infinity<=1.

Let k be the least power of two >=m, r=k-m, and choose a real Hadamard matrix H_k. Its normalized columns are an admissible ONB of R^k: their first m coordinates have equal squared magnitudes, and thus their top-left rank-one blocks have diagonal in V.

Construct an additive-character sign family S of size M<=4m^2. Let q=2^ceil(log2 m), regard x=0,...,m-1 as distinct elements of the field F_q, label coordinate x by (x,x^3) in F_q^2, and take every additive character of F_q^2. The resulting signs s_j in {+/-1}^m satisfy
 (1/M)sum_j s_j s_j^T=I_m,
and the functions 1 and s_{j,a}s_{j,b} (a<b) are mutually orthogonal across j. Pair-sum labels are distinct: x+y and x^3+y^3 determine xy when x!=y, hence determine {x,y}.

We now build a positive Parseval frame on R^k=R^m direct-sum R^r whose projectors span
 W={Z in S^k:diag(Z_old) lies in V};
W has dimension q_W=k(k+1)/2-(m-h-1).

Let h'=max(h,1), using a dummy a_1=0 if h=0. First put in old-only vectors
 (sqrt(c_j) s_j,0), where c_j=1/(2M) except for m selected linearly independent sign rows, where c_j=1/(2M)-2eta r,
 eta=1/[16M(r+1)] when r>0, otherwise eta=0.
For each a_i, each sign +/- and every sign row s_j, add
 (s_j coordinatewise-multiplied by sqrt(1 +/- a_i/2) /sqrt(4h'M), 0).
The baseline contributes half the old identity (before the cross correction); the paired a_i families contribute the other half. Their individual projectors have allowed diagonal vectors in V. Taking the difference of the + and - family sums isolates the diagonal direction a_i, while the baseline sign products span all equal-diagonal/off-diagonal directions.

For each selected sign row s_i and auxiliary coordinate e_a, add the paired vectors
 sqrt(eta)(s_i,+e_a), sqrt(eta)(s_i,-e_a).
Their old covariance exactly replenishes the 2eta r removed from each selected baseline coefficient; their auxiliary covariance is 2eta m I_r. Their projector differences span all old-auxiliary cross entries because the m selected sign rows are independent.

For each auxiliary pair a<b add sqrt(zeta)(e_a+e_b) and sqrt(zeta)(e_a-e_b), supported only in the auxiliary block, with zeta=1/[8(r+1)^2]. They span auxiliary off-diagonals. Finally add pure auxiliary e_a with squared coefficient
 c_aux=1-2eta m-2zeta(r-1)>1/2.
The auxiliary covariance is exactly I_r, and all cross covariance cancels by opposite signs. Consequently the full family is Parseval, every projector lies in W, and the projectors span W (old off-diagonals, diagonal V, cross blocks, auxiliary symmetric blocks).

The family is initially of polynomial size O(m^3). Conic reduction leaves at most 2q_W rank-one columns, preserving tightness and the span. The Hadamard basis is separately admissible. Apply the signed-anchor dilation and duplicate one old column for the nonreflection rotation:
 N<=3k+2q_W+4 <= k^2+4k+4 <= 4m^2+8m+4.
The statement uses the slightly relaxed +5 bound to cover every edge case. Encoding is
 J(X)=X direct-sum (tr X) I_r.
It is positive, has positive decoder given by its leading principal block, and its rank is rank X+r for nonzero PSD X and zero at X=0. After the fixed positive anchor the claims in Theorem C follow from Sections 1-2. A simultaneous orthogonal change of coordinates returns to the original, possibly dense, measurement matrices.

## 6. A sharp obstruction to bare rank-one compression at codimension two

Let m>=3 and set
 K_1=diag(1,-1,0,...,0),
 K_2=e_1e_2^T+e_2e_1^T.
The space L={K_1,K_2}^perp contains I and has codimension two. If vv^T belongs to L, then
 v_1^2-v_2^2=0 and 2v_1v_2=0,
so v_1=v_2=0. Hence all permitted rank-one projectors are supported on span(e_3,...,e_m); their span cannot contain I and cannot equal L. Therefore no direct single-copy, data-faithful rank-one frame (and thus no single-copy reflection dilation built from such a frame) can represent this measurement space. A generic simultaneous orthogonal conjugation makes both constraints dense without changing the obstruction.

This does NOT rule out a different positive auxiliary lift, and therefore does not refute unrestricted quadratic-size universality.

## 7. Computational and adversarial audit

Exact-arithmetic complexity: finite-field sign construction, sparse degree-four interpolation, linear independence tests, conic support elimination, anchor square roots, and rational grid avoidance use polynomially many real-algebraic arithmetic operations. For rational input, output can be given by finite algebraic circuits. Uniform Turing bit-polynomial time is claimed only with appropriate nonzero pivot, sign-comparison, trace-normalization and retained-frame singular-value promises; unqualified polynomial-bit performance through arbitrary nested radicals is NOT claimed.

The source-residual conditioning is explicitly measured by gamma_ret and the positive singular values of A. Tiny gamma_ret can cause severe deterioration; neither polynomial conditioning in m alone nor dimension-free margins are asserted.

Audited hazards: (1) all full ambient PSD competitors are included, not merely encoded rank curves; (2) a positive decoder is used, never an indefinite Schur-complement subtraction; (3) squared-root curves include their quadratic PSD repair; (4) at the zero source the auxiliary trace-scaled block vanishes and the anchor remains rank one; (5) after rotation a retained duplicate restores the missing compressed measurement; (6) commuting and block-noncommuting classes are distinguished; (7) algebraic arithmetic operations are distinguished from uniform Turing bit complexity; (8) the no-go theorem is architecture-relative.

Small-case tests (independent floating-point consistency checks, not proofs): m=3 dense hyperplane with 5-dimensional compressed measurement space; m=4 two block constraints with 8-dimensional space; commuting m=3 and m=5 cases with full sparse-compiler ranks, exact matching encoded data along nontrivial original fibres, exposing certificate gap above 2 and near-machine-precision Parseval errors. See AUDIT_README.md and the test program.

Relevant prior art: Hildebrand (2014), Spectrahedral cones generated by rank 1 matrices, arXiv:1409.4781, studies rank-one-generated cones. This work does NOT assume those cones are rank-one generated; frame spanning and a positive Parseval identity suffice. The real symmetric hollowization/zero-diagonal observation is classical, as is finite-field sign orthogonality and conic Caratheodory reduction. The reflection exposing certificate is inherited and quantitatively extended from the preceding Track 02 research, not claimed to be independently novel.

**Unresolved:** unrestricted near-quadratic N=O(m^2+p) for completely arbitrary dense noncommuting annihilator spaces; constant-factor rank amplification for Theorem C when r grows; global uniform conditioning independent of input degeneracy; a comprehensive external novelty audit.
