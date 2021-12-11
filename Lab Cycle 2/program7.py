# Program to prompt the user for a list of integers. For all 
# values greater than 100, store ‘over’ instead.

def over100(list):
    for i in list:
        if i > 100:
            list[list.index(i)] = 'over'
    return list

print("Enter a list of integers separated by spaces: ")
list = [int(i) for i in input().split()]
print("List of intergers: ", list)
print("List of intergers greater than 100 replaced with over is: ", over100(list))