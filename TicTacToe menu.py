import random

retry = True #variable for the loop which is used to replay
replay = 1 #variable used to have the request to replay or not

# Display the board
def print_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

# Random player begin first
flag = random.randint(0, 1)
if flag == 0:
    current_player = "X"
else:
    current_player = "O"

#Alterne X and O
def alternate_player(current_player):
    return "O" if current_player == "X" else "X"

def game(board, current_player):
    # Loop to define the different rounds of the game, with a maximum of 9 rounds
    cases = 0
    while cases < 9:
        print_board(board)
        try :
            new_value = int(input(f"Joueur {current_player}, choisissez votre coup (1-9) : "))  # Using "new_value" to choose the player's move
        except ValueError:
            print("Valeur invalide, veillez reessayer !")
            continue
        
        # The different conditions to be respected to save the choice of the current player
        if 1 <= new_value <= 9 and board[new_value -1] == " ":
            board[new_value-1] = current_player
            cases += 1
        else:
            print("Coup invalide, réessayez.")
            continue

        # Conditions to win the game
        if ((board[0] == board[1] == board[2] != " ") or # Victories by lines
            (board[3] == board[4] == board[5] != " ") or
            (board[6] == board[7] == board[8] != " ") or
            (board[0] == board[3] == board[6] != " ") or # Victories by column
            (board[1] == board[4] == board[7] != " ") or
            (board[2] == board[5] == board[8] != " ") or
            (board[0] == board[4] == board[8] != " ") or # Victories by diagonals
            (board[2] == board[4] == board[6] != " ")):
            print_board(board)
            print(f"Le joueur {current_player} gagne !") # Victory message
            break

        # Conditions for a draw
        if " " not in board:
            print_board(board)
            print("Match nul !") # Message of equality
            break

        current_player = alternate_player(current_player) # Change player at end of round

def start(retry, replay): #function of the menu and the choice xe replay or not
    print("Tic Tac Toa")
    print("1 - Joueur vs Joueur")
    print("2 - Joueur vs IA")
    try : 
        choice = int(input("Choisissez votre mode de jeux (1 ou 2): ")) #choice of game mode
    except ValueError:
        print("Valeur rentré incorrect !")

    if choice == 1:
        while retry == True:
            if replay == 1:
                board = [" "," "," "," "," "," "," "," "," "] #Create a table with 9 cases
                game(board, current_player)
                replay = 0
            val = str(input("Voulez vous rejouer ? (y ou n) : "))#choice to play again or not
            if val != "y" and val !="n":
                print("erreur d'input !")
            elif val == "y":
                replay = 1
            elif val == "n":
                retry = False

    elif choice == 2:
        print("Il y aura le mode de jeux contre l'IA ici !")

    else :
        print("Mode de jeux inexistant, choix uniquement entre 1 et 2")

start(retry, replay)