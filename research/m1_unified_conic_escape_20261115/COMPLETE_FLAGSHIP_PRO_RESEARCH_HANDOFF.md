# MANUSCRIPT I — GRAND UNIFYING PRO RESEARCH HANDOFF
## Spectral transport at infinity: universal last iterates, conic feasibility, and finite angular motion

**Research handoff prepared 2026-11-15.** Assign this complete file to a NEW independent high-effort Pro research chat. This is a research program, not an achieved theorem. Read all the pinned GitHub mathematics and all provided local data BEFORE making claims.

### One-sentence mission

Transform Manuscript I into a general and genuinely reusable mathematical theorem identifying **which geometric property at infinity makes the actual last steps of nonexpansive conic splitting obey precise asymptotic laws**, unifying semialgebraic cosmic convergence, exact convex-flow/forward–backward velocities, affine–PSD Douglas–Rachford, weak infeasibility, and the possibility of transverse spectral oscillations.

The paper must present ONE organizing theorem/structural dichotomy, with substantial new consequences in convex analysis, spectral matrix geometry and monotone splitting. A new isolated n=7 example, a conditional lemma, a repackaged alternating-projection theorem, or a long list of previous milestones is NOT a completed flagship breakthrough.

# I. The exact mathematical frontier

Let \(\mathbb S^m\) carry the Frobenius inner product, \(K=\mathbb S^m_+\), and
\[
U=\{X\in\mathbb S^m:\mathcal A(X)=b\},
\qquad b\in\overline{\mathcal A(K)}\setminus\mathcal A(K).
\tag{1}
\]
Thus \(U\ne\varnothing\), \(U\cap K=\varnothing\) and \(\operatorname{dist}(U,K)=0\). Ordinary, unanchored Douglas–Rachford (DRS) for the affine–PSD pair is
\[
\boxed{T(Z)=Z+P_K(2P_UZ-Z)-P_UZ,\quad Z_{k+1}=T(Z_k).}
\tag{2}
\]
No anchoring, damping, changing the algorithm to alternating projections, artificially changing the metric, or selecting a special starting point is allowed in the principal theorem.

Baseline prior project mathematics (Milestones 30–31) yields, for each instance and **every** starting point, a common leading state term
\[
Z_k=V k^p+o(k^p),\quad V\ne0,\quad
p=\frac{\alpha}{1+\alpha}\in\mathbb Q\cap(0,1),
\tag{3}
\]
where the primal escape radius is \(R_b(\delta)\asymp\delta^{-\alpha}\). This is a STATE statement; one may not differentiate it.

The unresolved original conjecture is the full vector last-step law
\[
\boxed{k^{1-p}(Z_{k+1}-Z_k)\longrightarrow pV.}
\tag{4}
\]

### Grand Theorem I — exact target

**Decide (4) in full generality for arbitrary PSD order and every initial point, AND establish a structural principle that explains the outcome.** There are exactly two legitimate possible research outcomes:

**Outcome A (universal positive):** Prove (4) for ALL such affine–PSD pairs, all m and starts; derive the correct exact leading constants for unanchored DRS residual norm, affine and PSD shadows, and original equation residual under the appropriate whitening. Establish a non-tautological spectral/monotone-geometric criterion which proves why transverse last-step oscillations are impossible in the affine–PSD setting, although they ARE possible for analytic firmly nonexpansive maps. Extend the invariant to an additional substantial class of conic splittings, e.g. arbitrary self-dual homogeneous cones or a meaningful product cone with coupled affine equations; do NOT just transfer a Lorentz theorem coordinatewise through coupled constraints.

**Outcome B (universal negative):** Construct an EXPLICIT rational affine–PSD system and rational start with a rigorously proved persistent transverse last-step obstruction; for example prove
\[
\limsup_{k\to\infty}k^{1-p}\|
\Pi_{\mathrm{tr}}\bigl(Z_{k+1}-Z_k\bigr)\|_F>0
\tag{5}
\]
where \(\Pi_{\mathrm{tr}}V=0\), or prove at least two distinct cluster vectors for the scaled steps. This must be an actual PSD projection iteration, not merely a firmly nonexpansive resolvent or a finite simulation. Then prove a **sharp corrected GENERAL theorem** that classifies when exact velocities do hold in the conic setting and gives a useful universal substitute in the oscillatory regime (sharp norms/limit sets/ergodic and radial laws, appropriate spectral conditions), with nontrivial applications outside one constructed example. The corrected theorem must be more significant than saying "the state still converges in direction."

A good final paper may unify these outcomes through an exact, geometrically testable **spectral transport / balance criterion**: the failure or success of the DRS derivative law should be controlled by matrix-cone complementarity, evolving eigenvectors/small eigenvalues, affine normal transport and a quantitative energy-dissipation identity. DISCOVER the right invariant; no speculative formula is assumed correct here. A restatement that "the residual directions converge if and only if they converge" is tautological and insufficient.

## II. The decisive n=7 candidate and what is NOT yet proved

The latest independent Pro researcher reports a **modified rational 7-by-7 affine–PSD construction**, whose full local source is named **04_BALANCED_VARIANT_AND_VERIFIED_STATUS.md** inside a local packet **DRS_progress_checkpoint_20261115.zip**. They report a proof of weak infeasibility and the exact primal escape exponent
\[
\alpha=1/3,\qquad p=1/4.
\tag{6}
\]
The reference orbit has an identically zero seventh row and column. Therefore (4) would force the transverse seventh-column component of \(k^{3/4}(Z_{k+1}-Z_k)\) to vanish.

At a specified rational perturbed initial point, numerical records (finite-precision experiments ONLY) show the following amplitudes:

| Number of iterations | \(k^{1/4}\|(Z_k)_{0:6,6}\|\) | \(k^{3/4}\|(Z_{k+1}-Z_k)_{0:6,6}\|\) |
|---|---:|---:|
| 200,000 | 0.0313400 | 0.0206325 |
| 2,000,000 | 0.0324799 | 0.0213759 |
| 6,000,000 | 0.0330047 | 0.0217200 |

These do NOT establish a nonzero limsup or rule out extremely late decay. They are not a proof and must not be sold as an SDP counterexample. The key missing step is to understand the **nonlinear small-eigenvalue spectral dynamics and accumulated feedback** well enough to prove nondecay or eventual decay, with certified asymptotic error bounds. A frozen or moving linearization does not prove the nonlinear orbit's long-time behavior unless its accumulated error is controlled.

**CRITICAL ACCESS WARNING.** The new n=7 packet was reported as NOT yet pushed to GitHub. The current verified remote branch is **research/pro-m1-allorder-drs-20261114** at **3ede4efb66c42da2b9b25584478a42e7cf35648f**. An earlier reported commit 2d1f975c4a0ecd3ec6b47baeee3be33639ad0118 exists in its history but is NOT the current branch head. The new local ZIP is not in the remote tree as of this handoff. Inspect Project/Library files or user-attached packet if available; if unavailable, reconstruct the candidate from earlier 02–04 checkpoint details and the above summary, and EXPLICITLY say the unpushed proof/code were not read. Do not invent its matrix entries or claim to have run its six-million-step code. The mathematical target remains universal even if the candidate fails.

**Strong n=7 success requirement:** If you claim a disproof, supply exact rational matrices \(\mathcal A,b,Z_0\), verify PSD weakness and \(\alpha=1/3\) directly, and prove persistent \(\Omega(k^{-3/4})\) transverse increments by rigorous comparison/spectral perturbation/averaging/normal-form control, not just plots. If instead the candidate converges, prove the exact convergence mechanism and extract a generalizable PSD-specific lemma.

## III. Mandatory historical work in GitHub — READ ALL BEFORE RESEARCH

Connected repository: **Harman6139/Posterity-Files**.

### Existing independent Track I branch (newest remote results)

**Branch** research/pro-m1-allorder-drs-20261114
**Pin** 3ede4efb66c42da2b9b25584478a42e7cf35648f
**Directory**
https://github.com/Harman6139/Posterity-Files/tree/3ede4efb66c42da2b9b25584478a42e7cf35648f/research/pro_m1_allorder_drs_20261114

Read every numbered file, in particular:

1. **00_CHECKPOINT.md** — honest prior reading and initial unproved status (historical, later 06 is newer).
2. **01_RECOVERED_BALANCE_AND_SATURATION_CRITERION.md** — primal–dual shadow balance, conditional scalar saturation criterion, and exact proof boundaries.
3. **02_DOUBLED_ARROW_CANDIDATE_CHECKPOINT.md** — first n=7 doubled-arrow candidate and spectral obstruction hypotheses; do not mistake its experimental observations for theorem.
4. **03_MATRIX_VIRIAL_AND_TRANSIENT_WARNING.md** — matrix-energy and virial identities, nonlinear transient hazards; distinguish from the locally reported balanced variant.
5. **04_RECOVERY_AND_NEXT_ATTACK.md** — reconstruction ledger, what failed.
6. **05_PROJECTIVE_ALTERNATIVE_DUALITY.md** — exact projective alternative system and DRS identities, with priority caveat: reciprocal escape exponent was ALREADY proved in the earlier Milestone 12.
7. **06_ONE_GOOD_ORBIT_TRANSFER.md** — a rigorously proved result: if 1/2 <= p < 1 and ONE actual firmly nonexpansive orbit has the exact last-step law, ALL starts have it, using square-summable velocity differences. DOES NOT create that good orbit; below p=1/2 the route fails for general firmly nonexpansive maps.
8. **diagnostics/** and related exact data if available. Inspect code and arithmetic assumptions rather than relying on summaries.

### Original Manuscript I / LAA project branch

Baseline research commit **22ed4becd320695b41f8a11f1223ea090ef89ecf**; directory:
https://github.com/Harman6139/Posterity-Files/tree/22ed4becd320695b41f8a11f1223ea090ef89ecf/research/laa_two_basis_track02_20261112

Mandatory full source files:

- **12_RECIPROCAL_ESCAPE_LAW_AND_SHARP_DIMENSIONAL_BOUNDS.md**: exact reciprocal trace/feasibility escape and sharp matrix-order exponent envelope.
- **26_ESCAPE_CONTROLLED_PROJECTION_DYNAMICS.md**: two-sided convergence rates with nonattained smooth convex infimum; ALL-order alternating projections (not plain DRS).
- **28_HALPERN_SPLITTING_RATES_AT_INFINITY.md**: anchored DRS, different algorithm.
- **30_TAME_COSMIC_CONVERGENCE_AND_POWER_LAWS.md**: common leading state vector for definable nonexpansive orbits. General cosmic conjecture false; do not re-prove an already established weaker theorem.
- **31_COMMON_LEADING_DIRECTION_FOR_MONOTONE_METHODS_AND_DRS.md**: exact all-order PLAIN DRS STATE and primal PSD shadow asymptotics, exponent \(p=\alpha/(1+\alpha)\); unanchored last step explicitly left open.
- **35_ANALYTIC_FIRM_COUNTEREXAMPLE_TO_LAST_STEP_ASYMPTOTICS.md**: real-analytic semialgebraic globally firmly nonexpansive resolvent with a circle of scaled last-step cluster vectors. It is NOT affine–PSD DRS, so is no disproof of (4).
- **36_EXACT_LAST_STEPS_FOR_ALL_SINGLE_LORENTZ_WEAK_INFEASIBILITY.md**: complete result for ANY affine space over ONE Lorentz cone in ANY dimension, including all real/Hermitian order-two SDP systems; arbitrary products with coupled affine constraints are not included.
- **40_EXACT_VELOCITIES_AND_FINITE_ANGULAR_MOTION.md** and **00_MANUSCRIPT1_EXACT_VELOCITY_STATUS.md**: exact leading velocity, objective gap, objective decrement, radial efficiency, and finite angular length for semialgebraic convex forward–backward splitting; covers alternating projections on ALL weakly infeasible SDP orders. Does NOT include PLAIN DRS. Crucial mechanism: convex cyclic subgradient/energy-tail identities which may FAIL for a general monotone DRS resolvent.

Read the ORIGINAL proofs in chunks if the connection truncates responses; source reading is not complete if only a prefatory section was fetched.

## IV. Primary literature and novelty gates

Check primary text (and updates as of 2026-11-15), giving theorem-level comparisons, not merely titles:

- Pazy: asymptotic behavior, minimal displacement and linear drift for nonexpansive maps.
- Bauschke–Douglas–Moursi: cosmic convergence conjecture and proximal example (2015); Ryu's counterexample to general cosmic conjecture.
- Bolte–Gaubert–Vigeral: definable nonexpansive dynamics and discounted-curve techniques; distinguish \(Z_k/k\) and the FIRST nonzero sublinear term.
- Liu–Ryu–Yin and later weak-infeasible conic/ADMM/DRS pathology literature; distinguish primal residual from iterate displacement and the effect of operator order.
- Strongly relevant 2025–2026 semialgebraic / tame nonexpansive orbit results, including the **2026 Do–Jentzen–Kuckuck paper** *On the gradient conjecture at infinity: Finite spherical length for gradient trajectories of definable potentials*, arXiv:2610.29211 (continuous-time result already established; it does NOT supply a new discrete DRS theorem).
- Grandjean, Loi, Daniilidis–Salas–Tapia-Garcia on gradient trajectories, continuous flow and slope/direction at infinity.
- Semialgebraic spectral perturbations, eigenvector transport near colliding eigenvalues, monotone operator dynamics, Łojasiewicz-type estimates, and gradient-like discrete systems. Do not import a gradient inequality without confirming DRS has the required potential.

If the named result is already proved in the literature, identify the exact theorem, proof and priority, then find a genuinely stronger unsolved target; do not claim another group's result.

## V. The required unifying mechanism and novel consequences

The central research problem is not merely a yes/no about one n=7 orbit. Develop a **mathematically checkable conic spectral balance invariant** with an exact identity or inequality that connects the following:

1. **Affine–cone complementarity along actual DRS iterates.** Write
\[
u_k=P_U Z_k,\quad y_k=P_K(2u_k-Z_k),\quad
d_k=y_k-u_k=Z_{k+1}-Z_k.
\tag{7}
\]
Use that \(u_k\in U\), \(y_k\succeq0\), and \(2u_k-Z_k-y_k\) is a normal to K at \(y_k\). For the PSD cone, understand the positive/negative spectral parts, their orthogonality, and changing spectral projectors. Derive a telescopeable (or Tauberian) energy controlling the **transverse** component of \(d_k\) relative to the leading state vector. Any proposed invariant must be proved, not named.
2. **Static escape and dynamical speed.** The static exponent \(\alpha\) fixes \(p=\alpha/(1+\alpha)\) for DRS state. Establish the strongest precise law for \(\|d_k\|\), vector direction, true equation residual and convergence of PSD shadows. If a component is slower, quantify its exponent and cluster set.
3. **Rotating eigenvector modes.** At repeated/vanishing eigenvalues, a small transverse state can drive an \(O(k^{p-1})\) oscillatory step. Either prove such modes cannot persist in affine–PSD DRS, or classify and construct them rigorously.
4. **One structural generalization beyond the original problem**, chosen by mathematical relevance: coupled products of Lorentz/PSD cones, general semialgebraic self-dual homogeneous cones, reflected resolvents of semialgebraic cyclically monotone pairs, or a complete necessary/sufficient spectral regularity criterion for broader tame firmly nonexpansive maps.
5. **Sharp contrast with forward–backward and continuous flow.** Explain precisely which convex energy identity makes Milestone 40 robust to even NONDEFINABLE splitting components, and why it does/does not transfer to the DRS algorithm. If a new "relative cyclic monotonicity at infinity" principle captures both methods, prove it with genuinely nontrivial corollaries; a tautological last-step condition is unacceptable.

Do not demand a single closed formula for every matrix order if the right invariant is algorithmically defined; however it must give a clear universally quantified theorem and effective conceptual predictions, not a list of n=2,3,7 cases.

## VI. Journal-standard significance (the user's upper-quintile demand)

The best current subject venues are **Journal of Convex Analysis** and **Advances in Nonlinear Analysis**. A truly broad, new structural theorem relating the escape dynamics of major splitting methods might justify **Bulletin of the London Mathematical Society**, **Proceedings of the AMS** (if concise), or a nonlinear analysis/optimization flagship. A journal's published 2025 median submission-to-final-acceptance is NOT an acceptance probability; the user prefers submission-to-acceptance in eight months but this cannot be guaranteed. Re-check current editorial policies and publisher changes (JCA changed publisher in 2026). The continuous gradient spherical-length theorem is 2026 prior art and raises the novelty bar, not a marketing opportunity.

**Defensible "80th percentile" content gate**, never a literal 80% editorial pass rate:

- Prove (4) or its exact affine–PSD disproof AND a strong new universal replacement. No isolated numerical example, conditional hypothesis, one-Lorentz special case, alternating-projections substitute or generic-firm counterexample suffices.
- Prove one reusable additional dynamics theorem that is genuinely broader than the one candidate and not inherited unchanged from 30–40.
- Full adversarial proof review, including small spectral eigenvalues, collisions, nonunique eigenvectors, rank losses, scaling, all initial conditions, and rigorous long-time asymptotic control. A floating-point six-million-step run is NOT a limit proof.
- Preregister and evaluate at least **12 real published papers in JCA/ANA** from at least two 2024–2026 issues plus close-topic controls; also >=10 for any more prestigious candidate. Compare theorem novelty, proof difficulty, generality, reusable tools, and audience fit using full theorems and proofs whenever accessible. Report DOIs and sampling limitations; do not invent an 8/10 rating.
- Deliver a self-contained main text of about 20–30 pages with one memorable title, central theorem, exact sharp examples, original equations and correct physical-time scales, and an honest 2026 related-work analysis. The project has many milestones; do NOT turn all 40 into one omnibus.
- Publication prospects are CONDITIONAL on a successful proof and an independently checked historical novelty audit; a paper cannot have guaranteed acceptance, no revisions, or an 80% actual chance based on this rubric.

## VII. Attack priorities and deliverables

### Research priority 1 — resolve the n=7 spectral transport

Recover the latest local packet if accessible. Verify its exact rational construction and \(\alpha=1/3\). Derive a **nonlinear** invariant/normal form for the shrinking seventh-column mode and its coupling to the semialgebraic PSD projection. Consider renormalized logarithmic time \(s=\log k\), evolving tangent spaces, and rigorous control of second-order spectral remainders (these are suggestions, not proofs). Identify whether a periodic/transverse mode can remain at \(k^{-3/4}\). If so, give a lower bound; if not, establish summable damping. A moving linearization without cumulative error estimates is not a result.

### Research priority 2 — arbitrary-order characterization, not case checking

Attempt all-order proof/disproof using the right matrix spectral principle, not brute force over matrix order or ad hoc proof-route searches. Preserve and use the positive one-Lorentz theorem and the p>=1/2 good-orbit transfer as boundary checks. Examine what changes at p<1/2, since the rotating firmly nonexpansive example already occurs there. If n=7 route fails, do not abandon the frontier; pursue the intrinsic criterion.

### Research priority 3 — manuscript-level synthesis

Derive sharp original residual consequences, identify canonical whitening where necessary, and prepare a theorem that unifies conic splitting and the broader convex-dynamical story. Crosscheck against 2026 literature.

**Deliverables in an independent GitHub results branch** (recommended research/pro-m1-grand-spectral-transport-20261115, branched from 3ede4efb66c42da2b9b25584478a42e7cf35648f):

1. COMPLETE_MASTER_THEOREM_AND_PROOF.md, including full exact hypotheses/proofs or the exact SDP counterexample and corrected universal theorem.
2. SPECTRAL_TRANSPORT_INVARIANT.md isolating the genuine common mathematical mechanism.
3. SDP_7X7_CERTIFIED_ANALYSIS.md with rational data, rigorous bounds, and verified source packet or an explicit unavailable-packet notice.
4. TESTS/ with independent high-precision numerics/symbolic checks only as corroboration, full saved results and resource reports.
5. PRIORITY_AUDIT_2026.md, at least two venue paper-level benchmarks, and a standalone submission-ready LATEX manuscript with a separate supplementary proof if needed.
6. STATUS_PROVED_VS_UNRESOLVED.md; commit all material mathematical progress incrementally with exact branch SHAs. Never overwrite the existing branch or imply unseen local proofs were read.

### Absolute success criterion

**ONE fundamental, correct mathematical theorem** explaining exact last-iterate behavior of plain affine–PSD Douglas–Rachford at infinity in arbitrary matrix order, positively or via a sharp universal corrected theory after rigorous disproof, with a genuinely broad dynamics consequence. Anything weaker is intermediate research; document it honestly and continue concentrating on the missing structural step.

The ideal possible paper claim—subject to PROOF, not currently achieved—would be:

> "A conic spectral transport principle determines when divergent nonexpansive splitting trajectories have exact last-step asymptotics, identifies sharp residual and escape constants for weakly infeasible SDPs, and classifies the role of transverse eigenvector dynamics. It unifies the favorable convex-gradient regime with the exact obstruction for reflected splitting."

Do NOT assert this claim as proven merely because it is a compelling title. Prove or rigorously correct it.
