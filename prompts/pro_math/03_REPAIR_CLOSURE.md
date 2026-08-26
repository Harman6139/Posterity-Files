# Pro Prompt 3 — Repair / Closure

Use this in a **fresh Pro chat** only after Prompt 2 has identified the exact defects. Replace bracketed placeholders before sending.

```text
Proof repair and closure

Read only:
1. [SCOPED_PACKET_PATH_OR_PASTED_PACKET]
2. [FROZEN_CANDIDATE_PROOF_PATH]
3. [HOSTILE_AUDIT_PATH]

Do not inspect unrelated repository material. Do not broaden the theorem unless the audit proves that the original target is false. Do not rewrite correct parts merely for style.

Target

Repair the proof so that it establishes exactly:

[EXACT_TARGET_THEOREM]

The hostile audit is authoritative only as a list of alleged defects, not as proof that its proposed repairs are correct. Re-check each defect independently.

Repair discipline

For every audit item:
1. restate the exact mathematical defect;
2. decide whether it is real;
3. if real, repair it with the smallest sufficient new argument;
4. verify that the repair does not silently change assumptions, quantifiers, constants, or the theorem statement;
5. propagate the repair through every downstream step that depends on it.

If an audit item reveals a theorem-strength gap, do not patch it with prose. Reopen mathematical search specifically for that gap, using several genuinely different mechanisms if needed. Treat any route that merely restates the missing lemma as blocked.

If the candidate architecture is fundamentally broken, abandon it and rebuild the proof from the packet. Do not preserve a failed strategy for sunk-cost reasons.

Concrete-mathematics requirement

Every repair must be a proved lemma, explicit construction, exact calculation, or exact reduction. No load-bearing “routine” steps.

Re-audit requirement

Once the repaired proof appears complete, audit the repaired argument from scratch. The repaired version inherits no approval from the original proof or prior audit.

At minimum recheck:
- exact target statement;
- all repaired interfaces;
- quantifiers and parameter ranges;
- boundary/degenerate cases;
- constants/signs/scaling;
- existence and compatibility claims;
- imported theorem hypotheses;
- limit/interchange steps;
- noncircularity;
- every problem-specific failure mode in the packet.

Output

Write one final standalone proof note to:
[OUTPUT_PATH]

It must contain:
1. exact theorem statement;
2. minimal setup;
3. short roadmap;
4. all lemmas needed for a self-contained proof;
5. complete repaired proof;
6. explicit edge-case/constant treatment;
7. concise closure audit listing the previously identified defects and how each was resolved.

Do not output a patch diff, project report, or discussion of repo history.

If the theorem cannot be repaired without a genuinely new theorem-strength idea and no such idea is found, do not pretend closure. Return the strongest rigorous partial result and the exact remaining gap.
```
