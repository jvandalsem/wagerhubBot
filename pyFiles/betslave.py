from discord.ext import commands
from dotenv import load_dotenv
from wagerBot import *
from helpers import *
from liveScores import *
import teams
import discord
import os
import time
import pandas
import mysql.connector

os.environ['MOZ_HEADLESS'] = '1'

wager = formDriver()
tracking = True

load_dotenv()
try:
    TOKEN = os.getenv('DISCORD_TOKEN')
    print('Discord Dev great success')
except:
    print('Discord Dev no good')

help_command = commands.DefaultHelpCommand(no_category = 'Commands')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'),
                   help_command=help_command)
#
try:
    cnx = mysql.connector.connect(user=os.getenv('mysql_user'),
                                  password=os.getenv('mysql_pass'),
                                  host=os.getenv('mysql_host'),
                                  database=os.getenv('mysql_db'))
    cursor = cnx.cursor(buffered=True)
    print('MySQL very good very nice')
except Exception as err:
    print('Error')
    print(err)
    exit()

def exec(query):
    try:
        cursor.execute(query)
        cnx.commit()
        return cursor.fetchall()
    except Exception as err:
        print('Error exec()')
        print(err)

@bot.command(name='login',brief='-> Login to WagerHub account')
async def bot_login(ctx,*args):
    if str(ctx.author.id) in [a[0] for a in exec('SELECT disc_id FROM betUsers')]:
        creds = exec("SELECT username, pass FROM betUsers WHERE disc_id = '{}'".format(ctx.author.id))
        wager.setCreds(creds[0][0],creds[0][1])
        await ctx.send('Logged in as {}'.format(creds[0][0]))
    else:
        if len(args)<2:
            await ctx.send('Please provide WagerHub login credentials')
        else:
            wager.setCreds(args[0],args[1])
            exec("INSERT INTO betUsers (username, pass, disc_id) values ('{}', '{}', '{}')".format(args[0],args[1],ctx.author.id))
            await ctx.send('Successfully logged in to WagerHub account for {}'.format(args[0]))
@bot.command(name='open',brief='-> Your open bets')
async def bot_openBets(ctx):
    await ctx.send(wager.getOpenBets())

@bot.command(name='balance',brief='-> Your current book balance')
async def bot_getSports(ctx):
    await ctx.send(wager.getWinnings())

@bot.command(name='sports',brief='-> Sports you can bet on.')
async def bot_getSports(ctx):
    await ctx.send(wager.getSports())

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

@bot.command(name='track',brief='-> <league> <team> <freq> (in minutes). Get updates on game based on frequency.')
async def bot_track(ctx,*args):
    game = [a for a in formatLS(scrapetheScore(args[0].lower())) if args[1] in a or args[1] in a.lower()]
    print(game)
    check1 = checkTeams(args[0])
    if args[1].lower() not in check1:
        await ctx.send("Master, I don't believe the {} are an {} team.".format(args[1],args[0].upper()))
    elif len(game)==0:
        await ctx.send("Master, I don't believe the {} are playing today".format(args[1]))
    else:
        while tracking:
            game = [a for a in formatLS(scrapetheScore(args[0].lower())) if args[1] in a or args[1] in a.lower()]
            await ctx.send(game[0])
            time.sleep(int(args[2])*60)



@bot.command(name='stop',brief='-> <league> <game> stop tracking a game')
async def bot_getSports(ctx):
    tracking = False
bot.run(TOKEN)
