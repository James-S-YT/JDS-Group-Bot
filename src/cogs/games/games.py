# .........................[imports]............................
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from TicTacToe.view import TicTacView

# .........................[game class]......................
class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="tictactoe", description="Play a game of TicTacToe !")
    async def ticc(self, interaction: Interaction, p1 : nextcord.Member, p2 : nextcord.Member):
        await interaction.send(f"A Tic Tac Toe game has begun between {p1.mention} and {p2.mention}, it is now {p1.mention}'s turn.", view=TicTacView(p1,p2))

# .........................[setup function]....................
def setup(client):
    client.add_cog(Games(client))