# LTG: plain process copy and final visual corrections

## Scope and precedence

Edit the existing LTG detail page and its necessary presentation assets. Keep the approved white editorial site style, LTG identity and existing working evidence. This specification supersedes conflicting older LTG names and captions. Do not rebuild the trading system, change real trade records, or redesign the entire site.

The current page has useful evidence but often reads like instructions to a programmer: 'Rebuild holdings...', 'Publish trade status...', and abstract lists of system components. Replace that language with a clear account of what a club portfolio manager does and what the software does next.

All QA and implementation instructions below stay in the private handoff, never on the public page.

## Shared visual and language rules

- Reuse the approved homepage serif headings and sans-serif body. Keep the warm-white page, navy text and restrained blue links. LTG gold belongs in the logo and small accents only.
- Reuse existing shared tokens. Fallback only: #FAFAF7 page, #FFFFFF artifact surfaces, #14273D text, #566170 secondary text, #DEE3E9 rules, #2F5FB3 links.
- Body around 16px, captions 15px, tool descriptions 14px. Ensure source images are readable at the actual displayed size.
- Replace dot-separated keyword strips and skill-pill walls with a compact three-column definition list under the introduction. Give each tool group a functional label and one short explanation. No surrounding cards, dot separators or slash lists. Stack the same component on mobile.
- Use present tense and real subjects: 'The form records...', 'Apps Script checks...', 'The website updates...'. Do not write commands such as 'Capture', 'Normalize', 'Rebuild' or 'Publish' as the reader-facing explanation.
- Use short sentences, not long chains of commas. Remove em dashes, slogans, miniature numbered headings, internal notes and repeated image instructions.
- Keep accessible image enlargement, visible focus and Escape-to-close without text telling people how to manipulate the image.
- Do not overwrite other agents' shared files. Scope changes to LTG and report shared-component needs to the integration agent.

## 1. Exact name and introduction

Use this exact project title:
LTG Trade Blotter & Reporting System

Update the detail-page H1, document title, breadcrumb and the title in the shared project registry used by the homepage card. Preserve the route and links. Do not independently rebuild the homepage card.

Small context line:
Laurier Trading Group

Use this hero description:

Club portfolio managers submit trade details through a Google Form. The system checks the entries, refreshes prices and updates the club's online report.

This is an educational club trading workflow, not a broker execution platform. Do not imply that submitting a form executes market trades. Keep any existing short simulation identification where necessary, without turning it into a warning banner.

Keep the LTG logo. Use the allocation chart subtly in the hero, but remove the repeated ghost pie-chart decoration currently appearing again near Portfolio State. The real allocation chart still belongs in the final reporting section.

### Replace the technology ribbon with these three exact columns

Trade entry
Google Forms records requests in Google Sheets.

Automation
Apps Script checks trades and refreshes prices.

Reporting
Squarespace displays the published trade report.

Do not call Google Sheets 'Excel'. Do not repeat all providers in this strip; the provider row below explains them.

## 2. Provider logos, not marketing cards

Keep the genuine Yahoo Finance, Stooq, Twelve Data and MarketData.app logos. Preserve their native colors and proportions. Use manual marks as a text entry or a small neutral editing icon, not a fake brand logo.

Heading:
Price sources

Use one short label per provider:

Yahoo Finance
Mapped market quotes

Stooq
Fallback closing prices

Twelve Data
Additional quote source

MarketData.app
Options quotes

Manual marks
Entered prices and overrides

Treat these as source adapters, not endorsements or a claim that every displayed position uses all feeds. Confirm that the captions match the adapters currently shown in the source. Do not expand provider roles from generic brand capabilities.

Use a single clean aligned row that wraps on mobile. No floating cards, thick borders, extra slogans or tiny tertiary captions. Do not remove the logos again.

## 3. Make the workflow read in order

Keep a compact six-stage anchor line, using the exact stages below. Subtle arrows may connect them, but do not add slash-separated labels, a 'Workflow' banner and another summary sentence that all say the same thing.

Submit trade -> Check request -> Refresh prices -> Daily refresh -> Update positions -> Update website

The following six sections explain that same path. Keep the alternating evidence layout, but ensure the reading order remains unambiguous on desktop and mobile. Arrows belong in the anchor line or the whitespace between stages, not across screenshots.

### Submit a trade

Exact explanation:

A club portfolio manager fills in the Google Form. The response records the instrument and trade details in Google Sheets.

Visual: use the real form if available. Otherwise keep the current intake-sheet capture as the recorded response, not a mock form. Crop to the meaningful columns: instrument, side, entry, stop and status, with the portfolio field where useful. Do not change the underlying values.

No extra caption saying 'structured record' is needed. The visual and explanation establish that.

### Check the request

Exact explanation:

Apps Script checks the required fields and allocation limits. It records whether the trade request was accepted or rejected.

Visual: one short real code excerpt showing validation and accepted/rejected event writes. Prefer 10–16 relevant lines to a long normalized-field list. A small actual audit-log output can be paired with it if that makes the result clearer.

Do not force normalization, validation and two branches into an unreadably small screenshot. If lines are omitted, use an honest gap marker. Do not manufacture a working function from unrelated code fragments.

### Refresh prices

Exact explanation:

The pricing code reads each instrument's provider symbol. It tries the configured quote sources and uses entered marks where required.

Visual: one short provider-selection excerpt with the request and success/fallback condition. Keep original function names and source text. Do not repeat the complete provider-logo row here.

Do not describe a manual price as a quote automatically obtained from another provider. Do not promise that every missing price has a successful fallback.

### Daily refresh

Exact explanation:

A daily Apps Script trigger refreshes prices and reporting data without a manual download. The execution log records the completed runs.

Visual: the actual time-driven execution-history table. Make dates, duration and Completed status legible. No second code screenshot or right-aligned repetition of the same explanation.

Confirm the daily cadence from the configured trigger or source. Do not publish a specific clock time unless it is both useful and verified.

### Update positions

Exact explanation:

Accepted trade actions update the holdings. The calculation then uses position size and current marks to work out trade-level P&L.

Visual: a compact split view with a short calculation excerpt and the resulting holdings table. Give the output at least as much visual weight as the code.

Keep three concepts distinct: position size, price movement and portfolio allocation. Do not label a weighted exposure chart as institutional NAV accounting, and do not claim that a simple price-return calculation handles every asset class correctly. Preserve only the claims supported by the implemented instrument handlers.

### Update the website

Preferred exact explanation:

The website updates after accepted trade actions and the daily refresh. It shows the latest trade status and instrument allocation without a separate website edit.

Before using that sentence, inspect the event-to-report handler and publishing/embedding behavior. The owner describes both event-driven and daily updates, but the wording must match the actual connection. If accepted events become visible only at the next reporting refresh, use this exact alternative instead:

The daily refresh updates the website automatically. Accepted trade actions appear when the published report next refreshes.

Do not say 'instant', 'real-time' or imply a direct website push when it is an embedded view that refreshes on load or polling. Put the accurate behavior in the sentence, not in a long disclaimer.

Visuals: the real public trade log followed by the instrument-allocation chart. This remains the visual payoff of the page.

## 4. Keep code supportive, not dominant

The page should show a human action, an automated check, price retrieval, a scheduled run and the resulting report. It should not become an Apps Script reference manual.

- Maximum three code visuals: validation, quote routing and position calculation.
- Use short focused excerpts, preferably 10–16 lines each; do not compress them to fit an arbitrary line limit.
- Code remains smaller than the public-output section and should occupy clearly less than half the page.
- Do not add more code to demonstrate 'technical depth'. The execution log and final report provide stronger evidence of use.
- Use sparse highlighting around the important real lines, not large blue highlight bands everywhere.
- Retain source authenticity. Redact secrets and unnecessary personal paths; never invent executions, returns or successful events.

## 5. Image framing and final reporting section

Use one image-framing style across this page and the other project pages: natural aspect ratio, fine neutral border, 3–4px radius and no heavy shadow. Explanation stays outside the frame, next to the image. Remove visible 'Click', 'Enlarge', 'Select image' and duplicate caption strips.

For the public trade-log image, preserve the URL or browser identity once if it helps. For the pie chart, crop the duplicated browser/header chrome and use the actual chart at a comfortable width. Do not let the chart become a giant mostly empty square that overwhelms the rest of the workflow.

The public link should be a normal link labelled:
View live report

Destination:
https://www.lauriertradinggroup.ca/simulation

The chart's title and allocation basis must remain accurate. Do not relabel synthetic returns as verified performance. Do not reintroduce the synthetic historical return chart merely to add another visual.

## 6. Final page order

Shared header
LTG logo, exact project title and two-sentence introduction
Purpose-labelled tool context
Price-source logos
Six-stage process navigation
The six process sections
Live-report link
Shared footer

No new testimonials, personal pitch, 'what this proves' paragraph or resume-style conclusion.

## 7. Acceptance and return

Inspect 1440px desktop and 390px mobile. Check that:
- The title is LTG Trade Blotter & Reporting System.
- The opening explains the Google Form to report journey.
- Tools are attached to their purpose, not listed as keywords.
- Provider logos remain with one factual label each.
- All process explanations are present-tense statements, not commands.
- Website-update wording reflects actual event/daily behavior.
- Code is concise and the public report remains the payoff.
- There are no repeated ghost motifs, internal notes, em dashes or image-manipulation instructions.

Return revised screenshots, exact final copy and the changed-file list. Report any factual difference between the preferred update sentence and the actual implementation privately. Do not put the implementation discussion on the public page.