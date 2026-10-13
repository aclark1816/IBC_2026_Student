#!/usr/bin/env python
# coding: utf-8

# In[32]:


file_path = r"C:\Users\Alexei Clark\Documents\IntroCompBiol\IntroBiolComp-2026\IntroBiolComp-2026\IBC_2026_Student\Assignments\Assignment1\origin.txt"
output_path = r"C:\Users\Alexei Clark\Documents\IntroCompBiol\IntroBiolComp-2026\IntroBiolComp-2026\IBC_2026_Student\Assignments\Assignment1\sterility_output.txt"

# Open the file in binary mode (rb) to read text and split into lines
with open(file_path, "rb") as f:
  binary_content = f.read()

# Split the binary content into a list of lines
lines = binary_content.splitlines()

# Convert a lowercase version of the whole text for counting
text = binary_content.lower()

# Since binary mode uses the byte object, the prefix b must be placed in front of terms
sterility_count = text.count(b"sterility")
isolation_count = text.count(b"isolation")

# Search for 3 lines before and after sterility
keyword = b"sterility"

# Open an output file to save your results
with open(output_path, "w", encoding="utf-8") as out:

  # For loop to track index i, which indexes every line in the origin.txt file
  for i in range(len(lines)):
      line = lines[i]
  
      # Check if the lowercase version of the line contains your keyword
      if keyword in line.lower():
          match_msg = f"A match was found at line {i + 1}\n"
          print(match_msg.strip())
          out.write(match_msg)
      
          # Define the range: 3 lines before (start) to 3 lines after (end)
          start = max(0, i - 3) # 0 prevents a negative number, i-3 refers to three lines earlier
          end = min(len(lines), i + 4) # Slicing stops right before line 4, so the next three lines are displayed
      
          # For loop for j in range of start and end parameters
          for j in range(start, end):
              # Decodes strings safely from binary (utf-8 formatting) with error replacement
              decoded_line = lines[j].decode('utf-8', errors='replace').rstrip()

              # Prints that a keyword match is found when j is exactly equal to i, but for all other values in the range, they are denoted as surrounding lines
              if j == i:
                  ster_file = f"Keyword Match ({j + 1}): {decoded_line}\n"
              else:
                  ster_file = f"Surrounding Lines ({j + 1}): {decoded_line}\n"
          
              print(ster_file.strip())
              out.write(ster_file)
          
          divider = "-" * 40 + "\n" # Prints "-" 40 times to delineate results
          print(divider.strip()) # Divider separates by spaces
          out.write(divider) # Writes divider into results

# Output path changed
output_path = r"C:\Users\Alexei Clark\Documents\IntroCompBiol\IntroBiolComp-2026\IntroBiolComp-2026\IBC_2026_Student\Assignments\Assignment1\isolation_output.txt"

# Search for 3 lines before and after isolation
keyword = b"isolation"

# Open an output file to save your results
with open(output_path, "w", encoding="utf-8") as out:

  # For loop to track index i, which indexes every line in the origin.txt file
  for i in range(len(lines)):
      line = lines[i]
  
      # Check if the lowercase version of the line contains your keyword
      if keyword in line.lower():
          match_msg = f"A match was found at line {i + 1}\n"
          print(match_msg.strip())
          out.write(match_msg)
      
          # Define the range: 3 lines before (start) to 3 lines after (end)
          start = max(0, i - 3) # 0 prevents a negative number, i-3 refers to three lines earlier
          end = min(len(lines), i + 4) # Slicing stops right before line 4, so the next three lines are displayed
      
          # For loop for j in range of start and end parameters
          for j in range(start, end):
              # Decodes strings safely from binary (utf-8 formatting) with error replacement
              decoded_line = lines[j].decode('utf-8', errors='replace').rstrip()

              # Prints that a keyword match is found when j is exactly equal to i, but for all other values in the range, they are denoted as surrounding lines
              if j == i:
                  isol_file = f"Keyword Match ({j + 1}): {decoded_line}\n"
              else:
                  isol_file = f"Surrounding Lines ({j + 1}): {decoded_line}\n"
          
              print(isol_file.strip())
              out.write(isol_file)
          
          divider = "-" * 40 + "\n" # Prints "-" 40 times to delineate results
          print(divider.strip()) # Divider separates by spaces
          out.write(divider) # Writes divider into results
