# CODEX MASTER EDITORIAL BRIEF — MANUSCRIPT II / LINEAR ALGEBRA AND ITS APPLICATIONS
**Date:** 2026-11-15. **Role:** Codex drafting and critical editorial agent. **Assignment:** turn the existing, fully specified ordinary-completely-positive all-local-rule theorem into one rigorous, compelling, concise, LAA-submittable mathematical research paper. This is a writing, verification, and packaging assignment, NOT a request to invent more theorems.

## 0. The single decision that governs the manuscript

Write ONE focused paper around:

> **Every strictly improving adjacent pivot rule can take exponentially many steps to find a copositive separator, even on positive definite matrices with all entries positive; nevertheless a short exact separator already exists. A general edge-movement theorem explains why all such local rules are trapped.**

That is the primary contribution. Do not make a survey, an omnibus of 40 milestones, a generalized-arithmetic-carrier treatise, or a second Lorentz rational-factorization paper. Those are separate works. The LAA reader should remember *one simple contrast*: **very long local pivot path versus short global matrix certificate**, plus the geometric reason.

Suggested title (preferred):
**Exponential pivot paths and short certificates in completely positive matrix separation**

Alternatives only if substantively better:
- *Long local paths in completely positive matrix separation*
- *Canonical pivot paths in completely positive matrix separation*
- *A local–global complexity gap for completely positive matrices*

Avoid "grand", "fundamental", "breakthrough", "universal", "spectacular", or vague slogan titles. The lead result is exceptional precisely because it has an exact theorem, not because of adjectives.

**Positioning:** this is a finite-dimensional LINEAR ALGEBRA paper about the completely positive/copropositive matrix-cone pair and geometry of perfect forms. Algorithmic complexity is the surprising consequence; it must not read like a narrowly specialized operational-research implementation note.

## 1. Source-of-truth mathematics — inspect all primary files before drafting

**Authenticated GitHub repository:** Harman6139/Posterity-Files.

**Pinned current ordinary-CP flagship results branch:**
research/pro-m2-ordinary-cp-canonical-all-rules-20261115
**Verified head at brief preparation:** 11ffd7fe0e83b7eda47459d1d9b90b7358a4fcfc.

**DIRECT SOURCE MANUSCRIPT — read entire text:**
https://github.com/Harman6139/Posterity-Files/blob/11ffd7fe0e83b7eda47459d1d9b90b7358a4fcfc/research/pro_m2_ordinary_canonical_20261115/release/manuscript/MAIN.tex

**PROOF STATUS — read entire text:**
https://github.com/Harman6139/Posterity-Files/blob/11ffd7fe0e83b7eda47459d1d9b90b7358a4fcfc/research/pro_m2_ordinary_canonical_20261115/release/STATUS_PROVED_NOT_PROVED.md

**DISCOVERY/PROOF CHECKPOINTS — read entire text:**
- research/pro_m2_ordinary_canonical_20261115/00_CHECKPOINT_BOUNDED_EDGE_MOVEMENT.md
- research/pro_m2_ordinary_canonical_20261115/01_PROOF_AND_FRESH_VERIFICATION.md
- research/pro_m2_ordinary_canonical_20261115/release/README_AND_SCOPE.md
- release/code/generate_certificates.py
- release/code/verify_certificates.py
- release/certificates/verification_report.json
- release/certificates/rebuild_and_remote_hashes.json

**Background proofs to read, but NOT merge into this paper:**
- quant branch research/pro-m2-quantitative-checkpoints-20261114, commit 98740002955f5bd9763137fc583a8d897b136ffe: checkpoints 01–09, for earlier one-rule canonical/shadow and sharp margin bounds.
- all-local generalized-cone branch research/pro-m2-all-local-obstruction-20261115, commit ea809bed847d103a4c586428972d0aeda1b4d9d1: earlier nonsimplicial result; now surpassed in the relevant ordinary cone/canonical model.
- source branch laa-track02-gptpro-analytic-frontier-20261112, commit 22ed4becd320695b41f8a11f1223ea090ef89ecf, especially milestone 37 for finite lattice certificates and earlier shadow rule.
- grand arithmetic-carrier and quadratic/Lorentz branches may inform a ONE-SENTENCE outlook only; do not splice their proofs here.

**Do not assume verification because a file is named PROVED.** Read the main argument line by line, check every constant and quantifier, rerun the two independent exact scripts and verify reported hashes. Fix errors with transparent mathematical justification, never quietly weaken the result while retaining a stronger abstract. If a central assertion fails, halt submission claims and document the issue rather than cosmetically rewriting it.

## 2. First page: explain the problem in everyday matrix language

Assume the reader knows elementary symmetric matrices, positive semidefiniteness, outer products, and eigenvalues, but has NEVER heard of a "copositive Ryshkov set", "perfect form", "minimum-ratio shadow", or "arithmetic exposure gap".

The first 200 words must explain:
1. **What kind of matrix?** A real symmetric matrix A is **completely positive** when \(A=\sum_j u_j u_j^\top\) for vectors \(u_j\ge0\) coordinatewise. It follows that A is positive semidefinite and entrywise nonnegative; the converse fails starting at order five. These are basic well-studied cones in matrix factorization and quadratic optimization. Cite the standard primary literature, not unverified applications.
2. **How do we prove failure?** A symmetric W is **copositive** when \(x^\top W x\ge0\) for every x>=0. If \(\langle A,W\rangle<0\), W is a *certificate* that A is not completely positive. That is an exact checkable mathematical statement, not a certificate that W itself can always be verified efficiently in variable dimension.
3. **Why would we walk among matrices?** One family of exact certificate procedures searches among neighboring **perfect copositive matrices**. A pivot is one move along a shared edge in a locally polyhedral matrix set. Strict decrease of the pairing \(\langle A,P\rangle\) looks like progress, but how many such moves might be necessary? This is the actual problem.
4. **What is surprising?** All possible locally improving edge choices can be slow even if A is positive definite, has no zero entries, and an explicit short separating W exists. So "any local improving choice" cannot serve as an efficient substitute for global certificate construction. This is a carefully delimited finding, NOT a lower bound for all algorithms.

Do NOT begin the abstract or introduction with \(\mathcal R_n\), \(\operatorname{Min}(P)\), high-dimensional integer vector enumeration, or the huge construction parameter N. The reader should first understand the mathematical problem in words.

**Avoid the common misleading terms:**
- "positive matrix" is ambiguous: say *positive definite* or *entrywise positive* separately.
- "certificate is easy" can imply a polynomial-time general cone-membership oracle: instead say *these instances have explicitly given rational separators with short binary descriptions*.
- "every algorithm" is false: only EVERY **strictly objective-descending extreme-ray adjacent-pivot rule, starting at the canonical vertex**, with the specified current-vertex/ray/identity-corrected-ray exits.
- "all dimensions" is false for the new strongest theorem: require **each fixed n>=5**.
- "time is exponential" is too strong unless the model includes overhead: say **number of adjacent pivots is exponential in input bit length**. The arithmetic cost of each pivot is a separate resource.
- "robust for every compact encoding" is false: robustness is for a ball, while arbitrary rational perturbations can have longer encodings.
- "disproves the 2021 conjecture" is false: its Conjecture 3.2 asks for FINITE TERMINATION under a suitable rule, not polynomial pivot complexity.
- "one possible rule" undersells the new result: the theorem controls all permitted descending edge choices and their branching.

## 3. EXACT primary theorem to place prominently, without clutter

Write \(\mathcal{CP}_n=\operatorname{cone}\{uu^\top:u\in\mathbb R_+^n\}\) and \(\mathcal{COP}_n=\mathcal{CP}_n^*\). The canonical perfect matrix \(T_n\) has diagonal ones and -1/2 on adjacent offdiagonal positions.

From source MAIN.tex (verify exact details), for EVERY n>=5 and integer t>=1 the authors give a rational center A=A(n,t) with total binary encoding \(O_n(\log(t+1))\) and a Frobenius perturbation radius rho(n,t)>0 such that:
- every matrix in the rho-ball is norm<=1, positive definite, strictly entrywise positive, and **not** completely positive;
- every rule starting at T_n and selecting an extreme tangent ray with negative objective pairing to A must make at least t bounded adjacent-vertex pivots. This includes adaptive and randomized tie-breaking, not arbitrary algorithms. Every improving option is covered.
- neither the current-vertex test, a copositive-ray test, nor any scalar identity adjustment R+tau I of the chosen improving ray supplies a separator during those t steps;
- one explicitly given RATIONAL strictly copositive separator W works for the entire ball, has bounded norm, a positive cone margin and negative pairing, and a short binary description for the compact centers.

State the precise constants in the FORMAL theorem after the reader sees the concepts. Give a clean qualitative "For each n>=5, there are instances of O_n(log t) bits requiring t steps" corollary before the construction. State the quantitative robustness in a separate following theorem or subpart. Main theorem must not be "dumbed down" mathematically.

**One proof mechanism with broader linear-algebra value:**
For a fixed positive-definite leading block H, a bounded edge in the associated Ryshkov quadratic epigraph changes a cross-block coordinate by no more than
\[
|b_i'-b_i|\ \le\ \tfrac12+2\sqrt{H_{ii}}.
\]
For the canonical tridiagonal block \(H=T_{n-1}\), this is **5/2** independent of matrix order and choice of adjacent edge. This is the memorable technical theorem. It shows that no edge move makes an arbitrarily large jump in the needed cross-block direction; a carefully scaled target then makes all possible improving choices remain inside the constrained face for a long time.

Define "edge" and "cross-block coordinate" with one ordinary block-matrix display before stating the quantitative lemma. Do not incorrectly claim *all* entries of *all* perfect-form edges are bounded by 5/2.

**Global certificate contrast:** the short separating matrix W is part of the theorem, not a separately discovered general polynomial-time algorithm for variable n. Explain what it proves and does NOT prove.

The all-choice result should appear visibly in the TITLE, last third of ABSTRACT, and first two pages of INTRODUCTION. The geometric bound should appear in intro as an accessible explanation and in the theorem hierarchy before its proof.

## 4. Abstract — use this as a carefully checked STARTING DRAFT, not mandatory verbatim

Target a SINGLE **145–180-word paragraph**. The first sentence defines the subject; the second states the natural problem; the third reveals the result; the remainder gives its mechanism and consequence. No formulas beyond perhaps n>=5 and "exponentially", no citations, no promises, no rhetorical adjectives.

**Editorial starting draft (original prose, may be revised for precision):**

"A symmetric matrix is completely positive if it is a sum of outer products of nonnegative vectors. One way to prove that a matrix is not completely positive is to move between neighboring perfect copositive matrices until a separating certificate is found. We show that such local searches can require exponentially many pivots even when a short certificate exists. For every fixed matrix order at least five, we construct rational matrices that are positive definite and have strictly positive entries but are not completely positive. Starting from the standard tridiagonal perfect matrix, every rule that follows a strictly improving extreme edge must take exponentially many adjacent steps in the input bit length. This behavior persists under small perturbations and cannot be avoided by adding a scalar multiple of the identity to the selected ray. The proof uses a bound on coordinate movement along edges of a fixed-block matrix polyhedron. Each instance nevertheless has an explicit rational copositive separator of short description."

This is a suggested **communication structure**, not an independent verification of any theorem or a source quotation. Refine until every clause matches MAIN.tex. Consider whether the "scalar correction" clause is too detailed for the abstract; if so move it into the introduction and use the word budget for the more meaningful contrast instead.

Do not write "we establish a foundational new paradigm", "far-reaching applications", "paradigm shift", "for the first time", or "the algorithm is practically useless". Do not make claims of guaranteed novelty or journal acceptance.

## 5. Introduction — precise paragraph-by-paragraph plan (aim ~700–1000 words)

**Paragraph 1 — one simple matrix definition and why it matters.**
Open in plain mathematical English, with \(\mathcal{CP}_n\) in ONE display or inline. Distinguish it from positive semidefinite and entrywise nonnegative, explain why n>=5 is the first nontrivial regime. Mention factorization/optimization as genuine motivation, with 1–2 accurate citations only.

**Paragraph 2 — the positive certificate idea.**
Explain the dual copositive test and the meaning of negative trace pairing without invoking abstract duality vocabulary first. "A single such W proves nonmembership." State that the certificate size matters even when discovering it is difficult.

**Paragraph 3 — neighboring matrix search as a natural strategy.**
Introduce "perfect" only after a friendly description: their integer minimal vectors determine them, and neighboring perfect forms define a graph of matrix certificates. A local pivot walks along one edge to another vertex while lowering a linear objective. Cite Dutour Sikirić–Schürmann–Vallentin (2020 online/2021 volume) and Dannenberg–Schürmann (2023), giving their actual contributions rather than one vague cluster of citations.

**Paragraph 4 — pose the sharp question.**
"Can a rule that always makes progress still take extremely many steps?" Explain that finiteness does not say anything about binary complexity. Use a human-intuitive illustration: a rational matrix may have few digits while the local walk visits many intermediate perfect matrices. State whether the question is specifically about rules restricted to adjacent edges, not all cone algorithms.

**Paragraph 5 — give the NEW result NOW.**
At n>=5, robust strictly positive PD rational nonmembers, canonical start, ALL improving extreme choices, exponentially many pivots, short explicit separator. No algebraic parameter definitions yet. This should be the clearest paragraph in the article and survive reading aloud.

**Paragraph 6 — explain the math behind the surprise.**
Mention the fixed-block edge-movement estimate as the main structural idea; describe that adjacent perfect matrices cannot change a key cross-block coordinate by more than a constant, and arithmetic scaling prevents a local route from escaping the slow face. ONE displayed block picture or inequality if helpful. Do not write detailed Dirichlet/Cramer calculations here.

**Paragraph 7 — explain EXACTLY the scope and novelty, with proper credit.**
The original 2021 conjecture is finite termination under a suitable pivot rule (not a polynomial bound). 2023 perfect-form geometry and shear/adjacency are earlier work. This paper's claimed difference is a robust all-choice quantitative lower bound **in the ordinary CP cone with canonical start**, supported by a dimension-independent edge-movement lemma and short global separator. It neither lower-bounds arbitrary nonlocal algorithms nor refutes the original finite-termination conjecture.

**Paragraph 8 — brief roadmap (optional, one or two sentences).**
E.g. define the local model and theorem; prove edge movement; build hard matrices; force all local choices and verify the global certificate. Avoid generic section-by-section paragraph if the manuscript is already clearly signposted.

Definitions must be introduced at first mention. No jargon in a sentence before it is explained. Do not introduce the long formula \(N=20000n^3 E^2\) until the proof/construction section. Aim for a clear statement of novelty within the FIRST PAGE, not page 5.

## 6. Proposed minimal full-paper architecture

**Target: roughly 14–18 pages INCLUDING references**, ideally 15–16. If mathematical correctness truly requires 19–21 pages, retain the proof; never hide a logical gap to hit a page target. Original source is nine pages of fairly compressed mathematics, so devote the extra pages to clarity, not extra unrelated results.

Suggested structure:
1. **Introduction** (~1.5 pages). Accessible question + immediate result, as above.
2. **The local problem and main result** (~2 pages). Define CP, COP, perfect forms/Ryshkov region only now, certificate exits, canonical start, all-choice quantifiers, precise full theorem, a two-line discussion of binary complexity. A small n=5 example may be useful if actually derived from source and not numerically embellished.
3. **Why an adjacent edge cannot move far** (~2.5–3 pages). State and prove the fixed-positive-definite-block movement lemma; explain why arbitrary denominator active lattice vectors and degeneracy are handled. This is the broadly reusable linear algebra/geometric core.
4. **Hard positive matrices and their short separators** (~2.5–3 pages). The explicit five-cycle/Horn based construction, diagonal scaling and small perturbation, strict PD and entrywise positivity, non-CP via explicit W, binary heights. Define technical constants only here.
5. **Why every local pivot is forced to remain slow** (~3–4 pages). Exposed fixed-block face, arithmetic gap, bound on primitive tangent ray entries, dominance of the leading objective term, bounded neighboring edges, induction simultaneously over every improving choice. Cover all allowed certificate exits, including scalar identity ray corrections, without silently granting unrelated global tests.
6. **Consequences and scope** (~0.5–1 page). Explicit distinction between pivot count and separator size; explain alternatives without claiming a new universal polynomial separation algorithm. One concise line on what genuinely transfers to other matrix-cone settings, if already proved, and one well-phrased open question. No extra half-page of grand claims.
7. **References** (accurate DOIs, all cited results).

If the edge-movement proof can be integrated into section 3 while keeping the entire article shorter, do so. No separate "Methods", "Results", or "Discussion" copied from applied science: LAA mathematics articles use normal theorem/proof sections. Technical scripts/certificate dumps belong in an online supplement or repository, not the main text.

**Theorem hierarchy**: one headline all-rule theorem, one standalone edge-movement lemma/theorem, one construction/separator lemma, one all-choice confinement lemma, one short binary-complexity corollary. Avoid dozens of numbered theorems or irrelevant quantitative embellishments in the abstract/intro. Never omit constants needed for a valid proof.

## 7. Actual recent LAA models — sampled and checked as of 2026-11-15

These are REAL 2025–2026 published LAA research articles, not invented acceptance examples. For this assignment their role is **editorial-form examples** (title, abstract, introduction, level of background), not a biased success-percentile comparison. Follow the *discipline of exposition*, not their copyrighted sentences or their exact subject-specific notation. Read the linked publisher abstracts and the full introduction where accessible, and independently retrieve the current 2026 LAA author guide.

| Journal article (volume/year) | Verified DOI / record | What to learn for OUR paper |
|---|---|---|
| Kubjas & Metsälampi, **Geometry of low nonnegative rank matrix completion**, 744 (2026), 82–116 | https://doi.org/10.1016/j.laa.2026.04.032 | Particularly good intro model: first define factorization in simple algebra, connect to practical matrix completion, state the precise gap, list key mathematical results in ordinary language, then short roadmap. Full HTML introduction was accessible. |
| Gabl, **Conic optimization techniques yield sufficient conditions for set-completely positive matrix completion under arrowhead specification pattern**, 731 (2026), 215–251 | https://doi.org/10.1016/j.laa.2025.11.011 | Begin with a problem the field already recognizes, explain which prior direction is being reversed, identify exactly TWO ways the theorem extends previous work, connect to quadratic optimization. This is the closest subject-style reference. |
| Nishijima & Lourenço, **Facial structure of copositive and completely positive cones over a second-order cone**, 743 (2026), 211–249 | https://doi.org/10.1016/j.laa.2026.04.019 | Very lean abstract: a precise classification result, geometric consequences, then outlook. Strong close-topic prestige benchmark; no unearned superlatives. |
| Das & Dmytryshyn, **Bundles of skew-symmetric matrix pencils and their minimal degenerations**, 744 (2026), 53–81 | https://doi.org/10.1016/j.laa.2026.04.029 | Start with an intuitive perturbation problem; explain basic matrix notions; pose natural questions and answer them. Author's published-version intro is available at https://research.chalmers.se/publication/552056/file/552056_Fulltext.pdf . Do not reproduce wording. |
| Cheung & Shader, **The strong singular value property for matrices**, 746 (2026), 213–245 | https://doi.org/10.1016/j.laa.2026.05.019 | Extremely compact abstract: define a new matrix property and say what matrix problem it solves. An example that brevity need not sacrifice mathematical weight. |
| Štrekelj & Zalar, **Construction of exceptional copositive matrices**, 727 (2025), 368–384 | https://doi.org/10.1016/j.laa.2025.08.010 | Begin with basic copositivity/complete positivity definitions and then give specific construction results. Direct topical precedent for not assuming the reader knows the cones. |
| Elsinger, Orzel & Welters, **Bessmertnyĭ realizations of symmetric multivariate rational matrix functions over any field**, 737 (2026), 80–118 | https://doi.org/10.1016/j.laa.2026.02.014 | Name one broad representation theorem, distinguish the symmetric case, and give the necessary counterexample boundary. Strong general matrix-theory framing. |
| Benner & Van Dooren, **On commuting matrices and pencils**, 738 (2026), 25–44 | https://doi.org/10.1016/j.laa.2026.02.032 | Familiar classical concept first; precise extension and clean needed assumptions second. |
| Shi, Wei & Wang, **On a question of Liu and Cheng**, 739 (2026), 1–9 | https://doi.org/10.1016/j.laa.2026.03.011 | A short focused theorem can be an LAA article. Useful model for concise authoring but do not copy its formula-first abstract for this broader-audience paper. |
| Ballarín, Delgado, Liu, Orera & Peña, **An accurate method for the LU decomposition of amazing matrices**, 740 (2026), 1–10 | https://doi.org/10.1016/j.laa.2026.03.014 | Clear named matrix question, explicit answer and verification; a short article should have a single unambiguous purpose. |

**Conclusions from this actual reading**: LAA consistently accepts (i) precise definitions up front when needed, (ii) a sharp mathematical question and theorem, (iii) an honest account of what differs from the closest paper, and (iv) ordinary numbered mathematical sections. Abstracts vary greatly in length; we choose a readable 145–180 words, not a rigid journal-imposed word count. The references above are a STYLE comparator set and must NOT be used to assert this manuscript is "top 20%" or 80% likely to pass.

**Formatting:** mimic the conventional manuscript skeleton, not Elsevier's typeset "article info", copyright line, received/accepted dates or graphical metadata. Normal \`article\` or supported Elsevier author template, single-column draft acceptable if current guide permits, standard section numbers, theorem environments, abstract, 4–6 keywords, verified MSC codes, references. If the publisher requests author highlights, supply a SEPARATE factual highlights file; do not insert marketing bullets into the research article. Do not invent authors' affiliations, funding or institutional claims.

## 8. Historical novelty and citations — absolute priority check

Read the FULL theorem statements and proof locations in these primary sources, not just abstracts:

1. Dutour Sikirić, Schürmann & Vallentin, **A simplex algorithm for rational cp-factorization**, *Mathematical Programming* 187 (2021) 25–45; published online 2020; https://doi.org/10.1007/s10107-020-01467-4 . Its **Conjecture 3.2 concerns finite termination for a suitable pivot rule**. It does not claim a polynomial bit-complexity theorem. Their Ryshkov walk and perfect-form machinery are direct antecedents.
2. Dannenberg & Schürmann, **Perfect copositive matrices**, *Communications in Mathematics* 31 (2023) 137–156, https://doi.org/10.46298/cm.11141 . Perfectness, neighborhood graph, shear/adjacency constructions are PRIOR ART. Do not imply the present authors invented the Ryshkov machinery or all nearby perfect matrices.
3. Oertel & Schürmann, **Generalized Perfect Matrices**, arXiv:2602.05841v2 (2026). Qualitative generalized-perfect/Interior-Ryshkov theory and certificate frameworks are prior art.
4. Horn five-cycle copositive form and elementary doubly nonnegative versus completely positive facts: locate authoritative published citations, distinguish a classic witness from our NEW scaled input family and all-choice forcing.
5. The earlier project manuscripts (source milestone 37, quantitative checkpoints 01–09, nonsimplicial all-local result) are not external citations until publicly available; do not add artificial "our previous paper" citations or invented prior publication statuses. If the existing construction depends on a prior project lemma, include a concise self-contained proof or properly cite a genuinely published source.

THE actual novelty claim must withstand this direct comparison:
- The fixed **ordinary CP_n** cone, not a specially constrained nonsimplicial column cone.
- The **canonical** tridiagonal initialization, not an expensive, tailored start.
- **ALL** improving extreme tangent rays, not just the minimizing-ratio choice.
- Robust **positive definite and entrywise strictly positive** nonmembers, not trivial PSD failures.
- Short explicit separator versus exponentially long local walk, with exact data-size dependence.
- One general **edge-coordinate movement** theorem, not merely a numerically traced path.

If the 2023/2026 texts already cover part of this, cite the precise proposition and narrow the novelty claim. Do not make a "first", "new", or "unprecedented" historical claim without support. The manuscript may say "We prove" a precise theorem; that is normal mathematical writing.

## 9. Very low-jargon, genuinely human research prose

Write as an expert mathematician explaining a clean idea to a colleague working in a DIFFERENT area of linear algebra.

- First sentence of abstract: understandable without CP/COP background.
- First paragraph of intro: one matrix factorization and its basic implications.
- Short declarative sentences; one new term or one displayed formula per conceptual step.
- Prefer "a step to a neighboring matrix" over "an extremal-ray traversal of the Ryshkov stratification" until the technical section.
- Prefer "its entries have short rational descriptions" over "polynomially bounded bit heights" before defining encoding size.
- Define even commonplace specialist words like *copositive*, *perfect*, *pivot*, *certificate*, *adjacent*, *canonical*, and *bit length* before relying on them.
- Do not patronize the mathematician or insert informal analogies about mazes/stairs/doors in the paper.
- Avoid repeated formulaic "We introduce X, we then Y, finally Z" filler, "it is worth noting", "importantly", "indeed", "key insight", "not merely X but Y" as repetitive rhetorical devices, exclamation marks, generic significance claims, or first-person meta commentary on writing choices.
- The mathematical excitement comes from a clean theorem and a sharp contrast, not promotional language.
- Keep citations relevant, give full bibliographic data with DOI and correct author diacritics, avoid citation piles.
- Do not mimic or closely paraphrase distinctive copyrighted prose from any sample paper. Replicate ONLY the legitimate academic macrostructure and level of clarity.
- No AI-related provenance, model acknowledgements, pseudo-editorial ratings, "80% chance", "impact score", author-page metadata, or a claim to have solved all CP decision complexity. Follow the author's applicable disclosure/ethics requirements separately; do not hide required disclosures or fabricate provenance.
- Accessible prose does not excuse omissions from definitions, proofs, quantifiers or the exceptional hypotheses.

## 10. Codex execution and exact deliverables

You are an EXECUTION agent, not an advisor. Create the actual FINAL manuscript package now, not merely an outline, draft abstract, or a checklist for another agent.

**Git branch:** create a new results branch e.g. research/m2-laa-submission-draft-20261115 starting from this editorial handoff branch research/m2-laa-focused-manuscript-codex-20261115; retain/trace the original ordinary-CP result at 11ffd7fe0e83b7eda47459d1d9b90b7358a4fcfc. Never overwrite original proof checkpoints, source manuscript, or mathematical results branches.

**Output directory** e.g. submission/laa_cp_pivot_20261115/:
- main.tex : complete coherent single-paper LAA submission draft, all proofs and references in order; no placeholder sections, invented author details or unproved claims.
- references.bib OR exact references in main.tex with DOI.
- README.md : compilation and source manifest, original theorem source commit and editorial differences.
- PROOF_AND_SCOPE_AUDIT.md : theorem-by-theorem proof check and boundary conditions, explicit no-global-algorithms limitation, accurate input length/radius interpretation.
- NOVELTY_VS_2021_2023_2026.md : precise result-level priority table against DSV, Dannenberg–Schürmann, Oertel–Schürmann, and relevant 2025–2026 LAA articles; mark unresolved priority concerns.
- LAA_EDITORIAL_CHECK.md : a short self-review of first-page accessibility, abstract, fit, theorem emphasis, pacing, citations, style, main-text length and absence of marketing/AI-sounding prose.
- OPTIONAL supplemental/ proof and exact generator/verifier link only if required for rigorous readability; avoid bloated main paper; ensure the theorem can be refereed without trusting numerical software.
- If environment permits, compile the PDF twice, render every page, visually inspect overflow and theorem labels, rerun generators/verifiers, check full source/derived-file hashes. Commit actual editable files and reproducibility instructions to GitHub. Do not assert a PDF exists online unless verified.
- Provide a final concise delivery status: manuscript page count, newest commit SHA, exact paper title, three specific improvements over the old nine-page version, any remaining proof or originality obstacle.

**Self-referee test before final:** Show just the first-page abstract and introduction to a hypothetical ordinary matrix theorist. After 30 seconds, could they answer:
(A) What is a completely positive matrix?
(B) Why does a copositive separator matter?
(C) Which local search is being studied?
(D) What was unknown?
(E) Exactly what does the theorem prove, including which algorithms it does NOT concern?
(F) Why do exponentially many local steps matter even when a short certificate exists?
If not, rewrite the first page until they can. Also read the abstract aloud: if it sounds like a proposal or journal cover letter, rewrite it as a mathematical abstract.

**Finish criterion:** a correct, modest-length, strikingly clear, mathematically rigorous LAA article that instantly conveys its exact new contribution and stands alone without the rest of the project. Do not inflate journal acceptance predictions or claim independent refereeing if none occurred. If a proof fails, report the failure and do not output a falsely submission-ready paper.
