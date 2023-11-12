import re
import time
import httpx
import colorama
from colorama import Fore

colorama.init(autoreset=True)

_capmonster_key = ""
_2cap_key = ""
_capsolver_key = ""

def extract(format_token):
    if re.compile(r"(.+):").match(format_token):
        return format_token.split(":")[1]
    else:
        token = format_token
    return token

def get_balance_capmonster():
    resp = httpx.post(f"https://api.capmonster.cloud/getBalance", json={"clientKey": _capmonster_key}).json()
    if resp.get("errorId") > 0:
        print(f"Error while getting captcha balance: {resp.get('errorDescription')}")
        return 0.0
    return resp.get("balance")

def get_balance_2cap():
    resp = httpx.post(f"https://api.2captcha.com/getBalance", json={"clientKey": _2cap_key}).json()
    if resp.get("errorId") > 0:
        print(f"Error while getting captcha balance: {resp.get('errorDescription')}")
        return 0.0
    return resp.get("balance")

def get_balance_capsolver():
    resp = httpx.post(f"https://api.capsolver.com/getBalance", json={"clientKey": _capsolver_key}).json()
    if resp.get("errorId") > 0:
        print(f"Error while getting captcha balance: {resp.get('errorDescription')}")
        return 0.0
    return resp.get("balance")

def captcha_bypass_capmonster(token, url, key, captcha_rqdata, captcha_rqtoken):
    if get_balance_capmonster == 0.0:
        return
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    startedSolving = time.time()
    url = "https://api.capmonster.cloud/createTask"
    data = {
        "clientKey": _capmonster_key,
        "task":
        {
            "type": "HCaptchaTaskProxyless",
            "websiteURL": url,
            "websiteKey": key
        }
    }
    response = httpx.post(url,json=data)
    if response.json()['errorId'] == 0:
        task_id = response.json()['taskId']
        url = "https://api.capmonster.cloud/getTaskResult"
        data = {
            "clientKey": _capmonster_key,
            "taskId": task_id
        }
        response = httpx.post(url,json=data)
        while response.json()['status'] == 'processing':
            time.sleep(3)
            response = httpx.post(url,json=data)
        print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [solver.py] {Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX}Solved{Fore.RESET} | {Fore.YELLOW}{response[-32:]} {Fore.RESET}In {Fore.YELLOW}{round(time.time()-startedSolving)}s{Fore.RESET} | " + extract_token)
        return response.json()['solution']['gRecaptchaResponse']
    else:
        print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [solver.py] {(response.json()['errorDescription'])}")
        return False
    
def captcha_bypass_2cap(token, url, key, captcha_rqdata, captcha_rqtoken):
    if get_balance_2cap == 0.0:
        return
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    startedSolving = time.time()
    url = "https://2captcha.com/in.php?key={}&method=hcaptcha&sitekey={}&pageurl={}".format(_2cap_key,key,url)
    response = httpx.get(url)
    if response.text[0:2] == 'OK':
        captcha_id = response.text[3:]
        url = "http://2captcha.com/res.php?key={}&action=get&id={}".format(_2cap_key,captcha_id)
        response = httpx.get(url)
        while 'CAPCHA_NOT_READY' in response.text:
            time.sleep(5)
            response = httpx.get(url)
            print(response.text)
        print(response.text)
        return response.text.replace('OK|','') , str(time.time() - startedSolving)
    else:
        print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [solver.py] {(response.text)}")
        return False
    
def captcha_bypass_capsolver(token, url, key, captcha_rqdata, captcha_rqtoken):
    if get_balance_capsolver == 0.0:
        return
    extract_token = f"{extract(token+']').split('.')[0]}.{extract(token+']').split('.')[1]}"
    startedSolving = time.time()
    json = {
        "clientKey": _capsolver_key,
        "task": {
            "type": "HCaptchaTaskProxyLess",
            "websiteURL": url,
            "websiteKey": key,
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = httpx.post('https://api.capsolver.com/createTask', headers=headers, json=json)
    try:
        taskid = response.json()['taskId']
    except:
        print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [solver.py] {(response.json()['errorDescription'])}")
        return 
    json = {"clientKey": _capsolver_key, "taskId": taskid}
    while True:
        time.sleep(1.5)
        response = httpx.post('https://api.capsolver.com/getTaskResult', headers=headers, json=json)
        if response.json()['status'] == 'ready':
            captchakey = response.json()['solution']['gRecaptchaResponse']
            print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [solver.py] {Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX}Solved{Fore.RESET} | {Fore.YELLOW}{response[-32:]} {Fore.RESET}In {Fore.YELLOW}{round(time.time()-startedSolving)}s{Fore.RESET} | " + extract_token)
            return captchakey
        else:
            continue