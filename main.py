# Import the required modules
import discord
import os
from discord.ext import commands 
from dotenv import load_dotenv
from insertGame import insertGame
from printText import printGame

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='/', intents=intents)

# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Set the commands for your bot




@bot.command()
async def functions(ctx):
    response = 'I am a simple Discord chatbot! I will reply to your command!'
    await ctx.send(response)

@bot.command()
async def game(ctx, *, arg):
    p=insertGame(arg)
    
    await ctx.send(f'Game data saved as: \n {printGame(p)}')

@bot.command()
async def stat(ctx):
    await ctx.send(" ")

@bot.command()
async def register(ctx):
    await ctx.send(" ")


# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('TOKEN'))

