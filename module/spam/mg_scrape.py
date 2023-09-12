import json
import base64
import tls_client
from tkinter.constants import E
import binascii
import os
import random
import re

messages = []

def get_headers(option=None):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","Accept-language": "en-US","Content-Type": "application/json","Accept-Encoding": "gzip, deflate","Sec-Fetch-Dest": "empty","Sec-Fetch-Mode": "cors","Sec-Fetch-Site": "same-origin"}
    headers["x-super-properties"] = base64.b64encode(json.dumps({"os": "Windows","browser": "Chrome","device": "","system_locale": "en-US","browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","browser_version": "107.0.0.0","os_version": "10","referrer": "","referring_domain": "","referrer_current": "","referring_domain_current": "","release_channel": "stable","client_build_number": 160996,"client_event_source": None}, separators=(',', ':')).encode()).decode()
    return headers

def get_session():
    session = tls_client.Session(client_identifier="chrome_105")
    headers = {"Pragma": "no-cache","Accept": "*/*","Content-Type": "application/json","Accept-Language": "en-US","Accept-Encoding": "gzip, deflate","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36","X-Debug-Options": "bugReporterEnabled","Sec-Fetch-Dest": "empty","Sec-Fetch-Mode": "cors","Sec-Fetch-Site": "same-origin"}
    r = str(re.findall(r"r:'[^']*'", session.get("https://discord.com/", headers=headers).text)[0]).replace("r:'", "").replace("'", "")
    m = str(re.findall(r"m:'[^']*'", session.get("https://discord.com/", headers=headers).text)[0]).replace("m:'", "").replace("'", "")
    payload = {"m": m,"results": [str(binascii.b2a_hex(os.urandom(16)).decode('utf-8')),str(binascii.b2a_hex(os.urandom(16)).decode('utf-8'))],"timing": random.randint(40, 120),"fp": {"id": 3,"e": {"r": [1920,1080],"ar": [1040,1920],"pr": 1,"cd": 24,"wb": False,"wp": False,"wn": False,"ch": True,"ws": False,"wd": False}}}
    headers["content-type"] = "application/json"
    session.post(f'https://discord.com/cdn-cgi/challenge-platform/h/b/cv/result/', headers=headers, json=payload)
    return session

def get_messages(tokens,channel_id):
    global messages
    while True:
        headers = get_headers()
        headers["authorization"] = tokens
        messages = []
        session = get_session()
        req = session.get(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers)
        if req.status_code == 200:
            for message in req.json():
                if 'bitrate' not in message and message['type'] == 0:
                    if message not in messages:
                        print(f"Scraped {messages}")
                        messages.append(message["id"])
            print(f"Total Scrapped: {len(messages)}")
            return messages
        else:
            continue