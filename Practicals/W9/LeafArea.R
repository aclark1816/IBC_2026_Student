# Once installed
library(EBImage)

# Task #2: Write a for loop that processes all images using the getArea function

# Set directory
dir <- "C:\\Users\\Alexei Clark\\Documents\\IntroCompBiol\\IntroBiolComp-2026\\IntroBiolComp-2026\\R\\DataFiles\\leafarea"

# Define the getArea function outside the loop
getArea <- function(f) {
  i <- normalize(readImage(f))
  i <- i + 0.05 # adjust brightness
  # extract the three RGB channels
  dr <- as.vector(i[,, 1])
  dg <- as.vector(i[,, 2])
  db <- as.vector(i[,, 3])
  # adjust the channels to enhance green and reduce red
  d <- dr + 2 * db + dg / 1.5
  # set background (white) to black
  d[d >= 1] <- NA
  # set everything else to white to create a mask
  d[d < 1] <- 1
  d[is.na(d)] <- 0
  d <- matrix(d, nrow = dim(i)[1])
  mask <- Image(d)    
  # erode and dilate to remove small objects
  kern <- makeBrush(size = 1, shape = "disc", step = FALSE)
  mask <- dilate(mask, kern)
  ## find object of less than 250 pixels and delete them
  m <- as.vector(mask[mask != 0])
  X <- table(m)
  todel <- names(X[X < 250])
  if (length(todel) > 0) mask <- rmObjects(mask, as.numeric(todel))
  ## apply gaussian blur to smooth contours
  mask <- gblur(mask, s = 5, r = 7)
  mask[mask >= 0.4] <- 1
  mask[mask < 0.4] <- 0
  # calculate the projected leaf area
  pic.shape <- computeFeatures.shape(mask)
  return(pic.shape[1])
}

# Task #2: Write a for loop that processes all images using the getArea function
image_list <- list.files(path = dir, pattern = "\\.JPG$", ignore.case = TRUE, full.names = TRUE)

# Initialize results data frame to store area and file names together
results_df <- data.frame(
  LeafArea = numeric(),
  FileName = character(),
  stringsAsFactors = FALSE
)

# Using the getArea function, create a data frame
for (file_path in image_list) {
  area_value <- getArea(file_path)
  
  results_df <- rbind(results_df, data.frame(
    LeafArea = area_value,
    FileName = basename(file_path)
  ))
}


# Task #3: Calculate growth/difference in time

# Clean up file names to extract Time and PlantID
results_df$Time <- substr(results_df$FileName, 1, 2)
results_df$PlantID <- gsub("^t[12]_|\\..*", "", results_df$FileName)

# Separate into t1 and t2 subsets
t1 <- subset(results_df, Time == "t1", c("PlantID", "LeafArea"))
t2 <- subset(results_df, Time == "t2", c("PlantID", "LeafArea"))

# Merge them together by PlantID to align rows for subtraction
growth_df <- merge(t1, t2, by = "PlantID", suffixes = c("_T1", "_T2"))

# Calculate growth and average
growth_df$Growth <- growth_df$LeafArea_T2 - growth_df$LeafArea_T1

# Show the average growth
mean_growth <- mean(growth_df$Growth, na.rm = TRUE)
cat("\nAverage leaf growth between time points:", mean_growth, "\n")

# Task #4: Save as a comma-separated file
# Reset directory
setwd("C:\\Users\\Alexei Clark\\Documents\\IntroCompBiol\\IntroBiolComp-2026\\IntroBiolComp-2026\\W9")
write.csv(growth_df, file = "LeafAreaGrowth.csv")
