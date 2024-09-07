# Task # 1
print("Welcome to Calculator")

num1 = eval(input("Enter the value 1:- "))
num2 = eval(input("Enter the value 2:- "))
opr = input("Enter the operation to perform(+,-,*,/):- ")
if opr == "+":
    print(f"{num1} + {num2} = {(num1 + num2)}")
elif opr == "-":
    print(f"{num1} - {num2} = {(num1 - num2)}")
elif opr == "*":
    print(f"{num1} * {num2} = {(num1 * num2)}")
elif opr == "/":
    print(f"{num1} / {num2} = {(num1 / num2)}")
else:
    print("Invalid operation")
