stepnum=int(input("Enter a number:\n"))
for i in range(0,stepnum):
    for j in range(0,i+1):
        print((i+1)*(j+1), end=" ")
    print('\n')
