import random
import string
import threading
import time
import requests
import re
from httpx import Client
from httpx_socks import SyncProxyTransport

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

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def start(delay, tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, contents, allchannel, allping, mentions, randomstring, ratelimit):
    global status
    global timelock
    status = True
    
    token = random.choice(tokens)
    
    print(token)
    print(serverid)
    
    while status is True:
        if status == False:
            break
        if timelock == True:
            print("[-] RateLimit Fixing...")
            time.sleep(8)
            print("[+] RateLimit Fixed")
            timelock = False
        threading.Thread(target=spammer_thread, args=(tokens, module_status, allping, proxysetting, proxies, proxytype,
                        allchannel, channelid, contents, randomstring, mentions, ratelimit)).start()
        time.sleep(float(delay))
        
def spammer_thread(tokens, module_status, allping, proxysetting, proxies, proxytype, allchannel, channelid, contents, randomstring, mentions, ratelimit):
    global status
    global timelock

    if timelock == True:
        return
    if status is False:
        return
    token = random.choice(tokens)
    applicationid = input("application id >> ")
    command_name = input("command name >> ")
    sub_command_name = input("sub command name >> ")
    sub_command_name_value = input("sub command value >> ")
    b = requests.get(f"https://discord.com/api/v9/channels/{channelid}/application-commands/search?type=1&query={command_name}&limit=7&include_applications=false", headers=headers)
    application = b.json()["application_commands"]["application_id" == applicationid]
    if sub_command_name == "":
        data = {"type":2,"application_id":"1087695135548129280","guild_id":"1102540101919191130","channel_id":"1109467509779878009","session_id":"NULLTRUE","data":{"version":application["version"],"id":application["id"],"name":command_name}}
    else:
        data = {"type":2,"application_id":"1087695135548129280","guild_id":"1102540101919191130","channel_id":"1109467509779878009","session_id":"NULLTRUE","data":{"version":application["version"],"id":application["id"],"name":command_name,"options":[{"type":6,"name":sub_command_name,"value":sub_command_name_value}]}}
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
        x = request.post(f"https://discord.com/api/v9/interactions", headers=headers, json=data)
        if x.status_code == 204:
            print(f"[+] 成功 Token: {extract_token}.******** Status: {x.status_code}")
        else:
            if x.status_code == 429 or 20016:
                if ratelimit == True:
                    timelock = True
                return
            print(f"[-] 失敗 Token: {extract_token}.******** Status: {x.status_code}")
    except:
        pass