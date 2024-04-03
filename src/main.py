class TicTacToe:
    def __init__(self, player1: str, player2: str):
        # Initialize the board
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        
        self.player1 = player1
        self.player2 = player2
        self.turn = 0

    def print_board(self):
        # Print the current board
        row = []
        for i in range(0, len(self.board)):
            for j in range(0, 3):
                if self.board[i][j] == "X":
                    row.append("X")
                elif self.board[i][j] == "O":
                    row.append("O")
                else:
                    row.append("_")
            print(row)
            row = []


    def make_move(self, row, col, turn):
        # Make a move on the board
        if self.turn == 0:
            self.board[row][col] = "X"
        else:
            self.board[row][col] = "O"

    def is_valid_move(self, row, col):
        # Check if the move is valid
        pass

    def is_winner(self, player):
        # Check if the player has won
        pass

    def is_board_full(self):
        # Check if the board is full
        pass

    def reset_board(self):
        # Reset the board for a new game
        pass

    def play_game(self):
        # Main game loop
        print("-----Welcome to TicTacToe-----")
        print()
        self.print_board()
        print()
        while True:
            print("------player one's turn-------")
            row = int(input("Row: "))
            column = int(input("Column: "))
            self.make_move(row, column, self.turn)
            self.print_board()
            self.turn = 1

            print("------player two's turn-------")
            row = int(input("Row: "))
            column = int(input("Column: "))
            self.make_move(row, column, self.turn)
            self.print_board()
            self.turn = 0
        
        


def main():
    game = TicTacToe(player1="X",player2="0")
    game.play_game()


if __name__ == "__main__":
    main()
