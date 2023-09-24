import requests
import sys
sys.dont_write_bytecode = True

def get_cookie():
    session = requests.Session()
    discord = session.get('https://discord.com')
    found_cookies = session.cookies.get_dict()
    return f'__dcfduid={found_cookies["__dcfduid"]}; __sdcfduid={found_cookies["__sdcfduid"]}; locale=ja-JP'
