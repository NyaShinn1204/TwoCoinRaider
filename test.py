import os
import time
import json
import threading
import webbrowser
import subprocess
import tkinter
 
try:
  import requests
  import colorama
  import customtkinter
  import CTkToolTip
  import CTkMessagebox
except ImportError:
  print("足りないモジュールをインストールします")
  os.system("pip install -r ./data/requirements.txt")
import requests
import colorama
import tkinter as tk
import customtkinter as ctk
from colorama import Fore
from customtkinter import *

colorama.init(autoreset=True)

version = "v1.0.3"

def get_filename():
  return os.path.basename(__file__)

def printl(num, data):
  if num == "error":
    print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [{get_filename()}] " + data)
  if num == "debug":
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [{get_filename()}] " + data)
  if num == "info":
    print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [{get_filename()}] " + data)


def get_hwid():
  if os.name == "posix":
    uuid = "Linux unsupported"
    return uuid
  else:
    cmd = "wmic csproduct get uuid"
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n") + 2
    uuid = uuid[pos1:-15]
    return uuid
  if uuid == "":
    printl("error", "get_hwid error wrong")

def update_check():
  try:
    version_get = requests.get("https://raw.githubusercontent.com/NyaShinn1204/twocoin-assets/main/version").text
    if version_get.__contains__('\n'):
      version_get = version_get.replace('\n', '')
    if version == version_get:
      printl("info", "Latest Version")
    else:
      printl("error", "You are using an older version")
      printl("error", "New Version "+version_get)
  except:
    printl("error", "Failed to Get Version")

def tkinter_check():
  try:
    tk.Tk()
    printl("info", "supported GUI, Start Gui")
    printl("debug", "Load Config")
    config_check("gui")
  except: 
    printl("error", "not supported GUI, Start Cli")
    config_check("cli")

print(
    f"""
       &#BB#&
     B?^:::^~?B        _______             _____      _       _____       _     _ 
    P^:::^^^^^^P      |__   __|           / ____|    (_)     |  __ \     (_)   | | 
    J~~^^~~~~~~J         | |_      _____ | |     ___  _ _ __ | |__) |__ _ _  __| | ___ _ __ 
    B7~!!~~~!~7B         | \ \ /\ / / _ \| |    / _ \| | '_ \|  _  // _` | |/ _` |/ _ \ '__|
     #5J7777J55          | |\ V  V / (_) | |___| (_) | | | | | | \ \ (_| | | (_| |  __/ |
       &&&&&&&           |_| \_/\_/ \___/ \_____\___/|_|_| |_|_|  \_\__,_|_|\__,_|\___|_|
                                            This Software was Paid Only

You HWID: [{get_hwid()}]                Version: [{version}]
-----------------------"""
)
printl("debug", "Checking Version")
update_check()
printl("debug", "Check use tkinter")
tkinter_check()