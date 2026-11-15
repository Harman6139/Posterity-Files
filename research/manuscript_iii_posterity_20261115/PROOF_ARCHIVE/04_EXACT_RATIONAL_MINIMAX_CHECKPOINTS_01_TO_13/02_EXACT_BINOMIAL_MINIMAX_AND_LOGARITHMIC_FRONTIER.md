# Checkpoint 02 — an exact rational conic minimax theorem

Date: 2026-11-15. Uses only the explicit construction in checkpoint 01. The original dimension-uniform power-law target is NOT declared resolved.

## Theorem A: exact minimax success probability

Let F_n={f_w:w in {-1,1}^n} be the rational weakly infeasible PSD-distance family of checkpoint 01. Set

    eta=1/4096, epsilon_n=(5/384) eta^n.

For every 0<epsilon<=epsilon_n and every integer T>=0,

    sup_alg inf_w Pr_alg{f_w(output)<=epsilon}
       = sup_alg E_(w uniform) Pr_alg{f_w(output)<=epsilon}
       = 2^(-n) sum_(j=0)^min(T,n) binom(n,j).            (1)

Algorithms may use at most T exact natural value-and-coordinate-gradient queries, any finite real query locations, unrestricted computation, independent randomization, and any unqueried finite output. The uniform prior is fixed before the algorithm's seed. The class template and every rational coefficient list may be known as candidates; only w is hidden. The upper algorithm needs gradients only and uses queries in the fixed quadratic field Q(sqrt(2)). There is no hidden degree or radius restriction in the lower bound.

### 1. A stronger prefix oracle simulates every natural query

Define a word-query oracle: query any complete guess g in {-1,1}^n; it returns the index of the first mismatch with w, or a special exact-match answer. The mismatch index reveals the true prefix through the mismatching position, because its earlier signs equal the guess and its last sign is the opposite guess. The unobserved suffix remains independent uniform under the uniform prior.

One call to this oracle suffices to simulate a natural conic query at ANY (x,z). Follow the nested intervals geometrically: whenever x belongs to one of the two children of the current interval, choose that child as the next guessed sign. If x is in neither, complete the guess arbitrarily. The children are disjoint. If the word oracle reports a mismatch before the arbitrary-completion stage, the revealed prefix includes the first true child not containing x. Exact locality from checkpoint 01 determines both H_w(x) and H'_w(x) from that prefix. If the true word agrees through the last geometrically selected child, the word oracle still supplies at least the next sign; x is outside both possible children at that node, so this again supplies all required information. Exact match reveals the entire word. Queries outside the initial interval already have the fixed exterior response and need no information. Endpoint cases use the same fixed exterior identities and do not reveal more.

The known phi(z) and phi'(z) add no information. Thus any natural T-query transcript and its arbitrary output can be generated with at most T calls to the stronger prefix oracle. This is a forward simulation for ALL finite real query locations, not only typical queries.

### 2. Exact success law of the prefix experiment

After any prefix-oracle transcript, the remaining candidates form a single prefix cylinder and are uniform there. Suppose r bits remain. A complete guess has first mismatch j with probability 2^-j, for j=1,...,r; exact match has probability 2^-r. At j=r or exact match the entire word is identified. All guesses are equivalent under the conditional uniform prior.

Let S(r,T) be the optimal probability of correctly naming the word after T remaining calls and an arbitrary unqueried final guess. Then

    S(0,T)=1, S(r,0)=2^-r,
    S(r,T)=sum_(j=1)^(r-1) 2^-j S(r-j,T-1)+2^(1-r), T>=1.

The unique solution is

    S(r,T)=2^-r sum_(j=0)^min(T,r) binom(r,j).

For a direct interpretation, predict each previously unseen sign independently. A query can correct the first mistaken prediction and all preceding correct predictions. There are T correction opportunities; the final unqueried guess succeeds exactly when the total number of mistaken predictions among r fair independent bits is at most T. This gives the binomial formula. The displayed recurrence gives a self-contained proof even without this interpretation.

Every epsilon-successful conic output has x in I_w by checkpoint 01, and the I_w are disjoint. Therefore it determines w. The prefix simulation gives the upper bound on average success in (1), including for every fixed algorithm seed and hence randomized algorithms. The minimax success is no larger than this uniform-prior success.

### 3. One natural gradient query realizes a complete word probe

For a guessed word g, let c_g be its interval center and query

    x_g=c_g+(h^n/16) sqrt(2), z=0, h=1/8.

This x_g lies strictly inside the zero interval J_g and has the form r+s sqrt(2) with rational s nonzero. It is bounded independently of n. If w=g, the x-gradient is zero.

If the first mismatch is at position j, x_g is inside every common ancestor's middle half and in the opposite child at level j. All ancestor reservoir terms vanish. It is outside the true child interval, where the remaining function has its fixed exterior quadratic. Thus, on a neighborhood of x_g, the true core is a rational quadratic with

    H''_w=lambda^j/2, lambda=1/64.

Its gradient at x_g is consequently

    H'_w(x_g)=(lambda^j/2)x_g+b,

where b is rational and is determined by the guessed prefix with its j-th sign flipped. For different j the rational slopes are distinct. Since x_g is irrational, rational affine functions with different slopes cannot give the same answer there. Nor can a nonconstant one have zero value there. Comparing the reply with the finitely many n candidate rational-affine replies and zero therefore determines j or exact match exactly. This is a finite effective decoder; no test of membership in Q over an infinite search space is needed.

After each such query, the algorithm knows the same prefix as in the word experiment. It can implement any complete word-probe strategy. At the end, output the center of its guessed leaf and a finite z with phi(z)<epsilon. If the word guess is correct, the objective is below epsilon. If it is wrong, the center belongs to a different disjoint leaf interval and the objective exceeds epsilon_n, so it fails at the displayed accuracies.

Under the uniform prior, the success law is S(n,T). To achieve the same success probability for EVERY fixed w, choose each previously unseen guessed sign independently and uniformly, continuing with a fresh random suffix after a mismatch. Relative to any fixed w, the prediction errors are independent fair bits. Thus the success probability is again S(n,T). This proves both equalities in (1).

## Corollaries: fixed-distribution lower bound and exact confidence complexity

For any fixed confidence 1-alpha, the exact query complexity on F_n at epsilon<=epsilon_n is the binomial quantile

    min{T:Pr{Binomial(n,1/2)<=T}>=1-alpha}.

For fixed alpha in (0,1/2), this is n/2+O_alpha(sqrt(n)). The exact finite formula, rather than this asymptotic, is the primary assertion.

In particular, choosing n=4(T+1) gives a fixed rational prior with

    Pr{f_w(output)>epsilon_n} >= 1-Pr{Binomial(4T+4,1/2)<=T} > 2/3.

For example, Chebyshev bounds the success probability by (T+1)/(T+2)^2<=1/4. The hard accuracy here is EXPONENTIAL in T:

    epsilon_n=(5/384)4096^(-4(T+1)).

The matrix order and total rational encoding length remain polynomial in T. This is a genuine randomized optimization lower bound in the ORIGINAL exact-rational oracle, but it is weaker than the sought polynomial-in-T objective threshold.

## Theorem B: exact expected minimax objective for the family

Put v0=(77/192)eta. For n>=1 the infimum expected minimax objective after T calls is

    Risk(n,0)=v0,
    Risk(n,T)=v0 sum_(k=T)^(n-1) binom(k-1,T-1)(eta/2)^k, 1<=T<n,
    Risk(n,T)=0, T>=n.                               (2)

These are infima because phi(z)>0 at every finite z. The same expressions are the uniform-prior Bayes risks.

Proof. If k<n signs have been identified, the unknown suffix is uniform. Its average core is even and convex, since reflecting x exchanges w with -w. Its minimum is at zero. At zero every nonempty suffix has exactly the same core value

    H_suffix(0)=eta Q_+(2)=(77/192)eta=v0.

Ancestor reservoir losses are nonnegative everywhere and vanish at the prefix center. Thus the conditional minimal expected core is exactly v0 eta^k, attained at that center. When k=n it is zero at the leaf center.

A complete word probe reveals a geometrically distributed number of further signs, truncated at n. All complete guesses have the same conditional law. A shorter or geometric-location probe is simulated by one complete word probe and cannot be more informative. Hence after T complete probes, the revealed depth is min(n,S_T), where S_T is a sum of T independent geometric(1/2) variables on {1,2,...}. For k<n,

    Pr{S_T=k}=binom(k-1,T-1)2^-k.

Averaging the displayed conditional risk gives (2). Natural-gradient probes realize the same experiment, establishing equality. Random independent guesses make this depth law identical for every fixed w; moreover, the actual core at a revealed prefix center is v0 eta^k for EVERY nonempty suffix, not merely on average. This gives a common worst-case risk. Make the known tail arbitrarily small by a finite z. QED.

The prefix-query experiment is closely related to the classical fixed-coordinate-order LeadingOnes black-box problem. The prefix-search methodology and binomial counting are not asserted to be historically new. The conic realization and the query-by-query equivalence, with rational isometry and uniform weak-infeasibility geometry, are the additional claims proved here.

## Theorem C: matching minimax law with two coordinates and arbitrary PSD order

Let C_2 be the class of ALL rational, Frobenius-isometric, genuinely weakly infeasible affine PSD pencils with exactly two coordinates, arbitrary finite matrix order, f(0)<=1, and

    (1/2)s^-1/2 <= rho_f(s) <= s^-1/2, 0<s<=1/8.

In the unrestricted exact natural value-and-gradient model, the worst-case fixed-confidence query complexity satisfies

    N_C2(epsilon; success 2/3)=Theta(log(1/epsilon)), epsilon down to zero.  (3)

The lower prior has order O(log(1/epsilon)) and polynomial binary encoding length in log(1/epsilon). The upper bound holds for every member of C_2, not just the known-template lower family.

### Lower bound

For epsilon sufficiently small, take

    n=floor(log_4096((5/384)/epsilon)).

Then epsilon<=epsilon_n and n=Theta(log(1/epsilon)). Checkpoint 01 places F_n in this SAME class. Formula (1) implies that fewer than n/2 queries cannot give success 2/3. For the stronger failure-at-least-2/3 formulation use any sufficiently small fixed fraction of n; the binomial formula supplies the constant. This proves the lower half of (3).

### Upper bound: an explicit two-dimensional central-cut algorithm

This is the classical cutting-plane mechanism, proved here for the nonattained profile and exact oracle. It is not a new ellipsoid algorithm.

Take a comparator u with f(u)<=epsilon/4 and ||u||<=R=2/sqrt(epsilon). Nonnegative convex 1-smoothness gives ||grad f(u)||<=sqrt(2f(u)). With r=sqrt(epsilon)/4, smoothness therefore gives for ||v-u||<=r,

    f(v)<=epsilon/4+epsilon/(4sqrt(2))+epsilon/32 < epsilon/2.

Thus the epsilon/2-sublevel contains the full disk B(u,r). It is contained in the initial search disk B(0,R+r) as far as this particular comparison disk is concerned; the entire sublevel need not be bounded.

Query the center c of the current ellipsoid. If f(c)<=epsilon, return c. Otherwise g=grad f(c) is nonzero, and convexity shows that the central halfspace

    {x:<g,x-c><=0}

contains the entire epsilon/2-sublevel and hence B(u,r). Replace the cut ellipsoid by its standard enclosing central-cut ellipse.

For completeness, in unit-disk coordinates the cut is y1<=0. The ellipse with center (-1/3,0) and semiaxes 2/3 and 2/sqrt(3) contains the half disk: using y2^2<=1-y1^2, its defining quadratic is at most

    1+(3/2)y1(y1+1)<=1, -1<=y1<=0.

Its area is 4/(3sqrt(3)) times the old area. An invertible affine map gives the update for every ellipse. Consequently N unsuccessful cuts would leave an ellipse of area at most

    pi(R+r)^2 [4/(3sqrt(3))]^N.

But it still contains B(u,r), of area pi*r^2. This is impossible when

    N > 2 log((R+r)/r)/log(3sqrt(3)/4)
      = 2 log(8/epsilon+1)/log(3sqrt(3)/4).

Thus O(log(1/epsilon)) exact natural oracle calls suffice. All centers and outputs are finite. No hidden data, unknown projection, minimizer or bounded-query assumption is used. QED.

The same standard ellipsoid argument in any FIXED coordinate dimension d gives O_d((beta+1/2)log(1/epsilon)) queries from a fixed profile upper bound C epsilon^-beta. Replacing the tail by the earlier fixed rational beta-tail gives a matching logarithmic lower bound in a suitable fixed dimension depending on beta. The fully explicit self-contained result above is beta=1/2 and d=2.

## 7. Precise relation to the original flagship target

This is now an actual exact-rational conic MINIMAX OPTIMIZATION theorem, not just a spectral-identification theorem. It shows that unrestricted exact rational arithmetic does not collapse the whole class to a fixed accuracy-independent number of queries. It also closes the fixed-two-coordinate frontier, even when PSD order is unbounded.

It does NOT prove the dimension-uniform Omega(epsilon^-1) bound requested at beta=1/2, nor a dimension-independent logarithmic upper bound. The two-coordinate upper bound cannot be asserted uniformly as the coordinate dimension grows. For the complete class with varying dimension, the proved bracket remains a logarithmic lower bound and the previously established accelerated O(epsilon^-1) upper bound. Deciding the gap is still the original outstanding problem.

No top-quintile journal benchmark or historical-priority certification is claimed. The earlier real-chart, rational positive-error, and charged-radius theorems remain separately labeled results. This exact-rational endpoint theorem neither imports their lower bounds nor changes their oracle definitions.