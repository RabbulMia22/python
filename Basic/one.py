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


fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

for fruit in fruits:
    print(fruit)

letters = set("hello")
print(letters)

fruits = {"apple", "banana", "cherry"}
fruits.update(["date", "elderberry"])
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.discard("kiwi")  # No error if not found
print(fruits)

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print(fruits[4])
# print(fruits[5])
# print(fruits[6])
