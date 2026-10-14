# Week 8 Practical
### The objective of this assignment is to analyze a disease risk file and to clean a dataset using the R programming language.
## Question 1 Response:

  ```R
# The following code analyzes the H938_Euro_chr6.geno file.

# Filepath of H938_Euro_chr6.geno, separates columns with spaces
df <- read.table("C:\\Users\\Alexei Clark\\Documents\\IntroCompBiol\\IntroBiolComp-2026\\IntroBiolComp-2026\\R\\DataFiles\\H938_Euro_chr6.geno", sep = "", h = T)

# View dataframe
View(df)

# View dataframe structure
str(df)

# Convert columns A1 and A2 to factors
df$A1 <- as.factor(df$A1)
df$A2 <- as.factor(df$A2)

#################################
# Question 1, Part 1
#################################

# Sum of last three columns (per site)
Total_Individuals_NoSum <- df$nA1A1 + df$nA1A2 + df$nA2A2

# Find the maximum sample size at a single site
total_NoSum <- max(Total_Individuals_NoSum, na.rm = TRUE)
print(total_NoSum) # 124 people were sampled

#################################
# Question 1, Part 2
#################################

# Sum of last three columns (per site)
Total_Individuals <- rowSums(df[, c("nA1A1", "nA1A2", "nA2A2")], na.rm = TRUE)

# Find the maximum sample size at a single site
total <- max(Total_Individuals, na.rm = TRUE)
print(total) # 124 people were sampled

##################################
# Question 1, Part 3
##################################

# Filepath for SNP_risks.csv
df_SNP <- read.csv("C:\\Users\\Alexei Clark\\Documents\\IntroCompBiol\\IntroBiolComp-2026\\IntroBiolComp-2026\\R\\DataFiles\\SNP_risks.csv")

# View file
View(df_SNP)

# Join the risk column to the end of the six columns
df_risks <- df_SNP$Risk

# Name the column "Risk" as you bind it
df_compl <- cbind(df, Risk = df_risks)
View(df_compl)

##################################
# Question 1, Part 4
##################################

# Average heterozygous individuals at risk
avg_het_risk <- function(data) {
  mean(data$nA1A2[data$Risk == "Risk"], na.rm = TRUE)
}

mean_het_risk <- avg_het_risk(df_compl)
print(mean_het_risk) # 37.31 individuals are heterozygous at sites associated with disease risk

# Average heterozygous individuals NOT at risk
avg_het_nonrisk <- function(data) {
  mean(data$nA1A2[data$Risk == "Non-Risk"], na.rm = TRUE)
}

mean_het_nonrisk <- avg_het_nonrisk(df_compl)
print(mean_het_nonrisk) # 36.97 individuals are heterozygous at sites not associated with diseasee risk

```
