# Program to Display the given pyramid with the step number 
# accepted from the user.

# Get the number of steps from the user
stepnum=int(input("Enter a number:\n"))

# loop to display the pyramid
for i in range(0,stepnum): 
    # loop to print the value with spaces
    for j in range(0,i+1):
        print((i+1)*(j+1), end=" ") # print the number
    print('\n')

""""
Algorithm
---------
Step 1: Get the step number from the user
Step 2: Loop to display the pyramid ranging from 0 to step number
Step 3: Inner Loop to print the value with spaces
Step 4: Print the number (i+1)*(j+1) with spaces at the end
Step 5: End of inner loop
Step 6: print the new line
Step 7: End of outer loop
Step 8: End
"""
