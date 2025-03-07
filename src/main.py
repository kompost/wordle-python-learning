import tkinter as tk
from word_utils import load_words, select_random_word
from game_logic import check_guess 
from ui_components import create_ui

class WordleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle Game")

        self.number_of_guesses = 6
        self.target_word = select_random_word(load_words('./src/data/words.txt'))
        self.guesses = [[]]

        self.create_widget()

    def create_widget(self):
        '''Create the UI components'''
        self.ui = create_ui(self.root, self.check_guess, self.play_again)

    def check_guess(self, guess):
        '''Check the guess and update the UI'''
        result = check_guess(guess, self.target_word)
        if len(result) < 5:
            return  

        # a valid guess
        self.number_of_guesses -= 1

        if(all(item['result'] == 'correct' for item in result)):
            self.ui.update_ui("win", self.target_word)
            return
         
        if self.number_of_guesses <= 0:
            self.ui.update_ui("game over", self.target_word)
            print("Game Over")
            return
                       
        self.guesses.append(result)
        self.ui.update_ui('playing', self.guesses)

    def play_again(self):
        '''Reset the game'''
        self.number_of_guesses = 6
        self.target_word = select_random_word(load_words('./src/data/words.txt'))
        self.guesses = [[]]
        self.ui.update_ui('play again', self.guesses)

if __name__ == "__main__":
    root = tk.Tk()
    game = WordleGame(root)
    root.mainloop()


