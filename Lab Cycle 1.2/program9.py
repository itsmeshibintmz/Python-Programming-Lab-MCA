# Program to print the reverse of a number 
# using while loop

# Getting the number from the user
num=int(input("Enter a number: "))

# Initializing the variables
temp=num
reverse=0

# Checking if the number is negative
while(temp>0):
    # Getting the last digit of the number
    remainder=temp%10
    # Multiplying the last digit with 10^n
    reverse=(reverse*10)+remainder
    # Removing the last digit from the number
    temp=temp//10

# Printing the reverse of the number
print("Reverse of the number",num,"is:",reverse)
