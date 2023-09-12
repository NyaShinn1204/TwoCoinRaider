import requests
import json
import bypass.header as header

def get_messages(token,guildid):
    global messages
    messages = []
    while True:
        req_header = header.request_header(token)
        headers = req_header[0]
        x = requests.get(
            f"https://discord.com/api/v9/guilds/{guildid}/channels", headers=headers)
        data = json.loads(x.text)
        print(x.json)
        print(json.loads(x.text))
        if x.status_code == 200:
            print(x.status_code)
            for message in data:
                if message['type'] == 0 or 2:
                    if message not in messages:
                        messages.append(message["id"])
            return messages
        else:
            print(token)
            print(str(x.status_code))
            return