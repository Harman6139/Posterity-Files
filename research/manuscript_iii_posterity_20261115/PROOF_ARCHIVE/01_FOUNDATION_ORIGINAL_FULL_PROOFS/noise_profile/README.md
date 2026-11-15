# Manuscript III: radius profiles, stochastic samples, and precision barriers

This packet contains a complete proof of the functional-profile extension of Milestone 38 and its sharp noisy-gradient/bias consequences. The main result is in `../39_GENERAL_ESCAPE_PROFILES_NOISE_BIAS_AND_PARALLELISM.md`.

For an admissible doubling near-optimal radius r(epsilon), the optimal worst-case scales are:

- Samples: r(epsilon)/sqrt(epsilon) + sigma^2 r(epsilon)^2/epsilon^2.
- B-parallel rounds: r(epsilon)/sqrt(epsilon) + sigma^2 r(epsilon)^2/(B epsilon^2).
- Critical absolute gradient bias: epsilon/r(epsilon).

Upper and lower bounds hold up to fixed class-dependent constants. The theorem specifies the fixed function class, conditional noise model, nonattainment, growing-dimension quantifiers, and the distinction between stochastic sampled losses and exact population values.

## Reproduce the checks

Requirements: Python 3, NumPy, SymPy.

```sh
OPENBLAS_NUM_THREADS=1 python test_noise_profile.py
```

The run writes `NOISE_PROFILE_RESULTS.json`. The included result records exact symbolic identities, 210 profile-witness checks, 1,200 numerical one-step energy checks, budget calculations, and a 24-run stochastic implementation illustration. These are reproducibility checks, not mathematical proofs of asymptotic or minimax claims.

`noise_profile.py` implements the scalar tails, the two-dimensional hard population pair, the common biased oracle, the convex sampled-loss model, the projected batched accelerated method, and conservative certified budgets. The solver uses gradient samples only. Its resource cap raises an exception rather than silently claiming a guarantee after a truncated run.

The random-frame lower core is fully defined and proved in the manuscript. It is not reimplemented here; the parent Milestone 38 packet contains its numerical constructor. No computation of its exact orientation-independent minimum is used as numerical evidence for the proof.

## Manuscript focus

Suggested title: **Oracle Complexity at Infinity: Escape Profiles, Noise, and Precision**.

The deterministic/randomized power law becomes one corollary. The principal result is a general profile-to-complexity theorem with three matching barriers. Logarithmic escape gives a distinct non-power example. The two-point stochastic and bias lower bounds are explicit and only two-dimensional; the sequential lower bound remains genuinely high-dimensional.

Known acceleration, statistical testing, and random local-oracle techniques are credited. A complete proof is not a claim of historical priority, an accepted paper, a randomized cone-projection lower bound, or a guaranteed journal upgrade.
