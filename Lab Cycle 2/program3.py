# Write a program to find the factorial of a number.
number= int(input("Enter a number\n"))
factorial=1
for i in range(1,number+1):
    factorial=factorial*i
print("Factorial of",number,"is",factorial)
