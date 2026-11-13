# Milestone 15 — escape as an unrestricted lift lower bound; optimal PSD and SOC representations

Date: 2026-11-13. This converts the weak-infeasibility and nonattainment machinery into an EXTENSION-COMPLEXITY theorem. It gives exact optimal representations of an infinite family of planar convex sets and three-dimensional power cones. The lower bounds allow arbitrary real coefficients, arbitrary auxiliary variables and affine couplings, and arbitrarily many linear inequalities. They are not lower bounds only for the two-basis construction, positive encoders, or mediated-graph formulations.

The resource counted must be stated precisely. A single PSD matrix of order d has resource d-1. A Lorentz cone of any dimension at least three has resource one. Polyhedral constraints have resource zero. The theorem proves a universal escape bound in terms of the sum of these resources. It then proves that the bound is attained and forces optimal representation sizes for the power-cone family below.

## 1. Definitions and principal result

For an integer k>=1 put q=2^k and define

    P_k={(x,t,z) in R^3 : x>=0, t>=0, x^(q-1) t >= |z|^q},
    S_k={(x,t) in R^2 : x>0, t>=x^(-(q-1))}.           (1)

The plane z=1 cuts P_k in S_k. Both sets are closed and convex; the construction in Section 6 proves convexity without needing a separate weighted-mean argument. They contain no affine line.

A PSD lift of order d means

    S=pi(L intersect S_+^d),                           (2)

where L is an arbitrary affine subspace and pi is an arbitrary affine map. We also allow products of PSD cones, Lorentz cones, and nonnegative scalar cones. Linear equalities are free, and scalar cones represent arbitrary additional linear inequalities. No positivity of pi, linear positive section, uniqueness of lifted witnesses, coefficient bound, or strict feasibility is assumed.

For a product lift with PSD orders d_1,...,d_s and h nonpolyhedral Lorentz factors, define its curvature resource by

    b=sum_j(d_j-1)+h.                                 (3)

Zero-dimensional factors are omitted; scalar PSD cones contribute zero. A Lorentz cone of dimension two is polyhedral and is counted as two scalar factors, not as a nonpolyhedral factor. Both real symmetric and complex Hermitian PSD factors are permitted, with the SAME matrix-order resource.

**Theorem A (exact optimal resources).** For every k>=1:

(a) The minimum order of a SINGLE real symmetric PSD lift of P_k or S_k is exactly k+1. The same minimum holds for complex Hermitian PSD lifts.

(b) The minimum number of Lorentz-cone factors in ANY SOC lift of P_k or S_k is exactly k. Their dimensions can be arbitrary, and arbitrary extra linear inequalities and free variables are allowed.

(c) More generally, every mixed PSD/SOC/polyhedral lift has curvature resource b>=k. This is sharp: one PSD block of order k+1, or k three-dimensional rotated Lorentz factors, attains it.

(d) The upper representations use rational coefficients. The single-PSD formulation has at most k-1 homogeneous copy equalities and uses a coordinate projection. Every point of P_k has a positive witness of rank at most two; there is no rank restriction on the full feasible fibre.

Thus the representation order is exactly known for an infinite family in FIXED target dimension. This does not classify all rational-weight power cones or all planar spectrahedral shadows.

IMPORTANT: Single-matrix order and total resources are different from the semidefinite EXTENSION DEGREE, which allows arbitrarily many PSD blocks and minimizes only their largest order. The sets in (1) have extension degree two, consistent with (b). There is no assertion that a planar convex semialgebraic set requires a large maximum block order.

## 2. A product-cone escape theorem

Consider

    K = product_j S_+^(d_j) times product_l L_(n_l) times R_+^u,

where L_n={(a,v):a>=||v||_2}, n>=3. The matrix factors can be real symmetric or complex Hermitian. Use a positive size gauge

    tau(X)=sum_j tr(X_j)+sum_l a_l+sum_i s_i.

It is strictly positive on nonzero cone points and bounds their Euclidean norm up to fixed constants. Let A be any real linear map on this product space. Suppose A(X)=c is weakly infeasible. Let b be (3).

**Theorem B.** Necessarily b>=1. There is an instance-dependent C>0 such that

    min{tau(X):X in K,||A(X)-c||<=delta}
           <= C delta^(-(2^b-1))                      (4)

for all sufficiently small delta>0. More sharply, b can be replaced by the number of partial, nonlinear reductions in the decomposition constructed below. Arbitrarily many polyhedral factors do not increase that number.

The proof is a product-cone version of the explicit Schur recurrence in milestone 12, supplied here to justify the stronger resource count rather than using the total order of a block-diagonal PSD embedding.

### 2.1 Cone compression and the nonlinear budget

Let L=ker A. Choose Z_base with A(Z_base)=c. An approximately feasible sequence in K can be corrected by a fixed linear right inverse of A into Z_base+L with distance to K tending to zero.

Start with the full product cone. At any stage, if the compression of L contains a nonzero cone point, choose one and lift it to H_i in L. For each factor of that compressed cone do the following.

* PSD factor: diagonalize the PSD component by an orthogonal or unitary change of coordinates. Remove its positive support and retain the compression to its kernel. If both removed and retained dimensions are nonzero, call that a partial reduction in this factor.
* Full Lorentz factor: an interior component removes the whole factor. A nonzero boundary component can, by a spatial orthogonal rotation, be written in coordinates (alpha,w,beta) with alpha>0,w=0,beta=0, where the cone is alpha>=0,beta>=0,alpha beta>=||w||^2. Retain only beta, a nonnegative scalar factor. This is one partial reduction. A zero component leaves the factor unchanged.
* Scalar factor: a positive component removes it; a zero component leaves it unchanged.

These maps send cone points into the remaining product cone. Each H_i has zero compression after its removed support is discarded. At least one positive rank is removed at each step, so the procedure terminates. The final compressed L has no nonzero point in the final cone.

A step is nonlinear if it includes at least one partial reduction. A PSD factor of original order d_j can undergo at most d_j-1 partial reductions: each removes a positive dimension while leaving at least one dimension. A Lorentz factor can undergo at most one, after which only a scalar remains. Hence the number h of nonlinear steps satisfies

    h<=sum_j(d_j-1)+number of Lorentz factors=b.         (5)

This is the essential reason why adding linear inequalities cannot increase the escape exponent.

### 2.2 The terminal affine problem is feasible

Project the corrected affine approximate sequence to the terminal product space. If the projected sequence were unbounded, normalize it and pass to a subsequence. Its limit would be a nonzero cone point in the terminal compressed L, contradicting termination. Thus it has a bounded subsequence and a terminal cone-feasible limit. Lift this limit to Z0 in Z_base+L.

The terminal product space is nonzero. Otherwise reverse addition of sufficiently large positive multiples of H_i would make Z0 cone feasible exactly. To see this, a fully removed factor is dominated by its positive interior component; a partially removed PSD block is made positive using the Schur complement against an already positive retained block; and a partially removed Lorentz factor is made positive by increasing alpha against an already positive beta. This would contradict weak infeasibility.

### 2.3 A quantitative Laurent path

Let the decomposition have n steps. Choose an interior reference vector e whose compression is the usual identity in each PSD factor, (alpha,beta,w)=(1,1,0) in each Lorentz factor and 1 in each scalar factor. Spatial rotations preserve this reference; coordinate scaling only changes fixed constants.

Define exponents backwards by

    e_(n+1)=0,
    e_i=2e_(i+1)+1 if step i is nonlinear,
    e_i=e_(i+1) otherwise.                             (6)

Then e_1=2^h-1. We construct positive constants C_i such that

    X(epsilon)=Z0+2 epsilon e+
                  sum_i C_i epsilon^(-e_i) H_i         (7)

belongs to K for all sufficiently small positive epsilon.

Here are explicit domination rules establishing this assertion. Let beta_i=1+i/(n+1). In descending order choose M_i>0 bounding every relevant coordinate/operator norm of Z0+sum_(j>i) C_j epsilon^(-e_j)H_j by M_i epsilon^(-e_(i+1)), for 0<epsilon<=1. Such an M_i is obtained by summing fixed norms. Let gamma_i>0 be the minimum, over components removed at that step, of the positive-support smallest PSD eigenvalue, the positive alpha component of a boundary Lorentz direction, the cone-interior domination margin of a fully removed Lorentz component, or the positive scalar coefficient. Increase M_i if necessary to account for the fixed Euclidean-to-cone-order bounds.

If step i is linear, choose C_i gamma_i>=M_i. Every newly restored factor has no retained coordinates in that factor, so this makes it positive without any inverse small gap.

If step i is nonlinear, choose

    C_i gamma_i>=M_i+(n+1)M_i^2.                       (8)

Inductively assume that the block/factor starting at stage i+1 dominates beta_(i+1)epsilon times its reference vector. Subtract beta_i epsilon times the stage-i reference vector. For a partial PSD factor the retained block has gap at least epsilon/(n+1). Its Schur term is bounded by

    (n+1)M_i^2 epsilon^(-(2e_(i+1)+1)),

and (8) dominates this and the possible negative top block. For a partial Lorentz factor, the retained beta coordinate is at least epsilon/(n+1); exactly the same estimate dominates ||w||^2/beta and a possibly negative alpha coordinate. Fully removed factors need only the first term in (8). Unchanged factors retain their larger margin. This proves the reverse induction.

Thus X(epsilon) is cone feasible, and its size is O(epsilon^(-(2^h-1))). Since H_i belongs ker A,

    A(X(epsilon))-c=2 epsilon A(e).                   (9)

A(e) cannot vanish: otherwise adding a sufficiently large multiple of the interior vector e to any exact affine solution would make it cone feasible. Taking epsilon proportional to delta proves (4). If h=0 the path would be bounded and yield exact feasibility by a limit, so weak infeasibility forces h>=1. QED.

The proof works in real or complex PSD factors because it uses only unitary diagonalization, positive-support compression and the Hermitian Schur inequality. It does not invoke any classification of positive maps.

## 3. The same resource bound for exact feasible near-optimization

Let F=K intersect {A(X)=c} be nonempty, and let a real affine objective l have finite but unattained infimum v. Then there are exactly feasible eta-optimal points of size

    O(eta^(-(2^b-1))).                                (10)

This statement uses the ORIGINAL resource b; it can be improved by replacing each cone factor with the minimum face of its feasible support.

**Proof.** The minimum face of F is a product of smaller PSD cones, full Lorentz factors, scalar rays, and zero factors. Removing zero factors gives another product cone with resource no larger than b. There is X0 in F interior relative to that face, by averaging finitely many feasible points spanning its minimal face. In its linear span use coordinates that identify the face with that product cone, and choose an interior reference e.

Augment A with the linear part of l and target the value v. The augmented system is weakly infeasible: near-optimal feasible points approach the target, but an exact point would attain v. Theorem B supplies PSD/product-cone points Y with augmented residual delta and size O(delta^(-(2^b-1))).

Correct the original source equalities with a fixed linear right inverse: Z=Y+T(c-A(Y)). The correction has norm O(delta), so Z>=_K -c1 delta e. Choose gamma>0 with X0>=_K gamma e, and mix

    Zplus=(1-s)Z+s X0,
    s=c1 delta/(gamma+c1 delta).

Then Zplus belongs F exactly. Its objective gap is O(delta), while its size is at most the size of Y plus O(delta). The latter estimate uses the coefficient 1-s<=1 on Y; it does not multiply the large size of Y by an adverse factor. Rescaling delta by a fixed constant proves (10).

For b=0 the product is polyhedral. A nonempty polyhedral feasible set with finite linear infimum attains it. Thus the unattained case necessarily has b>=1. QED.

This extends the upper-bound portion of milestone 14 to arbitrary mixed PSD/SOC/polyhedral lifts. No source Slater assumption is required before taking the actual minimum face, and no algorithm for finding that face is presumed.

## 4. Escape lower bounds for EVERY representation

Let S be a convex set in a finite-dimensional Euclidean space, and l an affine function whose finite infimum v on S is unattained. Suppose that, for some a>0,c>0, all sufficiently small eta satisfy

    inf{||x||:x in S,l(x)<=v+eta} >= c eta^(-a).        (11)

**Theorem C (intrinsic escape obstruction).** Every mixed-cone representation S=pi(F) of curvature resource b satisfies

    a<=2^b-1,
    b>=ceil(log_2(1+a)).                              (12)

For a single PSD lift of order d this gives

    d>=1+ceil(log_2(1+a)).                            (13)

**Proof.** The lifted objective l(pi(X)) has the same finite unattained infimum. By Section 3, some exactly feasible eta-optimal lifted points have size O(eta^(-(2^b-1))). For any fixed affine projection pi,

    ||pi(X)||<=c0+c2 tau(X)       for X in K,           (14)

because tau is a coercive gauge on K. This contradicts (11) if a>2^b-1. The constants in (14) may be arbitrarily large and may depend on the representation; they cannot defeat a strict power-exponent inequality as eta tends to zero. This proves (12) and (13). QED.

No encoder, canonical coordinates, positive projection, bounded coefficient size, rationality of a competing lift, or uniqueness of lifted points has entered this argument.

### Standard arbitrary-variable matrix-pencil models are covered

Suppose S has no affine line and is described by auxiliary variables u, affine output P(u), finitely many conic affine pencils M(u), and arbitrary affine equalities. Restrict u to the equality affine space first. If a direction h lies in the kernel of the LINEAR part of all conic pencils, u+t h is feasible for every real t whenever u is feasible. Hence P_lin(h) must be zero, or S would contain an affine line. Therefore P factors affinely through the conic pencil values M(u). The representation becomes an affine slice of the product cone followed by an affine projection, exactly the model used above. This argument also applies when linear inequalities are included as scalar conic pencils.

Thus arbitrary extra free variables do not evade Theorem C for the line-free sets studied here. A lift with no feasible point is irrelevant because our target sets are nonempty.

## 5. General inverse-power and power-cone lower bounds

For a>0 let

    S_a={(x,t):x>0,t>=x^(-a)}.

Minimizing x has infimum zero and forces norm at least eta^(-a) at objective tolerance eta. Minimizing t instead forces x>=eta^(-1/a). Therefore any mixed-cone lift of S_a obeys

    b>=ceil(log_2(1+max(a,1/a))).                     (15)

In particular every single PSD lift has order at least one more than this quantity, and every SOC lift has at least this number of nonpolyhedral Lorentz factors.

For the standard three-dimensional power cone

    P_alpha={(x,t,z):x,t>=0, |z|<=x^alpha t^(1-alpha)},
    0<alpha<1,

the section z=1 is S_a with a=alpha/(1-alpha). Adding a section to a lift costs only an affine equality, not another conic factor. Hence every representation satisfies

    b>=ceil(log_2(1/min(alpha,1-alpha))).             (16)

This lower bound is necessary for arbitrary coefficients and arbitrary auxiliary variables. It is not asserted sufficient at every rational alpha. An irrational alpha need not admit a finite semialgebraic conic lift at all; no general representability claim is made here for such alpha.

For alpha=1-2^(-k), formula (16) gives b>=k. The next section attains that exact bound.

## 6. An explicit order-(k+1) PSD lift of P_k

Use indices 0,...,k and impose the k-1 homogeneous copy equations

    Y_ii=Y_(0,i+1),             1<=i<=k-1.            (17)

Let Y>=0, and project by

    x=Y_00, t=Y_kk, z=Y_01.                           (18)

All unmentioned entries are free.

### Soundness

If x>0, the 2-by-2 principal minors and (17) give

    Y_11>=z^2/x,
    Y_ii>=Y_(i-1,i-1)^2/x       (2<=i<=k).

Induction yields

    t>=z^(2^k)/x^(2^k-1),

so (x,t,z) belongs P_k. If x=0, PSD forces the entire zeroth row to vanish, hence z=0; t>=0. This is again a point of P_k. Thus EVERY lifted PSD competitor decodes correctly, with no rank assumption.

### Completeness

For x>0 define a real vector v of length k+1 by

    v_0=sqrt(x),
    v_i=z^(2^(i-1))/x^(2^(i-1)-1/2),   1<=i<=k.

Then v_0 v_1=z, v_i^2=v_0 v_(i+1), and

    v_k^2=z^(2^k)/x^(2^k-1)<=t.

Therefore

    Y=v v^T+(t-v_k^2)e_k e_k^T                       (19)

is PSD, satisfies every copy equation, and has projection (x,t,z). It has rank at most two. The formula works for either sign of z. If x=0, the power-cone inequality forces z=0; use Y=t e_k e_k^T.

This proves equality of the entire projected feasible set and P_k. The affine section Y_01=1 gives S_k. All defining coefficients are 0,1 or -1. The nonlinear formula (19) is a witness construction, not an assumed positive linear section.

Since a single order-(k+1) PSD block has b=k, the lower bound in Section 5 proves exact optimality for arbitrary real or complex PSD lifts. The real construction is also a complex Hermitian construction by restriction, so the complex upper and lower bounds coincide.

## 7. Exactly k SOC factors, without an architectural restriction on the lower bound

Set a_0=z, a_k=t and introduce real a_1,...,a_(k-1). Impose

    [[x,a_(i-1)],[a_(i-1),a_i]] >=0,
                   i=1,...,k.                        (20)

These are k three-dimensional rotated Lorentz constraints. For x>0 their inequalities are exactly a_i>=a_(i-1)^2/x, so they project to P_k by the same induction. For x=0 they force z=a_1=...=a_(k-1)=0 and t>=0. Equality choices a_i=z^(2^i)/x^(2^i-1) for i<k prove completeness when x>0.

Thus k SOC factors suffice. Conversely any SOC lift, even one with Lorentz factors of arbitrary dimensions, coupled by arbitrary linear equations and inequalities, has b equal to its number of nonpolyhedral Lorentz factors. Section 5 forces b>=k. This proves Theorem A(b), not merely optimality within the displayed chain or a mediated-set template.

The relation between (17) and (20) is instructive: the k 2-by-2 blocks are the principal submatrices on the edges of a star with common center 0. Their PSD completion can be packed into one (k+1)-by-(k+1) PSD matrix. Formula (19) supplies the completion directly; no unproved completion theorem is used.

## 8. A necessary rank structure for every optimal single-PSD lift

An optimal single-PSD lift of S_k has order d=k+1. Its feasible affine slice must have a positive-definite point. Otherwise compression to its maximum feasible support would produce a lift of order at most k, contradicting the already proved lower bound. The same holds for the z=1 slice of any optimal lift of P_k.

For the lifted optimization problem minimizing x, the exact feasible trace profile has exponent exactly 2^k-1: the projected t-coordinate forces a lower bound of that power by (14), and the order-d upper bound supplies the matching upper power. The augmented infeasible optimality system has that same exponent, by the exact feasible-repair argument in Section 3 or milestone 14.

Let r0 be the maximum rank of a PSD matrix in the kernel of that augmented equality operator. The sharper bound in milestone 12 is 2^(d-r0)-1. Hence r0 cannot exceed one. It is at least one because a weakly infeasible PSD affine system has a nonzero PSD recession direction (normalize an unbounded affine approximate sequence). Therefore

    r0=1.                                             (21)

Moreover every complete hyper-feasible partition for that system must have k nontrivial partial steps: fewer would give a smaller exponent. In a (k+1)-dimensional PSD space this forces one-dimensional blocks with a one-dimensional terminal block.

This is a necessary rank-flag structure for every minimum-order lift. It is not a uniqueness or congruence-classification theorem for all such lifts.

## 9. The cones are not spectrahedra themselves when k>=2

For k>=2, P_k has no direct finite affine LMI representation in its three original coordinates, although it has the optimal projected representation above.

Here is an elementary proof. Put q=2^k>=4 and

    p(x,t,z)=x^(q-1)t-z^q.

This polynomial is irreducible over R: as a polynomial in t over R[x,z] it is primitive and linear, since x^(q-1) and z^q are relatively prime. Suppose an affine symmetric or Hermitian pencil M(x,t,z) represented P_k directly. At the interior point (1,1,0), delete the common kernel to arrange M(1,1,0)>0. Such a common-kernel deletion is valid: positivity of M at both small positive and negative coordinate perturbations forces every kernel vector at the interior point to lie in the kernel of every coefficient.

On the boundary graph x>0, t=z^q/x^(q-1), the pencil must be singular; otherwise a boundary point would have a neighborhood of feasible points. Thus det M vanishes identically on that graph. Polynomial division in t over R(x,z), followed by primitive polynomial divisibility, implies p divides det M in R[x,t,z].

Set x=t=1 and vary z=s. Then 1-s^q divides det M(1,1,s). But M(1,1,0)>0 implies that every zero of this determinant is real: after congruence by its positive square root, the pencil is I+s B with B symmetric/Hermitian and real eigenvalues. The polynomial 1-s^q has nonreal roots when q>=4. This is a contradiction.

For k=1, P_1 is the rotated Lorentz cone represented directly by [[x,z],[z,t]]>=0. The distinction is therefore exact. This argument is not used to prove the unrestricted lift-size lower bounds; it is an additional separation between direct and projected representations.

## 10. Examples and significance

For k=2, the cone is x^3 t>=z^4, x,t>=0. Its minimum PSD order is three and its minimum number of SOC factors is two. One explicit lift is

    [[x,z,u],[z,u,w],[u,w,t]] >=0,

where u,w are auxiliary. It is impossible to replace this with ANY order-two real or complex PSD lift, even with unlimited linear side constraints.

For k=3, the cone x^7 t>=z^8 has minimum PSD order four and minimum SOC count three. The sequence continues without increasing target dimension.

This is an optimality theorem for unrestricted conic lifts, rather than just an improved upper construction. The lower bound is intrinsic to how near-minimizers escape in the target set, and it survives arbitrary coefficients, auxiliary variables, singular faces and nonlinear choice of witnesses.

It does not prove a matching quadratic lower bound for the original two-basis normal form, solve exact SDP feasibility in polynomial time, classify all rational power-cone lift sizes, or establish an approximation lower bound for tolerance-dependent approximate representations. Those statements require different arguments.

## 11. Dependencies and related primary literature

The single-PSD pointwise escape theorem is in milestone 12 (commit 2e2f8f75c99f49e4b6e51fad2a37b41891928901). The exact-feasible near-optimal repair and all-minimizer regularization law are in milestone 14 (commit e9f76e9a21676dd93f7a890825ee3f22bf4af45c). Sections 2–3 here supply the needed product-PSD/Lorentz strengthening and the polyhedral-factor-independent resource count.

Related representation results are substantial and are not being relabeled as our work:

- Jie Wang, Weighted Geometric Mean, Minimum Mediated Set, and Optimal Simple Second-Order Cone Representation, SIAM Journal on Optimization 34(2) (2024), 1490–1514, DOI 10.1137/22M1531257. The stated abstract concerns optimal SIMPLE SOC representations, explicitly a particular subclass, and exact bivariate sizes. Primary page: https://epubs.siam.org/doi/10.1137/22M1531257 .
- Victor Blanco and Miguel Martinez-Anton, On Minimal Extended Representations of Generalized Power Cones, SIAM Journal on Optimization 34(3) (2024), 3088–3111, DOI 10.1137/23M1617205; arXiv:2311.10470. The work analyzes power-cone representations through mediated graphs and optimization formulations. Primary abstract: https://arxiv.org/abs/2311.10470 .
- Claus Scheiderer, Second-Order Cone Representation for Convex Sets in the Plane, SIAM Journal on Applied Algebra and Geometry 5(1) (2021), 114–139, DOI 10.1137/20M133717X. Every closed convex semialgebraic planar set has semidefinite extension DEGREE at most two. This is fully consistent with our unbounded minimum SINGLE PSD order and exact NUMBER of SOC factors. Primary page: https://epubs.siam.org/doi/10.1137/20M133717X .

The existence of repeated-square SOC representations is not claimed new. The statements proved here concern the unrestricted resource lower bound, its escape mechanism, and the matching single-PSD and arbitrary-dimension-SOC optimality for the specified infinite family. Full historical priority for the resulting synthesis is not certified. No claim is made that a specifically named previously open conjecture has been settled merely because an exact representation size has now been proved in this research.
