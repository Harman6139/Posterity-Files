# Checkpoint 03 — exact-oracle obstructions and model distinctions

These results are proved below. They do NOT constitute a universal disproof of the handoff's exact value/gradient lower-bound target.

## 1. Antipodal quadratic budget

Let H:R^d->S^m be a Frobenius isometry and f(x)=dist_F(X0+Hx,S_+^m)^2/2. For every v,

    lim_(t->infinity) [f(tv)+f(-tv)]/t^2 = ||v||^2/2.

Indeed cone distance is positively homogeneous and 1-Lipschitz, so f(tv)/t^2 tends to dist_F(Hv,S_+^m)^2/2. Spectral clipping gives dist(Hv,K)^2+dist(-Hv,K)^2=||Hv||_F^2=||v||^2. More quantitatively, with M=||X0||_F, the absolute error from t^2||v||^2/2 is at most sqrt(2)Mt||v||+M^2: each squared-distance error is at most 2Mt dist(+/-Hv,K)+M^2, and Cauchy--Schwarz bounds the sum.

Thus an isometrically parametrized natural PSD-distance objective cannot be subquadratic along both orientations of a nonzero ray. The linearly growing radial exterior of source milestone 38 cannot be represented unchanged as such an objective in its existing coordinates. Adding isometric padding changes the objective and requires a new proof. This rules out that direct transfer, not a different conic hiding construction.

## 2. One exact query identifies a rational quadratic

Let q(x)=x^T A x/2+b^T x+c, with rational symmetric A and rational b,c. In known dimension d set alpha=2^(1/(d+1)), v=(alpha,...,alpha^d). Eisenstein's criterion applied to z^(d+1)-2 makes 1,alpha,...,alpha^d linearly independent over Q. Each coordinate of grad q(v)=Av+b uniquely specifies its row of A and b; q(v) then specifies c.

This is an information theorem under unrestricted exact-real computation. The inverse on the countable response set is measurable. With exact equality tests, enumeration of rational candidate tuples terminates for each rational input, without any efficient runtime guarantee. Positive definite rational quadratics can then be minimized with no further queries. A known nonattained tail can likewise be driven below any positive tolerance.

Consequently rational approximation of a Haar-rotated quadratic is not an oracle-preserving reduction under exact unrestricted access. Real-coefficient randomized quadratic lower bounds are not contradicted.

## 3. A stronger oracle really does collapse

If the oracle supplies the complete rational affine embedding X(x)=X0+sum_i x_i H_i rather than only its distance and coordinate gradient, the same query v recovers EVERY matrix entry of X0 and H_i. For a promised weakly infeasible pencil, unrestricted computation then finds an approximate point at any specified positive tolerance without further oracle calls. For example, enumerate rational coordinates x and rational positive definite S until ||X(x)-S||_F is below the tolerance; density and the zero-distance promise guarantee termination. This is not a polynomial-bit runtime claim.

Similarly, an exact affine-projection oracle onto a rational affine subspace is an affine map with rational coefficients in rational matrix coordinates. Its matrix can be decoded by one algebraic query in the ambient dimension; its range then specifies the affine space. Thus exact affine-projection access with uncharged real precision differs materially from the handoff's value/coordinate-gradient oracle. Full explicit matrix data require zero identification calls under unrestricted computation.

## 4. Analytic subclasses collapse, but piecewise analytic classes need not

For any known countable family of pairwise distinct real analytic functions on connected R^d, one continuously distributed random query identifies the function almost surely from its exact value: each pairwise equality set has Lebesgue measure zero, and the countable union is null. The decoder is measurable by enumerating the family. In the abstract measurable-algorithm model, a preselected finite epsilon-approximate point for each member can then be returned. This is an information statement, not an effective bit algorithm for arbitrary analytic functions.

Rational conic data form a countable family, but the functions need NOT be globally analytic. For instance

    X_b(x,z)=diag(x-b, [[0,1],[1,z]]), b=-1 or -2,

are rational orthonormal weakly infeasible pencils. Their objectives min(x-b,0)^2/2+phi(z) agree on the OPEN set x>-1 and differ elsewhere. They share the beta=1/2 escape profile. A recovered analytic germ therefore does not determine the full conic objective. Countability alone proves no one-query recovery theorem for all rational conic instances.

## 5. Even exterior agreement does not imply equality

Let h_A(t) be the sum of (t-u)_+^2 for upper thresholds u={0,3,3} and (l-t)_+^2 for lower thresholds l={-1/2,-1/2,-7/2}. Let h_B use upper thresholds {1,1,4} and lower thresholds {1/2,-5/2,-5/2}. The two upper multisets have equal cardinality, sum 6 and square sum 18. The lower multisets have equal cardinality, sum -9/2 and square sum 51/4. Hence h_A=h_B outside [-7/2,4]. Nevertheless their zero sets are disjoint: [-1/2,0] and [1/2,1].

Both can be realized as natural rational scalar-cone distance terms, with an isometric coordinate: divide each of the six scalar affine inequalities by 3, add three common scalar blocks (t+10)/3, and append the known 2x2 weak-infeasibility tail. The nine t coefficients have squared sum 1. The extra three blocks are positive on both zero intervals and identical in both pencils. The resulting rational order-11 weakly infeasible objectives agree for all exterior t yet have different zero sets for their attained cores. Their tail escape profiles remain beta=1/2, with uniform constants over the pair.

Thus the antipodal theorem cannot be strengthened to the unsupported claim that all conic instances differing only on a bounded coordinate region are impossible. Constructing a dimension-growing, query-hard version with uniform escape geometry is a separate unsolved step.

## 6. PSD-valued unbiased projection samples are a different model

If S is a random PSD matrix with E S=P PSD, then ker P is contained in ker S almost surely. For each vector v in a finite basis of ker P, the nonnegative variable v^T S v has expectation zero; it vanishes almost surely, and PSD then implies Sv=0. Intersect the finitely many probability-one events.

Accordingly an arbitrary additive Gaussian coordinate-gradient error cannot automatically be interpreted as an unbiased PSD-valued approximate projection. Checkpoints 01--02 are results for measured natural coordinate gradients with prescribed conditional bias and variance. They are not lower bounds for a stronger oracle returning a cone-valued projection sample, and do not assume exact population values are supplied.

## 7. Present status

The handoff's universal exact value/gradient randomized lower bound is neither proved nor disproved here. The statistical and bias theorems in checkpoints 01--02 are independent of that gap, have a fixed two-point distribution chosen before the algorithm seed, and survive arbitrary finite query magnitudes. They must not be reported as the missing noiseless sequential lower bound.
