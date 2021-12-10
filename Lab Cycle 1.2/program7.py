# Program to generate all factors of a number 
# using while loop

# Get the number from the user
number=int(input("Enter a number: "))

i=1

print("The factors of",number,"are:")
# loop to find the factors
while i<=number:
    if number%i == 0: # check if i is factor of number
        print(i,end=" ") # if yes, print i
    i=i+1 # increment i

""""
Algorithm
---------
Step 1: Get the number from the user
Step 2: Initialize i to 1
Step 3: While i is less than or equal to number
            Check if number is divisible by i
                If yes, print i
            Increment i
Step 4: End
"""