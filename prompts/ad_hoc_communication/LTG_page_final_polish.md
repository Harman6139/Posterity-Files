# Codex prompt - LTG page final polish

You are editing the current **LTG Trading & Reporting System** page only.

The page is already structurally good. Do not redesign it. This is a final surgical pass focused on specificity, readability, visual balance, and removing the last generic or AI-sounding labels.

## Goal

The page should read like a real operating workflow:

trade intake -> validation and event logging -> quote routing -> scheduled refresh -> portfolio state -> public website reporting

The viewer should immediately understand that this is more than a spreadsheet. It is a workflow built across Google Forms, Google Sheets, Apps Script, quote-source adapters, scheduled execution and website reporting.

Do not add new sections. Do not change the overall light visual design.

## 1. Hero section

Keep the title:

LTG Trading & Reporting System

Use this description:

Built the workflow connecting trade intake, validation, quote routing, portfolio state and public reporting for Laurier Trading Group.

Keep the technology line, but make it clean and literal:

Google Forms · Google Sheets · Apps Script / JavaScript · Yahoo Finance · Stooq · Squarespace

Use this workflow line:

Trade Intake -> Validation & Event Log -> Quote Routing -> Portfolio State -> Web Reporting

Do not use em dashes.

## 2. Pricing adapters

Keep the provider logos / brand assets. They are visually useful and should remain prominent.

Section heading:

Pricing adapters

Use these exact short labels under the providers:

Yahoo Finance
Quote feed

Stooq
Fallback quote feed

Twelve Data
Quote adapter

MarketData.app
Options quote adapter

Manual marks
Bond and override prices

Do not use promotional microcopy.

Remove phrases such as:
- broad coverage
- reliable fallback
- flexible pricing
- institutional grade
- fast quotes
- seamless coverage
- robust fallback

Keep logos visually aligned and make sure none of the provider names or captions feel like SaaS marketing.

If the current page shows multiple lines under each logo, reduce them to the provider name plus the one short label above.

## 3. Trade Intake

Heading:

Trade Intake

Caption:

Capture instrument, direction, entry, stop and portfolio fields in one structured record.

Keep the current intake-sheet screenshot.

If needed, crop the screenshot slightly tighter so the fields are readable at normal browser scale.

Do not add extra helper text.

## 4. Event Engine

Heading:

Event Engine

Caption:

Normalize requests, validate portfolio constraints, and append accepted or rejected lifecycle events.

Keep one concise code excerpt only.

The visible code crop should focus on:
- normalized action / source / side / portfolio / entry price
- validation result
- accepted / rejected status
- event append

Do not show unrelated surrounding code.

Try to reduce the visible excerpt to roughly 18 to 24 lines if possible.

## 5. Quote Routing

Heading:

Quote Routing

Caption:

Resolve each instrument to its mapped provider, try fallback symbols, and use manual marks where required.

Keep one concise code excerpt only.

The visible crop should focus on:
- provider list
- mapped provider symbol
- provider request
- fallback / no-response handling
- successful price return

Do not repeat the pricing-adapter logos inside this section if they are already visible directly above. The provider strip at the top is enough.

Keep this code crop roughly 18 to 24 lines if possible.

## 6. Scheduled Refresh

Heading:

Scheduled Refresh

Caption:

Time-driven Apps Script runs refresh the reporting state and leave an execution history.

Use the execution-history screenshot as the main evidence.

Remove the current right-aligned helper sentence if it simply repeats the caption.

Make the execution-history table slightly larger if needed so the dates, duration and Completed status are readable.

Do not add a code excerpt here unless absolutely necessary.

## 7. Portfolio State

Heading:

Portfolio State

Caption:

Rebuild holdings from accepted events, determine notional from allocation, and calculate trade-level P&L from current marks.

Keep:
- one short code excerpt
- the resulting holdings/state table beneath it

The code crop should focus on:
- rebuilding state from events
- portfolio capital / notional logic
- P&L calculation

Remove unrelated lines.

The holdings table should remain visible because it proves the code produces a portfolio state.

## 8. Public Reporting

Heading:

Public Reporting

Caption:

Publish trade status and instrument allocation through embedded views on the LTG website.

Keep the live website screenshots large.

Use the browser chrome / visible URL once to prove the output is live.

Recommended presentation:
- first screenshot: keep browser chrome and visible lauriertradinggroup.ca/simulation URL
- second allocation screenshot: crop more tightly around the allocation chart so the page does not repeat unnecessary browser chrome twice

Keep the small source line:

lauriertradinggroup.ca/simulation

Do not add promotional text around it.

## 9. Visual cleanup

Do a pixel-level polish pass without changing the overall design.

Specifically:
- increase small captions by about 1 to 2px if they are hard to read
- darken body/caption text slightly where it is too faint
- keep the provider logos large enough to register immediately
- keep code subordinate to screenshots and outputs
- keep consistent vertical spacing between sections
- remove redundant right-aligned helper copy
- avoid excessive blank space inside code blocks
- crop screenshots tightly enough that the evidence is readable
- do not add cards, pills, badges or decorative labels
- do not add section numbers

The strongest visual should remain the Public Reporting section.

## 10. Language cleanup

Perform a final line-by-line visible-text pass.

Remove:
- em dashes
- generic AI phrasing
- redundant descriptions
- marketing copy
- vague terms such as multi-source pricing when a more literal term works

Prefer these exact nouns:
- trade intake
- event log
- validation
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
- seamless
- robust
- scalable
- dynamic
- flexible
- intelligent
- sophisticated
- high-performance
- comprehensive

## 11. Final output

Return:
1. a full-page screenshot of the revised LTG page
2. the exact visible copy used for:
   - hero description
   - pricing adapters
   - Trade Intake
   - Event Engine
   - Quote Routing
   - Scheduled Refresh
   - Portfolio State
   - Public Reporting
3. confirmation that:
   - provider logos remain visible
   - old AI-style provider captions are gone
   - browser chrome / URL is shown only where useful
   - code excerpts were tightened
   - no em dashes remain
   - no unrelated redesign changes were made

Do not make unrelated changes.
