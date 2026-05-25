from ai.brain import Brain
from discord_bot.bot import Futaba_Bot
from config import TOKEN
import asyncio

brain = Brain()
bot = Futaba_Bot(brain)
bot.run(TOKEN)
