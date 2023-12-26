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


def load_gui(mode, theme):
  if mode == "gui":
    if theme == "old":
      subprocess.run("python old.py")
    if theme == "new":
      subprocess.run("python new.py")
  elif mode == "cli":
    subprocess.run("python cli.py")

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

def config_check(mode):
  try:
    if os.path.exists(r"config.json"):
      printl("debug", "Config Found")
      ffmpeg_check()
      if mode == "gui":
        with open("config.json", "r") as f:
          json_show = json.load(f)
        theme = json_show["theme"]
      load_gui(mode, theme)
    else:
      printl("error", "Config Not Found")
      printl("error", "token path not found. Please point to it manually.")
      printl("error", "theme select not found. Please point to it manually.")
      config_load(mode)
  except Exception as error:
    print(error)
    printl("error", "Config Load Error")
    printl("error", "Please Retry Select")
    config_load(mode)

def ffmpeg_check():
  ffmpeg_path = os.path.join(os.getcwd(), "./data/ffmpeg.exe")
  dll_path = os.path.join(os.getcwd(), "./data/libopus.dll")
  if os.path.exists(ffmpeg_path):
    printl("debug", "FFmpeg Found")
  else:
    printl("debug", "FFmpeg Not Found")
    download_file("ffmpeg")
  if os.path.exists(dll_path):
    printl("debug", "FFmpeg lib Found")
  else:
    printl("debug", "FFmpeg lib Not Found")
    download_file("ffmpeg-dll")

def download_file(type):
  if type == "ffmpeg":
    with open("./data/ffmpeg.exe", mode="wb") as f:
      f.write(requests.get("https://github.com/NyaShinn1204/twocoin-assets/raw/main/ffmpeg.exe").content)
      printl("info", "Download FFmpeg")
  if type == "ffmpeg-dll":
    with open("./data/libopus.dll", mode="wb") as f:
      f.write(requests.get("https://github.com/NyaShinn1204/twocoin-assets/raw/main/libopus.dll").content)
      printl("info", "Download FFmpeg Dll")

def config_load(mode):
  if mode == "gui":
    window = tk.Tk()
    window.geometry("10x10")
    window.resizable(0, 0)
    window.title("TwoCoinRaider | " + version)
    window.iconbitmap(default="data/favicon.ico")
    filepath = filedialog.askopenfilename(
      filetype=[("", "*.txt")],
      initialdir=os.path.abspath(os.path.dirname(__file__)),
      title="Select Tokens File",
    )
  elif mode == "cli":
    filepath = input("Select Tokens File Name (e.x tokens.txt) >> ")
    filepath = os.getcwd()+"/"+filepath
  if filepath == "":
    printl("error", "Please Select Token File")
    sys.exit()
  else:
    printl("info", "Select " + os.path.basename(filepath))
  tokens = open(filepath, "r").read().splitlines()
  if tokens == []:
    printl("debug", "You Select 0 tokens File")
    sys.exit()
  import data.setting as config
  if mode == "gui":
    window.geometry("150x100")
    def optionmenu_callback(choice):
      printl("info", "Select Theme " + choice)
      config.Settingdata = {"token_path": filepath, "theme": choice}
      tokens_file = json.dumps(config.Settingdata)
      with open("config.json", "w") as configfile:
        configfile.write(tokens_file)
      window.destroy()
      load_gui("gui", choice)
    optionmenu = ctk.CTkOptionMenu(window, values=["old", "new"], command=optionmenu_callback)
    optionmenu.pack()
    optionmenu.set("Select Theme")
    window.mainloop()
  else:
    tokens_file = json.dumps({"token_path": filepath})
    with open("config.json", "w") as configfile:
      configfile.write(tokens_file)
    load_gui("cli", None)

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