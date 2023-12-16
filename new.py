import os
import time
import json
import threading
import webbrowser
import subprocess
import tkinter
 
import requests
import colorama
import tkinter as tk
import customtkinter as ctk
from PIL import Image
from colorama import Fore
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from CTkToolTip import *

import module.token_checker as token_checker
import module.proxy_checker as proxy_checker

colorama.init(autoreset=True)

version = "v1.0.3"
theme = "twocoin"

def get_filename():
  return os.path.basename(__file__)

def printl(num, data):
  if num == "error":
    print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [{get_filename()}] " + data)
  if num == "debug":
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [{get_filename()}] " + data)
  if num == "info":
    print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [{get_filename()}] " + data)
    
def extractfi(input_str):
  if len(input_str) >= 5:
    replaced_str = input_str[:-5] + '*' * 5
    return replaced_str
  else:
    return input_str

with open('config.json') as f:
    data_load = json.load(f)
try:
  if data_load['select_theme']:
    theme = data_load['select_theme']
  printl("info", "Load Theme Name: " + theme)
except:
  printl("debug", "Not Found Save Theme")
finally:
  if theme == "akebi":
    c1 = "#040f24"
    c2 = "#020b1f"
    c3 = "#0a2b63"
    c4 = "#020b1f"
    c5 = "#00bbe3"
    c6 = "#0a2b63"
    c7 = "#142326"
  if theme == "twocoin":
    c1 = "#28464B"
    c2 = "#213A3E"
    c3 = "#00484C"
    c4 = "#142326"
    c5 = "#2C8C99"
    c6 = "#002D2D"
    c7 = "#142326"

def update_theme(num1, num2):
  global c1,c2,c3,c4,c5,c6,c7
  if theme == "akebi":
    c1 = "#040f24"
    c2 = "#020b1f"
    c3 = "#0a2b63"
    c4 = "#020b1f"
    c5 = "#00bbe3"
    c6 = "#0a2b63"
    c7 = "#000117"
  if theme == "twocoin":
    c1 = "#28464B"
    c2 = "#213A3E"
    c3 = "#00484C"
    c4 = "#142326"
    c5 = "#2C8C99"
    c6 = "#002D2D"
    c7 = "#142326"
  apply_frame(num1, num2)

def apply_frame(num1, num2):
  modulelist.destroy()
  module_frame.destroy()
  module_list_frame()
  module_scroll_frame(num1, num2)

def setup_frame(num1, num2):
  module_list_frame()
  module_scroll_frame(num1, num2)

root = tk.Tk()
root.geometry("1280x720")
root.resizable(0, 0)
root.title("TwoCoinRaider | "+version)
root.iconbitmap(default="data/favicon.ico")
root.configure(bg="#fff")

import data.setting as config

Setting = config.Setting
SettingVariable = config.SettingVariable

def get_info():
  invite_code = invite_url.get()
  if invite_code.__contains__('discord.gg/'):
    invite_code = invite_code.replace('discord.gg/', '').replace('https://', '').replace('http://', '')
  elif invite_code.__contains__('discord.com/invite/'):
    invite_code = invite_code.replace('discord.com/invite/', '').replace('https://', '').replace('http://', '')
  try:
    invite_code = invite_code.split(".gg/")[1]
  except:
    pass
  printl("debug", "Connecting API Server...")
  res = requests.get(f"https://discord.com/api/v9/invites/{invite_code}?with_counts=true&with_expiration=true")
  if res.status_code == 200:
    printl("debug", "Successfull Get Info")
    info = json.loads(res.text)
    serverid = info["guild"]["id"]
    servername = info["guild"]["name"]
    serverdescription = info["guild"]["description"]
    membercount = str(info["approximate_member_count"])
    boostcount = str(info["guild"]["premium_subscription_count"])
    Setting.joiner_link.set(invite_code)
    Setting.joiner_serverid.set(serverid)
    Setting.leaver_serverid.set(serverid)
    Setting.spam_serverid.set(serverid)
    Setting.reply_serverid.set(serverid)
    Setting.vcspam_serverid.set(serverid)
    Setting.ticket_serverid.set(serverid)
    print(f"""----------\nServer ID\n{serverid}\n----------\nServer Name\n{servername}\n\nServer Description\n{serverdescription}\n----------\nMember Count\n{membercount}\n\nBoost Count\n{boostcount}\n----------""")
    printl("debug", "End Info")
    CTkMessagebox(title="Invite Info", message=f"Server ID: {serverid}\nServer Name: {servername}\nServer Description: {serverdescription}\n\nMember Count: {membercount}\nBoost Count: {boostcount}", width=450)
  if res.status_code == 404:
    printl("error", "Unknown Invite")

def get_hwid():
  if os.name == 'posix':
    uuid = "Linux unsupported"
    return uuid
  else:
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n")+2
    uuid = uuid[pos1:-15]
    return uuid
  if uuid == "":
    printl("error", "get_hwid error wrong")

def config_check():
  try:
    if os.path.exists(r"config.json"):
      filepath = json.load(open("config.json", "r"))
      tokens = open(filepath["token_path"], 'r').read().splitlines()
      if theme == "akebi":
        Setting.theme_var.set("Akebi Theme")
      if theme == "twocoin":
        Setting.theme_var.set("Default Theme")
      Setting.tokens = []
      Setting.validtoken = 0
      Setting.invalidtoken = 0
      Setting.token_filenameLabel.set(os.path.basename(filepath["token_path"]))
      Setting.totaltokenLabel.set("Total: "+str(len(tokens)).zfill(3))
      threading.Thread(target=token_checker.check(tokens, update_token)).start()
      printl("debug", "Config Found")
      return True
    else:
      printl("debug", "Config Not Found")
      printl("debug", "token path not found. Please point to it manually.")
      token_load()
      return False
  except:
    printl("error", "Config Load Error")
    printl("error", "Please Reselect")
    token_load()
    return False

def ffmpeg_load():
  global ffmpegfile
  fTyp = [("", "*.exe")]
  iFile = os.path.abspath(os.path.dirname(__file__))
  filepath = filedialog.askopenfilename(
    filetype=fTyp, initialdir=iFile, title="Select FFmpeg.exe")
  if filepath == "":
    return
  ffmpegfile = filepath
  if ffmpegfile == []:
    return

def voice_load():
  fTyp = [("", "*.mp3")]
  iFile = os.path.abspath(os.path.dirname(__file__))
  filepath = filedialog.askopenfilename(
    filetype=fTyp, initialdir=iFile, title="Select Voice File")
  if filepath == "":
    return
  Setting.voicefile = filepath
  if filepath == []:
    return
  voicefile_show = filepath.split('/')[len(filepath.split('/'))-1]
  Setting.voicefile_filenameLabel.set(voicefile_show)

# Token Tab
def token_load():
  fTyp = [("", "*.txt")]
  iFile = os.path.abspath(os.path.dirname(__file__))
  filepath = filedialog.askopenfilename(
    filetype=fTyp, initialdir=iFile, title="Select Tokens")
  if filepath == "":
    return
  if os.path.exists(r"config.json"):
    tokens = open(filepath, 'r').read().splitlines()
  else:
    tokens = open(filepath, 'r').read().splitlines()
  with open('config.json') as f:
    data = json.load(f)
  data.update({"token_path": filepath})
  with open('config.json', 'w') as f:
    json.dump(data, f)
  if tokens == []:
    return
  Setting.tokens = []
  Setting.validtoken = 0
  Setting.invalidtoken = 0
  Setting.token_filenameLabel.set(os.path.basename(filepath))
  Setting.validtokenLabel.set("Valid: 000")
  Setting.invalidtokenLabel.set("Invalid: 000")
  Setting.totaltokenLabel.set("Total: "+str(len(tokens)).zfill(3))
  threading.Thread(target=token_checker.check(tokens, update_token)).start()

def update_token(status, token):
  if status == True:
    Setting.tokens.append(token)
    Setting.validtoken += 1
    Setting.validtokenLabel.set("Valid: "+str(Setting.validtoken).zfill(3))
  if status == False:
    Setting.invalidtoken += 1
    Setting.invalidtokenLabel.set("Invalid: "+str(Setting.invalidtoken).zfill(3))

# Proxy Tab
def proxy_load():
  threading.Thread(target=proxy_main).start()
  
def proxy_main():
  proxy_type = Setting.proxytype.get()
  print(proxy_type)
  if proxy_type == "":
    print("[-] Cancel proxy")
    return
  proxy_filepath()

def proxy_filepath():
  fTyp = [("", "*.txt")]
  iFile = os.path.abspath(os.path.dirname(__file__))
  filepath = filedialog.askopenfilename(filetype=fTyp, initialdir=iFile, title="Select Proxies")
  if filepath == "":
    return
  proxies = open(filepath, 'r').read().splitlines()
  if proxies == []:
    return
  Setting.proxies = []
  Setting.totalproxies = str(len(proxies))
  Setting.vaildproxies = 0
  Setting.invaildproxies = 0
  Setting.proxy_filenameLabel.set(os.path.basename(filepath))
  Setting.totalProxiesLabel.set("Total: "+Setting.totalproxies.zfill(3))
  print("[+] Load: " + Setting.totalproxies + "Proxies")
  time.sleep(1)
  threading.Thread(target=proxy_checker.check(update_proxy, proxies, Setting.proxytype.get()))
     
def update_proxy(status, proxy):
  if status == True:
    Setting.proxies.append(proxy)
    Setting.vaildproxies += 1
    Setting.validProxiesLabel.set("Valid: "+str(Setting.vaildproxies).zfill(3))
  if status == False:
    Setting.invaildproxies += 1
    Setting.invalidProxiesLabel.set("Invalid: "+str(Setting.invaildproxies).zfill(3))

def clear_frame(frame):
  for widget in frame.winfo_children():
    widget.destroy()
  frame.pack_forget()

def module_scroll_frame(num1, num2):
  global invite_url, module_frame
  frame_scroll = module_frame = ctk.CTkScrollableFrame(root, fg_color=c2, bg_color=c2, width=1000, height=630)
  module_frame.place(x=245, y=70)
  clear_frame(frame_scroll)
  if num1 == 1:
    if num2 == 1:
      modules_frame01_01 = ctk.CTkFrame(module_frame, width=470, height=300, border_width=0, fg_color=c1)
      modules_frame01_01.grid(row=0, column=0, padx=6, pady=6)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Joiner", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame01_01, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkCheckBox(modules_frame01_01, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, text="Bypass MemberScreen", variable=Setting.bypass_ms).place(x=5,y=31)
      test = ctk.CTkLabel(modules_frame01_01, text_color="#fff", text="(?)")
      test.place(x=170,y=31)
      CTkToolTip(test, delay=0.5, message="Bypass the member screen when you join.") 
      ctk.CTkCheckBox(modules_frame01_01, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, text="Bypass hCaptcha", variable=Setting.bypass_cap).place(x=5,y=55) 
      test = ctk.CTkLabel(modules_frame01_01, text_color="#fff", text="(?)")
      test.place(x=140,y=55)
      CTkToolTip(test, delay=0.5, message="Automatically resolve hcaptcha")
      ctk.CTkCheckBox(modules_frame01_01, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, text="Delete Join Message", variable=Setting.delete_join_ms).place(x=5,y=79)
      test = ctk.CTkLabel(modules_frame01_01, text_color="#fff", text="(?)")
      test.place(x=160,y=79)
      CTkToolTip(test, delay=0.5, message="Delete the message when you join") 
      
      ctk.CTkButton(modules_frame01_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.joiner_link.set("")).place(x=5,y=109)
      ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c7, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_link).place(x=85,y=109)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Invite Link", font=("Roboto", 12)).place(x=240,y=107)
      ctk.CTkButton(modules_frame01_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.joiner_serverid.set("")).place(x=5,y=138)
      ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c7, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_serverid).place(x=85,y=138)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=136)
      ctk.CTkButton(modules_frame01_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.joiner_channelid.set("")).place(x=5,y=167)
      ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c7, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_channelid).place(x=85,y=167)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=165)

      CTkLabel(modules_frame01_01, text_color="#fff", text="Delay Time (s)", font=("Roboto", 15)).place(x=5,y=192)
      def show_value01_01(value):
          tooltip01_01.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame01_01, from_=0.1, to=3.0, variable=Setting.delay01_01, command=show_value01_01)
      test.place(x=5,y=217)
      tooltip01_01 = CTkToolTip(test, message=round(Setting.delay01_01.get(), 1))

      ctk.CTkButton(modules_frame01_01, text="Start", fg_color=c2, hover_color=c5, width=60, height=25, command=lambda: print("a")).place(x=5,y=237)
      ctk.CTkButton(modules_frame01_01, text="Stop", fg_color=c2, hover_color=c5, width=60, height=25, command=lambda: print("a")).place(x=70,y=237)

      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Join Status", font=("Roboto", 12)).place(x=205,y=30)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.suc_joiner_Label, font=("Roboto", 12)).place(x=210,y=58)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.fai_joiner_Label, font=("Roboto", 12)).place(x=210,y=83)

      modules_frame01_02 = ctk.CTkFrame(module_frame, width=470, height=300, border_width=0, fg_color=c1)
      modules_frame01_02.grid(row=0, column=1, padx=6, pady=6)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", text="Leaver", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame01_02, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkButton(modules_frame01_02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.leaver_serverid.set("")).place(x=5,y=33)
      ctk.CTkEntry(modules_frame01_02, bg_color=c1, fg_color=c7, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.leaver_serverid).place(x=85,y=33)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=31)

      CTkLabel(modules_frame01_02, text_color="#fff", text="Delay Time (s)", font=("Roboto", 15)).place(x=5,y=55)
      def show_value01_02(value):
          tooltip01_02.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame01_02, from_=0.1, to=3.0, variable=Setting.delay01_02, command=show_value01_02)
      test.place(x=5,y=80)
      tooltip01_02 = CTkToolTip(test, message=round(Setting.delay01_02.get(), 1))

      ctk.CTkButton(modules_frame01_02, text="Start", fg_color=c2, hover_color=c5, width=60, height=25, command=lambda: print("a")).place(x=5,y=100)
      ctk.CTkButton(modules_frame01_02, text="Stop", fg_color=c2, hover_color=c5, width=60, height=25, command=lambda: print("a")).place(x=70,y=100)
      
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", text="Leaver Status", font=("Roboto", 12)).place(x=5,y=130)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", textvariable=Setting.suc_leaver_Label, font=("Roboto", 12)).place(x=10,y=155)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", textvariable=Setting.fai_leaver_Label, font=("Roboto", 12)).place(x=10,y=175)

      modules_frame01_03 = ctk.CTkFrame(module_frame, width=470, height=200, border_width=0, fg_color=c1)
      modules_frame01_03.grid(row=1, column=0, padx=6, pady=6)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="VC Joiner", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame01_03, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkButton(modules_frame01_03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.vcjoin_serverid.set("")).place(x=5,y=31)
      ctk.CTkEntry(modules_frame01_03, bg_color=c1, fg_color=c7, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcjoin_serverid).place(x=85,y=31)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=29)
      ctk.CTkButton(modules_frame01_03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.vcjoin_channelid.set("")).place(x=5,y=60)
      ctk.CTkEntry(modules_frame01_03, bg_color=c1, fg_color=c7, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcjoin_channelid).place(x=85,y=60)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=58)

      CTkLabel(modules_frame01_03, text_color="#fff", text="Delay Time (s)", font=("Roboto", 15)).place(x=5,y=82)
      def show_value01_03(value):
          tooltip01_03.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame01_03, from_=0.1, to=3.0, variable=Setting.delay01_03, command=show_value01_03)
      test.place(x=5,y=107)
      tooltip01_03 = CTkToolTip(test, message=round(Setting.delay01_03.get(), 1))

      ctk.CTkButton(modules_frame01_03, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: print("a")).place(x=5,y=127)

      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="VC Joiner Status", font=("Roboto", 12)).place(x=135,y=124)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", textvariable=Setting.suc_vcjoiner_Label, font=("Roboto", 12)).place(x=140,y=149)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", textvariable=Setting.fai_vcjoiner_Label, font=("Roboto", 12)).place(x=140,y=174)

      modules_frame01_04 = ctk.CTkFrame(module_frame, width=470, height=200, border_width=0, fg_color=c1)
      modules_frame01_04.grid(row=1, column=1, padx=6, pady=6)
      tk.Label(modules_frame01_04, bg=c1, fg="#fff", text="VC Leaver", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame01_04, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkButton(modules_frame01_04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.vcleave_serverid.set("")).place(x=5,y=31)
      ctk.CTkEntry(modules_frame01_04, bg_color=c1, fg_color=c7, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcleave_serverid).place(x=85,y=31)
      tk.Label(modules_frame01_04, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=29)
      ctk.CTkButton(modules_frame01_04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.vcleave_channelid.set("")).place(x=5,y=60)
      ctk.CTkEntry(modules_frame01_04, bg_color=c1, fg_color=c7, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcleave_channelid).place(x=85,y=60)
      tk.Label(modules_frame01_04, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=58)

      CTkLabel(modules_frame01_04, text_color="#fff", text="Delay Time (s)", font=("Roboto", 15)).place(x=5,y=82)
      def show_value01_04(value):
          tooltip01_04.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame01_04, from_=0.1, to=3.0, variable=Setting.delay01_04, command=show_value01_04)
      test.place(x=5,y=107)
      tooltip01_04 = CTkToolTip(test, message=round(Setting.delay01_04.get(), 1))

      ctk.CTkButton(modules_frame01_04, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: print("a")).place(x=5,y=127)

      tk.Label(modules_frame01_04, bg=c1, fg="#fff", text="VC Leaver Status", font=("Roboto", 12)).place(x=135,y=124)
      tk.Label(modules_frame01_04, bg=c1, fg="#fff", textvariable=Setting.suc_vcleaver_Label, font=("Roboto", 12)).place(x=140,y=149)
      tk.Label(modules_frame01_04, bg=c1, fg="#fff", textvariable=Setting.fai_vcleaver_Label, font=("Roboto", 12)).place(x=140,y=174)
  
      printl("debug", "Open Join Leave Tab")
        
    if num2 == 2:
      modules_frame02_01 = ctk.CTkFrame(module_frame, width=470, height=300, border_width=0, fg_color=c1)
      modules_frame02_01.grid(row=0, column=0, padx=6, pady=6)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text="Spammer", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame02_01, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkCheckBox(modules_frame02_01, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allping ,text="All Ping").place(x=5,y=30)
      test = ctk.CTkLabel(modules_frame02_01, text_color="#fff", text="(?)")
      test.place(x=80,y=30)
      CTkToolTip(test, delay=0.5, message="Add a Mention to a random user to the message to be spammed") 
      ctk.CTkCheckBox(modules_frame02_01, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allch ,text="All Ch").place(x=5,y=52)
      test = ctk.CTkLabel(modules_frame02_01, text_color="#fff", text="(?)")
      test.place(x=70,y=52)
      CTkToolTip(test, delay=0.5, message="Randomly select channels to spam") 
      ctk.CTkCheckBox(modules_frame02_01, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_rdstring ,text="Random String").place(x=5,y=74)
      test = ctk.CTkLabel(modules_frame02_01, text_color="#fff", text="(?)")
      test.place(x=120,y=74)
      CTkToolTip(test, delay=0.5, message="Adds a random string to the message to be spammed") 
      ctk.CTkCheckBox(modules_frame02_01, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_ratefixer ,text="RateLimitFixer").place(x=5,y=96)
      test = ctk.CTkLabel(modules_frame02_01, text_color="#fff", text="(?)")
      test.place(x=120,y=96)
      CTkToolTip(test, delay=0.5, message="Wait a few seconds if the rate limit is reached") 
      ctk.CTkCheckBox(modules_frame02_01, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_randomconvert ,text="RandomConvert").place(x=5,y=118)
      test = ctk.CTkLabel(modules_frame02_01, text_color="#fff", text="(?)")
      test.place(x=125,y=118)
      CTkToolTip(test, delay=0.5, message="Randomly converts messages to spam") 
      
      ctk.CTkButton(modules_frame02_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.spam_serverid.set("")).place(x=5,y=146)
      ctk.CTkEntry(modules_frame02_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.spam_serverid).place(x=85,y=146)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=144)
      ctk.CTkButton(modules_frame02_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.spam_channelid.set("")).place(x=5,y=175)
      ctk.CTkEntry(modules_frame02_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.spam_channelid).place(x=85,y=175)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=173)

      CTkLabel(modules_frame02_01, text_color="#fff", text="Delay Time (s)", font=("Roboto", 15)).place(x=5,y=197)
      def show_value02_01(value):
          tooltip02_01.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame02_01, from_=0.1, to=3.0, variable=Setting.delay02_01, command=show_value02_01)
      test.place(x=5,y=222)
      tooltip02_01 = CTkToolTip(test, message=round(Setting.delay02_01.get(), 1))

      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text="Message", font=("Roboto", 12)).place(x=150,y=30)
      spam_message = ctk.CTkTextbox(modules_frame02_01, bg_color=c1, fg_color=c4, text_color="#fff", width=250, height=75)
      spam_message.place(x=150,y=55)
        
      ctk.CTkButton(modules_frame02_01, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: print("a")).place(x=5,y=245)
      ctk.CTkButton(modules_frame02_01, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: print("a")).place(x=70,y=245)

      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=330,y=144)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", textvariable=Setting.suc_nmspam_Label, font=("Roboto", 12)).place(x=335,y=169)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", textvariable=Setting.fai_nmspam_Label, font=("Roboto", 12)).place(x=335,y=194)

      modules_frame02_02 = ctk.CTkFrame(module_frame, width=470, height=300, border_width=0, fg_color=c1)
      modules_frame02_02.grid(row=0, column=1, padx=6, pady=6)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Reply Spammer", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame02_02, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkCheckBox(modules_frame02_02, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allping ,text="All Ping").place(x=5,y=30)
      test = ctk.CTkLabel(modules_frame02_02, text_color="#fff", text="(?)")
      test.place(x=80,y=30)
      CTkToolTip(test, delay=0.5, message="Add a Mention to a random user to the message to be spammed") 
      ctk.CTkCheckBox(modules_frame02_02, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allch ,text="All Mg").place(x=5,y=52)
      test = ctk.CTkLabel(modules_frame02_02, text_color="#fff", text="(?)")
      test.place(x=70,y=52)
      CTkToolTip(test, delay=0.5, message="Randomly select messages to spam") 
      ctk.CTkCheckBox(modules_frame02_02, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_rdstring ,text="Random String").place(x=5,y=74)
      test = ctk.CTkLabel(modules_frame02_02, text_color="#fff", text="(?)")
      test.place(x=120,y=74)
      CTkToolTip(test, delay=0.5, message="Adds a random string to the message to be spammed") 
      ctk.CTkCheckBox(modules_frame02_02, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_ratefixer ,text="RateLimitFixer").place(x=5,y=96)
      test = ctk.CTkLabel(modules_frame02_02, text_color="#fff", text="(?)")
      test.place(x=120,y=96)
      CTkToolTip(test, delay=0.5, message="Wait a few seconds if the rate limit is reached") 
      ctk.CTkCheckBox(modules_frame02_02, bg_color=c1, text_color="#fff", border_color=c4, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_randomconvert ,text="RandomConvert").place(x=5,y=118)
      test = ctk.CTkLabel(modules_frame02_02, text_color="#fff", text="(?)")
      test.place(x=125,y=118)
      CTkToolTip(test, delay=0.5, message="Randomly converts messages to spam") 
      
      ctk.CTkButton(modules_frame02_02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.reply_serverid.set("")).place(x=5,y=146)
      ctk.CTkEntry(modules_frame02_02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reply_serverid).place(x=85,y=146)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=144)
      ctk.CTkButton(modules_frame02_02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.reply_channelid.set("")).place(x=5,y=175)
      ctk.CTkEntry(modules_frame02_02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reply_channelid).place(x=85,y=175)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=173)
      ctk.CTkButton(modules_frame02_02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.reply_messageid.set("")).place(x=5,y=204)
      ctk.CTkEntry(modules_frame02_02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reply_messageid).place(x=85,y=204)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Message ID", font=("Roboto", 12)).place(x=240,y=202)

      CTkLabel(modules_frame02_02, text_color="#fff", text="Delay Time (s)", font=("Roboto", 15)).place(x=5,y=227)
      def show_value02_01(value):
          tooltip02_01.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame02_02, from_=0.1, to=3.0, variable=Setting.delay02_01, command=show_value02_01)
      test.place(x=5,y=252)
      tooltip02_01 = CTkToolTip(test, message=round(Setting.delay02_01.get(), 1))

      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Message", font=("Roboto", 12)).place(x=150,y=30)
      spam_message = ctk.CTkTextbox(modules_frame02_02, bg_color=c1, fg_color=c4, text_color="#fff", width=250, height=75)
      spam_message.place(x=150,y=55)
        
      ctk.CTkButton(modules_frame02_02, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: print("i")).place(x=5,y=275)
      ctk.CTkButton(modules_frame02_02, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: print("i")).place(x=70,y=275)

      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=330,y=144)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", textvariable=Setting.suc_replyspam_Label, font=("Roboto", 12)).place(x=335,y=169)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", textvariable=Setting.fai_replyspam_Label, font=("Roboto", 12)).place(x=335,y=194)

      printl("debug", "Open Spammer Tab")
        
  if num1 == 2:
    if num2 == 1:
      modules_frame10_01 = ctk.CTkFrame(module_frame, width=470, height=210, border_width=0, fg_color=c1)
      modules_frame10_01.grid(row=0, column=0, padx=6, pady=6)
      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="Tokens", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame10_01, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkButton(modules_frame10_01, text="Select File", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: token_load()).place(x=5,y=33)
      ctk.CTkEntry(modules_frame10_01, bg_color=c1, fg_color=c7, border_color=c4, text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=33)
      ctk.CTkLabel(modules_frame10_01, bg_color=c1, fg_color=c4, text_color="#fff", text="", width=150, height=20, textvariable=Setting.token_filenameLabel).place(x=85,y=33)
      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=31)

      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=70)
      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="Total: 000", font=("Roboto", 12), textvariable=Setting.totaltokenLabel).place(x=10,y=95)
      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="Valid: 000", font=("Roboto", 12), textvariable=Setting.validtokenLabel).place(x=10,y=115)
      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="Invalid: 000", font=("Roboto", 12), textvariable=Setting.invalidtokenLabel).place(x=10,y=135)
      
      modules_frame10_02 = ctk.CTkFrame(module_frame, width=470, height=210, border_width=0, fg_color=c1)
      modules_frame10_02.grid(row=0, column=1, padx=6, pady=6)
      tk.Label(modules_frame10_02, bg=c1, fg="#fff", text="Proxies", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame10_02, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkCheckBox(modules_frame10_02, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.proxy_enabled ,text="Enabled").place(x=5,y=31)
      def set_socket(socks):
        Setting.proxytype.set(socks)
      ctk.CTkOptionMenu(modules_frame10_02, values=["http", "https", "socks4", "socks5"], fg_color=c7, button_color=c5, button_hover_color=c4, command=set_socket, variable=Setting.proxytype).place(x=5,y=57)
      tk.Label(modules_frame10_02, bg=c1, fg="#fff", text="Socket Type", font=("Roboto", 12)).place(x=150,y=55)
      ctk.CTkButton(modules_frame10_02, text="Select File", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: proxy_load()).place(x=5,y=90)
      ctk.CTkEntry(modules_frame10_02, bg_color=c1, fg_color=c7, border_color=c4, text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=90)
      ctk.CTkLabel(modules_frame10_02, bg_color=c1, fg_color=c4, text_color="#fff", text="", width=150, height=20, textvariable=Setting.proxy_filenameLabel).place(x=85,y=90)
      tk.Label(modules_frame10_02, bg=c1, fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=87)
    
      tk.Label(modules_frame10_02, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=120)
      tk.Label(modules_frame10_02, bg=c1, fg="#fff", text="Total: 000", font=("Roboto", 12), textvariable=Setting.totalProxiesLabel).place(x=10,y=145)
      tk.Label(modules_frame10_02, bg=c1, fg="#fff", text="Valid: 000", font=("Roboto", 12), textvariable=Setting.validProxiesLabel).place(x=10,y=165)
      tk.Label(modules_frame10_02, bg=c1, fg="#fff", text="Invalid: 000", font=("Roboto", 12), textvariable=Setting.invalidProxiesLabel).place(x=10,y=185)
   
      modules_frame10_03 = ctk.CTkFrame(module_frame, width=470, height=200, border_width=0, fg_color=c1)
      modules_frame10_03.grid(row=1, column=0, padx=6, pady=6)
      tk.Label(modules_frame10_03, bg=c1, fg="#fff", text="Settings", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame10_03, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      
      CTkLabel(modules_frame10_03, text_color="#fff", text="Default Delay Time (s)", font=("Roboto", 15)).place(x=5,y=30)
      def show_value01_05(value):
          tooltip01_05.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame10_03, from_=0.1, to=3.0, variable=Setting.delay99_01, command=show_value01_05)
      test.place(x=5,y=55)
      tooltip01_05 = CTkToolTip(test, message=round(Setting.delay99_01.get(), 1))
      
      CTkLabel(modules_frame10_03, text_color="#fff", text="Default Mention Count (m)", font=("Roboto", 15)).place(x=5,y=79)
      def show_value01_06(value):
          tooltip01_06.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame10_03, from_=0.1, to=3.0, variable=Setting.delay99_02, command=show_value01_06)
      test.place(x=5,y=104)
      tooltip01_06 = CTkToolTip(test, message=round(Setting.delay99_02.get(), 1))
      
      ctk.CTkButton(modules_frame10_03, text="Get Info     ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: get_info()).place(x=5,y=126)
      invite_url = ctk.CTkEntry(modules_frame10_03, bg_color=c1, fg_color=c7, border_color=c4, text_color="#fff", width=150, height=20)
      invite_url.place(x=85,y=126)
      tk.Label(modules_frame10_03, bg=c1, fg="#fff", text="Defalut Sv ID", font=("Roboto", 12)).place(x=240,y=124)

      modules_frame10_04 = ctk.CTkFrame(module_frame, width=470, height=200, border_width=0, fg_color=c1)
      modules_frame10_04.grid(row=1, column=1, padx=6, pady=6)
      tk.Label(modules_frame10_04, bg=c1, fg="#fff", text="Custom Theme", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame10_04, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      tk.Label(modules_frame10_04, bg=c1, fg="#fff", text="Theme Select", font=("Roboto", 12)).place(x=5,y=30)
      def combobox_callback(choice):
        global theme
        printl("info", "Select Theme " + choice)
        if choice == "Default Theme":
          theme = "twocoin"
          update_theme(num1, num2)
        if choice == "Akebi Theme":
          theme = "akebi"
          update_theme(num1, num2)
        with open('config.json') as f:
          data = json.load(f)
        data.update({"select_theme": theme})
        with open('config.json', 'w') as f:
          json.dump(data, f)
  
      ctk.CTkOptionMenu(master=modules_frame10_04, values=["Default Theme", "Akebi Theme"], fg_color=c7, button_color=c5, button_hover_color=c4, text_color="#fff", command=combobox_callback, variable=Setting.theme_var).place(x=5, y=55)

      printl("debug", "Open Setting Tab")
        
    if num2 == 2:
      printl("debug", "Open Debug Tab")

def module_list_frame():
  global modulelist
  tk.Label(root, bg=c2, width=1024, height=720).place(x=0,y=0)
  tk.Label(root, bg=c4, width=32, height=720).place(x=0,y=0)
  tk.Label(root, bg=c4, text="TWOCOIN RAIDER", fg="#fff", font=("Carlito", 20, "bold")).place(x=13,y=25)
  
  modulelist = ctk.CTkFrame(master=root, width=230, height=720, corner_radius=0, fg_color=c4)
  modulelist.place(x=0,y=100)
  tk.Canvas(bg=c6, highlightthickness=0, height=2080, width=4).place(x=230, y=0)
  ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Joiner / Leaver", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w", command= lambda: module_scroll_frame(1, 1)).place(x=20,y=12)
  ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Spammer", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w", command= lambda: module_scroll_frame(1, 2)).place(x=20,y=57)
  ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=102)
  ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=148)
  ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=194)
  ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=240)
  ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/setting.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Settings", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w", command= lambda: module_scroll_frame(2, 1)).place(x=20,y=286)
  ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/info.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Debug", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w", command= lambda: module_scroll_frame(2, 2)).place(x=20,y=332)
  
  credit_frame = ctk.CTkFrame(root, width=1020, height=50, fg_color=c1, bg_color=c2)
  credit_frame.place(x=245, y=10)
  ctk.CTkButton(master=credit_frame, image=ctk.CTkImage(Image.open("data/link.png"),size=(20, 20)), compound="right", fg_color=c1, text_color="#fff", corner_radius=0, text="", width=20, height=20, font=("Roboto", 16, "bold"), anchor="w", command= lambda: CTkMessagebox(title="Version Info", message=f"Version: {version}\n\nDeveloper: NyaShinn1204\nTester: Mino3753", width=450)).place(x=10,y=10)
  ctk.CTkLabel(master=credit_frame, fg_color=c1, text_color="#fff", corner_radius=0, text="Username: "+os.getlogin(), width=20, height=20, font=("Roboto", 16, "bold"), anchor="w").place(x=40,y=5)
  ctk.CTkLabel(master=credit_frame, fg_color=c1, text_color="#fff", corner_radius=0, text="Hwid: "+get_hwid(), width=20, height=20, font=("Roboto", 16, "bold"), anchor="w").place(x=40,y=25)

# Load Menu
config_check()
setup_frame(2, 1)
printl("debug", "Loading Tkinter")

# Load About Tab
module_scroll_frame(2, 1)

root.mainloop()