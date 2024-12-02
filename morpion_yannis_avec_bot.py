import random

board = [" "," "," "," "," "," "," "," "," "]  # Plateau de jeu (liste avec 9 cases vides)

# Fonction pour afficher le plateau
def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

# Choisir aléatoirement qui commence. Le joueur humain sera toujours le joueur X, le bot toujours le joueur O
current_player=random.choice(["X","O"])
print(f"Le joueur {current_player} commence")


# Fonction pour alterner les tours entre les joueurs, de "X" à "O"
def alternate_player(current_player):
    return "O" if current_player == "X" else "X"

# Fonction pour le bot qui joue un coup aléatoire
def bot_move():
    available_moves = [i for i in range(1,9) if board[i] == " "]  # Liste des cases vides
    return random.choice(available_moves)

# Boucle pour définir les différents tours du jeu, avec un maximum de 9 tours
for turn in range(9):

    print_board()
    
    if current_player == "X":  # Joueur humain
        try:
            new_value = int(input(f"Joueur {current_player}, choisissez votre coup (1-9) : ")) 
        except ValueError:
            print("Veuillez entrer un nombre valide entre 1 et 9")
            
    else:  # Tour du bot
        print("Tour du bot...")
        new_value = bot_move()

    # Les différentes conditions à respecter pour enregistrer le choix du joueur actuel
    if 1 <= new_value <= 9 and board[new_value -1] == " ":
        board[new_value-1] = current_player
    else:
        print("Coup invalide, réessayez.")
        if current_player == "X":
            continue  # Si joueur humain, demander un nouveau coup
        else:
            new_value = bot_move()  # Si bot, choisir un nouveau coup
            board[new_value] = current_player


    # Conditions pour gagner la partie
    if ((board[0] == board[1] == board[2] != " ") or # Victoires par lignes
        (board[3] == board[4] == board[5] != " ") or
        (board[6] == board[7] == board[8] != " ") or
        (board[0] == board[3] == board[6] != " ") or # Victoires par colonnes
        (board[1] == board[4] == board[7] != " ") or
        (board[2] == board[5] == board[8] != " ") or
        (board[0] == board[4] == board[8] != " ") or # Victoires par diagonales
        (board[2] == board[4] == board[6] != " ")):
        print_board()
        print(f"Le joueur {current_player} gagne !") # Message de victoire
        break

    # Conditions pour un match nul
    if " " not in board:
        print_board()
        print("Match nul !") # Message d'égalité
        break

    current_player = alternate_player(current_player) # Changer de joueur à la fin du tour

