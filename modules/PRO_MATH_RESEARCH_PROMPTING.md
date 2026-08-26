# Pro Math Research Prompting Playbook

Purpose: maximize mathematical reasoning quality from a high-reasoning Pro model while minimizing repository, literature, tooling, and orchestration overhead.

This module is for frontier theorem proving, proof closure, and hostile proof audit. The Pro model should be treated as the mathematician, not as the project manager. Another agent should prepare the packet, handle Git, literature collection, formalization, and manuscript integration.

## Source methodology

This playbook is derived from the methodology used in:

- OpenAI, *Prompt Used for “A Proof of the Cycle Double Cover Conjecture”*: https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf
- Phillip Kerger, Appendix A.1 of *Closing the Oracle-Complexity Gap in Derivative-Free Convex Optimization*: https://arxiv.org/pdf/2607.13335
- Kerger’s discussion of the prompting process: https://www.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/
- Kerger’s public proof/verification repository: https://github.com/PhillipKerger/zero-order-bounds-lean-verification
- Kerger’s accompanying account: https://medium.com/@kerger.p/an-ai-assisted-breakthrough-in-convex-optimization-an-optimization-problem-dating-back-30-years-a-db5c631119de

The shared pattern is not “ask harder.” It is: specify the mathematical experiment exactly, enumerate what does not count, preserve multiple genuinely different proof mechanisms, force concrete mathematics, kill theorem-strength dead ends, and audit every load-bearing interface before accepting a proof.

## Core operating principle

**Give Pro one mathematically complete, aggressively scoped packet and one output target.**

Do not make Pro discover the repository, reconstruct project history, write manuscript prose, manage branches, run broad literature reviews, or coordinate infrastructure. Every token spent on project administration is a token not spent on the theorem.

A good Pro task should look like:

```text
READ ONLY:  one scoped mathematical packet
SOLVE ONLY: one exact theorem / gap / audit target
WRITE ONLY: one proof note
```

## 1. Build the problem packet before opening Pro

A project lead or cheaper agent should create a short file such as:

`pro_packets/<task>.md`

The packet should contain only what is mathematically necessary.

### Required packet contents

1. **Exact task statement**
   - all definitions;
   - all quantifiers;
   - parameter ranges;
   - exact conclusion;
   - conventions that could change the theorem.

2. **Verified baseline**
   - only lemmas/results already proved and permitted as inputs;
   - state them precisely enough to use;
   - include exact constants/rates when they matter.

3. **The precise remaining gap**
   - one sentence if possible;
   - distinguish a local technical gap from a theorem-strength missing lemma.

4. **Known failed routes / counterexamples**
   - only failures that prevent Pro from wasting large amounts of time;
   - state the exact obstruction, not a project history narrative.

5. **What counts as a complete solution**
   - spell out the exact theorem that must emerge;
   - list interfaces and edge cases that must be checked.

6. **Results that do not count**
   - special cases;
   - reductions to unproved statements;
   - asymptotic statements weaker than requested;
   - numerical evidence;
   - missing constants/quantifiers;
   - proofs that silently strengthen assumptions;
   - “standard/routine” compatibility claims with no proof.

7. **Allowed imported facts**
   - list named standard theorems Pro may use without rederiving, if any;
   - otherwise require exact statement and hypothesis alignment.

### Packet size rule

Prefer **2-6 dense pages**. Longer is justified only when the mathematical model itself requires it. Never paste an entire repository or manuscript merely “for context.”

## 2. Search posture

Use the CDC/Kerger posture:

- search as though a complete resolution is obtainable;
- do not stop merely because the problem is known or believed open;
- never lower the proof standard because the target is difficult;
- do not treat a reduction to an equally hard lemma as progress;
- do not return vague optimism, literature summaries, or status reports.

For famous open problems, distinguish **search posture** from **epistemic conclusion**: Pro may be told not to give up because the problem is open, but it must not claim success unless the proof survives its own adversarial audit.

## 3. Preserve genuinely different proof mechanisms

The CDC and Kerger prompts both deliberately prevented premature convergence on one attractive route.

Ask Pro to maintain several incompatible approach families early. Examples depend on the field:

- structural induction / extremal counterexample;
- algebraic or spectral reformulation;
- duality / variational formulation;
- probabilistic method;
- topology / geometry;
- explicit construction;
- compactness / limiting argument;
- local-to-global principle;
- contradiction via minimal obstruction;
- computational sanity checks used only to falsify local lemmas.

Do **not** allocate fixed effort mechanically. Redirect reasoning toward routes that produce concrete lemmas. Mark a route blocked when its missing lemma is essentially the original theorem in disguise. Reopen it only if a genuinely new mechanism appears.

If explicit subagent/multi-agent capability exists, use it dynamically. If not, emulate the same discipline internally by maintaining multiple independent proof routes before synthesis.

## 4. Concrete-mathematics rule

Every active route must produce at least one of:

- a formally stated lemma with proof;
- an explicit construction;
- an invariant and proof it is maintained;
- an exact reduction with all hypotheses checked;
- a counterexample killing a proposed lemma;
- an exact asymptotic/constant calculation;
- a precise local obstruction.

Reject “this should follow,” “routine,” “standard compactness,” “one can arrange,” or similar language at load-bearing steps.

## 5. Candidate-proof freeze and hostile audit

When a complete proof appears, stop expanding the search and attack it.

Audit from scratch for the problem-specific failure modes. At minimum check:

- quantifier order;
- hidden strengthened assumptions;
- edge/boundary cases;
- sign/normalization/constants;
- imported theorem hypotheses;
- circularity/equivalent missing lemma;
- existence/compactness claims;
- interchange of limits/integrals/infima;
- measurability/topology/regularity assumptions;
- finite-vs-asymptotic transitions;
- whether the construction actually lies in the stated class;
- whether every claimed object is globally compatible, not merely locally plausible.

A repaired proof receives **no inherited approval**. Re-audit the repaired version.

## 6. Imported theorem discipline

Public search is useful for standard background, precise statements of named results, and verifying hypotheses. It should not replace proof search.

Whenever a theorem is imported, require:

1. exact statement needed here;
2. exact hypotheses;
3. mapping from current objects to those hypotheses;
4. parameter/normalization compatibility;
5. proof that the theorem gives the required direction and strength.

## 7. Output discipline

Pro should write one standalone proof note, not a project report.

Preferred structure:

```text
Theorem
Definitions / setup actually used
Proof roadmap (short)
Lemmas
Complete proof
Edge cases / constants
Self-audit of load-bearing steps
```

Avoid:

- repo summaries;
- issue commentary;
- journal positioning;
- manuscript prose;
- broad literature survey;
- implementation notes unrelated to proof correctness.

The project lead handles Git after the proof is produced unless write access to one exact output path is trivial.

## 8. Three-prompt workflow

Use three fresh Pro sessions when the theorem is important enough:

1. **Discovery / solve** — independent proof search from the packet.
2. **Hostile audit** — treat the candidate proof as potentially false; attempt to break it.
3. **Repair / closure** — repair only the audited gaps, or rebuild the proof if a theorem-strength flaw was found.

Do not let Prompt 2 inherit Prompt 1’s confidence. Do not let Prompt 3 inherit Prompt 2’s approval.

Canonical templates live in:

- `prompts/pro_math/01_DISCOVERY.md`
- `prompts/pro_math/02_HOSTILE_AUDIT.md`
- `prompts/pro_math/03_REPAIR_CLOSURE.md`

## 9. Challenge/solution verification pattern

Kerger’s verification repository separates the **statement-only challenge** from the **solution**, then compares the proved solution against the original statement and records the trusted axioms/scope. For results suitable for formalization, future project leads should imitate this separation:

```text
challenge statement
    -> human/agent mathematical proof
    -> independent audit
    -> formal solution if feasible
    -> statement comparison / scope ledger
```

A proof map is valuable: list the load-bearing lemmas, dependencies, exact endpoint, and what is explicitly outside scope.

Formal verification is not mandatory for every task, but the *discipline* is: challenge and solution must be compared against the same exact theorem, not against a subtly weakened statement.

## 10. Provenance rule

Record the actual prompt used, the exact scoped packet, model/configuration, date, and whether prior attempts or AI-assisted prompt construction informed the final prompt. The Reddit discussion correctly highlights that prompt construction itself is research input. “One-shot” should mean one uninterrupted solving session from the final prompt, not that no prior human/AI work shaped the task.

## 11. Anti-patterns

Do not send Pro:

- “Read the whole repo and solve whatever is left.”
- a 40-page manuscript when a 3-page theorem packet suffices;
- twenty agents’ status reports;
- literature dumps;
- Git instructions mixed into the proof task;
- simulation/empirical requests mixed into the theorem task;
- “find the strongest result possible” with no exact acceptance criterion;
- a candidate proof before an independent discovery session unless the task is explicitly audit/repair.

## 12. Minimal project-lead recipe

```text
1. Project lead isolates one theorem/gap.
2. Cheap agent writes a 2-6 page problem packet.
3. Project lead checks packet for exactness and removes irrelevant context.
4. Fresh Pro gets Prompt 1 + packet only.
5. Candidate proof is frozen.
6. Fresh Pro gets Prompt 2 + packet + frozen proof only.
7. If needed, fresh Pro gets Prompt 3 + packet + audit + frozen proof.
8. Optional: formalize challenge/solution and compare exact statements.
9. Repo/manuscript agents integrate only after correctness lock.
```

This is the default posterity workflow for high-value mathematical research tasks.