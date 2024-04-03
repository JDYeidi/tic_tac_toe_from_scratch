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
        if row > 2 or row < 0 or col > 2 or col < 0:
            return False
        elif self.board[row][col] != 0:
            print(self.board[row][col])
            return False
        else:
            return True
        

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
            if self.turn == 0:
                print("------player one's turn-------")
                row = int(input("Row: "))
                col = int(input("Column: "))
                if self.is_valid_move(row, col) == True:
                    self.make_move(row, col, self.turn)
                    self.turn = 1
                    self.print_board()
                    print()
                else:
                    print("---Enter a valid movement---")
                    self.print_board()
                    print()

            if self.turn == 1:
                print("------player two's turn-------")
                row = int(input("Row: "))
                col = int(input("Column: "))
                if self.is_valid_move(row, col) == True:
                    self.make_move(row, col, self.turn)
                    self.turn = 0
                    self.print_board()
                    print()
                else:
                    print("---Enter a valid movement---")
                    self.print_board()
                    print()
            
            
            
        
        


def main():
    game = TicTacToe(player1="X",player2="0")
    game.play_game()


if __name__ == "__main__":
    main()
