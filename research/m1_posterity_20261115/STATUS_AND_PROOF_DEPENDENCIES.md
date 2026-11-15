# Mathematical status, precise theorems, dependencies and live gaps

_Date: 2026-11-15. This is an audit index, not a substitute for the full proofs in PROOFS and FOUNDATIONS._

## A. The exact universal problem

On `S^m` with Frobenius metric and `K=S^m_+`, let `U={X:A(X)=b}` be weakly infeasible, i.e. `b in closure A(K)\A(K)`. Plain, affine-first, unanchored Douglas–Rachford is
```
T(Z)=Z+P_K(2P_U Z-Z)-P_U Z,   Z_(k+1)=T(Z_k).
```
Inherited state theorem (Milestones 30–31): `Z_k=V k^p+o(k^p)`, `V!=0`, `p=alpha/(alpha+1)`, `0<p<1`, all starts. The **proposed universal last-step theorem** `k^(1-p)(Z_(k+1)-Z_k)->pV` is not asserted to hold. The source proof packages claim a **negative resolution** via a rational seven-by-seven gamma-2 family, subject to final adversarial audit as noted below.

## B. Explicit negative construction and proof dependency chain

Use indices 0,...,6, `Fij=Eij+Eji`, `a=-(F01+F34)/2`, and for rational `gamma in [3/2,5/2]`,
```
L_gamma=span{
 E00+E33,
 E11-F02/2,
 E44-F35/2,
 E66+gamma(F02-F35),
 F06,
 E22-E55
},   U_gamma=a+L_gamma.
```
The data are rational and the metric is the **original Frobenius metric**. An explicit rational starting family `Z0(gamma,M)` is supplied in [Checkpoint 16](PROOFS/02_GRAND_SPECTRAL/16_UNIFORM_RATIONAL_RESONANCE_FAMILY.md), Section 2, with the very conservative claimed sufficient threshold `M>=10^(50000000000)`. It is not an efficiency claim.

**Algebraically established construction:** the affine space is disjoint from the PSD cone, approximated by two exact PSD arrow blocks with equation error `2t^3` and trace `1/t+2t+2t^3`. A matching Schur-minor bound proves the escape exponent `alpha=1/3`; the state exponent is `p=1/4`. See [original local checkpoint](LOCAL_20261115/04_BALANCED_VARIANT_AND_VERIFIED_STATUS.md) and [full proof](PROOFS/02_GRAND_SPECTRAL/08_RATIONAL_PSD_RESONANCE_AND_EXACT_LIMIT_SET.md), Section 1.

**Claimed nonlinear last-step result:** for `c0=27sqrt(3)/256, N=9/16, cA=(4c0)^(1/4)` and `V=cA diag(1,0,1/sqrt(3),1,0,1/sqrt(3),0)`, set
```
a0=27(2sqrt(3)-3)/256,
F_gamma=9(2-sqrt(3))/(64 gamma(22gamma+1)),
R_gamma=N sqrt(F_gamma)/cA^3.
```
The source asserts
```
Clust {k^(3/4)(Z_(k+1)-Z_k)}
 = V/4 + R_gamma {cos(theta)F06+sin(theta)F26: theta in R}.
```
This circular cluster set is incompatible with a single `pV` limit. It also leads to a nonzero logarithmic angular-length coefficient, a constant full-step-norm coefficient, and nonconvergent *normal/whitened equation-residual norms* (Checkpoints 12, 14, 16).

Proof dependence is precise:
1. Matrix-cut complementarity gives exact transverse energy: [01](PROOFS/02_GRAND_SPECTRAL/01_EXACT_CUT_ENERGY_AND_SPECTRAL_ATTENUATION.md).
2. Exact weighted Riccati spectral graphs and sign margin separate the small eigenvalue: [07](PROOFS/02_GRAND_SPECTRAL/07_UNIFORM_TRAPPING_AND_RATIONAL_ENTRY.md).
3. Contractive symmetric and asymmetric fast maps, stable slow filter and exact quadratic charge control all perturbations on one compact chamber: [07](PROOFS/02_GRAND_SPECTRAL/07_UNIFORM_TRAPPING_AND_RATIONAL_ENTRY.md).
4. Quartic correction produces a logistic averaged amplitude with **strictly positive** stable equilibrium: [08](PROOFS/02_GRAND_SPECTRAL/08_RATIONAL_PSD_RESONANCE_AND_EXACT_LIMIT_SET.md).
5. Uniform quantitative envelope and rational-entry bound are proposed in [09](PROOFS/02_GRAND_SPECTRAL/09_EXPLICIT_RATIONAL_WITNESS_BOUND.md); an independent symbolic audit corrects a nonessential term count in [13](PROOFS/02_GRAND_SPECTRAL/13_AUDIT_FINDINGS_AND_BENCHMARK_PROTOCOL.md).
6. Uniform rational parameter extension and full circle theorem: [16](PROOFS/02_GRAND_SPECTRAL/16_UNIFORM_RATIONAL_RESONANCE_FAMILY.md).
7. Earlier parallel proof attempt retained separately under `PARALLEL_RESONANCE_AUDIT`.

**Audit status:** This archive has inspected the argument structure, rational construction and stated boundaries; the entire claimed `10^50000000000` quantitative Jacobian/Taylor envelope and multivariable no-first-exit hierarchy have not received a full independent referee-level verification. Do not call the counterexample independently certified solely because the authoring checkpoints call it proved. Its exact result is nevertheless fully written down and reproducible for further audit.

## C. The general replacement: static excess vs transverse kinetic energy

Let `K` be **any closed convex semialgebraic cone** in finite-dimensional Euclidean space, `U=a+L` disjoint from `K` at distance zero, `P=P_L`, `Q=I-P`, `Z_k=a+x_k+y_k`, and `d_k=Z_(k+1)-Z_k`. The cone shadow `v_k=P_K(a+x_k-y_k)` satisfies `Pv_k=x_(k+1)`, `Qv_k-a=Delta y_k`. Define
```
D(r)=min{||Qv-a||:v in K, ||Pv||<=r},
e_k=||Delta y_k||^2-D(||x_(k+1)||)^2 >= 0.
```
Put `V=H+G`, `H=PV`, `G=QV`; `I_(n,m)=sum_(j=n)^(m-1)j^(2p-2)`. For fixed `lambda>1` and `m=floor(lambda n)`, the documented main theorem gives under the equivalent natural-scale bounded-excess hypotheses
```
sum_(j=n)^(m-1)||d_j||^2
   = p^2||V||^2 I_(n,m) + 2 sum_(j=n)^(m-1)e_j + o(I_(n,m)).
```
The longitudinal coefficient `k^(1-p)<d_k,V> -> p||V||^2` then implies a macroscopic quadratic transverse energy equal to twice the excess. The exact velocity is equivalent to vanishing *averaged static excess*; positive limiting excess yields a nonradial speed increment and logarithmic spherical length. It supplies a sharp non-tautological criterion using an independent static convex optimization problem, not presupposed velocity-direction convergence. Full proofs in [10](PROOFS/02_GRAND_SPECTRAL/10_UNIVERSAL_STATIC_EXCESS_AND_KINETIC_DEFECT.md), [12](PROOFS/02_GRAND_SPECTRAL/12_ARBITRARY_CONES_AND_ANGULAR_TRANSPORT.md), [14](PROOFS/02_GRAND_SPECTRAL/14_TRANSVERSE_EQUIPARTITION_AND_RESIDUAL_CLUSTER_SETS.md).

This **is not** an unconditional claim that all conic orbits have natural-scale bounded last-step norms, and it is **not** a classification of every singular spectral switching orbit.

## D. Positive criterion and spectral-saddle explanation

For products of real symmetric and complex Hermitian PSD cones with *coupled* affine equations, the source proves that if the common leading ray is blockwise positive definite, then `Z_k=V sqrt(k)+o(sqrt(k))` and `sqrt(k)d_k->V/2`. This depends on a spectral-gap decomposition of the Jacobian of matrix absolute value, strict contraction in the normal complement and two orders of nonlinear tracking. [Full proof](PROOFS/02_GRAND_SPECTRAL/02_REGULAR_SPECTRUM_VELOCITY_THEOREM.md).

The center dynamics is described by an explicitly minimized quadratic functional `Phi(H,G)=min_C tr(H^-1 C G C*)`, with drift `(-grad_H Phi, +grad_G Phi)`, rather than one globally descending convex potential. [Full proof](PROOFS/02_GRAND_SPECTRAL/03_REGULAR_SPECTRAL_SADDLE_POTENTIAL.md). This is the mathematical explanation of why convex forward–backward energy arguments cannot automatically be transplanted into plain DRS.

## E. Specific unresolved original orbit

The 2026-11-15 *local* `gamma=1`, `epsilon=1/10` orbit with initial perturbation `(1/10)F06+(3/100)F26` still lacks an asymptotic theorem. Its finite-record scaled transverse amplitude is around `0.02172` after six million steps, **not proof**. At `gamma=1`, the leading small eigenvalue switches sign for some phases; the stable fast map acquires a neutral drifting charge in the switching chamber. [17](PROOFS/02_GRAND_SPECTRAL/17_SWITCHING_FAST_MAP_AND_NEUTRAL_CHARGE.md) proves only a frozen parameter classification. A coupled moving-parameter proof is absent. The general gamma-2 disproof, if validated, logically does not depend on resolving this older particular start.

## F. Adversarial verification and publication gates

- **Proof gate:** Independently check all exact finite-dimensional spectral identities and every constant in the gamma interval trapping proof, including the enormous quantitative analytic-implicit-function envelope.
- **Priority gate:** The 2025–2026 literature comparison remains targeted, not exhaustive; Pazy, Bauschke–Douglas–Moursi, Ryu, Bolte–Gaubert–Vigeral, Liu–Ryu–Yin and contemporary papers need theorem-level priority mapping. Continuous-time definable gradient spherical length was independently established by Do–Jentzen–Kuckuck in 2026.
- **Journal gate:** A separate 10+10 published-paper sample with DOI, proof access and editorial fit is now archived. An 8-of-10 superiority finding is NOT verified; no probabilistic acceptance claim is made.
- **Artifact gate:** Main LaTeX source is fully retained; layout/compile, authorship and publisher formatting need final review.

The complete original evidence and changes are retained to enable **correction**, not merely positive retrospective storytelling.
