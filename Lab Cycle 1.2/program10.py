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

""""
Algorithm
---------
Step 1: Get the number from the user
Step 2: Initialize sum as 0
Step 3: Store the number in a temporary variable
Step 4: Find the sum of the cube of each digit using adding the cube of each digit to the sum
Step 5: Compare the sum with the original number
Step 6: If both are equal then the number is an Amstrong number
Step 7: If not then the number is not an Amstrong number
Step 8: End
"""