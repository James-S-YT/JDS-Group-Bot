import nextcord,sys
from nextcord.ext import commands
from random import choice, shuffle

class YesOrNo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(description="Yes Or No Command Ask the bot a question")
    async def yesorno(self, interaction: nextcord.Interaction, question: str = nextcord.SlashOption(description="Question", required=True)):
        await interaction.response.defer()
        answers = ["Yes", "No", "Of Course", "Of Course ||No||", "I Can't Decide","是的，但是中文","不"]
        shuffle(answers)
        Embed = nextcord.Embed(title=question, description=f"{choice(answers)}", color=0xc9271e)
        await interaction.followup.send(embed=Embed)

# Setup
def setup(client):
    client.add_cog(YesOrNo(client))
