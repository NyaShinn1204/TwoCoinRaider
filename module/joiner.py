import time
import threading
import requests
import base64
import re

import bypass.header as header
import bypass.solver.solver as solver
    
def start(tokens, serverid, invitelink, memberscreen, delay, module_status, answers, apis, bypasscaptcha, delete_joinms, join_channelid):
    for token in tokens:
        threading.Thread(target=joiner_thread, args=(token, serverid, invitelink, memberscreen, module_status, answers, apis, bypasscaptcha, delete_joinms, join_channelid)).start()
        time.sleep(float(delay))

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def member_screen_bypass(token, requests, serverid):
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    session = header.get_session.get_session()
    req_header = header.request_header_joiner(token)
    headers = req_header[0]
    if 'show_verification_form' in requests:
        bypass_rules = session.get(f"https://discord.com/api/v9/guilds/{serverid}/member-verification?with_guild=false", headers=headers).json()
        accept_rules = session.get(f"https://discord.com/api/v9/guilds/{serverid}/requests/@me", headers=headers, json=bypass_rules)
        if accept_rules.status_code == 201 or accept_rules.status_code == 204:
            print("[+] Success Memberbypass: " + extract_token)
            return
        else:
            print("[-] Failed Memberbypass: " + extract_token)

def delete_join_msg(token, join_channel_id):
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    req_header = header.request_header_joiner(token)
    headers = req_header[0]
    messages = requests.get(f"https://discord.com/api/v9/channels/{join_channel_id}/messages?limit=100",headers=headers).json()
    for message in messages:
        bot_token_id = base64.b64decode(token.split(".")[0]+"==").decode()
        if message["content"]=="" and bot_token_id == message["author"]["id"]:
            deleted_join = requests.delete(f"https://discord.com/api/v9/channels/{join_channel_id}/messages/{message['id']}",headers=headers)
            if deleted_join.status_code==204:
                print("[+] Success Delete Join Message: " + extract_token)
            else:
                print("[-] Failed Delete Join Message: " + extract_token)
                print(deleted_join.text)
            break
        
def joiner_thread(token, serverid, invitelink, memberscreen, module_status, answers, apis, bypasscaptcha, delete_joinms, join_channelid):
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    session = header.get_session.get_session()
    req_header = header.request_header_joiner(token)
    headers = req_header[0]
    try:
        joinreq = session.post(f"https://discord.com/api/v9/invites/{invitelink}", headers=headers, json={})
        if joinreq.status_code == 400:

            if bypasscaptcha == True:
                print("[-] Captcha Bypassing.. "+ extract_token)
                sitekey = joinreq.json()['captcha_sitekey']
                url = "https://discord.com"
                payload = {
                    "captcha_key": solver.bypass_captcha(answers, token, url, sitekey, apis),
                }
                newresponse = session.post(f"https://discord.com/api/v9/invites/{invitelink}", headers=headers, json=payload)
                if newresponse.status_code == 200:
                    if "captcha_key" not in newresponse.json():
                        if "You need to verify your account in order to perform this action." in newresponse.json():
                            print(f"{extract_token}は認証が必要としています。")
                            module_status(1, 1, 2)
                        print("[+] Success Join: " + extract_token)
                        if delete_joinms == True:
                            print("[~] Deleting Join Message...")
                            delete_join_msg(token, join_channelid)
                        module_status(1, 1, 1)
                    if memberscreen == True:
                        member_screen_bypass(token, joinreq.json(), joinreq.json()["guild"]["id"])

            else:
                if "captcha_key" in joinreq.json():
                    print("[-] Failed join: (Captcha Wrong) " + extract_token)
                    print(joinreq.json())
                    module_status(1, 1, 2)
        elif joinreq.status_code == 200:
            if "captcha_key" not in joinreq.json():
                if joinreq.json().get("message") == "The user is banned from this guild.":
                    print(f"{extract_token}はサーバーからBANされています")
                if "You need to verify your account in order to perform this action." in joinreq.json():
                    print(f"{extract_token}は認証が必要としています")
                    module_status(1, 1, 2)
                print("[+] Success Join: " + extract_token)
                if delete_joinms == True:
                    print("[~] Deleting Join Message...")
                    delete_joinms(token, headers, join_channelid)
                module_status(1, 1, 1)
            if memberscreen == True:
                member_screen_bypass(token, joinreq.json(), joinreq.json()["guild"]["id"])
    except Exception as err:
        print(f"[-] ERROR: {err} ")
        return