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
    #@commands.command()
    #async def whatmatters(self, ctx):
        #"""tells a user a heartfelt message"""
        #await ctx.reply('You. :heart:')
        #became an easter egg.
    @commands.command(aliases=['lookingforgroup'])
    async def lfg(self, ctx):
        """tells a user how to lfg"""
        embedVar = discord.Embed(title='So you wanna LFG? Read on, and find out!',
                                 description='Please go to the channel associated with whatever game you want to get '
                                             'people for (grab the role if you cannot see the channel,) put your LFG '
                                             'post (EX: LF2M IB,) and then @here. Please do not spam ping, '
                                             'and be sensible with your lfg request. Thank you.',
                                 color=0x228B22)
        await ctx.send(embed=embedVar)

    @commands.command()
    async def improveme(self, ctx):
        """Tells a user how to improve me"""
        await ctx.send(
            'Hi there! If you think you have ways to improve me, please visit <#825588900906008636> and put your idea '
            'there. Thank you!')

    @commands.command()
    async def openuserticket(self, ctx):
        await ctx.send('If you are having issues with a user, please open a ticket. See <#785937547384586280> for '
                       'more info, or DM a staff member. Tickets are preferred.')

    @commands.command(aliases=['fetchmsg', 'messagefetch'])
    async def fetchmessage(self, ctx, *, msgid):
        fetched = await ctx.fetch_message(msgid)
        await ctx.send('Message Fetched, posted by {a}: {b}'.format(a=fetched.author.name, b=fetched.content))

    @commands.command()
    async def prefix(self, ctx):
        await ctx.reply('My Prefix is: ~')



def setup(bot):
    bot.add_cog(GeneralCog(bot))