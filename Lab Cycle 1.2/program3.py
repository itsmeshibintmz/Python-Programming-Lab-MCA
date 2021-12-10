# Program to find the factorial of a number.

# Getting input from the user
number= int(input("Enter a number\n"))
factorial=1

# Calculating the factorial
for i in range(1,number+1):
    factorial=factorial*i

# Displaying the factorial
print("Factorial of",number,"is",factorial)
