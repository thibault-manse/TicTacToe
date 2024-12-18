import random

board = [" "," "," "," "," "," "," "," "," "]  # Plateau de jeu (liste avec 9 cases vides)

# Fonction pour afficher le plateau
def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

# Le joueur "X" commence toujours
current_player=random.choice(["X","O"])
print(f"Le joueur {current_player} commence")


# Fonction pour alterner les tours entre les joueurs, de "X" à "O"
def alternate_player(current_player):
    return "O" if current_player == "X" else "X"

# Boucle pour définir les différents tours du jeu, avec un maximum de 9 tours
for turn in range(9):

    print_board()
    
    new_value = int(input(f"Joueur {current_player}, choisissez votre coup (1-9) : "))  # Utilisation de "new_value" pour choisir le coup du joueur
    
    # Les différentes conditions à respecter pour enregistrer le choix du joueur actuel
    if 1 <= new_value <= 9 and board[new_value -1] == " ":
        board[new_value-1] = current_player
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
        print_board()
        print(f"Le joueur {current_player} gagne !") # Message de victoire
        break

    # Conditions pour un match nul
    if " " not in board:
        print_board()
        print("Match nul !") # Message d'égalité
        break

    current_player = alternate_player(current_player) # Changer de joueur à la fin du tour