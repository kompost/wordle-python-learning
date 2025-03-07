# Wordle Game

This is a simple implementation of the popular word-guessing game, Wordle, using Python and Tkinter for the graphical user interface.

## Features

- **Interactive UI**: Built with Tkinter, providing a user-friendly interface for guessing words.
- **Word Validation**: Checks each guess against the target word and provides feedback on correctness.
- **Multiple Attempts**: Players have six attempts to guess the correct word.
- **Play Again Option**: Easily restart the game after winning or losing.

## How to Play

1. **Objective**: Guess the target five-letter word within six attempts.
2. **Input**: Enter your guess in the provided text entry field and click "Submit".
3. **Feedback**:
   - Letters in the correct position are highlighted in green.
   - Letters present in the word but in the wrong position are highlighted in yellow.
   - Letters not in the word are highlighted in gray.
4. **Win/Lose**: If you guess the word correctly within six attempts, you win. Otherwise, the game ends, and you can choose to play again.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kompost/wordle-python-learning.git
   ```
2. Navigate to the project directory:
   ```bash
   cd wordle-python-learning
   ```
3. Run the game:
   ```bash
   python src/main.py
   ```

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## File Structure

- `src/main.py`: Main entry point for the game.
- `src/game_logic.py`: Contains the logic for checking guesses.
- `src/ui_components.py`: Manages the user interface components.
- `src/word_utils.py`: Utility functions for loading and selecting words.

## License

This project is licensed under the Specialisterne.

## Acknowledgments

- Inspired by the original Wordle game.

