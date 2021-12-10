# Program to find gcd of 2 numbers using while loop

# Getting inputs from the user
num1=int(input("enter first number:\n"))
num2=int(input("Enter second number:\n"))

# checking if the numbers are equal
while num1!=num2:
  # finding the smaller number
  if num1>num2: 
    num1-=num2 # subtracting the smaller number from the larger number
  else:
    num2-=num1 # subtracting the smaller number from the larger number

print("GCD is",num1) # printing the gcd

""""
Algorithm
---------
Step 1: Get the two numbers from the user
Step 2: Check if the numbers are equal, if not, continue until they are equal
Step 3: If the numbers are not equal
          Check if the first number is greater than the second number
            go to step 4
            Repeat step 4 until the numbers are equal
          Else
            go to step 5
            Repeat step 5 until the numbers are equal
Step 4: Subtract the smaller number from the larger number
Step 5: Subtract the larger number from the smaller number
Step 6: Print the GCD result          
"""
