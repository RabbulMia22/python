def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

print("Welcome to the Calculator!")
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

operation = input("Choose an operation (+, -, *, /): ")
if operation == "+":
    print("Result:", add(number1, number2))
elif operation == "-":
    print("Result:", subtract(number1, number2))
elif operation == "*":
    print("Result:", multiply(number1, number2))
elif operation == "/":
    try:
        print("Result:", divide(number1, number2))
    except ValueError as e:
        print("Error:", e)
else:
    print("Invalid operation selected.")
