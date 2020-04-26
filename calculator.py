
num1 = float(input("Please enter a number: "))
op = input("Enter operator: ")
num2 = float(input("Please enter another number: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
