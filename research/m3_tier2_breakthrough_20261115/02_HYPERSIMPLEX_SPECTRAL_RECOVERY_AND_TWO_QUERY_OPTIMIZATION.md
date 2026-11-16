# Checkpoint 02 — conjugate-rank observability and two-query optimization

Date 2026-11-15. This is a new recovery/optimization theorem for a broad algebraically specified subclass in the ORIGINAL rational scalar value/coordinate-gradient oracle, without a noise budget, a radius charge, or a full projected-matrix reply. It removes the exceptional subset-sum coefficient cases left in grand-arithmetic checkpoint 07. The full all-pencil minimax problem is still not declared solved.

## 1. The theorem and the new observable invariants

Fix m>=2,d>=1. Let X(x)=X0+sum_i x_i Hi be a rational symmetric affine pencil with Frobenius-orthonormal rational directions. Suppose its affine image is genuinely weakly infeasible. Put

    f(x)=dist_F(X(x),S_+^m)^2/2,
    R_X(z,x)=det(zI-X(x)^2), tau_X(x)=tr(X(x)^2).

Work over F=Q(x_1,...,x_d). Choose the universal algebraic germ probe q in Section 2 below. At q the natural objective is analytic. Put h=2f as an algebraic analytic germ, let P_h(w) be its monic minimal polynomial over F, let H be its set of distinct F-Galois conjugates, and put

    M=deg P_h=|H|,
    r_obs=dim_Q span_Q H.                             (1)

The Q-linear span here is a span of ALGEBRAIC FUNCTIONS, not the one-dimensional real span of their numerical values at q. Its realification is used later to form an abstract polytope. This distinction is essential.

THEOREM A (maximal observation class). Suppose r_obs=m. Then R_X is irreducible over F with distinct nonzero roots. The local negative inertia k is recoverable from P_h by

    k=(m/M)[x_1^2] Tr(P_h),                           (2)

where Tr(P_h) is minus its next-to-leading coefficient. Here 1<=k<=m-1. If additionally

    M=binom(m,k),                                    (3)

then among ALL rational isometric weakly infeasible pencils of the same format giving the same first scalar observation f(q):

(a) if m!=2k, there is exactly ONE possible global natural objective;
(b) if m=2k, there are at most TWO possible global natural objectives. The only possible alternative squared spectrum is

    { tau_X/k-mu_i : 1<=i<=m },                       (4)

where the mu_i are the roots of R_X. An alternative need not be realizable by a real affine pencil; (b) is an upper bound, not an existence assertion.

Consequently, every instance satisfying (1) with r_obs=m and (3) can be optimized to ANY positive tolerance using at most TWO exact natural SCALAR value queries, with no coefficient-height bound. When m!=2k, ONE query suffices. The second query in the balanced case can simply test an approximate optimizer of the first matching rational candidate. The algorithm and its proof are in Section 7.

COROLLARY B. The hypotheses hold whenever R_X has Galois group S_m over F. They also hold when it has group A_m for m>=4. Hence at most TWO original scalar queries suffice on either of these classes, for arbitrary matrix order and dimension. A common mixed-inertia ball does not need to be supplied: weak infeasibility itself guarantees mixed inertia at every nonsingular point.

These results are not the earlier two-query FULL-PROJECTION theorem. Only f(q) is observed; the entire projected matrix and the unknown Hi remain unavailable. Nor are they confined to index-one pencils.

## 2. A single finite algebraic observation supplies an analytic germ

We reproduce the needed fixed-format probe fact rather than presume that the oracle supplies derivatives or formal germs. For every fixed m,d there is a computable B(m,d) such that in any rational open ball one can explicitly choose q with

    f_X(q)=f_Y(q) iff f_X and f_Y agree on a neighborhood of q

for ALL pairs of rational pencils of this format. Each pencil has locally constant maximal rank at q, so its natural objective is analytic there.

Proof. Express PSD projection by symmetric unknown matrices U,V satisfying U>=0,V>=0,UV=0 and X=U-V. These polynomial conditions uniquely give U=X_+ and V=(-X)_+. Thus equality of two natural losses is a fixed-format first-order real-algebraic formula in x and the two rational coefficient lists, using tr(V^2)/2. Apply effective quantifier elimination ONCE to this symbolic formula, retaining the coefficient entries and x as free variables. The resulting finite list of polynomial degrees has a bound B depending only on m,d. Increase B to at least m and, if desired, the degrees of the relevant characteristic discriminants. Rational specialization leaves either identically zero polynomials or nonzero rational polynomials in x of degree <=B.

Put L=B+1, N=L^d, alpha=2^(1/N), and v_j=alpha^(L^(j-1)). Distinct monomials of total degree <=B give distinct powers of alpha of degree below N. Eisenstein at 2 therefore prevents every nonzero such rational polynomial from vanishing at v. Rational translation and scaling place q in the specified ball with the same nonvanishing property. Every sign in the specialized quantifier-free equality formula is locally constant near q. Equality at q consequently implies equality throughout a neighborhood, and conversely. Every maximal nonzero minor of a rational pencil has degree <=m; at least one remains nonzero at q, proving constant maximal rank locally. The separated negative spectral projector is analytic there, and f=tr(X^2 P_-)/2 is analytic, even with persistent zero eigenvalues. QED.

All computation and algebraic query degrees may be enormous. They are free under the question's exact information model, and no polynomial bit-runtime assertion is made. This is the same foundational probe mechanism of grand-arithmetic checkpoint 02.

## 3. Weak infeasibility forbids both kinds of definite point

LEMMA 1. If a real affine subspace U is disjoint from S_+^m at zero distance, there exists nonzero Z>=0 such that tr(ZX)=0 for every X in U. In particular U contains neither a positive definite nor a negative definite matrix.

PROOF. Separate U from the nonempty open cone int S_+^m. A nonzero separating normal can be chosen Z>=0; unboundedness of the affine direction space makes it orthogonal to that space. The constant c=tr(ZX0) is <=0, since the infimum of tr(ZS) over positive definite S is zero. For affine points X_j at distance tending to zero from the PSD cone, write S_j>=0 with ||X_j-S_j||->0. Then c=tr(ZX_j)>=-||Z||_F||X_j-S_j||_F, so c>=0. Therefore c=0. A positive or negative definite X has strictly positive or negative inner product with nonzero PSD Z, respectively. QED.

Thus a nonsingular point in U has 1<=k<=m-1 negative eigenvalues. This is why a prescribed index-one neighborhood is no longer needed for the present theorem.

## 4. Maximal conjugate rank forces spectral irreducibility, even for competing pencils

Let mu_1,...,mu_s be the DISTINCT squared eigenvalues of a competing pencil, in a splitting field of its characteristic polynomial. Every conjugate of h is an integer linear combination of these mu_i, with coefficients given by how many negative eigenvalues of each squared magnitude were selected. Hence r_obs<=s<=m.

If r_obs=m, necessarily s=m: every squared eigenvalue is distinct, no zero root can occur, and each coefficient is zero or one. Let the Galois action on the m squared roots have t orbits O_1,...,O_t (the irreducible factors of R). The selected subset has a fixed cardinality k_j inside O_j under every conjugation. Its incidence vectors all lie in

    {v in Q^m : sum_(i in O_j) v_i = a k_j for all j,
                 for some a in Q}.

This subspace has dimension at most m-t+1: one free total scaling a plus the zero-sum subspaces on each orbit; if some k_j=0 the dimension can only decrease. The linear map v -> sum_i v_i mu_i cannot increase dimension. Therefore

    r_obs <= m-t+1.                                  (5)

When r_obs=m, this forces t=1, so R is irreducible. Also the mu_i are Q-linearly independent, because they span an at-most-m-dimensional space containing the m-dimensional span of H.

This applies to EVERY same-observation competing pencil: Section 2 gives the same h germ, hence the same minimal polynomial and conjugate rank. The competitors do NOT need a Galois-group promise in advance.

Average h over the Galois group. Transitivity on the m squared roots makes each root occur with frequency k/m. Distinct conjugates of h have equal multiplicity in this group average. Thus

    Tr(P_h)/M = (k/m)tau_X.                           (6)

Isometry gives tau_X(x)=||x||^2+2b.x+c, proving (2). Lemma 1 gives the mixed-inertia range. Equal first observations have equal k and equal tau_X. This recovers arithmetic inertia without assuming a full symmetric group.

If (3) holds, there are binom(m,k) distinct conjugates, while there are only that many k-subsets. Therefore H is EXACTLY the collection of ALL k-subset sums of the m Q-independent squared roots. The same statement holds for every competing pencil.

## 5. Subset-sum reconstruction without the Moser-coefficient exclusions

LEMMA 2 (independent subset-sum rigidity). Let u_1,...,u_m be Q-linearly independent elements of a characteristic-zero field. Let v_1,...,v_m be another Q-independent list with the SAME set of all k-subset sums, 1<=k<m. Then the lists agree up to permutation, except that for m=2k one may instead have

    v_i = (sum_j u_j)/k - u_(pi(i)).                 (7)

PROOF. The k-subset sums span exactly span_Q{u_i}: differences of two sums replacing just i by j give u_i-u_j, and the sum of all subset sums is binom(m-1,k-1)sum_i u_i. Combining differences and this total recovers every u_i. The same holds for the v_i, so both lists are bases of the same Q-vector space.

Use the u_i as the abstract coordinate basis, and extend scalars to R. The convex hull of the k-subset sums is the hypersimplex

    Delta(m,k)={z in [0,1]^m: sum_i z_i=k}.

The basis change u_i -> v_i is an invertible linear transformation preserving its vertex set and hence its face lattice. This is a convex hull in the REALIFICATION OF A Q-VECTOR SPACE OF FUNCTIONS, NOT the numerical real line of eigenvalue evaluations.

For k=1 the vertices are the basis vectors, so the transformation is a permutation. For k=m-1 recover by complements, or use the same simplex argument. For 2<=k<=m-2, the facets are precisely z_i=0 and z_i=1. They contain respectively binom(m-1,k) and binom(m-1,k-1) vertices. If m!=2k these two numbers differ, so each facet family is preserved. The induced permutation of the zero-coordinate facets determines every vertex; it is a coordinate permutation.

If m=2k, the two facets z_i=0 and z_i=1 are the unique disjoint pair involving either one: every pair with distinct coordinate indices has a common vertex. Thus a face automorphism permutes the m complementary facet pairs and may swap their orientations. After undoing the permutation, it sends vertex coordinate z_i to either z_i or 1-z_i. If S is the set of swapped coordinates, preservation of sum z_i=k requires

    sum_(i in S) z_i = |S|/2

for every k-subset indicator. For a nonempty proper S, choose i in S,j not in S and two k-subsets differing only by replacing i by j; the displayed sum changes, a contradiction. Hence S is empty or all coordinates. The latter is complementation. On the hyperplane sum z_i=k, its linear extension is z -> (sum z_i)/k *1-z, giving (7). QED.

The hypersimplex automorphism fact is classical (equivalently, the symmetry of Johnson graphs); it has been proved here to make the reconstruction self-contained. The new use is in the arithmetic conic observation theorem. This proof does NOT require any nonvanishing of the classical power-sum/Moser coefficients. For example m=8,k=2 is recovered despite the failure of that earlier sufficient coefficient test. The usual ambiguous finite multisets need not be Q-linearly independent as algebraic FUNCTIONS and do not contradict Lemma 2.

## 6. From the squared spectrum to at most two global natural objectives

Apply Lemma 2 to the squared eigenvalues of any two same-observation pencils. If m!=2k, the squared characteristic polynomial R is identical. If m=2k, it is either identical or the reflected polynomial with roots tau_X/k-mu_i.

For each one of those squared spectra, the observed function h singles out exactly one k-subset of its squared roots: all subset sums are distinct by Q-independence. On a small real regular neighborhood, take the positive square root of every mu_i; the selected k receive negative signs and all remaining roots positive signs. This uniquely determines the ordinary signed characteristic polynomial p_X(lambda,x) on that neighborhood. Its coefficients are rational polynomials in x, so equality on an open set implies global polynomial equality. The negative-square energy of that signed polynomial determines f globally.

There is therefore ONE global natural objective in the unbalanced case and at most TWO in the balanced case, as asserted. We do not claim unique coefficient matrices: globally isospectral pencils need not have the same matrix entries. Nor do we claim that the balanced reflected candidate always has a real affine symmetric realization.

## 7. A two-query optimizer without a coefficient-height cap

The algorithm is uniform for fixed known m,d, and it optimizes every instance satisfying r_obs=m and (3). For an effective finite-catalogue version, the same operations are simply finite searches.

1. Query f(q) at the universal algebraic point of Section 2. Enumerate rational affine pencils of the fixed format, filtering isometry and genuine weak infeasibility by real quantifier elimination, and evaluate their algebraic f(q) exactly. Stop at the first match, f_1. The true pencil occurs at a finite index, so this search terminates. Equal values give equal germs. Under the theorem's hypothesis the entire matching class has at most two distinct global objectives.
2. Offline enumerate rational points until finding u_1 with f_1(u_1)<epsilon. This terminates by continuity and inf f_1=0. If the unbalanced case has been determined, return u_1 after just the first query.
3. In the balanced case (or without testing the imbalance), make the SECOND query at u_1. If the returned true f(u_1)<=epsilon, return u_1. Otherwise enumerate rational candidate pencils matching BOTH replies, and stop at the first match f_2. No matching candidate has the global objective f_1, because f_1(u_1)<epsilon while the second reply is larger. Since there was at most one alternative, every matching candidate has the TRUE global objective. Find a rational u_2 with f_2(u_2)<epsilon offline and return it without another query.

This is an effective terminating procedure in the permitted exact-real equality model, not a polynomial-time algorithm. It does not have to decide whether a second candidate exists: it searches for one only after the second reply proves that the first objective was incorrect and a second exists. The output can be unqueried, exactly as allowed in the target problem. Nonattainment is not a difficulty because only a positive tolerance is required.

For a KNOWN FINITE catalogue, two scalar queries also identify the entire global objective: after the first response at most two objective classes remain, and a second rational point where their values differ can be found offline. For the unbounded countable class, the theorem above claims the effective TWO-QUERY OPTIMIZATION statement, not an algorithm which detects in finite time that no second spectral class exists.

## 8. Why S_m and A_m satisfy the hypotheses

If R has group S_m, a rational linear relation sum_i c_i mu_i=0 can be acted on by a transposition (ij). Subtraction gives (c_i-c_j)(mu_i-mu_j)=0. Distinct roots force all c_i equal, and tau_X!=0 forces that common coefficient to be zero. Thus the mu_i are Q-independent. The group is transitive on every k-subset, so P_h has all binom(m,k) subset sums as its distinct roots. Those sums span the m-dimensional root space. Therefore r_obs=m and (3) hold.

For A_m, m>=4, the group is two-transitive and transitive on every k-subset. Its real standard representation {sum z_i=0} is irreducible: the orthogonal projection onto any invariant subspace commutes with the group, so two-transitivity makes its diagonal entries constant and its off-diagonal entries constant. On the standard space it is a scalar idempotent, hence zero or identity. The kernel of the Q-linear map e_i -> mu_i is invariant. Group averaging and tau_X!=0 place it inside the standard space; if it were nonzero, realification and this irreducibility would force all differences mu_i-mu_j to vanish. Hence the kernel is zero. The same subset-sum argument proves the hypotheses.

This is a statement over Q(x), not the Galois group of a numerical specialization. Irreducibility of a matrix algebra or an interaction graph is not being substituted for the spectral Galois condition.

## 9. Necessary concentration of any prospective Tier II hard prior

For a known finite rational prior of the target fixed format, define the GOOD observable class by r_obs=m and M=binom(m,k), with k given by (2). The first germ observation determines whether its entire equality class is GOOD. The optimizer above succeeds with certainty on every GOOD member using at most two scalar queries; on other answers it may use any fallback.

Therefore a fixed prior that forces EVERY T-query algorithm (T>=2) to fail with probability at least 2/3 at any positive target tolerance must assign probability at least 2/3 to the EXCEPTIONAL class

    r_obs<m OR (r_obs=m and M<binom(m,k)).             (8)

In particular a prior supported entirely on full S_m or A_m squared spectral groups CANNOT provide the requested c/T exact-rational lower bound. This excludes generic full-group spectral families in the ORIGINAL oracle, not just rationalized quadratics or the stronger projection oracle.

The all-pencil problem is not closed: reducible spectra, repeated squared eigenvalues, and incomplete subset orbits can fall in (8). The previously proved logarithmic rational hard family does fall there. These exceptions do not automatically imply hardness: rational quadratic losses are also rank-deficient in this observation sense and are one-query recoverable by a different mechanism. No universal complexity law for the entire exceptional class is proved here.

## 10. Relation to previous checkpoints

Grand-arithmetic checkpoint 07 obtained index-one/index-(m-1) recovery and a nonvanishing Moser-coefficient sufficient criterion for other inertias. The current proof removes those numerical coefficient exclusions using Q-linear independence plus hypersimplex geometry, makes the mixed-inertia premise automatic for nonsingular weakly infeasible pencils, obtains an at-most-two GLOBAL-objective bound against unpromised competing pencils of the same rational format, and gives an actual two-query optimizer without a height cap.

Source ingredients (quantifier elimination, the algebraic germ probe, Galois transitivity, hypersimplex symmetries) are classical or previously established in this project. The proof of the stated conic synthesis and hard-prior consequence is supplied in full above. No journal claim or full Tier II completion is made.
