# Program to generate Fibonacci series of N terms

# Getting the limit upto which fibonocci numbers 
# need to print
limit = int(input("Enter limit:\n"))

# Initializing the first two fibonacci numbers
first = 0
second = 1
third = 1

print("Fibonocci Series upto",limit,"is")

# Printing the first two fibonacci numbers
print(first,end=' ')

# Looping till the limit and printing the fibonacci numbers
for i in range(0,limit):
    print(third,end=' ')
    third=first+second
    first=second
    second=third
