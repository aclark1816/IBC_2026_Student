# This is the main file for the Week 6 Practical Assignment
## Problem #1: Debug This Code
### The objective of this problem was to examine the given code. I am expected to (1) explain each line and (2) use pdb to find the bug.
### The annotated raw code is as follows, which answers Question 1.

  ```python

import pickle # Line 1: This line imports the pickle function
# load dictionary with genetic code from pickle file
genetic_code = pickle.load(open("../data/genetic_code.pickle", "rb")) # Line 2: This line opens the file genetic_code.pickle, which is stored under the variable of genetic_code

# test case: desired amino acid sequence
# MEFSL[stop] # Line 3: This function declares the amino acid string.
test_mRNA = "AUGGAAUUCUCGCUCUGAAGGUAA" # Line 4: This function declares a sample mRNA stand under the test_mRNA variable.

def get_amino_acids(mRNA): # Line 5: The get_amino_acid() function is defined for the mRNA variable
    i = 0 # Line 6: Declares that variable i starts at 0
    aa_sequence = [] # Line 7: Declares that the amino acid sequence is displayed in brackets
    while (i + 3) < len(mRNA): # Line
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
### I then debugged this code using pdb. The corrected code is as follows:

  ```python
some code
```

### I corrected the code by doing x, y, z...
