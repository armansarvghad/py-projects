def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        # Get player input
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Update the board
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        # Check if the current player wins
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break

        # Check if it's a tie
        if all(cell != ' ' for row in board for cell in row):
            print("It's a tie!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

play_game()
