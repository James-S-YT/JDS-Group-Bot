# .........................[tictactoe class]......................
class TicTacToe:
    def __init__(self):
        self.turn = 1
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

    def play(self, move, pos):
        #Sets the value of the grid to the player's sign, x or o only if it is a 0, an empty case
        if self.board[pos[0]][pos[1]] == 0:
            self.board[pos[0]][pos[1]] = move
            self.turn += 1

    def check_winner(self):
        """
        Returns : x if player 1 won
                  o if player 2 won
                  0 if the game is a tie
                  -1 if the game is not finished
        """
        #Check horizontal
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != 0:
                return self.grid[i][0]

        #Check vertical
        for i in range(3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != 0:
                return self.grid[0][i]

        #Check diag 1
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != 0:
            return self.grid[0][0]
        
        #Check diag 2
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[1][1] != 0:
            return self.grid[1][1]

        #Check Tie
        #Counting every 0's in the grid
        comp = 0
        for i in self.grid:
            for j in i:
                if j == 0:
                    comp+=1
        
        #If there is no 0's there is no empty case
        if comp == 0:
            return 0
        
        #The game is still going
        return -1