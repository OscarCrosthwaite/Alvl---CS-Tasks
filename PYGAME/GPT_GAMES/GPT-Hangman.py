import random

def hangman():
    words = ["apple", "banana", "orange", "grape", "melon"]  # List of words to guess
    chosen_word = random.choice(words).lower()  # Choose a random word from the list
    guessed_letters = []  # List to store guessed letters
    attempts = 6  # Number of attempts allowed

    while attempts > 0:
        display = ""  # Variable to store the word with placeholders for unguessed letters
        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print(display)

        if display.replace(" ", "") == chosen_word:  # Check if the word has been guessed
            print("Congratulations! You guessed the word:", chosen_word)
            break

        guess = input("Guess a letter: ").lower()  # Ask for a letter guess
        if len(guess) != 1 or not guess.isalpha():  # Validate input
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:  # Check if the letter has already been guessed
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)  # Add guessed letter to the list

        if guess not in chosen_word:  # If guessed letter is not in the word
            attempts -= 1
            print("Incorrect guess! Attempts left:", attempts)
            if attempts == 0:
                print("Sorry, you ran out of attempts. The word was:", chosen_word)
                break

hangman()