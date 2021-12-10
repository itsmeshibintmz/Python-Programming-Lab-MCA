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
