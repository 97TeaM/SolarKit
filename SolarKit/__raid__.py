import discord
import __text__
from discord.ext import commands
from art import *


#Discord_Raid_Tool
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="",intents=intents)

@bot.command()
async def raid(ctx):
    spam = ["@everyone @here loxed by 97tEaM"]
    while True:
        await ctx.send(spam)

bot.run("YOUR_TOKEN")
