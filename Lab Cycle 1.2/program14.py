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
	
""""
Algorithm
---------
Step 1: Take the number of rows as input from the user.
Step 2: print * in each row incremented by 1 till the limit in nested loop.
Step 3: print * in each row decremented by 1 till the limit in nested loop.
Step 4: End
"""