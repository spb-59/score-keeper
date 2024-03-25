# Import the required modules
import discord
import os
from discord.ext import commands 
from dotenv import load_dotenv
from insertGame import insertGame
from printText import printGame
from insertPlayer import register_player
from showStats import showLeaderboard,showStat

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Set the commands for your bot




@bot.command()
async def majong(ctx):
  
    await ctx.send(f" Hello! Use the following command: \n ``` /game - To log a game \n /leaderboard - to get current leaderboard \n /register -to register a player \n /stat - to view player stat ``` ")

@bot.command()
async def game(ctx, *, arg):
    p=await insertGame(ctx,arg)
    if p==None:
        await ctx.send("``` Please Try Again ```")
        return
    
    await ctx.send(f'Game data saved as: \n {printGame(p)}')

@bot.command()
async def stat(ctx,args):

    await ctx.send(showStat(args))

@bot.command()
async def leaderboard(ctx):
    await ctx.send(  showLeaderboard())

@bot.command()
async def register(ctx,args):
    await register_player(ctx,args)


# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv('TOKEN'))

