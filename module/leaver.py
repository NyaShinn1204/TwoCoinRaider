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

def start(serverid, delay, tokens):
    for token in tokens:
        threading.Thread(target=thread, args=(serverid, token)).start()
        time.sleep(float(delay))
    
def thread(serverid, token):
    if status is False:
        return
    try:
        if status is False:
            return
        headers = {"authorization": token}
        x = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{serverid}", headers=headers)
        if x.status_code == 204:
            print("sakusesu")
            return
        else:
            if x.status_code == 403:
                print("sippai")
                return
    except Exception as err:
        print("sippai")
        return
