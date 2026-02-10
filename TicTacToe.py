# Jigarjeet Mannan
# tictactoe.py

import math

# We will store the board as a list with 9 slots.
# The slots are +1 than the actual indices in the code
# (This is for a cleaner/more intuitive looking board)
# Indices of the board for reference:
# 1 | 2 | 3
# --- --- ---
# 4 | 5 | 6
# --- --- ---
# 7 | 8 | 9

def print_board(board):
    """Prints the current state of the board in a 3x3 grid."""
    print("\n")

    for i in range(3):
        row = board[3 * i: 3 * i + 3]


        # Build the row display
        row_display = []
        for cell in row:
            if cell is not None:
                row_display.append(cell)
            else:
                row_display.append(" ")
        

        print(" " + " | ".join(row_display))

        if i < 2:
            print(" --- --- ---")

    print("\n")



def empty_positions(board):
    """Returns a list of indices on the board that are still empty."""

    empty_spots = []

    for i, spot in enumerate(board):
        if spot is None:
            empty_spots.append(i)

    return empty_spots



def check_gamestate(board):
    """
    Returns:
    'X' if X has won,
    'O' if O has won,
    'D' for draw if the board is full and no one has won,
    None otherwise (game is still going).
    """

    # All possible winning combinations
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6)               # diagonals
]

    # Check for wins
    for combo in winning_positions:
        a, b, c = combo

        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]   # 'X' or 'O'

    # Check for draw
    is_board_full = True
    
    for spot in board:
        if spot is None:
            is_board_full = False
            break
    
    if is_board_full:
        return 'D'

    # Otherwise, no winner yet
    return None



def minimax(board, is_maximizing):
    """
    The Minimax function:
    - board: current board state
    - is_maximizing: bool, True if it's AI's turn to maximize score

    Returns:
    (best_score, best_move_index)
    """

    # First, check if the game is already won or drawn
    winner = check_gamestate(board)

    if winner == 'X':
        return -1, None   # Worst for AI, best for human

    elif winner == 'O':
        return 1, None    # Best for AI

    elif winner == 'D':
        return 0, None    # Draw

    # We define scores from AI's perspective:
    # O-win = 1
    # X-win = -1
    # draw = 0

    if is_maximizing:

        best_score = -math.inf
        best_move = None

        for move in empty_positions(board):

            board[move] = 'O'   # Temporarily make the AI's move

            score, _ = minimax(board, False)

            board[move] = None  # Undo move

            if score > best_score:
                best_score = score
                best_move = move

        return best_score, best_move

    else:

        best_score = math.inf
        best_move = None

        for move in empty_positions(board):

            board[move] = 'X'   # Temporarily make the human's move

            score, _ = minimax(board, True)

            board[move] = None  # Undo move

            if score < best_score:
                best_score = score
                best_move = move

        return best_score, best_move



def player_move(board):
    """Prompts the user for a valid move and places 'X' on the board."""

    while True:

        try:
            move = int(input("Your move (1 - 9): ").strip())

            if move < 1 or move > 9:
                print("Invalid input. Please enter a number between 0 and 9.")
                continue

            index = move - 1 # Convert 1-9 to 0-8

            if board[index] is not None:
                print("That position is already taken, try again.")
                continue

            board[index] = 'X'
            break

        except ValueError:
            print("Please enter an integer between 1 and 9.")



def ai_move(board):
    """AI calculates the best move using Minimax and places 'O'."""

    _, move = minimax(board, True)
    board[move] = 'O'



def main():
    """Runs the Tic-Tac-Toe game loop."""

    board = [None] * 9
    current_player = 'X'   # Human always goes first in this setup

    while True:

        print_board(board)

        # Check if game is over
        status = check_gamestate(board)

        if status == 'X':
            print("You win! Congratulations!")
            break

        elif status == 'O':
            print("AI wins! Better luck next time.")
            break

        elif status == 'D':
            print("It's a draw!\n")
            restart = input("Would you like to play again? (Y/N): ").strip().lower()

            if restart == 'y' or restart == 'yes':
                print("\nStarting a new game...\n")
                main()  # This will break out to the outer loop and restart
                return
            else:
                print("\nThanks for playing!")
                return  # This will exit the game completely
            

        if current_player == 'X':
            player_move(board)
            current_player = 'O'

        else:
            ai_move(board)
            current_player = 'X'



if __name__ == "__main__":
    main()
