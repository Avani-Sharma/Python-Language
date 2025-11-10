# Build a simple calculator that takes two numbers and an operator symbol (+, -, *, /) as input from the user. Based on the operator provided, perform the corresponding arithmetic operation using if-elif-else and print the result.


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
    print("result: ", result)
elif operator == '-':
    result = num1 - num2
    print("result: ", result)
elif operator == '*':
    result = num1 * num2
    print("result: ", result)
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator entered.")
