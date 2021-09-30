#!/usr/bin/python3
import discord
from discord.ext import commands

import pylistenbrainz

# get our token from config.py
from config import token
import database
import lbz

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
    if(lbz.doesAccExist(str(arg)) == False):
        await ctx.channel.send("Account does not exist")
        return
    print("adding " + str(uid) + " to the db with username " + arg)
    database.addentry(uid, arg)
    await ctx.channel.send("Linked your ListenBrainz Account successfully")

@bot.command()
async def lbzstatus(ctx):
    uid = ctx.author.id
    uname = database.getUsername(uid)
    if(uname != None):
        await ctx.channel.send("Your ListenBrainz account is linked to this bot!\n\nYour ListenBrainz Profile: https://https://listenbrainz.org/user/" + uname)
    else:
        await ctx.channel.send("You do not have a ListenBrainz account linked. Link it with &lbzsetup")

@bot.command()
async def nowplaying(ctx, arg=None):
    if(arg==None):
        uid = ctx.author.id
    elif(ctx.message.mentions):
        mentions = ctx.message.mentions
        if(len(mentions) > 1):
            await ctx.channel.send("This command only takes one mention for the argument")
            return
        uid = mentions[0].id
    print(uid)
    uname = database.getUsername(uid)
    if(uname != None):
        np = lbz.nowPlaying(uname)
        if(np == None):
            await ctx.channel.send("Nothing is currently playing")
            return
        await ctx.channel.send('**NOW PLAYING**```' + 
        '\nTitle:  ' + np.track_name + 
        '\nAlbum:  ' + np.release_name + 
        '\nArtist: ' + np.artist_name + 
        '```')
    else:
        await ctx.channel.send("There is no account linked for this user. You can link one by doing this ```&lbzsetup <ListenBrainz username here>```")

        

bot.run(token)
