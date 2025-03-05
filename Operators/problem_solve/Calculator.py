# Calculator Using Operators
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /, %, **, //): ")

if operator == '+':
    print(f"Result: {a + b}")
elif operator == '-':
    print(f"Result: {a - b}")
elif operator == '*':
    print(f"Result: {a * b}")
elif operator == '/':
    print(f"Result: {a / b}")
elif operator == '%':
    print(f"Result: {a % b}")
elif operator == '**':
    print(f"Result: {a ** b}")
elif operator == '//':
    print(f"Result: {a // b}")
else:
    print("Invalid operator")
