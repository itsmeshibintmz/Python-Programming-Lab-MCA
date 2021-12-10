# Program to find sum of all items in a list

# Getting input from the user
list_of_numbers = input("Enter a list of numbers separated by commas: ")

sum=0

# Converting the input string to a list
for i in list_of_numbers.split(','):
    # Converting the string to an integer and adding it to the sum
    sum = sum + int(i)

# Printing the sum
print("The sum of the numbers is: ", sum)

""""
Algorithm
---------
Step 1: Get the list input from the user
Step 2: Convert the input string to a list
Step 3: Initialize the sum variable to 0
Step 4: Loop through the list and add each item to the sum
Step 5: Print the sum
Step 6: End
"""