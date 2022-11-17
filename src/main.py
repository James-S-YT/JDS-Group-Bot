# main file for the project

#? ......................[ Imports ]...........................
# Built-in modules.
import os

# Nextcord modules.
import nextcord
from nextcord.ext import commands

#External modules.
from dotenv import load_dotenv

#? ......................[ Variables ].........................
#* Tokens
load_dotenv()
_Token = (os.getenv('token'))     #<- discord bot token>

#* Admin IDs
_adminUserID  = [ 395592439110565898 ]  # <- IDs of Admin Users
_adminGuildID = [ 909422700462751755 ]  # <- ID of Admin Guild (Server)


#? ......................[ Client init ].......................
intents = nextcord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "jb!", intents = intents)

#? ......................[on_ready event].....................
@client.event
async def on_ready():
    print("--------------------------------------------------")
    print(f'''linked successfully!! 🟢

Status:-
Appication ID   : {client.user.id}
Appication name : {client.user}
State           : Online
Ping            : {round(client.latency * 1000)}
''')
    print("--------------------------------------------------")

#? ......................[Main-code]...........................
# test cmd
@client.command()
async def status(ctx):
    await ctx.send(f"I'm alive, \nand logged in as '{client.user}', \n**Ping:** *{round(client.latency * 1000)}*")
    await ctx.send(f":sweat_smile:")
 
# Cogs
innitial_extensions = []

for i in os.listdir("cogs"):
    if i.endswith(".py"):
        innitial_extensions.append("cogs." + i[:-3])

#? ......................[ Run ]...............................
if __name__ == '__main__' :
    for extension in innitial_extensions:
        client.load_extension(extension)
    client.run(str(_Token))
