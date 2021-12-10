# Program to Display the given pyramid with the step number 
# accepted from the user.

# Get the number of steps from the user
stepnum=int(input("Enter a number:\n"))

# loop to display the pyramid
for i in range(0,stepnum): # loop to display the pyramid
    # loop to display the spaces
    for j in range(0,i+1):
        print((i+1)*(j+1), end=" ") # print the number
    print('\n')
