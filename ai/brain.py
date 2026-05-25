from config import MODEL_NAME, HOST, PORT
from ollama import AsyncClient, chat
import asyncio

class Brain:

    def __init__(self):
        self.model_name = MODEL_NAME
        self.client = AsyncClient(host = f"http://localhost:{PORT}")


    def build_messages(self, user_message):
        messages = [
            {'role': 'system',
                'content': 'You are Futaba, in charge of running the schools science club',},

            {'role': 'user',
            'content': user_message}
        ]
        return messages
    
    async def generate_response(self, message: str) -> str:
        message_list = self.build_messages(message)
        response = await self.client.chat(model = self.model_name, messages = message_list)
        return response.message.content
        
brain = Brain()


    

    
    