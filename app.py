# this is mostly generated by ChatGPT (GPT 3.5-turbo)
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.presences = True

bot = commands.Bot(intents = intents, command_prefix='!')

@bot.command
async def test(ctx, args):
    await ctx.send(str(args))
    print('Done!')



@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    # Check if the reaction was added to the correct message
    if payload.channel_id == 1095766880771383406 and payload.message_id == 1095767381957156944:  # these numbers represent CHANNEL_ID and MESSAGE_ID
        # Check if the reaction was added with a specific emoji
        if str(payload.emoji) == '1️⃣':
            # Get the member who added the reaction
            guild = bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            # Get the role to assign to the member
            role = discord.utils.get(guild.roles, name='ONE')
            # Assign the role to the member
            await member.add_roles(role)
            # Send a private message to the member
            await member.send(f'I just assigned the role "{role.name}" to you!')
        # Check if the reaction was added with a different emoji
        elif str(payload.emoji) == '2️⃣':
            # Get the member who added the reaction
            guild = bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            # Get the role to assign to the member
            role = discord.utils.get(guild.roles, name='TWO')
            # Assign the role to the member
            await member.add_roles(role)
            # Send a private message to the member
            await member.send(f'I just assigned the role "{role.name}" to you!')

@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    # Check if the reaction was removed from the correct message
    if payload.channel_id == 1095766880771383406 and payload.message_id == 1095767381957156944:
        # Check if the reaction was removed with a specific emoji
        if str(payload.emoji) == '1️⃣':
            # Get the member who removed the reaction
            guild = bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            # Get the role to remove from the member
            role = discord.utils.get(guild.roles, name='ONE')
            # Remove the role from the member
            await member.remove_roles(role)
            # Send a private message to the member
            await member.send(f'I just removed your "{role.name}" role!')
        # Check if the reaction was removed with a different emoji
        elif str(payload.emoji) == '2️⃣':
            # Get the member who removed the reaction
            guild = bot.get_guild(payload.guild_id)
            member = await guild.fetch_member(payload.user_id)
            # Get the role to remove from the member
            role = discord.utils.get(guild.roles, name='TWO')
            # Remove the role from the member
            await member.remove_roles(role)
            # Send a private message to the member
            await member.send(f'I just removed your "{role.name}" role!')

bot.add_command(test)  # registering a .ext command

with open('token', 'r') as tkn:
    token = str(tkn.read())

bot.run(token)