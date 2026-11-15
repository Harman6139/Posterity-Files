# Checkpoint 13 — spectral jumps cannot terminate along a hyperplane

Date: 2026-11-15. Continues checkpoints 11–12. This is a necessary structural theorem for natural affine PSD-distance objectives. It does not settle the original all-pencil randomized minimax frontier.

## 1. Statement: a polyhedral piecewise-quadratic rigidity theorem

Let X(x)=A+sum_i x_i H_i be any real symmetric affine pencil, of any finite order m, and put

    F(x)=dist_F(X(x),S_+^m)^2/2.

No rationality, isometry, feasibility or coefficient bound is assumed. Suppose F is quadratic on every cell of a finite full-dimensional polyhedral partition of R^d. Since F is a squared distance composed with an affine map, it is automatically C1. Such a function will be called finite polyhedral piecewise quadratic (PLQ) here.

THEOREM A. There are a global quadratic polynomial Q, distinct affine hyperplanes with unit-normal forms ell_j(x)=n_j.x-b_j, and real numbers kappa_j such that

    F(x)=Q(x)+(1/2)sum_{j=1}^s kappa_j (ell_j(x))_+^2.  (1)

In particular, the jump in the constant Hessian across a given hyperplane cannot change on another part of that hyperplane or stop at a facet endpoint. Terms with zero kappa are omitted, and

    s <= max_x rank X(x) <= m.                       (2)

The coefficients kappa_j can have either sign; no assertion that Q is convex or that (1) is by itself a sufficient PSD-distance representation is made. The theorem is a necessary condition on the scalar objective, not simultaneous diagonalization of the given pencil.

The one-dimensional version of (1) is the usual representation of a C1 piecewise quadratic by squared hinges. The substantive propagation step concerns d>=2.

## 2. The spectral second-order jump at a zero eigenvalue

Fix symmetric matrices M,B and let Pi project orthogonally onto ker M. Put C=Pi B Pi, viewed on the whole matrix space so its extra eigenvalues are zero. For

    h(t)=dist_F(M+tB,S_+)^2/2,

write the second-order Taylor coefficients from t>0 and t<0 as h''_+ and h''_-. These coefficients exist; if the restrictions are quadratic on the two sides they are their ordinary constant second derivatives. Then

    h''_+ - h''_- = -tr(C |C|), |C|=(C^2)^(1/2).    (3)

Here is a proof that also accounts for all nonzero eigenvalues. The negative eigenvalue cluster of M bounded away from zero continues analytically as a cluster for small t. The trace of its squared eigenvalues is analytic: it equals tr((M+tB)^2 E(t)), where E(t) is the analytic spectral projector onto that separated cluster. It therefore contributes the SAME second-order coefficient on both sides. The positive cluster contributes zero. The eigenvalues emerging from ker M have first-order terms t mu_i+o(t), where mu_i are the eigenvalues of the compression of B to ker M. This follows directly by splitting ker M and its orthogonal complement: the nonzero block is invertible, and the Schur complement of M+tB-lambda I on the kernel block, at lambda=t z, is t(C-z I)+O(t^2). Equivalently, an orthogonal change of coordinates with a skew off-diagonal generator cancels the O(t) off-diagonal block, leaving tC+O(t^2) on the kernel; Weyl's eigenvalue bound gives the same conclusion.

For t>0, these small eigenvalues contribute (t^2/2)sum_{mu_i<0}mu_i^2+o(t^2). For t<0 the sum is over mu_i>0. The difference is -sum_i mu_i |mu_i|=-tr(C|C|). Zero slopes contribute o(t^2) and create no missing term. This proves (3).

The eigenvalue perturbation and separated-projector facts are classical. Formula (3) is used here to control propagation along a polyhedral switching hyperplane, not to claim a new general spectral differentiation calculus.

## 3. Kernel projectors on an affine line have removable rank-drop singularities

LEMMA B. Let M(s)=M0+s M1 be a real symmetric affine pencil in one scalar parameter, and let r be its maximal rank on the line. On its rank-r locus, the projector Pi(s) onto ker M(s) has rational-function entries in s. It extends continuously across all exceptional real points, although its continued value there need not equal the projector onto the larger exceptional kernel.

PROOF. The characteristic polynomial is

    det(lambda I-M(s))=lambda^(m-r)
          [lambda^r+a_(r-1)(s)lambda^(r-1)+...+a0(s)],

where the a_i are real polynomials and a0 is not identically zero. At every rank-r point a0!=0, since all r nonzero eigenvalues are real and their product is nonzero. By applying the bracketed polynomial to M(s),

    Pi(s)=[M(s)^r+a_(r-1)(s)M(s)^(r-1)+...+a0(s)I]/a0(s). (4)

Indeed this is zero on every nonzero eigenspace and one on the kernel. The case r=0 is Pi=I. A nonzero polynomial has only finitely many real roots. Each entry of Pi(s) is bounded by one on the real regular locus, because it is an orthogonal projector. A rational function bounded near a real pole has a removable singularity there: cancel the common factors in numerator and denominator. Thus all entries extend continuously, in fact real analytically locally, across the finitely many exceptional real points. QED.

Boundedness is indispensable. No similar claim about an arbitrary multivariable rational projector extending across all of its singular locus is used. We need only the one-line statement (4).

## 4. Proof of global jump propagation

Extend the facets of a finite PLQ partition to a finite collection of full affine hyperplanes, merging repeated hyperplanes. Their arrangement refines the partition, so F is quadratic on each open chamber.

Fix one of these hyperplanes H={ell=0}, with ell(x)=n.x-b and ||n||=1. At a point p in H not on another arrangement hyperplane, let Q_+ and Q_- be the two adjacent quadratic formulas (they may be the same). C1 matching across the open facet implies

    Q_+(x)-Q_-(x)=(kappa(p)/2)ell(x)^2,              (5)

because a degree-at-most-two polynomial whose value and gradient vanish on an open part of H is a scalar multiple of ell^2. Thus the Hessian jump is kappa(p) n n^T. As p varies, kappa(p) takes only finitely many constant values.

Set B=sum_i n_i H_i and, at a point where the restriction X|_H has maximal rank, let Pi(p) project onto ker X(p). Applying (3) in the normal direction gives

    kappa(p)=-tr((Pi(p) B Pi(p)) |Pi(p) B Pi(p)|).     (6)

Take any two points p,q of H which lie on no other arrangement hyperplane and are rank-regular for X|_H. Along the affine line p+s(q-p), the restricted pencil has the same maximal rank as X|_H: a maximal minor is nonzero at p. Its rank can drop only at finitely many parameters. The line is not contained in another arrangement hyperplane, because p is on none of those; hence it meets each at most once. Lemma B continuously extends the kernel projector along the whole line. The right side of (6) is then a continuous function of s, since C -> tr(C|C|) is continuous on symmetric matrices.

Away from those finitely many exceptional parameters, that function equals one of the finitely many PLQ jump constants. A continuous function on a connected line whose values on a dense set belong to a fixed finite set is constant. Therefore kappa(p)=kappa(q). The rank-regular points are dense in H, so all open facet pieces carry the SAME jump kappa_H, including any open portion on which F has no actual switch (where the jump is zero).

Subtract (1/2)kappa_H (ell_H)_+^2 for every arrangement hyperplane. Across every generic facet the resulting C1 piecewise-quadratic function has zero Hessian jump. The chamber adjacency graph of a finite hyperplane arrangement is connected, so every chamber has the same Hessian. C1 matching then gives the same affine and constant terms. The remainder is one global quadratic polynomial. This proves (1).

For (2), let r=max_x rank X(x) and choose one nonzero r-by-r minor D(x), of degree at most r (for r=0 the function is constant and s=0). At an ambient rank-regular point, the kernel eigenvalues remain zero locally and the nonzero eigenvalues stay separated from zero; hence F is analytic there. An actual nonzero PLQ Hessian jump cannot pass through such a point. Thus the generic part of each nonzero-jump hyperplane lies in the rank-drop locus, and D vanishes on a relatively open subset of that hyperplane. Its affine linear defining polynomial divides D. Distinct hyperplanes give distinct linear factors; their product divides D. Therefore s<=deg D<=r. QED.

## 5. Exterior rigidity now holds for ALL finite-PLQ natural pencils

COROLLARY C. In dimension d>=2, suppose F_1,F_2 are natural affine PSD-distance objectives which are finite PLQ. If F_1=F_2 outside some Euclidean ball, then F_1=F_2 everywhere, even if the underlying matrices do not commute.

PROOF. Theorem A writes their difference as a quadratic plus finitely many signed squared affine hinges. For each distinct zero hyperplane, choose a point on that hyperplane outside the ball and on no other zero hyperplane; such a point exists because H has positive dimension. Both adjacent Hessians of the difference vanish there. Their jump is the hinge coefficient times n n^T, so that coefficient is zero. After all hinges are removed, the remaining quadratic vanishes on an open set and is zero globally. QED.

This extends checkpoint 06's commuting/ridge-sum obstruction, but only under the explicitly stated PLQ hypothesis. The compact ball-based masks of checkpoints 08 and 12 are not PLQ in dimensions >=2 and are not excluded.

## 6. An exact nonrepresentability consequence for smooth convex optimization

Let Delta={(u,v):u>=0,v>=0,u+v<=1}, and let

    g(u,v)=dist((u,v),Delta)^2/2.

This is a nonnegative convex C1, 1-smooth finite-PLQ function. For completeness, projection onto each face is affine on that face's polyhedral normal region; these finitely many regions cover R^2, and the squared distance is quadratic on each. No nonsmooth max objective is being substituted for g.

THEOREM D. For every a>0 and every global quadratic polynomial Q(u,v), there is NO finite-order real symmetric affine pencil Y(u,v) with

    dist_F(Y(u,v),S_+)^2/2 = a g(u,v)+Q(u,v)          (7)

on all R^2. Thus no rational pencil, no isometric pencil and no increase in PSD order can give (7).

PROOF. On the line u=0 and near a point with 0<v<1, the local formulas for g are u^2/2 on the u<0 side and zero on the u>0 side. Its u-normal Hessian jump is -1. Near (0,v) with v>1, the projection is the vertex (0,1) for all sufficiently small |u|; more explicitly |u|<v-1 gives the vertex normal-cone condition. Thus g=[u^2+(v-1)^2]/2 on both sides and the jump is zero. Adding Q does not change a Hessian jump, and multiplying by a makes the first jump -a but leaves the second zero. This violates Theorem A's propagation along the same full hyperplane u=0. QED.

The obstruction survives an independent nonattained tail: if a pencil in (u,v,z) represented a g(u,v)+Q(u,v)+phi(z), fix any finite z. The resulting affine pencil in (u,v) would contradict (7). Nor can a fixed invertible affine change of (u,v) remove the obstruction, since composition would pull an alleged pencil back to (7).

This is a concrete failure of an oracle-level universality shortcut. A triangle is polyhedral and easily represented by scalar semidefinite inequalities, and its squared distance has a quadratic-programming representation. Neither fact makes that squared-distance objective the natural squared PSD distance of an affine pencil in the original query variables. An auxiliary-variable minimization is not equality of oracle replies at arbitrary lifted points.

### Adjacent nonorthogonal facets give the same obstruction

The same proof applies to the squared distance of any full-dimensional polyhedron with two adjacent facets whose unit outward normals a,b have inner product gamma not equal to zero. At a relative-interior point of their common ridge, other constraints are locally slack. In the two-dimensional normal plane, the local cone is K={a.y<=0,b.y<=0}. Along a.y=0 with b.y<0, the a-normal Hessian jump is one. Along that line with b.y>0 it is zero:

* If gamma>0, y-(b.y)b has a-coordinate -gamma(b.y)<0, so projection lies in the interior of the b facet and the local squared distance is (b.y)^2/2.
* If gamma<0, write y=alpha a+beta b. The equations give beta=(b.y)/(1-gamma^2)>0 and alpha=-gamma beta>0. Thus y lies in the interior of the vertex normal cone, projection is the ridge, and the local normal-plane loss is ||y||^2/2.

Both latter expressions are smooth across a.y=0. Taking sufficiently small y makes this local wedge computation valid for the original polyhedron. Therefore its squared distance, up to a positive scale and global quadratic, cannot be a natural affine PSD distance. Every full-dimensional simplex in dimension >=2 has a nonorthogonal adjacent facet pair: it has d+1 pairwise adjacent nonparallel facets, whose normals cannot all be pairwise orthogonal in R^d.

For comparison, boxes and orthogonal cylinders DO have the usual sum-of-squared-affine-hinges distance formulas. For a rational box, one quarter of its squared Euclidean distance has a rational isometric scalar PSD realization: for each bounded coordinate use two copies of (x_i-l_i)/2 and two copies of (u_i-x_i)/2. The direction Gram is one and the objective is ((l_i-x_i)_+^2+(x_i-u_i)_+^2)/4. This establishes a nontrivial representable boundary; no full classification of polyhedra is claimed.

## 7. Why the PLQ restriction cannot be omitted

Consider

    X(x,y,z)=[[0,y,z],[y,x,0],[z,0,0]].

On x=0 with (y,z)!=(0,0), its kernel is spanned by (0,-z,y). For the x-direction B=diag(0,1,0), the kernel compression has sole nonzero eigenvalue z^2/(y^2+z^2). Formula (3) gives the normal second-order jump

    -z^4/(y^2+z^2)^2.                                (8)

This varies continuously along the hyperplane: it is zero at (y,z)=(1,0), -1 at (0,1), and -1/4 at (1,1). The characteristic polynomial is

    lambda^3-x lambda^2-(y^2+z^2)lambda+x z^2.

Thus general noncommuting PSD pencils CAN have spatially varying spectral curvature jumps. Theorem A rules out a FINITE, piecewise-constant change of those jumps under the global PLQ hypothesis; it is not a claim that every natural objective has constant curvature on rank strata.

## 8. Antecedents, verification and remaining target

First-order spectral calculus is classical: A. S. Lewis, Derivatives of Spectral Functions, Mathematics of Operations Research 21(3) (1996), 576–588, DOI 10.1287/moor.21.3.576. The first-order eigenvalue compression expansion appears, for example, as Lemma 2.3 in A. S. Lewis and H. S. Sendov, Twice Differentiable Spectral Functions, SIAM Journal on Matrix Analysis and Applications 23(2) (2001), 368–386, DOI 10.1137/S089547980036838X. The latter paper proves the general Hessian theorem, not the PLQ propagation or triangle nonrepresentability statement asserted here. Those classical perturbation ingredients are not claimed as inventions.

The specific claims supplied here are the full-hyperplane jump propagation, its finite-ridge consequence for an arbitrary noncommuting affine pencil, and the natural-distance nonrepresentability corollaries. A targeted literature check is not an exhaustive historical-priority certificate or independent external review. Exact checks of the displayed examples accompany the continuation verification packet; the all-order theorem rests on the proof, not finite tests.

This excludes another family of proposed exact oracle-preserving conic realizations. It neither constructs the original fixed rational hard prior at polynomial-in-T objective loss nor proves a universal faster optimizer for every weakly infeasible rational pencil. That flagship dichotomy remains unresolved in this continuation.
