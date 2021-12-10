# Program to find whether the given number is an 
# Amstrong number or not using while loop

# Get the number from the user
number=int(input("Enter a number: "))

# Initialize sum
sum=0
temp=number # Store the number in a temporary variable

# Find the sum of the cube of each digit
while temp>0: # Loop until the number is 0
    digit=temp%10 # Get the last digit
    sum+=digit**3 # Add the digit to the sum
    temp//=10 # Remove the last digit

# compare the sum with the original number
if number==sum: 
    # if both are equal then the number is an Amstrong number
    print(number,"is an Armstrong number")
else:
    # if not then the number is not an Amstrong number
    print(number,"is not an Armstrong number")
