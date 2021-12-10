# Program to calculate the average of first n natural 
# using for loop

# Getting input from the user
number = int(input("Enter number: "))

# Initializing the sum
sum = 0

# loop to calculate the sum
for num in range(1, number + 1, 1): # looping from 1 to number
    sum = sum + num # adding the number to the sum

# calculating the average
average = sum / number

# printing the result
print("Average of ", number, "numbers is: ", average)

""""
Algorithm
---------
Step 1: Get the number from the user
Step 2: Initialize the sum as 0
Step 3: Loop from 1 to number and add the each number to the sum
Step 4: Calculate the average by sum/number
Step 5: Print the result
Step 6: End
"""