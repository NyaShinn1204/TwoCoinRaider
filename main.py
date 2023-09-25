import subprocess
import tkinter as tk
import customtkinter as ctk
from customtkinter import *
from PIL import Image
import webbrowser
import threading
import os
import time

import module.token_checker as token_checker
import module.proxy_checker as proxy_checker
import module.joiner as module_joiner
import module.leaver as module_leaver
import module.spam.spammer as module_spammer
import module.vcspam as module_vc

class Setting:
  tokens = []
  validtoken = StringVar
  invalidtoken = StringVar
  totaltoken = StringVar
  proxies = []
  vaildproxies = StringVar
  invaildproxies = StringVar
  totalproxies = StringVar
  proxytype = "http"


def clear_terminal():
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    _ = os.system('cls')

def get_hwid():
  cmd = 'wmic csproduct get uuid'
  uuid = str(subprocess.check_output(cmd))
  pos1 = uuid.find("\\n")+2
  uuid = uuid[pos1:-15]
  return uuid

def token_load():
  tokens = open("tokens.txt", 'r').read().splitlines()
  if tokens == []:
      return
  Setting.tokens = []
  Setting.validtoken = 0
  Setting.invalidtoken = 0
  Setting.totaltoken = len(tokens)
  threading.Thread(target=token_checker.check(tokens, update_token)).start()

def update_token(status, token):
  if status == True:
      Setting.tokens.append(token)
      Setting.validtoken += 1
  if status == False:
      Setting.invalidtoken += 1

def proxy_load():
  proxies = open("proxy.txt", 'r').read().splitlines()
  if proxies == []:
      return
  Setting.proxies = []
  Setting.vaildproxies = 0
  Setting.invaildproxies = 0
  Setting.totalproxies = (len(proxies))
  proxy_checker.check(update_proxy, proxies, Setting.proxytype)
  threading.Thread(target=proxy_checker.check(update_proxy, proxies, Setting.proxytype))
     
def update_proxy(status, proxy):
  if status == True:
      Setting.proxies.append(proxy)
      Setting.vaildproxies += 1
  if status == False:
      Setting.invaildproxies += 1

def module_reload():
  time.sleep(3)
  menu()

def menu():
  clear_terminal()
  print(f"""          
       &#BB#&       
     B?^:::^~?B        _______             _____      _       _____       _     _             
    P^:::^^^^^^P      |__   __|           / ____|    (_)     |  __ \     (_)   | |          
    J~~^^~~~~~~J         | |_      _____ | |     ___  _ _ __ | |__) |__ _ _  __| | ___ _ __ 
    B7~!!~~~!~7B         | \ \ /\ / / _ \| |    / _ \| | '_ \|  _  // _` | |/ _` |/ _ \ '__|
     #5J7777J55          | |\ V  V / (_) | |___| (_) | | | | | | \ \ (_| | | (_| |  __/ |    　
       &&&&&&&           |_| \_/\_/ \___/ \_____\___/|_|_| |_|_|  \_\__,_|_|\__,_|\___|_|   
                                            This Software was Paid                                                      
                                       
You HWID: [{get_hwid()}]  
Loaded Token: {Setting.totaltoken}  Valid Token: {Setting.validtoken}  Invalid Token: {Setting.invalidtoken}  
Loaded Proxy: {Setting.totalproxies}  Valid Proxie: {Setting.vaildproxies}  Invalid Proxie: {Setting.invaildproxies}
-------------------------""")
  module_mode = input("""
    [01] Joiner     [03] Spammer
    [02] Leaver     [04] VC Spammer

Select Mode >> """)

  tokens = Setting.tokens
  delay = int(0.1)
  proxysetting = True
  proxies = Setting.proxies
  proxytype = Setting.proxytype
  if module_mode == "1":
    invitelink = input("InviteURL >> ")
    memberscreen = input("MemberScreen Found? True/False >> ")
    
    if invitelink.__contains__('discord.gg/'):
      invitelink = invitelink.replace('discord.gg/', '').replace('https://', '').replace('http://', '')
    elif invitelink.__contains__('discord.com/invite/'):
      invitelink = invitelink.replace('discord.com/invite/', '').replace('https://', '').replace('http://', '')
    try:
      invitelink = invitelink.split(".gg/")[1]
    except:
      pass
    
    if invitelink == "":
      print("[-] InviteLink is not set")
      return
    if memberscreen == True:
      serverid = input("ServerID >> ")
      
      if serverid == "":
        print("[-] ServerID is not set")
        return
    
    input("Enter to Start")
    threading.Thread(target=module_joiner.start, args=(tokens, serverid, invitelink, memberscreen, delay)).start()
    
  if module_mode == "2":
    serverid = input("ServerID >> ")
    
    input("Enter to Start")
    threading.Thread(target=module_leaver.start, args=(serverid, delay, tokens)).start()
    
  if module_mode == "3":
    serverid = input("ServerID >> ")
    channelid = input("ChannelID >> ")
    allchannel = input("AllChannel True/False >> ")
    allping = input("AllPing True/False >> ")
    randomstring = input("RandomString True/False >> ")
    ratelimit = input("RateLimitFixer True/False >> ")
    
    contents = input("Spam Message >> ")
    if allping == True:
      mentions = int(input("How Many Mentions? int>> "))
    else:
      mentions = 20
    
    if serverid == "":
        print("[-] ServerID is not set")
        return
    if channelid == "":
        print("[-] ChannelID is not set")
        return    
      
    input("Enter to Start")
    threading.Thread(target=module_spammer.start, args=(delay, tokens, proxysetting, proxies, proxytype, serverid, channelid, contents, allchannel, allping, mentions, randomstring, ratelimit)).start()
    
  if module_mode == "4":
    serverid = input("ServerID >> ")
    channelid = input("ChannelID >> ")
    file_name = input("Mp3 File Name >> ")
    
    if file_name.__contains__('.mp3'):
      file_name = file_name.replace('.mp3', '')
    
    if serverid == "":
      print("[-] ServerID is not set")
      return
    if channelid == "":
      print("[-] ChannelID is not set")
      return    
    if file_name == "":
      print("[-] Mp3 File Name is not set")
      return
    
  else:
    menu()
    
token_load()
time.sleep(1)
proxy_load()
print("Proxyの数が多いと時間がかかる可能性があります")
time.sleep(5)
menu()