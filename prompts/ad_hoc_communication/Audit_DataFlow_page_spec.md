# Audit DataFlow — Detailed Page Specification

## Objective
Refine the **DataFlow** page so it clearly presents the system as a market-data processing platform with a clean request-to-download workflow.

The page should look polished, product-like, and specific without sounding promotional or overclaimed.

This page must match the final homepage design system.

## Project naming
- **Primary title:** `DataFlow`
- **Secondary line (small):** `Market Data Infrastructure`

Do not use a longer artificial product name as the title.

## Design direction
Use a **white editorial background** with restrained blue accents.

This page should feel:
- like a clean product case study
- technical but approachable
- process-first
- quiet and modern

Use real UI screenshots as primary visuals.

Avoid:
- fake startup language
- exaggerated claims
- salesy subscription fluff
- generic AI phrasing

## Hero section
- title left
- small secondary line
- short description
- one clean product screenshot

Hero summary:
> Built a queued workflow for market-data requests that batches retrieval, processes time-series outputs and returns downloadable files.

Tech line:
- Next.js
- TypeScript
- Node.js
- Express
- SQLite
- node-cron
- Polygon

## Core workflow line
- `Request`
- `Queue`
- `Batch`
- `Retrieve`
- `Process`
- `Download`

## Main content structure
Use 5–6 sections at most, each with image plus brief copy.

### Request intake
Explain that users specify ticker, date range, interval and output format.
Show request UI.

### Queue management
Explain that requests are written to a queue, tracked in SQLite, and managed through status transitions.
Show queue/status evidence if available.

### Batched retrieval
Explain that the system groups or schedules data retrieval instead of making wasteful one-off calls.
Show workflow diagram or docs screenshot if stronger than raw code.

### Processing layer
Explain that retrieved data is normalized, checked and converted into the requested output form.

### Downloadable output
Explain that completed runs return structured downloadable outputs such as CSV or JSON.
Show end-state UI if available.

### System notes (optional)
Only if useful, include compact scheduling/backend orchestration detail.

## Copy style rules
- keep copy concrete
- remove BMO-adjacent or role-targeted language
- no startup LARP tone
- no empty phrases like “revolutionizing data access”
- captions say exactly what screenshot shows

Good caption style:
- `Specify ticker, date range, interval and output format before queuing the request.`
- `Requests are stored in SQLite and processed through explicit status stages.`
- `The retrieval layer batches API work before processing and export.`
- `Completed runs return structured downloadable outputs.`

## CTA / finish
At bottom, small CTA area can include:
- `View system`
- optional docs or GitHub link if already part of page

Keep it quiet.

## Output expectation
Return a page that feels product-like, precise, calm, visually consistent with homepage, and clearly human-made rather than AI-generated.