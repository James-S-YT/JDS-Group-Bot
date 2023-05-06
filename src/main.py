
import os
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, slash_command, SlashOption
from dotenv import load_dotenv

#? ......................[ Variables ].........................
#* Tokens
load_dotenv()
Token = os.getenv('_Token')     #<- discord bot token>

#* Admin IDs
adminUserID  = os.getenv('_adminUserID')    # <- IDs of Admin Users
adminGuildID = os.getenv('_adminGuildID')   # <- ID of Admin Guild (Server)
intents = nextcord.Intents.all()

#? ......................[ Client init ].......................
intents = nextcord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "jb!", intents = intents)

#? ......................[on_ready event].....................
@client.event
async def on_ready():
    print("--------------------------------------------------")
    print(f'''linked successfully!!

Status:-
Appication ID   : {client.user.id}
Appication name : {client.user}
State           : Online
Ping            : {round(client.latency * 1000)}
''')
    print("--------------------------------------------------")

#? ......................[Main-code]...........................
# test cmd



#? ......................[Slash-cmds]..........................
# This is a simple slash commands


@client.slash_command(description="Replies with pong!")
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!", ephemeral=True)

@client.slash_command(description="My first slash command")
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

#Simple drop down commands

class Dropdown(nextcord.ui.Select):
    def __init__(self):
        # Set the options that will be presented inside the dropdown
        options = [
            nextcord.SelectOption(
                label="Red", description="Your favourite colour is red", emoji="🟥"
            ),
            nextcord.SelectOption(
                label="Green", description="Your favourite colour is green", emoji="🟩"
            ),
            nextcord.SelectOption(
                label="Blue", description="Your favourite colour is blue", emoji="🟦"
            ),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(
            placeholder="Choose your favourite colour...",
            min_values=1,
            max_values=1,
            options=options,
        )
    async def callback(self, interaction: nextcord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        await interaction.response.send_message(f"Your favourite colour is {self.values[0]}")

        
class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())

@client.slash_command()
async def colour(interaction):
    """Sends a message with our dropdown containing colours"""

    # Create the view containing our dropdown
    view = DropdownView()

    # Sending a message containing our view
    await interaction.send("Pick your favourite colour:", view=view)



#? ......................[ Run ]...............................
if __name__ == '__main__' :
    client.run(Token)