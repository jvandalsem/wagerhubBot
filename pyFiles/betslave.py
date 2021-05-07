import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from wagerBot import formDriver
from helpers import formatMD_GS
os.environ['MOZ_HEADLESS'] = '1'

wager = formDriver()
wager.setCreds('jvandal', 'booshy')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

help_command = commands.DefaultHelpCommand(no_category = 'Commands')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'),
                   help_command=help_command)

@bot.command(name='OpenBets',brief='-> Your open bets')
async def bot_openBets(ctx):
    await ctx.send(wager.getOpenBets())

@bot.command(name='Sports',brief='-> Sports you can bet on.')
async def bot_getSports(ctx):
    await ctx.send(wager.getSports())

@bot.command(name='Balance',brief='-> Your current book balance')
async def bot_getSports(ctx):
    await ctx.send(wager.getWinnings())

@bot.command(name='Which',brief='-> Which <sport> games you can bet on')
async def bot_getSports(ctx,*args):
    response = formatMD_GS(wager.selectBetType('single').listGames(args[0]))
    for a in range(len(response)):
        await ctx.send(response[a])
        print(a)

bot.run(TOKEN)
