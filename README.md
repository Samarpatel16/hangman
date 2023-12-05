# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


# Hangman

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Description

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Currently, I have completed the following milestones that help to build this project:

Milestone 1: Setting up the Environment 
- This was the first step where I set up the Github repository

Milestone 2: Creating the variables for the game
- Using conditions and the users input. Once an answer is input there is a validation check

Milestone 3: Check that that guessed characters are in the word
- Checking that the guessed letter is actually inside of the word.

Milestone 4: Creating the game class
- Using OOP to develop the Hangman game

## Installation

1. Clone the Repository
git clone https://github.com/Samarpatel16/hangman/tree/main/hangman

2. Navigate to Project Directory
cd hangman

3. Install dependancies
pip install pandas (For example) 

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

## License


