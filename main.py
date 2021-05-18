import discord
import random
from discord.ext import commands
import asyncio


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = commands.Bot(command_prefix="/")


@client.command()
async def ok(ctx):
    await ctx.send(f"Ty ok na {random.randint(1,100)} %")


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def miotaj(ctx, member: discord.Member, channel: discord.VoiceChannel, channel2: discord.VoiceChannel):
    for i in range(1, 5):
        await member.edit(voice_channel=channel)
        await member.edit(voice_channel=channel2)
    await member.edit(voice_channel=ctx.author.voice.channel)


@client.command()
async def MONKE(ctx):
    await ctx.send("DZISIAJ JESTEŚ TAKIM MONKE")
    await ctx.send(f"https://www.placemonkeys.com/{random.randint(1000,3000)}/{random.randint(1000,3000)}")


@client.command()
async def cho(ctx, member: discord.Member):
    await member.edit(voice_channel=ctx.author.voice.channel)


@client.command()
async def pomocy(ctx):
    await ctx.send("""KOMENDY - 
    ok,
    kick
    miotaj
    MONKE
    cho""")


@client.command()
async def atak(ctx):
    linia = random.randint(1, 146)
    with open("ob.txt", "r") as o:
        for position, line in enumerate(o):
            if position == linia:
                await ctx.send(f"TY {(line.upper())}")

client.run(token)
