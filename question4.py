#Write a Python program that takes two numbers and an operation (+, -, *, /) from the user.
#Perform the operation and print the result.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (eg. +, -, *, /): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
