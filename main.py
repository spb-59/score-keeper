# Import the required modules
import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from insertGame import insertGame
from printText import printGame
from insertPlayer import register_player
from showStats import showLeaderboard, showStat

# Create a Discord client instance and set the command prefix
intents = discord.Intents.all()
client = discord.Client(intents=intents)


class Help(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        await self.get_destination().send(
            " Hello! Use the following command: \n ``` !game - To log a game \n !leaderboard - to get current leaderboard \n !register -to register a player \n !stat - to view player stat ``` "
        )


bot = commands.Bot(command_prefix="!", intents=intents, help_command=Help())


# Set the confirmation message when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


# Set the commands for your bot


@bot.command()
async def mahjong(ctx):
    await ctx.send(
        " Hello! Use the following command: \n ``` -!game - To log a game \n -!leaderboard - to get current leaderboard \n -!register -to register a player \n -!stat - to view player stat ``` "
    )


@bot.command()
async def game(ctx, *, arg=""):
    if arg=="":
        await ctx.send('Ensure game is logged as `!game [player]:[score]....-[game name:optional]`')


    p = await insertGame(ctx, arg)
    if p is None:
        await ctx.send("``` Please Try Again, ensure game is logged as `!game [player]:[score]....-[game name:optional]` ```")
        return

    await ctx.send(f"Game data saved as: \n {printGame(p)}")


@bot.command()
async def stat(ctx, args=''):
    if args=="":
        ctx.send('Please specify player in stat command, `!stat [player]`')
    await ctx.send(showStat(args))


@bot.command()
async def leaderboard(ctx):
    await ctx.send(showLeaderboard())


@bot.command()
async def register(ctx, args=''):
    if args=="":
        ctx.send('Please specify player to register, `!register [player]`')
    await register_player(ctx, args)


# Retrieve token from the .env file
load_dotenv()
bot.run(os.getenv("TOKEN"))
