# Chart chooser (by data structure and question)

| Question / data | Recommended | Avoid |
|---|---|---|
| Compare groups, continuous outcome, small n (<~20/group) | dot/strip plot + mean±CI or median | bar of means only |
| Compare groups, larger n | box + jittered points, violin, beeswarm | dynamite plot |
| Change over time (e.g., microbial growth) | line + points, ribbon for CI; log y for counts | stacked areas for few series |
| Dose/time–response, survival (D-value) | log10 survivors vs time + fitted line | linear y for log-scale processes |
| Relationship between two continuous vars | scatter (+ fit and CI) | connected lines without order |
| Part-to-whole (few parts) | stacked bar / single bar; pie only ≤3 parts | 3-D pie, donut with many slices |
| Distribution of one variable | histogram, density, ECDF | bar of mean |
| Many variables × samples | heatmap (with clustering, viridis) | rainbow colour map |
| Ranking | sorted horizontal dot/bar chart | unsorted categories |
| Paired before/after | slope graph (paired lines) | two independent bars |
| Exact values matter | table | figure |

Perception ranking (Cleveland & McGill 1984): position on common scale > position on unaligned scales > length > angle/slope > area > volume > colour hue/saturation.
