number=int(input("Enter a number: "))
i=1
while i<=number:
    if number%i == 0:
        print(i,end=" ")
    i=i+1
