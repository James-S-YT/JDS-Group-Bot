# .........................[imports]............................
import nextcord
from buttons import TicTacToeButton, ForfeitButton
from tictactoe import TicTacToe

# .........................[TicTacToe View]............................
class TicTacView(nextcord.ui.View):
    def __init__(self, p1, p2):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.game = TicTacToe()

        #Makes the TicTacToe grid with Discord buttons
        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))
        self.add_item(ForfeitButton(y+1))