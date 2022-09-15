# .........................[imports]............................
import nextcord
from nextcord import Interaction
from nextcord.ext import commands

# .........................[helpcmd class]......................
class helpcmd(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    # Help commands
    @nextcord.slash_command(name="help", description="Get information about the bot" )
    async def helpMessage(self, interaction: Interaction):

        # response embed
        embed = nextcord.Embed(title= "HELP", description="jBot", color=0x00ff00)
        embed.add_field(name= "Bot Name", value= "jBot", inline= False)

        # response
        await interaction.response.send_message()

# .........................[setup function]....................
def setup(client):
    client.add_cogs(helpcmd(client))