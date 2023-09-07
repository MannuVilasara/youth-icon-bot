import discord
from discord.ext import commands


class About(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(
        name="about", description="Get information about Youth Icon"
    )
    async def about(self, ctx: commands.Context):
        pass


async def setup(bot):
    await bot.add_cog(About(bot))
    print("Added About")
