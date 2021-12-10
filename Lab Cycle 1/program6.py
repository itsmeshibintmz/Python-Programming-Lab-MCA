# Program to check whether a given number is even or not

# Getting the input from the user
numberToCheck=int(input("Enter the number to be checked\n"))

# Checking whether the number is even or not
if numberToCheck%2==0:
    # If yes, printing the message : "The number is even"
    print("Number is even")
else:
    # If no, printing the message : "The number is not even"
    print("Number is not even")

""""
Algorithm
---------
Step 1: Get the input from the user
Step 2: Check whether the number is even or not
        if number % 2 == 0:
            go to step 3
        else:
            go to step 4
Step 3: Print the message : "The number is even"
Step 4: Print the message : "The number is not even"
Step 5: End

"""