from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

client = TelegramClient('anon', api_id, api_hash)

keywords = ['rocket', 'alert', 'evacuate']
channels = ['channel_username_or_id1', 'channel_username_or_id2']

@client.on(events.NewMessage(chats=channels))
async def handler(event):
    for keyword in keywords:
        if keyword in event.message.text.lower():
            print(f"Alert: {event.message.text}")
            break

client.start()
client.run_until_disconnected()

