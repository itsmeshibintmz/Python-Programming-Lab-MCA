# Program to Construct following pattern using nested loop
""" 
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

# Getting the limit of the pattern
number=int(input("Enter a number: "))

# loop to print the pattern till the limit
for i in range(number): # loop for rows 
    for j in range(i): # loop for columns
        print ('* ', end="") # printing the pattern with spaces
    print('') # printing the pattern with new line

# loop for printing the pattern in reverse
for i in range(number,0,-1): # loop for rows
    for j in range(i): # loop for columns
        print('* ', end="") # printing the pattern with spaces
    print('') # printing the pattern with new line
	