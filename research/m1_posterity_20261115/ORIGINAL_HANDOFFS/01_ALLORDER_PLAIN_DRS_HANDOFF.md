# PRO RESEARCH HANDOFF 01 — A UNIVERSAL LAST-ITERATE THEOREM FOR PLAIN DOUGLAS–RACHFORD ON WEAKLY INFEASIBLE SDPS
**Prepared 2026-11-14.** Independent fresh Pro chat. Research Track I of three. **Read the entire file before starting mathematical work.**

## A. The nonnegotiable research problem

Prove or rigorously refute the following exact all-dimensional conjecture, without assuming a low matrix order, one Lorentz block, a special starting point, nonsingular equality data, or a regular face.

Let \(m\ge2\), let \(\mathcal A:\mathbb S^m\to\mathbb R^q\) be any real linear map, and suppose \(b\in\overline{\mathcal A(\mathbb S_+^m)}\setminus\mathcal A(\mathbb S_+^m)\). Put
\[
U=\{X\in\mathbb S^m:\mathcal A(X)=b\},\quad K=\mathbb S_+^m,
\qquad
T(Z)=Z+P_K(2P_UZ-Z)-P_UZ.
\]
All projections use the Frobenius metric. Iterate **plain, unanchored** Douglas–Rachford \(Z_{k+1}=T(Z_k)\), for arbitrary \(Z_0\in\mathbb S^m\).

Previous project work has derived a common, nonzero leading state vector \(V\) and positive rational \(p<1\):
\[
Z_k=Vk^p+o(k^p),\quad p=\frac{\alpha}{1+\alpha},
\]
where \(\alpha>0\) is the minimum-trace escape exponent \(R_b(\delta)\asymp\delta^{-\alpha}\). The proposed **missing theorem** is the genuine vector LAST-ITERATE law
\[
\boxed{k^{1-p}(Z_{k+1}-Z_k)\longrightarrow pV\quad\text{for all }m,\mathcal A,b,Z_0.}\tag{I}
\]
Consequences to derive if true: exact leading constants for \(\|Z_{k+1}-Z_k\|_F\), primal cone shadows and equation residuals; analyze possible vanishing of the leading unwhitened residual vector under redundant or ill-conditioned data. Do not call a norm-order statement, an averaged/ergodic rate, or an anchored algorithm a proof of (I). Do not differentiate an \(o(k^p)\) state remainder.

If (I) is false, give an **explicit rational affine–PSD SDP** (not an arbitrary firmly nonexpansive resolvent), prove the claimed oscillatory/nonconvergent last-step behavior in exact mathematics, and derive the strongest correct replacement universal theorem with a sharp necessary/sufficient or structurally meaningful criterion. A standalone non-PSD counterexample or another isolated small example is not a sufficient flagship breakthrough.

### Required mathematical insight

The hard issue is ruling out a transverse component that is lower order in \(Z_k\) but survives at the \(k^{p-1}\) last-step scale. An existing real-analytic semialgebraic firmly nonexpansive resolvent has such a rotating transverse step (Milestone 35). A positive universal theorem must exploit properties **specific to an affine subspace paired with the PSD cone**: firm projections, monotone operator splitting, matrix spectral geometry, facial recession chains, or an invariant at infinity unavailable to general firmly nonexpansive maps. Find the organizing analytical invariant, rather than checking matrix orders case by case.

## B. Published mathematical context and source packet

Connected GitHub repository: Harman6139/Posterity-Files.
Immutable existing research baseline (prior to these prompts): commit **22ed4becd320695b41f8a11f1223ea090ef89ecf**, branch laa-track02-gptpro-analytic-frontier-20261112.
Main directory:
https://github.com/Harman6139/Posterity-Files/tree/22ed4becd320695b41f8a11f1223ea090ef89ecf/research/laa_two_basis_track02_20261112

You must fetch and read the full documents, not merely these notes:

1. **30_TAME_COSMIC_CONVERGENCE_AND_POWER_LAWS.md**: for fixed-point-free semialgebraic nonexpansive maps, discounted path \(z(t)\) has a Puiseux leading term and all unanchored orbits share \(V k^p+o(k^p)\). This DOES NOT imply the step law.
2. **31_COMMON_LEADING_DIRECTION_FOR_MONOTONE_METHODS_AND_DRS.md**: plain DRS on every weakly infeasible SDP has an initial-condition-independent leading matrix and a nonzero PSD recession shadow; escape exponent relation \(p=\alpha/(1+\alpha)\); actual unanchored residual law left open.
3. **35_ANALYTIC_FIRM_COUNTEREXAMPLE_TO_LAST_STEP_ASYMPTOTICS.md**: explicit \(3\)-dimensional analytic semialgebraic firmly nonexpansive \(T=(I+M)^{-1}\) with \(z_k\sim5^{1/5}k^{1/5}e_0\) but a circular cluster set of \(k^{4/5}(z_{k+1}-z_k)\). It is NOT of the special affine/PSD DRS form. An analytic shortcut is therefore invalid.
4. **36_EXACT_LAST_STEPS_FOR_ALL_SINGLE_LORENTZ_WEAK_INFEASIBILITY.md**: complete universal **one Lorentz cone** case, any dimension and start. With \(c=\operatorname{dist}(0,U)\), \(z_k/\sqrt{k}\to\sqrt2\,c\,e\), \(\sqrt{k}(Tz_k-z_k)\to c e/\sqrt2\); includes all real and Hermitian order-two SDP systems. Detailed normal form and recurrences. Do not merely reprove this.
5. **40_EXACT_VELOCITIES_AND_FINITE_ANGULAR_MOTION.md**: crucial new **all-order ALTERNATING PROJECTIONS** and convex forward–backward results, with exact state velocity, objective/decrement constants, asymptotic minimum-radius efficiency and finite normalized-state angular length. The result covers arbitrary-order SDP alternating projections, NOT arbitrary-order plain DRS. Its proof uses convex objective subgradients and tail-energy secants; investigate which part transfers or fundamentally fails for the DRS operator. Read its status in 00_MANUSCRIPT1_EXACT_VELOCITY_STATUS.md.
6. **12_RECIPROCAL_ESCAPE_LAW_AND_SHARP_DIMENSIONAL_BOUNDS.md** and **26_ESCAPE_CONTROLLED_PROJECTION_DYNAMICS.md**: static conic escape profiles and the accelerated/ordinary alternating-projection rates.
7. **28_HALPERN_SPLITTING_RATES_AT_INFINITY.md**: exact anchored Douglas–Rachford rates, with exact primal/operator radius identity for affine \(U\). Anchoring is not plain DRS.

Outside literature (inspect primary texts and any 2026 updates, rather than relying on this summary): Pazy on nonexpansive linear drift; Bauschke–Douglas–Moursi on cosmic convergence; Ryu's counterexample; Bolte–Gaubert–Vigeral on definable discounted paths; Liu–Ryu–Yin on pathological conic DRS/ADMM; Park–Ryu on accelerated infeasibility detection; and 2026 Do–Jentzen–Kuckuck on continuous-time definable finite spherical length. These are antecedents, not automatically the new theorem. Search specifically for post-2024 all-order DRS last-step results before claiming originality.

## C. Fully specified success standard — manuscript and journal

The purpose is to change **Manuscript I** from an interesting specialist paper into a truly significant discrete nonexpansive-dynamics result. First-choice publication audience: **Advances in Nonlinear Analysis** (reported 2025 median acceptance 6.9 months; PDE-heavy actual output); natural subject audience: **Journal of Convex Analysis** (publisher changed in 2026; turnaround unknown). Upgrade target: **Bulletin of the London Mathematical Society** or **Proceedings of the AMS**, ONLY if broad mathematical novelty is genuinely demonstrated. The user wants acceptance within eight months after submission, assuming no revisions; no journal or proof can guarantee this.

The requested editorial screen criterion is **upper quintile by published-paper substance**, NOT a literal 80% probability of an editor accepting. You may call it a credible "80th-percentile paper" ONLY after all of these pass:

* Independently verify exact statement and proof, with adversarial attention to pathological affine fibres, infinite-dimensional-looking recession behavior in finite dimension, data scaling, spectral multiplicity and all starts.
* Prove (I) in full, OR give a precise affine/PSD disproof and an equally substantive universal corrected theorem. No weak cases, generic-map counterexample, or speculative proof route counts.
* Establish actual novelty against primary literature as of the submission date; distinguish the 2026 continuous-gradient spherical-length result and old cosmic results.
* Choose at least **10 published research papers per proposed journal** from at least TWO identifiable 2024–2026 issues or volumes, under a predeclared reproducible sampling rule (e.g., fixed-seed random sampling from publisher article lists plus 3–5 closest-topic benchmarks). Read full results and proofs where accessible. Score theorem novelty, depth, generality, reuse by other subfields, clarity, and audience fit separately. Test whether this manuscript genuinely matches/exceeds at least **8/10** sampled publications on a defensible composite substance rubric, with no failed correctness or priority gate. Report comparator DOIs, article-level distinctions, sampling bias, and uncertainty. Five accepted articles is NOT enough to infer editorial probabilities.
* Deliver a coherent self-contained 18–25-page LaTeX manuscript with exact hypotheses and citations, emphasizing one theorem and a small set of high-value applications. No omnibus inclusion of 40 historic milestones. Compare editorial fit and actual fresh median submission-to-final-acceptance dates (source and sample sizes), or explicitly mark timing as unverified.
* Never equate a top-quintile comparison with a calibrated >=80% chance of desk acceptance. The "80%+" language is a research-quality **target**, not an empirically established probability.

If the mathematics cannot be fully closed, continue attacking the central invariant during the available attempt; do not rebrand partial results as resolution, and do not generate another merely illustrative example. At the end, report exactly what is/not proved rather than inventing success or implying work continues in the background.

## D. Deliverables and GitHub hygiene

Work on a NEW dedicated research branch, e.g. research/pro-m1-allorder-drs-20261114, starting at the immutable baseline or this handoff branch. Read all failed routes above before choosing an approach. Commit full proof (or disproof and universal replacement), a minimal independently runnable symbolic/numeric check (supporting, never substituting for proof), complete literature-priority map, and a submission-ready .tex manuscript to that branch. Do not overwrite milestones 01–40; keep a clear exact-result status file. If no GitHub write permission, produce uploadable standalone files and say so.

**Start by identifying the one missing PSD-geometric lemma; then prove it or construct the exact SDP obstruction. Your output is successful only if the all-order problem and publication-quality gate are genuinely closed.**
