---
name: data-to-figure
description: Use when turning data into a publication-ready plot or multi-panel figure in Python (matplotlib) or R (ggplot2 + patchwork) — setting fonts/sizes via a theme, automatic a/b/c or A/B/C panel labels, exact mm journal widths, and exporting PDF/SVG with embedded fonts or TIFF at 300–600 dpi. Trigger on "make this figure journal-ready", "export at 89 mm", "add panel labels", "fonts not embedded", growth/survival/CFU plots.
---

# Data → figure (code templates)

Design rules live in `figure-design-core`; this skill is the implementation.

## Files
- `scripts/fig_template.py` – matplotlib template: `set_theme()`, `add_panel_labels()`, `save_all()`, journal presets (`--journal nature|cell|elsevier|plos`).
- `scripts/fig_template.R` – ggplot2 + patchwork template: `theme_pub()`, `plot_annotation(tag_levels = "a"|"A")`, `ggsave(units = "mm", device = cairo_pdf)`.
- `scripts/simulate_data.py` – **simulated** food-microbiology data (Gompertz growth, log-linear D-value survival, CFU per treatment). Not real data.
- `scripts/check_fonts.sh` – `pdffonts` check (want `emb yes`, TrueType/CID, never Type 3).
- `templates/style_cheatsheet.md` – rcParams/theme snippets incl. Traditional Chinese (Noto Sans TC).
- `examples/output/` – rendered examples (Nature and Cell presets).

## Procedure
1. Pick the journal preset → width (single/double mm) and label case.
2. Set the theme **before** plotting; design at final size, never resize afterwards.
3. Build panels with `subplot_mosaic` (Py) or `|`, `/` (patchwork); share axes/legends where variables are shared.
4. Add labels with the helper (same offset from every axes → aligned).
5. Export: `save_all(fig, "out/Fig1")` → PDF (Type 42), SVG (`svg.fonttype='none'`), TIFF LZW 600 dpi, PNG preview.
6. Verify: `scripts/check_fonts.sh out/Fig1.pdf`; check TIFF pixel size = width_mm/25.4 × dpi.
7. Label simulated/example data as such on the figure.

## Run
```bash
python -m venv .venv && .venv/bin/pip install matplotlib numpy pandas
cd scripts && ../.venv/bin/python fig_template.py --journal nature
Rscript fig_template.R   # needs ggplot2, patchwork, svglite (checked before plotting)
```

## Gotchas
- matplotlib mathtext (`$_{10}$`) uses DejaVu by default → set `mathtext.default: regular` (done) so subscripts use the main font.
- If Arial is missing on Linux, Liberation Sans is metric-compatible; install `ttf-mscorefonts` or supply Arial for final submission.
- `bbox_inches="tight"` changes the final width — avoid it when exact mm matters.
