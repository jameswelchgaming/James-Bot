import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='For !commands', type = 3))
    await client.send_message(member, 'Welcome to Jamess Server')
    print('Sent message to ' + member.name)



@client.event
async def on_message(message):
    if message.content == '!ping':
        await client.send_message(message.channel,'Pong')
    if message.content == '!img':
        em = discord.Embed(description='an cute girl')
        em.set_image(url='https://cdn.discordapp.com/attachments/505574076975284236/517855012744069120/Screenshot_82.png')
        await client.send_message(message.channel, embed=em)
    if ('Fuck') in message.content:
       await client.delete_message(message)
    if message.content.startswith('!random'):
        randomlist = ["Hello","Goodbye","Want to hear and joke??"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!hello'):
        await client.send_message(message.channel,'Hello, <@%s>'  %(message.author.id))
    if ('fuck') in message.content:
       await client.delete_message(message)
    if ('bitch') in message.content:
       await client.delete_message(message)
    if ('nigger') in message.content:
       await client.delete_message(message)
    if ('Nigger') in message.content:
       await client.delete_message(message)
    if message.content == '!botinfo':
        await client.send_message(message.channel,' Owner: Jameswelchgamig    Version:V.1    Made: 11-29-18    ')
    if message.content == '!help':
        await client.send_message(message.channel,'```                      James Bot Commands:              '
'                          !help: Shows this list                                                                                      '
      
'                          !botinfo:  Shows  The bot Info                                                    '

'                          !ping: Shows the ping                                                              '

'                          !img: Shows an image                                                                '

'                          !random: Says random sentences                                                       '

'                           !hello: Says hello                                                                  '

                                                    '---More Coming Soon--- ```')

    if message.content == '!test':
        em = discord.Embed (description='I Fucked')
        em.set_image(url='https://cdn.discordapp.com/attachments/505574076975284236/517855012744069120/Screenshot_82.png')
        await client.send_message(message.channel, embed=em)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='For !commands',type =3))
    print("Running...")

#client.event
#async def on_message(message):




client.run('NTE3ODU5Nzc5NTYxOTE0MzY5.DuNLKw.xzka2MvV0YAJFMRMXGnQ2bmkjx8')
