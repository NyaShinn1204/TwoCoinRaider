import random
import string
import threading
import time
import json
import websocket
import typing
from httpx import Client
from httpx_socks import SyncProxyTransport

import module.spam.message_scrape as mg_scrape
import module.spam.user_scrape as user_scrape
import bypass.header as header

status = True
timelock = True

def status():
    global status
    return status

def stop():
    global status
    status = False

def randomname(n):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n))  

def get_default_soundboard_sounds(token):
    req_header = header.request_header(token)
    headers = req_header[0]
    request = Client()
    return request.get("https://discord.com/api/v9/soundboard-default-sounds", headers=headers).json()

def start(delay, tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, rdsongs):
    global status
    global timelock
    status = True
    
    token = random.choice(tokens)
    
    sounds = False
    while not sounds:
        sounds = get_default_soundboard_sounds(token)
    random_sounds = rdsongs == True
    if not random_sounds:
        for sound in sounds:
            print(f"[{sounds.index(sound) + 1}] {sound['name']}")
        sound_index = input(f"[sound] -> ")
        sounds = [sounds[int(sound_index) - 1]]
    
    print(token)
    print(serverid)
    print(channelid)
    
    while status is True:
        if status == False:
            break
        if timelock == True:
            print("[-] RateLimit Fixing...")
            time.sleep(8)
            print("[+] RateLimit Fixed")
            timelock = False
        threading.Thread(target=spammer_thread, args=(tokens, module_status, proxysetting, proxies, proxytype,
                         serverid, channelid, sounds)).start()
        time.sleep(float(delay))


def connect_vc(serverid, channelid, token):
    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
    hello = json.loads(ws.recv())
    ws.send(json.dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
    ws.send(json.dumps({"op": 4,"d": {"guild_id": serverid,"channel_id": channelid,"self_mute": False,"self_deaf": False, "self_stream?": False, "self_video": False}}))
    ws.send(json.dumps({"op": 18,"d": {"type": "guild","guild_id": serverid,"channel_id": channelid,"preferred_region": "singapore"}}))
    ws.send(json.dumps({"op": 1,"d": None}))
    while True:
        ws.recv()
        time.sleep(hello.get("d").get("heartbeat_interval") / 1000)

def spammer_thread(tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, sounds: list[dict[str, typing.Union[str, int]]]):
    global status
    global timelock

    if timelock == True:
        return
    if status is False:
        return
    token = random.choice(tokens)
    threading.Thread(target=connect_vc, args=(serverid, channelid, token)).start()
    sound = random.choice(sounds)
    data = {
        "sound_id":sound.get("sound_id"),
        "emoji_id":None,
        "emoji_name":sound.get("emoji_name"),
        "override_path": sound.get("override_path")
    }
    req_header = header.request_header(token)
    headers = req_header[0]
    try:
        if status is False:
            return
        request = Client()
        if proxysetting == True:
            proxy = random.choice(proxies)
            request = Client(transport=SyncProxyTransport.from_url(f'{proxytype}://{proxy}'))
        x = request.post(f"https://discord.com/api/v9/channels/{channelid}/voice-channel-effects", headers=headers, json=data)
        if x.status_code == 400:
            print(f"[-] 不明なエラー  Message: {x.json()['message']} ChannelID: {channelid} Token: {token} Status: {x.status_code}")
            module_status(4, 2)
        if x.status_code == 404:
            print(f"[-] このチャンネルは存在しません ChannelID: {channelid} Token: {token} Status: {x.status_code}")
            module_status(4, 2)
        if x.status_code == 200:
            module_status(4, 1)
        else:
            module_status(4, 2)
        time.sleep(0.3 + random.random() * 0.3)
    except:
        pass