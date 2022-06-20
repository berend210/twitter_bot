import discord

import openai3
import setup

TOKEN = setup.get_discord_token()

client = discord.Client()


@client.event
async def on_ready():
    print("Discord bot ready.")


@client.event
async def on_message(message):
    if message.content is not None and "?bv " in message.content:
        resp = openai3.response(prompt=message.content[3:])
        await message.channel.send(resp)


client.run(TOKEN)
