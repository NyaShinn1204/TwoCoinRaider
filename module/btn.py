import random
import requests
import threading
import time
import json
import websocket

status = True
timelock = True

def status():
    global status
    return status

def req_stop():
    global status
    status = False

def get_msg(token, channelid, messageid):
    global msgdata
    request = requests.get(f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1&around={messageid}", headers={"authorization": token})
    msgdata = json.loads(request.text)
    return msgdata
        
def start(delay, tokens, serverid, channelid, messageid):
    global status
    global timelock
    status = True
        
    print(serverid)
    print(channelid)
    print(messageid)

    while status is True:
        if status == False:
            break
        if timelock == True:
            print("[-] RateLimit Fixing...")
            time.sleep(8)
            print("[+] RateLimit Fixed")
            timelock = False
        threading.Thread(target=button_thread, args=(tokens, serverid, channelid, messageid)).start()
        time.sleep(float(delay))
        
def button_thread(tokens, serverid, channelid, messageid):
    global status
    global timelock

    token = random.choice(tokens)

    if timelock == True:
        return
    if status is False:
        return
    try:
        if status is False:
            return
        msg = get_msg(token, channelid, messageid)
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        heart = ws.recv()
        auth = {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "os": "windows",
                    "browser": "chrome",
                    "device": "pc"
                },
            }
        }
        ws.send(json.dumps(auth))
        res = json.loads(ws.recv())
        payload = {
            "type": 3,
            "guild_id": serverid,
            "channel_id": channelid,
            "message_id": messageid,
            "session_id":  res["d"]["session_id"],
            "application_id": msg[0]["author"]["id"],
            "data": {
                    "component_type": msg[0]['components'][0]['components'][0]["type"],
                    "custom_id": msg[0]['components'][0]['components'][0]['custom_id']
            },
        }
        req = requests.post('https://discord.com/api/v9/interactions', headers={"authorization": token}, json=payload)
        print(req.content+req.status_code)
        ws.close()
    except:
        pass