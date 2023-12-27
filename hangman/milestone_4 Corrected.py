
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
# Task 1: Create the class
        self.word_list = word_list
        self.num_lives = num_lives
        self.choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = set()

    def choose_random_word(self):
        """Choose a random word from the list."""
        self.word = random.choice(self.word_list)

    def check_guess(self, guess):
        """Check if the guessed letter is in the word."""
        guess = guess.lower()

        if guess in self.word:
# Task 2: Check whether the guessed letter is the word
            print(f"Good guess! '{guess}' is in the word.")
            self.update_word_guessed(guess)
        else:
# Task 4: Define what happens if the letter is not in the word
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def update_word_guessed(self, guess):
# Task 3: Create a function to run the checks
        """Update the word_guessed list."""
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
                self.num_letters -= 1

    def ask_for_input(self):
        """Ask the user for a valid letter input."""
        while True:
            guess = input("Guess a letter: ")

            if guess.isalpha() and len(guess) == 1 and guess not in self.list_of_guesses:
                self.check_guess(guess)
                self.list_of_guesses.add(guess)
                break
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

if __name__ == "__main__":
    # Testing the Hangman class
    word_list = ["apple", "banana", "orange", "strawberry", "grape"]
    hangman_game = Hangman(word_list)
    print("Chosen word:", hangman_game.word)
    hangman_game.ask_for_input()
    print("Word guessed:", hangman_game.word_guessed)
    print("List of guesses:", hangman_game.list_of_guesses)
    print("Number of unique letters:", hangman_game.num_letters)
    print("Number of lives:", hangman_game.num_lives)
