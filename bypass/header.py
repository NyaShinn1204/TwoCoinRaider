import base64
import json
import random

import bypass.get_cookie as get_cookie
import bypass.get_session as get_session
import bypass.get_fingerprint as get_fingerprint
import bypass.random_agent as random_agent

def request_header(token):
    agent_string = random_agent.random_agent()
    browser_data = agent_string.split(" ")[-1].split("/")
    possible_os_list = ["Windows", "Macintosh"]
    for possible_os in possible_os_list:
        if possible_os in agent_string:
            agent_os = possible_os
    if agent_os == "Macintosh":
        os_version = f'Intel Mac OS X 10_15_{str(random.randint(5, 7))}'
    else:
        os_version = "10"
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
        "Accept":"*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US",
        "Authorization": token,
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "discord.com",
        "Origin": "https://discord.com",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "sec-ch-ua-platform": "Windows",
        "sec-ch-ua-mobile": "?0",
        "TE": "Trailers",
        "User-Agent": agent_string,
        "X-Super-Properties": base64.b64encode(json.dumps(device_info).encode('utf-8')).decode("utf-8"),
        "X-Debug-Options": "bugReporterEnabled"
    }
    headers2 = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US',
        'DNT': '1',
        'origin': 'https://discord.com',
        'TE': 'Trailers',
        'X-Super-Properties': base64.b64encode(json.dumps(device_info).encode('utf-8')).decode("utf-8"),
        'authorization': token,
        'user-agent': agent_string
    },
    headers3 = {
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
    return headers, headers2, headers3

def request_header_fingerprint(token):
    agent_string = random_agent.random_agent()
    fingerprint = get_fingerprint.get_fingerprint()
    browser_data = agent_string.split(" ")[-1].split("/")
    possible_os_list = ["Windows", "Macintosh"]
    for possible_os in possible_os_list:
        if possible_os in agent_string:
            agent_os = possible_os
    if agent_os == "Macintosh":
        os_version = f'Intel Mac OS X 10_15_{str(random.randint(5, 7))}'
    else:
        os_version = "10"
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
    headers3 = {
        "Accept":"*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US",
        "Authorization": token,
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Host": "discord.com",
        "Origin": "https://discord.com",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "sec-ch-ua-platform": "Windows",
        "sec-ch-ua-mobile": "?0",
        "TE": "Trailers",
        "User-Agent": agent_string,
        "x-fingerprint": fingerprint,
        "X-Super-Properties": base64.b64encode(json.dumps(device_info).encode('utf-8')).decode("utf-8"),
        "X-Debug-Options": "bugReporterEnabled"
    }
    return headers3