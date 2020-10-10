# imports / libraries

# variables
max_wrongs = 7
wrongs = 0
used = []
hangman = (
"""
    ________
   |        |
   |
   |
   |
   |
   |
   |
   |
___|________
""",
"""
    ________
   |        |
   |        o
   |
   |
   |
   |
   |
   |
___|________
""",
"""
    ________
   |        |
   |        o
   |        |
   |
   |
   |
   |
   |
___|________
""",
"""
    ________
   |        |
   |        o
   |       /|
   |       
   |
   |
   |
   |
___|________
""",
"""
    ________
   |        |
   |        o
   |       /|\
   |       
   |
   |
   |
   |
___|________
""",
"""
    ________
   |        |
   |        o
   |       /|\
   |       /
   |
   |
   |
   |
___|________
""",
"""
    ________
   |        |
   |        o
   |       /|\
   |       / \
   |
   |
   |
   |
___|________
"""
    )

# main thing we wanna do
print("Welcome to the game Hangman...")
word = input("Enter the secret word: ").upper() # Player 1 input
print("\n"*40)

word_so_far = "_"*len(word)

while wrongs < max_wrongs and word_so_far != word:
    print(hangman[wrongs]) # print hangman
    print("Word so far: ", word_so_far)
    print("Letter used: ", ", ".join(used))    # come back to this for printing nicer

    guess = input("Enter a letter: ").upper() # Player 2 input
    
    while guess in used:
        print("Try again, you've already guessed that letter...")
        guess = input("Enter a letter: ").upper()

    used.append(guess)

    if guess in word:
        new = ""
        for index in range(len(word)):
            if guess == word[index]:
                new += guess
            else:
                new += word_so_far[index]
        word_so_far = new
    else:
        print("Incorrect!")
        wrongs += 1

print("The secret word was: ", word)
if wrongs == max_wrongs:
    print("Player 1 wins! Congratulations on picking a difficult word!")
else:
    print("Player 2 wins! Good job on guessing the word!")

input("(press enter to quit)")
