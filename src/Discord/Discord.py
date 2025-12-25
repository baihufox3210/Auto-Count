import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
channel_id = os.getenv("CHANNEL_ID")

url = f"https://discord.com/api/v10/channels/{channel_id}/messages"

headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}

def send_message(msg):
    requests.post(url, headers = headers, json = {"content": msg})

def get_message():
    return requests.get(url + "?limit=1", headers = headers).json()[0]