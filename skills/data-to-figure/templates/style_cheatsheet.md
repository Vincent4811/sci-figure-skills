# Style cheatsheet

## matplotlib
```python
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Arial", "Liberation Sans"],
  "font.size": 7, "pdf.fonttype": 42, "ps.fonttype": 42, "svg.fonttype": "none", "mathtext.default": "regular"})
fig = plt.figure(figsize=(89/25.4, 60/25.4))   # Nature single column
```
Traditional Chinese: `"font.sans-serif": ["Arial", "Noto Sans TC", "Noto Sans CJK TC"]` (Latin glyphs from Arial, CJK falls back to Noto, matplotlib ≥3.6).

## ggplot2
```r
theme_classic(base_size = 7, base_family = "Arial")
# Chinese: library(showtext); font_add_google("Noto Sans TC"); showtext_auto(); base_family = "Noto Sans TC"
p + plot_annotation(tag_levels = "a") & theme(plot.tag = element_text(size = 8, face = "bold"))
ggsave("Fig1.pdf", width = 183, height = 120, units = "mm", device = cairo_pdf)
```
## Size table (pt at final size)
| element | Nature | Cell | PLOS |
|---|---|---|---|
| panel label | 8 bold lower | ~9 bold UPPER | 10–12 |
| axis title | 7 | 7–8 | 8–10 |
| tick label | 5–6 | 6–7 | 8 |
