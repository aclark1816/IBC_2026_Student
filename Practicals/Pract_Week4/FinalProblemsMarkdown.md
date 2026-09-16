# Week 4 Final Problems Practical
## Assignment #1: About You
### To complete this assignment, I used the following code:

```python
# The following code aims to print an "all about you" panel, with each characteristic saved as a variable
# Saving each characteristic as a variable

name = "Alexei Clark" # Name
fav_color = "Blue" # Favorite Color
fav_activ = "Playing Video Gamees" # Favorite Activity
fav_anim = "Kiwi" # Favorite Animal

# Print out full panel, separating text and variables

# Use \n to separate lines

print("My Name: " + name +
     "\nMy Favorite Color: " + fav_color +
     "\nMy Favorite Activity: " + fav_activ +
     "\nMy Favorite Animal: " + fav_anim)

    My Name: Alexei Clark
    My Favorite Color: Blue
    My Favorite Activity: Playing Video Games
    My Favorite Animal: Kiwi
    
```

### To complete this task, I simply created a variable for each characteristic. 
### I then used the /n command to delineate separate lines within the scope of onee print() function.

## Assignment #2: Codon to Amino Acid

```python
# The following script intends to complete the "Codon to Amino Acids" portion of this
# week's practicals

# Codon Dictionary
codon_dict = {
    'AAA': 'Lys', 'AAC': 'Asn', 'AAG': 'Lys', 'AAT': 'Asn', 'ACA': 'Thr', 'ACC': 'Thr', 'ACG': 'Thr', 'ACT': 'Thr', 
    'AGA': 'Arg', 'AGC': 'Ser', 'AGG': 'Arg', 'AGT': 'Ser', 'ATA': 'Ile', 'ATC': 'Ile', 'ATG': 'Met', 'ATT': 'Ile', 
    'CAA': 'Gln', 'CAC': 'His', 'CAG': 'Gln', 'CAT': 'His', 'CCA': 'Pro', 'CCC': 'Pro', 'CCG': 'Pro', 'CCT': 'Pro', 
    'CGA': 'Arg', 'CGC': 'Arg', 'CGG': 'Arg', 'CGT': 'Arg', 'CTA': 'Leu', 'CTC': 'Leu', 'CTG': 'Leu', 'CTT': 'Leu', 
    'GAA': 'Glu', 'GAC': 'Asp', 'GAG': 'Glu', 'GAT': 'Asp', 'GCA': 'Ala', 'GCC': 'Ala', 'GCG': 'Ala', 'GCT': 'Ala', 
    'GGA': 'Gly', 'GGC': 'Gly', 'GGG': 'Gly', 'GGT': 'Gly', 'GTA': 'Val', 'GTC': 'Val', 'GTG': 'Val', 'GTT': 'Val', 
    'TAA': 'Stp', 'TAC': 'Tyr', 'TAG': 'Stp', 'TAT': 'Tyr', 'TCA': 'Ser', 'TCC': 'Ser', 'TCG': 'Ser', 'TCT': 'Ser', 
    'TGA': 'Stp', 'TGC': 'Cys', 'TGG': 'Trp', 'TGT': 'Cys', 'TTA': 'Leu', 'TTC': 'Phe', 'TTG': 'Leu', 'TTT': 'Phe'
}

# String of focus
codon_str = "CTA GGA GTG ATT ACG"

# Splitting codon string by spaces
# New variable stored under split_codon
codon_str.split(" ")

    ['CTA', 'GGA', 'GTG', 'ATT', 'ACG']

# Matches codon to corresponding amino acid
# Prints out a chain of amino acids
codon_dict["CTA"] + "-" + codon_dict["GGA"] + "-" + codon_dict["GTG"] + "-" + codon_dict["ATT"] + "-" + codon_dict["ACG"]

    'Leu-Gly-Val-Ile-Thr'
```
## To complete this portion of the assignment, I first created the codon dictionary (codon_dict) using the codon and corresponding amino acid
## as the key and value, respectively. After creating and separating a codon string (codon_str), I searched for each codon in the dictionary.
## Finally, I added dashes to print out the chain of amino acids in a more presentable manner.

