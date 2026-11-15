# Track III continuation checkpoint

Date: 2026-11-14. Source baseline: 22ed4becd320695b41f8a11f1223ea090ef89ecf. Source milestones remain immutable.

## Status

The complete handoff has been retrieved. Existing branch contained only BENCHMARK_PLAN.md when this continuation began. No full conic randomized minimax theorem is established by that plan or by this checkpoint.

Read so far: milestone 12 in full, milestone 26 in full, milestone 27 in full; milestone 38 reading underway. Still required: remainder of 38, 39, 40, manuscript-noise scope, and current primary literature. The compiler files will be read if a compiler route is used; no oracle-preserving compiler reduction is presently claimed.

## Firm source conclusions

Milestones 26-27 give the accelerated upper estimate f(x_T) <= s + 2 rho_f(s)^2/(T+1)^2, applicable to genuine affine PSD-distance objectives. Their fixed-instance rate and generic deterministic lower bound are not a conic randomized lower bound. Milestone 12 supplies instance-dependent conic escape estimates, not dimension-uniform hard-family constants.

## Hazards being investigated

1. A fixed distribution over rational quadratic coefficient matrices is vulnerable to arbitrary-precision exact queries: a generic algebraically independent query can encode the entire rational quadratic. Thus rational approximation of Haar-frame hard quadratics cannot simply inherit exact-oracle lower bounds.
2. Squared PSD-distance is C1 and 1-smooth in orthonormal affine coordinates, but need not be C2. Epigraph representability alone does not simulate its value-gradient oracle.
3. Isometric affine coordinates constrain direct-sum embeddings: an arbitrary quadratic chain plus a 2x2 weak-infeasibility tail does not automatically have orthonormal coefficient matrices.
4. Unbounded query radii can amplify signal under additive gradient noise. Any proposed noise lower bound needs a class-specific indistinguishability proof that survives such queries.

These are proof obligations or route obstructions, not a universal disproof of the target theorem. Next checkpoints will separate complete lemmas from open claims.
