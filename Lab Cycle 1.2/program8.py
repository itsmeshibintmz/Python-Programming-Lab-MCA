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
