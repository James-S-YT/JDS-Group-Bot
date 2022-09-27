import nextcord
from nextcord import Interaction

class TicTacToeButton(nextcord.ui.Button):
    def __init__(self, x, y):
        super().__init__()
        self.style = nextcord.ButtonStyle.gray
        self.label = "\u200b"
        self.row = y

        self.x = x
        self.y = y

    async def callback(self, interaction: Interaction):
        if self.view.game.board[self.x][self.y] != 0:
            return

        if self.view.game.turn % 2 == 1 and interaction.user == self.view.p1:
            self.style = nextcord.ButtonStyle.danger
            self.label = "X"
            #self.disabled = True
            self.view.game.play('x', (self.x, self.y))
            mess = f"It is now {self.view.p1.mention}'s turn"
        elif self.view.game.turn % 2 == 0 and interaction.user == self.view.p2:
            self.style = nextcord.ButtonStyle.success
            self.label = "O"
            #self.disabled = True
            self.view.game.play('o', (self.x, self.y))
            mess = f"It is now {self.view.p2.mention}'s turn"
        else:
            await interaction.send("Wait for your turn !", ephemeral=True)

        game_state = self.view.game.check_winner()
        if game_state != -1:
            if game_state == 0:
                mess = "The game is a tie !"
            elif game_state == "x":
                mess = f"{self.view.p1.mention} won !"
            elif game_state == "o":
                mess = f"{self.view.p2.mention} won !"

            for child in self.view.children:
                child.disabled = True

            self.view.stop()

        await interaction.response.edit_message(content = mess, view = self.view)

class ForfeitButton(nextcord.ui.Button):
    def __init__(self, y):
        super().__init__(style = nextcord.ButtonStyle.blurple, label = "Forfeit", row=y)
    
    async def callback(self, interaction: Interaction):
        for child in self.view.children:
            child.disabled = True

        self.view.stop()
        if interaction.user == self.view.player1:
            await interaction.response.edit_message(content=f"{self.view.player2.mention} won by forfeit.", view=self.view)
        else:
            await interaction.response.edit_message(content=f"{self.view.player1.mention} won by forfeit.", view=self.view)
