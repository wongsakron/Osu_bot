import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
data = os.getenv("BOT")
owner = os.getenv("OWNER")

class wyn_bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.token = data
        super().__init__(*args, **kwargs)

bot = wyn_bot(owner_id=[owner], case_insensitive=True)


@bot.event
async def on_ready():
    print(f'{bot.user} is Ready')

if __name__ == "__main__":
    for file in os.listdir('./cogs'):
        if file.endswith('.py') and not file.startswith('__'):
            bot.load_extension(f'cogs.{file[:-3]}')

    bot.run(bot.token)