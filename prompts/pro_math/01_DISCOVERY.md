# Pro Prompt 1 — Discovery / Solve

Use this in a **fresh Pro chat**. Replace bracketed placeholders before sending.

```text
Current task statement

Read only:
[SCOPED_PACKET_PATH_OR_PASTED_PACKET]

Do not inspect the rest of the repository unless a definition explicitly missing from the packet makes that unavoidable. Do not spend time on Git, project history, manuscript prose, simulations, empirical work, or literature surveying.

Your entire task is to resolve the following mathematical problem:

[EXACT_TARGET_THEOREM_OR_PROBLEM]

The packet is authoritative for definitions, parameter ranges, already-verified lemmas, and known obstructions.

Assume for purposes of search that a complete resolution is obtainable. Do not stop merely because the problem is believed open, difficult, or outside standard techniques. At the same time, do not claim success unless every load-bearing step is actually proved.

A complete solution must prove exactly the target above with no strengthened assumptions and no missing compatibility step.

Results that do not count

The following are insufficient unless they imply the exact target:

[PASTE THE PACKET'S “DOES NOT COUNT” LIST]

In particular, do not return:
- a special case;
- a reduction to another unproved statement of comparable strength;
- a candidate construction without global verification;
- numerical/computational evidence;
- a heuristic asymptotic when an exact theorem is requested;
- a proof with a theorem-strength lemma labeled routine/standard;
- a literature summary or explanation of why the problem is hard.

Search method

Begin with several genuinely different proof mechanisms. Preserve independence between them long enough to expose their actual strengths and failure modes. Examples may include structural/extremal arguments, algebraic or spectral reformulations, duality/variational methods, geometric/topological mechanisms, probabilistic constructions, compactness/local-to-global arguments, explicit constructions, or contradiction from a minimal obstruction, as appropriate to this problem.

If subagent or parallel-search capability is available, use it dynamically rather than with a fixed allocation. If it is not available, emulate the same discipline internally.

Maintain an internal registry of approach families. For each route track:
- central lemma/construction;
- what is actually proved;
- exact remaining gap;
- whether the gap is local or theorem-strength;
- counterexamples/failed variants;
- active / blocked / abandoned status.

A route that ends at a lemma essentially equivalent to the original theorem is blocked, not nearly complete. Reopen a blocked route only if a materially new invariant, construction, or mechanism appears.

Concrete-mathematics requirement

Every route you continue must produce concrete mathematics: a proved lemma, explicit construction, invariant, exact reduction, counterexample, or exact calculation. Reject vague optimism and “routine” interfaces.

Candidate-proof audit

When a complete proof first appears, freeze exploratory expansion and attack it before returning. Recheck from scratch:
- quantifier order;
- hidden strengthened assumptions;
- edge/boundary cases;
- normalization/sign/constants;
- existence and compactness claims;
- imported-theorem hypotheses;
- limit/interchange steps;
- global compatibility of locally defined objects;
- circularity or an equivalent missing lemma;
- every problem-specific failure mode listed in the packet.

If the proof fails, record the exact defect internally and resume search. A repaired proof receives no inherited approval: audit the repaired version again.

Imported results

You may use standard named theorems, but state the exact form needed and verify every hypothesis and normalization in the present setting. Public search, if available, may be used only to retrieve/verify ordinary background or standard theorem statements, not as a substitute for solving the target.

Final output

Write one standalone proof note to:
[OUTPUT_PATH]

The note should contain only:
1. precise theorem statement;
2. minimal setup/definitions actually used;
3. short proof roadmap;
4. proved lemmas;
5. complete proof;
6. explicit treatment of edge cases/constants;
7. concise self-audit of the load-bearing steps.

Do not write a project report.
Do not discuss repository management.
Do not give manuscript positioning.
Do not return a “best effort” summary if a complete proof has been claimed.

If, after exhausting materially different routes, no complete proof survives audit, return only the strongest rigorously established result and the single exact theorem-strength gap that remains. Do not disguise a gap as a proof.
```
