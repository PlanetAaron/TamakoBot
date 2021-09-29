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
async def lbzsetup(ctx, arg=None):
    if(arg == None):
        await ctx.channel.send("Usage: ```&lbzsetup <ListenBrainz account username```")
        return
    uid = ctx.author.id
    if(lbz.doesAccExist(str(arg)) == false):
        await ctx.channel.sent("Account does not exist")
        return
    print("adding " + str(uid) + " to the db with username " + arg)
    database.addentry(str(uid), str(arg))
    await ctx.channel.send("Linked your ListenBrainz Account successfully")

bot.run(token)
