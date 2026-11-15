# Manuscript III — general-profile noise and precision theorem

Date: 2026-11-14.

## Complete new result

Main proof: `39_GENERAL_ESCAPE_PROFILES_NOISE_BIAS_AND_PARALLELISM.md`.
Immutable main-proof commit: `1861aac6e49c9121daa4c12cb1a6556cd54f62fa`.

For an admissible, fixed doubling near-optimal radius profile r(epsilon), globally smooth convex objectives with unattained infimum have the following matching dimension-uniform minimax scales under the declared conditional noisy-gradient oracle:

    samples = Theta(r(epsilon)/sqrt(epsilon)
                        + sigma^2 r(epsilon)^2/epsilon^2),
    B-parallel rounds = Theta(r(epsilon)/sqrt(epsilon)
                        + sigma^2 r(epsilon)^2/(B epsilon^2)),
    critical absolute gradient bias = Theta(epsilon/r(epsilon)).

The sample/round upper bounds hold below a fixed constant times the critical bias; above another fixed constant, a two-function indistinguishability proof rules out the requested accuracy regardless of computation. Constants and profile onset are fixed independently of dimension and horizon. The main theorem states the admissible-tail and doubling assumptions precisely.

For r(epsilon) asymptotic to epsilon^(-beta), the expected minimax error after T rounds is, up to class constants and saturation at one,

    T^(-2/(2beta+1)) + (sigma^2/(BT))^(1/(2beta+2))
                           + nu^(1/(beta+1)).

Logarithmic escape instead yields sample complexity

    Theta(epsilon^(-1/2) log(1/epsilon)
                + sigma^2 epsilon^(-2) log^2(1/epsilon)),

and critical bias Theta(epsilon/log(1/epsilon)).

## Proof content

The upper proof is an explicit projected accelerated comparator-energy calculation with martingale variance and history-dependent bounded bias. The sequential lower proof uses the random hidden core of 38 at a profile-dependent scale, with all ingredients reproduced in 39. Exact locality means the same noiseless lower bound allows exact Hessians, but no uniform Lipschitz-Hessian hypothesis is imposed. The variance and bias lower bounds are independent, explicit, and two-dimensional. The statistical lower bound already holds when an oracle reveals entire convex sampled losses; that stronger model applies only to that lower bound, not to the sequential term.

## Reproducibility

`noise_profile/` contains the model constructors, noisy-gradient-only solver, conservative budget calculation, tests, complete results and README. The completed run has five exact symbolic identities, 210 profile-witness checks, 1,200 one-step energy checks, nine budget cases and a 24-run stochastic illustration. Universal correctness rests on the proof, not finite testing.

## Scope and manuscript significance

Proposed focus: **Oracle Complexity at Infinity: Escape Profiles, Noise, and Precision**.

This is a functional-profile classification with three matching barriers, rather than another power-law convergence bound. It is not a claim to invent stochastic acceleration or Gaussian testing. The noise oracle does not provide exact true objective values. The hard sample losses may be individually unbounded below. The sequential lower bound is high-dimensional; the other two are already two-dimensional. The conic projection application in 39 is an upper-bound transfer only. No new cone-projection minimax lower bound, named conjecture resolution, or editorial guarantee is claimed. Historical novelty and independent review remain separate from the supplied proof.
