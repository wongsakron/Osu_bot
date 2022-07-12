import discord
from discord.ext import commands
from discord.commands import slash_command, Option, user_command, message_command
from cogs.api.API import ID


class Myviwe(discord.ui.View): #class ui view
    def __init__(self, ctx):
        self.ctx = ctx  #input ctx
        super().__init__()

    async def interaction_check(self, interaction: discord.Interaction) -> bool: #chack user name = name
        if interaction.user == self.ctx.author:
            return True
        await interaction.response.send_message("you can't do this", ephemeral=True)
        return False


    @discord.ui.button(label="helloworld",style=discord.ButtonStyle.blurple) #button style = color
    async def button_1(self,button:discord.ui.Button,interaction:discord.Integration): 
        await interaction.response.send_message("you can")
    
    @discord.ui.select(placeholder="Selection. . .",  options=[
        discord.SelectOption(label="stacia", description="this is my name", emoji='⭐'),
        discord.SelectOption(label="renly", description="my 2nd name", emoji='💎'),
    ])
    async def myselect(self, select: discord.ui.Select, interaction: discord.Interaction):
        if select.values[0] == "stacia":
            mode = "0"
            await interaction.response.send_message("choice 1", ephemeral=True)
            
        elif select.values[0] == "renly":
            mode = "1"
            await interaction.response.send_message("choice 2", ephemeral=True)
            

class reference(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @slash_command(guild_ids=[ID],description='Show Status Player')
    async def button(self,ctx):

        view = Myviwe(ctx)
        
        await ctx.respond("text",view=view,ephemeral=True)



def setup(bot):
    bot.add_cog(reference(bot))