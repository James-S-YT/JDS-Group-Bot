import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="kick", description="Kicks a specified member.")
    @commands.has_permissions(kick_members = True)
    async def kick(self, interaction : Interaction, member : nextcord.Member = SlashOption(description="Member to kick", required = True), *, reason=None):
        await member.kick(reason = reason)
        await interaction.send(f'{member} has been kicked.')

    @kick.error
    async def kick_err(self, interaction : Interaction, error):
        if isinstance(error, nextcord.errors.Forbidden):
            await interaction.send("I or you don't have the required permissions.")

def setup(client):
    client.add_cog(Admin(client))