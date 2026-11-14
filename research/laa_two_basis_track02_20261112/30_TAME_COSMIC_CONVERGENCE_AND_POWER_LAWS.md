# Milestone 30 — Cosmic convergence of tame nonexpansive dynamics

Date: 2026-11-13 (America/Toronto).
Repository: Harman6139/Posterity-Files.
Branch: laa-track02-gptpro-analytic-frontier-20261112.
Parent snapshot: eb3b8b9aceb29d7a534216b46a4855524d0693ad.

## Status and relationship to the named question

The cosmic-convergence question asks whether an orbit escaping to infinity has a limiting normalized direction. Bauschke–Douglas–Moursi proposed a general conjecture for nonexpansive maps. Ryu supplied a counterexample, even for a firmly nonexpansive map on R^2. The unrestricted conjecture is therefore FALSE and is not being claimed solved positively here.

This manuscript proves an affirmative TAME version: every fixed-point-free nonexpansive self-map of a nonempty closed convex definable set in finite dimension has a common cosmic limit, when the map and set are definable in one o-minimal expansion of the real field. In the semialgebraic case it proves a common exact leading vector and rational growth power, and computes their relation to a discounted fixed-point path. The actual orbit need not be definable.

The proof uses only contraction, one-variable tame regularity, and an approximate-orbit comparison. It is independent of project manuscripts 01–29. The power-profile corollary reconnects it with 28, but is reproved here. Classical antecedents include Pazy's linear drift theorem and the definable discounted-curve arguments of Bewley–Kohlberg, Neyman, and Bolte–Gaubert–Vigeral. The latter's Theorem 3 establishes the limit of T^k(x)/k and an error estimate, not the nonzero first sublinear leading term asserted below. A targeted comparison is not an exhaustive historical novelty certification.

## 1. Setup and main theorem

Let C be a nonempty closed convex subset of R^d, definable in a fixed o-minimal expansion of the real field. Let T:C->C be definable and nonexpansive in the Euclidean norm:

    ||T(x)-T(y)|| <= ||x-y||.

Assume Fix(T) is empty. Fix an anchor a in C. For t>0 let z(t) be the unique solution of

    z(t) = [a+t T(z(t))]/(1+t),
    equivalently T(z(t))-z(t)=[z(t)-a]/t.                 (1)

### Theorem A — tame cosmic convergence

There is a unit vector v, independent of a and of the initial point x, such that

    T^k(x)/||T^k(x)|| -> v      for every x in C.          (2)

All these orbits tend to infinity in norm. The same v is

    lim_(t->infinity) [z(t)-a]/||z(t)-a||.               (3)

More precisely, put r(t)=||z(t)-a||. For sufficiently large t, r is C^1, strictly increasing with positive derivative, and has a C^1 inverse t=t(r). Define

    gamma(r)=z(t(r))-a,    delta(r)=r/t(r).

For any sufficiently large r_0 define

    r_(k+1)=r_k+delta(r_k).                              (4)

Then r_k->infinity and, for every x in C,

    T^k(x)=a+gamma(r_k)+o(r_k)=r_k v+o(r_k).              (5)

Thus a single scalar recursion obtained from the discounted path determines the first asymptotic scale of every orbit.

### Theorem B — exact semialgebraic power law

If C and T are semialgebraic, there are a rational exponent p in (0,1] and a nonzero vector c such that

    z(t)-a = c t^p + o(t^p).                            (6)

They are independent of a. For every initial x in C,

    T^k(x) = p^(-p) c k^p + o(k^p).                     (7)

In fact some eta>0 gives an error O(k^(p-eta)). No uniform lower bound on eta or uniform asymptotic onset is asserted.

If inf_C ||x-Tx||=0, then 0<p<1. If that infimum is positive, p=1. The normalized direction is c/||c|| in both cases.

If definability is only assumed in a polynomially bounded o-minimal structure, the same leading-power conclusion holds with a real positive p in its field of exponents; rationality is not asserted outside the semialgebraic setting. The general definable theorem A also covers logarithmic and other non-power growth, without asserting (6) there.

## 2. The discounted path exists, is tame, and diverges

For fixed t>0 the map x->[a+tT(x)]/(1+t) maps C into C by convexity and is a contraction of constant t/(1+t). Since C is complete it has exactly one fixed point. Its graph is defined by (1), so z(t) is definable.

For t in a compact positive interval, the contraction equation also proves continuity in t. Explicitly, comparing z(t) and z(s), with s fixed, gives

    ||z(t)-z(s)|| <= |t-s| ||T(z(s))-z(s)||.

To verify this, subtract z(t)+t(z(t)-Tz(t))=a and z(s)+s(z(s)-Tz(s))=a, or rearrange the contraction at parameter t with z(s) as comparison point. The resulting bound is local, which is all that is needed for continuity.

Nonexpansiveness gives the linear bound

    ||z(t)-a|| <= t ||T(a)-a||.                        (8)

Indeed multiply the fixed-point comparison with T(a) by 1+t and cancel the t||z(t)-a|| term.

If a sequence t_j->infinity had bounded z(t_j), take a convergent subsequence in the closed set C. By (1) the displacements tend to zero. Continuity of T then gives a fixed point, a contradiction. Hence r(t)->infinity.

One-variable definable regularity makes z and r eventually C^2 (or any prescribed finite differentiability order) and r eventually strictly increasing. Its derivative is eventually positive: a definable zero set of r' cannot have infinitely many isolated points, and r cannot have an eventual interval with identically zero derivative. Thus the stated inverse exists on a tail.

The vector gamma(r)/r is definable and bounded, so each coordinate has a limit by the monotonicity theorem. Let v be the vector of limits. Since ||gamma(r)/r||=1, ||v||=1.

The derivative gamma_i'(r) is also definable and therefore has a limit in R union {+/-infinity}. It cannot tend to either infinity, because |gamma_i(r)|<=r: integrating an eventually arbitrarily large positive or negative derivative contradicts that linear bound. Its finite derivative limit equals lim gamma_i(r)/r by elementary integration. Therefore

    gamma(r)/r -> v,       gamma'(r) -> v.              (9)

THIS derivative conclusion is the key use of tameness. Merely knowing convergence of gamma(r)/r for an arbitrary oscillatory curve would not justify it.

Finally, (8) gives

    0<delta(r)<=||T(a)-a||=:M.

Here M>0 because a is not fixed. The function delta is continuous and positive on the tail.

## 3. An asymptotically exact orbit on the path

Let r_k obey (4), and put y_k=a+gamma(r_k) in C. The scalar sequence increases. If it had a finite limit r_bar, continuity and positivity of delta at r_bar would contradict r_(k+1)-r_k->0. Hence r_k->infinity.

Equation (1) says EXACTLY

    T(y_k)=y_k+delta(r_k) gamma(r_k)/r_k.               (10)

On the other hand,

    y_(k+1)-y_k = integral_(r_k)^(r_k+delta(r_k)) gamma'(s) ds.

By (9), uniformly over intervals of length at most M,

    e_k:=y_(k+1)-T(y_k),
    ||e_k|| <= delta(r_k) omega(r_k),                  (11)

where omega(r)->0. For example take

    omega(r)=sup_(s>=r)||gamma'(s)-v||+||gamma(r)/r-v||.

The supremum is finite on a sufficiently large tail because gamma' converges.

Now x_k=T^k(x_0) satisfies, by nonexpansiveness,

    ||x_k-y_k|| <= ||x_0-y_0||+sum_(j<k)||e_j||.        (12)

Since sum_(j<k)delta(r_j)=r_k-r_0, the right-hand sum is o(r_k). To see this explicitly, for any epsilon>0 choose J with omega(r_j)<=epsilon for j>=J. The finite initial sum is constant, and the remaining sum is at most epsilon(r_k-r_J). Divide by r_k and let epsilon decrease to zero.

Combining (9), (11), and (12) yields (5), and hence (2). In particular it proves divergence of the actual iterates; no separate theorem claiming divergence is being assumed.

For different initial points, nonexpansiveness gives ||T^k x-T^k y||<=||x-y||, so they have the same scale and direction. For two anchors a,b, their discounted points obey ||z_a(t)-z_b(t)||<=||a-b||, by subtracting the two contraction equations. Thus the direction in (3), and the leading coefficient/exponent in (6) when applicable, are anchor independent. QED, Theorem A.

## 4. Exact power, coefficient, and a quantitative remainder

For a semialgebraic curve, one-variable Puiseux growth on a tail gives a nonzero first vector term (6). Divergence gives p>0 and (8) gives p<=1. The exponent p is rational. Eventual differentiation of the convergent Puiseux expansions gives

    z'(t)=p c t^(p-1)+o(t^(p-1)).                     (13)

Set t_k=t_0+k/p and y_k=z(t_k), for t_0 sufficiently large. Then

    y_(k+1)-y_k = c t_k^(p-1)+o(t_k^(p-1)),
    T(y_k)-y_k = [z(t_k)-a]/t_k
                 =c t_k^(p-1)+o(t_k^(p-1)).          (14)

The local orbit defect is o(k^(p-1)). Its sum through k is o(k^p) because p>0. The comparison (12) therefore gives

    T^k(x)=z(t_0+k/p)+o(k^p)
          =p^(-p)c k^p+o(k^p).

For the stated polynomial remainder, Puiseux expansion supplies kappa>0 such that, after subtracting the first term, z(t)-a=ct^p+O(t^(p-kappa)), with the corresponding derivative bound. Taking any eta with 0<eta<min(kappa,p,1) absorbs both the finite-difference O(t^(p-2)) error and the summation logarithm at a zero exponent. Thus the cumulative defect and first-term remainder are O(k^(p-eta)).

No regularity of T beyond nonexpansiveness and definability is used; the actual orbit is not asserted semialgebraic.

For zero infimal displacement, comparison with an arbitrary u in C gives

    ||z(t)-a|| <= 2||u-a||+t||T(u)-u||.               (15)

Divide by t, take limsup, and then take displacements tending to zero. It follows that r(t)/t->0, hence p<1. Conversely positive infimal displacement gives r(t)/t=||Tz(t)-z(t)|| bounded below, forcing p=1. This proves the dichotomy without appealing to Pazy's theorem. QED, Theorem B.

## 5. Exact relationship to the static escape exponent

Assume the zero-displacement case, and define

    R(epsilon)=min{||u-a||:u in C,||u-Tu||<=epsilon}.

If C,T are semialgebraic, this is finite, attained, semialgebraic, and diverges. Thus

    R(epsilon)=Theta(epsilon^(-a0)), a0 rational positive.

The exponent in Theorem B is exactly

    p=a0/(a0+1).                                      (16)

Proof: (15), with a radius minimizer at epsilon=t^(-1/(a0+1)), gives r(t)=O(t^(a0/(a0+1))). Conversely z(t) is itself a residual-r(t)/t point, so R(r(t)/t)<=r(t). Since r(t)/t->0, the lower profile inequality yields r(t)>=c t^(a0/(a0+1)). Comparing with (6) proves (16).

This proves a STATE-GROWTH result for plain Picard iteration from the profile, not a universal last-iterate displacement rate. The latter does not follow, as Section 9 illustrates.

## 6. Relaxation schedules and errors

In the semialgebraic setting let theta_k be ANY sequence in [0,1], with physical time

    tau_k=sum_(j<k)theta_j ->infinity.

The variable-relaxation iteration

    x_(k+1)=(1-theta_k)x_k+theta_k T(x_k)

satisfies

    x_k=p^(-p)c tau_k^p+o(tau_k^p).                    (17)

The schedule need not be definable or converge. Each relaxed map is nonexpansive and maps C into C. Compare it to y_k=z(t_0+tau_k/p). The derivative asymptotic (13), uniformly on increments of length at most 1/p, gives a local defect o(theta_k(t_0+tau_k)^(p-1)). Its sum is o(tau_k^p) by comparison with the integral of s^(p-1); the bounded mesh suffices. The same telescoping proof gives (17).

If errors e_k are added and iterates remain in C, (17) still holds provided

    sum_(j<k)||e_j||=o(tau_k^p).                       (18)

This is a sufficient accumulated-error condition, not a claim that fixed rounding errors always meet it. The proof adds their norms to (12).

For constant relaxation theta in (0,1], (17) reads

    x_k=(theta/p)^p c k^p+o(k^p).

Thus a constant relaxation changes the first coefficient in the predictable physical-time way but not the exponent or cosmic direction.

## 7. Anchoring: the same direction and an explicit leading coefficient

For fixed gamma>=0 run, with a in C,

    x_(k+1)=[gamma a+(k+1)T(x_k)]/(k+1+gamma).          (19)

Gamma=0 is ordinary Picard iteration. Gamma=1 is the Halpern anchor used in project manuscript 28. Then

    x_k=(p+gamma)^(-p)c k^p+o(k^p).                    (20)

Proof: compare to y_k=z(t_0+k/(p+gamma)). At y_k, the increment of the update in (19) is

    [(k+1)/((k+1+gamma)t_k)-gamma/(k+1+gamma)](y_k-a).

Its leading coefficient is p/k times (y_k-a), exactly matching y_(k+1)-y_k by (13). The defect is o(k^(p-1)). Each update has Lipschitz constant at most one, so summation as above proves (20). The finitely many initial steps have no effect.

In particular anchoring preserves the leading direction and growth exponent, but changes the norm coefficient by (p/(p+gamma))^p compared with the ordinary orbit. This comparison concerns STATES. It is not a claim that all these methods have identical last-displacement rates.

## 8. Definable continuous dynamics

For the globally Lipschitz vector field T-I on R^d, its ODE x'=T(x)-x is contractive because I-T is monotone. In the semialgebraic fixed-point-free case,

    x(t)=p^(-p)c t^p+o(t^p).                           (21)

Indeed y(t)=z(t_0+t/p) has y'-(Ty-y)=o(t^(p-1)). Monotonicity yields d||x-y||/dt <= ||y'-(Ty-y)|| wherever the norm is differentiable, with the usual continuous extension at a zero distance. Integration gives o(t^p). This is the same leading vector as the unrelaxed discrete iteration at physical time k.

For a closed convex domain C the forward invariance and corresponding flow existence require the usual viability argument; (21) is asserted here for full R^d to avoid silently importing that extension.

## 9. Examples, sharp scope, and what is NOT inferred

### Every rational power occurs

For p in Q intersect (0,1], define on [0,infinity)

    T_p(x)=(x^(1/p)+1)^p.

Its derivative for x>0 is (x^(1/p)/(x^(1/p)+1))^(1-p), between zero and one; it is continuous and nonexpansive at zero. It has no fixed point, is semialgebraic, and

    T_p^k(x)=(x^(1/p)+k)^p.

Its discounted path has c=p^p, consistent with (7). Extending T_p to x<0 by the constant one gives a nonexpansive full-line example.

### Logarithmic growth is covered by theorem A

T(x)=x+1/(1+exp(x)) is definable in R_exp, strictly increasing, and has derivative in [3/4,1]. It has no fixed point. Theorem A applies, though no positive power p describes its logarithmic orbit growth. On a product of such coordinates with different exponential scales the conclusion likewise fixes a common normalized direction.

### Cosmic convergence is NOT last-displacement convergence

On R^2 take

    T(x,y)=(sqrt(max(x,0)^2+1),-y).

It is semialgebraic, nonexpansive and fixed-point free. From x>=0,

    T^k(x,y)=(sqrt(x^2+k),(-1)^k y).

The cosmic limit is (1,0), exactly as the theorem predicts. But for y!=0 the displacement norm does not tend to zero. Thus a state expansion cannot be differentiated termwise along an arbitrary discrete orbit to assert a residual expansion. This example is not averaged/firmly nonexpansive; no blanket last-residual claim is made even for narrower classes without a separate proof.

The theorem is finite dimensional. It is not asserted for arbitrary infinite-dimensional Hilbert spaces, arbitrary oscillatory nondefinable maps, or expanding maps. It does not restore the already disproved unrestricted cosmic conjecture.

## 10. The discrete theorems also hold in every finite-dimensional norm

Theorems A and B, their relaxation/anchor versions, and the classification of semialgebraic growth powers remain valid when T is nonexpansive for ANY fixed norm ||.||_* on R^d. The norm itself need not be definable; definability is required only of C and T.

Here are the changes to the proof. Solve (1) by contraction in ||.||_*. Use the Euclidean radius r(t)=||z(t)-a||_2 for the definable reparametrization. Norm equivalence gives r(t)<=M_* t for a fixed constant, and does not affect divergence. The arguments gamma(r)/r->v and gamma'(r)->v are purely Euclidean statements about the definable curve. Measure the orbit defects and the comparison sum (12) in ||.||_*, where T is nonexpansive. Norm equivalence preserves the o(r_k) bound and every o(k^p) bound. All leading vector coefficients remain exactly the same because the comparison is asymptotically smaller than the leading term, not merely bounded by an equivalent norm. Anchor independence likewise follows in ||.||_*.

The continuous monotonicity argument in Section 8 is stated in its original Euclidean setting. No additional arbitrary-norm flow theorem is needed for the discrete extension.

This extension includes, for example, definable maps nonexpansive in the maximum norm, as encountered in dynamic programming. It is not a claim that all such maps are fixed-point free, or that a particular game has a new value theorem. Classical linear-average limits for definable nonexpansive maps are explicitly distinguished from the first NONZERO unnormalized term here.

## 11. Prior work and unresolved directions

1. H. H. Bauschke, G. R. Douglas, W. M. Moursi, On a result of Pazy concerning the asymptotic behaviour of nonexpansive mappings, J. Fixed Point Theory Appl. 18 (2016), 297–307. Original conjectural context.
2. E. K. Ryu, Cosmic divergence, weak cosmic convergence, and fixed points at infinity, J. Fixed Point Theory Appl. 20 (2018), article 109; arXiv:1709.02838v2. The unrestricted conjecture is false even for a proximal/firmly nonexpansive example on R^2. https://arxiv.org/html/1709.02838
3. A. W. Gutierrez, A. Karlsson, Comments on the cosmic convergence of nonexpansive maps, J. Fixed Point Theory Appl. 23 (2021), article 59, DOI 10.1007/s11784-021-00896-8. Further scope corrections and context.
4. J. Bolte, S. Gaubert, G. Vigeral, Definable zero-sum stochastic games, Mathematics of Operations Research (2015); arXiv:1301.1967v2, Theorem 3. Discounted paths and one-variable definable regularity; linear normalized orbit convergence and polynomial error estimates. https://arxiv.org/html/1301.1967
5. A. Pazy, Asymptotic behavior of contractions in Hilbert space, Israel J. Math. 9 (1971), 235–240. Linear drift antecedent.

The initial search also considered the nonsmooth slope-determination conjecture in Daniilidis–Salas–Tapia-Garcia, arXiv:2504.07259. That DIFFERENT conjecture was not resolved; it is not a premise or consequence of this manuscript. The result actually proved here is Theorems A–B and their stated consequences.

No claim is made that editors cannot reject a manuscript, that this exact tame strengthening is historically unprecedented, or that a published open conjecture in its unrestricted form has been settled by a restriction. The proof addresses a broad, explicitly stated positive version of the cosmic-convergence question.
