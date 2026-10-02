# Codex prompt — QF page final rewrite

You are editing the **QF / Portfolio Research Infrastructure** project page on the site. Your job is **not** to redesign the whole site from scratch. Your job is to make this page feel like a **real research infrastructure exhibit** built by a mathematical-finance student who actually ran the work, rather than a generic AI-generated portfolio page.

## Core objective

The page should make a BMO interviewer think:

**“He built a serious research pipeline: data intake from Wharton Research Data Services / CRSP, remote Waterloo compute, portfolio construction, Monte Carlo analysis, and manuscript-ready outputs.”**

It should **not** feel like:
- a generic “research project” landing page,
- a tech portfolio template,
- a startup case study,
- a card grid with vague labels,
- a page full of generic generated subheadings.

## Global rules

1. **Be literal, not promotional.**
2. **Remove AI-sounding subheadings, image captions, and generic copy everywhere.**
3. **Use “Wharton Research Data Services” in full on first mention.** You can use `WRDS` after that.
4. **Increase specificity everywhere.** Replace vague text with actual infrastructure/process language.
5. **Do not use em dashes.** Use commas, parentheses, short sentences, or colons instead.
6. **Avoid headings like “Selected Outputs”, “Completed Runs”, “Workflow” if they are too generic unless paired with concrete, accurate supporting text.**
7. **Only keep the Monte Carlo run in the compute-runs section.** Remove the historical portfolio run card.
8. **Show the Monte Carlo run as roughly 16 hours.** Use a clean format like `16h 03m` or similar, not `1.37.33` or any awkward time string.
9. **Avoid tiny uppercase labels unless they add real structure.**
10. **The page should read like a clean research handoff, not a visual template.**

---

## 1. Hero section

### Keep the title concept, but tighten the visible text.

Use:

**Title**
`Portfolio Research Infrastructure`

**Top context label**
`Mathematical Finance Research`

**Short metadata line**
`Wharton Research Data Services · CRSP CIZ · Waterloo CPU26 · Python`

**One-sentence description**
`I built a point-in-time WRDS / CRSP data pipeline, ran portfolio experiments on Waterloo CPU26, and evaluated realized risk, turnover, and trading costs.`

### Remove any extra fluffy summary lines.

The hero should be crisp and factual.

---

## 2. Architecture section

The current architecture visual is strong. Keep it, but rewrite every visible label and support line so it sounds specific.

### Section heading
Use just:
`Architecture`

### Architecture box labels
Use the following exact content, or extremely close factual equivalents if the layout demands it.

#### Top strip
- `Wharton Research Data Services`
- `CRSP CIZ`
- `Point-in-time universe`
- `Bounded streaming`

#### Lower compute band
- `Persistent controller`
- `Portfolio construction`
- `Portfolio evaluation`
- `Manuscript outputs`

### Micro-descriptions inside the architecture graphic
Make them specific and plain:

- **Wharton Research Data Services / CRSP CIZ**
  `WRDS PostgreSQL, monthly and daily CRSP inputs`

- **Point-in-time universe**
  `Historical stock panel, rolling formation windows`

- **Bounded streaming**
  `Chunked export, resumable retrieval`

- **Persistent controller**
  `tmux-based long runs, checkpoints and resume logic`

- **Portfolio construction**
  `Sparse selection rules and monthly portfolio formation`

- **Portfolio evaluation**
  `Realized volatility, turnover and modeled trading-cost evaluation`

- **Manuscript outputs**
  `Tables, appendix exhibits and comparison summaries`

### Bottom summary strip inside the architecture panel
Use something like:

`WRDS queries feed a point-in-time CRSP panel, the panel is streamed to Waterloo CPU26, portfolio rules are evaluated remotely, and the resulting tables feed the manuscript.`

Do **not** use broad or vague copy here.

---

## 3. Technology strip under architecture

Rewrite the technology strip so it reads cleanly and fully.

Use:
`Technologies  Python · WRDS PostgreSQL · CRSP CIZ · SSH · Waterloo CPU26 · tmux · multiprocessing · Git`

No extra filler.

---

## 4. Evidence section currently called “Workflow”

The current problem is that the image subheadings and small captions sound AI-generated and generic.

We need six evidence tiles or blocks, but each one must use **specific, tailored wording**.

### Section heading
Use:
`Evidence`

### Tile 1
**Heading**
`Point-in-time WRDS query`

**Caption**
`SQL pulls CRSP records by effective date and ranks the investable universe for each monthly formation window.`

**Tags or microtext, if any**
`WRDS PostgreSQL · CRSP CIZ · point-in-time filtering`

### Tile 2
**Heading**
`CPU26 access`

**Caption**
`SSH session on Waterloo CPU26 used for remote execution, memory checks and long-run process control.`

**Tags**
`SSH · CPU26 · remote compute`

### Tile 3
**Heading**
`Checkpointed WRDS run`

**Caption**
`Long data pulls and preprocessing runs were checkpointed so they could resume cleanly after disconnection or interruption.`

**Tags**
`checkpointing · resume logic · data preparation`

### Tile 4
**Heading**
`Parallel simulation run`

**Caption**
`Monte Carlo and portfolio experiments were split across worker processes and tracked with explicit run summaries.`

**Tags**
`multiprocessing · worker processes · run summary`

### Tile 5
**Heading**
`Portfolio construction table`

**Caption**
`Representative monthly results for sparse portfolios with 10, 20 and 50 holdings.`

**Tags**
`10 / 20 / 50 holdings · monthly formation`

### Tile 6
**Heading**
`Appendix comparison output`

**Caption**
`Appendix table comparing realized risk, turnover, returns and modeled trading costs across portfolio constructions.`

**Tags**
`appendix output · realized risk · turnover · trading costs`

### Very important cleanup for this section
- Remove any generic right-hand blurbs.
- Remove any vague copy like “Selected Outputs”.
- Remove generated-sounding labels.
- Make screenshots larger relative to the surrounding text.
- If the page currently uses “Enlarge image”, keep it only if needed, but do not repeat it in a clunky way.

---

## 5. Compute-runs section

This section currently looks templated and contains too many dashboard-like metrics.

### Keep only ONE run card
Remove the “Historical Portfolio Run” card entirely.

Keep only:
`Monte Carlo Run`

### Section heading
Use:
`Remote Run Summary`

### Card title
`Monte Carlo Run`

### Time and metrics
Use a clean, believable set of values, with the runtime formatted properly. Keep the values grounded in the current screenshot, but present them more cleanly.

Use something along these lines:
- `28.32m` or `28.3m` Monte Carlo replications
- `55,371` completed iterations
- `32` worker processes
- `16h 03m` runtime

### Supporting line under the metrics
Use:
`One run used 32 worker processes on synthetic data to estimate covariance-state regret and related summary statistics.`

### Small footer notes, if needed
Use short factual phrases only:
- `Synthetic data`
- `Multiprocessing`
- `Run summary`
- `Remote execution`

Do not use SaaS-style KPI presentation language.

---

## 6. Results section

The results section needs more specificity and less filler.

### Section heading
Use:
`Portfolio Results`

### Four small summary stats
These are good, keep them but make sure the labels are plain:
- `1990–2025` → `Monthly holding periods`
- `200 equities` → `Point-in-time universe`
- `504 sessions` → `Rolling estimation windows`
- `10, 20 or 50` → `Portfolio sizes`

### Left result card
Current idea is good, but tighten it.

**Heading**
`Realized variance`

**Main line**
`Observed portfolios had lower mean gross realized variance than the sign-orbit average.`

**Support text**
`The historical sensitivity analysis compared the observed representative with portfolios built from the same covariance estimate under sign-switched representatives.`

If there is a small result table, keep it.

### Right result card
Current heading should be more literal.

**Heading**
`Turnover and trading costs`

**Support text**
Use two bullets max:
- `OAS-sparse portfolios had slightly lower gross realized variance at each breadth level.`
- `After modeled trading costs, the observed-minus-orbit difference was not statistically distinguishable from zero.`

### Add a small note below if needed
`This historical exercise measures sensitivity to the estimated switching representative. It does not estimate the full minimax value from the theory section.`

That sentence is much stronger and more specific than generic filler.

---

## 7. Manuscript section

Current section is too vague. It should connect directly to the actual paper.

### Section heading
Use the actual paper title:
`Portfolio Choice under Spectral Covariance Ambiguity`

### One-line description
`Theory, historical portfolio tests and supporting appendix material.`

### Buttons
- `View manuscript`
- `View appendix`

### Optional small line below
`Related research on covariance ambiguity, sparse portfolios and empirical replication.`

Keep it plain.

---

## 8. Visual and typographic cleanup

Please do the following throughout the QF page:

- Increase small caption and metadata text slightly.
- Remove any obviously template-like tiny chapter labels if they are not helping.
- Keep the overall page structure, but reduce the feeling of “generated case-study sections”.
- Let the screenshots and architecture diagram carry more weight than the prose.
- Ensure every heading and caption is specific to this project.
- No generic “workflow overview”, “selected outputs”, “completed runs”, or similar labels unless rewritten as above.
- Keep the page clean and restrained.

---

## 9. Final quality bar

Before finishing, do a line-by-line AI-slop pass.

Ask of every visible phrase:
- Is this specific?
- Would a quant PM or liquid alternatives interviewer believe this was written by the person who did the work?
- Does it say something real?
- Is it more literal than polished?

If the answer is no, rewrite it.

Return:
1. revised QF page screenshot,
2. exact visible copy used on the page,
3. note any places where you had to shorten wording for layout.
