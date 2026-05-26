import random

# Generate a random floating-point number
random5 = random.randint(0, 10)
attempt = 0
attempts = 0
while attempt != random5:
    attempt = int(input("Guess the number from one to ten: "))
    attempts += 1

    if attempt < random5:
        print("Too low. Guess higher")
    elif attempt > random5:
        print("Too high. Guess lower.")
    elif attempt == random5:
        print()
    else:
        print("Invalid input. Please try again.")
print(f"Congratulations! You guessed the number in {attempts} attempts.")