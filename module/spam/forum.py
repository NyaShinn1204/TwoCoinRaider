import random
import string
import threading
import time
import re
from httpx import Client
from httpx_socks import SyncProxyTransport

import bypass.header as header

status = True
timelock = True

def status():
    global status
    return status

def req_stop():
    global status
    status = False
        
def randomname(n):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n))  

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def start(tokens, proxysetting, proxies, proxytype, channelid, forum_name, forum_message, delay, ratelimit):
    global status
    global timelock
    status = True
    
    token = random.choice(tokens)
        
    print(token)
    print(channelid)

    while status is True:
        if status == False:
            break
        if timelock == True:
            print("[-] RateLimit Fixing...")
            time.sleep(8)
            print("[+] RateLimit Fixed")
            timelock = False
        threading.Thread(target=forum_thread, args=(tokens, proxysetting, proxies, proxytype, channelid, forum_name, forum_message, ratelimit)).start()
        time.sleep(float(delay))
        
def forum_thread(tokens, proxysetting, proxies, proxytype, channelid, forum_name, forum_message, ratelimit):
    global status
    global timelock

    token = random.choice(tokens)

    if timelock == True:
        return
    if status is False:
        return
    payload = {"name": f"{forum_name} " +randomname(15), "message": {"content": f"{forum_message}"}}
    req_header = header.request_header(token)
    headers = req_header[0]
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    try:
        if status is False:
            return
        request = Client()
        if proxysetting == True:
            proxy = random.choice(proxies)
            request = Client(transport=SyncProxyTransport.from_url(f'{proxytype}://{proxy}'))
            return
        x = request.post(f"https://discord.com/api/v9/channels/{channelid}/threads?use_nested_fields=true", headers=headers, json=payload)
        if x.status_code == 201:
            print("[+] Success Send: " + extract_token)
        else:
            if x.status_code == 429:
                if ratelimit == "True":
                    timelock = True
                return
            print("[-] Failed Send: " + extract_token)
    except:
        pass