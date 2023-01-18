import discord
import __text__
from discord.ext import commands
from art import *


settings = {

"amount": "YOUR_AMOUNT",
"message": "YOUR_MESSAGE"

}

#Discord_Raid_Tool
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="",intents=intents)

@bot.command()
async def raid(ctx):
    spam = settings["message"]
    for x in range(settings["amount"]):
        await ctx.send(spam)

bot.run("YOUR_TOKEN")
