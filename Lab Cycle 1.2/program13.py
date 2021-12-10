# Program to sum the series - ½ + ⅔ + ……. + n/(n+1)

# Getting the length of the series
limit=int(input("Enter the limit: "))

sum=0

# loop to calculate the sum
for i in range (1,limit+1): # looping from 1 to length of series
    sum+=i/(i+1) # finding the sum

# Displaying the sum
print("The sum of the series 1/2+2/3+3/4+...+n/n+1 is: ",sum)
