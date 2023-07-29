import random
import time
import sys
sys.dont_write_bytecode = True
import threading
from httpx import Client
from httpx_socks import SyncProxyTransport

def start(tokens, proxysetting, proxies, proxytype, serverid, delay, update_module, alltokenuse, TokenuseCount):
    for token in tokens:
        threading.Thread(target=thread, args=(token, proxysetting, proxies, proxytype, serverid, delay, update_module)).start()
        time.sleep(float(delay))
    
def thread(token, proxysetting, proxies, proxytype, serverid, delay, update_module):
    try:
        headers = {"authorization": token}
        request = Client()
        if proxysetting == True:
            proxy = random.choice(proxies)
            request = Client(transport=SyncProxyTransport.from_url(f'{proxytype}://{proxy}'))
        x = request.delete(f"https://discord.com/api/v9/users/@me/guilds/{serverid}", headers=headers)
        if x.status_code == 204:
            update_module(2, 1)
            return
        else:
            update_module(2, 2)
            if x.status_code == 403:
                update_module(2, 2)
                return
    except Exception as err:
        update_module(2, 2)
        return