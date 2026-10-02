# Codex prompt — LTG page final rewrite

You are editing the **LTG Trading & Reporting System** page. Your job is to make this page feel like a **real operational workflow** that connects trade entry, validation, pricing, portfolio state and website reporting.

The current version is improved, but still needs another rigorous pass.

## Core objective

A BMO interviewer should think:

**“He built the operating layer behind a trading workflow: event capture, validation, multi-source pricing, scheduled refreshes, portfolio state, and public reporting.”**

The page should **not** feel like:
- a random pile of code screenshots,
- a generic low-code website,
- a generated systems page,
- or a cleaned-up code dump.

## Global rules

1. **Bring back the pricing-source logos / brand assets** for the data-provider section.
2. **Do not bring back the AI-style captions.** Logos stay, fluffy captions do not.
3. **Use plain factual labels only.**
4. **No em dashes.**
5. **Reduce any remaining AI-sloppy headings, subheadings, or mini-captions.**
6. **Keep the public-reporting screenshots large.** They are the strongest visual proof.
7. **The page should explain the pipeline clearly in 5 to 6 steps.**

---

## 1. Hero section

### Title
Use:
`LTG Trading & Reporting System`

### Description
Use:
`Built the workflow connecting trade intake, validation, price sourcing, portfolio state and public reporting for Laurier Trading Group.`

### Tech line
Use:
`Google Forms · Google Sheets · Apps Script / JavaScript · Yahoo Finance · Stooq · Squarespace`

### Workflow line
Use:
`Trade Intake → Validation → Quote Routing → Portfolio State → Web Reporting`

This should be clean and readable.

---

## 2. Pricing/data-source section

The prior version with provider logos was better visually, but the captions were bad. We want the logos back, with much cleaner language.

### Section heading
Use:
`Pricing adapters`

### Bring back the visual row/grid of source logos/assets for:
- Yahoo Finance
- Stooq
- Twelve Data
- MarketData.app
- Manual marks

### Under each source, use only short, factual labels
No marketing prose.

Use exactly this style:
- `Yahoo Finance` → `Equities / FX`
- `Stooq` → `Fallback source`
- `Twelve Data` → `Quote adapter`
- `MarketData.app` → `Quote adapter`
- `Manual marks` → `Overrides`

If layout needs one more short line, keep it factual, for example:
- `Used when a mapped instrument resolves there`
- `Manual current-price override`

But do **not** write anything that sounds promotional or AI-generated.

---

## 3. Trade Intake block

### Heading
`Trade Intake`

### Caption
`Capture instrument, direction, entry and portfolio fields in a structured record.`

Use the current sheet screenshot if it is the cleanest one.

---

## 4. Event Engine block

### Heading
`Event Engine`

### Caption
`Normalize requests, enforce allocation rules and write lifecycle events.`

Keep one concise code excerpt only. Make sure the crop highlights the normalization / validation / append logic.

Do not show too much code.

---

## 5. Quote Routing block

### Heading
`Quote Routing`

### Caption
`Map instruments to quote sources and fall back to manual marks where needed.`

Above or beside the code excerpt, show the provider logo strip from section 2, or at least keep a visual relationship between quote-routing logic and the actual providers.

Keep one cropped code excerpt only.

---

## 6. Scheduled Refresh block

### Heading
`Scheduled Refresh`

### Caption
`Run scheduled portfolio refreshes and retain execution history.`

The execution-history table is better than code for this section. Prefer the run-history screenshot.

If there is a short right-aligned helper line, use:
`Scheduled Apps Script triggers and execution logs.`

Nothing fluffier than that.

---

## 7. Portfolio State block

### Heading
`Portfolio State`

### Caption
`Rebuild holdings and calculate trade-level state from accepted events and marks.`

Use:
- one short code excerpt for the calculation logic,
- and the holdings/state table beneath it.

This is good as a two-part evidence block.

---

## 8. Public Reporting block

### Heading
`Public Reporting`

### Caption
`Publish trade status and allocation views to the LTG website.`

Keep the trade-log screenshot and the allocation-pie screenshot large.

If needed, add a small source line above the screenshots:
`lauriertradinggroup.ca/simulation`

But keep it subtle.

---

## 9. Structural and visual cleanup

Please do a rigorous pixel-level cleanup on the LTG page.

### Specifically:
- Keep the page light and clean.
- Keep more whitespace between sections.
- Keep the logos / data-source assets.
- Remove any weak or generic explanatory captions.
- Keep the code excerpts short and visually subordinate to the system story.
- Make sure the section headings are all consistent.
- Ensure all microcopy sounds like something a human who built the workflow would write.
- Avoid generated-sounding phrases like “powered by”, “flexible”, “reliable”, “robust”, “multi-source pricing” as a marketing phrase, etc.

`Price sourcing` and `quote routing` are fine. Promotional copy is not.

---

## 10. Final quality bar

Before finishing, do a visible-text review line by line.

Ask:
- Does this sound natural?
- Is it specific?
- Does it explain what the system actually does?
- Is it cleaner because of the rewrite, not more verbose?

Return:
1. revised LTG page screenshot,
2. exact visible copy used on the page,
3. a note confirming that the provider logos/assets were restored without the old AI-style captions.
