### Week 9 Practicals Main File
# The following Markdown file displays the solutions to the first and second questions of today's practical.
## Question #1 Response:
  ```R
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
```

# To complete this task, the directory pathway was first saved, and a file_list variable was created to recognize all .txt files at the given directory path. A matrix was stored along with the various data types for each appropriate heading as well. Iteration i was set to 1, and a while loop was established with the condition of i never exceeding the number of files that were present, which was 60. A matrix was initiated, which stored the relevant metrics into each heading. The results were finally stored in the results dataframe, which was then saved as the "MatrixStats.tsv" file.
