# Program to find the greatest number among three numbers.

# Getting inputs from the user
number1 = int(input("Enter first number\n"))
number2 = int(input("Enter second number\n"))
number3 = int(input("Enter third number\n"))

# Checking if the first number is greater than the second number 
# and the third number
if number1>number2 and number1>number3:
    # if yes, printing the first number
    print("Greatest number is",number1)
# Checking if the second number is greater than the third number 
# and the first number
elif number2>number1 and number2>number3:
    # if yes, printing the second number
    print("Greatest number is",number2)
else:
    # if no, printing the third number
    print("Greatest number is",number3)

""""
Algorithm
---------
Step 1: Get three numbers from the user
Step 2: Check if the first number is greater than the second number and the third number
Step 3: If yes, print the first number
Step 4: If not, check if the second number is greater than the third number and the first number
Step 5: If yes, print the second number
Step 6: If not, print the third number
Step 7: End
"""