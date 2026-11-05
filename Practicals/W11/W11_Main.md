# Week 11 Practical
## Problem 1: Recreating Figure 1 without the expand.grid() function

### The figure that is to be recreated without the expand.grid() function is shown as follows:

<img width="281" height="245" alt="image" src="https://github.com/user-attachments/assets/73ed6e00-4cf4-4f7b-919a-50a79f5ed83b" />

### The code for the original figure is as follows:

```R
grid <- expand.grid(1:5, 6:1)
plot(grid, pch = 0:30, cex = 2.5,
     yaxt = "n", xaxt = "n",
     ann = FALSE, xlim = c(0.5, 5.25),
     ylim = c(0.5, 6.5))

grid2 <- expand.grid(seq(0.6, 4.6, 1), 6:1)
text(grid2$Var1[1:26], grid2$Var2[1:26], 0:25)
```

### The revised code for recreating this figure without the expand.grid() function is shown as follows:

```R
# x and y = Shape coordinates
x <- rep(1:5, times = 6) # Times repeats the sequence
y <- rep(6:1, each = 5) # Each repeats the number

plot(x, y, pch = 0:30, cex = 2.5,
     yaxt = "n", xaxt = "n",
     ann = FALSE, xlim = c(0.5, 5.25),
     ylim = c(0.5, 6.5))

# Positions teext to the left of the points (0.6 is closer to the left than 1, for instance)
x2 <- rep(seq(0.6, 4.6, 1), times = 6)
y2 <- rep(6:1, each = 5)

# Labels the 26 coordinates 0 through 25
text(x2[1:26], y2[1:26], 0:25)

```

### Although less efficient, this code avoids expand.grid() function be separating each "grid" into the x and y components. The x-axis shape coordinate is determined by running through the sequence from 1-5 for a total of 6 times (i.e. starting from the top left corner, the places shapes 0-4 on the top row, before repeating with shapes 5-9 on the lower row). This is complemented by the y-axis shape coordinate, which places the first five shapes on row 6 (the uppermost), before descending. This allows for them to form organized rows and columns when plotted. The shapes are then able to be labeled via a similar mechanism, with x2 and y2 coordinates representing the label locations. These positions are quite similar, except the x2 coordinate is shifted slightly to the left to ensure that the numbers aren't covering up the shapes. The final line of code actually writes out the lists based on their relative position from 0-25.

### The final graph is as follows:
<img width="281" height="241" alt="image" src="https://github.com/user-attachments/assets/9aa14454-6269-4641-83cb-c29e4289367f" />


## Problem 2: Recreating a figure in scientific literature
### The original figure is displayed as follows:
<img width="239" height="194" alt="image" src="https://github.com/user-attachments/assets/b725988e-5219-4ab0-b4bd-236229f2857d" />

### It is from the paper titled "Whole-genome sequencing of _Verticillium alfalfae_ strain Va8." The link for this paper is: https://www.nature.com/articles/s41597-026-08555-8. The relevant file that contains this data is also included in this folder.

### The new figure is displayed as follows:

<img width="413" height="387" alt="image" src="https://github.com/user-attachments/assets/6b799aae-0da2-40b7-a12b-878d55a30e3f" />

### It should be noted that it was difficult to identify the specific dataset to use for recreating the graph. Instead, I believe that I used a modified dataset that shows a similar structure to the original but with additional data points. However, after scouring all of the raw data provided, I could not find a suitable alternative. If the exact dataset were to be found, then the file would simply be replaced.

## Question Answer:

### Overall, I think that this graph is quite effective. It's not cluttered and is quite readable. However, I found the color palette to be distracting, since the fluorescent rainbow colors distracted me from the overall trend of the data. Overall, though, it effectively conveyed the data in a concise, simple way, which I believe is most important in scientific literature.

### The overall script is as follows:

```R
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
ggplot(binned_data, aes(x = Length_Bin, y = Frequency, fill = Length_Bin)) +
  geom_bar(stat = "identity", show.legend = FALSE) +
  geom_text(aes(label = Frequency), vjust = -0.5, size = 3.5, fontface = "bold") +
  scale_fill_viridis_d(option = "plasma") +
  labs(
    x = "Length",
    y = "Frequency"
  ) +
  theme_classic() +
  theme(
    axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1, face = "bold", color = "black"),
    axis.text.y = element_text(face = "bold", color = "black"),
    axis.title = element_text(face = "bold", size = 12),
    panel.grid.major.y = element_blank()
  ) +
  scale_y_continuous(expand = expansion(mult = c(0, 0.12)))
```
### After importing the necessary libraries to read the FASTA file and tidyverse to design the histogram, the working directory was set, and the VA-8.all.cds.fasta master file was loaded. A simple dataframe was created containing the unique gene names along with their lengths. The bin intervals and labels were then established for the histogram, and using piping, the dataframe was mutated into binned_data. The frequency of each gene length was recorded and ordered from smallest to largest. Finally, a histogram plot was made, with various modifications to fit in line with the theme of the original histogram. Although there are large chunks of code in this portion, they served the purpose of modifying the aesthetics of the histogram, rather than function.
