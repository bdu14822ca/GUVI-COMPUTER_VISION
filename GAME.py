
import random

def computer_guesses(low, high):
    print(f"Think of a number between {low} and {high}. I'll try to guess it!")
    input("Press Enter when ready...")
    attempts = 0
    while True:
        guess = random.randint(low, high)
        attempts += 1
        print(f"My guess: {guess}")
        feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").lower()
        if feedback == 'c':
            print(f"I guessed your number in {attempts} tries!\n")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

def user_guesses(number):
    attempts = 0
    while True:
        guess = input("Your guess: ")
        if not guess.isdigit():
            print("Please enter a number.")
            continue
        guess = int(guess)
        attempts += 1
        if guess == number:
            print(f"Correct! You guessed my number in {attempts} tries!")
            break
        print("Too low." if guess < number else "Too high.")

def guessing_game():
    number = random.randint(1, 10)
    print("Welcome to the guessing game!\n")
    computer_guesses(1, 10)
    print("Now it's your turn to guess my number!")
    user_guesses(number)

guessing_game()

