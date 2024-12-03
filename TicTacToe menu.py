import random

retry = True
re = 1

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
    # Boucle pour définir les différents tours du jeu, avec un maximum de 9 tours
    cases = 0
    while cases < 9:
        print_board(board)
        try :
            new_value = int(input(f"Joueur {current_player}, choisissez votre coup (1-9) : "))  # Utilisation de "new_value" pour choisir le coup du joueur
        except ValueError:
            print("Valeur invalide, veillez reessayer !")
            continue
        
        # Les différentes conditions à respecter pour enregistrer le choix du joueur actuel
        if 1 <= new_value <= 9 and board[new_value -1] == " ":
            board[new_value-1] = current_player
            cases += 1
        else:
            print("Coup invalide, réessayez.")
            continue

        # Conditions pour gagner la partie
        if ((board[0] == board[1] == board[2] != " ") or # Victoires par lignes
            (board[3] == board[4] == board[5] != " ") or
            (board[6] == board[7] == board[8] != " ") or
            (board[0] == board[3] == board[6] != " ") or # Victoires par colonnes
            (board[1] == board[4] == board[7] != " ") or
            (board[2] == board[5] == board[8] != " ") or
            (board[0] == board[4] == board[8] != " ") or # Victoires par diagonales
            (board[2] == board[4] == board[6] != " ")):
            print_board(board)
            print(f"Le joueur {current_player} gagne !") # Message de victoire
            break

        # Conditions pour un match nul
        if " " not in board:
            print_board(board)
            print("Match nul !") # Message d'égalité
            break

        current_player = alternate_player(current_player) # Changer de joueur à la fin du tour

def start(retry, re):
    print("Tic Tac Toa")
    print("1 - Joueur vs Joueur")
    print("2 - Joueur vs IA")
    try : 
        choice = int(input("Choisissez votre mode de jeux (1 ou 2): "))
    except ValueError:
        print("Valeur rentré incorrect !")

    if choice == 1:
        while retry == True:
            if re == 1:
                board = [" "," "," "," "," "," "," "," "," "] #Create a table with 9 cases
                game(board, current_player)
                re = 0
            val = str(input("Voulez vous rejouer ? (y ou n) : "))
            if val != "y" and val !="n":
                print("erreur d'input !")
            elif val == "y":
                re = 1
            elif val == "n":
                retry = False

    elif choice == 2:
        print("Il y aura le mode de jeux contre l'IA ici !")

    else :
        print("Mode de jeux inexistant, choix uniquement entre 1 et 2")

start(retry, re)