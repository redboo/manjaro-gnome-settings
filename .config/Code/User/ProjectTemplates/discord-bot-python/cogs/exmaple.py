"""Cog module: Example"""
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    async def test(self, ctx) -> None:
        await ctx.send('Test is done')


def setup(bot) -> None:
    bot.add_cog(Example(bot))
