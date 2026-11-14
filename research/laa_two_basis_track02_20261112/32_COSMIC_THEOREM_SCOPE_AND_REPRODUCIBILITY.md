# Current theorem packet — tame cosmic convergence and common leading trajectories

Date: 2026-11-13 (America/Toronto).
Branch: laa-track02-gptpro-analytic-frontier-20261112.
Parent: eb3b8b9aceb29d7a534216b46a4855524d0693ad.

## Principal result

Manuscript 30 proves that every fixed-point-free definable nonexpansive self-map of a finite-dimensional closed convex definable set has a common cosmic direction: every orbit divided by its norm converges to the same unit vector. Definability means in one fixed o-minimal expansion of the real field; semialgebraic maps are included. No orbit is presumed definable. The discrete result holds for every fixed norm in which the map is nonexpansive.

For semialgebraic data, the discounted fixed point

    z(t)=[a+t Tz(t)]/(1+t)

has a first Puiseux term c t^p, where c!=0 and p is rational in (0,1]. Every plain orbit satisfies

    T^k(x)=p^(-p)c k^p+o(k^p).

The leading coefficient and exponent are independent of initial point and anchor. Every rational power in (0,1] occurs already in one dimension. Zero infimal displacement corresponds to p<1. General o-minimal definability also gives cosmic convergence without a power assumption, via the explicit scalar radius clock in the proof.

The central insight is to reparametrize the discounted path by its radius. Tameness forces both its normalized position and its radial derivative to tend to one vector. One step of the map is then shadowed by a short forward step along this curve, with accumulated defect little-o of the distance escaped. Nonexpansiveness transfers that leading direction to every actual orbit. This is a complete proof, not a numerical pattern.

## Stronger consequences in 31

- Semialgebraic maximal-monotone resolvents, proximal iterations, and strong monotone-flow trajectories have the SAME leading vector after the explicit physical-time change. For a convex objective with globally Lipschitz gradient, stable-step gradient descent shares it. Variable bounded positive proximal steps and arbitrary bounded gradient-step schedules with divergent total time are covered.
- Plain, UNANCHORED Douglas–Rachford on every weakly infeasible SDP has a unique direction and an exact rational state-growth power. Its PSD shadow has a nonzero leading PSD recession direction H in ker A.
- If the source minimum-trace profile has exponent a, the state exponent is p=a/(a+1). This relation is proved from approximate comparator bounds and the exact DRS profile identity, not from the earlier claimed sharp dimensional envelope.
- Halpern-type anchoring with parameter gamma changes the first state coefficient from p^(-p)c to (p+gamma)^(-p)c but not the direction or power.
- The elementary 2-by-2 weakly infeasible system yields exact constants sqrt(2) for plain DRS and sqrt(2/3) for Halpern, multiplying sqrt(k) I_2.

## What is classical and what is actually claimed

The unrestricted cosmic-convergence conjecture was DISPROVED by Ryu, even for firmly nonexpansive maps. The affirmative theorem here requires tameness. It does not repair the unrestricted conjecture by ignoring that counterexample.

Pazy/Crandall–Pazy linear drift, Minty resolvents, one-variable definable regularity, semialgebraic Puiseux expansions, and discounted-path arguments are classical. Bolte–Gaubert–Vigeral establish linear-average asymptotics for definable nonexpansive operators; manuscript 30 identifies a NONZERO first sublinear vector and its exact relation to the discounted curve. Continuous semialgebraic gradient-direction convergence also has antecedents; the manuscript does not attribute that narrower qualitative fact to this project.

No comprehensive priority certificate is claimed. No journal acceptance estimate is supported. The different nonsmooth slope-determination conjecture considered at the beginning of this continuation remains unresolved here.

The main cosmic theorem is independent of all project milestones 01–29. The exact leading-vector applications rely on 30 and standard resolvent facts. Earlier results are used only for contextual comparisons; the relevant DRS escape identity is reproved.

## Sharp limitations

No theorem here covers general oscillatory/nondefinable operators or infinite-dimensional Hilbert spaces. State expansions cannot simply be differentiated into last-iterate displacement rates: the explicit reflected-product counterexample has a cosmic limit but a residual bounded away from zero. In particular no universal plain-DRS last-residual rate is inferred from the leading state term. The PSD recession limit is asymptotic, not a finite infeasibility certificate.

The common-method theorem compares the SAME operator/objective in a fixed metric at matching physical time. It is not a claim that every algorithm, arbitrary acceleration, or adaptive preconditioner selects the same direction. Approximate-iteration guarantees require a displayed cumulative-error condition.

## Reproduction

Files in tame_cosmic/:

    test_tame_cosmic.py
    TAME_COSMIC_RESULTS.json
    README.md

Run:

    python test_tame_cosmic.py

Requires Python 3 and SymPy. The test script does not use the network, an optimization solver, or any original historical proof script.

The exact symbolic checks establish the closed-form discounted DRS equation, positive/negative spectral-part identities, and its leading coefficient. Numerical checks illustrate scalar exponents 1/4,1/2,3/4,1; arbitrary-clock relaxation; gamma anchors 0,1,2; the common proximal/gradient/flow trajectory for inverse-power objectives; and the no-residual-inference counterexample. These finite checks are NOT premises of the all-dimensional proof.

At 200,000 iterations, the 2-by-2 scaled diagonal is 1.4141958633220997 for plain DRS versus limit sqrt(2), and 0.8164871402408226 for Halpern versus limit sqrt(2/3). Nonleading transients and floating-point underflow of an exponentially small offdiagonal are reported, not hidden. Universal validity comes from the analytic proofs.

## Manuscript focus

A coherent paper can now be centered on:

    Tame Nonexpansive Dynamics at Infinity:
    Cosmic Limits and Exact Leading Asymptotics

Lead with the broad cosmic theorem and its short geometric tracking proof; then state the semialgebraic rational-power law; then give the common proximal/flow/gradient leading term and plain-DRS application. Keep the earlier minimax and representation-complexity projects separate. The premise for a strong submission is the precise theorem and its relation to the named question, not a prediction that editors will compete for the paper.
