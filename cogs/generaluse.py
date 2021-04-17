import discord
from discord.ext import commands
from config import *

class GeneralCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['statuwu','statowo'])
    async def status(self, ctx):
        """Tells the user the status of the bot."""
        await ctx.reply('Online and running: {}'.format(version))

    @commands.command()
    async def whoareyou(self, ctx):
        """tells the homies who the fuck i am"""
        embed = discord.Embed(title='Hello there! I am Thorn, Phant0m\'s cutsom bot.',
                              description='My creator is <@395813601316831254>, please reach out to him with any issues,'
                                          'or use the ~reportissue command. ',
                              color=0x228B22)
        embed.set_image(
            url='https://cdn.discordapp.com/attachments/763085775456829460/832782619157725184/thornbeta.jpg'
        )
        await ctx.send(embed=embed)
    @commands.command()


def setup(bot):
    bot.add_cog(GeneralCog(bot))