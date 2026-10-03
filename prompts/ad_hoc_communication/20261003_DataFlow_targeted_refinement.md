# DataFlow: image framing, request scope and final copy cleanup

## Scope and precedence

Edit the DataFlow project detail page in the selected-work website. Preserve its approved white editorial shell and the working product screenshots. This is a narrow correction pass, not a new DataFlow application or backend refactor. This specification supersedes conflicting older DataFlow page instructions.

The supplied view is generally clear. Its main problems are text trapped inside screenshot frames, repeated image instructions, an unexplained technology ribbon, missing product scope, and a few remaining marketing phrases inside the Docs screenshot.

Read the current site page and active DataFlow source before editing. Do not assume that older marketing copy describes supported capabilities.

## Shared style across all four project agents

- Inherit the homepage serif headings and sans-serif body. Keep a warm-white background with dark navy text and quiet blue links.
- Use existing shared tokens. Fallback only: #FAFAF7 page, #FFFFFF image surfaces, #14273D text, #566170 secondary text, #DEE3E9 rules, #2F5FB3 links.
- Body around 16px, captions 15px, tool explanations 14px. Check actual browser rendering, not the scale of the supplied long screenshot.
- Replace dot-separated keyword strings with a compact three-column definition list under the introduction. Each column has a functional label and a short sentence naming the tool's job. No tool-card grid, dot separators, slash lists or badge wall. Stack on mobile.
- Descriptions state what the software does in the present tense. Do not write instructions to the reader.
- Remove em dashes, slogans, tiny numbered eyebrows, internal QA commentary and visible instructions for opening or manipulating images.
- Keep accessible image enlargement, focus indication and Escape-to-close. These behaviors do not need repetitive text on the page.
- Scope changes to this detail page and required presentation assets. Coordinate shared component edits with the integration agent.

## 1. Project identity

Title:
DataFlow

Small context:
Historical market data

Use this hero description:

DataFlow takes a market-data request from the form to a downloadable CSV. The backend queues the work and retrieves the requested bars.

Do not add a slogan or a sentence saying 'Built a queued workflow...' just to restate the title.

Keep the real homepage screenshot to the right. Use the cleaned current version, not a mock dashboard or an old screenshot with unsupported institutional testimonials.

### Replace the current tools ribbon with these exact columns

Interface
Next.js and TypeScript handle the request form.

Queue
Node.js and Express track requests in SQLite.

Retrieval
A node-cron job fetches market bars from Polygon.

No second technology list is necessary. These name the technologies and explain why they appear.

## 2. Add the product's scope without making up capabilities

Add a compact native 'Request scope' band immediately below the introduction/tools. Put this on the detail page, not another long homepage-card paragraph.

The current repository's active homepage FAQ states stocks and ETFs, intervals from 1 minute to 1 day, up to 2 years per ticker, up to 3 tickers in the public form, and CSV downloads. Specifically inspect:
- frontend/components/homepage-faq.tsx
- frontend/components/enhanced-docs-tab.tsx
- the active request form and interval validation
- services/dataProcessor.js
- routes/download.js

Use these exact visible entries if they still match the active implementation:

Assets
Stocks and ETFs

Intervals
1 minute to 1 day

History per request
Up to 2 years

Batch size
Up to 3 tickers

One short line underneath:
Exports contain timestamped price and volume bars. Available history depends on the symbol and provider.

Keep this as a simple definition list or a two-by-two facts layout, not four statistic cards. It communicates configured scope, not claimed customer adoption or live processing speed.

Do not restore stocks/crypto/FX/option-chain claims from old drafts. Do not add '50,000+', 'unlimited', 'real time', 'tick data' or JSON simply because they appeared in former UI copy. Extend the list only if current retrieval code and actual supported examples establish the additional coverage. A dropdown or provider catalogue alone is not proof of working coverage.

## 3. Correct every image frame

The current hero image has 'The live application's request entry point' and 'Select image to expand' inside its border. Similar caption strips occur under the request, queue, Docs, CSV and completion images.

Use this single rule throughout:

The image frame contains only the image. Its explanation lives in the adjacent process text.

Implementation requirements:
- Remove visible 'Select image to expand', 'Read output values' when it merely exposes duplicate text, 'The live application's request entry point', and other redundant screenshot instructions.
- Remove redundant figcaptions that repeat the adjacent paragraph.
- Keep necessary output metadata once, such as the sample's actual date range and selected-column label. Do not repeat it in three places or erase information that changes what the example means.
- Use semantic figure elements, but do not place figure captions inside the border applied to the image.
- Keep aspect ratios and full UI components intact. No cover cropping of request parameters or completion status.
- Give all UI screenshots a consistent width, subtle neutral border and small radius. Preserve their native purple/navy design; do not tint the screenshot to match the white site.
- Use new high-resolution browser captures when available. Do not regenerate the interface or invent a success state.
- Put a single working product link near the hero and at the end: 'Open DataFlow'.

The cleaned UI, actual output and adjacent explanation are sufficient. No visible provenance essay is required.

## 4. Keep the sequential five-step structure

Remove the tiny '01', '02' chapter markers. Use normal section headings and subtle connections or arrows only where helpful. Do not use a second decorative ribbon that duplicates the whole explanation.

The following copy is deliberately short and in the present tense. Preserve any equally clear existing sentence, but remove duplicates.

### Choose the request

The form collects the symbols, dates and interval. The review screen shows those choices before the request enters the queue.

Visual: real Review & Submit screen. Use a capture with parameters that match the output example wherever possible.

### Wait for processing

The API stores the request in SQLite. A background worker picks up queued jobs, while the page checks their status.

One essential clarification, once only:
The percentage is a time estimate. Completion comes from the backend.

Visual: current Processing Estimate view. Do not display an animated percentage as measured row-level progress.

### Retrieve the bars

The worker divides each ticker request into date ranges. It fetches those batches from Polygon before passing the bars to the formatter.

Visual: the cleaned existing Docs pipeline or a small native diagram of the actual sequence. Prefer this to a large code screenshot.

### Prepare the CSV

The formatter removes duplicate timestamps and sorts the returned bars. It then writes the CSV columns and request metadata.

Visual: actual downloaded sample, displayed as a readable native table or a crisp capture. Keep the original values unchanged. Label selected columns as selected columns. Do not claim exhaustive price/volume quality validation unless the implementation has it.

### Download the result

Once processing finishes, the page provides the CSV download. Multi-ticker requests can return individual files or a ZIP bundle.

Visual: genuine Request Complete screen and a working download link to the associated permitted output. Only mention the ZIP path if it remains supported in routes/download.js.

## 5. Remove remaining AI-style text inside the Docs visual

The currently captured Docs section includes 'Dynamic Token Pooling', 'Multiple API keys for reliability and speed', 'Auto-Batching into Chunks', and 'Intelligent data grouping for efficiency'. These should not survive merely because they are inside an image.

Do not edit screenshot pixels to fake a revised application. Either change the relevant Docs copy in a narrowly scoped presentation branch and recapture it, or replace that image on the portfolio page with a plainly labelled native diagram of the implemented workflow. Do not alter backend behavior.

Use these exact Docs labels if updating the actual Docs component:

Provider keys
Uses the configured API credentials.

Ticker requests
Processes ticker tasks concurrently.

Date batches
Splits each ticker's history into date ranges.

CSV export
Sorts the returned bars and writes the file.

Do not call asynchronous Promise-based requests 'multithreading'. Do not imply token rotation bypasses provider limits. Keep the visible technical names tied to actual behavior.

Crop the Docs screenshot to the relevant pipeline after recapture. The unrelated 'Integration Examples' title currently visible below it need not appear in this figure.

## 6. Output example and link hygiene

The supplied screenshot shows a dated AAPL CSV example. Keep it as that example, not a claim about every dataset. If five daily rows are shown, do not turn them into a scale metric.

Maintain a clear title such as:
AAPL daily CSV sample

Put its date range directly below the title, once. Keep the actual UTC timestamps or the clearly documented displayed time zone. Do not change dates, values or row counts for presentation.

A functional download can be labelled 'Download sample CSV'. Remove self-congratulatory words such as 'verified' from the link label; retain verification records privately. Do not upload licensed raw files beyond the approved sample.

Final product link:
Open DataFlow

Delete 'Explore the request-to-download workflow'. The reader has just seen it.

## 7. Final check

Check desktop and mobile for image captions attached to borders, unreadable table columns, disconnected navigation and repeated explanations. All rendered tool names must have a purpose-labelled home. No standalone keyword soup remains.

Return revised screenshots, final scope wording, changed files, and any actual scope discrepancy found in source. Keep internal checks out of the public page. Do not claim the live pipeline was retested if this was only a presentation edit.