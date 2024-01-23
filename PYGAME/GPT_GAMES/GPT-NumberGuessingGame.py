import tkinter as tk
import random

# Function to check if the guessed number matches the generated number
def check_guess():
    guessed_number = int(guess_entry.get())
    if guessed_number == generated_number:
        result_label.config(text="Congratulations! You guessed it right!")
    elif guessed_number < generated_number:
        result_label.config(text="Too low! Try again.")
    else:
        result_label.config(text="Too high! Try again.")

# Function to generate a random number between 1 and 100
def generate_random_number():
    global generated_number
    generated_number = random.randint(1, 100)
    start_button.config(state=tk.DISABLED)
    guess_button.config(state=tk.NORMAL)
    guess_entry.config(state=tk.NORMAL)

# Create a GUI window
root = tk.Tk()
root.title("Number Guessing Game")

# Generate a random number
generated_number = 0

# Widgets
title_label = tk.Label(root, text="Welcome to the Number Guessing Game!", font=("Helvetica", 16))
title_label.pack(pady=10)

start_button = tk.Button(root, text="Start Game", command=generate_random_number)
start_button.pack(pady=5)

guess_entry = tk.Entry(root, width=20, state=tk.DISABLED)
guess_entry.pack(pady=5)

guess_button = tk.Button(root, text="Submit Guess", command=check_guess, state=tk.DISABLED)
guess_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()