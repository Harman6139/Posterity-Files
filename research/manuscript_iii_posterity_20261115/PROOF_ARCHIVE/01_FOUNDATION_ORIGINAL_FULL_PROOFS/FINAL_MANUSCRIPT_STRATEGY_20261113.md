# Submission strategy: exact dynamics at infinity, not another expanding omnibus

Date: 2026-11-13.
Branch: laa-track02-gptpro-analytic-frontier-20261112.
New proof: `26_ESCAPE_CONTROLLED_PROJECTION_DYNAMICS.md`.

## Decision

Make the exact rate theorem the next principal submission. It converts the earlier escape-profile work into a direct statement about two fully specified algorithms: ordinary alternating projections and a classical estimate-sequence accelerated projected-gradient scheme. This has a clearer methodological audience and a substantially shorter proof route than the explicit smooth-body target. The latter remains unproved in its strongest requested form and is NOT needed for the new paper.

The contribution is not a new momentum algorithm or the rediscovery of the usual O(1/k), O(1/k^2) inequalities. It is the two-sided conversion of a static radius profile into exact objective-decay AND iterate-growth powers without a minimizer, and its sharp all-order conic consequences. A fixed linear metric changes constants but cannot change the powers. Accelerating the specified scheme changes them exactly by a factor of two.

## Paper 1: primary submission

**Proposed title:** Escape Geometry and Exact Rates of First-Order Methods Without Minimizers

**More SDP-focused alternative:** Sharp Rates at Infinity for Alternating Projections and Accelerated Conic Feasibility

**One-sentence significance:** We determine exactly how fast residuals can vanish while iterates diverge in weakly infeasible conic problems, and show precisely what acceleration and fixed preconditioning can change.

### Draft abstract

We study convex minimization with finite unattained infimum. If the minimum distance to an objective sublevel grows as a negative power of its gap, we prove matching upper and lower power rates for both objective values and iterate norms of projected gradient. A specified accelerated projected-gradient scheme doubles both powers. Finite-dimensional semialgebraic data automatically admit the required radius profile. For weakly infeasible semidefinite systems, the theorem determines alternating-projection residual decay from the trace-escape exponent, yields sharp matrix-order-dependent rate intervals and rational endpoint examples, and shows that fixed linear preconditioning cannot change these powers. In particular every order-two weakly infeasible system has a quarter-power residual law for ordinary projections and a half-power law under acceleration. The proofs use comparator energy inequalities with approximate, rather than exact, minimizers and simultaneously control the iterates' escape to infinity.

### Theorem order and planned length

Target approximately 20–25 SIAM-format pages, not a compilation of the research log.

1. Motivation, exact problem, and a two-by-two example with an explicit recurrence.
2. Radius profile and the general two-sided projected-gradient theorem; semialgebraic nonattainment.
3. The precise accelerated algorithm, its comparator potential, and matching lower bounds.
4. Weakly infeasible SDP/SOCP specialization: equivalent profiles, sharp escape envelope and endpoint systems. Include the needed proof from manuscript 12 or a rigorous self-contained appendix; do not require a referee to accept a GitHub assertion as a theorem.
5. Fixed-metric invariance, residual/norm tradeoffs, and explicit iteration exponents.
6. A small reproducible numerical section that illustrates, but does not prove, the theorem.

The ordinary algorithmic core is short. The geometry supplies the importance: sharp dimension-only bounds, all starting points, cone-order examples, and acceleration at a nonexistent solution. Keep the optional two-basis transfer to a remark or a separate paper.

### Literature distinction

- Drusvyatskiy, Li, Wolkowicz (Mathematical Programming 2017, DOI 10.1007/s10107-016-1048-9) use singularity-degree error bounds for nonempty intersections and discuss attained displacement. Our target is disjoint sets at zero distance and an invariant at infinity.
- Sremac's Waterloo thesis (2019), Section 4.1, identifies the difficulty of extending the discussed singularity-degree definitions to weak infeasibility. We should cite this as motivation, NOT claim to have solved every singularity-degree question.
- Ochiai, Sekiguchi, Waki (Journal of Global Optimization 2026, DOI 10.1007/s10898-025-01581-7) address nontransversal affine/SOC intersections. Explain carefully why their feasible rate and our weakly infeasible rate refer to different settings and error quantities.
- Ji et al. (COLT 2020) analyze nonattainment and implicit regularization directions. We establish radius/value powers, not a new general implicit-bias principle.
- Siegel and Wojtowytsch (arXiv:2310.17610) show arbitrary slow decay for unrestricted convex nonattainment. The semialgebraic radius power is a material extra assumption.

This targeted comparison supports the problem choice; it is not an exhaustive priority certificate. The exact contribution to defend is the pair of matching rates and the sharp conic specialization, not the classical comparator inequalities.

### Venue strategy

**First target: SIAM Journal on Optimization.** Its official scope explicitly includes optimization theory, algorithms, convex programming, and variational analysis. Its current instructions normally limit papers to 25 SIAM-format pages; write to that constraint rather than expecting an exception.

**Alternative if the general theorem becomes the dominant presentation: Mathematics of Operations Research.** Its Continuous Optimization area explicitly includes conic/semidefinite optimization, first-order methods, convergence analysis, duality, and convex analysis. This is a fit judgement, not an acceptance forecast.

**Practical fallback: Computational Optimization and Applications.** Its scope welcomes algorithm analysis combined with carefully designed computational experiments. Retain the rigorous theorem and strengthen the experimental explanation of transient regimes, growth of iterates, and acceleration; do not turn the paper into an unsubstantiated benchmarking claim.

**Prestige-first alternative: Mathematical Programming, Series A.** The 2017 directly related article establishes a concrete subject precedent. Consider it if the final version demonstrates a sufficiently general, original method rather than mainly a concise corollary. It is not the recommended automatic first step under a tight calendar.

Do not submit the same manuscript simultaneously. The eight-month aspiration is not a defensible guarantee for any venue. A public preprint and archived scripts provide a stable research record while ordinary peer review proceeds. No acceptance percentage is assigned.

## Paper 2: distinct representation result, not a duplicate dynamics paper

**Working title:** Escape Rates as Lower Bounds for Semidefinite and Second-Order-Cone Lifts

This is the coherent geometry paper from 15–16 and 19: intrinsic near-optimal escape obstructs arbitrary competing lifts, with exact PSD order and SOC-factor counts for power cones, compact sections, and joins. It should not repeat the algorithmic results of paper 1 or repackage classical slack factorization as new. Cite a public version of the shared escape theorem and keep the main new lower-bound argument self-contained.

A reasonable ambitious target is Mathematical Programming, Series A; Mathematics of Operations Research or SIOPT are alternatives depending on exposition. This paper's strongest novelty comparison is against general, not merely simple/mediated-graph, power-cone representations. The resource convention must charge what it claims to count: total single PSD order, maximum block size, SOC count, and free scalar inequalities are different questions.

Draft paper 1 first. Develop paper 2 as a genuinely separate theorem package, not a promise that every milestone is an independent publication.

## Material to keep outside the initial submission

- The full two-basis compiler, quantum correlation consequences, smooth-body counting construction, and Boolean-moment succinctness barrier are different narratives. Preserve their proofs, but do not attach all of them to the dynamics paper.
- The strongest requested explicit polynomial-description, constant-accuracy, uniformly curved hard family has NOT been constructed. Its absence need not delay the independent exact-rate paper.
- Do not sell an existential family as an efficiently generated instance, a standard approximation theorem as new, or an exact-arithmetic asymptotic rate as a finite-precision infeasibility detector.
- Follow the target journal's authorship and AI-disclosure policy. A human author must understand and take responsibility for the proof and source attributions; this note does not assign authorship or submit a manuscript.

## Concrete submission package

The next deliverable should be one LaTeX paper with one theorem hierarchy, the short executable code archive already produced, and a cover letter centered on the precise two-sided rate contribution. References and provenance should identify the classical energy estimates and the preceding conic geometry honestly. Independent mathematical checking is necessary before making a journal claim, but further speculative theorem accumulation is not the priority.

### Suggested cover-letter contribution paragraph

The paper provides a radius-profile description of convex optimization without an attained minimizer. Unlike bounds involving distance to an existing solution, it controls both residual decay and diverging iterate size and gives matching lower bounds for every starting point. Its specialization determines alternating-projection rates throughout weakly infeasible semidefinite feasibility, proves sharp dimension-dependent endpoints, and characterizes the changes caused by acceleration and fixed linear metrics. The theoretical analysis is accompanied by reproducible small-dimensional experiments and an elementary exact example.

## Official venue sources consulted on 2026-11-13

- SIOPT scope: https://www.siam.org/publications/siam-journals/siam-journal-on-optimization/
- SIOPT author instructions and 25-page policy: https://epubs.siam.org/journal/siopt/instructions-for-authors
- MOR editorial statement, especially Continuous Optimization: https://pubsonline.informs.org/page/moor/editorial-statement
- COAP aims and scope: https://link.springer.com/journal/10589/aims-and-scope

This is an editorial recommendation based on fit and theorem scope, not a journal decision, a comprehensive novelty certificate, or a promised publication date.
