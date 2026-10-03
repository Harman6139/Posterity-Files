# Parallel project-page dispatch

Use the four existing audit chats and run them in parallel.

The chats all start with:
- `Audit QF`
- `Audit LTG`
- `Audit Citadel`
- `Audit DataFlow`

## What to do
1. Find and open each matching chat.
2. In each chat, load the matching specification from `Harman6139/Posterity-Files/prompts/ad_hoc_communication/`.
3. Delegate only that page to that audit agent.
4. Run all four page revisions in parallel.

Matching specifications:
- Audit QF -> `Audit_QF_page_spec.md`
- Audit LTG -> `Audit_LTG_page_spec.md`
- Audit Citadel -> `Audit_Citadel_page_spec.md`
- Audit DataFlow -> `Audit_DataFlow_page_spec.md`

## Global design rules
All four pages must inherit the finalized homepage design system:
- white or soft off-white editorial background
- restrained navy / blue accents
- human-looking typography
- clean spacing and hierarchy
- consistent buttons, borders, image radius, footer and nav
- minimal buzzwords
- no AI-sounding captions

Keep each page visual and process-led.

If anything seems obscure, rewrite it more plainly.
If wording is too polished or generic, simplify it.
If there is too much code and not enough process, rebalance it.
If there is too much process text and not enough visual evidence, rebalance it.
Do not let code dominate a page unless the code itself is the evidence.

## Page-specific content
The project-specific specification is the source of truth for copy, evidence, naming and layout details.

Do not overwrite finalized project content with generic homepage copy.

## Integration pass
After all four agents finish:
1. review all four pages side by side
2. standardize font family, font sizes, spacing, colors, buttons, borders, image framing, nav, footer, and hover behavior
3. remove any remaining AI-style labels, filler copy, em dashes, internal notes, or placeholder wording
4. make sure the four pages feel like one cohesive site while retaining project-specific visual identity

## Final deliverable
Return:
- updated QF page
- updated LTG page
- updated Citadel page
- updated DataFlow page
- desktop screenshots of each
- mobile screenshots if available
- a short note of what changed on each page
- any final inconsistency still requiring manual intervention