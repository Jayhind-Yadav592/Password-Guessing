
import random

easy_words = ["apple", "trains", "banana", "tiger", "india"]
medium_words = ["python", "monkey", "bottle", "laptop", "planet"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Welcome to the Password Guessing Game 🎯")
print("Choose difficulty: easy | medium | hard")

level = input("Enter difficulty: ").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice! Defaulting to easy.")
    secret = random.choice(easy_words)

attempts = 0

print(f"💡 Hint: The word starts with '{secret[0]}'")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"🎉 Congratulations! You guessed the word in {attempts} attempts.")
        break
    else:
        print("❌ Wrong guess. Try again!")
