# PUT ALL EASTER EGGS IN THIS COG AND THIS COG ONLY.
# Thankfully hsould be fairly easy. I hope anyways.
# check howtodoeastereggs in log file for info on transfer.
import discord
from discord.ext import commands


class EasterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        content = message.content.casefold()

        if "pog" in content:
            await message.reply('Stfu you\'re actually cringe wtf')
        if 'bonk' in content:  # casefold case-ignores fuckface #SHIT (although how the hell does it work for you and not me)
            # https://www.w3schools.com/python/ref_string_casefold.asp # I meant the await part #format #FUCK
            await message.reply('https://tenor.com/view/bonk-gif-18805247')
        if "fuck thorn" in content:
            await message.reply("You rn: {} https://tenor.com/view/lion-king-hyena-thorns-ouch-painful-gif-12925804".format(message.author.mention))
        if "flop" in content:
            await message.reply("god")
        if "Necro is amazing" in content:
            await message.reply('Totally. Y\'all should buy him Nitro')
        if "GME" in content:
            await message.reply(':rocket: to the moon :rocket:')
        if "thighs" in content:
            await message.reply('Mine are the thickest of them all')
        if "hellfire" in content:
            await message.reply('Ĩ̸̝͝ ̷̧̼̮̤̖͚̬̣͕̖̆̓̆ẉ̶̢̧̟̺̱͖̺̙̥̲̖͚̟̖̈̽̀͐̿̄͛͜į̴̣̱̻̬̦̪̱̜̪̳̲̬͖̟̳̏͒̕ͅl̴̻͎͋́́̋̏̑̉̾͗͌̒͌́̑̚̚͠l̴̛͔͖̱̜̪̹͔̞̯̺̘̜̣̟̝̘̾̍ͅ ̴̜̞̙̐͗̇̉̀͆̏r̵̛̛̹̍̆͛̈̆̎̈́̑̍̑̃̈̂̄́͗͝ą̸̝͙̩̼̠̖͉͉͙̹̥̘̫̗̲̩̝̥͚͊͐͋̇ḯ̸̧̨̧̯͍͖̰̻̣̖̙̺̙̭̺͍̳̣͔̩͐̄̀͊̏̀̋̅͋́̆̏̏̈̔́̈́̕͘͜͠n̷̨̡̡̲̤͚̺͒ ̷̡͉̰̠͓̥̙̅͛͛͑͐̋͐̂̑͂̚͠͠͠͝h̴̢̩̣̲̟͎͉͚̿͛̀̎̽̉̿̂̂̒́̓̐̀́͐͛̐̀̚͝ͅḛ̴̡̛̠̖̟̼͚̩̈̍̆͂̒̄̔̀̔͂̃͝͝ļ̷̗̱̖͔̰̩̯͈͇̔̎́̔̊̿͜l̶̨͚̻͍̤͕̪̟̣̭̞̱̪͚̬̩̤̻͍̔̍f̵̛̗̰̻͉̯͙̣̗̞̆̌͒̿̽̅̍̀̆̔͌̈́̈̂͑͘͜͝ỉ̴̡̢̨̮̞͈̖͙͙̺̣̻̠͕͙̮̰͍̀̌̅̓͒͗͌̑̈͂̕͘͜͜͠ŗ̴̨̧̜͇̞̻͖̞͛͋̕e̸̢̧̡̨̜̼̟̫̱̮̱̱̜̰̝͕͑͜ ̶̧̻̺̪̪̳̩͙͔̼̹̰͐͜ứ̸̧̡̛͚̞̩̤̜͕͍̮͖̇̃̅̀̑͊̾̈́̌̏̾̓̂͑́̚͝͝ͅp̸̙̰̣̱̫̱̯͈̩̌̎̊̔̕̚͝o̴͉͎̰͔̺̐̆̓̌̽̆̂̈́̌͐̄͂͝͝n̴̖̆̈́ ̸̛͔͔̗̖͖̠͛̋̈́̈́y̸̨̎̎̂̐̂̈́̾̽̄̂͌͋̅̓̂͆̐́̎͝o̶̮̺͍̰̩͖̾́̌̎̎͛͘u̴̢̢͇̗͎̣̰̞̲̲̎͆̈́̄̈̓̏͂͌͑̄̆̈́̋̏̕͜͠͝')
        if "Tex Mechanica" in content:
            await message.reply('YEEEEEEEE HAWWWWW')
        if 'what matters' in content:
            await message.reply('You. :heart:')
    @commands.command()
    async def hint(self, ctx):
        await ctx.reply('Your hint for today is:')
        await ctx.send('https://tenor.com/view/love-beating-heart-heart-beating-gif-15458916')

    @commands.command()
    async def hint2(self, ctx):
        await ctx.reply('Your second hint of the day is:')
        await ctx.send('https://tenor.com/view/plasma-gif-18879114')
    @commands.command()
    async def hint3(self, ctx):
        await ctx.reply('Your third **__and final__** hint of the day is:')
        await ctx.send('https://tenor.com/view/i-matter-lewis-thomas-stereoscope-the-red-wall-brian-white-gif-18822219')




"""Command attribute predeclared as hidden in class
If you want something unhidden,  use the 'hidden=False' kward
in the command decorator
"""


def setup(bot):
    bot.add_cog(EasterCog(bot))
