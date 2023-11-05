import random
import string
import requests
import re
import time

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

def get_app(token, proxy, proxies, serverid, channelid, messageid):
    referre = f"https://discord.com/channels/{serverid}/{channelid}"
    print(referre)
    req_header = header.request_header(token)
    headers = req_header[0]
    print(channelid)
    if proxy == False:
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
    else:
        proxy2 = random.choice(proxies)
        proxies2 = {
            'http' : f'{proxy}://{proxy2}',
            'https' : f'{proxy}://{proxy2}',
        }
        x1 = requests.get(f"https://discord.com/api/v9/channels/{channelid}/messages?limit=1&around="+messageid, headers=headers, proxies=proxies2)
        if x1.status_code == 200:
            print("[+] Success Get application " + token)
            x1json = x1.json()[0]
            print(x1json)
            appliid = x1json['author']['id']
            x1json2 = x1json['components'][0]['components'][0]
            customid = x1json2['custom_id']
            return appliid, customid
        else:
            print(x1.status_code)

def start(delay, tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, messageid):
    global status
    global timelock
    status = True
        
    print(token)
    print(serverid)
    print(channelid)
    print(messageid)

    for token in tokens:
        ticket_thread(delay, token, module_status, proxysetting, proxies, proxytype, serverid, channelid, messageid)
        
def ticket_thread(delay, token, module_status, proxysetting, proxies, proxytype, serverid, channelid, messageid):
    time.sleep(float(delay))
    req_header = header.request_header(token)
    headers = req_header[0]
    if proxysetting == False:
        getdata = get_app(token, proxy, proxies, serverid, channelid, messageid)
        appliid = getdata[0]
        customid = getdata[1]
        print("[+] Application ID: " + appliid)
        print("[+] Custom ID: " + customid)
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
        x1 = requests.post("https://discord.com/api/v9/interactions", headers=headers, json=data)
        if x1.status_code == 204:
            module_status(5, 1)
            print("[+] Success Ticket Create" + token)
            print("[*] Cooldown... ")
        else:
            module_status(5, 2)
            print("[-] Failed Ticket Create" + token)
    else:
        proxy = random.choice(proxies)
        proxy2 = random.choice(proxies)
        proxies2 = {
            'http' : f'{proxy}://{proxy2}',
            'https' : f'{proxy}://{proxy2}',
        }
        getdata = get_app(token, proxy, proxies, serverid, channelid, messageid)
        appliid = getdata[0]
        customid = getdata[1]
        print("[+] Application ID: " + appliid)
        print("[+] Custom ID: " + customid)
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
        x1 = requests.post("https://discord.com/api/v9/interactions", headers=headers, json=data, proxies=proxies2)
        if x1.status_code == 204:
            module_status(5, 1)
            print("[+] Success Ticket Create" + token)
            print("[*] Cooldown... ")
        else:
            module_status(5, 2)
            print("[-] Failed Ticket Create" + token)