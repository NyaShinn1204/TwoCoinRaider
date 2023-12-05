import random
import websocket
import re
import threading
import time
import json
import sys

status = True

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def status():
    global status
    return status

def stop():
    global status
    status = False

def start(delay, tokens, status, type, randomse):
    for token in tokens:
        threading.Thread(target=online_thread, args=(token, status, type, randomse)).start()
        time.sleep(float(delay))
    
def online_thread(token, status, type, randomse):
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    game = "Onliner | TwoCoin"
    stream_text = "Onliner | TwoCoin"
    try:
        if randomse == True:
            type = random.choice(['Playing', 'Streaming', 'Watching', 'Listening', ''])
            status = ['online', 'dnd', 'idle']
            status = random.choice(status)
            ws = websocket.WebSocket()
            ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
            hello = json.loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval']
            if type == "Playing":
                game = "Minecraft"
                gamejson = {
                    "name": game,
                    "type": 0
                }
            elif type == 'Streaming':
                gamejson = {
                    "name": game,
                    "type": 1,
                    "url": stream_text
                }
            elif type == "Listening":
                game = random.choice(["Spotify", "Apple Music", "YouTube", "SoundCloud"])
                gamejson = {
                    "name": game,
                    "type": 2
                }
            elif type == "Watching":
                game = random.choice(["YouTube", "Twitch"])
                gamejson = {
                    "name": game,
                    "type": 3
                }
            else:
                gamejson = {
                    "name": game,
                    "type": 0
                }
            auth = {
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "$os": sys.platform,
                        "$browser": "RTB",
                        "$device": f"{sys.platform} Device"
                    },
                    "presence": {
                        "game": gamejson,
                        "status": status,
                        "since": 0,
                        "afk": False
                    }
                },
                "s": None,
                "t": None
            }
            ws.send(json.dumps(auth))
            ack = {
                "op": 1,
                "d": None
            }
            while True:
                time.sleep(heartbeat_interval / 1000)
                try:
                    print(f"[+] Success Online: {extract_token}")
                    ws.send(json.dumps(ack))
                except Exception as e:
                    print(f"[-] Failed Online: {extract_token}")
                    break
        else:
            ws = websocket.WebSocket()
            ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
            hello = json.loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval']
            if type == "Playing":
                gamejson = {
                    "name": game,
                    "type": 0
                }
            elif type == 'Streaming':
                gamejson = {
                    "name": game,
                    "type": 1,
                    "url": stream_text
                }
            elif type == "Listening":
                gamejson = {
                    "name": game,
                    "type": 2
                }
            elif type == "Watching":
                gamejson = {
                    "name": game,
                    "type": 3
                }
            else:
                gamejson = {
                    "name": game,
                    "type": 0
                }
            auth = {
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "$os": sys.platform,
                        "$browser": "RTB",
                        "$device": f"{sys.platform} Device"
                    },
                    "presence": {
                        "game": gamejson,
                        "status": status,
                        "since": 0,
                        "afk": False
                    }
                },
                "s": None,
                "t": None
            }
            ws.send(json.dumps(auth))
            ack = {
                "op": 1,
                "d": None
            }
            while status is True:
                if status == False:
                    break
                time.sleep(heartbeat_interval / 1000)
                try:
                    print(f"[+] Success Online: {extract_token}")
                    ws.send(json.dumps(ack))
                except Exception as e:
                    print(f"[-] Failed Online: {extract_token}")
                    break
    except:
        pass