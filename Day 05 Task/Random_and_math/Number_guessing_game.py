import random
import math

secret = random.randint(1, 50)

print("Guess the number between 1 and 50")

for attempt in range(1, 6):
    guess = int(input("Attempt " + str(attempt) + ": "))

    if guess == secret:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        difference = math.fabs(secret - guess)
        print("Wrong guess!")
        print("You are", difference, "away from the correct number.")

if guess != secret:
    print("Sorry! The correct number was", secret)