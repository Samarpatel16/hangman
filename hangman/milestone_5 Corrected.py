import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initializes the Hangman game.

        Parameters:
        - word_list (list): A list of words for the game.
        - num_lives (int): Number of lives the player starts with. Default is 5.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.choose_random_word()  # Assign the result of choose_random_word to self.word
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.guesses_made = set()  # Renamed list_of_guesses to make it more accurate

    def choose_random_word(self):
        """
        Chooses a random word from the list.

        Returns:
        - str: The chosen word.
        """
        return random.choice(self.word_list)  # Return the chosen word

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates the game state accordingly.

        Parameters:
        - guess (str): The guessed letter.
        """
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            self.update_word_guessed(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            print("Word guessed:", self.word_guessed)  # Display word_guessed after each incorrect guess

    def update_word_guessed(self, guess):
        """
        Updates the word_guessed list based on the correct guess.

        Parameters:
        - guess (str): The correct guessed letter.
        """
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
                self.num_letters -= 1

    def ask_for_input(self):
        """Ask the user for a valid letter input."""
        while True:
            guess = input("Guess a letter: ")

            if self.is_valid_guess(guess):
                self.check_guess(guess)
                self.guesses_made.add(guess)  # Update the set of guesses
                break

    def is_valid_guess(self, guess):
        """
        Checks if the guess is a valid input.

        Parameters:
        - guess (str): The guessed letter.

        Returns:
        - bool: True if the guess is valid, False otherwise.
        """
        if guess.isalpha() and len(guess) == 1 and guess not in self.guesses_made:
            return True
        elif guess in self.guesses_made:
            print("You already tried that letter!")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
        return False

def play_game(word_list):
    """
    Plays the Hangman game.

    Parameters:
    - word_list (list): A list of words for the game.
    """
    num_lives = 5
    game = Hangman(word_list)
    print(game.word)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.choose_random_word()  # Reset the game for a new word
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

if __name__ == "__main__":
    # Testing the Hangman class
    word_list = ["apple", "banana", "orange", "strawberry", "grape"]
    play_game(word_list)
