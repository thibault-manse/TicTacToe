import random

class TicTacToe:
    def __init__(self):
        self.board = [" "," "," "," "," "," "," "," "," "]
        self.current_player = random.choice(["X", "O"])
        self.retry = True #variable for the loop which is used to replay
        self.replay = 1 #variable used to have the request to replay or not

    # Display the board
    def print_board(self):
        print(self.board[0], "|", self.board[1], "|", self.board[2])
        print("---------")
        print(self.board[3], "|", self.board[4], "|", self.board[5])
        print("---------")
        print(self.board[6], "|", self.board[7], "|", self.board[8])

    #Alterne X and O
    def alternate_player(self):
        return "O" if self.current_player == "X" else "X"

    def game(self):
        # Loop to define the different rounds of the game, with a maximum of 9 rounds
        cases = 0
        while cases < 9:
            TicTacToe.print_board(self)
            try :
                new_value = int(input(f"Joueur {self.current_player}, choisissez votre coup (1-9) : "))  # Using "new_value" to choose the player's move
            except ValueError:
                print("Valeur invalide, veillez reessayer !")
                continue
            
            # The different conditions to be respected to save the choice of the current player
            if 1 <= new_value <= 9 and self.board[new_value -1] == " ":
                self.board[new_value-1] = self.current_player
                cases += 1
            else:
                print("Coup invalide, réessayez.")
                continue

            # Conditions to win the game
            if ((self.board[0] == self.board[1] == self.board[2] != " ") or # Victories by lines
                (self.board[3] == self.board[4] == self.board[5] != " ") or
                (self.board[6] == self.board[7] == self.board[8] != " ") or
                (self.board[0] == self.board[3] == self.board[6] != " ") or # Victories by column
                (self.board[1] == self.board[4] == self.board[7] != " ") or
                (self.board[2] == self.board[5] == self.board[8] != " ") or
                (self.board[0] == self.board[4] == self.board[8] != " ") or # Victories by diagonals
                (self.board[2] == self.board[4] == self.board[6] != " ")):
                TicTacToe.print_board(self)
                print(f"Le joueur {self.current_player} gagne !") # Victory message
                break

            # Conditions for a draw
            if " " not in self.board:
                TicTacToe.print_board(self)
                print("Match nul !") # Message of equality
                break

            self.current_player = TicTacToe.alternate_player(self) # Change player at end of round

    def start(self): #function of the menu and the choice xe replay or not
        print("Tic Tac Toa")
        print("1 - Joueur vs Joueur")
        print("2 - Joueur vs IA")
        try : 
            choice = int(input("Choisissez votre mode de jeux (1 ou 2): ")) #choice of game mode
        except ValueError:
            print("Valeur rentré incorrect !")

        if choice == 1:
            while self.retry == True:
                if self.replay == 1:
                    TicTacToe.game(self)
                    self.replay = 0
                val = str(input("Voulez vous rejouer ? (y ou n) : "))#choice to play again or not
                if val != "y" and val !="n":
                    print("erreur d'input !")
                elif val == "y":
                    self.replay = 1
                    self.board = [" "," "," "," "," "," "," "," "," "]
                elif val == "n":
                    self.retry = False

        elif choice == 2:
            print("Il y aura le mode de jeux contre l'IA ici !")

        else :
            print("Mode de jeux inexistant, choix uniquement entre 1 et 2")


#exemple = TicTacToe()
#exemple.start()