# Two-basis SDP universality — full-strength quadratic normal form

Branch: laa-track02-gptpro-analytic-frontier-20261112
Date: 2026-11-12
Historical handoff/corpus: ff6117295c329dc88d5bc280ee18adfe64cda8b0.

## Current strongest result

**The unrestricted quadratic positive-quotient frontier is proved, and milestones 06–08 strengthen it to one construction preserving the full facial and dual structure and admitting complete-positive matrix amplification.** The strongest unified statement is 08_DENSE_NONREFLECTION_FULL_STRENGTH_THEOREM.md.

For every rational trace-controlled A:S^m->R^p, m,p>=1, the final construction has

  N=11m^2+8m+14+2p,
  D(Y)=VYV^T, VV^T=I_m,
  E(X)=E_lin(X)+Y_0,
  y_b=Phi b+y_0,
  D E=id, B_U E=Phi A+y_0,
  D({Y>=0:B_U(Y)=y_b})={X>=0:A(X)=b} for EVERY b.

The linear part E_lin and D are completely positive, Y_0 is fixed rank-one PSD, and D(Y_0)=0. Every basis overlap is nonzero, with an explicit inverse-polynomial margin. U is not equivalent to any symmetric matrix under independent signed row and column permutations. All target observations are positive, including zero-source data. There are exactly two complete REAL basis lists, no extra measurements.

For every ambient Y>=0, with delta=||B_U(Y)-y_b||,

  ||A(D(Y))-b||<=K_+ delta,
  dist(D(Y),F_b)<=omega_b(K_+ delta) when F_b is nonempty.

K_+ is explicitly polynomial in dimensions and source coefficient magnitudes, without source Slater/rank/face-gap assumptions. Source objective pullback V^T C V preserves the entire spectrum of C with additional zeros, its rank, operator norm and Frobenius norm. Both SDP dual suprema and finite dual attainment are preserved.

For nonzero feasible b, let E_b be the maximum source support, r_b its dimension, and k_b the source singularity degree. Then

  maximum lifted rank = r_b+m^2+m+3,
  singularity degree of the lifted fibre = max(1,k_b).

The maximum rank formula also applies pointwise to the positive preimages of any nonzero feasible X, with r_b replaced by rank X. The minimum lifted support is explicitly described in 08. The zero source is represented by the unique rank-one Y_0, with lifted depth one.

The exact full-ambient modulus is controlled by an intrinsic ORIGINAL-SOURCE quantity:

  mu_b(t)=max{tr(P_(E_b^perp) X):X>=0,||A(X)-b||<=t},
  Omega_b(t) asymp sqrt(t+mu_b(t)) for nonzero feasible b,
  Omega_0(t) asymp t.

Omega uses all ambient PSD competitors and distance to the ENTIRE lifted fibre, not to the encoder image. Its constants include explicit, genuine source relative-interior and restricted-analysis condition parameters. The rational depth-k family in 06 proves that source exponent 2^{-(k-1)} can become ambient exponent 2^{-k} even though depth is exactly preserved. This is a proved separation, not a failure hidden by a source-only residual claim.

At every ancillary level n, complete positivity, exact entire-fibre surjectivity, cost identities and the global residual constant persist with NO ancillary-dimension factor. The observations at n>1 are explicitly two lists of n-by-n blocks, not two scalar rank-one diagonal lists on the entire Nn-dimensional space. No ancillary-level facial-depth formula is silently assumed.

## Computational model

Given a rational z with H=A*z>0, exact construction takes polynomial bit time in the ordinary input and certificate lengths. Each individual output coefficient is rational or a rational multiple of a positive rational square root, with degree at most two and polynomial bit length. The target map is rational affine. The deterministic finite grids in 08 use rational comparisons and have polynomially controlled overlap/observation margins. No general algebraic sign oracle or expanded multiquadratic number field is used.

Without a supplied certificate, 03 gives a rational certificate-finding algorithm polynomial in the input length and the declared numerical inverse cone margin. This is a conditioned algorithm, not an unconditional exact SDP solver. Whole-ambient stability constants are distinguished from the rank-independent decoded residual constant.

## Stronger proof milestones

### 06_FACIAL_DUAL_AND_SHARP_AMBIENT_STRENGTHENING.md
Proof commit: f152760f6e4f2cd47a50384206bf0115ac34e6c0.

Strict auxiliary positivity, exact minimum-face and pointwise maximum-preimage-rank formulas, inner depth equality and outer depth max(1,k), both standard SDP dual transformations including attainment, the source-leakage modulus, matching whole-ambient upper/lower laws, and the explicit rational all-depth separation family. The minimal shielded reflection has order 9m^2+4m+6+2p.

### 07_COMPLETE_POSITIVITY_AND_ANCILLA_UNIFORM_UNIVERSALITY.md
Proof commit: 2b0f214d0dba60b4540bc529d5d3a8970fe41700.

Explicit positive Choi/Gram matrices prove a real completely positive encoder extension. A sum-of-squares identity controls the entry-copy arrow. At most m^3+m^2+2m+1 real Kraus matrices suffice. Matrix-valued PSD stress and Frobenius estimates prove exact fibre and residual transfer at every ancillary level with the same constants.

### 08_DENSE_NONREFLECTION_FULL_STRENGTH_THEOREM.md
Proof commit: c69aefea9cd2b74dfff238287dd65e987356ad32.

One uniform order-11m^2+8m+14+2p construction combines all the above. A rational factored-column anchor supplies positive zero data and dense overlaps; an equal-weight, equal-radical-factor plane rotation gives a genuinely nonreflection transition. Finite polynomial root counts and interpolation produce explicit margins, rather than unquantified generic choices. The retained observations preserve the exact extraction, facial, dual, CP and sharp ambient results.

### 09_STRENGTHENING_AUDIT_REPORT.md

Adversarial scope audit, full diagnostic results, exact certificate identification, and reproducibility. The accompanying strengthening_audit/ directory contains both constructor modules, the numerical/symbolic suite, the independent Fraction suite, complete JSON outputs, and run instructions. Numerical evidence is not used as a premise of the all-dimensional theorems.

## Original frontier proof, retained unchanged

### 01_EXACT_LIPSCHITZ_CERTIFICATES_AND_FIRST_EXPOSURE.md
Proof commit: 22b8075cf1455c7d0212b690d8f89b089d72eaa4.

All-PSD Lipschitz residual control is equivalent to attained two-sided bounded dual certificates without Slater. Stable observables are range(M*)+S(R), where R is the range of a maximum-rank first globally PSD measured zero stress.

### 02_UNIVERSAL_QUADRATIC_TWO_BASIS_NORMAL_FORM.md
Proof commit: 9030a69bab7f5358065f836a826e9f5a9bbe2c86.

The original exact entire-fibre positive quotient at N=9m^2+4m+3+2p: bounded-entry lift, four-character anchor copies, two source-equation observations, block-respecting Parseval completion and strict signed reflection exposure. Its free auxiliary covariance is essential; the full lifted fibre is larger than E(F_b).

### 03_CONDITIONING_COMPLEXITY_AND_RECOVERY.md
Proof commit: b91ba45c2dd85bd5712e032456623488474065f3.

Encoder/data norms, decoded recovery, optimization errors, two-sided weak-feasibility gaps, finite precision, polynomial-bit certificate-input construction, and conditioned rational trace-certificate discovery.

### 04_QUADRATIC_ALGEBRAIC_OUTPUT_AND_EXACT_CERTIFICATION.md
Proof commit: cee61d6d1482cfbf5dea43d54e248460b2eee6d3.

Column-factor structure proves individually quadratic algebraic coefficients and rational exact verification. The final nonreflection compiler preserves this representation by matching the two rotated column factors.

### 05_ADVERSARIAL_AND_HISTORICAL_AUDIT.md
Proof commit: d82c889cc5e420c58101d0c3d3258a9635ffffed.

Original full-cone, objective, infeasibility, nonspectrahedral-dual and historical obstruction audit. Earlier NOT CLOSED status entries remain preserved in Git history; they preceded the proved construction.

Original reproducible diagnostics: audit_quadratic_quotient.py (c3f80deaaebcfd9b3e1788616250b99e798c8c40), audit_adversarial.py (811c02f761e3e47c735554fdab6c6ffbc720f445), ADVERSARIAL_RESULTS.json (1d0209ca30beb92425901f5a0a2638e8f8c3200f), audit_historical_corrections.py (c9c44eb8d0e186195ed9d5a67614ee1c371ed63e).

## Historical coverage and limits

The initial continuation read the complete handoff, original brief, archive 00, all canonical numbered manuscripts 01–64, six additional 26–28 variants, and the original dense-quadratic, rigidity-open, codimension-two and rational-obstruction proofs. Actual correction diffs for 17,47,51,60 were inspected. Historical scripts were read but not all rerun. The new strengthening suites were run, including exact rational and symbolic checks. No assertion is made that every historical proof or repository revision has been independently referee-certified.

Inherited index: ../laa_two_basis_track02_20261108/MASTER_INDEX.md.
Original brief: ../../prompts/laa_two_basis_significance_20261107/02_UNIVERSAL_STABILITY_TRANSFER.md.
Complete handoff: ../../prompts/laa_two_basis_frontier_20261112/FRESH_GPT_PRO_COMPLETE_ANALYTIC_FRONTIER_HANDOFF.md.
Dense source work: ../laa_two_basis_track02_20261107/dense_quadratic/.

External literature priority and independent refereeing are not certified. Those are distinct from the explicit algebraic proofs and the declared computational model.
