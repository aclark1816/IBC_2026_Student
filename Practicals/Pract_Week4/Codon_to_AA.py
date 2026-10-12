#!/usr/bin/env python

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

# Matches codon to corresponding amino acid
# Prints out a chain of amino acids
codon_dict["CTA"] + "-" + codon_dict["GGA"] + "-" + codon_dict["GTG"] + "-" + codon_dict["ATT"] + "-" + codon_dict["ACG"]


