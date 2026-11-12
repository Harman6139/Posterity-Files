# 132 — Rank universality, complete central spectra, and the single-paper architecture

**Date:** 2026-11-12.  
**Branch:** `research/psd-joint-depth-universal-20261107`.  
**Starting head:** `c050ce82501611ff0ce14ee5d1810abf309c9645`.  
**Purpose:** strengthen and consolidate ONE paper, not start another research program.  
**Status:** complete research arguments for the extensions below, conditional only on the established real-PSD one-switch theorem in Milestone 128 and standard Euclidean Jordan algebra facts explicitly identified below. These arguments have not been independently refereed. The literature audit is an examination of the cited primary sources, not a certification of worldwide priority.

## Executive recommendation

The strongest coherent paper is about **sharp tangency of affine spaces to irreducible symmetric cones**, not primarily about inverse recovery. Its core is the exact compatibility of an analytic invariant (the optimal error exponent), a facial invariant (minimum reduction depth), and a size invariant (cone rank).

There is a useful, compact strengthening: the attainable spectrum is **independent of the irreducible cone type at fixed Jordan rank**, and the one-switch construction realizes the **entire primal/dual central eigenvalue-order profile with arbitrary prescribed multiplicities**, while realizing every permitted minimum facial depth. These conclusions use the same proof mechanism; they do not require a separate theory of all facial rank profiles.

Recommended title:

> **Sharp error exponents and facial depth in irreducible symmetric cones**

Recommended first journal: **Transactions of the American Mathematical Society**. JLMS is a strong alternative. The rank-universal version gives a materially stronger generalist case than a recovery-only formulation, but does not establish that Advances in Mathematics would accept it. Do not delay submission for a full rank-profile classification or unrelated algorithmic applications. The remaining publication work should be consolidation and independent proof review.

---

# Part I. The geometric theorem

## 1. The invariant is an affine-section error exponent

Let V be a finite-dimensional Euclidean Jordan algebra, with unit e, trace inner product, rank N, and closed cone C of squares. For matrices, V is the space of real symmetric or complex/quaternionic Hermitian matrices and N is matrix order. Rank is not the vector-space dimension of V. Write x <= y when y-x belongs to C.

Let

\[
F=\{x\in C:A x=b\}\ne\varnothing,
\]

and let r be the largest Jordan rank of a point of F. Equivalently, r is the rank of the minimal face containing F. Assume initially 1 <= r < N and put nu=N-r.

Define the sharp bounded-set error exponent alpha(F) as the largest beta in (0,1] such that, on every bounded set, for all sufficiently small residuals,

\[
\operatorname{dist}(x,F)
\le c_B\bigl(\operatorname{dist}(x,C)+\|Ax-b\|\bigr)^\beta.
\tag{1.1}
\]

The constants may depend on the bounded set and the instance. This is not a global estimate with one constant for all unbounded x. The exponent is attained and sharp: on a ball around a relative-interior feasible point the worst-case modulus is Theta(delta^alpha). The proof below reduces this assertion to the singleton case.

Let d(F) be the **minimum** facial-reduction length to the minimal face, not the length of a selected certificate. On a current face with support idempotent f, a valid ambient stress Z satisfies

\[
Z\in(\ker A)^\perp,\qquad \langle Z,x_0\rangle=0,
\qquad Q_f Z\in C\cap V(f,1),
\tag{1.2}
\]

where x_0 is any relative-interior point of F, V(f,1) is the face's linear span, and Q_f is the orthogonal face compression. For matrices, Q_f Z=fZf.

### The arithmetic certificate

Choose k<=nu and strictly increasing weights

\[
0=w_0<w_1<\cdots<w_k=1,
\qquad 2w_i=w_{a_i}+w_{b_i},\quad
0\le a_i<i<b_i\le k\quad(1\le i<k).
\tag{1.3}
\]

For 1<=j<k set

\[
\ell(j)=\#\{1\le i<j:2w_i<w_{j+1}\},
\]
\[
p(j)=\min\{1\le i\le j:2w_i>w_j+w_{i-1}\},\qquad
u(j)=p(j)-1.
\tag{1.4}
\]

In this display the letter u in u(j) denotes the upper successor; it is unrelated to nullity nu. Let L(w), respectively U(w), count transitions from k to k-1 and then repeatedly using ell, respectively u, until zero. For k=1, L=U=1.

For fixed parents, the harmonic boundary system is nonsingular. A nonzero solution with zero boundary values would have a nonzero extreme value propagated along strictly increasing upper parents to the terminal boundary. Thus its solution is rational, and only finitely many parent assignments occur at fixed k. The weights can be written as ratios of integer determinants.

### Theorem A — rank-universal affine-section classification

For **every irreducible symmetric cone C of rank N**, and every 1<=r<N, the attainable pairs (d(F),alpha(F)) among nonempty affine sections with maximum feasible rank r are exactly the following:

\[
(d,\alpha)=(1,1),
\]

or there exist (1.3), with k<=N-r, and v in {1,...,k}, such that

\[
\boxed{\alpha=w_v/2\le w_1,\qquad L(w)\le d\le U(w).}
\tag{1.5}
\]

This is the **same set as for real positive semidefinite matrices of order N**. It is independent of the real/complex/quaternionic type, the dimension of the offdiagonal Peirce spaces, and the choice of irreducible cone of that rank. It includes the rank-two Lorentz cones and the rank-three exceptional cone, at their available ranks.

Every admissible pair can already be realized by a singleton section. Consequently the exact minimum-nullity characterization from Milestone 128 is also the exact minimum-rank-defect characterization for the real, complex, and quaternionic matrix series. The phrase "minimum dimension" must be translated to **Jordan rank** in this statement: ambient vector-space dimensions differ between cone types.

When r=N the bounded-set exponent is 1 and d=0. When F={0}, homogeneity gives exponent 1 and d=1. The theorem is not a classification of empty or weakly infeasible sections.

**Irreducibility is essential.** In an orthant, uniquely feasible sections have only exponent 1. Indeed, at a feasible x_0 the tangent cone consists of vectors nonnegative on zero coordinates. Uniqueness implies that this tangent cone meets ker A only at zero, since every such tangent vector is feasible for a sufficiently small positive displacement. Compactness of its unit section gives ||Ah||>=c||h|| for every tangent vector h. All x-x_0 with x in the orthant are tangent vectors, so the recovery bound is linear. In contrast S_+^2 has exponent 1/2 at a rank-one target. Thus total Jordan rank alone does not classify spectra for reducible symmetric cones.

---

## 2. Feasible-direction removal preserves the exponent and every facial chain

The real-PSD bounded-set version was already established in Milestone 15. The lemma here states and proves the Jordan-algebra version, and removes boundedness of F by working on bounded test regions. It is a reduction used in the main theorem, not an independent headline contribution.

### Lemma 2.1 — exact gauge reduction

Choose x_0 in ri(F), with support idempotent c and rank r, and put

\[
K=\ker A,\qquad M=K\cap V(c,1),\qquad
\widehat A h=(Ah,P_Mh).
\tag{2.1}
\]

Then x_0 is the unique C-feasible point with data widehat A x_0. The original and augmented systems have the same sharp bounded-set exponent and exactly the same valid facial-reduction chains.

**Proof.** Every feasible x is supported on c. To see this, relative interior gives x_0+t(x_0-x) in F for some t>0. Pairing with e-c shows <e-c,x>=0, and positivity forces x into V(c,1). Conversely, x_0 is interior in its face, so x_0 +/- s h belongs to F for small s when h belongs to M. Thus

\[
\operatorname{aff}F=x_0+M.
\]

A feasible point of the augmented system differs from x_0 by an element of M with zero M projection, and hence equals x_0.

Fix a bounded region. Write h=x-x_0=n+h_perp, where n=P_Mh, and set eta=||h_perp||. There is a fixed M_0 with ||n||<=M_0 on that region. Choose mu>0 with x_0>=mu c in its face. For x in C, its affine projection z=x_0+n satisfies z>=-eta c, because Q_c x>=0 and the spectral norm of Q_c h_perp is at most eta. Therefore

\[
z'=(1-\theta)z+\theta x_0\in F,
\qquad \theta=\frac{\eta}{\mu+\eta}.
\]

It follows that

\[
\eta\le\operatorname{dist}(x,F)
\le(1+M_0/\mu)\eta.
\tag{2.2}
\]

Choose a fixed lambda>0 so small that (1-lambda)mu>=lambda M_0. Then

\[
\widehat x=x_0+\lambda h_{\perp}
=\lambda x+(1-\lambda)x_0-\lambda n\in C.
\]

Its gauge residual is zero, its original residual is lambda||Ax-b||, and its displacement from x_0 is lambda eta. Thus the original bounded-region modulus is at most a fixed multiple of the augmented singleton modulus at a constant multiple of the residual.

Conversely, an augmented residual-delta competitor has ||n||<=delta and

\[
\|x-x_0\|\le\operatorname{dist}(x,F)+\delta.
\]

All augmented small-residual competitors lie in any fixed neighborhood of x_0 for sufficiently small residual: uniqueness gives K' cap C={0}, strict positive separation bounds residual sublevels, and their limit points are feasible. This proves equality of the sharp exponents for on-cone competitors. When r<N, x_0+t e supplies a linear lower modulus, so the exponent-one case is also nontrivial. For general x, project to C: the projection changes x by dist(x,C) and changes the affine residual by at most ||A||dist(x,C). The on-cone estimate therefore proves (1.1), with the same sharp exponent.

For facial chains, let f>=c be a current support. An augmented stress has the form Z=Y+T with Y in K^perp and T in M. If Q_f Z is positive and annihilates x_0, positivity makes its compression to V(c,1) zero. Consequently <Z,T>=<Q_f Z,T>=0. But <Y,T>=0, so

\[
0=\langle Z,T\rangle=\|T\|^2.
\]

Thus T=0: every augmented stress at every possible intermediate face is already an original stress. The converse is immediate. All facial chains, not only their minimum lengths, coincide. QED.

---

# Part II. Complete proof of rank universality

## 3. Standard Jordan facts and the exact new argument

We use the spectral theorem, Peirce decomposition, self-duality, and quadratic representations of Euclidean Jordan algebras; see [FK94], Chapters II–V. These are standard inputs, not new claims. Define

\[
Q_a=2L(a)^2-L(a^2),\qquad L(a)x=a\circ x.
\]

For a positive invertible a, Q_a is a self-adjoint cone automorphism, its inverse is Q_(a^{-1}), and det(Q_a x)=(det a)^2 det x. The Hessian of -log det at x is Q_(x^{-1}). Positive elements have norm at most their trace. Faces correspond to support idempotents; Q_f is orthogonal projection onto V(f,1). Ordered Jordan eigenvalues are monotone for the cone order.

For orthogonal idempotents c_0,...,c_k with sum e, write V_ii=V(c_i,1) and V_ij for the cross-Peirce blocks. If a=sum a_i c_i, then Q_a acts by a_i^2 on V_ii and by a_i a_j on V_ij.

### Lemma 3.1 — block order bound

If x belongs to C and s_i=<c_i,x>, then

\[
\|x_{ij}\|\le (k+1)\sqrt{s_i s_j}.
\tag{3.1}
\]

In particular, s_i=0 forces all blocks touching c_i to vanish.

**Proof.** When all s_i>0, apply Q_a with a=sum s_i^(-1/2)c_i. The result is positive and has trace k+1, hence bounded norm. Its ij block is x_ij/sqrt(s_i s_j). Approximation by x+epsilon e handles zero traces. QED.

This is the precise replacement for the matrix two-by-two-minor estimate. Its exponents, unlike its constants, do not depend on Peirce multiplicities.

## 4. The fixed graded central chart

Consider first a unique positive-rank target x_*, and put K=ker A. Define

\[
c_t=\arg\max\{\log\det x:x\in\operatorname{int}C,
\ x-x_*-te\in K\}.
\tag{4.1}
\]

Uniqueness implies K cap C={0}; separation of K from the compact trace-one cone section gives a positive definite element of K^perp. This bounds every shifted feasible section. The section contains x_*+te, so strict concavity and divergence of -log det at the boundary give a unique maximum. Stationarity gives c_t^(-1) in K^perp. The polynomial central equations and uniqueness imply semialgebraicity and convergent Puiseux expansions. Boundedness and uniqueness give c_t -> x_*.

The central trace identity is

\[
N=\langle c_t^{-1},x_*\rangle+t\operatorname{tr}c_t^{-1}.
\]

Consequently c_t >= (t/N)e. With z_t=t c_t^(-1), we have z_t in K^perp cap C, tr z_t<=N, and <z_t,x_*><=Nt. A bounded right inverse of A* gives, for any y in C of residual at most delta,

\[
\boxed{0\le y\le N(1+\kappa\delta/t)c_t.}
\tag{4.2}
\]

Indeed <z_t,y><=Nt+kappa N delta. Normalize by Q_(c_t^(-1/2)); a positive element is bounded by its trace times e, and undo the normalization. This is a full-ambient bound, not an assertion about one selected path.

Start with c_0=support(x_*). Compress c_t to the complement of c_0, take the support of its first nonzero positive Puiseux coefficient, and repeat inside the remaining face. This yields orthogonal idempotents c_0,...,c_k, with positive ranks m_i, and strictly increasing diagonal orders

\[
0=w_0<w_1<\cdots<w_k\le1,\qquad
\sum_{i=1}^k m_i=N-r.
\]

The first coefficient on each V_ii is positive definite. Lemma 3.1 implies that the coefficient A_v of t^v has zero ij block whenever

\[
w_i+w_j>2v.
\tag{4.3}
\]

### Lemma 4.1 — finite positive coefficient rescaling

Suppose a finite generalized polynomial has positive definite first diagonal coefficient on V_ii at exponent w_i, and every coefficient satisfies (4.3). Multiply its coefficient of t^v by exp(sigma v^2). For sufficiently large fixed sigma, the polynomial is positive definite for sufficiently small t.

**Proof.** Normalize by Q_b with

\[
b=\sum_i e^{-\sigma w_i^2/2}t^{-w_i/2}c_i.
\]

The diagonal limit is the direct sum of its positive definite first coefficients. A cross block can survive only at v=(w_i+w_j)/2, and its multiplier then equals

\[
e^{-\sigma(w_i-w_j)^2/4}.
\]

All strictly higher-order blocks vanish. There are finitely many distinct grades. Choose sigma so large that the finite cross-block perturbation of the positive diagonal limit remains in the cone interior, and then take t small. QED.

If w_k<1, truncate the center through w_k and apply the lemma. Every nonconstant coefficient lies in K, since c_t-x_*-te belongs to K. This produces a positive definite exact feasible curve, contradicting uniqueness. Hence w_k=1.

Apply the lemma to the truncation through exponent one. Its residual is O(t), because A_v belongs to K for v<1 and A_1-e belongs to K. Its normalized positive limit supplies a thick lower chart. The envelope (4.2) transfers that lower chart to c_t. The center's diagonal orders and positivity bound its normalized trace from above. Thus, with a_t=sum t^(w_i/2)c_i,

\[
\boxed{c\sum_i t^{w_i}c_i\le c_t\le C\sum_i t^{w_i}c_i.}
\tag{4.4}
\]

No moving eigenbasis has been frozen: this is an order comparison in a genuinely fixed idempotent decomposition, not exact simultaneous diagonalization. The normalized center Q_(a_t^(-1))c_t is semialgebraic, bounded, and bounded away from the cone boundary; hence it has a positive definite limit.

## 5. Harmonicity, the sharp exponent, and both facial bounds

### Lemma 5.1 — harmonic grade obstruction

For every i<k, some nonzero block of H_i=A_(w_i) joins grades a<i<b with 2w_i=w_a+w_b.

**Proof.** H_i belongs to K, is positive definite on V_ii, and satisfies (4.3). Suppose there is no such equality block. Every nonzero cross-grade block then has midpoint strictly below w_i. Lower the whole grade w_i slightly, to w_i' between w_(i-1) and w_i, so all nonzero blocks of H_i still have midpoint at most w_i' under the modified weights. Add t^(w_i')H_i to the finite center expansion and apply Lemma 4.1. The old coefficients still satisfy the relaxed support inequalities. The resulting positive curve has residual O(t) and a V_ii diagonal bounded below by a positive multiple of t^(w_i'). This contradicts (4.2) and the original O(t^(w_i)) diagonal order. QED.

Choose one equality pair at each internal grade. This gives precisely (1.3), independently of the ranks m_i or dimensions of V_ij.

### Lemma 5.2 — sharp exponent from finite weighted support

For K nonzero define

\[
\tau(K,w)=\min_{0\ne h\in K}\max_{h_{ij}\ne0}\frac{w_i+w_j}{2}.
\tag{5.1}
\]

Then alpha=min(1,tau). If K=0, alpha=1. For k>=2,

\[
\alpha=w_v/2\le w_1
\]

for some v. For k=1 the possibilities are alpha=1 or 1/2.

**Proof.** The symmetric-cone Dikin modulus theorem was already established in Milestone 13. Here is the essential argument to make its use transparent. Set

\[
\rho_t=\max\{\|h\|:h\in K,
\ \|Q_{c_t^{-1/2}}h\|\le1\}.
\]

The points c_t +/- h are positive and have the same measurement residual as c_t. Along with x_*+te they give a lower bound proportional to t+rho_t. Conversely, write any residual-O(t) competitor as c_t+h+E, with h in K and ||E||=O(t). The envelope and c_t>=(t/N)e bound the normalized norms of h and E. Apply the same argument to c_t-x_*-te. It follows that

\[
\omega(t)\asymp t+\rho_t,
\tag{5.2}
\]

where a fixed rescaling of t absorbs ||Ae||.

Write c_t=Q_(a_t)M_t using (4.4), with M_t in a fixed compact subset of int C. Barrier-Hessian covariance under Q_(a_t), obtained by differentiating the determinant identity, gives

\[
\langle h,Q_{c_t^{-1}}h\rangle
\asymp\|Q_{a_t^{-1}}h\|^2
=\sum_{i\le j}t^{-(w_i+w_j)}\|h_{ij}\|^2.
\tag{5.3}
\]

This argument does not assume operator monotonicity of the quadratic representation. The finite support threshold tau is attained. A fixed h attaining it gives one side of rho_t=Theta(t^tau). Projection from K onto blocks of weight at least tau is injective; otherwise a nonzero vector would have smaller maximum support weight. Uniform boundedness below of this finite-dimensional injective map gives the other side. Equation (5.2) proves the formula.

For k>=2, H_1 is a nonzero kernel vector of maximum support weight w_1, so alpha<=w_1. Equality is a half-weight because the lowest harmonic grade has source parent zero. If alpha<w_1, a minimizing h has no null-null block. It cannot lie entirely in V(c_0,1), because small signed perturbations of x_* there would contradict uniqueness. Therefore its largest support-to-null block gives alpha=w_v/2. With k=1, the only nonzero block weights outside the support face are 1/2 and 1, proving the boundary alternatives. QED.

### Lemma 5.3 — universal facial sandwich

Every singleton system with grades w satisfies

\[
\boxed{L(w)\le d\le U(w).}
\tag{5.4}
\]

**Proof of the lower bound.** A positive compressed stress annihilating x_* has zero source block and all cross blocks touching it. Pair it successively with H_1,...,H_(k-1). Once all lower rows are zero, the only surviving pairing in H_i is its positive definite V_ii diagonal; all higher-higher blocks are forbidden by (4.3). Positivity forces this diagonal, and then the entire i-th row, to vanish. Thus a first exposing stress is supported on c_k. The constant coefficient of z_t=t c_t^(-1) is positive definite on c_k and zero elsewhere, so this first maximal step is attained.

Suppose an arbitrary current face contains the prefix f_j=c_0+...+c_j. For every i<=ell(j), 2w_i<w_(j+1), so H_i is entirely supported in V(f_j,1). The same successive pairings force all grades through ell(j) to survive the next step. This argument does not assume that the whole current face is a grade prefix. Induction gives d>=L(w).

**Proof of the upper bound.** By (4.4) and the inverse identity for Q_a, the diagonal leading orders of z_t are 1-w_i, with positive definite leading coefficients, and its ij block has order at least 1-(w_i+w_j)/2. All full Puiseux coefficients belong to K^perp.

On a current prefix f_j, take p=p(j) and truncate the compressed dual series through E=1-w_p. The rows below p vanish in this truncation. Indeed for a<p<=i<=j,

\[
1-(w_a+w_i)/2\ge1-(w_{p-1}+w_j)/2>1-w_p.
\]

The lower-lower blocks also occur after E. Every grade p,...,j has its positive definite first diagonal coefficient included. Lemma 4.1, applied to the dual weights 1-w_i, makes a fixed positive coefficient rescaling of the truncation positive definite on the suffix and zero on the lower prefix. It is the compression of a genuine linear combination of full coefficients in K^perp; its pairing with x_* is zero. It is therefore an actual ambient facial-reduction stress. Repeating the upper recurrence constructs U(w) steps. QED.

These arguments establish the necessary arithmetic conditions for **every** symmetric cone. Irreducibility will be used only for the converse, through a rank-preserving real-symmetric subalgebra.

## 6. The converse transfers without changing minimum depth

### Lemma 6.1 — a rank-preserving positive retraction

Every simple Euclidean Jordan algebra V of rank N contains a unital Jordan subalgebra S isomorphic to real symmetric N-by-N matrices, with the same rank, determinant, and trace on S. The orthogonal projection pi:V->S is positive and commutes with face compression by every idempotent in S.

**Proof.** Use the standard classification [FK94]. For real, complex, and quaternionic Hermitian matrices, take the real symmetric entries. For the exceptional algebra H_3(O), take the real symmetric 3-by-3 matrices. For a rank-two spin factor, choose two spatial coordinate directions; their unital subalgebra is H_2(R). Rank one is R. In each case real spectral idempotents remain primitive, proving rank and trace preservation, and the Jordan determinant restricts to the ordinary determinant.

For x in C and y in S_+, <pi x,y>=<x,y>>=0. Self-duality of S_+ gives pi x in S_+. If c is an idempotent in S, Q_c maps S to itself and is self-adjoint. Therefore pi Q_c=Q_c pi. QED.

### Lemma 6.2 — preservation of the full-ambient exponent and greedy faces

Let K_0 be a real-symmetric measurement kernel and x_* in S_+ a uniquely feasible target. In V impose the old measurements on pi x and also measure the entire S-perpendicular component. The new kernel is exactly K_0, viewed inside S. The sharp exponent, minimum facial degree, and every maximal-stress facial rank drop are unchanged. The maximum-determinant central curve is exactly the embedded original curve.

**Proof.** An ambient residual-delta positive competitor has pi x in S_+, old residual O(delta), and ||x-pi x||=O(delta). The old sharp error upper bound thus bounds its displacement with the same exponent, since alpha<=1. Embedded old sharp competitors give the converse. Exact feasible points lie in S, so uniqueness is unchanged.

For facial depth, consider a current face whose idempotent c is in S. Let p<=c be the largest support of an original valid compressed positive stress. Such a largest support exists: a finite positive sum of stresses realizes the union of all their exposed ranges. For any new valid ambient stress Z, the compressed element T=Q_c Z is positive. Its projection pi T=Q_c pi Z is an old valid compressed positive stress, hence supported on p. Thus

\[
\langle c-p,T\rangle=\langle c-p,\pi T\rangle=0.
\]

Positivity forces T to be supported on p, including all cross-Peirce components. Therefore no new ambient stress can expose anything beyond the old maximal support. The embedded old stress attains p. Induction identifies all greedy faces and their ranks.

For completeness, greedy maximal-stress facial reduction has minimum length: if f<=g, restriction of any valid stress on g is a valid stress on f, and positivity makes its kernel on f the intersection with the old kernel. Hence the greedy survivor map is inclusion-preserving. Induction shows its survivor after t steps is contained in the survivor of any other t-step chain. It reaches the minimal face in the fewest possible steps. Thus equality of greedy faces gives equality of minimum degrees, not merely equality of one chosen chain length.

Finally, the shifted affine slice x_*+te+K_0 lies entirely in S because the embedding is unital. Its positivity and determinant are the original ones. Therefore its determinant maximizer is exactly the embedded original maximizer. QED.

### Completion of Theorem A

Necessity follows from Lemma 2.1 and Sections 4–5. For sufficiency apply the established real-PSD Milestone 128 at order N and rank r, and then Lemmas 6.1–6.2. This proves the equality of attainable spectra for every simple cone. The minimum rank-defect formula is the identical finite arithmetic minimum from Milestone 128; its explicit finite cutoff carries over unchanged in the matrix series. No change of ambient coordinates, scalar field, or Jordan multiplication can improve that minimum. QED.

---

# Part III. One substantial optimization consequence

## 7. Complete central eigenvalue-order spectra

The consequence concerns the external maximum-determinant regularization (4.1), which is a specific, established family of feasibility central paths. It is **not** a theorem about all objective-barrier SDP central paths or all interior-point algorithms.

### Theorem B — exact joint primal/dual central-spectrum realization

Fix a simple Euclidean Jordan algebra of rank N, a positive target rank r<N, and positive integers m_1,...,m_k with sum N-r. Let m_0=r. For a singleton feasible section define c_t by (4.1) and z_t=t c_t^(-1).

For k>=2, the following data are attainable simultaneously if and only if w is a strict harmonic certificate (1.3), alpha=w_v/2<=w_1, and L(w)<=d<=U(w):

* exactly r eigenvalues of c_t have order Theta(1);
* exactly m_i eigenvalues of c_t have order Theta(t^(w_i)), for every i=1,...,k;
* the corresponding eigenvalues of z_t have order Theta(t^(1-w_i)), including the source exponent one;
* the full-ambient recovery exponent is alpha and the minimum facial degree is d.

For k=1, w_1=1, d=1, and alpha is either 1 or 1/2, with arbitrary multiplicity m_1=N-r.

Here "order" means two-sided power comparison, not a complete Puiseux series, its ramification index, or its leading coefficient. The theorem also does not require the eigenvectors to be constant.

**Necessity.** Sections 4–5 give the fixed order chart and all arithmetic restrictions. Ordered Jordan eigenvalue monotonicity applied to (4.4) gives the stated primal multiplicities. The eigenvalues of t c_t^(-1) are t divided by the primal eigenvalues, giving the dual orders. It remains to prove the prescribed-multiplicity converse; this is not contained in a classification of just the scalar pair (d,alpha).

### Lemma 7.1 — multiplicity lifting of the one-switch construction

Every real one-switch realization with scalar grades w_1,...,w_k can be replaced by one with any prescribed positive grade multiplicities m_i. It retains those exact central grades, the sharp exponent, and the same grouped greedy exposing schedule. If its scalar layer at step t is C_t, the new facial rank drop is sum_(i in C_t) m_i.

**Construction.** In the scalar construction of Milestone 128 replace each null diagonal E_ii by the identity I_i on an m_i-dimensional group. Select one representative coordinate in each group and put every old tight, release, blocker, and optional leading edge between the same representatives. All omitted entries are observed. Replace each generator's source diagonal coefficient by minus the total trace of its new null diagonal part. The source target remains rank one; fully observed positive support padding subsequently gives rank r. Choose the common positive rational edge coefficient lambda small relative to the total matrix order.

The tight generators have form

\[
\widetilde H_j=I_j+\sum_{i\in S_j\setminus\{j\}}I_i
-\Bigl(m_j+\sum_{i\in S_j\setminus\{j\}}m_i\Bigr)E_{00}
+\lambda F_{P_j}+\lambda F_{R_j},
\tag{7.1}
\]

with the same absent/duplicate/final-omitted release conventions as Milestone 128. An extra child i always has w_i<w_j. New blocker generators replace E_ii by I_i similarly. The optional pure leading edge is unchanged.

**Proof of the chart and exponent.** Let D_t be identity on the source and t^(w_i/2)I_i on group i. Assign each generator its old scalar degree: w_j for a tight generator, its edge midpoint eta>=w_i for a new blocker, and alpha for the optional leading edge. Normalize a degree-q generator as t^q D_t^(-1)H D_t^(-1). The normalized generators have independent limits: their unique main offdiagonal pivots are unchanged. A different generator can share a tight pivot only as a strictly higher-degree release, and therefore disappears at that pivot in the limit. Extra child identities disappear as well.

Their limiting span has a strictly positive definite separator. Put W on each group equal to z_i I_i, where z_i=exp(sigma w_i^2). On a tight main edge P_i put

\[
W_{P_i}=-\frac{m_i z_i}{2\lambda}.
\tag{7.2}
\]

Use the same assignment for a new blocker whose midpoint equals w_i; for a strictly safe blocker put its entry zero. Put every additional leading release and the optional leading edge equal to zero. There is no assignment conflict by the original edge-ownership and release-synchronization lemmas. The separator annihilates every leading form. Each nonzero normalized offdiagonal has a fixed multiplicity factor times

\[
\exp\{-\sigma(w_a-w_b)^2/4\}.
\]

For sufficiently large fixed sigma the matrix is positive definite by diagonal dominance. For rational weights the exponential notation can be replaced by integer powers of a sufficiently large rational base. Thus the limiting scaled kernel intersects the PSD cone only at zero.

For any ambient PSD residual-t competitor, write X-X_*=H+E with H in the new kernel and ||E||=O(t). The scaled term D_t^(-1)(X_*+E)D_t^(-1) is bounded because every weight lies in [0,1]. If D_t^(-1)X D_t^(-1) were unbounded, division by its norm and passage to a subsequence would give a nonzero PSD element of the limiting scaled kernel. The separator rules this out. Hence X<=C D_t^2. Independence of the normalized generator limits bounds each generator coefficient by its assigned power of t. This proves the full-ambient O(t^alpha) recovery bound.

Activate the tight generators at coefficients t^(w_i), add t I_k on the terminal group, and activate the optional leading edge at t^alpha when needed. Each group diagonal is t^(w_i)I_i plus nonnegative higher-order terms, the source diagonal tends to one, and normalized offdiagonals are small for fixed sufficiently small lambda. This is a positive definite curve with residual O(t), displacement Theta(t^alpha), and a thick D_t^2 lower bound. The central envelope gives the lower central chart; the all-competitor bound gives its upper chart. Thus the central multiplicities are exactly the prescribed m_i.

**Proof of exact facial degree.** In every generator equation replace a scalar stress diagonal Z_ii by the trace T_i of its compressed block on group i. For a positive compressed stress, T_i>=0; if T_i=0, the entire group row, including all cross terms, vanishes. The smallest-positive-child argument in the upper phase and the forced-survivor argument in the lower phase of Milestone 128 therefore apply without change to arbitrary stresses, not just block-diagonal ones. In particular, a stress cannot expose a proper part of a forbidden group prematurely.

To construct the attaining stresses, take the scalar formulas and replace each intended scalar trace z_i by the block (z_i/m_i)I_i, retaining the prescribed edge entries. Every generator pairing is then exactly the old pairing; the new source correction pairs with zero. Ordinary lower-phase stresses have only off-face offdiagonals, so their compressions remain positive diagonal matrices. For upper-phase and final-repair stresses use z_i=exp(sigma w_i^2). The normalization of an active edge gains only a fixed factor sqrt(m_a m_b), while each contributing child satisfies

\[
(w_a^2+w_b^2)/2-w_i^2>0.
\]

Increasing sigma makes the compressed stresses positive definite on the whole intended groups. This step is important: arbitrary scalar PSD stresses are not blindly copied and presumed PSD after changing diagonal sizes. The explicit convex-square scaling supplies positivity anew.

The maximal upper prefix and the lower forced-survival bound consequently give the same minimum number of steps. Every exposed scalar coordinate is replaced by its entire prescribed group, proving the rank-drop assertion. QED.

**Completion of Theorem B.** Apply Lemma 7.1 to a one-switch schedule of any requested depth between L and U. Pad the positive support to rank r. Then use the rank-preserving embedding of Section 6, which preserves the central curve and the greedy faces. The k=1 cases are fully observed singular targets or an unobserved source-to-null edge with all null diagonals observed. QED.

### A concrete consequence: full spectral orders do not identify facial depth

Take

\[
w=(0,3/11,6/11,7/11,9/11,1),
\]

with parents ((0,2),(1,4),(1,5),(3,5)). Exact arithmetic gives

\[
5\to4\to1\to0\quad\text{for the lower path},
\qquad
5\to4\to3\to1\to0\quad\text{for the upper path}.
\]

Thus L=3 and U=4. With rank one, simple null multiplicities, and alpha=3/22, Theorem B produces two order-six real PSD systems with identical full primal eigenvalue orders

\[
0,3/11,6/11,7/11,9/11,1
\]

and identical full dual orders 1-w_i, and the same sharp recovery exponent, but minimum facial degrees three and four. The same statement holds for the complex and quaternionic order-six cones. More generally, the exact ambiguity for every admissible spectral vector is the entire integer interval [L(w),U(w)], even after all multiplicities and alpha have been fixed.

This is stronger than a single counterexample and is not a scalar change of variables in the recovery theorem. It classifies a whole vector of primal and dual degeneration orders, provides arbitrary multiplicities, and identifies exactly what minimum facial depth that spectral information permits.

A different illustration of the strengthening is that the same scalar data (nu,d,alpha)=(3,2,1/4) permit either grades (1/2,1) with multiplicities (2,1), or grades (1/2,3/4,1) with multiplicities (1,1,1). Both grade systems are harmonic and have L=U=2. Thus the scalar tuple theorem alone cannot determine the central spectrum.

## 8. What compact strengthening should enter the paper?

Include Theorem B and the weighted one-switch profile from Lemma 7.1. They strengthen the same central story and need only one lifting lemma.

Do **not** claim a classification of all prescribed facial rank-drop profiles. The known impossible grade-aligned schedule in Milestone 125 remains a genuine obstruction. A full answer would require additional signed face-compression data and a separate analysis of which flags are realizable. That is a substantially different problem, not a missing detail of this paper.

Likewise, do not add a long catalogue of KL exponents. For convex residual objectives, established error-bound/KL equivalences [BNPS17] already transport many such statements. A short remark may be useful; it is not the substantial cross-disciplinary consequence sought here.

---

# Part IV. Adversarial novelty and significance audit

## 9. What the primary literature already does

**[S00] Sturm.** Establishes the classical singularity-degree error estimate with exponent 2^(-d). This is a guaranteed exponent, not an assertion that every individual problem has exactly that sharp exponent. Our theorem does not refute or replace that bound; it determines the full attainable spectrum and the exact rank needed for every permitted pair.

**[L21] Lourenço.** Develops amenable cones and facial residual functions, including error bounds on symmetric cones without constraint qualifications. Therefore extending *an error bound* from real SDP to symmetric cones is not new by itself. The distinguishing statement here is the exact equality of attainable spectra across simple cone types, with unchanged rank and exact realization of every permitted depth.

**[SWW21] Sremac–Woerdeman–Wolkowicz.** Studies the very same external maximum-determinant family, with a positive definite shift B (our normalization uses B=I). Section 4 obtains limiting ranks, rate bounds, and implications between slow spectral convergence and singularity degree. Theorems 4.4 and 4.7 and Corollary 4.8 are especially relevant. We must cite this as the closest optimization predecessor. The new conclusion is an exact joint primal/dual order-vector spectrum, arbitrary multiplicities, and a necessary-and-sufficient interval of attainable minimum degrees, with realizations at fixed rank.

**[BMN22] Basu–Mohammad-Nezhad.** Uses real algebraic geometry and Puiseux representations to bound the algebraic degree and worst-case convergence of SDP central paths. We do not claim Puiseux asymptotics or algebraicity as new, and the standard objective-barrier path there is not silently identified with our feasibility path. Our finite harmonic certificate gives sharper structural information for the explicitly specified family, not a blanket improvement of their algorithmic results.

**[BMN24] Basu–Mohammad-Nezhad.** Provides effective Łojasiewicz inequalities and error-bound applications. Rationality of exponents and finite semialgebraic classification mechanisms are insufficient novelty claims. The additional content here is the precise harmonic restriction, coupling with minimum facial depth, and dimension-preserving converse. It replaces general real-algebraic feasibility in this problem by a structural arithmetic realization theorem.

**[HSW22/23] Hu–Sotirov–Wolkowicz.** Proves preservation of singularity degree under symmetry reduction. Positive projections and rank-preserving reductions therefore have substantial precedent. Lemma 6.2 is presented with its proof and used to establish the cross-type theorem, not advertised as the invention of degree-preserving projection.

**[NLL26], submitted 10 August 2026.** Studies radial dependence of semidefinite error-bound constants and asymptotic tightness, including optimality systems. Our classification does not provide their explicit radial constants or supersede that analysis. Conversely, control of constants in a guaranteed bound is not the exact spectrum of sharp local exponents.

**[MST26], submitted 4 November 2026.** Studies common ramification of weighted AHO central paths and higher-order interior-point convergence under a predictor regularity condition. Our result does not classify their full Puiseux ramification, establish their predictor assumptions, or prove new iteration-complexity bounds. The manuscript must make this scope distinction explicit because the preprint is current and closely related in language.

## 10. The strongest defensible novelty statement

The examined primary sources do not give the following combined conclusion:

> At a fixed rank defect, all possible sharp affine-section error exponents and minimum facial degrees form one finite harmonic-arithmetic spectrum, the same for every irreducible symmetric cone of that rank; every admissible combination of central eigenvalue orders, multiplicities, exponent, and depth has a realization without increasing rank.

This is the statement to defend. Do not defend a weaker slogan such as "we give an explicit universal error bound." There are already important universal bounds and sophisticated algebraic algorithms.

The main mathematical mechanism is positivity forcing every internal central order to be a midpoint of two others, followed by the nontrivial one-switch construction controlling exact facial depth without losing rank. The Jordan extension shows that the mechanism is intrinsic to positive-cone rank, not the accidental number of scalar matrix entries. The full central-spectrum theorem exposes precisely the limits of spectral detection of degeneracy.

A skeptical referee may reasonably regard some Jordan manipulations as a natural extension once the PSD proof is known. That is a reason to integrate the argument into the paper's main necessity proof, rather than submit it as a separate extension or advertise it as a second unrelated breakthrough. The difficult one-switch real realization remains central.

No exhaustive priority claim is made. The cited audit covers the most directly related primary works found, including the 2026 developments. A specialist must still check the complete bibliography and the proofs before publication claims are finalized.

## 11. Communities and precise reasons for interest

**Convex and spectrahedral geometry:** an exact compatibility theorem between orders of tangency and facial degeneration, including realization and minimum rank, for arbitrary linear sections rather than generic or sparse ones.

**Real algebraic geometry and error-bound theory:** a concrete class where the sharp Łojasiewicz/error-exponent spectrum is determined structurally, not just bounded by polynomial format or obtainable in principle by elimination.

**Semidefinite and symmetric-cone optimization:** a complete answer for central eigenvalue-order data and their compatibility with minimum facial depth, including an exact description of the information that spectral orders fail to determine.

**Jordan/symmetric-cone geometry:** equality of these analytic-combinatorial spectra across simple cone types of the same rank, with an explicit explanation of why Peirce dimensions affect constants but not admissible orders.

These interests arise from one theorem and its spectral strengthening. They do not justify claims about all matrix-completion graphs, arbitrary spectrahedral shadows, non-symmetric cones, weak infeasibility, or every interior-point algorithm.

---

# Part V. The optimal single-paper architecture

## 12. Proposed title and abstract

### Title

**Sharp error exponents and facial depth in irreducible symmetric cones**

### Abstract

An affine space can meet a curved convex cone in a single point while small constraint errors permit much larger displacements. We classify the optimal Hölder error exponents jointly with the minimum facial-reduction degree for affine sections of irreducible symmetric cones at fixed cone rank and maximum feasible rank. The attainable spectrum is independent of the cone type: it is the same for real, complex, and quaternionic positive semidefinite cones, and for the Lorentz and exceptional cones at their respective ranks. The classification is a finite arithmetic one, expressed through harmonic midpoint weights and two facial-peeling recurrences. Every permitted integer depth between the recurrences is realized without increasing rank, by a construction that switches once between the two extremal peelings. A fixed graded maximum-determinant chart explains the arithmetic restrictions. We also classify the joint primal and dual eigenvalue orders of maximum-determinant regularization, with prescribed multiplicities, and determine exactly which minimum facial degrees are compatible with those spectral data. A feasible-direction reduction extends the results from isolated feasible points to general nonempty affine sections on bounded sets. The classification yields an exact arithmetic characterization of the minimum rank defect required for each exponent–depth pair.

This abstract makes no claim about general objective-barrier paths, full ramification, or arbitrary exposing profiles.

## 13. Draft introduction

An error bound compares two different notions of proximity. The residual of a system measures how nearly its equations and inequalities are satisfied, whereas the distance to its feasible set measures how nearly the system has actually been solved. For affine equations intersected with a polyhedral cone, these quantities admit a linear comparison. Curved cones behave differently. An affine space may touch the cone of positive semidefinite matrices in a unique matrix, yet feasible perturbations of much larger size may have very small measurement residual. The power relating these quantities is a local geometric invariant of the intersection.

A second invariant is discrete. When an affine section does not meet the interior of its ambient cone, facial reduction successively identifies smaller faces until strict feasibility holds relative to the final face. The smallest possible number of reductions is the singularity degree. It measures how many layers of degeneracy the linear equations conceal. The sharp error exponent and the singularity degree describe different aspects of the same intersection: one measures the order of tangency, and the other the depth of facial exposure.

The classical theory links these invariants through guaranteed error bounds. Sturm established the characteristic repeated-square-root estimate for linear matrix inequalities [S00], and the facial-residual-function framework extends such estimates to symmetric cones [L21]. These theorems do not identify every sharp exponent compatible with a given facial degree and cone rank. Nor do they decide the smallest rank in which a prescribed combination can occur. Those are realization questions as well as estimation questions.

This paper answers these questions for irreducible symmetric cones. At fixed rank defect, the attainable exponent–degree pairs are described by a finite system of harmonic midpoint equalities and two elementary integer recurrences. The description is both necessary and sufficient, and every permitted pair has a realization at the original rank. The spectrum is the same for all irreducible symmetric cones of a given rank. In particular, the real dimension of a matrix's offdiagonal entries does not alter the possible orders of instability. Rank, rather than ambient vector-space dimension, is the relevant size parameter.

The necessity proof identifies a fixed graded description of maximum-determinant regularization. Positivity bounds a cross block by the geometric mean of its diagonal scales. If an internal scale were not balanced by a genuine cross-grade midpoint, a positive kernel coefficient could be moved to a lower order and would contradict the maximal-determinant envelope. Every internal scale is therefore a harmonic midpoint. The original primal coefficients force lower bounds on facial reduction, while truncated dual coefficients construct upper bounds. These arguments apply to arbitrary real linear constraints and do not require a sparse kernel or a commuting family of matrices.

The converse is the main realization mechanism. The lower and upper recurrences need not agree, and scalar asymptotic weights do not determine a unique facial depth. Moreover, arbitrary intermediate exposing schedules can be obstructed by cancellations of ambient stress entries. We avoid that stronger and generally false realization problem. Schedules that follow the upper recurrence for a prefix and then switch once to the lower recurrence already attain every intermediate depth. A synchronized ownership of offdiagonal edges makes these schedules realizable without auxiliary null directions. This is what preserves the sharp minimum-rank information.

The same construction has a consequence for optimization that retains more information than a single error exponent. We classify the entire vector of primal and dual eigenvalue orders along maximum-determinant regularization, with arbitrary prescribed multiplicities, jointly with minimum facial degree. This concerns the external-type central paths studied by Sremac, Woerdeman, and Wolkowicz [SWW21]. For each admissible spectral vector we obtain the exact interval of possible minimum degrees. Thus even complete leading spectral orders can leave genuine ambiguity about facial degeneracy. The result is a classification of asymptotic geometry, not a statement about the iteration complexity of an unspecified algorithm.

Our use of algebraic curves and barrier geometry is compatible with, but different from, algebraic-degree and convergence analyses of central paths [BMN22]. The contribution is not the existence of Puiseux expansions or rational error exponents. It is the exact structural spectrum, its rank-preserving realization, and its independence of the irreducible cone type. The positive-retraction argument needed for the latter is stated with full control of facial degree; mere preservation of feasible points would not be sufficient.

We first remove free feasible directions, reducing the error exponent of a general affine section to an isolated intersection while preserving every facial chain. We then establish the graded central chart, derive the harmonic and facial restrictions, and prove the one-switch realization. A multiplicity lift and a rank-preserving real-symmetric subalgebra complete the general theorem. The final section gives the central-spectrum classification, the minimum-rank characterization, and examples marking the limits of the result. We do not classify every exposing rank profile or every interior-point central path.

## 14. Economical theorem and proof order

1. **Introduction and two main theorems.** State the geometric rank-universal classification and the central-spectrum theorem. Define the arithmetic certificate once. Include one small non-dyadic example and one spectral ambiguity example, not the historical tables.
2. **Affine sections and the central chart.** Give the gauge reduction, the maximum-determinant envelope, and the finite coefficient-rescaling lemma. Prove the chart directly in Jordan notation. This replaces, rather than duplicates, a separate real-matrix necessity argument.
3. **Arithmetic necessity and facial bounds.** Prove harmonicity, the weighted-support formula for the exponent, and the primal/dual peeling sandwich. These are one continuous argument.
4. **The one-switch realization.** Work in real symmetric matrices. Include only the path-length lemma, the common blocking endpoint, edge ownership, release synchronization, the all-competitor bound, actual ambient stresses, and the final leading-edge repair. Exact minimum depth must be proved here, not deferred to a numerical appendix.
5. **Multiplicity and cone-type transfer.** Prove the two compact lifting lemmas. Deduce both main theorems and the exact minimum-rank-defect formula.
6. **Consequences and limitations.** Give the complete primal/dual spectral interpretation, the dimension-unrestricted projection of the spectrum, and the sharp limitations on type independence, rank profiles, and central-path scope.

Move small-nullity catalogues, failed routes, and historical milestones to the research repository. Retain a short reproducibility appendix only if it helps verify explicit examples. The paper's proof must not depend on finite enumerations or a numerical solver.

The central narrative should fit one substantial article. There is no reason to attach separate chapters on matrix completion, stochastic games, KL calculus, and algorithmic complexity merely to increase the number of applications.

## 15. Journal recommendation and publication decision

**Transactions AMS is the best first fit.** Its stated criteria include a correct, new, significant contribution of interest to a substantial number of mathematicians, and it explicitly discourages piecemeal variations. The proposed paper is a complete structural classification with substantial proofs, rather than a partial step or a minor application. This is a fit assessment, not an acceptance prediction.

**JLMS is a strong alternative.** Its current submission page explicitly treats a broad, motivating introduction as an acceptance criterion. It currently specifies a minimum of 18 pages and no maximum; do not use obsolete short-paper assumptions to remove necessary proofs. Its current policy also requires an AI Declaration identifying the tools/models actually used and explaining their contributions. The authors must reconstruct this accurately from the research record, not invent model/version details.

**Advances in Mathematics is a defensible ambitious option only after independent specialist review confirms the core proofs and assesses their novelty.** The rank-universal theorem improves that case, but a larger catalogue of routine applications would not establish the required importance. Editorial judgment cannot be inferred from the number of milestones, universal quantifiers, or the amount of computation used.

**Decision:** include the rank-universal theorem and the complete central-spectrum consequence; then stop expanding the research program for this paper. They increase mathematical breadth by explaining the existing classification, not by adding unrelated material. Further delay for every possible facial rank profile is not justified. The next substantive investment should be a hostile mathematical review of the one-switch construction and the Jordan/multiplicity lifts, followed by one clean manuscript.

---

# Part VI. Primary-source references and provenance

The literature and journal-policy check was performed on 12 November 2026. Preprints are identified as preprints. The attached BibTeX file contains persistent identifiers.

[FK94] J. Faraut and A. Korányi, *Analysis on Symmetric Cones*, Oxford Mathematical Monographs, Oxford University Press, 1994. DOI: 10.1093/oso/9780198534778.001.0001. Standard spectral, Peirce, quadratic-representation, and classification inputs.

[S00] J. F. Sturm, *Error Bounds for Linear Matrix Inequalities*, SIAM Journal on Optimization 10 (2000), 1228–1248. DOI: 10.1137/S1052623498338606.

[L21] B. F. Lourenço, *Amenable cones: error bounds without constraint qualifications*, Mathematical Programming 186 (2021), 1–48. DOI: 10.1007/s10107-019-01439-3. Preprint arXiv:1712.06221.

[SWW21] S. Sremac, H. J. Woerdeman, and H. Wolkowicz, *Error Bounds and Singularity Degree in Semidefinite Programming*, SIAM Journal on Optimization 31 (2021), 812–836. DOI: 10.1137/19M1289327. Preprint arXiv:1908.04357. Relevant locations: Section 4, equation (4.1), Theorems 4.4 and 4.7, and Corollary 4.8.

[BMN22] S. Basu and A. Mohammad-Nezhad, *On the central path of semidefinite optimization: Degree and worst-case convergence rate*, SIAM Journal on Applied Algebra and Geometry 6 (2022), 299–318. DOI: 10.1137/21M1419933. Preprint arXiv:2105.06630.

[BMN24] S. Basu and A. Mohammad-Nezhad, *Improved effective Łojasiewicz inequality and applications*, Forum of Mathematics, Sigma 12 (2024), e115. DOI: 10.1017/fms.2024.66. Published online 3 December 2024. Preprint arXiv:2211.10034.

[HSW22/23] H. Hu, R. Sotirov, and H. Wolkowicz, *Facial Reduction for Symmetry Reduced Semidefinite and Doubly Nonnegative Programs*. Primary version examined: arXiv:1912.10245v3, 3 February 2022. Published article DOI: 10.1007/s10107-022-01890-9. Relevant location: Section 3.4, preservation of singularity degree under symmetry reduction.

[BNPS17] J. Bolte, T. P. Nguyen, J. Peypouquet, and B. Suter, *From error bounds to the complexity of first-order descent methods for convex functions*, Mathematical Programming 165 (2017), 471–507. DOI: 10.1007/s10107-016-1091-6. Preprint arXiv:1510.08234.

[NLL26] M. Nishijima, G. Li, and B. F. Lourenço, *Radial-type error bounds for semidefinite feasibility problems without strict feasibility: qualitative estimates and asymptotic tightness*, arXiv:2608.09013, submitted 10 August 2026. Preprint.

[MST26] A. Mohammad-Nezhad, P. Sampourmahani, and T. Terlaky, *Ramification of Weighted Central Paths and Super-linear Interior-Point Methods for Semi-definite Optimization*, arXiv:2611.07080v1, submitted 4 November 2026. Preprint.

[AMS26] American Mathematical Society, *Transactions of the American Mathematical Society: Aims and Scope / Submission*, official journal information, accessed 12 November 2026.

[LMS26] London Mathematical Society, *Submit to the Journal of the London Mathematical Society*, official submission page, accessed 12 November 2026. Especially Scope, Article length, and AI declaration.

[ADV26] Elsevier, *Advances in Mathematics: Description*, official journal page, accessed 12 November 2026.

### Internal dependencies and what is genuinely added here

- Milestone 13 already provides the symmetric-cone Dikin modulus comparison. Section 5 restates its argument rather than claiming it as new.
- Milestone 15 already supplies the bounded real-PSD feasible-direction gauge. Section 2 extends the proof to Jordan cones and bounded test regions for possibly unbounded feasible sections.
- Milestone 128 supplies the scalar real-PSD one-switch construction and its exact minimum-nullity theorem. It is assumed established as requested by the research assignment.
- The added mathematical content is the fixed graded Jordan chart and harmonic/peeling necessity, the rank-preserving cross-type realization with exact facial-depth control, and the prescribed-multiplicity central-spectrum theorem.
- The new research file is not a second-paper proposal. It is a consolidation and strengthening packet for the same paper.
