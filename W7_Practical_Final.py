#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import re module
import re


# In[3]:


# Beginning of Question 1
# Open ZIP code file
zip_main = open(r"c:\Users\Alexei Clark\Documents\IntroCompBiol\IntroBiolComp-2026\Python\zipcodes_coordinates.txt", "r") 


# In[4]:


# Search for 5 number sequence
zip_motif = r'(\d{5})\b'

# Create zip_code list
zip_code = []


# In[5]:


# For loop: Find all numbers that fit the "zip code motif" and extend the list
for line in zip_main:
    zip_match = re.findall(zip_motif, line)
    zip_code.extend(zip_match) # All values are stored in the zip_code list


# In[6]:


# Print zip_code
print(zip_code)


# In[10]:


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


# In[11]:


# Print each list to confirm their existence
print(zip_code)
print(zip_long)
print(zip_lat)
print(zip_count)


# In[13]:


# Beginning of Question 3

import matplotlib.pyplot as plt
# let plots be produced within the IPython notebook
get_ipython().run_line_magic('matplotlib', 'inline')

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


# In[97]:


get_ipython().run_line_magic('pip', 'install matplotlib')

