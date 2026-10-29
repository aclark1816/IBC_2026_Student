# W10 - Assortative Mating
# Establish working directory
setwd("C:\\Users\\Alexei Clark\\Documents\\IntroCompBiol\\IntroBiolComp-2026\\IntroBiolComp-2026\\R\\DataFiles")

# Use read.delim or specify sep = "\t" since the file uses tabs instead of commas
assort_mating <- read.delim("Jiang2013_data.csv", header = TRUE)

# Print column names to confirm they split properly into multiple columns
print(colnames(assort_mating))

# Q1: Write a function that takes the desired Taxon and returns the mean r value
get_mean_r <- function(data, taxon_name, taxon_col = "Taxon", r_col = "r") {
  
  # Subset the data for the requested taxon
  subset_data <- data[data[[taxon_col]] == taxon_name, ]
  
  # Calculate the mean r value, ensuring it's numeric and removing NAs
  mean_r <- mean(as.numeric(subset_data[[r_col]]), na.rm = TRUE)
  
  return(mean_r)
}

# Example: Fish
results <- get_mean_r(assort_mating, taxon_name = "Fish")
print(results)

# Q2: Randomization test for mean r value
# Determine the sample size of taxon
target_subset <- assort_mating[assort_mating$Taxon == "Fish", ]
sample_size <- nrow(target_subset)

# Calculate your observed mean r for that taxon
obs_mean_r <- mean(as.numeric(target_subset$r), na.rm = TRUE)

# 50,000 randomized trials
nTrials <- 50000
sim_mean_r <- numeric(nTrials)

# Ensure the entire 'r' column is numeric
all_r_values <- as.numeric(assort_mating$r)

for (i in 1:nTrials) {
  # Randomly sample 'sample_size' values from the entire dataset's r column
  random_sample_r <- sample(all_r_values, size = sample_size, replace = TRUE)
  
  # Calculate and store the mean of this random sample
  sim_mean_r[i] <- mean(random_sample_r, na.rm = TRUE)
}

# Calculate the p-value for higher than mean r-value
p_value_r <- sum(sim_mean_r >= obs_mean_r)/nTrials

# Print the results
cat("Observed Mean r:", obs_mean_r, "\n")
cat("Randomization Test p-value (Higher Mean):", p_value_r, "\n")

# Q3: Repeat procedure with all taxa
# Establish overall function
run_taxon_randomization <- function(data, taxon_name, nTrials = 50000) {
  # Subset data for the specified taxon
  target_subset <- data[data$Taxon == taxon_name, ]
  sample_size <- nrow(target_subset)
  
  # Check if taxon exists
  if (sample_size == 0) {
    return(paste("No data found for taxon:", taxon_name))
  }
  
  # Calculate the observed mean r for that specific taxon
  obs_mean_r <- mean(as.numeric(target_subset$r), na.rm = TRUE)
  
  # Initialize vector for simulation results
  sim_mean_r <- numeric(nTrials)
  all_r_values <- as.numeric(data$r)
  
  # Randomized simulation
  for (i in 1:nTrials) {
    # Randomly sample with replacement from the entire dataset
    random_sample_r <- sample(all_r_values, size = sample_size, replace = TRUE)
    
    # Store the mean of this random sample
    sim_mean_r[i] <- mean(random_sample_r, na.rm = TRUE)
  }
  
  # Calculate the p-value for observing a mean r as high or higher
  p_value_r <- sum(sim_mean_r >= obs_mean_r) / nTrials
  
  # Print the formatted results
  cat("--- Randomization Test Results for Taxon:", taxon_name, "---\n")
  cat("Sample Size:", sample_size, "\n")
  cat("Observed Mean r:", obs_mean_r, "\n")
  cat("Randomization Test p-value (Higher Mean):", p_value_r, "\n\n")
  
  # Return results as a list if you want to store them
  return(list(taxon = taxon_name, n = sample_size, obs_mean = obs_mean_r, p_val = p_value_r))
}

# Identify all taxa
table(assort_mating$Taxon)

# Reproduce the "fish" example for all taxa by calling the previously-made function
# Automatically loop through all unique taxa shown in your dataset
all_taxa <- unique(assort_mating$Taxon)

# Call the function for each taxon in the list
results_list <- lapply(all_taxa, function(t) {
  run_taxon_randomization(assort_mating, taxon_name = t, nTrials = 50000)
})