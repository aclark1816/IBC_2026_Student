# Define directory and list files WITH full paths
dir_path <- "C:\\Users\\Alexei Clark\\Documents\\IntroCompBiol\\IntroBiolComp-2026\\IntroBiolComp-2026\\R\\DataFiles\\Saavedra2013"
file_list <- list.files(path = dir_path, pattern = "\\.txt$", full.names = TRUE)

# Store matrix results: Confirm each variable type
results <- data.frame(
  FileName = character(),
  Rows = integer(),
  Columns = integer(),
  PropOne = numeric(),
  PropZero = numeric(),
  stringsAsFactors = FALSE
)

# While loop to process files
# Start position at file 1
i <- 1 
while(i <= length(file_list) && i <= 60) {
  
  # Get the full path for the current file
  file_path <- file_list[i]
  
  # Read matrix
  mat <- as.matrix(read.table(file_path, header = FALSE))
  
  # Compute required metrics
  file_name <- basename(file_path)
  num_rows <- nrow(mat)
  num_cols <- ncol(mat)
  prop_one <- mean(mat == 1, na.rm = TRUE)
  prop_zero <- mean(mat == 0, na.rm = TRUE)
  
  # Store results
  results <- rbind(results, data.frame(
    FileName = file_name,
    Rows = num_rows,
    Columns = num_cols,
    PropOne = prop_one,
    PropZero = prop_zero
  ))
  
  # Increment the correct counter (i) to avoid infinite loop
  i <- i + 1
}

setwd("C:\\Users\\Alexei Clark\\Documents\\IntroCompBiol\\IntroBiolComp-2026\\IntroBiolComp-2026\\W9")
write.table(results, "MatrixStats.tsv", sep = "\t")
