import discord
from discord.ext import commands


class OwnerCog(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['load', 'load_cog', 'cog_load'], hidden=True)
    @commands.is_owner()
    async def cogload(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(aliases=['unload', 'cog_unload', 'unload_cog'], hidden=True)
    @commands.is_owner()
    async def cogunload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(aliases=['reload', 'reload_cog', 'cog_reload'], hidden=True)
    @commands.is_owner()
    async def cogreload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(aliases=['objectiveadd'])
    @commands.is_owner()
    async def addobjective(self, ctx, *, msgid):
        """adds objective to a channel"""
        suggestion = await ctx.fetch_message(msgid)
        channel = self.bot.get_channel(825566825805905940)
        embedVar = discord.Embed(title='OBJECTIVE ACQUIRED',
                                 description='Objective added: {}'.format(suggestion.content))
        await channel.send(embed=embedVar)
        await ctx.send('Objective addition successful. Thank you.')
    @commands.command()
    @commands.is_owner()
    async def goodnight(self, ctx):
        await ctx.send('Shutting down now.')


def setup(bot):
    bot.add_cog(OwnerCog(bot))