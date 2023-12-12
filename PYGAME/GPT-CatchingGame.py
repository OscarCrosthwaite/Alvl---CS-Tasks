import random
import time

def game():
    score = 0
    while True:
        print("Catch the falling objects!")
        print("Type 'c' to catch.")
        print("Press 'q' to quit.")

        # Generate a random falling object
        falling_object = random.choice(['*', '#', '$', '%'])

        print(f"A {falling_object} is falling!")

        start_time = time.time()
        user_input = input()

        # Calculate reaction time
        end_time = time.time()
        reaction_time = end_time - start_time

        if user_input == 'c':
            score += 1
            print(f"You caught the {falling_object}! Score: {score}")
        elif user_input == 'q':
            print(f"Game over! Your final score is {score}.")
            break
        else:
            print("You missed!")

        print(f"Reaction time: {reaction_time:.2f} seconds")
        print("-------------------")

if __name__ == "__main__":
    game()
