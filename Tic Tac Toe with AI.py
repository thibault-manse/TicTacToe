import random
import time
# Library for the Tic-Tac-Toe game
# Game board with 9 empty spaces
board = [" "]*9

"""Display the game board."""
def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

# Initial player chosen at random
current_player = random.choice(["X", "O"])
print(f"Player {current_player} begin !")

# Function to alternate turns between players, from "X" to "O"
def alternate_player(current_player):
    return "O" if current_player == "X" else "X"
# Function to set AI reactions
def ai_move():
    if board[0] == "X" and board[1] == "X" and board[2] == " ":   # Block lines
        board[2] = "O"
    elif board[1] == "X" and board[2] == "X" and board[0] == " ":
        board[0] = "O"
    elif board[0] == "X" and board[2] == "X" and board[1] == " ":
        board[1] = "O"
    elif board[3] == "X" and board[4] == "X" and board[5] == " ":
        board[5] = "O"
    elif board[4] == "X" and board[5] == "X" and board[3] == " ":
        board[3] = "O"
    elif board[3] == "X" and board[5] == "X" and board[4] == " ":
        board[4] = "O"
    elif board[6] == "X" and board[7] == "X" and board[8] == " ":
        board[8] = "O"
    elif board[7] == "X" and board[8] == "X" and board[6] == " ":
        board[6] = "O"
    elif board[6] == "X" and board[8] == "X" and board[7] == " ":
        board[7] = "O"
    elif board[0] == "X" and board[3] == "X" and board[6] == " ":  # Block columns
        board[6] = "O"
    elif board[3] == "X" and board[6] == "X" and board[0] == " ":
        board[0] = "O"
    elif board[0] == "X" and board[6] == "X" and board[3] == " ":
        board[3] = "O"
    elif board[1] == "X" and board[4] == "X" and board[7] == " ":
        board[7] = "O"
    elif board[4] == "X" and board[7] == "X" and board[1] == " ":
        board[1] = "O"
    elif board[1] == "X" and board[7] == "X" and board[4] == " ":
        board[4] = "O"
    elif board[2] == "X" and board[5] == "X" and board[8] == " ":
        board[8] = "O"
    elif board[5] == "X" and board[8] == "X" and board[2] == " ":
        board[2] = "O"
    elif board[2] == "X" and board[8] == "X" and board[5] == " ":
        board[5] = "O"
    elif board[0] == "X" and board[4] == "X" and board[8] == " ":  # Block diagonals
        board[8] = "O"
    elif board[4] == "X" and board[8] == "X" and board[0] == " ":
        board[0] = "O"
    elif board[0] == "X" and board[8] == "X" and board[4] == " ":
        board[4] = "O"
    elif board[6] == "X" and board[2] == "X" and board[4] == " ":
        board[4] = "O"
    elif board[2] == "X" and board[4] == "X" and board[6] == " ":
        board[6] = "O"
    elif board[6] == "X" and board[4] == "X" and board[2] == " ":
        board[2] = "O"
    else:   # If no possibility to block, the AI ​​will choose the first empty square
        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "O"
                break

# Loop to define the different rounds in the game, with a maximum of 9 rounds
for turn in range(9):

    print_board()

    if current_player == "X":
        new_value = int(input(f"Player {current_player}, choisissez votre mouvement (1-9): ")) # Utiliser "new_value" pour choisir le mouvement du joueur
    
       # The different conditions to be respected to save the choice of the current player
        if 1 <= new_value <= 9 and board[new_value -1] == " ":
            board[new_value -1] = current_player
        else:
            print("Invalid movement, try again.")
            continue
    else:
        ai_move()
        print("The AI ​​has played its turn.")
# Conditions to win the game
    if ((board[0] == board[1] == board[2] != " ") or # Victories by lines
        (board[3] == board[4] == board[5] != " ") or
        (board[6] == board[7] == board[8] != " ") or
        (board[0] == board[3] == board[6] != " ") or # Victories by columns
        (board[1] == board[4] == board[7] != " ") or
        (board[2] == board[5] == board[8] != " ") or
        (board[0] == board[4] == board[8] != " ") or # Victories by diagonals
        (board[2] == board[4] == board[6] != " ")):
        print_board()
        print(f"Player {current_player} has won!") # The message in case of victory
        break

    # Equal conditions
    if " " not in board:
        print_board()
        print("It's a draw!") # The message in case of a tie
        break

    current_player = alternate_player(current_player) # Change player at end of round
