# Codex prompt - Final homepage redesign for Selected Quantitative Systems

You are editing the **homepage only** of the Selected Quantitative Systems site.

The current homepage is too loud, too template-like, and still feels AI-generated. Rebuild it into a **minimal, white, image-led, editorial homepage** with the polish of an Apple product page and the restraint of Citadel's corporate website.

Do not redesign the project detail pages in this task. The detail pages already have their own content and evidence. The homepage should simply present the four projects beautifully and send the viewer into those pages.

## Core design objective

The homepage should feel:
- quiet
- premium
- white-space driven
- editorial
- finance-professional
- human-made
- visually distinctive without being flashy

It should **not** feel:
- like a SaaS landing page
- like a ChatGPT / OpenAI template
- like an AI-generated portfolio
- like a dark cyberpunk site
- like a grid of generic cards
- like a résumé

The visual emphasis should come from the **real project imagery**, not from decorative UI.

---

## 1. Page background and overall tone

Use a light, warm-white page background.

Recommended:
- page background: #F7F7F4 or #FAFAF7
- primary text: deep navy / charcoal, around #0C1B2A
- secondary text: muted slate, around #647080
- borders: very light cool grey, around #D9E0E7
- blue accent: restrained institutional blue, around #2F5FB3
- optional muted red accent: #B84952, used sparingly

Do not use a dark global background.

Do not use large gradients.

Do not use neon.

Do not use obvious BMO branding or colors in a way that looks tailored to BMO. The blue/red accents should simply feel institutional.

---

## 2. Typography

The current typography feels too generic.

Use a distinctive editorial finance pairing.

Preferred:
- display / project titles: **Newsreader** or **Source Serif 4**
- body / navigation / tech labels: **IBM Plex Sans**

If one of those is unavailable, use:
- display: Cormorant Garamond or Libre Baskerville
- body: IBM Plex Sans

Do not use Inter as the dominant typeface on the homepage.

Do not use oversized OpenAI-style headings.

Recommended sizes:
- site name / hero title: 56-68px desktop
- hero subtitle: 18-20px
- card title: 30-38px
- card description: 15-17px
- small context label: 12-13px
- tech labels: 11-12px

Use tighter line-height on titles.

Use restrained letter-spacing.

---

## 3. Header

Remove the current top-left website logo/icon entirely.

Header should be minimal.

Left:
**Harman Singh**

Right:
- Projects
- About
- Contact

Make Harman Singh visually stronger than the nav:
- bold or semibold
- around 18-20px

No internal status text.

No “integration draft”.

No extra site-brand logo.

---

## 4. Hero

Keep the hero compact and editorial.

Use:

**Selected Quantitative Systems**

Subtitle:
**Research systems, trading infrastructure, scenario engines and market-data workflows.**

Do not add slogans.

Do not add fake-profound lines.

Do not add a quote.

Do not add category lists like "Research / Markets / Systems" unless extremely subtle and genuinely useful.

The hero should end quickly and move into the projects.

---

## 5. Main project layout

Use a **2 x 2 grid** on desktop.

Each project should be a **large image-led card**.

The cards should not look like generic cards sitting on a page. Think more like editorial project covers.

### Card structure

Each card should have:
- large project image occupying most of the card
- subtle white / frosted text panel integrated over the image or across the bottom
- project name
- very short context line where needed
- 10-15 word description maximum
- 4-5 genuine tech labels
- small arrow CTA

No long workflow line.

No project numbers.

No category numbers.

No long body copy.

No giant blank rectangles.

---

## 6. Card image behavior

The project image is the main visual element.

At rest:
- image is slightly softened / darkened / low-contrast behind the text
- text remains fully legible
- image still clearly identifies the project

On hover:
- image should gently sharpen
- background image may scale 1.015-1.03 or shift a few pixels
- allow a subtle parallax / background-position movement
- text panel can become slightly clearer or more opaque
- border can pick up a subtle institutional-blue highlight

Animation should feel Apple-like:
- slow
- smooth
- subtle
- no bouncing
- no glowing neon
- no constant motion

Respect reduced-motion preferences.

---

## 7. Project card 1 - Mathematical Finance manuscript

This project name must be exact.

### Main title
**Portfolio Choice under Spectral Covariance Ambiguity**

### Small sublabel
**Submission to Mathematical Finance**

Do not use "Portfolio Research Infrastructure" as the homepage project name.

### Description
**Point-in-time WRDS/CRSP portfolio research with remote compute and realized-risk evaluation.**

### Tech labels
- Python
- WRDS
- CRSP CIZ
- SSH
- CPU26

### Background image
Use the **first page / title section of the actual manuscript**.

The manuscript title and author name should be visually recognizable in the image.

Use it as:
- a large card background
- slightly angled or cropped if tasteful
- low-opacity under the text panel
- clearer on hover

Do not use a generic architecture diagram as the homepage thumbnail.

### CTA
**Open project**

---

## 8. Project card 2 - Laurier Trading Group

Use the real LTG visual identity.

### Main title
**LTG Trading & Reporting System**

### Small visual identity
Show the **LTG logo** clearly in or near the card header.

### Description
**Trade intake, quote routing, portfolio state and live reporting for Laurier Trading Group.**

### Tech labels
- Google Forms
- Google Sheets
- Apps Script
- Yahoo Finance
- Stooq

### Background image
Use the **instrument allocation pie-chart screenshot** as the main background image.

The LTG logo and allocation chart should make the card immediately recognizable.

Do not use code as the homepage thumbnail.

Do not use a spreadsheet as the primary homepage visual.

### CTA
**Open project**

---

## 9. Project card 3 - Citadel

Use the project name exactly.

### Main title
**Citadel FI&M Central Bank Challenge**

Do not use "Policy-Path Scenario Engine" as the main homepage card title.

### Optional small sublabel
**Policy-Path Scenario Engine**

Use this only as secondary context, not the main project name.

### Description
**Semi-structural model for comparing feasible Fed paths across macro scenarios.**

### Tech labels
- Python
- ARDL
- BVARX
- Scenario scoring

### Background image
Use **slide 2 from the Citadel presentation** as the main card image.

Also show the **Citadel logo** clearly.

The slide should remain recognizable.

Do not invent new visuals.

Do not use a generic chart.

### CTA
**Open project**

---

## 10. Project card 4 - DataFlow

The project name should be exactly:

### Main title
**DataFlow**

### Small sublabel
**Market Data Infrastructure**

### Description
**Queued market-data retrieval, batch processing and downloadable time-series outputs.**

### Tech labels
- Next.js
- TypeScript
- Node.js
- SQLite
- Polygon

### Background image
Use the **actual DataFlow homepage / hero screen** as the full card background.

This should feel like a real product screenshot.

Do not use a generic workflow diagram.

Do not use placeholder server imagery.

### CTA
**Open project**

---

## 11. Card text treatment

The image and text must remain visually distinct.

Recommended treatment:
- frosted white panel across the lower 32-40% of the card
- backdrop blur around 12-20px
- white at approximately 84-92% opacity
- dark navy text
- tech labels in small, low-contrast outlined pills or tiny text boxes

Do not make the panel too opaque.

Do not make the image unreadable.

Do not overlay white text directly on a busy image unless the contrast is excellent.

---

## 12. Card dimensions and spacing

Desktop:
- two equal-width columns
- card aspect around 4:3 or 5:4
- generous 24-32px gap
- cards should feel large enough for imagery to breathe

Mobile:
- stack cards
- image remains prominent
- text panel remains readable
- tech labels wrap naturally

No horizontal scroll.

---

## 13. Footer

Minimal only.

Left:
**Harman Singh**

Right:
**Quantitative research, markets and systems**

No giant footer.

No duplicate navigation unless necessary.

---

## 14. Remove AI-template cues

Remove all of these from the homepage:
- project numbers
- tiny uppercase numbered labels
- workflow arrows
- buzzword-heavy sentences
- decorative micro-metrics
- giant dark panels
- generic generated architecture thumbnails
- em dashes
- "View workflow"
- "View system"
- "View model"

Use one CTA consistently:
**Open project**

Do not use:
- robust
- scalable
- sophisticated
- seamless
- powerful
- cutting-edge
- comprehensive
- innovative
- high-performance

---

## 15. Human-made visual details

Add small imperfections / editorial details that make the page feel designed by a person:
- slightly different image crops per project
- varied but aligned card focal points
- subtle serif / sans contrast
- fine 1px rules
- restrained image grain if tasteful
- small custom arrow icon rather than generic UI button
- non-uniform but balanced whitespace

Do not randomize layout.

Keep it clean.

---

## 16. Final output

Return:
1. desktop full-page screenshot
2. mobile screenshot
3. exact homepage copy
4. exact font families
5. exact color palette
6. confirmation that:
   - background is white / warm-white
   - top-left logo is removed
   - no integration-draft text remains
   - Harman Singh is prominent in header
   - QF card uses the exact manuscript title
   - QF card says Submission to Mathematical Finance
   - QF uses manuscript first page as image
   - LTG card uses LTG logo and allocation pie chart
   - Citadel card main title is Citadel FI&M Central Bank Challenge
   - Citadel card uses slide 2 and Citadel logo
   - DataFlow card main title is DataFlow
   - DataFlow uses the actual homepage / hero screen
   - all four cards have subtle image motion on hover
   - no em dashes remain
   - no generic AI / OpenAI-like homepage typography remains

Do not change the project detail-page copy in this task.
