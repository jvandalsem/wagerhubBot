import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from wagerBot import formDriver
os.environ['MOZ_HEADLESS'] = '1'


wager = formDriver()
wager.setCreds('jvandal', 'booshy')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$')

@bot.command(name='openbets')
async def bot_openBets(ctx):
    await ctx.send(wager.getOpenBets())

@bot.command(name='getsports')
async def bot_getSports(ctx):
    await ctx.send(wager.getSports())

bot.run(TOKEN)
