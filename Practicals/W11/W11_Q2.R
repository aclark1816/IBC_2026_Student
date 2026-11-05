# The objective of this assignment is to recreate a designated figure listed in the week 11 markdown file

# Download libraries to read fasta files and tidyverse to design the histogram
library(seqinr)
library(tidyverse)

# Setting working directory
setwd("C:\\Users\\Alexei Clark\\Documents\\IntroCompBiol\\IntroBiolComp-2026\\IntroBiolComp-2026\\R\\DataFiles")

# Load dataset from the CDS FASTA file
fasta_data <- read.fasta("VA-8.all.cds.fasta")

# Extract the length of each sequence
gene_lengths <- lengths(fasta_data)

# Create a data frame containing unique gene IDs and their corresponding sequence lengths
unique_genes <- data.frame(
  Query_id = names(fasta_data),
  Query_length = gene_lengths
)

# Define bin intervals starting at 200
bin_interv <- c(200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, Inf)

# Define bin labels in order from left to right
bin_labels <- c("200-400", "400-600", "600-800", "800-1000", "1000-1200",  
                "1200-1400", "1400-1600", "1600-1800", "1800-2000", "2000-2200",  
                "2200-2400", "2400-2600", "2600-2800", "2800-3000", ">3000")

# Calculate bin data frequencies
binned_data <- unique_genes %>%
  
  # Determine the length of each datapoint for each unique gene via mutate function
  mutate(Length_Bin = cut(Query_length, breaks = bin_interv, labels = bin_labels, right = FALSE)) %>%
  
  # Count number of unique gene lengths within the confines of each bin to find frequency
  count(Length_Bin, name = "Frequency", .drop = FALSE) %>%
  
  # Complete list
  complete(Length_Bin = bin_labels, fill = list(Frequency = 0)) %>%
  
  # Order bin length (ascending from smallest to largest) with mutate function and explicit factor levels
  mutate(Length_Bin = factor(Length_Bin, levels = bin_labels))

# Plot overall data with ggplot2
# Establish x and y axes
ggplot(binned_data, aes(x = Length_Bin, y = Frequency, fill = Length_Bin)) +
  geom_bar(stat = "identity", show.legend = FALSE) +
  geom_text(aes(label = Frequency), vjust = -0.5, size = 3.5, fontface = "bold") +
  scale_fill_viridis_d(option = "plasma") +
  labs(
    x = "Length",
    y = "Frequency"
  ) +
  # For thematic purposes and to match the unique rainbow color of the target graph
  theme_classic() +
  theme(
    axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1, face = "bold", color = "black"),
    axis.text.y = element_text(face = "bold", color = "black"),
    axis.title = element_text(face = "bold", size = 12),
    panel.grid.major.y = element_blank()
  ) +
  scale_y_continuous(expand = expansion(mult = c(0, 0.12)))