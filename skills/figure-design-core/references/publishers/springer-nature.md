# Springer Nature (Nature Portfolio): figure specifications

Last checked: 2026-11-01. ✅ verified at the cited source; ⚠️ unverified or secondary source, so check before use.

## Publisher base rules (Nature Portfolio house style; taken from the Nature research figure guide)
| Item | Rule | Source / status |
|---|---|---|
| Font | Sans-serif, Arial or Helvetica. Courier (monospaced) for amino-acid sequences, one-letter code in lines of 50 or 100 characters. Symbol font for Greek. | ✅ [NFG-spec] |
| Font size | Text 5–7 pt (min 5, max 7) | ✅ [NFG-spec] |
| Panel label style | 8 pt **bold, upright, lowercase** a, b, c | ✅ [NFG-spec] |
| Column widths | 89 mm single / 183 mm double | ✅ [NFG-build] |
| Max figure dimensions | Max height 170 mm, so the legend fits underneath | ✅ [NFG-build] |
| File formats | Vector PDF or EPS preferred; text editable, not outlined | ✅ [NFG-spec] |
| Font embedding | Fonts embedded as TrueType 2 or 42, not Type 3; matplotlib `pdf.fonttype=42` | ✅ [NFG-spec] |
| Resolution | Photos at least 300 dpi; 450 dpi or more gives the best online proof; images in exported figures at least 450 dpi | ✅ [NFG-spec] |
| Colour mode | RGB; converted to CMYK automatically for print | ✅ [NFG-spec] |
| Scale bars | Kept on a separate editable layer; use scale bars, not magnification factors | ✅ [NFG-spec] |
| Other | Axis lines and ticks; units in parentheses; accessible palette (e.g. Wong 2011); no background gridlines, drop shadows, patterns, or coloured text; avoid text on busy images | ✅ [NFG-spec] |
| Layout | Panels tidy and space-efficient, in alphabetical order where possible | ✅ [NFG-build] |

**Scope caveat:** the figure guide is written for Nature. Other Springer Nature journals (non-Nature-branded Springer and BMC titles) have their own artwork guidelines, which are not covered here. ⚠️ Check before use.

## Journal exceptions

### Nature
| Item | Differs how | Source / status |
|---|---|---|
| Widths at initial submission | Some Nature pages quote 90 / 180 mm and a 170 mm page depth; the final-submission page quotes 89 / 183 mm, 1.5-column 120–136 mm, and a 247 mm page depth. Build to 89 / 183 mm. | ⚠️ secondary summary [SCIFIG]; check before use |

### Nature Communications
| Item | Differs how | Source / status |
|---|---|---|
| Column widths | **88 mm** single / **180 mm** double. Bitmaps at least 1,040 px (single) or 2,080 px (double) wide. | ✅ [NCOMMS] |
| Page size | Prepare figures to fit the PDF page, 210 × 276 mm | ✅ [NCOMMS] |
| Panel labels | Bold lowercase a, b, … **in the same type size as the other figure text**, not a fixed 8 pt | ✅ [NCOMMS] |
| Font | Clear sans-serif, e.g. Helvetica; the same typeface at roughly the same size in every figure | ✅ [NCOMMS] |
| Lines | Thinnest lines at least 1 pt | ✅ [NCOMMS] |
| Line art | Vector EPS, AI, or PDF; if vector is impossible, 1,200 dpi | ✅ [NCOMMS] |
| Photos | TIFF, at least 300 dpi, RGB | ✅ [NCOMMS] |
| Other | Lettering in lower case with the first letter capitalised; SI units with a space before the unit; comma separators for numbers ≥ 10,000; recolour red/green images, e.g. to green/magenta | ✅ [NCOMMS] |

## Sources
- [NFG-spec] Nature research figure guide, "Preparing figures – our specifications": https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/
- [NFG-build] Nature research figure guide, "Building and exporting figure panels": https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/ (checked 2026-11-01)
- [NCOMMS] Nature Communications, "How to submit": https://www.nature.com/ncomms/submit/how-to-submit (checked 2026-11-01)
- [SCIFIG] Secondary summary of Nature's conflicting width statements: https://scifig.ai/blog/nature-formatting-requirements
- Nature formatting guide: https://www.nature.com/nature/for-authors/formatting-guide. Check before use.
- Wong B (2011). Points of view: Color blindness. *Nat Methods* 8:441.
