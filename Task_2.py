import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Guess the Number Game")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label_instruction = tk.Label(root, text="I'm thinking of a number between 1 and 100...", font=("Arial", 12))
        self.label_instruction.pack(pady=20)

        self.entry_guess = tk.Entry(root, font=("Arial", 14))
        self.entry_guess.pack(pady=10)

        self.button_submit = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12))
        self.button_submit.pack(pady=10)

        self.label_feedback = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.label_feedback.pack(pady=10)

        self.button_restart = tk.Button(root, text="Restart Game", command=self.restart_game, font=("Arial", 10))
        self.button_restart.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.label_feedback.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.label_feedback.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("🎉 Congratulations!", f"You guessed it right in {self.attempts} attempts!\nThe number was {self.number_to_guess}.")
                self.entry_guess.config(state="disabled")
                self.button_submit.config(state="disabled")
        except ValueError:
            self.label_feedback.config(text="Please enter a valid number.")

    def restart_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry_guess.config(state="normal")
        self.button_submit.config(state="normal")
        self.label_feedback.config(text="")
        self.entry_guess.delete(0, tk.END)

# Create the GUI window
root = tk.Tk()
game = GuessNumberGame(root)
root.mainloop()
