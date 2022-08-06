# main file for the project

#? ......................[ Imports ]...........................
# Built-in modules.
import os

# Nextcord modules.
import nextcord

#? ......................[ Variables ].........................
# Tokens
_Token = (os.getenv('token'))     #<- discord bot token>

# Admin IDs
_adminUserID = [395592439110565898]
_adminGuildID = 909422700462751755

#? ......................[ Client config ].....................
intents = nextcord.Intents.all()
intents.members = True
client = nextcord.Bot(command_prefix = "", intents = intents)

#? ......................[ Setup ].............................
@client.event
async def on_ready():
    print(f"I'm logged in as {client.user}")

#? ......................[Main-code]...........................
# test cmd
@client.command()
async def status(ctx):
    await ctx.send(f"I'm alive, \nand logged in as '{client.user}', \n**Ping:** *{round(client.latency * 1000)}*")
    await ctx.send(f":sweat_smile:")

#? ......................[ Run ]...............................
if __name__ == '__main__' :
    client.run(_Token)