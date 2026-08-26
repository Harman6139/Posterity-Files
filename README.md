# Posterity Files

Private operational knowledge base for future research agents.

The purpose of this repository is to preserve verified infrastructure, data-access procedures, and research-agent methods so future projects can reuse them without reconstructing setup or prompting strategy from chat history.

## Canonical modules

Future agents should read the relevant modules **before** configuring access, launching computation, or assigning frontier mathematical work:

1. [`modules/UW_CPU26.md`](modules/UW_CPU26.md)  
   Verified Waterloo CPU26 connection, hardware, resource policy, persistence, preflight, and six-hour overnight limits.

2. [`modules/WRDS_CRSP_CIZ.md`](modules/WRDS_CRSP_CIZ.md)  
   Verified WRDS authentication behavior from CPU26, CRSP CIZ schema/field mapping, point-in-time construction rules, and zero-heavy-data streaming policy.

3. [`modules/AUTONOMOUS_OVERNIGHT_EMPIRICS.md`](modules/AUTONOMOUS_OVERNIGHT_EMPIRICS.md)  
   Generic end-to-end workflow combining VPN, passwordless SSH, upfront WRDS/Duo authentication, bounded data streaming, remote computation, checkpointing, and compact-result retention.

4. [`modules/PRO_MATH_RESEARCH_PROMPTING.md`](modules/PRO_MATH_RESEARCH_PROMPTING.md)  
   CDC/Kerger-inspired playbook for assigning frontier mathematical research to a high-reasoning Pro model with minimal repository/context overhead, independent proof search, hostile audit, and repair/closure discipline.

## Canonical Pro math prompts

Use these as the default three-session workflow for important theorem work:

1. [`prompts/pro_math/01_DISCOVERY.md`](prompts/pro_math/01_DISCOVERY.md) — fresh independent discovery/solve session.
2. [`prompts/pro_math/02_HOSTILE_AUDIT.md`](prompts/pro_math/02_HOSTILE_AUDIT.md) — fresh falsification-first audit of the frozen proof.
3. [`prompts/pro_math/03_REPAIR_CLOSURE.md`](prompts/pro_math/03_REPAIR_CLOSURE.md) — fresh minimal repair or full rebuild, followed by re-audit.

The preferred interface is one scoped mathematical packet in, one standalone proof/audit note out. Do not ask Pro to survey the whole repository or manage the project unless absolutely necessary.

## Verification record

[`REPORT.md`](REPORT.md) is the 2026-08-26 infrastructure smoke-test record that established the WRDS-to-CPU26 workflow and live CRSP CIZ mapping. Treat the modules above as the operational interface; use the report when auditing or troubleshooting details.

## Security rules

This repository must **never** contain:

- Waterloo passwords;
- WRDS passwords;
- Duo codes or secrets;
- SSH private keys;
- GitHub tokens;
- contents of `~/.pgpass`;
- raw licensed WRDS observations;
- large proprietary extracts.

Verified secrets remain only in their standard local locations, such as the user's SSH key store and a mode-`0600` PostgreSQL password file on CPU26.

## Agent contract

When a future prompt says to use the posterity modules:

- read the relevant module(s) first;
- do not rebuild SSH if the verified alias works;
- do not infer old CRSP/SIZ conventions when CIZ mappings are documented here;
- do not download an entire licensed database;
- perform any required WRDS password/Duo gate near the start while the user is present;
- run long work persistently on CPU26 rather than the user's laptop;
- preserve resumability and compact provenance;
- fail closed rather than inventing unsafe authentication workarounds;
- for frontier math, isolate one exact theorem/gap, give Pro only the scoped packet it needs, and use fresh discovery/audit/repair sessions rather than one sprawling project chat.

Last verified/updated: **2026-08-26**.
