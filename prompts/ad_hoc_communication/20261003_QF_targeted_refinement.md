# QF: manuscript-specific process and presentation corrections

## Scope and sources

Edit only the existing QF detail page and its necessary assets. Preserve the approved white editorial design and the actual manuscript. This prompt supersedes conflicting older QF page instructions, including old metric formatting and generic copy. Do not start a new research project or redesign the whole site.

Use the current supplied desktop view, the final manuscript titled 'Portfolio Choice under Spectral Covariance Ambiguity', its matching appendix, and the source records behind the compute exhibits. Section 7 and Table 2 support the historical comparison. Source records, not earlier prompts, establish compute timings and screenshot provenance.

Internal editing instructions below must not appear in the public page.

## Shared style across all four project pages

- Inherit the approved homepage serif headings and sans-serif body. No new font family.
- Keep the warm-white background, navy text, quiet blue links and thin neutral rules. Use existing shared tokens. Fallback only: #FAFAF7 page, #FFFFFF artifact surfaces, #14273D text, #566170 secondary text, #DEE3E9 rules, #2F5FB3 links.
- Body approximately 16px, captions 15px, tool descriptions 14px. Do not shrink dense source material to fit a decorative card.
- Replace keyword ribbons and dot-separated technology lists with a compact three-column definition list. Each column has a functional label and a brief explanation naming the tools. No surrounding cards, skill pills, dot separators or slash lists. Stack the same pattern on mobile.
- Use present-tense descriptions of what happens. No imperatives to the visitor. Prefer two short sentences over long comma chains.
- Remove em dashes, generic slogans, miniature numbered eyebrows, file paths, QA notes, and visible image-manipulation instructions. Preserve accessible zoom with accurate aria-labels and visible keyboard focus.
- Page edits stay scoped. Shared component changes belong to the integration agent so parallel agents do not overwrite one another.

## 1. Exact identity and introduction

H1:
Portfolio Choice under Spectral Covariance Ambiguity

Small journal line:
Submission to Mathematical Finance

Hyperlink the words 'Mathematical Finance' wherever they refer to the journal, including this line, status copy, relevant homepage metadata and manuscript section. Use the official journal destination:
https://onlinelibrary.wiley.com/journal/14679965

Do not link generic mentions of the academic subject to the journal automatically.

Replace the current long hero explanation with:

The study tests how covariance information changes stock selection. Its empirical work uses CRSP data from Wharton Research Data Services and runs on Waterloo CPU26.

Keep the actual manuscript-title crop at the right of the introduction. Do not fade it so much that it becomes an empty white rectangle. Use a sharp export, no invented cover and no unrelated paper version.

### Tool context: exact three columns

Data access
CRSP CIZ records are queried through WRDS PostgreSQL.

Computation
Python runs the portfolio tests on Waterloo CPU26.

Run control
SSH provides access. tmux and checkpoints keep long jobs resumable.

Wharton Research Data Services is already spelled out in the introduction. Do not repeat a second long list of Python, WRDS, PostgreSQL, CRSP, SSH, tmux, multiprocessing and Git. Mention versioning beside the relevant run/report only if useful.

## 2. Integrate the architecture into the page

The current white rectangle looks like a pasted architecture screenshot. Rebuild its labels and connectors as native HTML with a small SVG connector layer, or as accessible responsive SVG. Match the page font, text size and spacing. Do not regenerate or alter any measured result.

Section heading:
How the study runs

Remove the old multi-clause sentence beginning 'WRDS queries form a point-in-time CRSP panel...'. Do not replace it with another long summary.

Use these six readable process nodes, with exactly one short explanation each:

1. Retrieve CRSP records
PostgreSQL queries read the records through Wharton Research Data Services.

2. Form the monthly universe
Each formation date selects the 200 largest eligible stocks.

3. Read the return history
Each stock contributes 504 daily total returns to the estimation window.

4. Select the portfolios
A greedy search with one-stock swaps chooses 10, 20 or 50 names.

5. Measure next-month risk
The selected weights drift through the month as daily returns arrive.

6. Compare the results
Risk and trading-cost comparisons become the manuscript tables.

Around the actual remote-execution stages, use one quiet group label:
Waterloo CPU26

Do not imply that SSH is a data-transformation stage. Show SSH as a dashed access/control connection to CPU26. Add only these short control annotations:
- SSH access
- tmux session
- Saved checkpoints

Place 'Queries read data in chunks' beside retrieval if the implementation demonstrates that behavior. Do not claim that every query or every input cache is resumable unless it is.

One optional sentence below the figure:
The calculations run on CPU26 rather than the laptop. The controller saves completed work for later resumption.

The first data-source node represents CRSP reached through WRDS, not two successive databases. Avoid multiple redundant WRDS labels.

## 3. Replace 'Evidence' with a sequential research walkthrough

Section heading:
From data to portfolio tests

Use a semantic ordered sequence, not six unrelated feature cards. Keep approximately the current evidence density. On desktop, connect adjacent steps with subtle arrows where the reading order is unambiguous. On mobile, use a simple vertical flow. Do not draw decorative connectors across text or connect a separate synthetic experiment to historical results as though they were one run.

Use the following exact step text and the specified evidence.

### Run on Waterloo CPU26

The run starts on Waterloo CPU26. A preflight check reads the available CPU and memory before work begins.

Visual: existing CPU26 environment or setup evidence. Describe a documentation extract as an extract, not as a live terminal session. Hide usernames, keys and private paths.

### Select the monthly universe

The SQL query then selects each month's 200 largest eligible stocks. It uses CRSP records valid at that formation date.

Visual: the actual point-in-time CRSP SQL excerpt, focused on effective dates and universe selection. Keep source text intact.

### Retrieve the return history

The query reads the daily returns needed for each estimation window. The runner saves progress so interrupted work can continue.

Visual: existing bounded-retrieval/checkpoint record. Confirm that the caption describes the demonstrated checkpoint boundary; do not promise resumption halfway through an individual SQL query if only completed tasks are resumable.

### Run the covariance comparisons

The prepared returns feed the same portfolio selector under two inputs: the observed covariance estimate and sign-switched versions. The comparison uses 1,024 persistent sign paths.

Visual: prefer a small native diagram based on the manuscript's actual comparison:
Observed covariance -> Same selector -> Following month's returns
Sign-switched covariance -> Same selector -> Same following month's returns

Add this short explanatory line only if needed:
The sign switches preserve eigenvalues and individual-asset variances.

Do not use the separate synthetic Monte Carlo screenshot as evidence that this historical sign-path run completed. Move that screenshot into the compute section below. Do not claim the massive synthetic replication count is the number of historical sign paths.

### Measure the following month's risk

Each selected portfolio is evaluated on the same subsequent returns. The table compares average realized variance for 10, 20 and 50 holdings.

Visual: a crisp excerpt of manuscript Table 2. Caption describes the table's actual aggregate, not 'representative monthly results'.

### Compare turnover and costs

The next comparison adds turnover and trading-cost assumptions. It also includes OAS shrinkage and an equal-weight portfolio of all 200 stocks.

Visual: matching appendix Table G.2. Use the appendix version paired with the manuscript. If the matching source is unavailable, preserve the existing source image only when its version is established; do not fabricate a companion table.

Do not repeat the step prose as another caption beneath the image. One explanation per step is enough. Keep code secondary and use plain captions rather than words such as 'artifacts', 'target statistics' or 'research-grade outputs'.

## 4. One concise Monte Carlo section

Heading:
Monte Carlo computation

The owner explicitly corrected the replication total in the current request. The visible total is:

283.23M
Monte Carlo replications

Replace every 28.32m, 28.32M and 283.23m reference belonging to this page's replication total. Use uppercase M.

Use this process explanation instead of the existing jargon-heavy sentence:

The runner divides the simulation into batches. Python workers process them in parallel, then the results are combined.

Use the existing synthetic parallel-run screenshot here, not as a historical portfolio-production proof. Label the experiment 'Synthetic simulation' if that is the source record's scope.

A second metric may read:
32
Worker processes

Only retain 32 for the corrected run if the current records or owner confirmation connect that worker count to it. Likewise, retain completed-shard counts and runtime only when they describe this same run. Do not combine an old run's 55,371 shards or runtime with a new total merely because they were previously displayed together.

Important correction: earlier assistant prompts prescribed 16h 03m without establishing a source. Those prompts are not runtime evidence. Use a genuine duration from the matching run record, or omit the duration. Do not invent a replacement duration or alter a log screenshot. If a sourced duration is retained, format it as '16 h 03 min' or the actual corresponding value.

The updated count is owner-provided, not independently measured during this presentation task. Preserve that distinction in internal provenance only. Public metrics should stay compact, not acquire a compliance paragraph.

## 5. Make the results table understandable

Keep the portfolio-results section, but remove slash-separated number pairs and the cryptic subtitle.

Section heading:
Portfolio results

Scope row, without dot-separated prose:
- Period: 1990–2025
- Holding months: 432
- Stocks per universe: 200
- Estimation history: 504 trading days

Use a native HTML table with real column headings:

| Holdings | Observed correlations | Sign-switched correlations, mean |
| 10 | 0.0318 | 0.0518 |
| 20 | 0.0282 | 0.0459 |
| 50 | 0.0275 | 0.0385 |

Table title:
Average annualized variance

Explanation above the table:

The portfolio rule is unchanged between the two columns. Only the signs in its covariance input change.

Explanation below:

Each value averages realized variance across 432 holding months. Lower values mean less variation in portfolio returns.

Use the supplied Table 2 numbers exactly. These are variances, not volatility percentages, returns, alpha or profits. Do not append percent signs or recalculate them into a different metric. Do not call this an allocation/holdings table.

Short main finding:
Observed correlations produced lower average variance at all three portfolio sizes.

### Practical comparison

Heading:
After trading costs

Use three short sentences rather than a vague bullet list:

OAS shrinkage produced slightly lower gross variance. The full-universe equal-weight portfolio had the highest reported certainty equivalent after the stated costs. The cost-adjusted observed-versus-sign-orbit difference was not statistically distinguishable from zero.

Keep 'View cost comparison' as a link to the actual matching appendix/table, if available. Retain the result limitations because they explain the finding, not as a separate defensive box.

Delete this standalone sentence exactly as requested:
'This historical exercise measures sensitivity to the estimated switching representative. It does not estimate the full minimax value from the theory section.'

Do not replace it with a similar defensive disclaimer. The page can identify itself as a covariance-input comparison in its normal explanation.

## 6. Manuscript finish and journal link

Heading:
Read the paper

Use the exact manuscript title as the linked document title:
Portfolio Choice under Spectral Covariance Ambiguity

Replace 'Minimax theory, labelled-data results and the 1990–2025 portfolio study' with:

The paper asks what covariance information is needed to choose a small portfolio. The appendix contains the proofs and full empirical comparisons.

Then add the owner's requested current status:

Passed desk review at Mathematical Finance; currently under expert review.

Hyperlink 'Mathematical Finance' to:
https://onlinelibrary.wiley.com/journal/14679965

The owner supplied this submission status in the current request. It is not verified by the journal homepage. Do not describe the manuscript as accepted, published, endorsed or externally verified. If a known current submission record contradicts the owner-provided status, flag that privately before publishing; do not invent a status.

Links:
View manuscript
View appendix

Do not expose editor correspondence, IDs or reviewer details.

## 7. Technical and visual acceptance

- The architecture labels are native and readable, not a screenshot of another page.
- The tools block names each tool's purpose rather than listing keywords.
- The research sequence reads in a single direction. Every step explains what happens next.
- The separate synthetic computation stays separate from the 1,024-path historical comparison.
- Tables have explicit column names and units.
- The requested standalone disclaimer is gone; actual comparative findings remain accurate.
- Journal references link to the official journal homepage.
- Screenshot captures have no internal notes or manipulation instructions. Code/log extracts are not presented as live interfaces.
- Check 1440px desktop and 390px mobile, readable zoom, image aspect ratios and all links.

Return screenshots, changed files, final visible copy and a short private record of metric/source checks. Do not print these developer checks on the website.