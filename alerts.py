import discord
import asyncio
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='.') #add prefix, although it won't be used

@bot.event
async def on_message(message):
    if message.author == bot.user: #don't allow the bot to reply to it's own message
        return
    alerts_channel = 'Channel ID here' #alerts channel ID, ignore everything else. 
    if 1 == 1 and message.channel.id == alerts_channel: #reply on any message and limit to alerts channel
        await bot.send_message(discord.Object(id='Channel ID here'), '*Alerts spawn successfully recognized, beginning spam.*')
        await asyncio.sleep(1)
        spam = 0
        while spam != 5:
            spam += 1
            await asyncio.sleep(0.5)
            await bot.send_message(discord.Object(id='Channel ID here'), 'An alerts worthy Pokémon has spawned, look above!')
        await bot.send_message(discord.Object(id='Channel ID here'), 'Completed alerts spam. :wave:')

bot.run('Insert BOT token here!')
