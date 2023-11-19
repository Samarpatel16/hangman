##file milestone_2.py: 
#This file will contain the code for the first milestone.
#In Python, Lists are used to store multiple data in a single variable. In this task, we are going to create a list of words.

import random

def choose_random_word(word_list):
    """Choose a random word from the list."""
    return random.choice(word_list)

def get_user_guess():
    """Prompting the user to enter a single letter and validate the input. If they don't an Oops message appears"""
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Oops! That is not a valid input.")

# Below are the variable definitions for the list of fruits.
# First a print statement of the list of favorite fruits
# Second the user must choose a random fruit
# Third is the users input of a single letter and the code will validate this input.

def main():
    favorite_fruits = ["apple", "banana", "orange", "strawberry", "grape"]
    
    
    print("Favorite Fruits:", favorite_fruits)
    
    
    word = choose_random_word(favorite_fruits)
    print("Randomly chosen fruit:", word)
    
    
    guess = get_user_guess()
    
    
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")

if __name__ == "__main__":
    main()