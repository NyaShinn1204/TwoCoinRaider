import random
import string
import threading
import time
import binascii
import os
import re
import requests
from httpx import Client
from httpx_socks import SyncProxyTransport

import module.spam.channel_scrape as ch_scrape
import module.spam.user_scrape as user_scrape
import bypass.header as header
import bypass.random_convert as random_convert

status = True
timelock = False

def status():
    global status
    return status

def stop():
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

def start(delay, tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, messageid, optionbutton):
    global status
    global timelock
    status = True
    
    token = random.choice(tokens)
    
    print(token)
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
        threading.Thread(target=button_thread, args=(tokens, module_status, proxysetting, proxies, proxytype,
                        serverid, channelid, messageid, optionbutton)).start()
        time.sleep(float(delay))
        
def button_thread(tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, messageid, optionbutton):
    global status
    global timelock

    if timelock == True:
        return
    if status is False:
        return
    token = random.choice(tokens)
    req_header = header.request_header(token)
    headers = req_header
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    try:
        payload = {'limit': '50','around': messageid}
        response1 = requests.get(
            f'https://discord.com/api/v9/channels/{channelid}/messages',
            params=payload,
            headers=headers
        )
        messagebottoclick = next((x for x in response1.json() if x["id"] == messageid), None)
        if messagebottoclick is None:
            pass
        buttons = []
        for x in messagebottoclick["components"]:
            buttons.append(x["components"][0])
        data = {
            'type': 3,
            'guild_id': serverid,
            'channel_id': channelid,
            'message_flags': 0,
            'message_id': messageid,
            'application_id': messagebottoclick["author"]["id"],
            'session_id': str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),
            'data': {
                'component_type': 2,
                'custom_id': buttons[int(optionbutton)]["custom_id"],
            },
        }
        response2 = requests.post(
            'https://discord.com/api/v9/interactions',
            headers=headers,
            json=data
        )
        match response2.status_code:
            case 200:
                print(f"[+] Success Send {token[:25]}")
            case _:
                print(f"[-] Failed Send {token[:25]}")
    except Exception as e:
        print(f"[-] Failed Send {token[:25]}")
    except:
        pass