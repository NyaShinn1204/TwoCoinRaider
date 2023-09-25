import random
import string
import threading
import time
import re
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

def randomname(n):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n))  

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def start(delay, tokens, proxysetting, proxies, proxytype, serverid, channelid, messageid, contents, allmg, allping, mentions, randomstring, ratelimit):
    global status
    global messages
    global users
    global timelock
    status = True
    
    token = random.choice(tokens)
    
    print(token)
    print(serverid)
    print(channelid)
    if allmg == True:
        messages = mg_scrape.get_messages(token,int(channelid))
        print(messages)
        if messages == None:
            print("[-] んーメッセージが取得できなかったっぽい token死なないように一回止めるね")
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
                         serverid, allmg, channelid, messageid, contents, randomstring, mentions, ratelimit)).start()
        time.sleep(float(delay))
        
def spammer_thread(tokens, allping, proxysetting, proxies, proxytype, serverid, allmg, channelid, messageid, contents, randomstring, mentions, ratelimit):
    global messages
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
    if allmg == True:
        messageid = random.choice(messages)
    data = {"content": content,"message_reference": {"guild_id": serverid,"channel_id": channelid,"message_id": messageid}}
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
        x = request.post(f"https://discord.com/api/v9/channels/{channelid}/messages", headers=headers, json=data)
        if x.status_code == 400:
            print(f"[-] 不明なエラー  Message: {x.json()['message']} ChannelID: {channelid} Token: {extract_token} Status: {x.status_code}")
        if x.status_code == 403:
            print(f"[-] このチャンネルで発現する権限がないっぽい ChannelID: {channelid} Token: {extract_token} Status: {x.status_code}")
        if x.status_code == 404:
            print(f"[-] このチャンネルは存在しません ChannelID: {channelid} Token: {extract_token} Status: {x.status_code}")
        if x.status_code == 200:
            print("[+] Success Send: " + extract_token)
        else:
            if x.status_code == 429 or 20016:
                if ratelimit == True:
                    timelock = True
                return
            print("[-] Failed Send: " + extract_token)
    except:
        pass