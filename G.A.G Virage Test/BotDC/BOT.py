import discord
import subprocess

TOKEN = 'Put the token of your dc bot'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Connected as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == "!rejoin":
        await message.channel.send("Connecting to the vip...")
        subprocess.Popen([r"Path of your ahk v2", r"C:\Users\33616\Desktop\G.A.G Virage Test\AHK\RejoinGAG.ahk"])

client.run(TOKEN)