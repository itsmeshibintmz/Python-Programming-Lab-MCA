# Program to calculate salary of an employee

# Getting the basic salary details of the employee
nameOfEmployee=input("Enter name of the Employee\n")
basicPay=float(input("Enter Basic Pay\n"))

# Calculating the HRA, DA and Salary
hra=(10/100)*basicPay
ta=(5/100)*basicPay
salary=basicPay+hra+ta

# Printing the salary details
print("Name of the Employee:",nameOfEmployee)
print("Basic Pay:",basicPay)
print("HRA:",hra)
print("TA:",ta)
print("Salary:",salary)

""""
Algorithm
---------
Step 1: Getting the basic details of the employee
Step 2: Calculating the HRA, DA and Salary using formulas
        HRA = 10% of basic pay
        TA = 5% of basic pay
        Salary = Basic Pay + HRA + TA
Step 3: Printing the salary details
Step 4: End
"""