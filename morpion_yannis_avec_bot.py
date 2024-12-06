import random
import time
from time import sleep

board = [" "," "," "," "," "," "," "," "," "]  # Playground (list of 9 empty slots)

# Function : display board
def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

# Randomly choosing the first player. Human player will always be X, bot will always be O
current_player=random.choice(["X","O"])
print(f"Le joueur {current_player} commence")


# Function to alternate turns
def alternate_player(current_player):
    return "O" if current_player == "X" else "X"

# Function : a bot that plays randomly
def bot_move():
    print(board)
    available_moves = []
    for i in range(9) : 
        if board[i] ==" " :
            available_moves.append(i + 1)
    print(available_moves)
    a=random.choice(available_moves)
    print(a)
    return a

# Loop to determine turns (max = 9)
for turn in range(9):

    print_board()
    
    if current_player == "X":  # Human
        try:
            new_value = int(input(f"Joueur {current_player}, choisissez votre coup (1-9) : ")) 
        except ValueError:
            print("Veuillez entrer un nombre valide entre 1 et 9")
            
    else:  # Bot's turn
        print("Tour du bot...")
        time.sleep(1)
        new_value = bot_move()

    # Mandatory conditions to register a move
    if 1 <= new_value <= 9 and board[new_value - 1] == " ":
        board[new_value-1] = current_player
    else:
        print("Coup invalide, réessayez.")
        if current_player == "X":
            continue  # if human, ask for another move
        else:
            new_value = bot_move()  # If bot, chose another move
            board[new_value-1] = current_player


    # Winning conditions/combinaisons
    if ((board[0] == board[1] == board[2] != " ") or # Victory by rows
        (board[3] == board[4] == board[5] != " ") or
        (board[6] == board[7] == board[8] != " ") or
        (board[0] == board[3] == board[6] != " ") or # Victory by columns
        (board[1] == board[4] == board[7] != " ") or
        (board[2] == board[5] == board[8] != " ") or
        (board[0] == board[4] == board[8] != " ") or # Victory by diagonals
        (board[2] == board[4] == board[6] != " ")):
        print_board()
        print(f"Le joueur {current_player} gagne !") # Yay ! You won :)
        break

    # Conditions for a draw
    if " " not in board:
        print_board()
        print("Match nul !") # Oh, it's a draw!
        break

    current_player = alternate_player(current_player) # allows to alternate between the two players

