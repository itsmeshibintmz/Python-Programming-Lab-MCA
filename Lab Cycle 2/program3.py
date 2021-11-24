# Program to find the factorial of a number.

# Prompt user for input
number= int(input("Enter a number\n"))
factorial=1
# Calculate the factorial
for i in range(1,number+1):
    factorial=factorial*i
# Display the factorial
print("Factorial of",number,"is",factorial)
