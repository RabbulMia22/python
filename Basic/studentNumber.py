print("Welcome to the Student Number Program!")
name = input("Enter your name: ")

english = float(input("Enter your English score: "))
math = float(input("Enter your Math score: "))
science = float(input("Enter your Science score: "))
biology = float(input("Enter your Biology score: "))
history = float(input("Enter your History score: "))

total_score = english + math + science + biology + history
average_score = total_score / 5

if average_score >= 80:
    grade = "A"
elif average_score >= 70:
    grade = "B"
elif average_score >= 60:
    grade = "C"
elif average_score >= 50:
    grade = "D"
else: 
    grade = "F"
print("\n--- 📊 Student Report ---")
print(f"Student Name: {name}")
print(f"Your grade is: {grade}")
