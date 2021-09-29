#!/usr/bin/python3

from discord.ext import commands

# get our token from config.py
from config import token

import database

# database for tracking users' listenbrainz names


entries = database.dbcount()
print("entries: " + str(entries))

bot = commands.Bot(command_prefix='&')

@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong!")

@bot.command()
async def lbzsetup(ctx, arg):
	uid = ctx.author.id
	#print(uid)
	print("adding " + str(uid) + " to the db with username " + arg)
	

bot.run(token)