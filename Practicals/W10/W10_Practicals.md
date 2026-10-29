# Week 10 Practicals
## The Week 10 practical includes two problems. The first one involves determining whether most toads are right-handed or not. The second one involves analyzing assortative mating.

## Question #1:

### To complete this problem, the following code was used:

  ```R
# W10 - Toads
# Establish working directory
setwd("C:\\Users\\Alexei Clark\\Documents\\IntroCompBiol\\IntroBiolComp-2026\\IntroBiolComp-2026\\R\\DataFiles")

# Establish file path (use read.delim for .tsv files)
toad_hand <- read.delim("Toad_Handedness.tsv")

# Q1: Run a simulation to determine the hand preference for each toad

# Make sure columns are treated as numbers (this is simply to prevent errors when reading the code)
toad_hand$N_trials <- as.numeric(as.character(toad_hand$N_trials))
toad_hand$N_rights <- as.numeric(as.character(toad_hand$N_rights))

# Initialize an empty vector to store the conclusions for each toad
results_conclusion <- c()

# Loop through each row in your toad_hand data frame
for (i in 1:nrow(toad_hand)) {
  
  # Pull the specific number of trials and observed rights for the current toad
  n_trials <- toad_hand$N_trials[i]
  obs_rights <- toad_hand$N_rights[i] # Seen on frogs
  
  # Run a binomial simulation 10,000 times for this specific trial size under null hypothesis (p = 0.5)
  sim_rights <- rbinom(10000, size = n_trials, prob = 0.5) # Assuming equal chance
  
  # How often is a random simulation as extreme as or more extreme than the observed data?
  # n_trials divided by 2 to reflect the 2-sided nature of extremity
  p_value <- sum(abs(sim_rights - (n_trials / 2)) >= abs(obs_rights - (n_trials / 2))) / 10000
  
  # Determine handedness based on alpha = 0.05 and the direction of the bias
  if (p_value > 0.05) {
    conclusion <- "No handedness"
  } else if (obs_rights > (n_trials / 2)) {
    conclusion <- "Right handedness"
  } else {
    conclusion <- "Left handedness"
  }
  
  # Store the conclusion in conclusion vector
  results_conclusion[i] <- conclusion
}

# Attach results back to dataframe and view the final table
toad_hand$Handedness <- results_conclusion
toad_hand

# Q2: Using test 1 result, test the null hypothesis that a frog is equally likely to be right or left handed

# Sum total right-handed trials and total trials across all toads in the dataset
total_rights <- sum(toad_hand$N_rights)
total_trials <- sum(toad_hand$N_trials)

# Run a binomial test on the pooled trial data against a 50/50 probability (p = 0.5)
frog_binom_test_all <- binom.test(x = total_rights, n = total_trials, p = 0.5)

# View the test results
print(frog_binom_test_all)

# It is determined that frogs are not equally likely to be left or right handed

# Q3: Determine if male and female frogs are equally likely to be right handed

# Calculate the proportion of right-handed trials for each individual toad
toad_hand$Prop_rights <- toad_hand$N_rights / toad_hand$N_trials

# Calculate the observed test statistic (e.g., difference in mean proportion between Males and Females)
obs_diff <- mean(toad_hand$Prop_rights[toad_hand$Sex == "M"]) - 
  mean(toad_hand$Prop_rights[toad_hand$Sex == "F"])

# Set up the randomization test (e.g., 10,000 iterations)
nExp2 <- 10000
nExp2_diffs <- numeric(nExp2)

for (i in 1:nExp2) {
  # Shuffle the Sex labels across the rows
  shuffled_sex <- sample(toad_hand$Sex)
  
  # Calculate the test statistic using the shuffled sex assignments
  nExp2_diffs[i] <- mean(toad_hand$Prop_rights[shuffled_sex == "M"]) - 
    mean(toad_hand$Prop_rights[shuffled_sex == "F"])
}

# Calculate the two-sided p-value
p_value_sex <- sum(abs(nExp2_diffs) >= abs(obs_diff)) / n_perms

# Print results
cat("Observed Difference in Proportions (M - F):", obs_diff, "\n")
cat("Randomization Test p-value:", p_value_sex, "\n")

```
### Part 1 Response: Running this code should display a table as follows.
<img width="356" height="290" alt="image" src="https://github.com/user-attachments/assets/cfcaf0ea-fe82-4a26-ad4f-06c3f92f815a" />

### A binomial model was used to simulate the probability of each frog being right-handed, with the null hypothesis being p = 0.5. If a trial was more or less extreme with an assumed p-value = 0.05, then the frog was labeled as right- or left-handed depending on its position in the distribution. If a p-value = 0.05 was not observed, then no preference was assumed; The null hypothesis failed to be rejected.

### Part 2 Response: Running this code should display the following message.

<img width="554" height="169" alt="image" src="https://github.com/user-attachments/assets/b56941cf-c1ee-4d39-a598-994c799b7808" />

### The built-in R function to perform a binomial test was used. The only relevant information was that the p-value was very close to 0. This is indicative that, assuming the null hypothesis was correct, this simulation was an extremely rare outcome. More likely, however, one may conclude that frogs have a preference for being right-handed.

### Part 3 Response: Running this code reveals the following message.

<img width="527" height="71" alt="image" src="https://github.com/user-attachments/assets/29072919-df9f-45f7-9a09-a6c2c9d9de25" />

### The randomization test from the observed difference in proportions revealed a p-value of 0.4276; There is not sufficient evidence to reject the null hypothesis. It is therefore assumed that there is no variation between male and female frogs in hand preference.

### Overall Notes: This code utilized for loops and the sample function to randomize data. Additionally, hypothesis testing was used to confirm or deny assumptions made.

## Question 2:

### To complete this problem, the following code was used:
  ```R
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
```
### Part 1 Response: To complete this code, a function was created to allow a generic taxon to be parsed from the file and return the mean r value. Additional amendments were made to ignore NAN values, should they be present.

### Part 2 Response: The following information was produced from the script.
<img width="524" height="75" alt="image" src="https://github.com/user-attachments/assets/eaea4b6b-d71c-41e3-8726-845713f85375" />

### The script utilizes 50,000 simulations (via a for loop and the sample function) to compare the observed mean to other likely outcomes. Ultimately, the randomization tests suggested that higher means were not likely. Overall, this script compiled from the first part, which returned the mean value for r.

### Part 3 Response: The following information was produced from the script.
<img width="462" height="371" alt="image" src="https://github.com/user-attachments/assets/11a4966b-3892-4aa8-ac8f-ce4f81f461b1" />

<img width="433" height="445" alt="image" src="https://github.com/user-attachments/assets/e6d6c013-347a-4bbb-baab-a15b35e142a4" />

### The script essentially performs the function for part 2 for every single taxon. This method utilizes the creation of a function, composed similarly to the script developed in question 2. From there, a list was created to perform the new function on every single taxon.




