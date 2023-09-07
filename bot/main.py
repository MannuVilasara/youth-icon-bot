import discord
from discord.ext import commands
import os
from utils.constants import TOKEN


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!", help_command=None, intents=discord.Intents.all()
        )

    async def on_ready(self):
        pass


bot = Bot()


@bot.event
async def on_ready():
    for fn in os.listdir("bot/cogs/"):
        if fn.endswith(".py"):
            await bot.load_extension(f"cogs.{fn[:-3]}")
    await bot.tree.sync()
    print("Hey")


if __name__ == "__main__":
    bot.run(token=TOKEN)
