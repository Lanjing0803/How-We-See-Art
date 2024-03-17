##renaissance 1400-1600
library(ggplot2)
#rococo
colors <- read.csv("dominant_colors_renaissance.csv", header = FALSE)

n_cols <- 14
n_rows <- ceiling(nrow(colors) / n_cols)


df <- expand.grid(x = 1:n_cols, y = 1:n_rows)
df$col <- rep(colors$V1, length.out = n_cols * n_rows)

###########ggplot
p <- ggplot(df, aes(x = x, y = y, fill = col)) +
  geom_tile(color = "white") +
  scale_fill_identity() +
  theme_void() +
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.position = "none",
        axis.text = element_blank(),
        axis.title = element_blank(),
        axis.line = element_blank(),
        plot.margin = unit(c(0, 0, 0, 0), "cm"))

############## ggsave
ggsave("colors.jpeg", p, width = 20, height = 10, dpi = 300)




