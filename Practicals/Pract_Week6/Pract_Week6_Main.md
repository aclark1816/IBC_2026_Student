# This is the main file for the Week 6 Practical Assignment
## Problem #1: Debug This Code
### The objective of this problem was to examine the given code. I am expected to (1) explain each line and (2) use pdb to find the bug.
### The raw code is as follows:

  ```python

import pickle
# load dictionary with genetic code from pickle file
genetic_code = pickle.load(open("../data/genetic_code.pickle", "rb"))

# test case: desired amino acid sequence
# MEFSL[stop]
test_mRNA = "AUGGAAUUCUCGCUCUGAAGGUAA"

def get_amino_acids(mRNA):
    i = 0
    aa_sequence = []
    while (i + 3) < len(mRNA):
        codon = mRNA[i:(i + 3)]
        aa = genetic_code[codon]
        if aa == "Stop":
            break
        else:
            aa_sequence.append(aa)
        # advance to the next codon
        i = i + 4
    return "".join(aa_sequence)

print(get_amino_acids(test_mRNA))
# problem: the program returns MNLLEV instead of MEFSL!


```

## Problem #2: Gobbler Proteins
### The objective of this problem is to use the fixed version to analyze the first 15 amino acids of the Turkey_transcripts_15_coding.fafsa
