import random
import time
# Library for the Tic-Tac-Toe game
class TicTacToe:
    def __init__(self):
        # Game board with 9 empty spaces
        self.board = [" "] * 9
        self.current_player = random.choice(["X", "O"])
        print(f"The player {self.current_player} starts!")
    def print_board(self):
        """Display the game board."""
        print(self.board[0], "|", self.board[1], "|", self.board[2])
        print("---------")
        print(self.board[3], "|", self.board[4], "|", self.board[5])
        print("---------")
        print(self.board[6], "|", self.board[7], "|", self.board[8])
    def alternate_player(self):
        """Switch the current player."""
        self.current_player = "O" if self.current_player == "X" else "X"
    def check_winner(self):
        """Check if there is a winner."""
        b = self.board
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for combo in winning_combinations:
            if b[combo[0]] == b[combo[1]] == b[combo[2]] != " ":
                return True
        return False
    def check_draw(self):
        """Check if the game is a draw."""
        return " " not in self.board
    def get_ia_move(self):
        """Basic AI: choose a move to win or block the opponent."""
        for i in range(9):
            if self.board[i] == " ":
                # Try to win
                self.board[i] = self.current_player
                if self.check_winner():
                    return i
                self.board[i] = " "
        # Otherwise, pick a random move
        return random.choice([i for i, v in enumerate(self.board) if v == " "])
          
    def start_game(self, mode):
        """Run the game loop."""
        turn = 0          
        while turn < 9:
            self.print_board()
            if mode == "friend" or (mode == "ia" and self.current_player == "X"):
                # Player input
                try:
                    move = int(input(f"player {self.current_player},chose move (1-9): ")) -1
                    if move < 0 or move > 8 or self.board[move] != " ":
                        print("Invalid move. Try again.")
                        continue
                except ValueError:
                    print("Please enter a valid number between 1 and 9.")
                    continue
            else:
                # AI move
                print("The AI is thinking...")
                time.sleep(1)  # Simulate AI processing time
                move = self.get_ia_move()
            self.board[move] = self.current_player  
            turn += 1
            
            if self.check_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                return
            elif self.check_draw():
                self.print_board()
                print("It's a draw!")
                return

            self.alternate_player()
            time.sleep(1)  # Pause between turns

        print("Game over. No winner.")
# Menu for the game
def main():
    print("Welcome to Tic-Tac-Toe!")
    print("1. Play against a friend")
    print("2. Play against the computer (AI)")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        mode = "friend"
    elif choice == "2":
        mode = "ia"
    else:
        print("Invalid choice. Please restart the game.")
        return

    game = TicTacToe()
    game.start_game(mode)

if __name__ == "__main__":
    main()