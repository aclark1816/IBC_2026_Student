#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Allows for arguments to be accessed from terminal
import sys

# The filename and ID are inputted on the command line
filename = sys.argv[1] # Declare first argument
target_id = sys.argv[2] # Declare second argument

count = 0

# With loop to open and read file
with open(filename, 'r') as f:
    for line in f:
        # Strip each line and split it by spaces
        columns = line.strip().split()

        # Compare the first column to the target ID
        if columns[0] == target_id:
            count += 1 # Continue the loop

# Print the overall count
print(count)

