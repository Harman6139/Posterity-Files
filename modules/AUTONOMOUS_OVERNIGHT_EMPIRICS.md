# Autonomous Overnight Empirical Workflow

Reusable agent protocol for future projects that need WRDS data and heavy empirical computation on Waterloo CPU26 with minimal human supervision.

Last verified: **2026-08-26**.

Read first:

- [`UW_CPU26.md`](UW_CPU26.md)
- [`WRDS_CRSP_CIZ.md`](WRDS_CRSP_CIZ.md)

This module integrates those two capabilities into one operational sequence.

## Objective

The intended pattern is:

```text
user starts night workflow with Waterloo VPN connected
        -> passwordless SSH to CPU26
        -> upfront WRDS password + Duo gate while user is present
        -> fresh unattended WRDS reconnect verified
        -> heavy empirical job starts early/persistently on CPU26
        -> Codex/other agents may continue independent work or disappear
        -> CPU26 streams bounded data directly from WRDS
        -> raw licensed rows are discarded after use
        -> compact results are aggregated/QA'd
        -> lightweight permissible outputs are committed/pushed
```

The user's laptop is not part of the heavy computation and should not receive heavy raw data.

## Phase 0 — assumptions

Before starting:

- user has connected the local machine to the Waterloo VPN;
- `ssh uw-cpu26` is expected to work passwordlessly;
- WRDS username is `harman2020_2`;
- secure WRDS PostgreSQL reuse via CPU26 `~/.pgpass` has previously been configured;
- the workflow knows which project/branch/remote path it should operate on;
- any empirical protocol that must be frozen before results is frozen before OOS evaluation.

## Phase 1 — access gate while user is present

### 1. Verify SSH only

Do not rebuild keys/config unless this fails:

```bash
ssh uw-cpu26 'hostname; whoami'
```

Require:

```text
cpu26.student.math.uwaterloo.ca
h56singh
```

### 2. Perform WRDS pre-authentication from CPU26

Open an interactive CPU26 TTY and instantiate the official WRDS connection.

If requested:

- user types the WRDS password directly into hidden terminal input;
- user approves Duo Push.

Never place the password in chat, code, environment variables, Markdown, logs, or Git.

### 3. Prove unattended reconnect

After successful auth:

1. close the WRDS connection;
2. terminate that Python process;
3. start a fresh noninteractive process;
4. reconnect to WRDS;
5. require no password and no Duo prompt;
6. run only a tiny metadata query.

If successful, print:

```text
WRDS AUTH READY FOR NIGHT
```

If not, do not leave the workflow unattended.

## Phase 2 — start empirical work early

Because only immediate and ~60-second unattended WRDS reconnects were directly tested, do not deliberately wait several hours before the first empirical connection.

Preferred strategy:

- launch the empirical controller near the beginning of the night;
- let it operate in parallel with independent theorem/manuscript/agent work;
- keep its own DB connection lifecycle, checkpoints, and status.

This minimizes risk that a later reauthentication gate appears when the user is absent.

## Phase 3 — project synchronization and validation

On CPU26:

1. resolve the project-specific remote directory;
2. synchronize the intended branch/commit;
3. activate/create the project-specific Python environment;
4. record Git commit and package/environment fingerprint;
5. run deterministic tests;
6. validate the empirical protocol/configuration hash;
7. verify required WRDS schema/table metadata with a tiny query.

Do not infer that an old remote checkout is current.

## Phase 4 — host preflight

Run:

```bash
hostname
free -h
uptime
nproc --all
ps -eo user,pid,%cpu,%mem,etime,cmd --sort=-%cpu | head -50
```

Thread limits:

```bash
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1
```

Institutional limits:

```text
MFCF authorized maximum: 150 processes overnight
project ceiling:          140 processes
physical cores:           168
logical CPUs:             336
RAM:                      ~251 GiB
minimum desired headroom: ~40 GiB
hard heavy-run limit:     6 hours
```

Never interfere with another user's processes.

## Phase 5 — tiny end-to-end pilot

Before production, execute a small project-specific path through:

```text
WRDS query
 -> point-in-time filtering/join logic
 -> in-memory transformation
 -> one representative empirical calculation
 -> compact checkpoint/result write
 -> raw-row disposal
 -> aggregation
```

Also test interruption/resume for the controller if the production design is sharded.

No large data pull is justified before this passes.

## Phase 6 — benchmark and choose concurrency

Measure representative production work rather than assuming 140 workers is optimal.

Benchmark:

- typical task runtime;
- largest/heaviest task runtime;
- worker peak RSS;
- scaling at sensible process counts;
- WRDS query throughput and DB-pressure behavior;
- aggregation cost.

Choose:

```text
workers = min(140, CPU-safe, RAM-safe, DB-safe, current-capacity-safe)
```

Database-bound empirical work may need far fewer than 140 simultaneous query processes. Prefer centralized/batched data streaming with CPU-parallel downstream computation rather than hundreds of independent agents hammering WRDS.

## Phase 7 — zero-heavy-data streaming

For CRSP CIZ-style equity studies, use the canonical architecture:

```text
server-side monthly universe ranking/filtering
        -> bounded membership candidates
        -> coalesced required trailing intervals
        -> narrow daily columns streamed in calendar chunks
        -> rolling RAM buffer / sufficient statistics
        -> project calculations
        -> discard consumed licensed rows
        -> compact derived outputs only
```

Do not:

- download all CRSP;
- create a durable raw data lake;
- transfer raw CRSP to the laptop;
- commit licensed observations;
- refetch overlapping historical windows naively for every rebalance.

Where possible, separate database ingestion from CPU-intensive calculation so WRDS is queried efficiently while local CPU26 workers consume prepared in-memory or short-lived task state.

## Phase 8 — persistent controller

Use `tmux` because CPU26 has no scheduler.

Suggested session naming:

```text
<project>-empirical
```

The controller must survive local disconnection and enforce its own deadlines.

Maintain:

```text
experiments/<run>/STATUS.md
experiments/<run>/logs/controller.log
```

Recommended `STATUS.md` fields:

```text
status
hostname
Git commit
start time
current time
elapsed time
stop-launching time
hard stop time
workers configured
active workers
total tasks
completed tasks
failed tasks
current module
WRDS connection status
last successful DB query/checkpoint
host load
available RAM
latest error
projected finish
```

Update atomically and regularly.

## Phase 9 — six-hour deadline

Treat six hours as absolute.

Recommended budget:

```text
preflight/pilot/benchmark    <= 30 min
production                  <= 4 h 45 min
aggregation/QA              <= 30 min
remaining                   contingency
```

Stop issuing new substantial tasks early enough to finish owned workers and aggregation inside the cap.

If work cannot complete, leave valid checkpoints and stop. Do not overrun merely to complete a grid.

## Phase 10 — authentication failure behavior

If WRDS unexpectedly requests password/Duo after unattended production has begun:

1. stop issuing new DB-dependent tasks;
2. preserve/checkpoint all completed derived work;
3. do not repeatedly send Duo requests;
4. do not invent a second credential store;
5. mark status `AUTH_REQUIRED` or equivalent;
6. continue only DB-independent aggregation that is safe;
7. surface the exact reauthentication requirement when the user returns.

The workflow must never trade security for autonomy.

## Phase 11 — completion and cleanup

At the end:

1. stop all owned workers cleanly;
2. aggregate valid task outputs;
3. run QA/invariants/no-lookahead checks;
4. generate compact tables/figures/reports;
5. delete temporary licensed/raw chunks;
6. verify no raw WRDS observation files are staged in Git;
7. run project tests;
8. commit/push permitted lightweight artifacts;
9. leave a final status report and exact provenance/query code.

Permissible retained material usually includes:

```text
frozen design
SQL/query code
field/schema mapping
configuration
Git/environment provenance
aggregate derived results
portfolio-level series when legally derived/compact
statistics/confidence intervals
tables
figures
logs
reports
```

## Recommended user-visible launch confirmations

Before the user leaves:

```text
SSH CPU26: PASS
WRDS initial authentication: PASS
fresh unattended WRDS reconnect: PASS
input/schema gate: PASS
WRDS AUTH READY FOR NIGHT
```

Once the empirical controller is detached/persistent:

```text
EMPIRICAL PRODUCTION LAUNCHED SUCCESSFULLY
```

along with:

```text
tmux session
controller PID
worker count
start time
hard stop time
log path
status command
```

After those conditions are satisfied, the laptop/VPN/foreground Codex session may disappear without terminating CPU26's tmux job.

## Future-agent instruction

A future project lead can simply instruct an agent:

> Read `Harman6139/Posterity-Files` modules `UW_CPU26.md`, `WRDS_CRSP_CIZ.md`, and `AUTONOMOUS_OVERNIGHT_EMPIRICS.md`, then use those verified procedures for the project's remote empirical stage. Do not copy raw WRDS data to the laptop and do not exceed the documented CPU/time limits.

The project should add only its own scientific protocol, not reconstruct infrastructure from scratch.
