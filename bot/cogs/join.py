import discord
from discord.ext import commands
import requests
from utils.constants import WEBHOOK_URL


class Join(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="join", description="Join Our Server")
    async def join(self, ctx: commands.Context, gmail: str):
        if gmail[-10:] != "@gmail.com":
            await ctx.send("Please enter a valid Gmail")
            return
        requests.post(
            url=WEBHOOK_URL,
            data={
                "content": "New Request",
                "embeds": [
                    {
                        "title": f"{ctx.author} wants to join the server.",
                        "description": f"**__Gmail__**:\n {gmail}",
                        "color": 58368,
                    }
                ],
            },
        )
        await ctx.send("Sent")


async def setup(bot):
    await bot.add_cog(Join(bot))
    print("Added Join")
