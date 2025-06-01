import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # Enable message intent
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as testing python")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am your Discord bot!")

bot.run("MTM3NzkxNDc3MzczNTQ3MzE1Mg.GvjJkU.o6_yQOAggnYqqqb7P451b8zzHK0fBuZ3vRFO34")
O34")
