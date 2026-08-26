# Pro Prompt 2 — Independent Hostile Audit

Use this in a **fresh Pro chat** after freezing the candidate proof from Prompt 1. Replace bracketed placeholders before sending.

```text
Independent proof audit

Read only:
1. [SCOPED_PACKET_PATH_OR_PASTED_PACKET]
2. [FROZEN_CANDIDATE_PROOF_PATH]

Do not inspect unrelated repository material. Do not read prior praise, discussion, manuscript prose, or the original solver's reasoning. Treat the candidate proof as potentially false.

Your task is not to improve exposition. Your task is to determine whether the candidate proof actually proves:

[EXACT_TARGET_THEOREM]

Audit posture

Attempt to falsify the proof before accepting it. Re-derive every load-bearing step independently. Look especially for a proof that is locally plausible but globally incompatible, a theorem imported with the wrong hypotheses, a hidden strengthening of assumptions, a quantifier reversal, an unjustified limiting step, or a missing lemma equivalent in strength to the target.

The packet is authoritative for definitions and permitted baseline facts.

Required audit

Check at minimum:
- exact theorem statement versus what is actually proved;
- all quantifiers and parameter ranges;
- every construction belongs to the stated class;
- edge/boundary/degenerate cases;
- signs, constants, scaling, normalization, dimensions;
- existence/compactness/attainment claims;
- continuity/measurability/regularity assumptions;
- every interchange of limit, infimum, integral, expectation, derivative, or summation;
- every local-to-global or patching argument;
- imported theorem statement and exact hypothesis alignment;
- noncircularity of all key lemmas;
- whether any “routine/standard” step is actually theorem-strength;
- all problem-specific failure modes listed in the packet.

Adversarial methods

Actively try to:
- build counterexamples to intermediate lemmas;
- push parameters to endpoints or degenerate regimes;
- reverse inequalities to see where sign assumptions enter;
- construct objects satisfying the local hypotheses but violating global compatibility;
- recompute constants/scalings from scratch;
- identify whether a claimed reduction is really equivalent to the original problem;
- replace prose arguments with exact equations at the fragile interfaces.

Do not repair while auditing unless a tiny local correction is needed to diagnose the issue. The main goal is an independent verdict.

Verdict standard

Use exactly one verdict:

VALID
The proof establishes the exact target as written. No theorem-strength gap remains.

VALID WITH LOCAL REPAIRS
The proof strategy is correct, but one or more explicitly identified local gaps/errors must be repaired. Each repair must be strictly weaker than reproving the main theorem.

INVALID — THEOREM-STRENGTH GAP
At least one missing/false step is comparable in strength to the target, circular, or requires a materially new idea.

INVALID — FALSE STATEMENT
The target or a necessary claimed lemma is false under the stated assumptions; provide a concrete counterexample or contradiction.

Output

Write one audit note to:
[OUTPUT_PATH]

It must contain:
1. verdict;
2. exact theorem audited;
3. concise dependency map of the candidate proof;
4. numbered list of every load-bearing issue checked;
5. for each defect, the exact location, statement, and reason it fails;
6. concrete counterexample/calculation where possible;
7. if VALID WITH LOCAL REPAIRS, the smallest mathematically sufficient repair specification;
8. if VALID, a concise independent justification of why the fragile interfaces are sound.

Do not rewrite the entire proof unless necessary to demonstrate a fatal flaw.
Do not soften uncertainty. If a step has not been justified, mark it unresolved.
Do not let the candidate proof inherit credibility from the original solver.
```
