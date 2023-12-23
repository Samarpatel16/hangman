import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game.

        Parameters:
        - word_list (list): List of words to choose from.
        - num_lives (int): Number of lives the player has, default is 5.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = ['_']
        self.num_letters = 0
        self.list_of_guesses = set()

    def choose_random_word(self):
        """
        Choose a random word from the list and initialize game attributes accordingly.
        """
        self.word = random.choice(self.word_list)
        self.num_letters = len(set(self.word))
        self.word_guessed = ['_'] * len(self.word)

    def check_guess(self, guess):
        """
        Check if the guessed letter is in the word.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            self.update_word_guessed(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def update_word_guessed(self, guess):
        """
        Update the word_guessed list.

        Parameters:
        - guess (str): The letter guessed by the player.
        """
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
                self.num_letters -= 1

    def ask_for_input(self):
        """
        Ask the user for a valid letter input.
        """
        while True:
            guess = input("Guess a letter: ")

            if self.is_valid_guess(guess):
                self.check_guess(guess)
                self.list_of_guesses.add(guess)
                break

    def is_valid_guess(self, guess):
        """
        Check if the guess is a valid input.

        Parameters:
        - guess (str): The letter guessed by the player.

        Returns:
        - bool: True if the guess is valid, False otherwise.
        """
        if guess.isalpha() and len(guess) == 1 and guess not in self.list_of_guesses:
            return True
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
        return False

def play_game(word_list):
    """
    Run the Hangman game.

    Parameters:
    - word_list (list): List of words to choose from.
    """
    num_lives = 5
    game = Hangman(word_list)

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

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

if __name__ == "__main__":
    # Testing the Hangman class
    word_list = ["apple", "banana", "orange", "strawberry", "grape"]
    play_game(word_list)
    hangman_game = Hangman(word_list)
    hangman_game.choose_random_word()
    print("Chosen word:", hangman_game.word)
    hangman_game.ask_for_input()
    print("Word guessed:", hangman_game.word_guessed)
    print("List of guesses:", hangman_game.list_of_guesses)
    print("Number of unique letters:", hangman_game.num_letters)
    print("Number of lives:", hangman_game.num_lives)


