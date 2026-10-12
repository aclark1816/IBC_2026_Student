#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Create an empty dictionary to store counts
counts = {}

# Open and read the data file
with open(r"C:\Users\Alexei Clark\Documents\IntroCompBiol\IntroBiolComp-2026\Assignment1\Gesquiere2011_data.csv", "r") as x:
    for line in x: # For loop
        columns = line.split() # Columns are delineated by spaces
        if columns:
            ind_id = columns[0] # Establishes first column

            # Skips the maleID row, which isn't the purpose of this count
            if ind_id == "maleID":
                continue

            # Count the occurrences of each ID
            if ind_id in counts:
                counts[ind_id] += 1 # If a repeated ID occurs, then it is cumulatively added to the count
            else:
                counts[ind_id] = 1 # The count is stopped

# Save the results into a new CSV file
with open(r"C:\Users\Alexei Clark\Documents\IntroCompBiol\IntroBiolComp-2026\Assignment1\Num_samples.csv", "w") as x:
    x.write("maleID,sample_count\n")
    for ind_id, count in counts.items(): # Counts all pieces of data in the counts dictionary for each ind_id
        x.write(f"{ind_id},{count}\n") # The write function is simply used to format the table with individual ID in column 1 and the counts in column 2


# In[ ]:





# In[ ]:




