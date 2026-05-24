#Stores important stuff
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME")
MAC_IP = os.getenv("MAC_IP")
PORT = os.getenv("PORT")
