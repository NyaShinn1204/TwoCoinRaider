import requests
import time
import threading
import traceback
import random
import base64
import json
import tls_client
import re
from httpx import Client
import bypass.header as header
from httpx_socks import SyncProxyTransport
from capmonster_python import HCaptchaTask
from concurrent.futures import ThreadPoolExecutor
from anticaptchaofficial.hcaptchaproxyless import hCaptchaProxyless
    
def start(tokens, serverid, invitelink, memberscreen, delay, module_status):
    for token in tokens:
        threading.Thread(target=joiner_thread, args=(token, serverid, invitelink, memberscreen, module_status)).start()
        time.sleep(float(delay))

def get_session():
    session = tls_client.Session(client_identifier="chrome_105")
    return session

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def joiner_thread(token, serverid, invitelink, memberscreen, module_status):
    data = {}
    agent_string = header.random_agent.random_agent()
    browser_data = agent_string.split(" ")[-1].split("/")
    possible_os_list = ["Windows", "Macintosh"]
    for possible_os in possible_os_list:
        if possible_os in agent_string:
            agent_os = possible_os
    if agent_os == "Macintosh":
        os_version = f'Intel Mac OS X 10_15_{str(random.randint(5, 7))}'
    else:
        os_version = "10"
    cookie_string = header.get_cookie.get_cookie()
    device_info = {
        "os": agent_os,
        "browser": browser_data[0],
        "device": "",
        "system_locale": "ja-JP",
        "browser_user_agent": agent_string,
        "browser_version": browser_data[1],
        "os_version": os_version,
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": 36127,
        "client_event_source": None
    }
    headers = {
        "Accept":"*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US",
        "Authorization": token,
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": cookie_string,
        "Host": "discord.com",
        "Origin": "https://discord.com",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "sec-ch-ua-platform": "Windows",
        "sec-ch-ua-mobile": "?0",
        "TE": "Trailers",
        "User-Agent": header.random_agent.random_agent(),
        "X-Super-Properties": base64.b64encode(json.dumps(device_info).encode('utf-8')).decode("utf-8"),
        "X-Debug-Options": "bugReporterEnabled"
    }
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    try:
        session = get_session()
        joinreq = session.post(f"https://discord.com/api/v9/invites/{invitelink}", headers=headers, json={})
        x = requests.post(f"https://discord.com/api/v9/invites/{invitelink}", headers=headers, json=data)
        if "captcha_key" not in joinreq.json():
            if "You need to verify your account in order to perform this action." in joinreq.json():
                print(f"{extract_token}は認証が必要としています。")
                module_status(1, 2)
            print("[+] Success Join: " + extract_token)
            module_status(1, 1)
        if "captcha_key" in joinreq.json():
            print("[-] Failed join: (Captcha Wrong) " + extract_token)
            
        if memberscreen == True:
            device_info2 = {
                "os": agent_os,
                "browser": browser_data[0],
                "device": "",
                "system_locale": "ja-JP",
                "browser_user_agent": agent_string,
                "browser_version": browser_data[1],
                "os_version": os_version,
                "referrer": "",
                "referring_domain": "",
                "referrer_current": "",
                "referring_domain_current": "",
                "release_channel": "stable",
                "client_build_number": 36127,
                "client_event_source": None
            }
            headers2 = {
                'Content-Type': 'application/json',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US',
                'Cookie': cookie_string,
                'DNT': '1',
                'origin': 'https://discord.com',
                'TE': 'Trailers',
                'X-Super-Properties': base64.b64encode(json.dumps(device_info2).encode('utf-8')).decode("utf-8"),
                'authorization': token,
                'user-agent': header.random_agent.random_agent()
            }
            x1 = requests.get(f"https://canary.discord.com/api/v9/guilds/{serverid}/member-verification?with_guild=false&invite_code=" + invitelink, headers=headers2).json()
            data = {}
            data['version'] = x1['version']
            data['form_fields'] = x1['form_fields']
            data['form_fields'][0]['response'] = True
            x2 = requests.put(f"https://canary.discord.com/api/v9/guilds/{str(serverid)}/requests/@me", headers=headers2, json=data)
            if x2.status_code == 200 or 203:
                print("[+] Success Memberbypass: " + extract_token)
                module_status(1, 3)
                return
            else:
                print("[-] Failed Memberbypass: " + extract_token)
    except Exception as err:
        print(f"[-] ERROR: {err} ")
        print(traceback.print_exc())
        return