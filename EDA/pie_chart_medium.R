library(ggplot2)
artwork_info <- read.csv("artwork_info_renaissance_title.csv", header = TRUE)

artwork_info$Medium_Category <- ""
artwork_info$Medium_Category[grep("oil", artwork_info$Medium, ignore.case = TRUE)] <- "OIL"
artwork_info$Medium_Category[grep("tempera", artwork_info$Medium, ignore.case = TRUE)] <- "TEMPERA"
artwork_info$Medium_Category[grep("bronze", artwork_info$Medium, ignore.case = TRUE)] <- "BRONZE"
artwork_info$Medium_Category[grep("watercolor", artwork_info$Medium, ignore.case = TRUE)] <- "WATERCOLOR"
artwork_info$Medium_Category[grep("Distemper", artwork_info$Medium, ignore.case = TRUE)] <- "DISTEMPER"
artwork_info$Medium_Category[grep("gold|gilt|metal", artwork_info$Medium, ignore.case = TRUE)] <- "GOLD"
artwork_info$Medium_Category[grep("ink", artwork_info$Medium, ignore.case = TRUE)] <- "INK"
artwork_info$Medium_Category[grep("silver", artwork_info$Medium, ignore.case = TRUE)] <- "SILVER"
artwork_info <- subset(artwork_info, !(Medium %in% c("transferred to canvas", "laid down on wood", "transferred from wood")))



head(artwork_info)

my_colors <- c( "#140a02","#d6d5d3", "#e4d9c2", "#bda67e",  "#140a02","#5d5d5d",
                        "#73543e", "#eae0d4", "gold")
                        
medium_freq <- table(artwork_info$Medium_Category)


pie_chart <- ggplot(data = artwork_info, aes(x = "", fill = reorder(Medium_Category, -table(Medium_Category)[Medium_Category]))) +
  geom_bar(width = 1, color = "transparent") +
  scale_fill_manual(values = my_colors) +
  coord_polar("y", start=0) +
  theme_void() +
  theme(legend.position = "right") +
  labs(fill = NULL)


###############################
ggsave("pie_chart.png", plot = pie_chart, width = 8, height = 6, dpi = 300, bg = "transparent")
