# Publication multi-panel figure template (R: ggplot2 + patchwork). SIMULATED data only.
# install.packages(c("ggplot2", "patchwork", "svglite"))  # svglite required for .svg export

# --- preflight: required packages (avoid partial outputs) [F02]
req <- c("ggplot2", "patchwork", "svglite")
missing <- req[!vapply(req, requireNamespace, FUN.VALUE = logical(1), quietly = TRUE)]
if (length(missing) > 0) {
  stop(sprintf("Missing required R packages: %s. Please install before running.", paste(missing, collapse = ", ")))
}
library(ggplot2); library(patchwork)
mm <- function(x) x / 25.4
journal <- list(nature = list(w = 183, case = "a", label = 8, base = 7),
                cell   = list(w = 174, case = "A", label = 9, base = 7))
J <- journal[["nature"]]
okabe <- c("#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7")

theme_pub <- function(base = 7, family = "Arial") {   # Chinese: family = "Noto Sans TC"
  theme_classic(base_size = base, base_family = family) +
    theme(axis.line = element_line(linewidth = .3), axis.ticks = element_line(linewidth = .3),
          axis.text = element_text(size = base - 1, colour = "black"),
          legend.position = "none", plot.tag = element_text(size = J$label, face = "bold"),
          plot.tag.position = c(0, 1))
}
set.seed(42)
# --- simulated growth (modified Gompertz)
t <- seq(0, 48, 3); pars <- data.frame(temp = c(10, 25, 37), mu = c(.15, .45, .7), lag = c(12, 4, 2))
growth <- do.call(rbind, lapply(1:3, function(i) {
  p <- pars[i, ]
  y <- 3 + 6 * exp(-exp(p$mu * exp(1) / 6 * (p$lag - t) + 1))
  do.call(rbind, lapply(1:3, function(r) data.frame(temp = factor(p$temp), time = t, y = y + rnorm(length(t), 0, .12))))
}))

# --- mean±SD by base R (remove Hmisc::mean_sdl dependency) [F02]
agg_mean <- aggregate(y ~ temp + time, data = growth, FUN = mean)
agg_sd   <- aggregate(y ~ temp + time, data = growth, FUN = sd)
colnames(agg_sd)[3] <- "sd"
gsum <- merge(agg_mean, agg_sd, by = c("temp", "time"))

# --- simulated survival (log-linear, D-values)
surv <- do.call(rbind, lapply(list(c(55, 8), c(60, 2.5), c(65, .8)), function(p) {
  tt <- rep(seq(0, 5 * p[2], length.out = 7), 3); data.frame(temp = factor(p[1]), time = tt, y = 7 - tt / p[2] + rnorm(length(tt), 0, .15)) }))
# --- simulated CFU
cfu <- data.frame(trt = factor(rep(c("Control", "Washed", "Washed+PAA", "UV-C"), each = 8), levels = c("Control", "Washed", "Washed+PAA", "UV-C")),
                  y = rnorm(32, rep(c(6.2, 5.1, 3.4, 4.3), each = 8), .45))

pa <- ggplot(gsum, aes(time, y, colour = temp)) +
  geom_ribbon(aes(ymin = y - sd, ymax = y + sd, fill = temp), alpha = .2, colour = NA) +
  geom_line() +
  scale_colour_manual(values = okabe[5:7]) + scale_fill_manual(values = okabe[5:7]) +
  labs(x = "Time (h)", y = expression(log[10]~CFU/mL), colour = "Temperature (°C)", fill = "Temperature (°C)") +
  theme_pub(J$base) + theme(legend.position = "right")  # [F03]
pb <- ggplot(surv, aes(time, y, colour = temp)) +
  geom_point(size = .8) + geom_smooth(method = "lm", se = FALSE, linewidth = .5) +
  scale_colour_manual(values = okabe[5:7]) +
  labs(x = "Time at temperature (min)", y = expression(log[10]~survivors), colour = "Temperature (°C)") +
  theme_pub(J$base) + theme(legend.position = "right")  # [F03]
pc <- ggplot(cfu, aes(trt, y)) + geom_boxplot(width = .45, outlier.shape = NA, linewidth = .3) + geom_jitter(width = .12, size = .9, colour = okabe[5]) +
  labs(x = NULL, y = expression(log[10]~CFU/g)) + theme_pub(J$base)

fig <- (pa | pb) / pc +
  plot_layout(guides = "collect") +
  plot_annotation(tag_levels = J$case, caption = "SIMULATED DATA - template only") &
  theme(legend.position = "bottom", plot.caption = element_text(size = 5, colour = "grey50"))
dir.create("../examples/output", showWarnings = FALSE, recursive = TRUE)
ggsave("../examples/output/fig_food_micro_R.pdf", fig, width = J$w, height = 110, units = "mm", device = cairo_pdf)
ggsave("../examples/output/fig_food_micro_R.svg", fig, width = J$w, height = 110, units = "mm")
ggsave("../examples/output/fig_food_micro_R.tiff", fig, width = J$w, height = 110, units = "mm", dpi = 600, compression = "lzw", bg = "white")
