# Audit LTG — Detailed Page Specification

## Objective
Refine the **LTG Trading & Reporting System** page so it clearly presents the workflow without looking like a random dump of code and screenshots.

The page should explain the system as a practical trading workflow: intake, validation, price routing, portfolio state, and web reporting.

This page must match the final homepage design language.

## Project naming
- **Primary title:** `LTG Trading & Reporting System`
- **Secondary line (small):** `Laurier Trading Group`

Do not rename it to vague alternatives.

## Design direction
Use a **white or soft off-white background** with restrained navy accents and touches of LTG gold.

Overall feel:
- editorial
- crisp
- process-led
- not like a code scrapbook
- professional but visually attractive

Use:
- LTG logo
- pie chart / allocation visual as subtle hero or card background
- navy and gold accents, restrained

Avoid:
- AI-sounding source captions
- code-heavy clutter
- too much raw code at the expense of process
- unnecessary buzzwords

## Hero section
- large title left
- small secondary line: `Laurier Trading Group`
- 1–2 sentence explanation only
- faint pie chart / public-reporting visual can appear behind or beside hero

Hero summary:
> Built the workflow connecting trade intake, validation, quote routing, portfolio-state calculation and public reporting for Laurier Trading Group.

Tech line:
- Google Forms
- Google Sheets
- Apps Script
- JavaScript
- Yahoo Finance
- Stooq
- Twelve Data
- MarketData.app
- Squarespace

## Workflow navigation line
Use:
- `Trade Intake`
- `Validation / Event Log`
- `Quote Routing`
- `Scheduled Refresh`
- `Portfolio State`
- `Public Reporting`

## Pricing adapters strip
Keep source logos and names. Bring the logos back.

Use:
- **Yahoo Finance** — `Equities / ETFs / FX`
- **Stooq** — `Fallback quotes`
- **Twelve Data** — `Quote adapter`
- **MarketData.app** — `Options quotes`
- **Manual marks** — `Bonds / override prices`

No fake captions.

## Main body structure
Use alternating image/text sections so the process is easy to follow.

### Trade Intake
Capture instruments, direction, entry price, stops and portfolio fields in a structured record.
Show the intake table screenshot.

### Validation and Event Log
Explain that requests are normalized, portfolio allocation rules are checked, and accepted/rejected events are written to the lifecycle log.
Show a tightly cropped event-engine code screenshot.

### Quote Routing
Explain that instruments are mapped to source-specific symbols, providers are attempted in order, and manual marks are used when needed.
Show a tightly cropped quote-routing code screenshot.

### Scheduled Refresh
Explain that time-driven Apps Script jobs refresh reporting state and retain execution history.
Show scheduled run history.

### Portfolio State
Explain that accepted events and sourced marks are combined to rebuild holdings, notional allocation and trade-level P&L.
Show portfolio-engine snippet plus holdings table.

### Public Reporting
Show public website views: trade logs and instrument-allocation pie chart.
Explain that the system publishes trade status and allocation views through embedded reporting on the LTG website.

## Public-reporting finish
Prominently show:
- trade-log website screenshot
- instrument-allocation pie chart
- public link: `lauriertradinggroup.ca/simulation`

This should be the payoff.

## Copy cleanup rules
- remove all AI-sounding captions
- shorten vague or ornamental wording
- no buzzwords
- make code secondary to workflow
- keep visual hierarchy strong
- keep logo use tasteful

Good caption style:
- `Capture instrument, direction, entry and stop fields in one structured record.`
- `Normalize requests, validate portfolio constraints, and append accepted or rejected lifecycle events.`
- `Resolve each instrument to its mapped provider, try fallback symbols, and use manual marks where required.`
- `Time-driven Apps Script runs refresh the reporting state and retain execution history.`
- `Rebuild holdings from accepted events, determine notional allocation, and calculate trade-level P&L from current marks.`
- `Publish trade status and instrument allocation through embedded views on the LTG website.`

## Output expectation
Return a page that feels clear, operational, well designed, less code-heavy, consistent with the homepage, and specific enough that the workflow is obvious at a glance.