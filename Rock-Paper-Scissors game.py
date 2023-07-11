import random

def main():
    options = ['rock', 'paper', 'scissors']
    player_1 = input("Player 1, make your choice: rock, paper, or scissors? ")
    player_2 = input("Player 2, make your choice: rock, paper, or scissors? ")

    if player_1 not in options or player_2 not in options:
        print("Invalid choice. Please choose either rock, paper, or scissors.")
    elif player_1 == player_2:
        print("It's a tie!")
    elif (player_1 == 'rock' and player_2 == 'scissors') or (player_1 == 'paper' and player_2 == 'rock') or (player_1 == 'scissors' and player_2 == 'paper'):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

if __name__ == "__main__":
    main()
