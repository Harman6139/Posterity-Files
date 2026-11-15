# Milestone 26 — Escape geometry determines sharp projection and acceleration rates

Date: 2026-11-13 (America/Toronto).
Repository: Harman6139/Posterity-Files.
Branch: laa-track02-gptpro-analytic-frontier-20261112.
Parent research snapshot: 3184728adc4953d16224bd35be29ca06e57b47f7.

## Status and central result

This manuscript proves two-sided asymptotic rates for specified first-order methods when the infimum is finite but is not attained. The invariant is the minimum radius needed to approach the infimum. It gives, in particular, an exact rate formula for alternating projections on EVERY weakly infeasible semidefinite system, and for a fully specified accelerated projection scheme. Neither algorithm needs to know the invariant.

The core dynamics proof is self-contained and independent of the two-basis constructions, geometric counting arguments, Boolean-moment families, and complexity assumptions. The sharp dimension-only SDP envelope uses the escape theorem and explicit endpoint examples of project manuscript 12. The mixed-cone extension uses 15–16. Those dependencies are explicit.

Projection inequalities and accelerated estimate sequences are classical. This manuscript derives matching upper AND lower rates from them by also controlling the radius of the algorithm's iterates. It is not a claim that these algorithms are new, that acceleration always doubles every convergence rate, or that a famous named complexity conjecture has been resolved. No comprehensive historical-priority certification has occurred. The specific mathematical question answered here is stated precisely below.

## 1. A general nonattainment problem and its radius profile

Let Q be a nonempty closed convex subset of a finite-dimensional Euclidean space. Let f be convex and continuously differentiable on an open convex neighborhood of Q. Assume its gradient is L-Lipschitz on Q, with a known L>0; equivalently the usual smoothness inequality on pairs in Q suffices below. Suppose

    f_* = inf_{x in Q} f(x) is finite and is not attained.

Write g(x)=f(x)-f_*>0 on Q. For x_0 in Q define

    rho(s)=min{ ||x-x_0|| : x in Q, g(x)<=s },  s>0.       (1)

The feasible set in (1) is nonempty and closed. A minimizing sequence is bounded, so the minimum exists. If rho(s) stayed bounded along s decreasing to zero, a convergent subsequence would attain f_*, a contradiction. Thus rho(s) tends to infinity.

Assume, for some beta>0 and fixed positive c,C,s_0,

    c s^(-beta) <= rho(s) <= C s^(-beta),  0<s<=s_0.    (2)

The constants may depend on the instance and starting point. Changing x_0 changes rho by at most a fixed additive constant, so beta is independent of the starting point. Replacing the norm by any fixed equivalent norm likewise leaves beta unchanged.

If Q and f are semialgebraic, (2) holds automatically for some positive rational beta. Indeed the value graph in (1) is semialgebraic by quantifier elimination; the standard one-variable growth theorem gives rho(s)~c_0 s^(-beta). Its divergence forces beta>0. This is a statement about a static value function, not a claim that an infinite algorithmic trajectory is semialgebraic.

## 2. General projected-gradient theorem

For any fixed 0<eta<=1/L consider

    x_{k+1}=Proj_Q(x_k-eta grad f(x_k)).                 (3)

**Theorem A.** Under (1)–(2), from EVERY x_0 in Q,

    g(x_k) = Theta(k^(-1/(2beta+1))),
    ||x_k-x_0|| = Theta(k^(beta/(2beta+1))).             (4)

Theta means two-sided positive constant bounds for all sufficiently large integers k. It does not assert a limit for the leading coefficient. In particular the iterates escape to infinity while their objective values approach the unattained infimum.

### 2.1 Comparator energy inequality

For every u in Q, projection optimality, convexity, and smoothness give

    2eta [f(x_{k+1})-f(u)]
        <= ||x_k-u||^2-||x_{k+1}-u||^2.                 (5)

For completeness, put d=x_{k+1}-x_k. Projection optimality gives

    <grad f(x_k),x_{k+1}-u>
      <= [||x_k-u||^2-||x_{k+1}-u||^2-||d||^2]/(2eta).

Convexity at x_k and smoothness from x_k to x_{k+1} give

    f(x_{k+1})-f(u)
      <= <grad f(x_k),x_{k+1}-u>+(L/2)||d||^2.

Since eta L<=1, the remaining squared-step coefficient is nonpositive. This proves (5). Taking u=x_k also proves monotonicity of f(x_k).

Sum (5) and use monotonicity. With R_u=||u-x_0|| and T=eta k,

    g(x_k) <= g(u)+R_u^2/(2T),                          (6)
    ||x_k-u||^2 <= R_u^2+2T g(u).                       (7)

The second inequality follows by dropping the nonnegative terms g(x_j) from the summed inequality. The sharper joint inequality also holds:

    T[g(x_k)-g(u)]+(1/2)||x_k-u||^2 <= R_u^2/2.

Crucially, u is an arbitrary approximate minimizer, not a nonexistent exact minimizer.

### 2.2 Finite-horizon profile bounds

Use a minimizer in (1) as u. For EVERY s>0 and k>=1,

    g(x_k) <= s+rho(s)^2/(2T),                          (8)
    ||x_k-x_0|| <= rho(s)+sqrt(rho(s)^2+2Ts).            (9)

These formulas hold without the power-law assumption (2). Choose s=T^(-1/(2beta+1)) in the power-law case. It gives constants C_1,C_2 with

    g(x_k)<=C_1 T^(-1/(2beta+1)),
    ||x_k-x_0||<=C_2 T^(beta/(2beta+1)).                 (10)

Thus g(x_k) tends to zero, so the lower half of (2) applies at g(x_k) for large k.

### 2.3 Why both rates have matching lower bounds

By definition of rho,

    rho(g(x_k)) <= ||x_k-x_0||.                         (11)

Using its lower bound and the radius upper bound in (10),

    c g(x_k)^(-beta) <= C_2 T^(beta/(2beta+1)),

which implies g(x_k)>=c_1 T^(-1/(2beta+1)). Using instead the objective upper bound in (10) inside the left side of (11) gives

    ||x_k-x_0|| >= c_2 T^(beta/(2beta+1)).

This proves (4). The lower rate is not an inference from a worst-case example: it holds for every trajectory satisfying the hypotheses. QED.

### 2.4 Variable steps and proximal steps

The identical proof allows 0<eta_j<=1/L with T_k=sum_{j<k}eta_j tending to infinity; replace k in (4) by T_k. Objective monotonicity is retained and the energy estimate telescopes with these weights. This does not imply a k-rate without a lower bound on cumulative steps.

For the exact proximal-point method on a proper lower-semicontinuous convex objective F with finite unattained infimum,

    x_{k+1}=argmin_x [F(x)+||x-x_k||^2/(2eta)],

the stronger standard proximal inequality implies (5). Thus (4) holds for its norm profile as well, without differentiability. A proximal subproblem may be expensive; this corollary is not an oracle-cost improvement.

## 3. A specified accelerated scheme and its exact rate

The conclusion is for the following scheme, not for every method called accelerated. Initialize x_0=z_0 in Q and A_0=0. For k>=0 set

    a_{k+1}=(1+sqrt(1+4 L A_k))/(2L),
    A_{k+1}=A_k+a_{k+1}=L a_{k+1}^2,
    y_k=(A_k x_k+a_{k+1} z_k)/A_{k+1},
    z_{k+1}=Proj_Q(z_k-a_{k+1} grad f(y_k)),
    x_{k+1}=(A_k x_k+a_{k+1} z_{k+1})/A_{k+1}.        (12)

All x_k,y_k,z_k lie in Q. The updates do not involve beta, f_*, or any approximate-minimizer oracle. They use one gradient and one projection per iteration.

**Theorem B.** Under (1)–(2), the outputs x_k in (12) satisfy

    g(x_k)=Theta(k^(-2/(2beta+1))),
    ||x_k-x_0||=Theta(k^(2beta/(2beta+1))).              (13)

Hence this scheme exactly doubles the objective-decay power of (3) for this nonattainment class. It also doubles the iterate-growth power. This is not a claim about an attained minimizer or about all acceleration schemes.

### 3.1 The estimate sequence, with arbitrary comparators

For every u in Q,

    A_k[g(x_k)-g(u)]+(1/2)||z_k-u||^2
                   <= (1/2)||x_0-u||^2.               (14)

Here is a direct proof, including the constrained case. Abbreviate A=A_k, a=a_{k+1}, A'=A+a, y=y_k, z'=z_{k+1}, x'=x_{k+1}, and v=grad f(y). Since x'-y=(a/A')(z'-z_k), smoothness and La^2=A' give

    A'f(x')<=A'f(y)+a<v,z'-z_k>+(1/2)||z'-z_k||^2.

Convexity and the definition of y give

    A f(x_k)+a f(u)>=A'f(y)+a<v,u-z_k>.

Projection optimality gives

    a<v,z'-u> <= [||z_k-u||^2-||z'-u||^2
                                     -||z'-z_k||^2]/2.

Combining the three inequalities yields

    A'f(x')+(1/2)||z'-u||^2
        <=A f(x_k)+a f(u)+(1/2)||z_k-u||^2.

Subtract A'f(u) and telescope from A_0=0. This proves (14) without assuming an exact optimizer exists.

### 3.2 Radius control for the actual output

Equation (14) gives

    g(x_k)<=g(u)+||x_0-u||^2/(2A_k),
    ||z_j-u||^2<=||x_0-u||^2+2A_k g(u), j<=k.          (15)

The second inequality uses g(x_j)>=0 and A_j<=A_k. Moreover

    x_k=(1/A_k)sum_{j=1}^k a_j z_j.

Thus convexity of the norm gives

    ||x_k-x_0||<=||u-x_0||
                 +sqrt(||u-x_0||^2+2A_k g(u)).         (16)

With a radius-minimizing comparator, (15)–(16) are exactly (8)–(9) with T=A_k. The argument of Section 2.3 supplies both lower bounds as well.

For k>=1 the weight sequence satisfies

    (k+1)^2/(4L)<=A_k<=k^2/L.                          (17)

Indeed t_k=sqrt(L A_k) obeys t_{k+1}=(1+sqrt(1+4t_k^2))/2, t_1=1, and t_k+1/2<=t_{k+1}<=t_k+1. Thus A_k=Theta(k^2), proving (13). No monotonicity of accelerated objective values is needed. QED.

## 4. A regularization interpretation, not a trajectory identity

For T>0 the problem

    min_{x in Q} [g(x)+||x-x_0||^2/(2T)]                (18)

has a unique minimizer x_T: the objective is coercive and strongly convex on Q. Choosing the same comparator as in (8) bounds its value by O(T^(-1/(2beta+1))). The quadratic penalty then bounds ||x_T-x_0|| by O(T^(beta/(2beta+1))). The radius lower bound (11) supplies the matching objective and radius lower bounds.

Consequently (3) has the SAME objective/radius power orders as (18) at T=Theta(k), and (12) has them at T=Theta(k^2). This is not equality of points, asymptotic directions, or leading coefficients. It is also not optimality over all algorithms: a specialized method can use additional structure, nonlocal information, or a direct formula.

## 5. Alternating projections for general disjoint semialgebraic convex sets

Let U,V be nonempty closed convex sets in a finite-dimensional Euclidean space with

    U intersect V = empty, dist(U,V)=0.

Fix x_0 in U and define

    R_{U,V}(delta)=min{||x-x_0||:x in U,
                                      dist(x,V)<=delta}. (19)

If U,V are semialgebraic, there is a positive rational a such that

    R_{U,V}(delta)=Theta(delta^(-a)).                   (20)

Proof: nonempty closed sublevel sets give attained radius minima; bounded radii as delta->0 would give an intersection point; semialgebraic growth gives the positive rational exponent. This uses no conic structure.

Set f(x)=(1/2)dist(x,V)^2 and Q=U. Then f is convex, differentiable, and has 1-Lipschitz gradient grad f(x)=x-Proj_V(x). Its infimum over U is zero and unattained. Its objective-radius exponent is beta=a/2, because rho(s)=R_{U,V}(sqrt(2s)).

**Theorem C.** Ordinary alternating projections

    x_{k+1}=Proj_U Proj_V(x_k)

have, from every x_0 in U,

    dist(x_k,V)=Theta(k^(-1/[2(a+1)])),
    ||x_k-x_0||=Theta(k^(a/[2(a+1)])).                 (21)

Applying (12) with L=1 and grad f(y)=y-Proj_V(y) gives

    dist(x_k,V)=Theta(k^(-1/(a+1))),
    ||x_k-x_0||=Theta(k^(a/(a+1))).                    (22)

Both methods use one V-projection and one U-projection per iteration. The accelerated scheme's reported x_k, not its auxiliary z_k or an arbitrary momentum iterate, is the output in (22).

The exponent a is unchanged if the roles of U and V are exchanged: projecting a point at distance delta to the other set changes its radius by at most delta plus a fixed change of origin, and the converse comparison is identical. The statements concern zero-distance disjointness, NOT the distance to an existing intersection.

## 6. Semidefinite translation: the escape invariant from manuscript 12

Let A:S^m->R^p be linear and let b be weakly infeasible:

    b in closure A(S_+^m) but b not in A(S_+^m).

Since range A is closed, b belongs range A, so the affine space

    L_b={Z:A(Z)=b}

is nonempty. Fix Z_0 in L_b. Let

    R_b(delta)=min{tr X:X>=0,||A(X)-b||<=delta}
                  =Theta(delta^(-a)),                 (23)

and let r_aff(delta) be the radius profile in (19) with U=L_b,V=S_+^m.

**Lemma.** These two profiles have the SAME exponent a.

Choose a fixed right inverse T of A on range A, with tau=||T||>0. Given X>=0 with ||A(X)-b||<=delta/tau, put Z=X+T(b-A(X)). Then Z belongs L_b, dist(Z,S_+^m)<=delta, and

    ||Z-Z_0||<=trX+delta+||Z_0||.

Conversely, from Z in L_b within delta of the cone put X=Proj_{S_+^m}(Z). Then

    ||A(X)-b||<=||A||delta,
    trX<=sqrt(m)(||Z-Z_0||+||Z_0||+delta).

Thus

    R_b(||A||delta)/sqrt(m)-||Z_0||-delta
      <=r_aff(delta)
      <=R_b(delta/tau)+||Z_0||+delta.                  (24)

The divergence of the profiles and (23) prove the lemma. Neither a favorable rank nor a source Slater point is assumed.

**Theorem D (all weakly infeasible SDPs).** Let

    Z_{k+1}=Proj_{L_b} Proj_{S_+^m}(Z_k),
    r_k=dist_F(Z_k,S_+^m).

For every affine starting point Z_0,

    r_k=Theta(k^(-1/[2(a+1)])),
    ||Z_k||_F=Theta(k^(a/[2(a+1)])).                   (25)

The accelerated algorithm (12), specialized as in Section 5, satisfies

    r_k=Theta(k^(-1/(a+1))),
    ||Z_k||_F=Theta(k^(a/(a+1))).                      (26)

For the PSD companions X_k=Proj_{S_+^m}(Z_k), their Frobenius norm and trace have the same growth order as ||Z_k||. Their ORIGINAL equation residual ||A(X_k)-b|| has the SAME decay order as r_k, for either algorithm.

For the last claim, the upper bound is ||A(X_k)-b||<=||A||r_k. For the lower bound use R_b(||A(X_k)-b||)<=trX_k and the already proved upper trace-growth rate, together with the lower profile in (23). Norm comparability follows from ||Z_k-X_k||=r_k->0 and ||Z_k||->infinity; PSD trace and Frobenius norm are equivalent. QED.

The theorem does not turn a small residual into an infeasibility certificate. It quantitatively describes a sequence that looks more feasible while its size diverges.

## 7. Sharp dimension-only rate intervals

Manuscript 12 proves that for order-m weakly infeasible SDPs, m>=2,

    E_m=2^(m-1)-1,      1/E_m<=a<=E_m.                (27)

The endpoints are attained by rational bounded-coefficient systems at every m. Substitution in (25)–(26) gives the following exact interval for the residual decay power gamma in r_k=Theta(k^(-gamma)):

    alternating projections:
        2^(-m) <= gamma <= 1/2-2^(-m),                (28)
    accelerated scheme (12):
        2^(-(m-1)) <= gamma <= 1-2^(-(m-1)).           (29)

Both endpoints in BOTH intervals are attained at every m. These are sharp bounds on all attained exponents, not a classification asserting that every number between them occurs.

### 7.1 Why the inherited envelope has the displayed dimension

For clarity, the proof dependency is quantitative, not merely a use of a conjectural singularity-degree bound. Manuscript 12 removes positive recession-support blocks until no PSD recession direction remains. There are at most m-1 nontrivial blocks; otherwise a reverse positive Schur construction would give exact feasibility. Each reverse partial-support step sends a Laurent exponent e to 2e+1, starting from zero, so an approximately feasible PSD path has trace O(delta^(-(2^(m-1)-1))). Applying this same construction to the normalized dual affine space {A*y:b.y=-1} and using the exact conic profile-duality identity gives the reverse lower bound R_b(delta)>=c delta^(-1/E_m). That proof handles arbitrary real coefficients and does not require a supplied recession chain as input to the algorithms here.

The algorithmic statements (25)–(26) depend only on (23); they remain valid independently of (27) if a radius exponent is supplied by another argument.

### 7.2 Explicit endpoint systems

Use indices 0,...,m-1. The fast-escape system is

    X00=0, X01=1,
    Xii-X0,i+1=0, 1<=i<=m-2.                         (30)

PSD zero-row propagation makes it infeasible. With epsilon>0 put

    u0=sqrt(epsilon),
    ui=epsilon^(-(2^(i-1)-1/2)), 1<=i<=m-1,
    X=uu^T.

Only X00=0 has residual epsilon; trace is Theta(epsilon^(-E_m)). The 2-by-2 principal minors, read successively along (30), give the matching lower bound. Thus a=E_m, and the algorithms have their SLOW residual endpoints (28)–(29):

    ordinary r_k=Theta(k^(-1/2^m)),
    accelerated r_k=Theta(k^(-1/2^(m-1))).             (31)

For the slow-escape system impose

    X_(m-1,m-1)=0, X01=-1/2,
    2X0j+X_(j-1,j-1)=0, 2<=j<=m-1,
    Xij=0, 1<=i<j<=m-1.                              (32)

Set d_j=t^(2^j-1), Xjj=d_j, X00=(m-1)/(4t),
X01=-1/2, and X0j=-d_(j-1)/2 for j>=2. The leaf block is diagonal positive and its Schur sum equals X00, so X>=0. Only the final diagonal equation is violated, by t^E_m, whereas trace is Theta(t^(-1)). The lower bound in (27) makes a=1/E_m. Thus (32) attains the FAST residual endpoints in (28)–(29).

The names fast and slow here refer to static trace escape, not algorithmic speed; their algorithmic ordering is reversed.

### 7.3 An elementary order-two leading constant

For (30) at m=2, every affine iterate is

    Z_k=[[0,1],[1,t_k]].

Let d_k=sqrt(t_k^2+4). Direct spectral projection gives the EXACT recurrence

    t_{k+1}=t_k+(d_k-t_k)^2/(4d_k).                   (33)

The increment is positive. A bounded monotone sequence would have a finite limit with positive increment, impossible; thus t_k->infinity. Since the increment is asymptotic to t_k^(-3),

    t_{k+1}^4-t_k^4 ->4,
    t_k~(4k)^(1/4),
    r_k=(d_k-t_k)/2~(4k)^(-1/4).                     (34)

This provides an elementary exact example independent of the general dynamic argument. More generally EVERY order-two weakly infeasible SDP has the Theta(k^(-1/4)) ordinary residual law and Theta(k^(-1/2)) accelerated law, by (27).

## 8. Practical consequences and invariances

### 8.1 Iteration powers

For a fixed instance, the first index at which r_k<=delta has order

    ordinary: Theta(delta^(-2(a+1))),
    accelerated: Theta(delta^(-(a+1))).               (35)

For the accelerated, potentially nonmonotone output this follows from the two-sided bounds for ALL sufficiently large k; the finitely many earlier positive residuals do not affect the delta->0 statement.

For (30), (35) becomes Theta(delta^(-2^m)) versus Theta(delta^(-2^(m-1))). This is a sharp iteration statement for the two specified exact-arithmetic methods. It is NOT an oracle lower bound for all algorithms or a polynomial-time impossibility result.

### 8.2 Fixed linear preconditioning cannot change these powers

Replace the Euclidean inner product by ANY fixed positive-definite inner product, using its orthogonal projections consistently. Distances and radii are equivalent to their original versions, so (20) has the same a. The squared-distance gradient is still 1-Lipschitz in that Hilbert norm. The proofs of Sections 2–5 therefore give exactly the same powers (21)–(22).

Equivalently, any fixed invertible linear change of coordinates of both sets can change constants and transients but not these asymptotic powers. In an SDP, fixed nonsingular congruences and fixed invertible data scalings likewise preserve a. This is NOT a statement about adaptive metrics, nonlinear transformations, facial reduction, adding unrestricted auxiliary variables, or using inconsistent metrics for the two projections.

### 8.3 Mixed conic feasibility and a dimension-free SOC case

For a product of PSD cones of orders d_j, h Lorentz cones of arbitrary dimensions >=3, and arbitrary finitely many nonnegative scalar cones, define

    B=sum_j(d_j-1)+h.

Manuscripts 15–16 give the weak-infeasibility envelope

    1/(2^B-1)<=a<=2^B-1, B>=1,

for a coercive positive cone gauge. Gauge and Euclidean norm are equivalent on the cone; the affine correction argument (24) works unchanged. Hence the residual powers satisfy

    ordinary: 2^(-(B+1))<=gamma<=1/2-2^(-(B+1)),
    accelerated: 2^(-B)<=gamma<=1-2^(-B).             (36)

With ONE nonpolyhedral Lorentz factor and any finite number of scalar factors, B=1 and necessarily a=1. Therefore EVERY weakly infeasible instance in this class has ordinary residual Theta(k^(-1/4)) and accelerated residual Theta(k^(-1/2)), independent of Lorentz dimension and number of linear constraints. If no nonlinear factor exists, a weakly infeasible finite polyhedral system is impossible.

### 8.4 Connection with the existing dual and representation results

The normalized approximate Farkas-certificate exponent from manuscript 12 is beta_dual=1/a. The ordinary residual power can therefore also be written

    gamma=beta_dual/[2(1+beta_dual)],

and acceleration doubles it. This relates primal size, approximate certificate size, and algorithmic dynamics without identifying an approximate certificate with a finite exact infeasibility proof.

The rational two-basis one-scale reduction of manuscript 11 preserves a by its two-sided minimum-trace profile bounds. Thus applying these algorithms to its centered lifted affine system preserves the corresponding asymptotic powers. It does not preserve trajectories, transient iteration counts, floating-point conditioning, or total cost per projection. The present proof does not use that reduction; this is a corollary linking the two parts of the programme.

## 9. Numerical diagnostics and reproducibility

The accompanying escape_dynamics/test_escape_dynamics.py uses only NumPy and Python. It implements PSD eigenvalue clipping and the affine orthogonal projection, both algorithms, and fixed-comparator checks of (5)/(14). The output DYNAMICS_RESULTS.json records 40,000 iterations for m=2 fast, m=3 fast, and m=3 slow, and scalar tests f(x)=(1+x)^(-p) on x>=0 for p=1/2,1,2,4.

For m=2 the observed residual tail slopes were approximately -0.25195 and -0.49991, compared with -1/4 and -1/2. For m=3 fast they were -0.12573 and -0.24995, compared with -1/8 and -1/4. For m=3 slow they were -0.38472 and -0.75118, compared with -3/8 and -3/4. Transients are visible and these slope fits do NOT establish the asymptotic theorems. The displayed algebraic proofs do.

No normalized comparator-energy violation was observed in the recorded tests. The maximum affine residual was below 2e-13. These are floating-point diagnostics, not exact numerical certificates, rank-uniform stability guarantees, or evidence of finite-time infeasibility detection.

## 10. Positioning, established inputs, and limits

Drusvyatskiy–Li–Wolkowicz (2017) connect alternating-projection rates for semidefinite feasibility to singularity degree through error bounds on nonempty intersections, also discussing attained displacement. Sremac's 2019 thesis, Section 4.1, explicitly distinguishes the weakly infeasible gap when discussing extensions of singularity degree. The result here supplies a different, real-valued invariant at infinity and exact two-sided residual AND size rates. It does not redefine the integer facial singularity degree, nor assert that every prior question about it is solved.

Recent work by Ochiai–Sekiguchi–Waki (2026) analyzes exact/tight rates for nontransversal affine/SOC INTERSECTIONS; this manuscript concerns disjoint sets at distance zero. Ji–Dudik–Schapire–Telgarsky (2020) relate gradient-descent and regularization directions for linear-predictor losses. The regularization statement here is about two-sided size/value powers, not a new discovery of all implicit-bias phenomena. Siegel–Wojtowytsch show arbitrary slow decay can occur for general convex nonattainment; the semialgebraic power profile is an additional, material restriction, so there is no contradiction.

All statements concern a fixed problem and exact projections/gradients. Constants and asymptotic thresholds may depend badly on that problem. Theorems do not supply a uniform floating-point stopping certificate, a polynomial-bit exact SDP solver, a leading-constant formula in every instance, or a lower bound for all first-order algorithms. Neither stochastic perturbations nor Douglas–Rachford, ADMM, arbitrary momentum/restart variants, or adaptive preconditioning are covered merely by naming them.

The mathematical arguments above resolve the precise rate problem stated here. Their historical novelty and the appropriate journal claim require careful comparison with existing work; no assertion of a recognized broad conjecture resolution or guaranteed acceptance is made.

## References

1. D. Drusvyatskiy, G. Li, H. Wolkowicz, A note on alternating projections for ill-posed semidefinite feasibility problems, Mathematical Programming 162 (2017), 537–548. DOI: 10.1007/s10107-016-1048-9. Author version: https://sites.math.washington.edu/~ddrusv/SDP_ill.pdf
2. S. Sremac, Error Bounds and Singularity Degree in Semidefinite Programming, University of Waterloo PhD thesis (2019), Section 4.1, printed page 30. https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/stefanphdthesisdec.pdf
3. H. Ochiai, Y. Sekiguchi, H. Waki, Convergence rate of alternating projection method for the intersection of an affine subspace and the second-order cone, Journal of Global Optimization 94 (2026), 539–567. DOI: 10.1007/s10898-025-01581-7.
4. Z. Ji, M. Dudik, R. E. Schapire, M. Telgarsky, Gradient descent follows the regularization path for general losses, COLT/PMLR 125 (2020), 2109–2136. https://proceedings.mlr.press/v125/ji20a.html
5. J. W. Siegel, S. Wojtowytsch, A qualitative difference between gradient flows of convex functions in finite- and infinite-dimensional Hilbert spaces, arXiv:2310.17610. https://arxiv.org/html/2310.17610v1
6. B. F. Lourenco, M. Muramatsu, T. Tsuchiya, A structural geometrical analysis of weakly infeasible SDPs, JORSJ 59 (2016), 241–257. DOI: 10.15807/jorsj.59.241. The qualitative recession decomposition is an established input to the quantitative profile proof in project manuscript 12.
7. Project manuscripts 12, 15–16, and 11 at the parent snapshot stated above: sharp escape envelope, mixed-cone envelope, and optional normal-form invariance, respectively. These are identified dependencies, not external peer-reviewed results.

The classical proximal and accelerated energy arguments are proved directly in Sections 2–3, rather than claimed as new algorithm inventions. The one-variable semialgebraic growth principle is used only to guarantee the static power profile.
