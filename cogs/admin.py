import discord
from discord.ext import commands

class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['dmgcontrol', 'dmgcntrl', 'lock'])
    async def damagecontrol(ctx):
        """ADMIN ONLY COMMAND. Locks channel for time speficified, in seconds."""
        if ctx.message.author.guild_permissions.administrator:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.send(ctx.channel.mention + " ***is now in lockdown.***")

        else:
            await ctx.send('You can\'t use that, you silly goose! You aren\'t an admin. I\'m not that stupid!')

    @commands.command(aliases=['unlockchannel', 'unlock', 'unlckchnl'])
    async def dmgcontrolend(ctx):
        """ADMIN ONLY. Causes a locked channel to unlock."""
        if ctx.message.author.guild_permissions.administrator:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send(ctx.channel.mention + ' is now **unlocked!**')
        else:
            await ctx.send('Think you\'re funny, huh?')
            await ctx.send('https://tenor.com/view/facepalm-dismay-disappointed-stressed-this-bitch-gif-17906721')


def setup(bot):
    bot.add_cog(AdminCog(bot))
