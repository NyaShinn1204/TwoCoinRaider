import random
import re
import threading
import time
import json
import emoji as ej
import urllib
from httpx import Client
from httpx_socks import SyncProxyTransport

import module.spam.channel_scrape as ch_scrape
import module.spam.user_scrape as user_scrape
import bypass.header as header

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def start(delay, tokens, proxysetting, proxies, proxytype, channelid, messageid, emoji):
    for token in tokens:
        threading.Thread(target=req_reaction, args=(token, proxysetting, proxies, proxytype, channelid, messageid, emoji)).start()
        time.sleep(float(delay))
    
def req_reaction(token, proxysetting, proxies, proxytype, channelid, messageid, emoji):
    req_header = header.request_header(token)
    headers = req_header[0]
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    emoji2 = urllib.parse.quote_plus(ej.emojize(emoji,use_aliases=True))
    try:
        request = Client()
        if proxysetting == True:
            proxy = random.choice(proxies)
            request = Client(transport=SyncProxyTransport.from_url(f'{proxytype}://{proxy}'))
        x = request.put(f"https://discord.com/api/v9/channels/{channelid}/messages/{messageid}/reactions/{emoji2}/%40me", headers=headers)
        if x.status_code == 204:
            if proxysetting == True:
                print(f"[-] 送信に成功しました ChannelID: {channelid} Token: {extract_token}.******** Proxy: {proxy}")
            else:
                print(f"[-] 送信に成功しました ChannelID: {channelid} Token: {extract_token}.********")
        else:
            if x.status_code == 429 or 20016:
                print("[-] RateLimit!! "+json.loads(x.text)["retry_after"])
    except:
        pass