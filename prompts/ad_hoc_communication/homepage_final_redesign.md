# Homepage final redesign + cross-page design system

You are editing the current **Selected Quantitative Systems** website.

This is a deliberate visual redesign of the homepage plus a shared design-system pass across the QF, LTG, Citadel and DataFlow project pages.

Do not treat this as a generic template cleanup. The goal is to make the site feel **authored, editorial, specific and human-made**, while remaining clean and professional.

## Core objective

The homepage should feel like a curated selection of serious quantitative systems work, not an AI-generated portfolio grid.

It should:
- look more designed and authored
- remove obvious AI cues
- use a clear, distinctive color system
- use stronger typography
- make each project card feel like a visual object
- use project-specific backgrounds and identity
- feel consistent with the underlying projects

---

## 1. Global design system across homepage and all project pages

### Typography

The current site is too close to the generic ChatGPT / OpenAI showcase style.

Replace the current typographic feel with something more editorial and human-made.

Preferred:
- Display / hero headings: Space Grotesk, Satoshi, or General Sans
- Body text: Inter
- Small labels / metadata / tech: Inter with tighter tracking

Fallback if needed:
- General Sans / Inter only

Rules:
- reduce the generic AI-site feeling from oversized ultra-clean headings
- keep hero headings assertive but more compact
- make project names strong and readable
- keep metadata smaller and quieter
- avoid excessive tiny uppercase labels
- avoid large ChatGPT-like line-height and card spacing

Suggested sizes:
- homepage hero: 54-62px desktop
- homepage subtitle: 18-20px
- project card titles: 28-34px
- project descriptions: 15-17px
- tech boxes: 12-13px
- page section headings: 28-34px
- detail-page body: 16-17px

### Color system

Standardize the entire site with one consistent palette.

Base:
- Background: #07111F
- Secondary background / panels: #0E1A2B
- Primary text: #F4F6F8
- Secondary text: #A8B3C2
- Border: rgba(140, 170, 210, 0.16)

Accents:
- Blue: #4A7CFF
- Red: #C84B5A
- White / off-white remains dominant

Use blue and red sparingly:
- hover state
- link underline
- small labels
- subtle border accent
- active buttons
- faint glow

Do not flood the site with bright accent colors.

### Layout feel

Use:
- clean editorial grid
- balanced spacing
- cards that feel intentional, not templated
- stronger visual previews
- fewer lines of card text

The evidence should be more visually important than the website chrome.

---

## 2. Remove obvious current homepage problems

Remove completely:
- top-left site logo / icon
- "Integration draft · remaining project evidence awaiting handoffs"
- decorative project numbers 01 / 02 / 03 / 04
- generic placeholder diagrams where a real image can be used
- repetitive workflow text on homepage cards
- excessive uppercase micro-labels

Header:
- make "Harman Singh" larger and bolder
- keep header minimal
- no fake site branding
- no internal status / QA copy

---

## 3. Homepage hero

Title:
**Selected Quantitative Systems**

Subtitle:
**Research systems, trading infrastructure, scenario engines and market-data workflows.**

Keep hero compact.

Do not add:
- slogans
- pseudo-profound fragments
- X / Y headline structures
- marketing copy

---

## 4. Homepage project-card structure

Show four main cards only:

1. Portfolio Research Infrastructure
2. LTG Trading & Reporting System
3. Policy-Path Scenario Engine
4. Market Data Processing Platform

Each card should contain only:
- small project/context label
- project title
- 10-15 word description maximum
- small tech-skill boxes
- project-specific visual background / thumbnail
- one CTA

Do not put long workflow arrows on the homepage cards.

Do not include generic buzzwords.

Tech boxes should contain only genuine technologies or methods used.

Card interactions:
- subtle hover lift
- subtle border glow
- background image becomes slightly clearer on hover
- no flashy animation

---

## 5. QF card

Context:
**Mathematical Finance Research**

Title:
**Portfolio Research Infrastructure**

Description:
**Point-in-time WRDS/CRSP research pipeline for portfolio construction and realized-risk evaluation.**

Tech boxes:
- Python
- WRDS
- CRSP CIZ
- SSH
- CPU26

Background / visual:
Use the manuscript heading / top of the paper as the glassy background identity.

The visual should:
- be recognizably a research manuscript
- stay low-opacity behind the text
- become slightly more visible on hover

CTA:
**Open project**

---

## 6. LTG card

Context:
**Laurier Trading Group**

Title:
**LTG Trading & Reporting System**

Description:
**Trade intake, quote routing, portfolio state and live web reporting for LTG.**

Tech boxes:
- Google Forms
- Google Sheets
- Apps Script
- Yahoo Finance
- Stooq

Background / visual:
Use the LTG instrument-allocation pie chart as the glassy background identity.

Keep the chart recognizable but muted.

On hover, slightly increase opacity / clarity.

CTA:
**Open project**

---

## 7. Citadel card

Context:
**Citadel FI&M Central Bank Challenge**

Title:
**Policy-Path Scenario Engine**

Description:
**Semi-structural engine for ranking feasible Fed paths across macro scenarios.**

Tech boxes:
- Python
- ARDL
- BVARX
- Scenario scoring

Background / visual:
Use **slide 2 from the Citadel presentation** as the primary thumbnail / background.

Also display the **Citadel logo** on the card.

The slide should feel like a real presentation asset, not a generic placeholder.

If useful, use the slide as a slightly blurred / glassy background behind a darker text overlay.

CTA:
**Open project**

---

## 8. DataFlow card

Context:
**Market Data Infrastructure**

Title:
**Market Data Processing Platform**

Description:
**Queued market-data retrieval, batch processing and downloadable time-series outputs.**

Tech boxes:
- Next.js
- TypeScript
- Node.js
- SQLite
- Polygon

Background / visual:
Use the cleaned DataFlow home screen as the glassy background identity.

On hover:
- slightly animate the background position or opacity
- keep movement subtle

CTA:
**Open project**

---

## 9. Card visual language

All cards should share:
- same radius
- same border logic
- same title spacing
- same tech-box sizing
- same CTA treatment
- same hover behavior

But each should have project-specific art.

Do not use:
- giant white placeholder rectangles
- generated workflow diagrams as thumbnails
- random code screenshots as the homepage visual
- oversized body copy

The card should entice. The project page provides the proof.

---

## 10. Cross-page standardization

Apply the same visual language across:
- homepage
- QF
- LTG
- Citadel
- DataFlow

Standardize:
- background color
- heading font
- body font
- text hierarchy
- accent blue
- accent red
- card/panel border color
- buttons
- link styling
- captions
- section spacing
- image corners
- hover behavior

The pages must not look like separate AI-generated microsites.

Do not erase project-specific visual character. Standardize the site shell, not the evidence itself.

---

## 11. Detail-page visual identities

Add a restrained project-specific background motif to each detail page.

### QF
Use a low-opacity crop from the manuscript header / title page.

### LTG
Use a low-opacity version of the instrument-allocation pie chart.

### Citadel
Use the Citadel logo and a low-opacity crop from the presentation.

### DataFlow
Use the DataFlow home-screen visual or market-data UI.

Rules:
- background must never hurt readability
- keep opacity low
- glass / blur is allowed but restrained
- background may become slightly clearer during scroll/hover if tasteful
- do not animate constantly
- respect reduced-motion preferences

---

## 12. Remove AI / template cues

Remove or rewrite anything that feels like:
- generic OpenAI showcase styling
- fake professionalism
- measured work / traceable runs style phrases
- infrastructure buzzwords
- repetitive "View workflow / View system / View model" patterns
- excessive slashes
- em dashes
- perfectly symmetrical robotic copy

No em dashes across the homepage.

Do not use:
- robust
- seamless
- scalable
- sophisticated
- innovative
- cutting-edge
- actionable insights
- high-performance framework
- comprehensive system
- powerful platform

Use literal project names, real tools, and short descriptions.

---

## 13. Homepage footer

Keep minimal.

Left:
**Harman Singh**

Right:
**Quantitative research, markets and systems**

Make Harman Singh more visually prominent than the current tiny footer treatment.

---

## 14. Homepage visual composition

Preferred desktop layout:
- compact hero
- 2x2 project grid
- cards with full visual identity
- minimal footer

Do not include RBC on the homepage in this redesign pass unless specifically instructed later.

The four project cards should dominate the page.

---

## 15. Mobile

Make sure:
- titles stay readable
- tech boxes wrap naturally
- backgrounds remain legible
- cards stack cleanly
- hover-dependent information is still visible without hover
- no horizontal scrolling

---

## 16. Final output

Return:
1. full-page homepage screenshot
2. mobile homepage screenshot
3. exact font families and sizes used
4. exact final color palette
5. exact visible copy on all four cards
6. screenshots of QF, LTG, Citadel and DataFlow after shared design-system standardization
7. confirmation that:
   - top-left logo is removed
   - Integration draft text is removed
   - Harman Singh is larger / bolder
   - project numbers are gone
   - QF uses manuscript imagery
   - LTG uses allocation-pie imagery
   - Citadel uses slide 2 and the Citadel logo
   - DataFlow uses its home-screen visual
   - no em dashes remain on homepage
   - typography no longer resembles generic ChatGPT / OpenAI showcase styling

Do not preserve the current homepage merely because it exists. The homepage needs a real redesign.
