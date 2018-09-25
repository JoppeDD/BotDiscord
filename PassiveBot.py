import discord
from discord.ext import commands

Token = 'NDkzODY0MTY3Mjg0MDE1MTA0.DovY1A.we3DSt029qKH2DL9uzSVeMYH9rk'

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print('ready')


@client.event
async def on_message(message):
    author = message.author
    message = message.content
    print('{} sent by {}'.format(message, author))


# @client.event
# async def on_message_delete(message):
#     author = message.author
#     content = message.content
#     channel = message.channel
#     await client.send_message(channel, '{}: {}'.format(content, author))


@client.event
async def


client.run(Token)
