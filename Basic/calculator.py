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
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Select operation (1-4): ")
if operation == "1":
    print("Result:", add(num1, num2))
elif operation == "2":
    print("Result:", subtract(num1, num2))
elif operation == "3":
    print("Result:", multiply(num1, num2))
elif operation == "4":
    try:
        print("Result:", divide(num1, num2))
    except ValueError as e:
        print("Error:", e)
else:
    print("Invalid operation selected.")
