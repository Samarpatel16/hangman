##Task 1: Create the Class


import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def choose_random_word(self):
        """Choose a random word from the list."""
        return random.choice(self.word_list)

if __name__ == "__main__":
    # Testing the Hangman class
    word_list = ["apple", "banana", "orange", "strawberry", "grape"]
    hangman_game = Hangman(word_list)
    print("Chosen word:", hangman_game.word)
    print("Word guessed:", hangman_game.word_guessed)
    print("Number of unique letters:", hangman_game.num_letters)
    print("Number of lives:", hangman_game.num_lives)
    print("List of guesses:", hangman_game.list_of_guesses)


##Task2: Create methods for running the checks


import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def choose_random_word(self):
        """Choose a random word from the list."""
        return random.choice(self.word_list)

    def check_guess(self, guess):
        """Check if the guessed letter is in the word."""
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")

    def ask_for_input(self):
        """Ask the user for a valid letter input."""
        while True:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

if __name__ == "__main__":
    # Testing the Hangman class
    word_list = ["apple", "banana", "orange", "strawberry", "grape"]
    hangman_game = Hangman(word_list)
    print("Chosen word:", hangman_game.word)
    hangman_game.ask_for_input()
    print("Word guessed:", hangman_game.word_guessed)
    print("List of guesses:", hangman_game.list_of_guesses)

##Task 3: Define what happens if the letter is in the word


    import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def choose_random_word(self):
        """Choose a random word from the list."""
        return random.choice(self.word_list)

    def check_guess(self, guess):
        """Check if the guessed letter is in the word."""
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")

    def ask_for_input(self):
        """Ask the user for a valid letter input."""
        while True:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

if __name__ == "__main__":
    # Testing the Hangman class
    word_list = ["apple", "banana", "orange", "strawberry", "grape"]
    hangman_game = Hangman(word_list)
    print("Chosen word:", hangman_game.word)
    hangman_game.ask_for_input()
    print("Word guessed:", hangman_game.word_guessed)
    print("List of guesses:", hangman_game.list_of_guesses)
    print("Number of unique letters:", hangman_game.num_letters)


##Task 4: What happens if the letter is not in the word


    import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_random_word()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def choose_random_word(self):
        """Choose a random word from the list."""
        return random.choice(self.word_list)

    def check_guess(self, guess):
        """Check if the guessed letter is in the word."""
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """Ask the user for a valid letter input."""
        while True:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

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


##Task 7: Refactor and Optimise

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
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
            print(f"Good guess! '{guess}' is in the word.")
            self.update_word_guessed(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def update_word_guessed(self, guess):
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
