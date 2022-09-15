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
_Token = os.getenv('token')     #<- discord bot token>

#* Admin IDs
_adminUserID  = [ 395592439110565898, 557756298838409226 ]  # <- IDs of Admin Users
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
    embed = nextcord.Embed(title= "Current Status", description="jBot", color=0x00ff00)
    embed.add_field(name= "Appication ID", value= client.user.id, inline= False)
    embed.add_field(name= "Appication name", value= client.user, inline= False)
    embed.add_field(name= "State", value= "Online", inline= False)
    embed.add_field(name= "Ping", value= round(client.latency * 1000), inline= False)
    await ctx.send(embed = embed)

#? ......................[ cog ]...............................
for folder in os.listdir("./src/cogs"):
    for file in os.listdir(f"./src/cogs/{folder}"):
        if file.endswith(".py"):
            client.load_extension(f"cogs.{folder}.{file[:-3]}")

#? ......................[ Run ]...............................
if __name__ == '__main__' :
    client.run(str(_Token))
