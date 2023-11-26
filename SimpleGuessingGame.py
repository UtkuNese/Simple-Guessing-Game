# Simple Guessing Game

import random

print("Welcome to the Simple Guessing Game!")

number = random.randint(1, 50)
guess_attempts = 5

while True:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < number:
        print("Enter a larger number.")
    else:
        print("Enter a smaller number.")
    
    guess_attempts -= 1
    
    if guess_attempts == 0:
        print("Out of guess attempts! The correct answer was", number, ".")
        break