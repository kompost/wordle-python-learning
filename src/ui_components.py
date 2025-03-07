import tkinter as tk

class UIComponents:
    def __init__(self, root, check_guess_callback, play_again_callback):
        self.root = root
        self.check_guess_callback = check_guess_callback
        self.play_again_callback = play_again_callback
        self.create_ui()

    def create_ui(self):
        # Clear the current UI
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create a frame to hold the widgets
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Entry widget for user input
        self.entry = tk.Entry(frame, width=10, validate="key", validatecommand=(self.root.register(self.validate_entry), '%P'))
        self.entry.grid(row=0, column=0, padx=5, pady=5)

        # Submit button
        submit_button = tk.Button(frame, text="Submit", command=self.submit_guess)
        submit_button.grid(row=0, column=1, padx=5, pady=5)

        # Label to display results
        self.result_label = tk.Label(frame, text="")
        self.result_label.grid(row=1, column=0, columnspan=2, pady=5)

    def validate_entry(self, new_value):
        return len(new_value) <= 5
        
    def submit_guess(self):
        guess = self.entry.get()
        self.check_guess_callback(guess)

    def update_ui(self, type, result):
        if type == "playing":
            self.render_guesses(result)
        elif type == "game over":
            self.render_game_over_screen()
        elif type == "win":
            self.render_win_screen(result)
        elif type == "play again":
            self.create_ui()

    def render_guesses(self, guesses):
        # color mapping for each result type
        color_mapping = {
            'correct': ('green', 'white'),
            'present': ('yellow', 'black'),
            'absent': ('gray', 'white')
        }

        # Create a new label for each character in the result
        for i, guess in enumerate(guesses):
            for j, letter in enumerate(guess):
                bg_color, fg_color = color_mapping.get(letter['result'], ('white', 'black'))
                label = tk.Label(self.result_label, text=letter['value'], bg=bg_color, fg=fg_color, width=2)
                label.grid(row=i, column=j, padx=2, pady=2)

    def render_game_over_screen(self):
        # Clear the current UI
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create a frame for the game over screen
        game_over_frame = tk.Frame(self.root)
        game_over_frame.pack(padx=10, pady=10)

        # Game over message
        game_over_label = tk.Label(game_over_frame, text="Game Over", font=("Arial", 24))
        game_over_label.pack(pady=10)
        
        # Restart button
        restart_button = tk.Button(game_over_frame, text="Restart", command=self.play_again_callback)
        restart_button.pack(side=tk.LEFT, padx=5)

        # Exit button
        exit_button = tk.Button(game_over_frame, text="Exit", command=self.root.quit)
        exit_button.pack(side=tk.RIGHT, padx=5)

    def render_win_screen(self, result):
        # Clear the current UI
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create a frame for the win screen
        win_frame = tk.Frame(self.root)
        win_frame.pack(padx=10, pady=10)

        # Win message
        win_label = tk.Label(win_frame, text="Congratulations! You Win!", font=("Arial", 24))
        win_label.pack(pady=10)

        # Display the correct word
        correct_word_label = tk.Label(win_frame, text=f"The word was: {result}", font=("Arial", 16))
        correct_word_label.pack(pady=5)

        # Play again button
        restart_button = tk.Button(win_frame, text="Play again", command=self.play_again_callback)
        restart_button.pack(side=tk.RIGHT, padx=5)
           
def create_ui(root, check_guess_callback, play_again_callback):
    return UIComponents(root, check_guess_callback, play_again_callback)

