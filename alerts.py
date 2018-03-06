import discord
import asyncio
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='.') #add prefix, although it won't be used
channel_id = 'Channel ID here' # for future reference.
token = 'Insert BOT token here!' # bot token

@bot.event
async def on_message(message):
    if message.author == bot.user: #don't allow the bot to reply to it's own message
        return
    if True and message.channel.id == channel_id: #reply on any message and limit to alerts channel
        await bot.send_message(discord.Object(id=channel_id), '*Alerts spawn successfully recognized, beginning spam.*')
        await asyncio.sleep(1)
        spam = 0
        while spam != 5:
            spam += 1
            await asyncio.sleep(0.5)
            await bot.send_message(discord.Object(id=channel_id), 'An alerts worthy Pokémon has spawned, look above!')
        await bot.send_message(discord.Object(id=channel_id), 'Completed alerts spam. :wave:')

bot.run(token)
