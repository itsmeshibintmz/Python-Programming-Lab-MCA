# Program to sum the series - ½ + ⅔ + ……. + n/(n+1)

# Getting the length of the series
limit=int(input("Enter the limit: "))

sum=0

# loop to calculate the sum
for i in range (1,limit+1): # looping from 1 to length of series
    sum+=i/(i+1) # finding the sum

# Displaying the sum
print("The sum of the series 1/2+2/3+3/4+...+n/n+1 is: ",sum)

""""
Algorithm
---------
Step 1: Get the length of the series
Step 2: Initialize the sum as 0 
Step 3: Loop from 1 to length of series
Step 4: Add the value of i/(i+1) to sum
Step 5: Display the sum
Step 6: End
"""
