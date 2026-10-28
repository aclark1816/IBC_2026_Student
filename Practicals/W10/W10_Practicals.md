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

