import discord
from ai.brain import Brain

class Futaba_Bot(discord.Client):
    
    def __init__(self):
        super().__init__()
        self.brain = Brain

    async def on_message(self, message):
        if message.author.bot: return
        
        intents = discord.Intents.default()
        intents.message_content = True
        user = message.author
        clean_message = message.content
        response = self.brain.generate_response(clean_message)

        await message.reply(response)

    
