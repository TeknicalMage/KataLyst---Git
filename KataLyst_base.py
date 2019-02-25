#KataLyst made by Teknical Mage
#12/3/2018
import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import logging
import time 
import random

x = 1   

log_filename = '[.log File in the same location]'
logging.basicConfig(filename=log_filename, level=logging.INFO)

TOKEN =''

players = {}

scope = scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('[Json File Location]', scope)
gc = gspread.authorize(creds)

sheet = gc.open('[Google Sheets Name here]').sheet1

current = time.asctime(time.localtime(time.time()))
broken = 2  

bot = commands.Bot(command_prefix=";")
sh = gc.create(current)
sxrwewer

@bot.event  
async def on_ready():
    print ("Good to Go")
    print ("I am running on " + bot.user.name)
    print ("with the ID" + bot.user.id) 
    logging.info("The Bot joined")
    
    
@bot.event
async on_message(message):
    it = time.asctime(time.localtime(time.time()))
    global broken
    server = message.server  
    author = message.author 
    content = message.content
    channel = message.channel
    print ('[{}] {}: {}: {} '.format(server, author, channel, content)) 
    logging.info('[{}] {}: {}: {} '.format(server, author, channel, content)) 
    sheet.update_cell(broken,1, '[{}] {}: {}: {} '.format(server, author, channel, content))
    sheet.update_cell(broken,2, it)
    broken = broken + 1
    await bot.process_commands(message) 

@bot.command(pass_context=True)
async def ping(ctx):
    tot = random.randint,range(6)
    if tot == 1:
        await bot.say("Neet") 
    elif tot == 2: 
        await bot.say("Can't go like that")
    elif tot == 3:
        await bot.say("I don't respond to communist demands")
    elif tot == 4:
        await bot.say("Just like the Simulations")
    elif tot == 5:
        await bot.say("What do you mean?")
    else:
        await bot.say("No u")
    print ("user has pinged")
    
@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)
        

@bot.event
async def leave_server(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()

    
@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()
    
@bot.command(pass_context=True)
async def commandz(ctx):
    await bot.say("#help  - get a list of commands \n#ping - ping the bot \n#echo - repeat a line you want \n#join - join the server \n#leave - leave the server")   

@bot.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await bot.say(output)
       
bot.run(TOKEN)


