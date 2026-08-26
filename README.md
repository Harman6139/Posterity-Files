# Posterity Files

Private operational knowledge base for future research agents.

The purpose of this repository is to preserve verified infrastructure and data-access procedures so future projects can use University of Waterloo compute and WRDS without reconstructing the setup from chat history.

## Canonical modules

Future agents should read the relevant modules **before** configuring access or launching computation:

1. [`modules/UW_CPU26.md`](modules/UW_CPU26.md)  
   Verified Waterloo CPU26 connection, hardware, resource policy, persistence, preflight, and six-hour overnight limits.

2. [`modules/WRDS_CRSP_CIZ.md`](modules/WRDS_CRSP_CIZ.md)  
   Verified WRDS authentication behavior from CPU26, CRSP CIZ schema/field mapping, point-in-time construction rules, and zero-heavy-data streaming policy.

3. [`modules/AUTONOMOUS_OVERNIGHT_EMPIRICS.md`](modules/AUTONOMOUS_OVERNIGHT_EMPIRICS.md)  
   Generic end-to-end workflow combining VPN, passwordless SSH, upfront WRDS/Duo authentication, bounded data streaming, remote computation, checkpointing, and compact-result retention.

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
- fail closed rather than inventing unsafe authentication workarounds.

Last verified: **2026-08-26**.
