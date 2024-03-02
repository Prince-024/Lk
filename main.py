import os 
os.system("pip install discord")
# This example requires the 'message_content' privileged intent to funct
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from PIL import Image, ImageDraw, ImageFont
import io
import os
intents = discord.Intents.all()
intents.message_content = True
bot = Bot('!', intents=intents)

@bot.command()
async def ping(ctx):
    ping = round(bot.latency* 1000)
    await ctx.send(f"{int(ping)}ms")
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!emoji'):
        
        ping = round(bot.latency* 1000)
        
        await message.channel.send(f"{int(ping)}ms")

bot.run(os.environ["TOKEN"])

        


