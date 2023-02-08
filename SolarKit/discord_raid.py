import discord

print('Launch "!raid_help" command in Discord after executing!')

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!raid_help':
        await message.channel.send('Usage: **"!raid + ID + message + MSG"**\nP.S bot must be in one or more same servers with your victim!')
    
    #if '!raid' in message.content
    ID = str
    MSG = str
    if message.content == '!raid ' + ID + ' !message ' + MSG:
        user = await client.fetch_user(ID)
        while True:
            await message.channel.send(MSG)

client.run('YOUR_TOKEN')