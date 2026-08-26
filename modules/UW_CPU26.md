# University of Waterloo CPU26 Module

Canonical instructions for future agents using the verified Waterloo Math Faculty CPU host.

Last verified: **2026-08-26**.

## Connection

The user is expected to connect the local machine to the Waterloo VPN **before** starting any workflow that needs CPU26.

Verified passwordless SSH alias:

```bash
ssh uw-cpu26
```

Expected identity:

```text
hostname: cpu26.student.math.uwaterloo.ca
user:     h56singh
```

A dedicated SSH key and local SSH alias have already been configured and tested. Do **not** rebuild SSH configuration if this works:

```bash
ssh uw-cpu26 'hostname; whoami'
```

Expected output:

```text
cpu26.student.math.uwaterloo.ca
h56singh
```

If this check fails, stop and surface the access problem. Do not request or persist the Waterloo password unless the user explicitly needs to repair access interactively.

## Verified hardware

```text
CPU:       2 x AMD EPYC 9634
Cores:     84 physical cores/socket
Physical:  168 cores total
Logical:   336 SMT threads
RAM:       ~251 GiB usable
NUMA:      2 nodes
Scheduler: none detected
Persistence: tmux 3.2a available
```

The verified process affinity exposed logical CPUs `0-335`.

### `nproc` caveat

The login environment sets:

```bash
OMP_NUM_THREADS=1
```

Therefore plain `nproc` may report `1` even though the process can access the full host. Use:

```bash
nproc --all
```

or Python affinity inspection:

```python
import os
print(os.cpu_count())
print(len(os.sched_getaffinity(0)))
```

The verified values were `336` and `336`.

## Institutional resource authorization

The user received explicit MFCF permission to run **up to 150 processes overnight** on this host.

For autonomous research workflows use:

```text
MAX_PROCESSES = 140
```

as the project-level ceiling. It is a ceiling, not a target.

Before every substantial launch, re-check current host conditions and reduce concurrency when necessary.

Never kill, renice, signal, suspend, pin, or otherwise interfere with another user's process.

## Mandatory preflight

Before heavy computation run:

```bash
hostname
free -h
uptime
nproc --all
ps -eo user,pid,%cpu,%mem,etime,cmd --sort=-%cpu | head -50
```

Confirm:

- correct host;
- sufficient available RAM;
- no unexpected competing load;
- project directory and environment are correct.

## Thread policy

Prefer process-level parallelism for Monte Carlo, backtests, rolling empirical panels, and independent task shards.

Before importing NumPy/SciPy/BLAS-backed libraries in workers, use:

```bash
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1
```

Verify that workers are not spawning nested BLAS/OpenMP threads.

Choose actual concurrency from:

```text
min(
    140,
    safe CPU concurrency,
    safe RAM concurrency,
    currently available host capacity
)
```

Benchmark representative work rather than assuming more workers are faster. A prior simulation pilot found short tasks stopped scaling well beyond 32 workers, so production-sized scaling should be measured for each new workload.

## RAM policy

Maintain approximately **40 GiB or more available-memory headroom** during heavy work.

Do not intentionally use swap as planned capacity.

Measure peak RSS for representative tasks before selecting large concurrency.

## Six-hour overnight limit

The authorized heavy run should remain an overnight job of **no more than six hours**.

Treat six hours as an absolute ceiling, not a utilization target.

A good internal budget is:

```text
preflight / pilot / benchmark    <= 30 min
main production computation     <= 4 h 45 min
aggregation / QA                <= 30 min
remaining time                  contingency
```

The controller should stop issuing new substantial tasks early enough that all owned workers can terminate cleanly inside the six-hour cap.

Checkpoint incomplete work instead of overrunning.

## Persistence

There is no Slurm/PBS scheduler on CPU26. Long work must therefore run through a persistent mechanism, preferably `tmux`.

Suggested pattern:

```bash
tmux new-session -d -s <project-session> '<controller command>'
```

The run must survive:

- Codex closing;
- SSH disconnect;
- VPN disconnect;
- laptop sleep/shutdown;
- agent handoff.

Do not depend on the foreground Codex shell for production.

## Status and resumability

Every long project should maintain a durable human-readable status file, for example:

```text
experiments/<run>/STATUS.md
```

Recommended contents:

```text
status
hostname
start time
current time
elapsed time
hard stop time
workers configured
active workers
total tasks
completed tasks
failed tasks
current module
host load
available RAM
latest checkpoint
latest error
projected finish
```

Also keep a durable controller log.

Production should be task/shard resumable. Completed validated work should not be rerun unnecessarily after an SSH loss, failed worker, agent handoff, or interrupted aggregation.

## Project storage

Use the user's Waterloo home/project space for durable code and compact results. Raw licensed data should follow the separate WRDS module and should not be copied into Git.

Do not assume a particular repository path across projects. The historical QF project used `/home/h56singh/projects/QF-paper`, but future agents should resolve the current project's remote path explicitly.

## Minimal future-agent sequence

```text
1. User connects Waterloo VPN.
2. Agent runs: ssh uw-cpu26 'hostname; whoami'.
3. Agent syncs/creates the project-specific remote checkout.
4. Agent inspects current CPU/RAM/load.
5. Agent activates/creates the project environment.
6. Agent runs a tiny end-to-end pilot.
7. Agent benchmarks representative production work.
8. Agent chooses safe concurrency <= 140.
9. Agent launches persistent tmux controller.
10. Agent monitors through status/checkpoints.
11. Agent terminates gracefully within six hours.
12. Agent aggregates, QA-checks, and retains compact outputs only.
```
