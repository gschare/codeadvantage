import random

number = random.randint(1, 10)
print("I'm thinking of a number...")
guesses = 10
while guesses > 0:
    guess = input("Guess the number: ")
    guess = int(guess)
    if number == guess:
        print("Correct! You won.")
        break
    elif number > guess:
        print("Incorrect. Guess higher.")
    else:
        print("Incorrect. Guess lower.")
    guesses = guesses - 1

if guesses == 0:
    print("You lost!")
    print("The correct number is", number)
