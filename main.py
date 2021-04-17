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





























#ditto

















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
