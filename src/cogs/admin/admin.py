# .........................[imports]............................
import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

# .........................[admin class]......................
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
            await interaction.send("I or you don't have the required permissions.", ephemeral=True)
        else:
            raise error

    @nextcord.slash_command(name="ban", description="Bans a specified member.")
    @commands.has_permissions(ban_members = True)
    async def ban(self, interaction : Interaction, member : nextcord.Member = SlashOption(description="Member to ban", required=True), *, reason=None):
        await member.ban(reason = reason)
        await interaction.send(f'{member} has been banned.')

    @ban.error
    async def ban_err(self, interaction: Interaction, error):
        if isinstance(error, nextcord.errors.Forbidden):
            await interaction.send("I or you don't have the required permissions.", ephemeral=True)
        else:
            raise error

    @nextcord.slash_command(name="ban", description="Unbans a specified member.")
    @commands.has_permissions(ban_members=True)
    async def unban(self, interaction : Interaction, member : nextcord.Member = SlashOption(description="Member to unban", required=True), *, reason=None):
        await member.unban(reason = reason)
        await interaction.send(f'{member} a été unban.')

    @unban.error
    async def unban_err(self, interaction: Interaction, error):
        if isinstance(error, nextcord.errors.Forbidden):
            await interaction.send("I or you don't have the required permissions.", ephemeral=True)
        else:
            raise error

# .........................[setup function]....................
def setup(client):
    client.add_cog(Admin(client))