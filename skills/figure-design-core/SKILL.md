---
name: figure-design-core
description: Use when designing, planning, or fixing any scientific figure (chart choice, colour, typography/fonts, multi-panel layout and a/b/c panel labels, statistical honesty, figure vs table). Trigger on questions like "which chart should I use", "what font/size for my figure", "how to label and arrange panels", "is this colour-blind safe", or before generating any publication figure.
---

# Figure design core

Backbone: Fujii's five tactics (Nat Hum Behav 2026), summarised in our own words:
1. **One message per figure** – write the take-home sentence first; every element must serve it.
2. **Match the chart to the data structure and the comparison** (see chooser below).
3. **Reduce cognitive load** – remove non-data ink, label directly, keep reading order natural.
4. **Use colour purposefully** – few hues, consistent meaning, accessible.
5. **Be honest and transparent** – show the data and the uncertainty, define every error bar.

## Workflow
1. Write the message (one sentence) and the audience/venue (paper, poster, slide).
2. Identify the target journal → load `references/journal-specs.md` (index) → open `references/publishers/<publisher>.md` for base rules + journal exceptions (width, fonts, label style).
3. Choose chart type with `references/chart-chooser.md`.
4. Apply typography + layout rules below; build on a grid at final size (mm).
5. Self-review with the `figure-review-rubric` skill (1-second test).

## Colour rules
- ≤4–5 distinguishable hues per figure; use grey for context, one accent colour for the key result.
- Same variable = same colour across all panels and figures of the paper.
- Colour-blind safe palettes: Okabe–Ito (Wong 2011, Nat Methods), viridis/cividis for continuous data; never rely on red–green contrast alone; diverging maps only for data with a meaningful midpoint.
- Check with a CVD simulator (e.g., Coblis, Color Oracle) and in greyscale.
- Avoid coloured text; use black text + coloured keys (Nature guideline).

## Cognitive load & direct labelling
- Delete gridlines, borders, 3-D, shadows, redundant legends (data-ink ratio, Tufte).
- Put labels next to lines/groups instead of a distant legend; use Gestalt proximity and similarity to group.
- Put the comparison of interest side by side on a common aligned scale (position > length > angle > area > colour; Cleveland & McGill 1984).

## Statistical honesty
- Prefer showing raw points (dot/strip, beeswarm) over bar-of-means ("dynamite plots"); add box/violin when n is large.
- State in the legend: n (and what a replicate is), what the centre is, and whether bars are **SD** (spread of data), **SE** (precision of mean), or **95% CI** (inference). Never leave "error bars" undefined.
- Axes: bar charts start at zero; log scales labelled as such (e.g., log10 CFU/g); don't truncate to exaggerate.
- Don't hide distributions behind means; don't cherry-pick representative images.

## Figure vs table
- Figure: patterns, trends, comparisons, distributions, relationships.
- Table: exact values needed, many heterogeneous variables, lookup use.
- If a figure needs >1 legend paragraph to read, consider splitting or a table.

## TYPOGRAPHY (fonts)
- **One sans-serif family** for the whole figure: Arial or Helvetica (Nature, Cell, Elsevier all accept; Liberation Sans is a metric-compatible free Arial substitute on Linux).
- **Size at final print size** (not on screen): body text 5–7 pt (Nature), ~6–8 pt (Cell), ~7 pt with ≥6 pt sub/superscripts (Elsevier), 8–12 pt (PLOS). Practical default: 7 pt ticks, 7–8 pt axis titles, 8 pt bold panel labels. Design at 100% width, never scale a figure after setting fonts.
- **Hierarchy with ≤3 sizes**: panel label (largest, bold) > axis titles/annotations > tick labels. Use weight, not many sizes, for emphasis. No italic except gene/species names (*Listeria monocytogenes*) and variables.
- Units in parentheses: "Time (h)", "log10 CFU/g". Use real minus signs, superscripts, and µ (not "u").
- **CJK figures (Traditional Chinese)**: pair Noto Sans TC (or Noto Sans CJK TC / 思源黑體) for Chinese with Arial/Helvetica for Latin & numbers; set the same visual size (CJK often looks larger—drop ~0.5 pt or match x-height); avoid Microsoft JhengHei/PMingLiU mixing within one figure; don't use bold for long CJK strings.
- **Embed fonts**: matplotlib `pdf.fonttype=42`, `ps.fonttype=42` (TrueType, editable; Nature explicitly asks for Type 2/42, not Type 3); SVG `svg.fonttype='none'` keeps text as text. R: `cairo_pdf()` or `ggsave(device=cairo_pdf)`; check with `pdffonts file.pdf`. Never outline text unless the journal asks.

## MULTI-PANEL LAYOUT (a/b/c panels)
- **Label style depends on the journal**: Nature family = **bold lowercase a, b, c, 8 pt, upright**; Cell Press = **bold uppercase A, B, C**; PLOS/Elsevier = follow journal, commonly uppercase; be consistent with how the legend and text cite them ("Fig. 1a" vs "Figure 1A").
- **Position**: top-left corner of each panel, outside the axes area, all labels aligned on the same baseline/left edge across a row/column.
- **Reading order**: Z-pattern (left→right, then down) following the story; panel a should be the entry point (often the setup/schematic), the key result prominent.
- **Grid**: build on an invisible grid of equal columns; align axes edges (not label edges) between panels; equal gutters (~2–4 mm).
- **Share** axes and legends when panels share variables (one legend for the figure, or direct labels); identical scales for panels meant to be compared; same colour mapping throughout.
- **Small multiples**: same axes, same size, varied single factor—better than one crowded panel.
- **Widths**: Nature 89 mm (single) / 183 mm (double); Cell 85 / 114 / 174 mm; Elsevier 90 / 140 / 190 mm; PLOS 13.2 cm common, max 19.05 cm. Max height ~ 170–240 mm depending on journal.
- Whitespace is structure: more space between unrelated groups than within a group (Gestalt proximity).
- Implementation: `data-to-figure` skill (patchwork `tag_levels`, matplotlib `subplot_mosaic` + `fig.text`).

## References
See `references/sources.md` (all paraphrased; no figures copied), `references/journal-specs.md` (index) and `references/publishers/`.
