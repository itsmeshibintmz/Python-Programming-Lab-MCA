# Program to find the greatest number from three numbers.

# Get the three numbers from the user
number1 = int(input("Enter first number\n"))
number2 = int(input("Enter second number\n"))
number3 = int(input("Enter third number\n"))
# Check which is the greatest number and display it
if number1>number2 and number1>number3:
    print("Greatest number is",number1)
elif number2>number1 and number2>number3:
    print("Greatest number is",number2)
else:
    print("Greatest number is",number3)
