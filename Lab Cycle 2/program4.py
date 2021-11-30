limit = int(input("Enter limit:\n"))
first = 0
second = 1
third = 1
print("Fibonocci Series upto",limit,"is")
print(first,end=' ')
for i in range(0,limit):
    print(third,end=' ')
    third=first+second
    first=second
    second=third
