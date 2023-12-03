import random
import threading
import time
import json
import requests
import re
from httpx import Client
from httpx_socks import SyncProxyTransport

import bypass.header as header

status = True
timelock = False

def status():
    global status
    return status

def stop():
    global status
    status = False

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def get_app(token, serverid, channelid, messageid):
    referre = f"https://discord.com/channels/{serverid}/{channelid}"
    print(referre)
    req_header = header.request_header(token)
    headers = req_header[0]
    print(channelid)
    x1 = requests.get(f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1&around="+messageid, headers=headers)
    if x1.status_code == 200:
        print("[+] Success Get application " + token)
        x1json = x1.json()[0]
        appliid = x1json['author']['id']
        x1json2 = x1json['components'][0]['components'][0]
        customid = x1json2['custom_id']
        return appliid, customid
    else:
        print(x1.status_code)

def start(delay, tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, messageid, ratelimit):
    global status
    global getdata
    global appliid
    global customid
    global timelock
    status = True
    
    token = random.choice(tokens)
    
    getdata = get_app(token, serverid, channelid, messageid)
    appliid = getdata[0]
    customid = getdata[1]
        
    print(token)
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
        threading.Thread(target=ticket_thread, args=(tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, messageid, ratelimit)).start()
        time.sleep(float(delay))
   
def ticket_thread(tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, messageid, ratelimit):
    global status
    global getdata
    global appliid
    global customid
    global timelock

    if timelock == True:
        return
    if status is False:
        return
    token = random.choice(tokens)
    data = {
        "guild_id": serverid,
        "channel_id": channelid,
        "message_flags": 0,
        "message_id": messageid,
        "type": 3,
        "application_id": appliid,
        "data": {
            "component_type": 2,
            "custom_id": customid
        }
    }
    req_header = header.request_header(token)
    headers = req_header[0]
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    try:
        if status is False:
            return
        requests = Client()
        if proxysetting == True:
            proxy = random.choice(proxies)
            request = Client(transport=SyncProxyTransport.from_url(f'{proxytype}://{proxy}'))
        x = requests.post("https://discord.com/api/v9/interactions", headers=headers, json=data)
        if x.status_code == 200:
            module_status(2, 5, 1)
            if proxysetting == True:
                print(f"[-] 作成に成功しました Token: {extract_token}.******** Proxy: {proxy}")
            else:
                print(f"[-] 作成に成功しました Token: {extract_token}.********")
        else:
            if x.status_code == 429 or 20016:
                print("[-] RateLimit!! Please Wait!! "+json.loads(x.text)["retry_after"])
                if ratelimit == True:
                    timelock = True
                return
            module_status(2, 5, 2)
    except:
        pass