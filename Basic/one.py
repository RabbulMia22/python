def my_function():
    print("Hello from my_function!")
my_function()

number = 17
if number > 10:
    print("You are a child")
elif number > 18:
    print("You are an adult")
else:
    print("You are a teenager")


fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]  # List of fruits this is list called a list

for fruit in fruits:
    print(fruit)

letters = set("hello")
print(letters)

fruits = {"apple", "banana", "cherry"} # This is a set
fruits.update(["date", "elderberry"])
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.discard("kiwi")  # No error if not found
print(fruits)


numbers = (1, 2, 3, 4, 5)  # This is a tuple
print(numbers)
print(numbers[0])  # Accessing elements in a tuple
numbers.count(2)  # Counting occurrences of an element
print(numbers.count(2))

person = {"name": "Alice", "age": 30, "city": "New York"}  # This is a dictionary
print(person)
print(person["name"])  # Accessing values in a dictionary
person["age"] = 31  # Modifying values in a dictionary
print(person)

numbers = [1, 2, 3, 4, 5, 10, 40, 100]  # This is a list
maximub = max(numbers)  # Finding the maximum value in a list
print(maximub)
heightNumber = numbers[0]
for number in numbers:
    if number > heightNumber:
        heightNumber = number
print(heightNumber)