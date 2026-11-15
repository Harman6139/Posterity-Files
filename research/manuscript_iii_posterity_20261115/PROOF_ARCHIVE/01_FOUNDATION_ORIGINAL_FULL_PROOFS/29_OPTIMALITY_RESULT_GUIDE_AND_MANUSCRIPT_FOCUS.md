# Current algorithmic result: optimal complexity without minimizers

Date: 2026-11-13. Parent snapshot before this continuation: 415ac86b4a6031e73e37a320f305fb20a921bdce.

## The main upgrade

The previous milestone 26 established exact power rates for specified algorithms from a static escape-radius profile. Milestone 27 adds a matching lower bound against EVERY deterministic adaptive first-order value-and-gradient oracle algorithm in a uniformly normalized class. It allows arbitrary queries, unlimited internal computation and an output not previously queried.

For fixed beta>0, rho_f(s) is bounded above and below by constant multiples of s^(-beta) over one common interval, with constants independent of function dimension and oracle horizon. The optimum is finite, known and unattained; the objective is globally convex C2 and 1-smooth. Then the optimal dimension-uniform oracle complexity is

    N_beta(epsilon)=Theta_beta(epsilon^(-beta-1/2)).

An accelerated algorithm achieves the upper bound without knowing beta in its updates. A bounded-coefficient dyadic weighted quadratic chain, a positive nonattained scalar tail and a consistent resisting rotation prove the lower bound in dimension 2T+3. For rational beta, the examples are semialgebraic.

This is a precise minimax classification, not merely a worst-case example for one algorithm. It is not randomized, not fixed-dimensional, and not an explicit-input computational hardness assertion.

## Proof files and immutable commits

- 27_MINIMAX_ORACLE_COMPLEXITY_WITHOUT_MINIMIZERS.md: 5670a71c4cb270b558acc74be65533da0ec79f56.
- 28_HALPERN_SPLITTING_RATES_AT_INFINITY.md: 5af0e7dc9d9674786b19aec498d958b42a481d95.
- oracle_optimality/: exact weighted-chain checks, resisting-transcript diagnostic, anchored Douglas–Rachford examples, complete recorded JSON, and reproduction instructions.

## Operational application

For a nonexpansive T with no fixed point and infimum displacement zero, define R_T(epsilon) as the smallest radius of an epsilon-fixed point. If R_T(epsilon)=Theta(epsilon^(-a)), Halpern iteration has residual Theta(k^(-1/(a+1))) and radius Theta(k^(a/(a+1))). This is a two-sided statement for every anchor. A semialgebraic operator automatically has such a rational exponent.

For Douglas–Rachford on an affine U and convex V, with anchor in U, the operator radius profile is EXACTLY the primal radius profile for points in U within epsilon of V. This gives the same powers for actual primal shadows and original equation residuals of weakly infeasible SDPs. The sharp matrix-order endpoint bounds import manuscript 12; the profile identity and anchored rate proof do not.

Plain, unanchored Douglas–Rachford exact power rates remain outside the proved result. Exploratory observations do not fill that gap. The smooth first-order minimax theorem does not silently imply minimax optimality in a nonexpansive-operator or cone-projection oracle model.

## A focused manuscript rather than a research anthology

Recommended working title:

    Optimal First-Order Complexity Without Minimizers

The mathematical narrative should be: minimum-radius profiles replace distance to a nonexistent optimizer; acceleration gives a universal upper bound; a uniformly controlled family proves no deterministic first-order method can improve its power; anchored splitting illustrates the same geometry in conic feasibility.

Suggested theorem order: (1) normalized class and main minimax theorem; (2) comparator energy upper bound; (3) dyadic chain resistance and uniform radius profile; (4) arbitrary-query lower bound; (5) relation to fixed-instance rates; (6) a concise splitting application, or a separately scoped companion paper if length warrants it.

The matching lower bound is the proposed central contribution, not a new claim to have invented acceleration, first-order oracle lower bounds, or Halpern iteration. Classical predecessors must be compared theorem by theorem. Novelty and editorial response are not mathematically guaranteed by a correct proof.

Do not include the unrelated smooth-body, quantum-correlation, Boolean-membership and two-basis compiler material merely to increase apparent breadth. They remain separate research outputs on the branch. Neither the earlier succinct smooth-body target nor a famous named complexity conjecture has been resolved by this continuation.
