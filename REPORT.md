# WRDS -> CPU26 Empirical Access and Data-Capability Smoke Test

Date: 2026-08-26

## Verdict

- SSH to `cpu26.student.math.uwaterloo.ca` as `h56singh`: PASS
- Programmatic WRDS PostgreSQL connection from CPU26: PASS
- CRSP Stock Version 2 / CIZ access: PASS
- Point-in-time common-stock universe query: PASS
- Tiny daily panel query: PASS
- Correlation spectrum and orientation pipeline: PASS
- Zero-heavy-data design: FEASIBLE
- Overall autonomous WRDS -> CPU26 empirical flow: READY, subject to the observed authentication gate below

No licensed security-day observations, security identities, returns, prices, market
capitalizations, return matrices, correlations, eigenvalues, or eigenvectors are retained
in this report.

## Observed authentication behavior

- Initial connection: password required YES; Duo Push required YES; connection PASS.
- Standard secure password reuse: `~/.pgpass` created by the official `wrds` client.
- `~/.pgpass` permission mode: `0600` (safe).
- Second completely fresh Python process: password NO; Duo NO; connection PASS; elapsed 0.75 seconds.
- Third completely fresh Python process after approximately 60 seconds: password NO; Duo NO; connection PASS; elapsed 0.75 seconds.
- No password was placed in a command, script, environment manifest, project file, or custom credential file.

The WRDS account name supplied for the test was normalized to the lowercase PostgreSQL
username `harman2020_2`, consistent with WRDS username rules.

## Live CRSP CIZ structure

Accessible front-end schema/library: `crsp`.

The live `crsp` views used in this test are permission-gated views over the accessible
backing library `crsp_a_stock`.

Primary daily CIZ access:

- `crsp.dsf_v2`: flattened CIZ daily stock view with security traits, daily data,
  capitalization, shares, identifiers, and point-in-time classification fields.
- `crsp.stkdlysecurityprimarydata`: narrow daily price/return/capitalization subset,
  used for the 115-row return-panel query.
- `crsp.stkdlysecuritydata`: complete daily security time-series component.

Security and history metadata:

- `crsp.stksecurityinfohist`: point-in-time security/history metadata.
- `crsp.stocknames_v2`: point-in-time name/identifier history.
- `crsp.stksecurityinfohdr`: current/header metadata; do not substitute it for the
  history table when historical point-in-time status matters.

Monthly CIZ access for efficient universe formation:

- `crsp.msf_v2`, including `MthCalDt`, `MthCap`, the CIZ security/share/exchange/status
  fields, and `ShrOut`.

## Exact field mapping

- Stable security identifier: `PERMNO` (`permno`). `PERMCO` is also available at the
  issuer/company level. Ticker is never used as the permanent identifier.
- Trading date: `DlyCalDt` (`dlycaldt`); integer period `YYYYMMDD` is also present.
- Daily total return: `DlyRet` (`dlyret`).
- Delisting treatment: CIZ `DlyRet` already incorporates the delisting return when
  appropriate. `DlyDelFlg='Y'` marks a delisting-return row; `DlyRetMissFlg` explains
  missing returns. A separate legacy-style delisting-return merge is not required for
  the ordinary daily total-return panel. Missing delisting outcomes still require an
  explicit, documented research rule if alternate imputation is desired.
- Price: `DlyPrc`, with provenance/type in `DlyPrcFlg`.
- Shares outstanding: `ShrOut`, measured in thousands.
- Market capitalization: direct `DlyCap`, with type/provenance in `DlyCapFlg`.
  CRSP defines it as closing trade price (or bid/ask average) times shares outstanding,
  in thousands; `DlyPrc * ShrOut` is the consistent construction when needed.
- Exchange / primary listing: `PrimaryExch`; `ConditionalType` distinguishes regular-way
  and special trading conditions; `ExchangeTier` is also available.
- Common-stock/security type: `ShareType`, `SecurityType`, `SecuritySubType`,
  `USIncFlg`, and `IssuerType`.
- SIC / industry: `SICCD` in `dsf_v2`; `NAICS`, `ICBIndustry`, and `UESIndustry` in
  `stksecurityinfohist`.
- Trading/security status: `TradingStatusFlg` and `ConditionalType` on daily rows;
  `SecurityActiveFlg` and delisting action/status/reason/payment fields in
  `stksecurityinfohist`.
- Human-readable labels: `Ticker` in `dsf_v2`; `SecurityNm` and `IssuerNm` in
  `stksecurityinfohist`.

Point-in-time joins use `PERMNO` and the observation date:

```sql
d.permno = h.permno
AND d.dlycaldt BETWEEN h.secInfoStartDt AND h.secInfoEndDt
```

For `stocknames_v2`, use `d.dlycaldt BETWEEN namedt AND nameenddt`. Do not join to a
current header row or current ticker for historical universe construction.

## Historical coverage and tiny capability checks

- 1990 coverage: YES. An exact-date `EXISTS ... LIMIT 1` check succeeded for 1990-01-02.
- 2025 coverage: YES. An exact-date `EXISTS ... LIMIT 1` check succeeded for 2025-01-02.
- Point-in-time test date: 2024-06-28.
- Eligible U.S. common-stock filter:
  - `ShareType='NS'`
  - `SecurityType='EQTY'`
  - `SecuritySubType='COM'`
  - `USIncFlg='Y'`
  - `IssuerType IN ('ACOR','CORP')`
  - `PrimaryExch IN ('N','A','Q')`
  - `ConditionalType='RW'`
  - `TradingStatusFlg='A'`
  - valid positive price, shares, and market cap; nonmissing daily return
- Server-side market-cap ranking with `LIMIT 5`: PASS (exactly five rows retrieved in
  memory). Replacing the limit with 100, 200, or 500 supports the planned universe
  sizes without changing the point-in-time logic or using current membership.
- Point-in-time metadata join for the five test securities: PASS (five rows).
- Daily panel interval: 2024-05-28 through 2024-06-28.
- Raw panel fetched into one Python process: 115 rows, five securities, 23 dates;
  below the hard maximum of 150.
- Stable identifiers, unique security-date keys, date ordering, numeric returns, and
  missing-return handling: PASS. This tiny panel had zero missing returns.
- Complete overlapping return matrix: 23 x 5.
- Sample volatility calculation: PASS.
- Volatility standardization: PASS.
- Correlation matrix: 5 x 5, finite and symmetric.
- Symmetric eigendecomposition: five eigenvalues and a 5 x 5 eigenvector matrix;
  eigenvector orthonormality tolerance below `1e-10`: PASS.
- Spectrum availability: PASS.
- Orientation availability: PASS. Production comparisons must align eigenvector signs
  (and handle near-degenerate subspaces) because eigensolver sign is conventional.

All raw rows and matrix inputs existed only in process memory and were explicitly
discarded after these checks.

## Full empirical-module capability

The discovered CIZ data and CPU26 numerical stack support:

- monthly point-in-time liquid common-stock universes for N=200 and N=100/500 checks;
- one- or two-year trailing daily estimation windows;
- volatility-standardized returns and rolling correlation matrices;
- rolling spectra and rolling eigenvector/orientation measures;
- near-isospectral empirical-state searches;
- sparse long-only minimum-variance portfolios;
- spectrum-only randomized equal-weight subset benchmarks;
- even sparse breadths h=10, 20, and 50;
- strictly out-of-sample realized variance/volatility;
- turnover from consecutive portfolio weights;
- drawdown and raw-return Sharpe diagnostics from the OOS portfolio return stream
  (an excess-return Sharpe additionally requires a chosen risk-free series);
- orientation-confidence/actionability diagnostics;
- point-in-time universe maintenance without current-membership or ticker joins;
- delisting-safe daily total-return treatment using `DlyRet` plus its flags; and
- point-in-time SIC/NAICS/ICB/UES interpretation.

No real empirical study was executed.

## Zero-heavy-data design for the full 1990-2025 run

1. Query `crsp.msf_v2` in bounded year ranges and perform the point-in-time common-stock
   filters plus market-cap ranking on the WRDS server. Return no more than the required
   top-500 monthly membership candidates and keep them as temporary CPU26 state.
2. Convert each selected PERMNO/month into its required one- or two-year estimation
   interval, merge overlapping intervals per PERMNO, and place only those compact
   intervals in a PostgreSQL temporary table for the connection lifetime.
3. Stream only `PERMNO`, `DlyCalDt`, `DlyRet`, and needed return flags from
   `crsp.stkdlysecurityprimarydata` in non-overlapping calendar chunks (for example,
   quarterly or semiannual), joined to the coalesced intervals. Use a server-side cursor
   or `wrds.raw_sql(..., chunksize=...)` so a batch is bounded in RAM.
4. Maintain a rolling two-year RAM ring buffer and rolling sufficient statistics.
   Compute every eligible monthly rebalance as dates advance; do not refetch a separate
   overlapping two-year panel for each month.
5. Validate each dependent calculation, then discard the consumed raw batch and expired
   ring-buffer rows. Retain only compact derived portfolio-level, spectral/orientation,
   diagnostic, table, figure, log, checksum, configuration, and provenance artifacts.

This design creates no full CRSP clone, durable raw CSV/parquet lake, laptop transfer,
or committed licensed observation file.

## Required authentication gate for the main nightly workflow

Observed gate:

1. Start with the Waterloo VPN connected.
2. SSH to CPU26 and verify the expected host/user.
3. Near the beginning of the workflow, open an interactive CPU26 TTY and instantiate
   the official `wrds.Connection` for lowercase username `harman2020_2`.
4. User enters the WRDS password with hidden input and approves the Duo Push.
5. Verify standard `~/.pgpass` exists with mode `0600`.
6. Close the connection and terminate that Python process.
7. Open a completely fresh process with stdin disabled and reconnect.
8. Optionally repeat after approximately 60 seconds. If both reconnects pass without
   password or Duo, print `WRDS AUTH READY FOR NIGHT` and continue.

Human action required at workflow start: hidden WRDS password entry and Duo Push
approval.

Human action after the verified preflight: NONE was observed for an immediate fresh
process and a third fresh process after approximately 60 seconds. This smoke test did
not directly observe a several-hour delay, so the production workflow must fail closed
and surface a new auth gate if a later connection ever requests interaction.

## Cleanup and retention

- Heavy data downloaded or retained: NO.
- Raw CRSP rows saved to disk: NO.
- Raw CRSP transferred to the laptop: NO.
- Tiny raw panel and matrix inputs retained: NO.
- Authorized durable items after cleanup: this report, the small Python virtual
  environment at `~/venvs/wrds-smoke/`, and standard `~/.pgpass` mode `0600`.

## Documentation provenance

- CRSP US Stock & Indexes Database Guide, CIZ flat-file format 2.0:
  https://www.crsp.org/crsp_pdf/crsp-us-stock-indexes-databases-guide-flat-file-format-2-0/
- WRDS CIZ-to-SIZ mapping macro:
  https://wrds-www.wharton.upenn.edu/pages/wrds-research/macros/crsp-ciztosiz-macro/
- WRDS CIZ event-study macro (documents delisting return incorporation):
  https://wrds-www.wharton.upenn.edu/pages/wrds-research/macros/run-an-event-study-ciz-format-macro/
- WRDS PostgreSQL MFA guidance:
  https://wrds-www.wharton.upenn.edu/pages/about/log-in-to-wrds-using-two-factor-authentication/
