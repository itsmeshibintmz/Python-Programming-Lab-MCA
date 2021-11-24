# Program to calculate salary of an employee

# Employee Details
nameOfEmployee=input("Enter name of the Employee\n")
basicPay=float(input("Enter Basic Pay\n"))
hra=(10/100)*basicPay
ta=(5/100)*basicPay
salary=basicPay+hra+ta
# Display Employee Details with Salary
print("Name of the Employee:",nameOfEmployee)
print("Basic Pay:",basicPay)
print("HRA:",hra)
print("TA:",ta)
print("Salary:",salary)