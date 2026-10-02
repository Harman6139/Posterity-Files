# Codex prompt - LTG page visual redesign

You are editing the current **LTG Trading & Reporting System** detail page only.

I have already shown the current full-page screenshot. The page is structurally correct, but visually it still reads too much like a long technical document with code blocks and spreadsheet screenshots stacked vertically.

Do not rebuild the underlying system. Redesign the presentation so the page feels like a **real trading-operations workflow** with technical evidence, not a code dump.

Use the shared site design system from the homepage redesign:
- dark navy base
- off-white text
- muted blue accent
- restrained red accent
- Space Grotesk / General Sans style display type
- Inter body text
- consistent buttons, borders, spacing and image radius

Do not make it look like a separate microsite.

## Core visual story

The page should communicate this sequence immediately:

Trade Intake -> Validation / Event Log -> Quote Routing -> Scheduled Refresh -> Portfolio State -> Public Reporting

The viewer should understand in seconds that I built the automation layer joining:
- Google Forms / Sheets
- Apps Script
- multiple quote sources
- scheduled execution
- portfolio state / P&L
- public website reporting

## 1. Hero

Title:
LTG Trading & Reporting System

Description:
Built the workflow connecting trade intake, validation, quote routing, portfolio state and public reporting for Laurier Trading Group.

Tech boxes:
- Google Forms
- Google Sheets
- Apps Script
- Yahoo Finance
- Stooq
- Squarespace

Do not show a long technology sentence.

Use the **LTG allocation pie chart** as a low-opacity glassy hero background motif.

The chart should be recognizable but subtle.

## 2. Pricing adapters

Keep the provider logos. They are important visual evidence.

Show:
- Yahoo Finance
- Stooq
- Twelve Data
- MarketData.app
- Manual marks

Under each logo, use only one factual line:

Yahoo Finance
Equities / FX

Stooq
Fallback quotes

Twelve Data
Quote adapter

MarketData.app
Options quotes

Manual marks
Bond / override prices

No extra AI-style captions.

Do not use words like:
- robust
- seamless
- flexible
- reliable
- broad coverage
- intelligent
- dynamic

## 3. Replace the current long vertical code-document feel

The current page has too much code occupying full-width blocks.

Change the evidence layout so each stage has:
- one concise heading
- one sentence
- one visual
- optional small code crop if needed

Use a more editorial alternating layout.

Recommended desktop rhythm:

LEFT text / RIGHT evidence
then
RIGHT text / LEFT evidence

Do not stack six identical full-width sections.

## 4. Trade Intake

Heading:
Trade Intake

Caption:
Capture instrument, direction, entry, stop and portfolio fields in one structured record.

Visual:
Use the current trade-intake sheet screenshot.

Crop tightly around the useful columns.

Do not show empty sheet area.

## 5. Event Engine

Heading:
Validation and Event Log

Caption:
Normalize requests, validate portfolio constraints, and append accepted or rejected lifecycle events.

Visual:
Use one short Apps Script crop only.

Show only the lines covering:
- normalized action/source/side/portfolio
- validation
- accepted / rejected status
- append

Do not show more than roughly 18 to 22 lines.

Highlight 2 to 4 key lines subtly.

## 6. Quote Routing

Heading:
Quote Routing

Caption:
Resolve each instrument to its mapped provider, try fallback symbols, and use manual marks where required.

Visual:
Use one short Apps Script crop only.

Show only:
- provider list
- mapped provider symbol
- provider request
- fallback / no-response
- successful price return

Do not repeat the provider-logo strip here if it is already visible above.

## 7. Scheduled Refresh

Heading:
Scheduled Refresh

Caption:
Time-driven Apps Script runs refresh the reporting state and leave an execution history.

Visual:
Use the execution-history table.

Make the table large enough to read:
- date
- duration
- Completed status

Do not include code in this section.

## 8. Portfolio State

Heading:
Portfolio State

Caption:
Rebuild holdings from accepted events, determine notional from allocation, and calculate trade-level P&L from current marks.

Visual:
Use a split view:
- left: short calculation-code crop
- right: resulting holdings/state table

Keep code to the smallest useful crop.

The output table should be visually as important as the code.

## 9. Public Reporting

This is the strongest section and should be the visual payoff.

Heading:
Public Reporting

Caption:
Publish trade status and instrument allocation through embedded views on the LTG website.

Show:
1. Trade Logs screenshot
2. Instrument Allocation pie-chart screenshot

For the first screenshot, keep browser chrome / URL visible once:
lauriertradinggroup.ca/simulation

For the second screenshot, crop more tightly around the chart.

Make these screenshots substantially larger than the code screenshots.

The viewer should feel:
"all of the preceding machinery produces this."

## 10. Page background / identity

Use the LTG allocation pie chart as a subtle glassy background motif in the hero and selected transition areas.

On hover / scroll, it may become slightly clearer, but do not animate continuously.

Respect reduced-motion settings.

## 11. Visual cleanup

Apply these exact rules:

- darken the page to match the homepage design system
- remove the current stark white-document feel
- keep code syntax readable
- use more whitespace between stages
- do not use giant code blocks
- do not use tiny AI-style uppercase section labels
- do not use section numbers
- remove redundant right-aligned helper copy
- use one CTA style consistently
- increase caption text so it is comfortably readable
- keep provider logos crisp
- keep public-reporting screenshots large
- no em dashes

## 12. Copy cleanup

Use literal language only.

Preferred nouns:
- trade intake
- validation
- event log
- quote routing
- mapped provider
- fallback symbol
- manual mark
- scheduled refresh
- execution history
- portfolio state
- trade-level P&L
- public reporting

Avoid:
- robust
- scalable
- sophisticated
- dynamic
- seamless
- optimized
- intelligent
- comprehensive
- end-to-end

## 13. Final hierarchy

The page should read visually as:

Hero
Pricing adapters
Trade Intake
Validation and Event Log
Quote Routing
Scheduled Refresh
Portfolio State
Public Reporting

The public-reporting section should be the largest visual section.

## 14. Final output

Return:
1. full-page desktop screenshot
2. mobile screenshot
3. exact visible copy
4. confirmation that:
   - provider logos remain
   - old AI-style provider captions are gone
   - code excerpts are materially shorter
   - public reporting is the visual payoff
   - LTG pie-chart background motif is used
   - shared homepage color / typography system is applied
   - no em dashes remain

Do not make unrelated changes.
