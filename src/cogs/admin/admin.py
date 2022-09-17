# .........................[imports]............................
import nextcord
import datetime
import asyncio
from nextcord import Interaction, SlashOption
from nextcord.ext import commands

def time2sec(time):
    # There is actually a library to make this whole thing easier, humanfriendly, but it would add a dependency.
    mult = {
        'ms': 0.001, 
        's': 1, 
        'm': 60, 
        'h': 3600, 
        'd': 86400, 
        'w': 604800, 
        'y': 31564000, 
    }

    nb = ''
    unit = ''
    for i in time:
        try:
            int(i)
            nb += i
        except:
                unit += i
    ftime = float(int(nb)*mult[unit])
    return ftime 

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

    @nextcord.slash_command(name="timeout", description="Unbans a specified member.")
    @commands.has_permissions(ban_members=True)
    async def unban(self, interaction : Interaction, member : nextcord.Member = SlashOption(description="Member to unban", required=True), *, reason=None):
        await member.unban(reason = reason)
        await interaction.send(f'{member} has been unbanned.')

    @unban.error
    async def unban_err(self, interaction: Interaction, error):
        if isinstance(error, nextcord.errors.Forbidden):
            await interaction.send("I or you don't have the required permissions.", ephemeral=True)
        else:
            raise error

    @nextcord.slash_command(name="timeout", description="timeouts a specified member.")
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, interaction : Interaction, member : nextcord.Member = SlashOption(description="Member to timeout", required=True), time : str = SlashOption(description = "Duration of the timeout. (50s, 4h, 7d...)", required=True) ,*, reason=None):
        ftime = time2sec(time)
        await member.timeout(timeout = nextcord.utils.utcnow() + datetime.timedelta(seconds = ftime), reason = reason)
        await interaction.send(f'{member} has been timeouted for {time}.')

    @timeout.error
    async def timeout_err(self, interaction: Interaction, error):
        if isinstance(error, nextcord.errors.Forbidden):
            await interaction.send("I or you don't have the required permissions.", ephemeral=True)
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
            await interaction.send("I or you don't have the required permissions.", ephemeral=True)
        else:
            raise error

    @nextcord.slash_command(name="tempban", description="Ban temporairement un membre du serveur", guild_ids=ids)
    @commands.has_permissions(ban_members=True)
    async def tempban(self, interaction : Interaction, member : nextcord.Member = SlashOption(description="Member to unban", required=True),time : str = SlashOption(description = "Duration of the timeout. (50s, 4h, 7d...)", required=True), *, reason=None):
        await member.ban(reason = reason)
        await interaction.send(f'{member} a été ban.')
        await asyncio.sleep(time2sec(time))
        await member.unban()
        await interaction.send(f'{member} a été unban.')

    @tempban.error
    async def tempban_err(self, interaction: Interaction, error):
        if isinstance(error, nextcord.errors.Forbidden):
            await interaction.send("Vous ou je n'ai pas les permissions requises.", ephemeral=True)
        else:
            raise error

# .........................[setup function]....................
def setup(client):
    client.add_cog(Admin(client))