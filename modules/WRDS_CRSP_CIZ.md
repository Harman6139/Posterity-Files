# WRDS + CRSP CIZ Module

Canonical instructions for future agents that need autonomous WRDS access from Waterloo CPU26 and point-in-time CRSP CIZ equity data.

Last verified: **2026-08-26**.

## Verified account and authentication behavior

WRDS username:

```text
harman2020_2
```

Programmatic WRDS PostgreSQL access from CPU26: **PASS**.

Observed initial authentication:

```text
WRDS password required: YES
Duo Push required:      YES
```

The official `wrds` Python client created/uses a standard PostgreSQL password file at:

```text
~/.pgpass
```

Verified permissions:

```text
0600
```

Never print, log, copy, commit, or expose the contents of `~/.pgpass`.

After the initial password + Duo authentication, two completely fresh Python processes reconnected without another password or Duo prompt; the third reconnect occurred after approximately 60 seconds.

Several-hour reuse was **not** directly tested. Future workflows must therefore authenticate near the beginning while the user is present and fail closed if later WRDS reauthentication unexpectedly appears.

## Required startup auth gate

At the beginning of any unattended nightly workflow that will need WRDS later:

```text
1. User has Waterloo VPN connected.
2. SSH to CPU26 and verify host/user.
3. From CPU26, instantiate the official WRDS connection.
4. If requested, user types WRDS password in a hidden interactive TTY.
5. User approves Duo Push.
6. Confirm ~/.pgpass exists and is mode 0600.
7. Close the WRDS connection and terminate that Python process.
8. Open a completely fresh process with no interactive stdin and reconnect.
9. Require password=NO, Duo=NO, connection=PASS.
10. Print: WRDS AUTH READY FOR NIGHT.
```

Do not defer this first authentication until hours later if the workflow can perform it up front.

Never place the WRDS password in prompts, scripts, Markdown, logs, environment manifests, or Git.

## Python connection

Use the official/current WRDS package, conceptually:

```python
import wrds

db = wrds.Connection(wrds_username="harman2020_2")
```

Do not embed the password in code.

## Verified CRSP CIZ access

Accessible schema/library:

```text
crsp
```

The accessible views are backed by `crsp_a_stock`.

### Daily stock data

Primary flattened CIZ daily view:

```text
crsp.dsf_v2
```

Narrow daily component useful for return streaming:

```text
crsp.stkdlysecurityprimarydata
```

Complete daily security component:

```text
crsp.stkdlysecuritydata
```

### Monthly stock data

Useful for efficient point-in-time universe formation:

```text
crsp.msf_v2
```

### Security/history metadata

```text
crsp.stksecurityinfohist
crsp.stocknames_v2
crsp.stksecurityinfohdr
```

Use the history tables for historical point-in-time status. Do not replace historical metadata with a current header row or current ticker.

## Verified CIZ field mapping

```text
stable security ID        PERMNO / permno
company-level ID          PERMCO / permco
daily date                DlyCalDt / dlycaldt
daily total return        DlyRet / dlyret
price                     DlyPrc / dlyprc
shares outstanding        ShrOut / shrout
market capitalization     DlyCap / dlycap
exchange                  PrimaryExch
trading condition         ConditionalType
security/share type       ShareType, SecurityType, SecuritySubType
US incorporation flag     USIncFlg
issuer type               IssuerType
SIC                       SICCD
other industry metadata   NAICS, ICBIndustry, UESIndustry
trading status            TradingStatusFlg
history active flag       SecurityActiveFlg
human labels              Ticker, SecurityNm, IssuerNm
```

### Delisting treatment

For the verified CIZ daily panel:

```text
DlyRet already incorporates applicable delisting returns.
```

Supporting flags include:

```text
DlyDelFlg
DlyRetMissFlg
```

Do **not** mechanically apply the legacy SIZ `RET + DLRET` merge logic on top of CIZ `DlyRet`.

If a project wants alternate treatment of genuinely missing delisting outcomes, it must predeclare and document that rule separately.

### Market capitalization

Prefer direct:

```text
DlyCap
```

when available and appropriate.

The consistent construction is also available from:

```text
DlyPrc * ShrOut
```

with the CRSP unit conventions understood and validated.

## Point-in-time joins

Join daily rows to security-history metadata by stable ID and effective dates, conceptually:

```sql
d.permno = h.permno
AND d.dlycaldt BETWEEN h.secInfoStartDt AND h.secInfoEndDt
```

For `stocknames_v2` use the corresponding `namedt` / `nameenddt` effective-date interval.

Never build historical universes from current ticker membership.

## Verified common-stock filter

A successful point-in-time test used the CIZ concepts:

```text
ShareType       = 'NS'
SecurityType    = 'EQTY'
SecuritySubType = 'COM'
USIncFlg        = 'Y'
IssuerType      IN ('ACOR','CORP')
PrimaryExch     IN ('N','A','Q')
ConditionalType = 'RW'
TradingStatusFlg = 'A'
```

plus valid positive price/shares/market cap and the return availability required by that test.

Future projects may legitimately adjust liquidity/size/status filters, but should use current CIZ semantics rather than blindly porting legacy `SHRCD` rules.

## Verified coverage

Tiny indexed/date-bounded checks confirmed coverage in:

```text
1990: YES
2025: YES
```

The historical smoke test also successfully formed a point-in-time top-five universe, fetched a 115-row daily panel, and constructed volatility-standardized returns, a correlation matrix, eigenvalues, and eigenvectors.

No licensed observations were retained.

## Zero-heavy-data rule

For future projects, the default architecture is:

```text
WRDS PostgreSQL
    -> server-side filters/ranking
    -> bounded narrow query chunks
    -> CPU26 RAM or temporary ignored working state
    -> rolling sufficient statistics / empirical calculations
    -> discard licensed raw rows
    -> persist compact derived results only
```

### Forbidden by default

Do not:

- download all of CRSP;
- create a durable full-market raw CSV;
- create a giant raw Parquet lake merely for convenience;
- transfer raw CRSP data to the user's laptop;
- commit licensed WRDS observations;
- refetch the same overlapping multi-year window independently for every rebalance when a streaming design can avoid it.

### Recommended large-panel strategy

For a long daily-equity study such as 1990–2025:

1. Query `crsp.msf_v2` in bounded year ranges and perform point-in-time common-stock filters and market-cap ranking on the WRDS server.
2. Return only the monthly membership candidates actually needed, e.g. top 100/200/500.
3. Convert selected PERMNO/month pairs into required trailing estimation intervals.
4. Merge/coalesce overlapping intervals per PERMNO.
5. Stream only narrow daily columns from the CIZ daily table in non-overlapping calendar chunks.
6. Use a server-side cursor or chunked `raw_sql` so each batch is RAM-bounded.
7. Maintain the rolling lookback window or sufficient statistics in RAM.
8. Compute eligible rebalances as dates advance.
9. Validate downstream calculations, then discard consumed raw batches and expired ring-buffer state.
10. Persist only compact derived artifacts.

## What may be retained

Safe project artifacts include:

```text
frozen empirical protocol
SQL/query code
schema/field mapping
query provenance
configuration manifests
aggregate statistics
portfolio-level OOS results
spectral/orientation summaries
confidence intervals
diagnostics
tables
figures
logs
checksums/hashes
reports
```

Raw licensed security-day observations should not be retained unless a future project has a specific justified need and a compliant storage plan.

## Known WRDS entitlement context

As of the verification date:

- Full CRSP access: YES.
- CRSP CIZ daily: YES.
- CRSP/Compustat Merged: available.
- Compustat / Capital IQ: available.
- Fama-French portfolios/factors: available.
- LSEG / IBES: available.
- FactSet: available.
- Cboe Indexes: available.
- SEC MIDAS: available.
- Full NYSE TAQ: NO; sample only.
- WRDS Intraday Indicators / Millisecond Intraday Indicators: require TAQ and are not available under the current entitlement.
- Full OptionMetrics: NO; sample only.

For ordinary covariance/portfolio empirical work, CRSP CIZ daily is sufficient. Do not broaden a project into unrelated databases without a theory-driven reason.

## Failure behavior

If a later connection asks for password or Duo after the unattended run has begun:

- do not repeatedly trigger Duo;
- do not invent an alternate credential store;
- checkpoint/fail closed;
- surface that human reauthentication is required.

If a table/field mapping changes, rediscover metadata from the live WRDS schema and update this module only after a tiny validated capability test.
