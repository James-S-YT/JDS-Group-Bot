# .........................[imports]............................
import nextcord
from nextcord import Interaction
from nextcord.ext import commands

# .........................[game class]......................
class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

# .........................[setup function]....................
def setup(client):
    client.add_cog(Games(client))