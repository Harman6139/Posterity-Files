# Editorial decision memo — Manuscript I against SIOPT and Journal of Nonlinear Science
_Date: 2026-11-15. This is a critical submission-readiness screen, not a manuscript-authoring prompt, and not an estimated acceptance probability._

## Decision

**Not very confident of acceptance at either journal today.** SIOPT is a serious, more natural target; Journal of Nonlinear Science (JNS) has a material cross-field-scope/desk-rejection risk. The earlier 85–90th-percentile estimate for ANA was provisional, not a measurement, and cannot be imported into SIOPT or JNS. Even proven mathematical correctness is necessary but not sufficient for editorial acceptance.

The sources in `PROOFS/02_GRAND_SPECTRAL` claim a rational gamma-2 affine–PSD counterexample, the exact circular last-step cluster set, a universal static-excess/kinetic defect principle for arbitrary semialgebraic convex cones, and an interior-leading-spectrum positive theorem. They are **the right raw ingredients** for a significant paper. The draft is not yet a confidently top-quintile *optimization* or *nonlinear-science* paper without a sharper demonstration of why the general mechanism matters to each readership.

## Primary editorial requirements

- SIOPT: https://epubs.siam.org/journal/siopt/editorial-policy requires **substantially new results**, broad interest to the optimization community, scholarly relation to earlier work, and clear English. Suggested **25 SIAM-typeset pages** (longer only exceptional). **No supplements of any kind** unless requested in review. Author guide: https://epubs.siam.org/journal/siopt/instructions-for-authors requires a stand-alone one-paragraph abstract <=250 words, minimal formulas/references, and SIAM LaTeX macros.
- JNS: https://link.springer.com/journal/332 describes a journal for fundamental description/modeling/prediction of nonlinear phenomena; original advance in a technical area **plus illumination beyond that field**. The introduction must be readable to a wide range of scientists. Its reported 9-day median **first decision** is not time to acceptance.

## Non-random contemporary comparators actually inspected (not a completed upper-quintile sample)

SIOPT:
1. J. Diakonikolas, "Pushing the Complexity Boundaries of Fixed-Point Equations: Adaptation to Contraction and Controlled Expansion," DOI 10.1137/25M1821144 (2026). New tractability frontier and parameter-free algorithm with almost tight complexity, general normed/geodesic spaces.
2. Lee–Papp–Varga, "Dual Certificates of Primal Cone Membership," DOI 10.1137/25M1769934 (2026). Constructive primal cone-membership certificates and actual numerical/exact-arithmetic transfer, broad classes of nonnegative-polynomial cones.
3. Ouyang–Milzarek, "Variational Properties of Decomposable Functions. Part I," DOI 10.1137/24M1686140 (2026). New epi-calculus and equivalences linking proximity regularity, strict complementarity and metric regularity across function classes.
4. Boţ–Chenchene, "Extragradient Method with Flexible Anchoring," DOI 10.1137/24M1703562 (2026). A concrete method, strong convergence and sharp residual rates.
5. de Oliveira–Sessa–Sossa, "Measuring Dissimilarity between Convex Cones by Means of Max-Min Angles," DOI 10.1137/25M1794371 (2026). A new conic geometry invariant plus a computational method and application.

JNS:
1. Buza–Haller, "Existence of Spectral Submanifolds in Time Delay Systems," DOI 10.1007/s00332-026-10327-y (2026). Reusable invariant-manifold theory for a dynamical class, not just one equation.
2. Cândido–Novaes–Rivera, "Limit Tori in Non-smooth Systems," DOI 10.1007/s00332-026-10328-x (2026). General analytic method detecting genuine nonsmooth invariant tori.
3. Straube et al., "Unfolding the Geometric Structure and Multiple Timescales of the Urea–Urease pH Oscillator," DOI 10.1007/s00332-026-10336-x (2026). Nonlinear timescale mechanism directly tied to observable chemical oscillations.
4. Berlyand–Krupchytskyi–Laux, "Change of Bifurcation Type in 2D Free Boundary Model of a Moving Cell," DOI 10.1007/s00332-026-10313-4 (2026). New dynamical bifurcation caused by a specified nonlinearity.
5. Shi–Shi–Wang, "A Nonlocal p-Laplacian Interface Model with Sharp Interface," DOI 10.1007/s00332-026-10323-2 (2026). New energy-based PDE interface method with implications beyond one interface.

**These are targeted 2026 comparator readings, not a predeclared 10-per-venue full-results/full-proofs percentile study. No 8/10 superiority claim is supported.**

Recent LAA **style** reference, not a target for these two submissions: (i) Bourin–Lee, "Some hybrid matrix triangle inequalities", DOI 10.1016/j.laa.2026.06.033, opens from a named recent inequality and says exactly what it refines; (ii) Kian–Rostamian Delavar–Krnić, "Characterizations of completely positive trace preserving majorants", DOI 10.1016/j.laa.2026.02.035, puts the constructive result and necessary/sufficient conditions in the first abstract sentences; (iii) Pikul et al., "Joint numerical ranges of three Hermitian 4x4 matrices", DOI 10.1016/j.laa.2026.05.014, gives a comprehensible object before its fine classification. Borrow **editorial structure** (problem → exact known limitation → new theorem → consequence), not text or distinctive wording.

## Exact mathematical and substance gaps; tiers

### Tier 0: indispensable even for a credible submission

- Independently verify the all-time gamma-2 analytic spectral chamber: every Riccati coefficient, uniform eigenvalue-sign margin, exact error hierarchy, corrected quartic amplitude and rational entry. Distinguish gamma=1 switching orbit (still open) from the gamma-2 rational counterexample (claim depends on uniform trapping). Avoid implying the former is solved.
- Recheck the universal static-excess energy law and equivalences for arbitrary **non-self-dual semialgebraic cones**, including redundant affine equations and hidden bounded-excess assumptions.
- Fix the severe scholarly-positioning deficit: the current 60 KB manuscript `spectral_transport.tex` has only four bibliography items (BGV, LRY, DJK and Ryu). Add rigorous comparative accounts of Douglas–Rachford/Lions–Mercier, Pazy, cosmic results, conic pathologies, monotone splitting and modern last-iterate/complexity works, and exact theorem-level distinctions.
- Make the paper stand alone. Every nonclassical proof needed for the headline result belongs in the paper. SIOPT does **not** allow supplementing with an unpublished GitHub proof instead of meeting its 25-page limit. Re-typeset in SIAM format before claiming page compliance.

### Tier 1: one new **substantive SIOPT** theorem (highest priority)

Prove an optimization-facing consequence **not just another asymptotic description of the constructed orbit**. Candidates, in decreasing directness:

**A. Universal natural-scale bound or sharp obstruction.** For every weakly infeasible affine–PSD DRS system with state power p, establish
```
||Z_(k+1)-Z_k|| = O(k^(p-1))
```
without the existing *bounded static-excess* hypothesis, OR rigorously disprove this bound and give the sharp general replacement upper-rate classification. This would materially increase the utility of the universal theory.

**B. A directly checkable spectral certificate for velocity convergence/failure.** Starting from affine/PSD input or finitely determined spectral/Puiseux data, provide sufficient/necessary conditions identifying when the excess tends to zero, and derive exact rate/residual consequences. Distinguish from defining a test that simply restates the desired infinite-trajectory limit.

**C. A real algorithmic implication.** Transfer the circular counterexample to a standard explicitly defined ADMM formulation with exact primal/dual residual statements; then establish a quantitatively sharp, implementable averaging/certification rule that recovers reliable decay information for a meaningful wider class. Merely noting DRS–ADMM equivalence without the right metrics and updates is insufficient.

For SIOPT, **one successful A or B, plus honest C if possible**, would significantly improve the substance/acceptance case. An attractive new numerical example alone would not.

### Tier 2: significant **JNS-specific** mathematics

Prove a **robust nonlinear resonance-at-infinity theorem** with transparent hypotheses, a stable positive-amplitude circle or other cluster set, and a spectral/averaging mechanism that survives nontrivial perturbations **of the operator or underlying affine data** (not only a parameter interval and relatively open starts inside one invariant block). Apply it to a second independently motivated projected/nonsmooth nonlinear evolution or continuous-time flow, or another genuine nonlinear model. Explicitly show what physical/dynamical phenomenon the theorem explains and why it is not just a change of names for one SDP projection iteration. This would address JNS's requirement to illuminate issues beyond the originating specialty.

The original gamma=1 switching orbit is **not needed** to refute the universal proposition, but resolving its neutral-charge crossing and its coupled phase/amplitude dynamics would be a strong way to generalize the spectral mechanism and would materially help JNS.

### Tier 3: a true upper-quintile shared flagship

A theorem characterizing, for a broad class of semialgebraic firmly nonexpansive/conic splitting maps, the **spectral transport at infinity** into (a) exact radial last velocities and (b) bounded nonzero transverse resonances, with testable hypotheses and at least one application outside affine–PSD feasibility. This should genuinely subsume the regular-spectrum result and the gamma-2 family. The static-excess criterion can be part of the proof, but the main theorem should *predict* the phenomenon from geometry rather than from observed infinite-trajectory excess.

## Manuscript packaging if/when these gates pass

Do **not** attempt one unchanged introduction/abstract for the two journals. Keep the mathematical proofs and core structure shared, but use:
- **SIOPT** front end: weak infeasibility and why practitioners need reliable last-iterate information; false expectation; explicit counterexample; general theorem and rate/certificate; no extrapolation of a state little-o; clear limits.
- **JNS** front end: nonlinear systems can head toward one direction while their microscopic motions circle; stable spectral resonances at infinity; transparent normal-form mechanism; why the result illuminates other nonlinear dynamics; concrete second model.
- Both: plain-language 150–200-word abstract, 2–3-page introduction; define projection, PSD, weak infeasibility before operator notation; state **one surprising negative result plus one explanatory positive/general result** before proof machinery; put matrix-entry bookkeeping after the main results; avoid promotional language or unearned 'fundamental breakthrough' claims.

### Editorial final decision

**Do not claim 'very very confident' acceptance, a verified top-20% rank, or ready-to-submit status today.** SIOPT is the stronger target *conditionally*; JNS is a substantial scope stretch. The best next investment is one substantive optimization-facing theorem for SIOPT and, if both journals remain desired, a genuinely general and robust nonsmooth-dynamics theorem for JNS. Manuscript polish cannot substitute for either.
