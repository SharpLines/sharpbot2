import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.ext import commands, tasks
from itertools import cycle
from discord.voice_client import VoiceClient
import time
import random
from discord import Game
import youtube_dl
import pickle
import os

client = commands.Bot(command_prefix = '/')
client.remove_command('help')
status = cycle(['Шо бы сюда написатб'])

@client.event
async def on_ready():
    chang_status.start()
    print('Ебать работает')

@tasks.loop(seconds=0.5)
async def chang_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def help(ctx):
    await ctx.send("Доступные команды: /clear, /зачистка, /kick (Ник), /ban (Ник), /dice, /megadice")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, ammount=6):
    await ctx.channel.purge(limit=ammount)
    embed = discord.Embed(
        title='Сообщение удалено',
        colour=discord.Colour.green()
    )
    
    embed.set_image(url='https://cdn.discordapp.com/attachments/447540683574738952/588744831539347468/me_irl.gif')

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def зачистка(ctx):
    await ctx.channel.purge(limit=100)
    embed = discord.Embed(
        title='Произошла зОчистка',
        colour=discord.Colour.green()
    )
    
    embed.set_image(url='https://cdn.discordapp.com/attachments/447540683574738952/589700786338922509/image0-11-1.jpg')

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def dice(ctx):
    responses = ['1', '2', '3', '4', '5', '6', 'пошел нахуй']
    await ctx.send(random.choice(responses))

@client.command()
async def megadice(ctx):
    responsus = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33',
                 '34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64',
                 '65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95',
                 '96','97','98','99','100']
    await ctx.send(random.choice(responsus))

token = os.environ.get('BOT_TOKEN')
token = (str(token))