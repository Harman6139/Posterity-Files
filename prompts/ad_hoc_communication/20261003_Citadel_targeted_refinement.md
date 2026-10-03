# Citadel: targeted presentation corrections

## Scope and precedence

Edit the existing Citadel detail page, not the underlying research or the whole website. This specification supersedes conflicting older Citadel copy and styling instructions. Keep the approved white editorial homepage style. Read the current page source and inspect the original presentation before editing. Do not restart the audit or propose another design.

The supplied desktop view shows four particular problems: an unexplained dot-separated technology list, tiny A/B/C markers with decorative overlines, low-resolution slide captures, and slide frames that look pasted onto the page. Correct those problems while retaining the result-first structure.

All instructions and acceptance checks below are for the developer. None belongs on the public page.

## Shared presentation rules for all four project agents

- Reuse the homepage's approved serif heading font and sans-serif body font. Do not introduce another font family.
- Keep a warm-white page, dark navy text and restrained blue links. Reuse existing shared tokens. Suggested fallback values only if tokens are absent: page #FAFAF7, artifact surface #FFFFFF, text #14273D, secondary text #566170, rules #DEE3E9, accent #2F5FB3.
- Desktop body text 16px, captions 15px, tool descriptions 14px, section headings 26–30px. Keep text readable at 100% browser zoom. Do not infer CSS sizes from a downscaled full-page screenshot.
- Replace the keyword ribbon and repeated skill badges with a compact three-column definition list beneath the introduction. Each column has a functional label and one short explanation naming the tools. No enclosing cards, logos, bullets, middle-dot separators, slash lists or monospace styling. Use the same arrangement on all four detail pages; stack it on mobile.
- Write statements about what the system does, not commands to the reader. Prefer two short sentences over one chain of clauses.
- Remove em dashes, fake slogans, repeated micro-headings, implementation notes, QA badges, file paths, and phrases such as 'click to enlarge' or 'select image to expand'. Preserve keyboard-accessible image enlargement without visible instructions.
- Do not remove qualifiers that are necessary to understand an actual result. Do not put an internal audit report on the public page either.
- Work only on this page and its assets. Coordinate any shared-component change with the integration agent; do not overwrite another page agent's work.

## 1. Header and introduction

Keep the shared header with Harman Singh and working navigation. Remove any old HS icon, build banner or duplicate site identity.

Keep the detail-page heading:

Policy-Path Scenario Engine

The project context immediately above it is:

Citadel FI&M Central Bank Challenge

Use this introduction:

The model compares possible Fed decisions under the same forecasts and stress scenarios.

Do not add a second tagline or a keyword row.

### Replace the technology ribbon with these three purpose-labelled columns

Inputs
Bloomberg exports and public macro data supply the starting assumptions.

Model
Python estimates how policy changes affect financial conditions.

Comparison
A BVARX model checks the baseline transmission specification.

ARDL and the use of economic priors belong in the relevant process section below, not in an unexplained skill list. Do not imply a live Bloomberg API, automatic ingestion of every workbook, or three equally empirical transmission blocks.

## 2. Citadel logo

Use an existing proper transparent SVG or transparent PNG for the standalone logo. Preserve the original navy wordmark at full opacity on the white page. 'Transparent' means a transparent background, not a barely visible logo.

Do not use a white screenshot rectangle around the standalone logo. Do not redraw or generate an imitation. If extracting from a supplied asset, remove only the uniform background and preserve antialiasing. If the only clean source is inside the PDF, export that vector asset. Keep logos within historical slide images unchanged.

Show the small standalone logo once near the project context. No repeated decorative Citadel watermarks behind body text. Its presence identifies competition context, not employment or endorsement.

## 3. Replace low-resolution captures with original slide exports

Use the original presentation or PDF as the source. Do not enlarge a screenshot of the browser or upscale the current low-resolution images and call that a fix.

- Locate the slides by their titles: Model Result, Overview & Block A, Overview & Block B, Overview & Block C, and Presentation Agenda / Team 5.
- Slide 2 is the agenda/team slide. It is not the Model Result slide. Preserve that distinction.
- Export each relevant slide directly at its original aspect ratio. Supply at least twice the maximum CSS display width: for a 1120px display, export at least 2240px wide; approximately 2800–3200px is preferable for dense text when file size permits.
- Prefer vector output with embedded/outlined fonts when dependable. Otherwise use crisp PNG or lossless WebP, not a heavily compressed JPEG.
- Set intrinsic width and height, responsive srcset where appropriate, display:block, width:100%, height:auto. Use contain rather than cover for complete slides.
- Check top headings, footnotes, chart axes and both outer edges. Nothing substantive may be clipped. Remove browser chrome and accidental external whitespace only.
- Keep the original slide colors and fonts. Do not recolor the source slides to match the site, fade them, blur them, or apply dark-mode filters.

### Integration with the page aesthetic

Treat each slide as a white document plate, not as a screenshot card. Put it on a true-white surface with a very fine neutral border and no prominent shadow. Use square or 3–4px corners. Give it consistent internal framing and align it with the text column.

The site heading and explanation should sit outside the plate. No caption strip inside the image border. Avoid a stack of nested cards. This lets the white Citadel slides fit the warm-white site without altering the evidence.

Keep enlargement on image activation. Use an accessible button/link with an accurate aria-label, visible focus and Escape-to-close. No repeated instructional microcopy.

If originals genuinely cannot be located, use the highest-resolution supplied slide and report the missing source privately. Do not fabricate clearer charts, text or numbers.

## 4. Result-first opening

Keep the Model Result slide first. Keep the three understated statistics directly below it:

365 | Feasible policy paths
17 | Scenarios
6,205 | Path-scenario comparisons

Use these only for the saved run represented by the displayed slide. Do not replace the result, smooth the charts or exaggerate the distance between Hold and Cut.

No 'quantitative model output', 'what this proves', 'evidence', or decorative KPI cards are needed.

Optional one-sentence result caption, only if the slide needs interpretation:

Hold ranks first after the policy-stability penalty.

Do not say Hold minimizes unpenalized economic loss; that is a different score.

## 5. Remove duplicate navigation decoration

Remove the long five-stage arrow ribbon if it duplicates the three model sections. Replace it, if navigation is useful, with ordinary inline links:

Assumptions    Transmission    Ranking

No dot separators, numbered pills or tiny uppercase labels. These links point to the three sections below.

## 6. Replace tiny A/B/C markers

Remove the short decorative line above each letter and the miniature section-marker treatment.

Use a simple two-column section heading: a navy serif A, B or C around 36–42px alongside the normal heading. Align the letter with the heading baseline. No circle, badge, colored box or overline. On mobile the letter sits immediately beside the heading at a smaller size. The letter reflects the actual model block, not an arbitrary UI step number.

### A: Shared assumptions

Exact text:

First, the engine fixes one policy-conditioned baseline across all four sectors. Every candidate path uses the same starting data and shock set.

Visual: the complete Block A slide, freshly exported from the source.

### B: Policy transmission

Exact text:

Each meeting path becomes a day-weighted quarterly policy rate. The model then traces changes from the reference through financial conditions into growth, labour and inflation.

Short method sentence beneath the paragraph, not a badge list:

Financial conditions use ARDL estimates. The later channels use economic priors, with BVARX as a comparison model.

Visual: the complete Block B slide, freshly exported.

Do not describe the theoretical-prior channels as empirically fitted if the saved run used fallbacks. Do not confuse propagation of policy changes with independent raw economic forecasts.

### C: Policy ranking

Exact text:

The model scores the resulting paths against the policy targets. It combines the scenario losses and adds a penalty for policy reversals.

Visual: the complete Block C slide, freshly exported.

Keep all slide content unchanged. These paragraphs orient the visitor; they should not restate every bullet inside the slide.

## 7. Full presentation

Keep the agenda/team slide as a smaller complete thumbnail. Do not crop out team members or replace it with the Model Result slide.

Heading:
Full presentation

Text:
The 15-slide team pitch includes the sector outlooks and policy recommendation.

Links:
View presentation
Open PDF

Use native links, a restrained arrow and the shared button/link style. Verify that they resolve to the intended presentation, not a local path or an owner-only session.

## 8. Final checks and handoff

Inspect at 1440px desktop and 390px mobile. Check full slides at 100% and in the enlargement view. Confirm that the assets are high-resolution enough to read chart labels, not merely that the image request succeeds.

Return the revised page screenshots, the exact replacement copy, the slide-export filenames/dimensions, and the changed-file list. Keep the source-to-export mapping in the handoff only. Do not insert it into the website.

Done means: no keyword ribbon, no tiny overlined letters, transparent standalone logo background, consistently framed full slides, plain sequential explanations, and no unrelated redesign.