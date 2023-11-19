##file milestone_3.py: 
#This file will contain the code for the second milestone.
#In Python, Lists are used to store multiple data in a single variable. In this task, we are going to create a list of words.

import random

word_list = ["apple", "banana", "orange", "strawberry", "grape"]
secret_word = random.choice(word_list)

def check_guess(guess):
    """Check if the guessed letter is in the word."""
    # Step 2
    guess = guess.lower()

    # Step 3
    if guess in secret_word:
        # Step 4
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    """Ask the user for a valid letter input."""
    while True:
        # Step 2
        guess = input("Guess a letter: ")

        # Step 3
        if guess.isalpha() and len(guess) == 1:
            # Step 4
            check_guess(guess)
            break
        else:
            # Step 5
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 3
ask_for_input()