import discord
import os
from dotenv import load_dotenv
from sheets import get_application_counts

intents = discord.Intents.default()
intents.message_content = True
intents.typing = True

load_dotenv()
token = os.getenv('DISCORD_TOKEN') 

bot = discord.Client(intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "counts" in message.content.lower():
        await message.channel.send(get_application_counts())



bot.run(token)
