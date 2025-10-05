import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = input(f"Attempt {attempts + 1}/{max_attempts}. Make a guess: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        break