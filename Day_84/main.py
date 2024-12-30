# Function to print the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check if the current player has won
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]  # diagonals
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (draw)
def check_draw(board):
    return all(space != " " for space in board)

# Function to handle player's turn
def player_turn(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                break
            else:
                print("This spot is already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid move. Please select a number between 1 and 9.")

# Main function to run the game
def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        player_turn(board, current_player)
        print_board(board)
        
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
