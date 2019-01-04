#Hangman
#Jacob Jensen
#11/18
import time
import random

HANGMAN = (
"""
-------
|     |
|
|
|
|
|
|
|
|
|
|
----------------
"""
,
"""
-------
|     |
|     O
|
|
|
|
|
|
|
|
|
----------------

"""
,
"""
-------
|     |
|     O
|    -+-
|
|
|
|
|
|
|
|
----------------
"""
,
"""
-------
|     |
|     O
|    -+-
|   / | 
|
|
|
|
|
|
|
----------------
"""
,
"""
-------
|     |
|     O
|    -+-
|   / | \\
|
|
|
|
|
|
|
----------------
"""
,
"""
-------
|     |
|     O
|    -+-
|   / | \\
|     |   
|    /
|
|
|
|
|
----------------
"""
,
"""
-------
|     |
|     O
|    -+-
|   / | \\
|     |   
|    / \\
|
|
|
|
|
----------------
""")


MAX_WRONG = len(HANGMAN)-1
WORDS = ("float","double","if","else","string","python","false","true","comment","def")
#initialize variables
word = random.choice(WORDS)# the word to be guessed
so_far = "-" * len(word)#one dash for each letter in the word to be guessed
wrong = 0 #number of wrong guesses
used = [] #letters already guessed

print("welcom to hangman. Good luck!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\n you've used the following letters:\n", used)
    print("\n so far, the word is :\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.lower()
    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("enter your guess: ")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print("\nYes!", guess, "is in the word!")
        new = ""

        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
            so_far = new

        else:
            print("\nSorry," ,guess,"isn't in the word.")
            wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[WRONG])
    print("\nyou've been hanged!")
else:
    print("\nyou guessed it!")

print("\nthe word was", word)

input("\n\nPress the enter key to exit.")



























































