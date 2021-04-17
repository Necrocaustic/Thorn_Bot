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

    @commands.command()
    async def zodiac(self, ctx, *, UserID):
        """Calls the user a Babylonian Racist"""
        await ctx.send(
            'Hey there, <@{}>, you ancient Babylonian racist. https://vm.tiktok.com/ZMeUcjhSB/ . Have fun!'.format(UserID)
        )
    @commands.command()
    async def goldstar(self, ctx):
        """You tried (TM)"""
        await ctx.send('https://tenor.com/view/ahtf-gif-5633413')


def setup(bot):
    bot.add_cog(FunCog(bot))
