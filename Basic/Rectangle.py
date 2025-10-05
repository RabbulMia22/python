length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Exiting the loop.")
        break

    # Convert input to integer
    number = int(user_input)   # ✅ conversion

    if number < 0:
        print("Negative number, try again.")
        continue

    print(f"You entered: {number}")



