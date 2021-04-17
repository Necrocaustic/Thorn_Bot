import discord
from discord.ext import commands

import sys
from config import *
import traceback

"""
intents = discord.Intents.default()
intents.typing = False
intents.members = True
"""


# UPDATE CHANNEL IDS SOMEWHERE IF YOU RUN OUT OF TIME IN CLASS
def get_prefix(bot, message):
    prefixes = ['~']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['cogs.admin',
                      'cogs.owner',
                      'cogs.mngemnt',
                      'cogs.easter',
                      'cogs.generaluse'
                      ]

bot = commands.Bot(command_prefix=get_prefix,
                   activity=discord.Activity(type=discord.ActivityType.playing,
                                             name='with Phant0m'),
                   intents=discord.Intents.all())

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print('Version: ', version)


@bot.command(aliases=['objectiveadd'])
async def addobjective(ctx, *, msg_id):
    """Adds Objective to Channel"""
    suggestion = await ctx.fetch_message(msg_id)
    channel = bot.get_channel(825566825805905940)
    embedVar = discord.Embed(title='OBJECTIVE ACQUIRED', description='Objective added: {}'.format(suggestion.content))
    await channel.send(embed=embedVar)
    await ctx.send('Objective added, thank you for contributing to the bot.')








@bot.command(aliases=['issuereport'])
async def reportissue(ctx, *, issue):
    """Allows a user to report found bugs."""
    channel = bot.get_channel(825566825805905940)
    embedVar = discord.Embed(title="**ISSUE REPORTED**", description="ISSUE: {}".format(issue), color=0x228B22)
    await channel.send(embed=embedVar)
    await ctx.send('Issue reported. Thank you for your help.')


@bot.command()
async def improveme(ctx):
    """Tells a user where to go if they want to improve me"""
    await ctx.send(
        'Hi there! If you think you have ways to improve me, please visit <#825588900906008636> and put your idea there. Thank you!')


@bot.command()
async def whatmatters(ctx):
    """Delievers a nice message to the author of the message."""
    await ctx.send('You, {}'.format(ctx.author.mention))


@bot.command(aliases=['looking for group'])
async def lfg(ctx):
    """Tells a user how to LFG"""
    embedVar = discord.Embed(title="So you wanna LFG? Read on, and find out!",
                             description="Please go to the channel associated with whatever game you are trying to LFG for, put your LFG post (example: LF2M IB) and then @here. Please do not spam pings, and be sensible with your LFG. Thank you!",
                             color=0x228B22)
    await ctx.send(embed=embedVar)







#admin cog, deal with later.
@bot.command(aliases=['dmgcontrol', 'dmgcntrl', 'lock'])
async def damagecontrol(ctx):
    """ADMIN ONLY COMMAND. Locks channel for time speficified, in seconds."""
    if ctx.message.author.guild_permissions.administrator:
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(ctx.channel.mention + " ***is now in lockdown.***")

    else:
        await ctx.send('You can\'t use that, you silly goose! You aren\'t an admin. I\'m not that stupid!')

#ditto

@bot.command(aliases=['unlockchannel', 'unlock', 'unlckchnl'])
async def dmgcontrolend(ctx):
    """ADMIN ONLY. Causes a locked channel to unlock."""
    if ctx.message.author.guild_permissions.administrator:
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(ctx.channel.mention + ' is now **unlocked!**')
    else:
        await ctx.send('Think you\'re funny, huh?')
        await ctx.send('https://tenor.com/view/facepalm-dismay-disappointed-stressed-this-bitch-gif-17906721')

#either make a general use cog, or put this in mgmt
# ready for import in 2.0.1
@bot.command(aliases=['fetchmsg', 'fetchmessage'])
async def fetch(ctx, *, msgid):
    """Fetches a message based off of a message ID"""
    if msgid != "":
        fetched = await ctx.fetch_message(msgid)
        await ctx.send('Your message, by {a}: {b}'.format(a=fetched.author.name, b=fetched.content))
    else:
        await ctx.send('You need a message ID, you silly goose. {}'.format(ctx.author.mention))


@bot.command(aliases=['userticketopen'])
async def openuserticket(ctx):
    await ctx.send(
        'If you are having issues with a user, please open a ticket. See <#785937547384586280> for more info, or DM a staff member. Tickets are preffered.')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(819009513041559572)
    await channel.send(
        'Everyone welcome our newest member to the server, {b}! {a}, please stop by <#755448631187996773> to get some roles, allowing you access to color roles and access to the game channels. Thank you!'.format(
            a=member.mention, b=member.mention))
    embed = discord.Embed(title='New Member Incoming!',
                          description='Welcome to Phant0m! Enjoy talking about anything you wish, sending memes, playing games, and having a great time! Welcome {}!!'.format(
                              member.mention), color=0x228B22)
    embed.set_image(
        url="https://images-ext-2.discordapp.net/external/E9zGnCcnFguwBq0-9oCLkVhHzqOPhCawjG5z0_vkrcY/%3Fitemid%3D16851952/https/media1.tenor.com/images/fa07c1868a49311e35b307a9dcaf809f/tenor.gif")
    channel = bot.get_channel(542830671333163048)
    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    embed = discord.Embed(title='Oh No!', description='{} left Phant0m :('.format(member), color=0x228B22)
    embed.set_image(
        url="https://images-ext-2.discordapp.net/external/EHxF-Pa2pegAm-vu3wJO3PWp97FzgEe4oHAIBzKlN-M/%3Fitemid%3D5184314/https/media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif")
    channel = bot.get_channel(542830671333163048)
    await channel.send(embed=embed)




@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        pass
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        await ctx.send(
            'There was an error. Try running the command again with the right parameters, or use ~reportissue to let my developer know about you seeing this. If you are running a command that require arguements, check to ensure all of the fields are filled. And yes, ~fetchmessage REQUIRES a message ID. You won\'t get anything without it.')


# keep_alive() don't need this
bot.run(token, bot=True, reconnect=True)
