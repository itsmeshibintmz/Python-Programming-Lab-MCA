limit=int(input("Enter the limit: "))
sum=0
for i in range (1,limit+1):
    sum+=i/(i+1)
print("The sum of the series 1/2+2/3+3/4+...+n/n+1 is: ",sum)
