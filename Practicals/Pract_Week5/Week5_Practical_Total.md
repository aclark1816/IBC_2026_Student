# Week 5 Practicals

## Assignment #1: Baking a Cake
### The objective of this task was to describe baking a cake in pseudocode. As such, pseudocode for this assignment is only included in this master file, rather than in a separate ### file.
### ---------------------------------------------------------------------------------------------
### Pseudocode Script

  ```Python

# Ingredients list
i = ["Flour," "Eggs", "Milk", "Butter", "Sugar"]
      
# Add all ingredients in order
for x in i:
print(x)

# Hypothetical mix function for ingredients, saves as ing_mixed variable
ing_mixed = mix(i)

# while loop for determining if cake batter is cooked
cookTemp = 400
t = 20
cakeDone = False

while batterSticktoKinfe == True
      if cakeDone == False:
            t = t + 1
      else butterSticktoKnife == False:
            print("Your cake is done!")

  ```

### Firstly, I made a list i, listed them in order with a for loop, and mixed the ingredients in the ing_mixed variable. Then, I created a while loop, with the start time (t) at 20 minutes and a cookTemp variable at 400 degrees Fahrenheit. With the cakeDone variable set to False, and the batterSticktoKnife variable set to True, I made the loop conditional on ending when the batterSticktoKnife variable is false. If that isn't the case, then the cake variable would be assumed to be false.

## Assignment #2: Fizz Buzz
### The objective of this assignment is to write pseudocode and actual code for the FizzBuzz game.
### ---------------------------------------------------------------------------------------------------------------------------
### Pseudocode Script:

  ```Python


# for loop for printing fizz, buzz, and fizzbuzz
x = 1

for x in range(100): 
     if x % 15 == 0: # Least common denominator for numbers divisible by 3 and 5
        x = x + 1
        print(x, "fizzbuzz")
    elif x % 3 == 0:
        print(x, "fizz")
        x = x + 1
    elif x % 5 == 0:
        print(x, "buzz")
        x = x + 1

```

### The previous pseudocode runs the Fizz Buzz game for numbers 1-100. Firstly, the for loop checks if x is divisible by 15, which indicates that the number is divisible by 3 and 5. Then, it checks if x is divisble by 3, before checking if it's divisible by 5. This is laid out such that there won't be three print statements for x if it's divisible by 3 and 5.
--------------------------------------------------------------------------------------------------------------------------------------
### Python Script

  ```Python

# for loop for printing fizz, buzz, and fizzbuzz
for x in range(1, 101):
    if x % 15 == 0: # Divisible by 5 and 3
        print(x, "fizzbuzz")
    elif x % 3 == 0: # Divisible by 3
        print(x, "fizz")
    elif x % 5 == 0: # Divisible by 5
        print(x, "buzz")
    else:
        print(x) # Prints number if it is not divisible by 5 or 3

```







```

