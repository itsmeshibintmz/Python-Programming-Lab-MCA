num1=int(input("enter first number:\n"))
num2=int(input("Enter second number:\n"))
while num1!=num2:
  if num1>num2:
    num1-=num2
  else:
    num2-=num1
print("GCD is",num1)
