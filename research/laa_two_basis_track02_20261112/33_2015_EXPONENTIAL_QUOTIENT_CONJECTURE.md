# Milestone 33 — A proof of the 2015 exponential-quotient proximal conjecture

Date: 2026-11-14.
Repository: Harman6139/Posterity-Files.
Branch: laa-track02-gptpro-analytic-frontier-20261112.
Parent snapshot: 606fb27376ac0bb68fdaa319895483cc7f1bfec9.

## Historical statement and limits of the priority claim

Heinz H. Bauschke, Graeme R. Douglas, and Walaa M. Moursi explicitly conjectured the directional limit below in Example 2.10, equations (18)–(19), of *On a result of Pazy concerning the asymptotic behaviour of nonexpansive mappings*. The arXiv v1 is dated May 15, 2015. The article appeared in Journal of Fixed Point Theory and Applications 18 (2016), 297–307, DOI 10.1007/s11784-015-0278-4. The authors wrote: “however, we do not have a proof for this conjecture.”

Their specific example is F(x,y)=exp(x)/y for y>0, extended by +infinity elsewhere, and T=prox_F. They conjectured T^k(z)/||T^k(z)|| -> (-1,0). Section 2 proves exactly this claim for every initial z in R^2, and in fact every fixed positive proximal parameter. No restriction on the initial second coordinate is imposed.

This is NOT the general cosmic-convergence conjecture. The unrestricted conjecture was disproved by Ernest K. Ryu in *Cosmic divergence, weak cosmic convergence, and fixed points at infinity* (2018; arXiv:1709.02838). That counterexample does not contradict the affirmative statement for this specific F.

A targeted search on 2026-11-14 located the original conjecture but no later proof of this particular example. Sources checked included the original versions, Ryu's paper, Gutierrez–Karlsson (2021), and the original first author's publication list through 2026. This establishes the documented age and original open statement; it DOES NOT certify that no subsequent proof or general theorem settles it. Do not advertise historical priority or an uninterrupted eleven-year open status without additional confirmation. The mathematical proof below is independent of that bibliographic question and of all earlier project manuscripts.

## 1. The result

For lambda>0 define

    prox_(lambda F)(u,v)
       = argmin_(x in R,y>0) [exp(x)/y + ((x-u)^2+(y-v)^2)/(2lambda)].

Let z_(k+1)=(x_(k+1),y_(k+1))=prox_(lambda F)(z_k) from ANY z_0 in R^2.

**Theorem A.** Every iterate after the initial point has y_k>0, and

    x_k -> -infinity,
    y_k -> +infinity,
    z_k/||z_k|| -> (-1,0).                                    (1)

The first and third conclusions, which include the conjecture in its full stated scope, follow just from the first-order equations and a decreasing quadratic phase. The second conclusion follows as part of the stronger asymptotics below.

**Theorem B.** With natural logarithms, there is a finite constant H_infinity, depending on the initial point and lambda, such that

    H_k := x_k+y_k^2/2 -> H_infinity,
    lambda k F(z_k) -> 1,                                    (2)

    x_k = -log k + (1/2)log log k + (1/2)log 2
                              -log lambda + o(1),             (3)

    y_k^2 = 2log k-log log k+2log lambda-log 2
                              +2H_infinity+o(1).              (4)

In particular x_k ~ -log k and y_k ~ sqrt(2log k). The directional error has the precise constant

    sqrt(log k) ||z_k/||z_k|| - (-1,0)|| -> sqrt(2).            (5)

The coordinate increments satisfy

    x_k-x_(k+1) ~ 1/k,
    y_(k+1)-y_k ~ 1/[k sqrt(2log k)].                          (6)

These are exact asymptotic claims for the fixed-parameter iteration, not numerical fits, variable-step claims, or finite-precision guarantees.

### Well-posedness, including starts outside the domain

The extended-real function F is proper and lower semicontinuous. On y>0 its Hessian is

    Hess F(x,y) = exp(x)/y^3 * [[y^2,-y],[-y,2]],

which is positive definite, since the inner matrix has positive first leading minor and determinant y^2. Its domain is convex, so F is convex. At any finite point of the boundary y=0 the value tends to +infinity from inside the domain. The quadratic term in each proximal objective makes it coercive and strongly convex. Its lower-semicontinuous extension therefore has a unique minimizer of finite value, necessarily with y>0. This holds even when the input second coordinate is nonpositive.

## 2. An elementary proof of the exact 2015 conjecture

Work from k>=1, so both y_k and y_(k+1) are positive. First-order optimality gives

    A_k := x_k-x_(k+1) = lambda exp(x_(k+1))/y_(k+1) > 0,
    B_k := y_(k+1)-y_k = lambda exp(x_(k+1))/y_(k+1)^2 > 0.
                                                                  (7)

Thus x_k decreases, y_k increases, and

    A_k=y_(k+1) B_k.                                       (8)

For H_k=x_k+y_k^2/2,

    H_(k+1)-H_k
      = -A_k + [y_(k+1)^2-y_k^2]/2
      = -y_(k+1) B_k + [2y_(k+1)B_k-B_k^2]/2
      = -B_k^2/2.                                         (9)

Consequently H_k<=H_1 and

    0<y_k^2<=2H_1-2x_k.                                   (10)

If x_k were bounded below, it would have a finite limit by monotonicity. Equation (10) would bound y_k, which would also have a finite positive limit by monotonicity and y_1>0. But (7) would then give

    A_k -> lambda exp(x_infinity)/y_infinity > 0,

contradicting convergence of x_k. Hence x_k -> -infinity. From (10),

    0< y_k/|x_k| <= sqrt(2H_1-2x_k)/|x_k| -> 0.

As x_k is eventually negative, normalization now gives

    (x_k,y_k)/sqrt(x_k^2+y_k^2) -> (-1,0).

This proves the original Example 2.10 conjecture for all initial points; setting lambda=1 is exactly its stated operator. No cosmic-convergence theorem, definability assumption, limiting ODE, experiment, or conjectural prior project result has been used. QED.

## 3. The finite limiting phase

The proximal minimizer can be compared to the previous point, whose value is finite for k>=1:

    F(z_(k+1)) + (A_k^2+B_k^2)/(2lambda) <= F(z_k).

Because F>=0, telescoping gives

    sum_(k>=1)(A_k^2+B_k^2) <= 2lambda F(z_1)<infinity.     (11)

In particular A_k,B_k ->0, and (9) yields the finite limit

    H_infinity = H_1-(1/2)sum_(k>=1) B_k^2.                (12)

Combining x_k -> -infinity with y_k^2=2H_k-2x_k proves y_k -> +infinity.

## 4. Reciprocal objective and exact leading constants

Set r_k=exp(-x_k) and G_k=r_k y_k=1/F(z_k). By (7),

    r_(k+1)=r_k exp(A_k),
    A_k=lambda/[r_(k+1)y_(k+1)],
    B_k=lambda/[r_(k+1)y_(k+1)^2].

The reciprocal objective has the exact increment

    G_(k+1)-G_k
       = y_(k+1)(r_(k+1)-r_k)+r_k B_k
       = lambda[(1-exp(-A_k))/A_k
                         + exp(-A_k)/y_(k+1)^2].           (13)

Since A_k->0 and y_k->infinity, this increment tends to lambda. Cesaro summation gives

    G_k/k -> lambda,

which proves the objective law in (2).

Let u_k=-x_k ->infinity. Equations (12)–(13) imply

    u_k+log y_k=log k+log lambda+o(1),
    y_k^2=2u_k+2H_infinity+o(1).

Therefore

    u_k+(1/2)log u_k+(1/2)log 2
         =log k+log lambda+o(1).                         (14)

Because log u_k=o(u_k), (14) first gives u_k/log k ->1. Hence log u_k=log log k+o(1). Substituting again into (14) gives (3); using y_k^2=2H_k-2x_k gives (4).

Write q_k=y_k/(-x_k), which tends to zero. Then

    z_k/||z_k||=(-1,q_k)/sqrt(1+q_k^2),
    ||z_k/||z_k||-(-1,0)|| ~ q_k.

Equations (3)–(4) give sqrt(log k) q_k ->sqrt(2), proving (5). Finally, A_k=lambda F(z_(k+1))~1/k, and B_k=A_k/y_(k+1), proving (6). QED, Theorem B.

## 5. A multidimensional extension, with its own complete proof

The same mechanism covers a fixed finite collection of positive powers. Let d>=1, a>0 and q_i>0. Define

    F_(a,q)(x,y)=exp(a x) product_(i=1)^d y_i^(-q_i)
                        when every y_i>0,
               =+infinity otherwise.

For any lambda>0, run its Euclidean proximal iteration from any point of R^(d+1). Put Q=sum_i q_i and

    C_star=product_i (2q_i/a^2)^(q_i/2).

**Theorem C.** The full normalized orbit tends to (-1,0,...,0). More precisely,

    lambda a^2 k F_(a,q)(z_k) ->1,
    x_k=-(1/a)log k+(Q/(2a))log log k
                +[log C_star-log(lambda a^2)]/a+o(1),     (15)
    y_(i,k) ~ sqrt((2q_i/a^2)log k).

Also

    sqrt(log k)||z_k/||z_k||-(-1,0,...,0)|| ->sqrt(2Q).    (16)

For each i there is a finite H_(i,infinity) with

    x_k+(a/(2q_i))y_(i,k)^2 -> H_(i,infinity).             (17)

### Proof

On the positive domain, put v=(a,-q_1/y_1,...,-q_d/y_d). The Hessian is

    F_(a,q) [v v^T+diag(0,q_1/y_1^2,...,q_d/y_d^2)],

which is positive definite. Extension and proximal well-posedness follow exactly as in Section 1.

Let A_k=x_k-x_(k+1) and B_(i,k)=y_(i,k+1)-y_(i,k). The optimality equations are

    A_k=lambda a F_(a,q)(z_(k+1))>0,
    B_(i,k)=lambda q_i F_(a,q)(z_(k+1))/y_(i,k+1)>0.

Hence y_(i,k+1)B_(i,k)=(q_i/a)A_k, and direct expansion gives

    H_(i,k+1)-H_(i,k)=-(a/(2q_i))B_(i,k)^2.

If x_k were bounded below, all y_(i,k) would be bounded by these phase inequalities; their positive monotone limits would force A_k to have a positive limit, a contradiction. Therefore x_k->-infinity, and the phase upper bounds already imply all y_(i,k)/|x_k|->0, proving the directional limit.

The proximal descent inequality implies square summability of all increments, so every phase has a finite limit. Equation (17) gives y_(i,k)->infinity for every i.

Set G_k=1/F_(a,q)(z_k). Then A_k=lambda a/G_(k+1), and

    G_k/G_(k+1)=exp(-a A_k)
                     product_i (1-B_(i,k)/y_(i,k+1))^(q_i).

Here

    [B_(i,k)/y_(i,k+1)]/A_k
           =q_i/[a y_(i,k+1)^2] ->0.

Since d and the q_i are fixed and A_k->0, the product is 1+o(A_k). Thus

    1-G_k/G_(k+1)=a A_k+o(A_k),
    G_(k+1)-G_k ->lambda a^2.

This proves the reciprocal-objective law in (15). Put u_k=-a x_k. From (17),

    y_(i,k)^2=(2q_i/a^2)(u_k+a H_(i,infinity))+o(1).

Taking logarithms of G_k~lambda a^2 k gives

    u_k+(Q/2)log u_k+log C_star
                   =log k+log(lambda a^2)+o(1).

As in Section 4, u_k~log k and substitution gives (15). The squared transverse-to-longitudinal norm ratio is asymptotic to 2Q/log k, proving (16). QED.

This extension is a result for the stated exponential-product family. It is not a claim about every convex function or every fixed-point-free proximal map. Its historical priority is not independently certified either.

## 6. Provenance, reproducibility, and correct reporting

The original conjecture and its age are directly documented. The proof above establishes its exact mathematical conclusion, not merely a special starting point or a restriction replacing a broader original statement. It also proves quantitative conclusions the conjecture did not ask for.

The sources checked do not establish that this example was still unresolved immediately before this derivation. Failure to find a subsequent proof is not evidence strong enough for an unqualified priority claim. This file deliberately distinguishes a proof of a historically stated conjecture from a certified first solution of a still-open problem. The latter status remains unverified. The general cosmic-convergence conjecture is known to be false and is not being claimed resolved positively.

The accompanying check_proximal_example.py numerically solves each proximal step by a scalar equation and checks (7), (9), and proximal descent on starts both inside and outside the domain. NUMERICAL_ILLUSTRATIONS.json records 20,000-step trajectories for four starting-point/step-size pairs. They are illustrations, not premises in any proof. Logarithmic convergence is slow, so the finite snapshots need not be close to their limiting constants.

No independent external refereeing, author confirmation of current open status, or journal acceptance prediction is claimed. Nothing in this note depends on the accuracy of the preceding thirty-two research milestones.

## References

1. H. H. Bauschke, G. R. Douglas, W. M. Moursi. On a result of Pazy concerning the asymptotic behaviour of nonexpansive mappings. arXiv:1505.04129v1, May 15, 2015, Example 2.10 and equations (18)–(19). Journal of Fixed Point Theory and Applications 18 (2016), 297–307. DOI: 10.1007/s11784-015-0278-4.
   https://arxiv.org/html/1505.04129v1
2. E. K. Ryu. Cosmic divergence, weak cosmic convergence, and fixed points at infinity. Journal of Fixed Point Theory and Applications 20 (2018), article 109. arXiv:1709.02838v2. DOI: 10.1007/s11784-018-0592-8.
   https://arxiv.org/html/1709.02838v2
3. A. W. Gutierrez and A. Karlsson. Comments on the cosmic convergence of nonexpansive maps. Journal of Fixed Point Theory and Applications 23 (2021), article 59. DOI: 10.1007/s11784-021-00896-8.
   https://link.springer.com/article/10.1007/s11784-021-00896-8
4. H. H. Bauschke. Publication list, accessed 2026-11-14. Used as a bibliographic cross-check, not as proof of nonexistence of a later solution.
   https://bauschke.ca/publications
