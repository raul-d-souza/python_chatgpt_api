import requests
import json

import utils.utils

API_KEY = utils.utils.get_config("API_KEY")
url_chat = utils.utils.get_config("url_chat")


def chatgpt_answer(content):
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    body = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": content}]
    }
    body_chat = json.dumps(body)

    req_chat = requests.post(url=url_chat, headers=headers, data=body_chat)

    response = req_chat.json()

    return response
