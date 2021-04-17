import discord
from discord.ext import commands

class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.get_channel(819009513041559572)
        await channel.send(
            'Everyone welcome our newest member to the server, {b}! {a}, please stop by <#755448631187996773> to get '
            'some roles, allowing you access to color roles and access to the game channels. Thank you!'.format(
                a=member.mention, b=member.mention))
        embed = discord.Embed(title='New Member Incoming!',
                              description='Welcome to Phant0m! Enjoy talking about anything you wish, sending memes, '
                                          'playing games, and having a great time! Welcome {}!!'.format(
                                  member.mention), color=0x228B22)
        embed.set_image(
            url="https://images-ext-2.discordapp.net/external/E9zGnCcnFguwBq0-9oCLkVhHzqOPhCawjG5z0_vkrcY/%3Fitemid"
                "%3D16851952/https/media1.tenor.com/images/fa07c1868a49311e35b307a9dcaf809f/tenor.gif")
        channel = self.get_channel(542830671333163048)
        await channel.send(embed=embed)
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = discord.Embed(title='Oh No!', description='{} left Phant0m :('.format(member), color=0x228B22)
        embed.set_image(
            url="https://images-ext-2.discordapp.net/external/EHxF-Pa2pegAm-vu3wJO3PWp97FzgEe4oHAIBzKlN-M/%3Fitemid%3D5184314/https/media1.tenor.com/images/ce52606293142a2bd11cda1d3f0dc12c/tenor.gif")
        channel = self.get_channel(542830671333163048)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(EventCog(bot))