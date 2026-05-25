import discord
from ai.brain import Brain
from config import MODEL_NAME

class Futaba_Bot(discord.Client):
    
    def __init__(self, p_brain):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.brain = p_brain

    async def on_ready(self):
        print(f"{MODEL_NAME} is online")

    async def on_message(self, message):
        if message.author.bot: return
        
        user = message.author
        clean_message = message.content
        async with message.channel.typing():
            response = await self.brain.generate_response(clean_message)

        await message.reply(response)

    
