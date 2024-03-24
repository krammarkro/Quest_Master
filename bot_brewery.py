import discord
from discord import app_commands
from discord.ext import commands
import sheet as sh
import logging
import inspect
from dotenv import load_dotenv
import os
import sys
from requests import get

logger = logging.getLogger(__name__)
handler = logging.FileHandler('example.log', 'w', 'utf-8')
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

load_dotenv()
TOKEN = os.getenv("TOKEN")  # Discord Token
role_dict = {
    "RP": ("B", "C"),
    "TL": ("D", "E"),
    "PR": ("F", "G"),
    "CLRD": ("H", "I"),
    "TS": ("J", "K"),
    "QC": ("L", "M")
}
role_dict_reaction = {
    "B": "RP",
    "D": "TL",
    "F": "PR",
    "H": "CLRD",
    "J": "TS",
    "L": "QC"
}

line_number = inspect.currentframe().f_lineno


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())


@bot.event
async def on_ready():
    logger.info(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        logger.info(f"Synced {len(synced)} command(s)")
    except Exception as e:
        logger.error(e)


async def remove_reaction(channel_id, message_id, emoji, add):
    channel = bot.get_channel(channel_id)
    message = await channel.fetch_message(message_id)
    await message.clear_reaction(emoji)
    if add:
        await message.add_reaction("🥂")


async def delete_message(channel_id, message_id):
    channel = bot.get_channel(int(channel_id))

    message = await channel.fetch_message(int(message_id))

    await message.delete()


async def reactionhelper(data, assignmentlog, status):
    role = data[2]
    if role in role_dict_reaction:
        role = role_dict_reaction[role]
    sh.write(data, status)
    await assignmentlog.send(
        f"{sh.getchannelid(data[0])} | CH {data[1]} | {role} | sheet updated to status: {status} by: {data[4]}")


@bot.event
async def on_raw_reaction_add(payload):
    assignmentlog = bot.get_channel(1219030657955794954)
    channel_id = payload.channel_id
    target_channel_id = 1218705159614631946  # only checks the assignment channel
    bot_id = 1218682240947458129  # id of the bot
    if (channel_id == target_channel_id) and payload.user_id != bot_id:
        data, row_name = sh.getmessageid(payload.message_id)
        if f"<@{payload.user_id}>" == data[4]:
            print(payload.emoji)
            print(repr(payload.emoji))
            if repr(payload.emoji) == "<PartialEmoji animated=False name='✅' id=None>":
                await remove_reaction(payload.channel_id, payload.message_id, "❌", True)
                await remove_reaction(payload.channel_id, payload.message_id, "✅", True)
                await reactionhelper(data, assignmentlog, "Working")
            elif repr(payload.emoji) == "<PartialEmoji animated=False name='🥂' id=None>":
                data, row_name = sh.getmessageid(payload.message_id)
                role = data[2]
                if role in role_dict_reaction:
                    role = role_dict_reaction[role]
                target_channel = bot.get_channel(1219030657955794954)  # ID of the done channel
                await target_channel.send(f"{sh.getchannelid(data[0])} | CH {data[1]} | {role} | Done | {data[4]}")
                sh.write(data, "Done")
                sh.delete_row(row_name)  # clear message data
                await remove_reaction(payload.channel_id, payload.message_id, "🥂", False)

            else:
                data, row_name = sh.getmessageid(payload.message_id)
                role = data[2]
                await reactionhelper(data, assignmentlog, "Declined")
                await delete_message(payload.channel_id, payload.message_id)
                sh.delete_row(row_name)  # clear


@bot.tree.command(name="findid")
@app_commands.describe(user="User")
async def findid(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message("Done")
    sh.findid(user.name, str(user.id))


@bot.event
async def on_member_join(member):
    sh.findid(member.name, str(member.id))


@bot.tree.command(name="say")
@app_commands.describe(arg="what to say")
async def say(interaction: discord.Interaction, arg: str):
    user = interaction.user.name
    await interaction.response.send_message(f"Hey{interaction.user.mention}, test 2, {user}")


@bot.tree.command(name="assign")
@app_commands.describe(series="# of the series", chapter="What chapter", role="What needs to be done", who="Who")
async def assign(interaction: discord.Interaction, series: str, chapter: str, role: str, who: str):
    target_channel_id = int("1218705159614631946")  # Replace with the ID of the target channel
    target_channel = bot.get_channel(target_channel_id)
    role = role.upper()
    first = None
    second = None
    if role.upper() in role_dict:
        first, second = role_dict[role]
    if first is None:
        await interaction.response.send_message(f" '{role.upper()}' is not a valid Role ", ephemeral=True)
    else:
        await interaction.response.defer(ephemeral=True)
        message = await target_channel.send(f"{series}| CH {chapter} | {role} | {who}")
        data = [sh.getsheetname(series), chapter, first, second, who]
        sh.store(message.id, data[0], chapter, who, first, second)
        sh.write(data, "Assigned")
        await interaction.followup.send(content="Assigned")
        await message.add_reaction("✅")
        await message.add_reaction("❌")


@bot.tree.command(name="channel")
@app_commands.describe(channel="# of the channel", sheet="Name of the sheet")
async def channel(interaction: discord.Interaction, channel: str, sheet: str):
    await interaction.response.send_message(f"{channel} was assigned to {sheet}")
    # datatest.add_to_json_file('channel.json', sheet, channel)
    sh.writechannel(channel, sheet)


@bot.tree.command(name="create")
@app_commands.describe(channelname="Name of the channel", sheet="Name of the sheet")
async def create(interaction: discord.Interaction, channelname: str, sheet: str):
    guild = interaction.guild
    category = bot.get_channel(1218035431078236323)
    sh.copy(sheet)

    channel = await guild.create_text_channel(channelname, category=category)
    new_position = 2  # Define new_position here
    await channel.edit(position=new_position)
    channels = sorted(guild.channels, key=lambda c: c.position)
    channels_positions = {channels[i].id: i for i in range(len(channels))}
    channels_positions[channel.id] = new_position
    id = channel.id
    sh.writechannel(f"<@{channel.id}>", sheet)


@bot.tree.command(name="updatechannelname")
@app_commands.describe(channel="# of the Channel", new_name="The new name for the sheet")
async def updatechannelname(interaction: discord.Interaction, channel: str, new_name: str):
    await interaction.response.send_message(f"{channel} was reassigned to {new_name}")
    sh.updatesheet(channel, new_name)


@bot.tree.command(name="updatechannelid")
@app_commands.describe(new_channel="new # of the Channel", name="Name of the sheet")
async def updatechannelid(interaction: discord.Interaction, new_channel: str, name: str):
    await interaction.response.send_message(f"{name} was reassigned to {new_channel}")
    sh.updatechannel_id(new_channel, name)


@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)


@bot.tree.command(name="done")
@app_commands.describe(series="# of the Series", chapter="What chapter", role="What role")
async def assign(interaction: discord.Interaction, series: str, chapter: str, role: str):
    first = None
    second = None
    target_channel_id = int("1218705159614631946")  # change to actual channel 
    target_channel = bot.get_channel(target_channel_id)
    user = interaction.user.id

    role = role.upper()
    if role.upper() in role_dict:
        first, second = role_dict[role]
    if first == None:
        if target_channel is None:
            logger.error("Done command used with invalid role")
        else:
            await interaction.response.send_message(f" '{role.upper()}' is not a valid Role ", ephemeral=True)
    else:
        # await target_channel.send(f"{interaction.user.mention} | {series}| CH {chapter} | {role.upper()} | Done")
        await target_channel.send(f"{series} | CH {chapter} | {role.upper()} | Done | {interaction.user.mention}")
        list = [sh.getsheetname(series), chapter, first, second, f"<@{user}>"]
        sh.write(list, "Done")
        # await interaction.response.send_message("Send", ephemeral=True)


@bot.tree.command(name="ip")
@app_commands.describe()
async def ip(interaction: discord.Interaction):
    if interaction.user.id == 611962086049710120:
        ip = get('https://api.ipify.org').content.decode('utf8')
        await interaction.response.send_message(ip, ephemeral=True)
    else:
        await interaction.response.send_message("You are not allowed to use this command")


@bot.tree.command(name="logs")
@app_commands.describe()
async def logs(interaction: discord.Interaction):
    with open("example.log", "r") as file:
        await interaction.response.send_message(file.read(), ephemeral=True)


bot.run(TOKEN)
