import discord

import openai3
import setup

TOKEN = setup.get_discord_token()

client = discord.Client()


@client.event
async def on_ready():
    """
    Lets it know if the Discord bot is ready.
    :return: None.
    """
    print("Discord bot ready.")


@client.event
async def on_message(message):
    """
    Replies on a users message with a generated response when they call upon the bot.
    :param message: The message which is checked.
    :return: None.
    """
    if message.content is not None and "?bv " in message.content:
        resp = openai3.response(prompt=message.content[3:], build_prompt=True, translate_nl=True)
        if resp is None:
            resp = openai3.response(prompt=message.content[3:], build_prompt=True, translate_nl=True)

        await message.channel.send(resp)


client.run(TOKEN)
