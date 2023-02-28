import discord
from discord.ext import commands

settings = {

"amount": "YOUR_AMOUNT",
"message": "YOUR_MESSAGE",
"token": "YOUR_TOKEN"

}

#Discord_Nuke_Tool
intents = discord.Intents.all()

bot = commands.Bot(intents=intents)

@bot.command()
async def raid(ctx):
    spam = settings["message"]
    for x in range(settings["amount"]):
        await ctx.send(spam)

bot.run(settings["token"])

#I DONT WANT TO MAKE MY NUKE TOOL OPEN-SOURCE, IF YOU REALLY WANT DO THIS TOOL, I CAN MAKE YOU CONTRIBUTOR, DM ME: Solar#1845
