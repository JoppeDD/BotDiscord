import discord
import random
from discord.ext import commands

Token = 'NDkzODY0MTY3Mjg0MDE1MTA0.DovY1A.we3DSt029qKH2DL9uzSVeMYH9rk'

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print('ready')


@client.event
async def on_message(message):
    # sender = message.author
    # message = message.content
    # print('{} send by {}'.format(sender, sender))
    print('a user send a message')
    await client.process_commands(message)


# @client.command()
# async def gaydar(person):
#     getal = random.randint(1,2)
#     if (getal == 1):
#         await client.say('')


@client.command()
async def ping():
    await client.say('Pong!')


@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)


client.run(Token)
