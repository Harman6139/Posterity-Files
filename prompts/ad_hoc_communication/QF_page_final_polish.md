# Codex prompt - QF page final polish

You are editing the current Portfolio Research Infrastructure page only.

The page is already structurally strong. Do not redesign it. This is a final surgical pass focused on specificity, readability, and removing the last generic or AI-sounding labels.

## Goal

The page should read like a real mathematical-finance research handoff:

Wharton Research Data Services / CRSP data -> Waterloo CPU26 -> checkpointed remote compute -> portfolio construction -> realized-risk / turnover / cost evaluation -> manuscript outputs

Do not add new sections. Do not change the overall visual structure.

## 1. Evidence section

Keep the six existing evidence blocks and their current screenshots.

Replace the current headings and captions with the following exact copy.

### Block 1
Heading: Point-in-time CRSP universe query
Caption: Effective-dated CRSP filters form each month’s 200-stock universe before estimation.
Optional metadata: WRDS PostgreSQL · CRSP CIZ · point-in-time filtering

### Block 2
Heading: CPU26 access
Caption: SSH session used to check CPU, memory and active processes before remote runs.
Optional metadata: SSH · Waterloo CPU26 · remote compute

### Block 3
Heading: Checkpointed WRDS data pull
Caption: Long data pulls write checkpoints so interrupted work can resume without restarting the full query.
Optional metadata: checkpointing · resume logic · data preparation

### Block 4
Heading: 32-worker Monte Carlo run
Caption: Persistent sign paths were split across worker processes and aggregated after completion.
Optional metadata: multiprocessing · persistent sign paths · run summary

### Block 5
Heading: Observed vs. sign-orbit portfolios
Caption: Realized variance for the observed covariance representative and 1,024 persistent sign paths at each breadth.
Optional metadata: 10 / 20 / 50 holdings · 1,024 sign paths

### Block 6
Heading: Risk, turnover and cost comparison
Caption: OAS, observed, sign-orbit and full-universe portfolios compared on realized risk, turnover and modeled trading costs.
Optional metadata: OAS · turnover · modeled trading costs

## 2. Architecture section

Keep the architecture diagram.

Change the first data box title from:
CRSP CIZ

to:
CRSP CIZ via WRDS

Keep these core stages visible:
- Wharton Research Data Services
- CRSP CIZ via WRDS
- Point-in-time universe
- Bounded streaming
- Persistent controller
- Portfolio construction
- Portfolio evaluation
- Manuscript outputs

Reduce microscopic prose. Delete or shorten any tiny explanatory text that is too small to read at normal browser scale.

Bottom architecture sentence:
WRDS queries form a point-in-time CRSP panel, the panel is streamed to Waterloo CPU26, portfolio rules are evaluated remotely, and the resulting tables feed the manuscript.

## 3. Remote Run Summary

Keep only the single Monte Carlo run card.

Section heading:
Remote Run Summary

Card title:
Monte Carlo Run

Use these metric labels exactly:

28.32M
Monte Carlo replications

55,371
Completed shards

32
Worker processes

16h 03m
Runtime

Important:
- use uppercase M, not lowercase m
- format runtime as 16h 03m
- do not use awkward punctuation-based time formats

Supporting sentence:
32 worker processes evaluated persistent sign-path experiments and aggregated covariance-state regret statistics.

Remove generic phrases such as:
- related summary statistics
- synthetic computation framework
- scalable parallel execution
- high-performance compute

If tiny footer labels are retained, keep only literal ones such as:
Synthetic data · multiprocessing · remote execution

## 4. Portfolio Results

Keep the current layout.

### Left result card
Heading: Realized variance

Main statement:
Observed portfolios had lower mean gross realized variance than the sign-orbit mean at all three breadths.

Support sentence:
The historical sensitivity analysis compares the observed covariance representative with portfolios formed from sign-switched representatives of the same estimated covariance state.

Keep the existing numerical table:
- 10 holdings: 0.0318 / 0.0518
- 20 holdings: 0.0282 / 0.0459
- 50 holdings: 0.0275 / 0.0385

Do not over-explain the table.

### Right result card
Heading: Turnover and trading costs

Use only these two bullets:
- OAS-sparse portfolios had slightly lower gross realized variance at each breadth level.
- After modeled trading costs, the observed-minus-orbit difference was not statistically distinguishable from zero.

Keep the View cost intervals link if it already works.

Small note beneath the section:
This historical exercise measures sensitivity to the estimated switching representative. It does not estimate the full minimax value from the theory section.

## 5. Manuscript section

Keep the exact manuscript title:
Portfolio Choice under Spectral Covariance Ambiguity

Replace the generic description with:
Minimax theory, labelled-data results and the 1990-2025 portfolio study.

Keep buttons:
- View manuscript
- View appendix

Remove any extra generic descriptive sentence unless needed for spacing.

## 6. Typography and visual cleanup

Do not change the font family or overall page design.

Make only these final readability changes:
- increase evidence-caption text by roughly 1-2px
- slightly darken evidence-caption text on the off-white background
- keep headings visually stronger than captions
- reduce tiny architecture annotations instead of shrinking them further
- crop the first evidence screenshot slightly tighter if needed so the first row is more balanced
- if possible, enlarge the CPU26 screenshot slightly so the first row feels even
- do not add new cards, pills, badges, or section numbers

## 7. Language rules

Perform a final visible-text pass.

Do not use:
- em dashes
- generic AI phrases
- vague section names such as Selected Outputs
- generic artifact names such as Portfolio construction table
- generic labels such as Parallel simulation run
- promotional wording

Prefer exact nouns:
- CRSP universe
- WRDS query
- CPU26 access
- checkpointed data pull
- persistent sign paths
- Monte Carlo run
- realized variance
- turnover
- trading costs
- manuscript

## 8. Final output

Return:
1. a full-page screenshot of the revised QF page
2. the exact visible copy used for all six evidence blocks, Remote Run Summary, Portfolio Results, and manuscript section
3. confirmation that:
   - 28.32M uses uppercase M
   - runtime is 16h 03m
   - the historical run card is absent
   - first mention of WRDS is written as Wharton Research Data Services
   - no em dashes remain on the page

Do not make unrelated changes.
