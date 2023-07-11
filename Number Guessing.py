import random

def guess_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    while True:
        # Take user input
        user_guess = int(input("Guess a number between 1 and 100: "))

        # Compare the guess with the random number
        if user_guess == random_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Run the game
guess_number()
