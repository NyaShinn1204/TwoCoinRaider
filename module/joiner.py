import colorama
import time
import threading
import traceback
import requests
import random
import base64
import json
import tls_client
import re
from colorama import Fore

import bypass.header as header
import bypass.solver.solver as solver

colorama.init(autoreset=True)
    
def start(tokens, serverid, invitelink, memberscreen, delay, module_status, answers, apis, bypasscaptcha):
    for token in tokens:
        threading.Thread(target=joiner_thread, args=(token, serverid, invitelink, memberscreen, module_status, answers, apis, bypasscaptcha)).start()
        time.sleep(float(delay))

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def joiner_thread(token, serverid, invitelink, memberscreen, module_status, answers, apis, bypasscaptcha):
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    session = header.get_session.get_session()
    req_header = header.request_header_joiner(token)
    headers = req_header[0]
    try:
        joinreq = session.post(f"https://discord.com/api/v9/invites/{invitelink}", headers=headers, json={})
        if joinreq.status_code == 400:

            if bypasscaptcha == True:
                print("[-] Captcha Bypassing.. "+ extract_token)
                solver.bypass_captcha(answers, "https://discord.com", f"{joinreq.json()['captcha_sitekey']}", apis)
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
        return