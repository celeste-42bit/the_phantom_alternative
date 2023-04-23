# this is mostly generated by ChatGPT (GPT 3.5-turbo)
import discord
import youtube_dl
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.presences = True

description = '''This is the alternative version to "The Phantom", based on discord.py and discord.ext'''

bot = commands.Bot(intents = intents, description = description, command_prefix='$')

@bot.event
async def on_ready():
    print('I logged in!')

@bot.command(name='embed')
async def embed(ctx, title, description, color, field_name, field_content, footer):
    embed = discord.Embed(title=str(title), description=str(description), color=discord.Color(int(color, 16)))
    embed.add_field(name=str(field_name), value=str(field_content), inline=False)
    embed.set_footer(text=str(footer))
    await ctx.send(embed=embed)

''' made other options optional, by ChatGPT
@bot.command(name='embed')
async def embed(ctx, title, description="", color="000000", field_name="", field_content="", footer=""):
    embed = discord.Embed(title=str(title), description=str(description), color=discord.Color(int(color, 16)))
    if field_name and field_content:
        embed.add_field(name=str(field_name), value=str(field_content), inline=False)
    if footer:
        embed.set_footer(text=str(footer))
    await ctx.send(embed=embed)
'''

@bot.command(name='play')
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send("You need to be in a voice channel to use this command!")
        return
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice is None:
        voice = await voice_channel.connect()
    else:
        await voice.move_to(voice_channel)
    await ctx.send(f"Playing {url}")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice.play(discord.FFmpegPCMAudio(URL), after=lambda e: print('done', e))

@bot.command(name='stop')
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice is not None:
        await voice.disconnect()
        await ctx.send("Stopped playing music and left the voice channel.")
    else:
        await ctx.send("I am not currently in a voice channel.")

@bot.command(name='say')
async def say(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    if payload.channel_id == 1095766880771383406 and payload.message_id == 1095767381957156944:
        if str(payload.emoji) == '1️⃣':
            guild = bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            role = discord.utils.get(guild.roles, name='ONE')
            await member.add_roles(role)
            await member.send(f'I just assigned the role "{role.name}" to you!')
        elif str(payload.emoji) == '2️⃣':
            guild = bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            role = discord.utils.get(guild.roles, name='TWO')
            await member.add_roles(role)
            await member.send(f'I just assigned the role "{role.name}" to you!')

@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    if payload.channel_id == 1095766880771383406 and payload.message_id == 1095767381957156944:
        if str(payload.emoji) == '1️⃣':
            guild = bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            role = discord.utils.get(guild.roles, name='ONE')
            await member.remove_roles(role)
            await member.send(f'I just removed your "{role.name}" role!')
        elif str(payload.emoji) == '2️⃣':
            guild = bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            role = discord.utils.get(guild.roles, name='TWO')
            await member.remove_roles(role)
            await member.send(f'I just removed your "{role.name}" role!')


#bot.add_command(test)  # registering a .ext command

with open('token', 'r') as tkn:
    token = str(tkn.read())

bot.run(token)