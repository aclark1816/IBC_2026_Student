# Week 7 Practicals
## Objective: This week's practical instructs us to use the pubmed_results.txt and zipcodes_coordinates.txt files to complete three simple tasks. They are to (1) extract all US ZIP codes from the pubmed_results.txt file, to (2) create lists under zip_code, zip_long, zip_lat, and zip_count to document the longitudes, latitudes, and counts of each ZIP code, and to (3) visualize the data generated using a provided code.

## Note: A W7_Practical masterfile has also been uploaded.

## Question 1 Response:

  ```python
# Import re module
import re

# Beginning of Question 1
# Open ZIP code file
zip_main = open(r"c:\Users\Alexei Clark\Documents\IntroCompBiol\IntroBiolComp-2026\Python\zipcodes_coordinates.txt", "r")

# Search for 5 number sequence
zip_motif = r'(\d{5})\b'

# Create zip_code list
zip_code = []

# For loop: Find all numbers that fit the "zip code motif" and extend the list
for line in zip_main:
    zip_match = re.findall(zip_motif, line)
    zip_code.extend(zip_match) # All values are stored in the zip_code list

# Print zip_code
print(zip_code)
```
