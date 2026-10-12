#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Open the file in binary mode (rb). This is to allow for the code to read any unorthodox characters.
with open(r"C:\Users\Alexei Clark\Documents\IntroCompBiol\IntroBiolComp-2026\Assignment1\origin.txt", "rb") as f:
    text = f.read().lower() # Reads the text in only lowercase letters. This is to get around the case requirements.

# Since binrary mode uses the byte object, the prefix b must be placed in front of any terms that are to be searched
sterility_count = text.count(b"sterility")
isolation_count = text.count(b"isolation")

# Variables must explicitly be considered strings to ensure variable uniformity
print(f"The word 'sterility' appears " + str(sterility_count) + " times.")
print(f"The word 'isolation' appears " + str(isolation_count) + " times.")

