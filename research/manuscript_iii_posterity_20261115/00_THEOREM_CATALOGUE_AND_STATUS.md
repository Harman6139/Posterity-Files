# Theorem catalogue, with strict scope labels

## Original problem (still open)

Unknown rational affine symmetric pencil X(x)=X0+sum_i x_i Hi with Frobenius-orthonormal **rational** Hi, genuinely weakly infeasible slice, f(x)=dist(X(x),PSD)^2/2, and common comparison-radius profile rho_f(s) comparable to s^(-beta). Oracle returns **only exact (f(x), grad f(x))** at any finite real x, with no query-size/precision fee. Algorithms may randomize, compute without restriction and output unqueried points. Target beta=1/2 is a fixed-prior randomized lower bound Pr[f(output)>=c/(T+1)]>=2/3 with polynomial rational encoding, or a uniform universal disproof and sharp replacement. **Neither is proved.**

Known beta=1/2 bracket: Omega(log(1/epsilon)) and O(1/epsilon), over all coordinate dimensions and orders; the constants are class-normalization dependent.

## Genuine conic / original-oracle results

1. **Conic exact-rational moment-matched minimax (new continuation checkpoint 01–02).** Rational isometric weakly infeasible order 24(n+1)+2 pencil with two coordinates and *uniform* beta=1/2 profile. A fixed uniform n-bit prior gives exact minimax success S(n,T)=2^(-n)sum_{j=0}^{min(T,n)} binom(n,j) for epsilon <= (5/384)*4096^(-n). Proof includes the moment equations, positive four-square realization, all-real-location prefix simulation and matching irrational-gradient probes. This is a true optimization lower bound, but only at exponentially small accuracy in T.
2. **Fixed-two-coordinate universal minimax.** Over all normalized rational PSD-distance pencils in two affine coordinates and arbitrary PSD order, N(epsilon)=Theta(log(1/epsilon)), with a global central-cut ellipse upper bound and the above matching rational prior. This does NOT extend uniformly to growing coordinate dimension.
3. **Compact noncommuting two-center mask (checkpoints 11–12).** Exact exterior value/gradient equality in every large core-space direction, disjoint near-optimal regions, same isometric rational PSD model, exact fixed-prior lower at exponentially small accuracy. One algebraic exterior scalar query identifies distinct rational radial centers; centroid cuts yield O(1+r log(1/epsilon)) with r their recovered affine-hull dimension and a supplied center/radius envelope. At any fixed center budget M>=2 the subclass optimum is Theta_M(log(1/epsilon)).
4. **Spectral field-trace inertia fingerprint (grand arithmetic checkpoint 07).** For a rational isometric pencil with squared-characteristic polynomial irreducible over Q(x), a single algebraic scalar value determines the local negative inertia using Tr(P)/deg P=(k/m)tr(X^2). For inertia k=1 or m-1, recovers the entire characteristic polynomial globally, allowing rank-changing strata elsewhere, under a declared common probe. The sufficient S_m subset-sum criterion is conditional. NOT a universal identification theorem.
5. **PLQ spectral jump propagation (exact-rational checkpoint 13).** A natural PSD-distance objective quadratic on a finite polyhedral partition is a global quadratic plus signed squared affine hinges, with at most rank(X) distinct switching hyperplanes. Hence squared Euclidean distance to a triangle or any full-dimensional nonorthogonal-facet simplex (modulo a global quadratic and positive scaling) is not a natural affine PSD distance in the same query variables. Does not cover general non-PLQ PSD spectra.

## Distinct stronger / different oracle models

6. **Full PSD projection matrix oracle (exact-rational checkpoint 09).** For a KNOWN FINITE family of rational approximately feasible affine symmetric pencils, two nonadaptive antipodal full projection matrices P_+(X(q)), P_+(X(-q)) identify the pencil. Proof uses positively visible irreducible spectral factors and simultaneous finite-list separation. This is NOT the original compressed value/gradient oracle. Checkpoint 10 exhibits a one-vs-Theta(n) projection/vg interface separation on identical rational instances.
7. **Real coefficient chart, free-radius exact oracle (conic checkpoint 09).** Fixed Haar rotation, growing dimension O_beta(T^3), true conic squared PSD distance, matching Pr[f(output)>=c T^(-2/(2beta+1))]>=7/8, for all positive rational beta. Chart coefficients are REAL, not rational.
8. **Rational charged-radius exact oracle (conic checkpoint 08).** Fixed rational prior and charged excursions; matching T^(-2/(2beta+1)) power. This does not resolve uncharged queries.
9. **Rational positive input-relative gradient error (conic checkpoint 11).** For any positive bias budget within c_beta epsilon^(2beta+1) (and without population exact values), complexity Theta_beta(epsilon^(-beta-1/2)+tau^2 epsilon^(-4beta-2)); error threshold Theta_beta(epsilon^(2beta+1)). The support/height may depend on the positive bias budget; NOT valid at zero by continuity.
10. **Absolute, residual-relative noise, exact Gaussian testing and bias** in conic checkpoints 01–06, 10. These are for explicitly declared gradient or sampled-loss information models with no exact population value on the statistical lower route. No claim about unbiased PSD-valued projection samples.

## Original general smooth/projection manuscript results (not to call new conic lower proofs)

- Original source milestone 12: exact approximate Farkas/escape profile duality and sharp PSD order-dependent escape envelope.
- Original milestones 26 and 40: exact alternating/projection rates and semialgebraic last-velocity results for specified algorithms; not universal oracle lower bounds.
- Original 27: deterministic dimension-uniform nonattainment smooth convex lower bound.
- Original 38 and 39: fixed random smooth convex arbitrary-query lower bounds and general escape-profile sample/noise/bias results, **not** a natural PSD-distance conic realization.

## Known false shortcuts and unresolved tasks

- Rational quadratic lifts are decoded by one specially chosen algebraic exact gradient query. Rationalizing a Haar quadratic is not enough.
- Inactive spectral branches can agree on open sets, so one generic analytic-germ query does not identify ALL pencils.
- Full PSD projection access is not equivalent to coordinate residual contraction.
- Equal-scale rotated scalar copies still admit exponential convergence with an explicit gradient recurrence (checkpoint 05).
- Finite-PLQ simplex-distance hard functions cannot be realized as natural affine PSD-distance objectives even with a global quadratic adjustment (checkpoint 13).
- Current exact-rational moment-nesting construction loses energy exponentially at every revelation, so arbitrarily increasing depth does not give a c/T lower barrier.
- No fully general bit-height/precision phase diagram; no universal optimizer of growing-dimensional exact-rational class; no polynomial-threshold fixed rational prior.
