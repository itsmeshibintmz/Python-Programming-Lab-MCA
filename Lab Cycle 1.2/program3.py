# Program to find the factorial of a number.

# Getting input from the user
number= int(input("Enter a number\n"))
factorial=1

# Calculating the factorial
for i in range(1,number+1):
    factorial=factorial*i

# Displaying the factorial
print("Factorial of",number,"is",factorial)

""""
Algorithm
---------
Step 1: Get the number to find the factorial of
Step 2: Initialize the factorial variable to 1
Step 3: Loop from 1 to the number
Step 4: Multiply the factorial variable by the current value of the loop
Step 5: Display the factorial
Step 6: End
"""
