from core.start import DBot
import discord
import os

from dotenv import load_dotenv
load_dotenv()

Token = os.environ['DISCORD_BOT_TOKEN']

# Bot立ち上げ
DBot(
    token=Token,
    intents=discord.Intents.all()
).run()