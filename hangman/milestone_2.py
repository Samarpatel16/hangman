##file milestone_2.py: 
#This file will contain the code for the first milestone.
#In Python, Lists are used to store multiple data in a single variable. In this task, we are going to create a list of words.

#Task 1: Define the list of possible words

# Below is a list of fruits
favorite_fruits = ["apple", "banana", "orange", "strawberry", "grape"]

word_list = favorite_fruits

print(word_list)


# Using the same list of fruits. I want to select a fruit at random
import random

word_list = ["apple", "banana", "orange", "strawberry", "grape"]

word = random.choice(word_list)

print(word)

# I now want to ask for an input of a single letter only

guess = input("Enter a single letter: ")

# I want this input to confirm that a single letter has been entered. If not an error message will appear.

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
