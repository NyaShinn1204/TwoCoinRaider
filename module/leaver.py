import requests
import time
import sys
import atexit
sys.dont_write_bytecode = True
import threading

def start(serverid, delay, tokens, module_reload):
    for token in tokens:
        threading.Thread(target=thread, args=(serverid, token, module_reload)).start()
        time.sleep(float(delay))
    
def thread(serverid, token, module_reload):
    try:
        atexit.register(module_reload)
        headers = {"authorization": token}
        x = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{serverid}", headers=headers)
        if x.status_code == 204:
            print("[+] Success Leave: " + token)
            return
        else:
            print("[-] Failed Leave: " + token)
            return
    except Exception as err:
        print("[-] Failed Leave: " + token)
        return
