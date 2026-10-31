---
name: graphical-abstract-and-infographic
description: Use when creating a graphical abstract (GA), visual abstract, TOC graphic, or a vertical science infographic/poster panel — planning the message, layout/flow, icons, arrows, text and colour, choosing journal GA sizes, and tool tips for PowerPoint, Inkscape, BioRender or Canva. Trigger on "graphical abstract", "visual summary", "infographic", "TOC image".
---

# Graphical abstract & infographic

## Shared workflow (do in this order)
1. **Message** – one sentence: what was done → what was found → why it matters. If you can't say it, you can't draw it.
2. **Layout / flow** – choose a skeleton: *linear* (process, left→right), *circular* (cycle/feedback), *parallel* (comparison, control vs treatment), *nested* (scale: food → cell → molecule). Sketch on paper first, 3–5 elements max.
3. **Icons** – one consistent style (all flat or all outline); free, licensed libraries: Bioicons, Servier Medical Art (SMART), Reactome icons, PhyloPic, Health Icons, SVGRepo; record each licence and credit as required.
4. **Arrows** – one arrow style meaning one thing (e.g., causes/leads to); avoid crossing; consistent weight.
5. **Text** – minimal: short labels, no sentences, no abbreviations unexplained; ≥ legible size when shrunk (test at thumbnail).
6. **Colour** – 2–3 hues + neutrals, CVD-safe, ≥4.5:1 text contrast (WebAIM checker); reuse paper's colour codes.

## Spec switch
| | Graphical abstract | Vertical infographic |
|---|---|---|
| Purpose | entice & summarise one paper at a glance (thumbnail) | explain a topic to broader audience, scroll/print |
| Shape | landscape; Elsevier min. 1328 px wide × 531 px high; Cell Press uses its own square-ish template (verify current spec) | portrait, e.g., 1080×1920 px or A4/A3 |
| Text | very little; no data tables; title optional | headings + short blocks, numbered sections |
| Reading | single entry point, left→right | top→bottom, Z/F pattern, sections |
| Data | key result as icon/simple chart | can include 1–3 simplified charts with sources |

## Ten-rule checklist (paraphrased from Jambor & Bornhäuser 2024, PLoS Comput Biol, CC BY)
1 Identify the single main finding · 2 Know the journal's format first · 3 Sketch several layouts · 4 Pick a clear reading direction · 5 Use metaphors/icons consistently · 6 Minimise text · 7 Use colour sparingly and accessibly · 8 Keep visual hierarchy (biggest = most important) · 9 Get feedback from outsiders (1-second test) · 10 Iterate and check at small size.

## Tool notes
- **PowerPoint**: set slide size to target px/mm first; use Align/Distribute and Smart Guides; group icons; export via File → Export → PNG/TIFF at high resolution (registry or "Save as PDF" then rasterise).
- **Inkscape** (free, vector): Document Properties for mm size; Align & Distribute; snapping to grid; File → Save a Copy as PDF (embed fonts) / Export PNG at 300–600 dpi; import SVG icons directly.
- **BioRender**: large licensed biology icon library; check plan—publication requires paid licence & citation line; export PNG/PDF at high res.
- **Canva**: quick infographics; custom size in px/mm; check icon/element licences for publication; export PDF Print with fonts; Canva's colour palette tool to lock brand/paper colours.
See `templates/ga_planning_sheet.md`.

## Infographic types & design patterns (paraphrased from Figma's "46 infographic examples")
Source: Figma Resource Library, https://www.figma.com/resource-library/infographic-examples/ (accessed 2026-11-01). Summarised in our own words; no images reused.

**When to choose an infographic:**
- simplifying statistics
- explaining a process
- summarising a report's takeaways
- comparing options
- outreach on social media

For a single paper's key finding, use a graphical abstract instead.

**Three families of infographic.** Pick one first; they can be combined.
1. **Statistical:** numbers and survey or study results shown as charts. You may mix chart types in one piece (map + line + bar + donut), as long as each chart answers a different question. Big bold numbers draw the eye; keep the units and the source next to them.
2. **Informational:** concepts shown as
   - a **list** (tips/checklist, one icon per item)
   - a **timeline** (milestones, roadmap)
   - a **hierarchy** (pyramid or tree, e.g. a food pyramid)
   - a **comparison** (side by side, pros and cons, a Venn diagram)
   - a **map** (regional data; colour-code the regions and keep the map unlabelled if a legend suffices)
3. **Process:** a sequence of actions shown as a flowchart, cycle, decision tree, or numbered how-to steps. Arrows and large step numbers guide the reader; illustrations can be more detailed because they instruct.

**Patterns from the gallery that are worth reusing in science:**
- One explanatory "key" panel that teaches the reader how to read a repeated small chart, e.g. the first radar chart in a grid. This is the same idea as small multiples plus a legend.
- Numbered steps with one icon each, for protocols (e.g. sample → enrichment → plating → counting).
- A decision-tree flowchart with even spacing and highlighted end-points, e.g. "which test or chart should I use?".
- A shape metaphor that encodes data, e.g. circle size for magnitude. Use it only if the sizes stay honest (area, not radius).
- A limited or complementary palette (e.g. blue + orange, or monochrome) and plenty of negative space for legibility.
- A scrolling or "winding road" vertical narrative for long explanatory pieces.

**Figma's four elements of a good infographic:**
1. Important, concise content with no filler.
2. A clear story that stands alone, without the article around it.
3. Coherent design and style: palette, relevant images.
4. Size and shape that suit where it will be shown, with legible fonts and no crowding; resize per platform.

**Science caveat.** Marketing-style examples often use decorative gradients, photos behind text, mixed fonts, or 3-D. For scientific outreach:
- keep one sans-serif family
- keep contrast ≥4.5:1
- cite the data sources on the graphic
- label simulated or illustrative numbers as such
