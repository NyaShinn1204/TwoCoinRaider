import colorama
import time
import threading
import traceback
import random
import base64
import json
import tls_client
import re
from capmonster_python import HCaptchaTask
from colorama import Fore

import bypass.header as header

colorama.init(autoreset=True)
    
enable_captcha = False
    
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

def captcha_bypass(token, url, key, captcha_rqdata):
    startedSolving = time.time()
    capmonster = HCaptchaTask('capmonster_key')
    task_id = capmonster.create_task(url, key, is_invisible=True, custom_data=captcha_rqdata)
    result = capmonster.join_task_result(task_id)
    response = result.get("gRecaptchaResponse")
    print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [joiner.py:34] {Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX}Solved{Fore.RESET} | {Fore.YELLOW}{response[-32:]} {Fore.RESET}In {Fore.YELLOW}{round(time.time()-startedSolving)}s{Fore.RESET}")
    return response

def joiner_thread(token, serverid, invitelink, memberscreen, module_status):
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
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
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
        "Authorization": token,
        "Cookie": cookie_string,
        "Host": "discord.com",
        "Pragma": "no-cache",
        "Authority": "discord.com",
        "Accept":"*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://discord.com",
        "Referer": "https://discord.com/channels/@me",
        "Sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108"',
        "Sec-ch-ua-mobile": "?0",
        "Sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": header.random_agent.random_agent(),
        "X-Debug-Options": "bugReporterEnabled",
        "X-Discord-Locale": "en-US",
        "X-Discord-Timezone": "America/New_York",
        "X-Super-Properties": base64.b64encode(json.dumps(device_info).encode('utf-8')).decode("utf-8")
    }
    try:
        session = get_session()
        joinreq = session.post(f"https://discord.com/api/v9/invites/{invitelink}", headers=headers, json={})
        if joinreq.status_code == 400:
            
            if enable_captcha == True:
                payload = {
                    "captcha_key": captcha_bypass(token, "https://discord.com", f"{joinreq.json()['captcha_sitekey']}", joinreq.json()['captcha_rqdata']), 'captcha_rqtoken': joinreq.json()['captcha_rqtoken']
                }
                newresponse = session.post(f"https://discord.com/api/v9/invites/{invitelink}", headers=headers, json=payload)
                if newresponse.status_code == 200:
                    if "captcha_key" not in newresponse.json():
                        if "You need to verify your account in order to perform this action." in newresponse.json():
                            print(f"{extract_token}は認証が必要としています。")
                            module_status(1, 2)
                        print("[+] Success Join: " + extract_token)
                        module_status(1, 1)
                    if memberscreen == True:
                        b = newresponse.json()
                        server_id = b["guild"]["id"]
                        if 'show_verification_form' in b:
                            bypass_rules = session.get(f"https://discord.com/api/v9/guilds/{server_id}/member-verification?with_guild=false", headers=headers).json()
                            accept_rules = session.get(f"https://discord.com/api/v9/guilds/{server_id}/requests/@me", headers=headers, json=bypass_rules)
                            if accept_rules.status_code == 201 or accept_rules.status_code == 204:
                                print("[+] Success Memberbypass: " + extract_token)
                                return
                            else:
                                print("[-] Failed Memberbypass: " + extract_token)
            
            if "captcha_key" in joinreq.json():
                print("[-] Failed join: (Captcha Wrong) " + extract_token)
                module_status(1, 2)
        elif joinreq.status_code == 200:
            if "captcha_key" not in joinreq.json():
                if "You need to verify your account in order to perform this action." in joinreq.json():
                    print(f"{extract_token}は認証が必要としています。")
                    module_status(1, 2)
                print("[+] Success Join: " + extract_token)
                module_status(1, 1)
            if memberscreen == True:
                b = joinreq.json()
                server_id = b["guild"]["id"]
                if 'show_verification_form' in b:
                    bypass_rules = session.get(f"https://discord.com/api/v9/guilds/{server_id}/member-verification?with_guild=false", headers=headers).json()
                    accept_rules = session.get(f"https://discord.com/api/v9/guilds/{server_id}/requests/@me", headers=headers, json=bypass_rules)
                    if accept_rules.status_code == 201 or accept_rules.status_code == 204:
                        print("[+] Success Memberbypass: " + extract_token)
                        return
                    else:
                        print("[-] Failed Memberbypass: " + extract_token)
    except Exception as err:
        print(f"[-] ERROR: {err} ")
        print(traceback.print_exc())
        return