# Week 7 Practicals
## Objective: This week's practical instructs us to use the pubmed_results.txt and zipcodes_coordinates.txt files to complete three simple tasks. They are to (1) extract all US ZIP codes from the pubmed_results.txt file, to (2) create lists under zip_code, zip_long, zip_lat, and zip_count to document the longitudes, latitudes, and counts of each ZIP code, and to (3) visualize the data generated using a provided code.

### Note: A W7_Practical masterfile has also been uploaded.

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
### The previous code uses the re module to search for 5-digit sequences. From there, a zip_code list is created, which searches for pieces of data (zip_match) that fit the criteria of the zip_motif. This for loop ultimately stores all of the zip codes in the zip_code list.

## Question 2 Response:

  ```python
# Beginning of Question 2
# Import csv module
import csv

# Refresh zip_code variable
all_zips = list(zip_code)

# Create zip_code, zip_long, zip_lat, and zip_count lists
zip_code = []
zip_long = []
zip_lat = []
zip_count = []

# Open coordinates file
coord_main = open(r"c:\Users\Alexei Clark\Documents\IntroCompBiol\IntroBiolComp-2026\Python\zipcodes_coordinates.txt")

# csv module to parse the file
coord_reader = csv.reader(coord_main)

# For loop: Extract coordinates and counts for unique zip codes
for row in coord_reader:
    # Ensure the row actually has data to prevent an IndexError
    if len(row) >= 3:
        # Remove hidden spaces in the file, similar to previous practicals
        current_zip = row[0].strip()
        
        # Check if the zip code from the file exists in extracted text
        if current_zip in all_zips:
            
            # Adds zip codes not in zip_code variable, ensures that they're unique
            if current_zip not in zip_code:
                zip_code.append(current_zip)
                zip_lat.append(row[1].strip())
                zip_long.append(row[2].strip())
                
                # Count the occurrences directly from the all_zips list
                zip_count.append(all_zips.count(current_zip))
```

### The previous code follows a similar logic to the code for the first question. The csv module was included to parse through the data, and four lists were ultimately built to represent the zip code, the zip code count, and the zip code longitude and latitude. This was achieved through an overall for loop, with several nested if loops. The first if statement confirmed that the row had at least 3 elements, and the second two if statements determined if the current_zip was already found in every other zip that was observed (all_zips). If the zip was unique, then the zip_code, zip_lat, and zip_long lists were amended. However, regardless, zip_count was always amended to quantify the occurrence of each zip code.

## Question 3 Response:

  ```python
# Beginning of Question 3

import matplotlib.pyplot as plt
# let plots be produced within the IPython notebook
%matplotlib inline

plt.scatter(zip_long, zip_lat, s = zip_count, c = zip_count)
plt.colorbar()

# only continental us without Alaska
plt.xlim(-125,-65)
plt.ylim(23, 50)

# add a few cities for reference (optional)
ard = dict(arrowstyle="->")
plt.annotate('Los Angeles', xy = (-118.25, 34.05), 
               xytext = (-108.25, 34.05), arrowprops = ard)
plt.annotate('Palo Alto', xy = (-122.1381, 37.4292), 
               xytext = (-112.1381, 37.4292), arrowprops= ard)
plt.annotate('Cambridge', xy = (-71.1106, 42.3736), 
               xytext = (-73.1106, 48.3736), arrowprops= ard)
plt.annotate('Chicago', xy = (-87.6847, 41.8369), 
               xytext = (-87.6847, 46.8369), arrowprops= ard)
plt.annotate('Seattle', xy = (-122.33, 47.61), 
               xytext = (-116.33, 47.61), arrowprops= ard)
plt.annotate('Miami', xy = (-80.21, 25.7753), 
               xytext = (-80.21, 30.7753), arrowprops= ard)

params = plt.gcf()
plSize = params.get_size_inches()
params.set_size_inches( (plSize[0] * 3, plSize[1] * 3) )

plt.show()
```
### The previous code was copied from GitHub, as instructed. It simply displays a few reference point cities on the scatter plot.
