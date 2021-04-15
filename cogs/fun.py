import discord
from discord.ext import commands


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, target: discord.User = None):
        """Shows a Users avatar. Defaults to the Author"""
        if target is None:
            target = ctx.author
        await ctx.send(target.avatar_url)

    @commands.command(aliases=['hi'])
    async def hello(self, ctx):
        """Kenobi Gif"""
        await ctx.send('https://tenor.com/view/hello-there-hi-there-greetings-gif-9442662')


def setup(bot):
    bot.add_cog(FunCog(bot))
