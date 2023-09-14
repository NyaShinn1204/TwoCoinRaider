import requests
import time
import sys
sys.dont_write_bytecode = True
import threading

status = True

def status():
    global status
    return status

def stop():
    global status
    status = False

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
    if status is False:
        return
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    try:
        if status is False:
            return
        headers = {"authorization": token}
        x = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{serverid}", headers=headers)
        if x.status_code == 204:
            print("[+] Success Leave: "+extract_token)
            return
        else:
            if x.status_code == 403:
                print("[-] Failed Leave: "+extract_token)
                return
    except Exception as err:
        print("sippai")
        return
