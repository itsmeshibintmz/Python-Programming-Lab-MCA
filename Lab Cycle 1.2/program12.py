# Program to print the multiplication table of n, 
# where n is entered by the user.

# Getting the number to perform the multiplication
number=int(input("enter a number:\n"))

# looping through the range of numbers from 1 to number
for i in range(1,number+1):
    # calculating the product and printing the result 
    # in the form of multiplication table
    print(i,"x",number,"=",i*number)

""""
Algorithm
---------
Step 1: Get the number to perform the multiplication
Step 2: Loop through the range of numbers from 1 to number
Step 3: Calculate the product and print the result in the form of multiplication table (i.e. i*number=product)
Step 4: End
"""