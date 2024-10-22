from pprint import pprint

import json
import requests


API_KEY = ""
API_URL = f"https://api.telegram.org/bot{API_KEY}"

get_update_api_url = f"{API_URL}/getUpdates"
send_message_api = f"{API_URL}/sendMessage"
send_document_api = f"{API_URL}/sendDocument"
chat_id = ""

def get_channel_id():
    ...

def send_message(text):
    ...

def send_file():
    ...

if __name__ == "__main__":
    get_channel_id()
