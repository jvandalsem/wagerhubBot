import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from wagerBot import formDriver
from helpers import *
from liveScores import scrapetheScore
import teams
import pandas
os.environ['MOZ_HEADLESS'] = '1'

wager = formDriver()
wager.setCreds('jvandal', 'booshy')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

help_command = commands.DefaultHelpCommand(no_category = 'Commands')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'),
                   help_command=help_command)

@bot.command(name='open',brief='-> Your open bets')
async def bot_openBets(ctx):
    await ctx.send(wager.getOpenBets())

@bot.command(name='sports',brief='-> Sports you can bet on.')
async def bot_getSports(ctx):
    await ctx.send(wager.getSports())

@bot.command(name='balance',brief='-> Your current book balance')
async def bot_getSports(ctx):
    await ctx.send(wager.getWinnings())

@bot.command(name='lines',brief='-> Which <sport> games you can bet on')
async def bot_getSports(ctx,*args):
    response = formatMD_GS(wager.selectBetType('single').listGames(args[0]))
    await ctx.send('Master, here are all the {} games you can bet on'.format(args[0].upper()))
    for a in range(len(response)):
        await ctx.send(response[a])

@bot.command(name='score',brief='-> score <league> <team> vs. <team>')
async def bot_getSports(ctx,*args):
    game = [a for a in formatLS(scrapetheScore(args[0].lower())) if args[1] in a or args[1] in a.lower()]
    print(game)
    check1 = checkTeams(args[0])
    if args[1].lower() not in check1:
        await ctx.send("Master, I don't believe the {} are an {} team.".format(args[1],args[0].upper()))
    elif len(game)==0:
        await ctx.send("Master, I don't believe the {} are playing today".format(args[1]))
    else:
        await ctx.send(game[0])

@bot.command(name='scores',brief='-> score <league>')
async def bot_getSports(ctx,*args):
    for a in formatLS(scrapetheScore(args[0].lower())):
        await ctx.send(a)

bot.run(TOKEN)
