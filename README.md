# Hangman
Hangman is a classic game in which a player thinks of a word, and the other player tries to guess that word within a certain number of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This implementation features the computer thinking of a word, and the user attempting to guess it.

Currently, I have completed the following milestones that help to build this project:

Milestone 1: Setting up the Environment
- This was the first step where I set up the Github repository.

Milestone 2: Creating the variables for the game
- Using conditions and the users input. Once an answer is input there is a validation check.

Milestone 3: Check that the guessed characters are in the word
- Checking that the guessed letter is actually inside of the word.

Milestone 4: Creating the game class
- Using OOP to develop the Hangman game.

Milestone 5: Putting it all together
- The final milestone where all components come together to create a playable Hangman game.

### Methods in the Completed Game (Milestone 5):

- **`__init__(self, word_list, num_lives=5)`**
  - Initializes the Hangman game with a word list and an optional number of lives.

- **`choose_random_word(self)`**
  - Chooses a random word from the list and sets up the initial game state.

- **`check_guess(self, guess)`**
  - Checks if the guessed letter is in the word and updates the game state accordingly.

- **`update_word_guessed(self, guess)`**
  - Updates the `word_guessed` list based on the correct guess.

- **`ask_for_input(self)`**
  - Asks the user for a valid letter input, handles input validation, and calls `check_guess`.

- **`is_valid_guess(self, guess)`**
  - Checks if the guess is a valid input.

- **`play_game(word_list)`**
  - Runs the entire Hangman game, handling game states, user input, and determining win/loss conditions.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Samarpatel16/hangman/tree/main/hangman
Navigate to Project Directory

bash
Copy code
cd hangman
Install Dependencies

bash
Copy code
pip install python 3.12  # (For example)
Usage
Run the Game:

bash
Copy code
python milestone_5.py
Follow On-Screen Prompts:

Enter a single alphabetical character when prompted to guess a letter.
Continue guessing until you win or lose the game.
Game Output:

The game will display messages indicating whether your guess is correct, the word guessed so far, and the remaining lives.
The game will end when you either correctly guess the word or run out of lives.
File Structure
The project files are organized as follows:

milestone_5.py: The main script that combines the Hangman class and the play_game function.

hangman.py: Contains the Hangman class with methods for initializing the game, checking guesses, and handling user input. Each method is described below:

__init__(self, word_list, num_lives=5)

Initializes the Hangman game with a word list and optional number of lives.
choose_random_word(self)

Chooses a random word from the list and sets up the initial game state.
check_guess(self, guess)

Checks if the guessed letter is in the word and updates the game state accordingly.
update_word_guessed(self, guess)

Updates the word_guessed list based on the correct guess.
ask_for_input(self)

Asks the user for a valid letter input, handles input validation, and calls check_guess.
is_valid_guess(self, guess)

Checks if the guess is a valid input.
README.md: Documentation for the project.


This updated README includes brief descriptions of each method in the `Hangman` class, providing users with insights into the purpose of each method


## Usage
Run the Game:

python milestone_5.py
Follow On-Screen Prompts:

Enter a single alphabetical character when prompted to guess a letter.
Continue guessing until you win or lose the game.
Game Output:

The game will display messages indicating whether your guess is correct, the word guessed so far, and the remaining lives.
The game will end when you either correctly guess the word or run out of lives

## File Structure

The project files are organized as follows:

milestone_5.py: The main script that combines the Hangman class and the play_game function.

hangman.py: Contains the Hangman class with methods for initializing the game, checking guesses, and handling user input.

README.md: Documentation for the project.

