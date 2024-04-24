import json
import os

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

with open('api.json', 'r') as file:
    data = json.load(file)

def mistral(user_message, model="mistral-small-latest", is_json=False):
    client = MistralClient(api_key=data['apiKey'])
    messages = [ChatMessage(role="user", content=user_message)]

    if is_json:
        chat_response = client.chat(
            model=model, messages=messages, response_format={"type": "json_object"}
        )
    else:
        chat_response = client.chat(model=model, messages=messages)

    return chat_response.choices[0].message.content