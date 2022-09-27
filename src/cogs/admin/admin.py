# .........................[imports]............................
import nextcord, datetime, asyncio
from utils import time2sec
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
            await interaction.send("You or I don't have the required permission.", ephemeral=True)
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

    @nextcord.slash_command(name="unban", description="Unbans a specified member.")
    @commands.has_permissions(ban_members=True)
    async def unban(self, interaction : Interaction, member : nextcord.Member = SlashOption(description="Member to unban", required=True), *, reason=None):
        await member.unban(reason = reason)
        await interaction.send(f'{member} has been unbanned.')

    @unban.error
    async def unban_err(self, interaction: Interaction, error):
        if isinstance(error, nextcord.errors.Forbidden):
            await interaction.send("You or I don't have the required permission.", ephemeral=True)
        else:
            raise error

    @nextcord.slash_command(name="mute", description="Mutes a specified member.")
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, interaction : Interaction, member : nextcord.Member = SlashOption(description="Member to mute", required=True), time : str = SlashOption(description = "Mute duration. (50s, 4h, 7d...)", required=True) ,*, reason=None):
        ftime = time2sec(time)
        await member.timeout(timeout = nextcord.utils.utcnow() + datetime.timedelta(seconds = ftime), reason = reason)
        await interaction.send(f'{member} has been muted for {time}.')

    @timeout.error
    async def timeout_err(self, interaction: Interaction, error):
        if isinstance(error, nextcord.errors.Forbidden):
            await interaction.send("You or I don't have the required permission.", ephemeral=True)
        else:
            raise error

    @nextcord.slash_command(name="unmute", description="Unmutes a specified member.")
    @commands.has_permissions(moderate_members=True)
    async def untimeout(self, interaction : Interaction, member : nextcord.Member = SlashOption(description="Member to unmute", required=True), *, reason=None):
        await member.timeout(timeout = None, reason = reason)
        await interaction.send(f'{member} has been unmuted.')

    @untimeout.error
    async def untimeout_err(self, interaction: Interaction, error):
        if isinstance(error, nextcord.errors.Forbidden):
            await interaction.send("You or I don't have the required permission.", ephemeral=True)
        else:
            raise error

    @nextcord.slash_command(name="tempban", description="Temporarily bans a specified member.")
    @commands.has_permissions(ban_members=True)
    async def tempban(self, interaction : Interaction, member : nextcord.Member = SlashOption(description="Member to tempban", required=True),time : str = SlashOption(description = "Duration of the ban. (50s, 4h, 7d...)", required=True), *, reason=None):
        await member.ban(reason = reason)
        await interaction.send(f'{member} has been banned.')
        await asyncio.sleep(time2sec(time))
        await member.unban()
        await interaction.send(f'{member} has been unbanned.')

    @tempban.error
    async def tempban_err(self, interaction: Interaction, error):
        if isinstance(error, nextcord.errors.Forbidden):
            await interaction.send("You or I don't have the required permission.", ephemeral=True)
        else:
            raise error

# .........................[setup function]....................
def setup(client):
    client.add_cog(Admin(client))