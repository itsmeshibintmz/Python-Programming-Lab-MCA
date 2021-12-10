# Program to calculate the average of first n natural 
# using for loop

# Getting input from the user
number = int(input("Enter number: "))

# Initializing the sum
sum = 0

# loop to calculate the sum
for num in range(1, number + 1, 1): # looping from 1 to number
    sum = sum + num # adding the number to the sum

# calculating the average
average = sum / number

# printing the result
print("Average of ", number, "numbers is: ", average)