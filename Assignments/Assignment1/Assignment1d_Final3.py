#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Create an empty dictionary to store counts
counts = {}

# Open and read the data file
with open(r"C:\Users\Alexei Clark\Documents\IntroCompBiol\IntroBiolComp-2026\IntroBiolComp-2026\IBC_2026_Student\Assignments\Assignment1\Gesquiere2011_data.csv", "r") as x:
    for line in x: # For loop
        # Use split() to automatically handle tabs and spaces in the file
        columns = line.strip().split()
    
        if columns:
            # Remove any accidental quotes and grab the first column
            ind_id = columns[0].strip('"\'') 
        
            # Skip the header row ("maleID") or any non-numeric rows safely
            if ind_id == "maleID" or not ind_id.isdigit():
                continue
            
            # Count the occurrences of each ID
            if ind_id in counts:
                counts[ind_id] += 1 # If a repeated ID occurs, then it is cumulatively added to the count
            else:
                counts[ind_id] = 1 # The count is initialized

# Save the results into a new CSV file
with open(r"C:\Users\Alexei Clark\Documents\IntroCompBiol\IntroBiolComp-2026\IntroBiolComp-2026\IBC_2026_Student\Assignments\Assignment1\Num_samples.csv", "w", newline="") as x:
    x.write("maleID,sample_count\n")

    # Sort the IDs numerically
    for ind_id in sorted(counts.keys(), key=int): # Forces python to treat all values as integers
        count = counts[ind_id]
        x.write(f"{ind_id},{count}\n") # Writes the individual ID and its count


# In[ ]:





# In[ ]:





# In[ ]:




