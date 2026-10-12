#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Displays two lists: One to represent the 12 days of Christmas, and one to represent all of the gifts.
days = [
    "First", "Second", "Third", "Fourth", "Fifth", "Sixth",
    "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelfth"
]

gifts = [
    "A Partridge in a Pear Tree",
    "Two Turtle Doves",
    "Three French Hens",
    "Four Colly Birds",
    "Five Gold Rings",
    "Six Geese-a-Laying",
    "Seven Swans-a-Swimming",
    "Eight Maids-a-Milking",
    "Nine Ladies Dancing",
    "Ten Lords-a-Leaping",
    "Eleven Pipers Piping",
    "Twelve Drummers Drumming"
]

# Describes the days from index 0 to 11 (the 12 days of Christmas)
for i in range(len(days)):
    print(f"On the {days[i]} Day of Christmas, my true love sent to me:") # Prints index value for days, starting with "first"

    # Counts backward from the current day down to 0
    for j in range(i, -1, -1): # Ensures that the loop stops at index 0 and that the step size is down one
        # Add "And" before the partridge on the verse following the first one
        if i > 0 and j == 1:
            print(f"{gifts[j]}, and") # Displays gifts in descending order, starting with the newest gift of the present day
        else:
            print(gifts[j]) # On the first day, only the initial gift is displayed

    # Add a blank space between verses
    print("\n")

