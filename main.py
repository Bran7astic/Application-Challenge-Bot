import discord
import os
from dotenv import load_dotenv
from sheets import get_application_counts
import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.typing = True

load_dotenv()
token = os.getenv('DISCORD_TOKEN') 

bot = discord.Client(intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')

    CHANNEL_ID = 1505983005548613732

    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        embed = discord.Embed(
            title = '🎯 LEADERBOARD',
            description="📊 The current rankings are...",
            color=discord.Color.dark_gold(),
            timestamp=datetime.datetime.now(datetime.timezone.utc)        
        )
    
        app_counts = get_application_counts()
        app_counts = dict(sorted(app_counts.items(), key=lambda item: item[1], reverse=True))

        max_count = max(app_counts.values())

        for name, count in app_counts.items():
            prefix = "⭐️" if count == max_count else ""
            embed.add_field(name=f"{prefix} {name}", value=f"Apps: {count}")

        embed.add_field(name="Wanna join?", value="Add a sheet with your name to the [Application Tracker](https://docs.google.com/spreadsheets/d/13mV8ePdSnflnxogMRZGRWnJmrITVoxhn0Qt0gc0DKYA/edit?gid=1490322798#gid=1490322798)!", inline=False)

        await channel.send(embed=embed)
    else: 
        print("Channel not found.")    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
        



bot.run(token)
