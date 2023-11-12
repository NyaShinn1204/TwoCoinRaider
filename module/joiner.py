import colorama
import time
import threading
import traceback
import random
import base64
import json
import tls_client
import re
import httpx
from capmonster_python import HCaptchaTask
from colorama import Fore

import bypass.header as header
import bypass.solver.solver as solver

colorama.init(autoreset=True)
    
enable_captcha = False
capmonster_key = "1Mi37Ee2Ehsimx7DFohjQrBrER6Ysjfodk"
    
def start(tokens, serverid, invitelink, memberscreen, delay, module_status):
    for token in tokens:
        threading.Thread(target=joiner_thread, args=(token, serverid, invitelink, memberscreen, module_status)).start()
        time.sleep(float(delay))

def get_session():
    session = tls_client.Session(
        client_identifier="chrome_105",
        random_tls_extension_order=True,
        ja3_string="771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,10-23-27-43-13-65281-16-5-45-18-0-11-35-17513-51-21-41,29-23-24,0",
        h2_settings={"HEADER_TABLE_SIZE": 65536,"MAX_CONCURRENT_STREAMS": 1000,"INITIAL_WINDOW_SIZE": 6291456,"MAX_HEADER_LIST_SIZE": 262144},
        h2_settings_order=["HEADER_TABLE_SIZE","MAX_CONCURRENT_STREAMS","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"],
        supported_signature_algorithms=["ECDSAWithP256AndSHA256","PSSWithSHA256","PKCS1WithSHA256","ECDSAWithP384AndSHA384","PSSWithSHA384","PKCS1WithSHA384","PSSWithSHA512","PKCS1WithSHA512",],
        supported_versions=["GREASE", "1.3", "1.2"],
        key_share_curves=["GREASE", "X25519"],
        cert_compression_algo="brotli",
        pseudo_header_order=[":method",":authority",":scheme",":path"],
        connection_flow=15663105,
        header_order=["accept","user-agent","accept-encoding","accept-language"]
    )
    return session

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

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
    headers_finger = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://discord.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.51',
        'X-Track': 'eyJvcyI6IklPUyIsImJyb3dzZXIiOiJTYWZlIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKElQaG9uZTsgQ1BVIEludGVybmFsIFByb2R1Y3RzIFN0b3JlLCBhcHBsaWNhdGlvbi8yMDUuMS4xNSAoS0hUTUwpIFZlcnNpb24vMTUuMCBNb2JpbGUvMTVFMjQ4IFNhZmFyaS82MDQuMSIsImJyb3dzZXJfdmVyc2lvbiI6IjE1LjAiLCJvc192IjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfZG9tYWluX2Nvb2tpZSI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOiJzdGFibGUiLCJjbGllbnRfZXZlbnRfc291cmNlIjoic3RhYmxlIn0',
    }
    session = get_session()
    response = session.get('https://discord.com/api/v9/experiments', headers=headers_finger)
    if response.status_code == 200:
        data = response.json()
        fingerprint = data["fingerprint"]
        print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [joiner.py:88] {Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX}Got Fingerprint {Fore.RESET} | {Fore.GREEN}{fingerprint}{Fore.RESET}")
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
        "x-fingerprint": fingerprint,
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
                print("[-] Captcha Bypassing.. "+ extract_token)
                payload = {
                    "captcha_key": solver.captcha_bypass_capmonster(token, "https://discord.com", f"{joinreq.json()['captcha_sitekey']}", joinreq.json()['captcha_rqdata']), 'captcha_rqtoken': joinreq.json()['captcha_rqtoken']
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
            
            else:
                if "captcha_key" in joinreq.json():
                    print("[-] Failed join: (Captcha Wrong) " + extract_token)
                    module_status(1, 2)
        elif joinreq.status_code == 200:
            if "captcha_key" not in joinreq.json():
                if joinreq.json().get("message") == "The user is banned from this guild.":
                    print(f"{extract_token}はサーバーからBANされています")
                if "You need to verify your account in order to perform this action." in joinreq.json():
                    print(f"{extract_token}は認証が必要としています")
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