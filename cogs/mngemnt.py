import discord
from discord.ext import commands

class ManagementCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=['issuereport'])
    async def reportissue(self, ctx, *, issue):
        """allows a user to report a bug"""
        channel = self.get_channel(825566825805905940)
        embedVar = discord.Embed(title='**ISSUE REPORTED**',
                                 description='ISSUE REPORTED BY {a}; Issue: {b}'.format(a=ctx.author, b=issue))
        await channel.send(embed=embedVar)
        await ctx.send('Issue reported. Thank you for your help.')


def setup(bot):
    bot.add_cog(ManagementCog(bot))
