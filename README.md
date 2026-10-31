# sci-figure-skills

Agent Skills for designing scientific figures, graphical abstracts and infographics — with special focus on **typography** and **multi-panel (a/b/c) layout**, plus runnable Python/R templates.

| Skill | Use it for |
|---|---|
| `skills/figure-design-core` | Design rules: Fujii's 5 tactics, chart chooser, colour, typography, multi-panel layout, statistical honesty, verified journal specs (Nature, Cell, PLOS, Elsevier) |
| `skills/data-to-figure` | matplotlib & ggplot2/patchwork templates: theme, auto panel labels, exact mm export to PDF/SVG/TIFF |
| `skills/graphical-abstract-and-infographic` | Message → layout → icons → arrows → text → colour workflow; GA vs vertical infographic specs; tool notes |
| `skills/figure-review-rubric` | 1-second test, reverse feedback, 32-point rubric for self-review or grading |

Teaching material (Traditional Chinese): `docs/teaching-zh-TW/`.

## Install
Each folder under `skills/` is a self-contained skill (`SKILL.md` with YAML frontmatter `name` + `description`).
- **Claude Code / Agent-Skills-compatible agents**: copy or symlink folders into `~/.claude/skills/` (user) or `.claude/skills/` (project).
- **Other agents**: point the agent's skill directory at `skills/`, or paste `SKILL.md` into a system prompt.

Python templates:
```bash
python -m venv .venv && .venv/bin/pip install matplotlib numpy pandas
cd skills/data-to-figure/scripts && ../../../.venv/bin/python fig_template.py --journal nature
```
R: `install.packages(c("ggplot2","patchwork"))` then `Rscript fig_template.R`.

## Example data
All example data are **simulated** food-microbiology values (growth curves, D-value survival, CFU counts) produced by `simulate_data.py`. They are not experimental results.

## Sources & copyright
Content paraphrases and cites the sources listed in each skill's `references/`. No figures or long passages are reproduced. Midway (2020) is CC BY-NC-ND, Healy (2018) is all rights reserved, Amoah-Oppong (2025) is CC BY-NC, and Jambor & Bornhäuser (2024) is CC BY. See `LICENSE-NOTES.md`.

## Licence
- Code (`*.py`, `*.R`, `*.sh`): **MIT**, see `LICENSE` (© 2026 Vincent Chiang).
- Text, skills documentation and teaching material (`SKILL.md`, `references/`, `templates/*.md`, `docs/`): **CC BY 4.0**, see `LICENSE-CC-BY-4.0`. Attribute as: "sci-figure-skills by Vincent Chiang, CC BY 4.0".
- Third-party works cited remain under their own licences.
