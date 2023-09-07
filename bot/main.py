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
        await load()


bot = Bot()


async def load():
    for fn in os.listdir("bot/cogs"):
        if fn.endswith(".py"):
            await bot.load_extension(f"cogs.{fn[:-3]}")


if __name__ == "__main__":
    bot.start(token=TOKEN)
