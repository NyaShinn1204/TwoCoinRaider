import requests
import time
import re
import threading

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def start(serverid, delay, tokens):
    for token in tokens:
        threading.Thread(target=thread, args=(serverid, token)).start()
        time.sleep(float(delay))
    
def thread(serverid, token):
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    try:
        headers = {"authorization": token}
        x = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{serverid}", headers=headers)
        if x.status_code == 204:
            print("[+] Success Leave: "+extract_token)
            return
        else:
            if x.status_code == 403:
                print("[-] Failed Leave: "+extract_token)
                return
    except Exception:
        print("[-] Failed Leave: "+extract_token)
        return
