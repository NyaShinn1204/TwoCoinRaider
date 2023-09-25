import random
import string
import threading
import time
import json
from httpx import Client
from httpx_socks import SyncProxyTransport

import module.spam.channel_scrape as ch_scrape
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

def start(delay, tokens, proxysetting, proxies, proxytype, serverid, channelid, contents, allchannel, allping, mentions, randomstring, ratelimit):
    global status
    global channels
    global users
    global timelock
    status = True
    
    token = random.choice(tokens)
    
    print(token)
    print(serverid)
    if allchannel == True:
        channels = ch_scrape.get_channels(token,int(serverid))
        if channels == None:
            print("[-] んーチャンネルが取得できなかったっぽい token死なないように一回止めるね")
            return
    if allping == True:
        users = user_scrape.get_members(serverid, channelid, token)
        if users == None:
            print("[-] んーメンバーが取得できなかったっぽい token死なないように一回止めるね")
            return
    
    while status is True:
        if status == False:
            break
        if timelock == True:
            print("[-] RateLimit Fixing...")
            time.sleep(8)
            print("[+] RateLimit Fixed")
            timelock = False
        threading.Thread(target=spammer_thread, args=(tokens, allping, proxysetting, proxies, proxytype,
                         serverid, allchannel, channelid, contents, randomstring, mentions, ratelimit)).start()
        time.sleep(float(delay))
        
def spammer_thread(tokens, allping, proxysetting, proxies, proxytype, serverid, allchannel, channelid, contents, randomstring, mentions, ratelimit):
    global channels
    global users
    global status
    global timelock

    if timelock == True:
        return
    if status is False:
        return
    token = random.choice(tokens)
    content = contents
    if content == "":
        print("[-] メッセージが設定されていないので初期のメッセージを送信します")
        content = "Sussy Raider V3 REWRITE"
    if allping == True:
        for i in range(int(mentions)):
            content = content + f"<@{random.choice(users)}>"
    if randomstring == True:
        content = f"{content}\n{randomname(10)}"
    if allchannel == True:
        channelid = random.choice(channels)
    data = {"content": content}
    req_header = header.request_header(token)
    headers = req_header[0]
    try:
        if status is False:
            return
        request = Client()
        if proxysetting == True:
            proxy = random.choice(proxies)
            request = Client(transport=SyncProxyTransport.from_url(f'{proxytype}://{proxy}'))
        x = request.post(f"https://discord.com/api/v9/channels/{channelid}/messages", headers=headers, json=data)
        if x.status_code == 400:
            print(f"[-] AutoModによりメッセージが削除されたっぽい  Message: {x.json()['message']} ChannelID: {channelid} Token: {token} Status: {x.status_code}")
            module_status(3, 2)
        if x.status_code == 403:
            print(f"[-] このチャンネルで発現する権限がないっぽい ChannelID: {channelid} Token: {token} Status: {x.status_code}")
            module_status(3, 2)
        if x.status_code == 404:
            print(f"[-] このチャンネルは存在しません ChannelID: {channelid} Token: {token} Status: {x.status_code}")
            module_status(3, 2)
        if x.status_code == 200:
            module_status(3, 1)
        else:
            if x.status_code == 429 or 20016:
                if ratelimit == True:
                    timelock = True
                return
            module_status(3, 2)
    except:
        pass