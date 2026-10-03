# Audit QF — Detailed Page Specification

## Objective
Refine the **QF / Portfolio Choice under Spectral Covariance Ambiguity** page so it looks deliberate, editorial, and human-made. The goal is to present the work as a serious research-and-systems artifact, not a generic AI-generated project page.

This page must visually match the final homepage design system.

## Project naming
Use this exact naming structure everywhere on the page:
- **Primary title:** `Portfolio Choice under Spectral Covariance Ambiguity`
- **Secondary line (small):** `Submission to Mathematical Finance`

Do **not** use generic labels like “Portfolio Research Infrastructure” as the main project name.

## Design direction
Use a **white or off-white editorial background** with restrained navy/blue accents.

Style reference:
- clean and minimal like a serious research microsite
- typography with personality, but still professional
- not generic ChatGPT/OpenAI landing-page styling
- not overly dark, not glass-heavy, not noisy
- page should feel closer to a refined research feature than a dashboard

Avoid:
- buzzwords
- overdesigned gradients
- oversized glowing effects
- repetitive AI-sounding captions
- vague placeholder language

## Hero section
- large project title on the left
- small secondary line: `Submission to Mathematical Finance`
- 1–2 sentence summary only
- on the right or softly behind the hero, use a faint crop from the manuscript first page
- background image must be subtle and low-contrast

Hero summary:
> Built a point-in-time equity research pipeline using Wharton Research Data Services (WRDS), CRSP CIZ data, and Waterloo CPU26 to study portfolio selection under spectral covariance ambiguity.

Tech line:
- Python
- WRDS
- PostgreSQL
- CRSP CIZ
- SSH
- Waterloo CPU26
- tmux
- multiprocessing
- Git

## Architecture section
Heading: `Architecture`

Flow:
1. Wharton Research Data Services (WRDS) / CRSP CIZ
2. Point-in-time universe formation
3. Bounded streaming / retrieval
4. Remote compute on Waterloo CPU26
5. Portfolio construction
6. Portfolio evaluation
7. Manuscript tables / appendix outputs

Use direct box copy:
- `CRSP CIZ via WRDS` — `Monthly and daily CRSP inputs retrieved through WRDS PostgreSQL`
- `Point-in-time universe` — `Effective-dated filtering and monthly formation windows`
- `Bounded streaming` — `Chunked export with resumable retrieval`
- `Persistent controller` — `tmux, checkpoints and resume logic for long remote runs`
- `Portfolio construction` — `Sparse portfolio rules evaluated across monthly formation dates`
- `Portfolio evaluation` — `Realized variance, turnover and modeled trading costs`
- `Manuscript outputs` — `Tables, appendix exhibits and portfolio comparisons`

Avoid vague labels like “data flow” or “workflow engine” unless concrete.

## Evidence section
Heading: `Evidence`

Use a clean 2-column editorial card grid. Each card has image, short title, one sentence caption.

1. **Point-in-time CRSP universe query**
   - show query / extraction screenshot
   - caption should explain effective-dated CRSP filters used to form each month’s eligible universe

2. **CPU26 access**
   - show SSH / remote environment screenshot
   - caption should mention remote execution, CPU / memory checks, and pre-run environment control

3. **Checkpointed WRDS data pull**
   - show retrieval / checkpoint screenshot
   - caption should mention long data pulls that can resume without restarting the full run

4. **32-worker Monte Carlo run**
   - show the parallel simulation screenshot
   - caption should say Monte Carlo and portfolio experiments were distributed across 32 workers and aggregated after completion

5. **Observed vs. sign-orbit portfolios**
   - show output table or manuscript figure
   - caption should reference realized variance comparison across portfolio sizes

6. **Risk, turnover and cost comparison**
   - show appendix/manuscript comparison output
   - caption should mention realized risk, turnover, and modeled trading costs

Remove generic or repetitive sublabels. Keep captions specific and restrained.

## Remote run summary strip
Heading: `Remote Run Summary`

Keep one concise run summary:
- `28.32m` Monte Carlo replications
- `55,371` completed shards
- `32` worker processes
- `16h 03m` runtime

Small line:
> 32 worker processes evaluated persistent sign-path experiments and aggregated covariance-state target statistics.

## Results section
Heading: `Portfolio Results`

Summary row:
- `1990–2025` monthly holding periods
- `200 equities` point-in-time universe
- `504 sessions` rolling estimation windows
- `10, 20 or 50` portfolio sizes

Block 1: `Realized variance`
- state that observed portfolios had lower mean gross realized variance than the sign-orbit benchmark
- include the three breadth comparisons already on the page
- keep wording restrained and factual

Block 2: `Turnover and trading costs`
- explain that after modeled trading costs, the observed-minus-orbit difference was not statistically distinguishable from zero
- do not oversell

## CTA / manuscript section
At the bottom:
- show manuscript title again
- small line: `Minimax theory, labelled-data results and the 1990–2025 portfolio study.`
- buttons: `View manuscript` and `View appendix`

Keep CTA quiet.

## Global cleanup rules
- remove AI-sounding phrases
- no em dashes if avoidable
- no buzzwords like “measured work”, “traceable runs”, “robust stack”
- no unnecessary jargon when plainer language works
- every heading and caption should say something concrete
- preserve specificity around WRDS, CRSP CIZ, SSH, CPU26, Monte Carlo, turnover, trading costs
- keep copy short and visually elegant
- ensure page feels cohesive with homepage

## Output expectation
Return a polished page that feels clean, research-grade, visually premium, clearly human-edited, and consistent with the homepage design system.