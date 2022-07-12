import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from cogs.api.API import API1, ID
from cogs.Fn.function import fncheck, fnmode





class status(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @slash_command(guild_ids=[ID],description='Show Status Player')
    async def status(
        self,
        ctx,
        name: Option(str, "Enter You Name",require=True),
        mode: Option(str, "mode", choices=['osu','taiko','cbt','mania'], default='osu'),
        chorice : Option(str, "T = Showdata",choices=['True','False'], require=False,default='F')
    ):
        embed = discord.Embed(color=0xF4BFBF, timestamp=discord.utils.utcnow())
        embed.title ='Welcome to Osu Bot Status'
        
        try:
            M = fnmode(x=mode)
            OSU = API1(name=name,mode=M)
            embed.add_field(name='🎎Name', value=f'`[{OSU["uname"]}]`', inline=True)
            embed.add_field(name='🔰Level', value=f'`[{OSU["level"]:.0f}]`', inline=True)
            embed.add_field(name='🏆Rank_Total', value=f'`[#{OSU["rank"]}]`', inline=False)
            embed.add_field(name='🚀Performance', value=f'`[{OSU["pp"]}pp]`', inline=True)
            embed.add_field(name='🎯Accuracy', value=f'`[{OSU["acc"]:.2f}%]`', inline=True)
            embed.add_field(name='🎖️Rank_from', value=f'`[#{OSU["rankfrom"]}]` || `[From {OSU["From"]}]`', inline=False)
            embed.add_field(name='☃️Play_Count', value=f'`[{OSU["play"]}]`', inline=False)
            embed.add_field(name='🗓️join_Data', value=f'`[{OSU["join"][:10]}]`', inline=False)
            embed.add_field(name='✈️Go TO Web', value=f'{OSU["Profile"]}', inline=False)
            
            
            embed.set_thumbnail(url=f'{OSU["imge"]}')
            embed.set_footer(text='🛠️ Dev By Wongsakron', icon_url=f'{OSU["icon"]}')
        except:
            embed = discord.Embed(color=0xFF0000 ,timestamp=discord.utils.utcnow())
            embed.description = 'Player information not found.'       
    
        chorice = fncheck(chorice=chorice)
        await ctx.respond(embed=embed,ephemeral=chorice)
        



def setup(bot):
    bot.add_cog(status(bot))
    