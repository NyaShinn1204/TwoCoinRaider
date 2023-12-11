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
  os.system('pip install -r ./data/requirements.txt')
import requests
import colorama
import tkinter as tk
import customtkinter as ctk
from PIL import Image
from colorama import Fore
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from CTkToolTip import *

colorama.init(autoreset=True)

version = "v1.0.3β"
theme = "twocoin"

if theme == "akebi":
    c1 = "#040f24"
    c2 = "#020b1f"
    c3 = "#0a2b63"
    c4 = "#020b1f"
    c5 = "#00bbe3"
    c6 = "#0a2b63"
if theme == "twocoin":
    c1 = "#28464B"
    c2 = "#213A3E"
    c3 = "#00484C"
    c4 = "#142326"
    c5 = "#2C8C99"
    c6 = "#002D2D"

root = tk.Tk()
root.geometry("1280x720")
root.resizable(0, 0)
root.title("TwoCoinRaider | "+version)
root.iconbitmap(default="data/favicon.ico")
root.configure(bg=c2)

import setting as config

Setting = config.Setting
SettingVariable = config.SettingVariable

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

def get_filename():
  return os.path.basename(__file__)

def printl(num, data):
  if num == "error":
    print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [{get_filename()}] " + data)
  if num == "debug":
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [{get_filename()}] " + data)
  if num == "info":
    print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [{get_filename()}] " + data)

def clear_frame(frame):
  for widget in frame.winfo_children():
    widget.destroy()
  frame.pack_forget()

def set_moduleframe_scroll(num1, num2):
  frame_scroll = module_frame = ctk.CTkScrollableFrame(root, fg_color=c2, width=1000, height=630)
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
      ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_link).place(x=85,y=109)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Invite Link", font=("Roboto", 12)).place(x=240,y=107)
      ctk.CTkButton(modules_frame01_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.joiner_serverid.set("")).place(x=5,y=138)
      ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_serverid).place(x=85,y=138)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=136)
      ctk.CTkButton(modules_frame01_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.joiner_channelid.set("")).place(x=5,y=167)
      ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_channelid).place(x=85,y=167)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=165)

      CTkLabel(modules_frame01_01, text_color="#fff", text="Delay Time (s)", font=("Roboto", 15)).place(x=5,y=187)
      def show_value01_01(value):
          tooltip01_01.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame01_01, from_=0.1, to=3.0, variable=Setting.delay01_01, command=show_value01_01)
      test.place(x=5,y=212)
      tooltip01_01 = CTkToolTip(test, message="0.1")

      ctk.CTkButton(modules_frame01_01, text="Start", fg_color=c2, hover_color=c5, width=60, height=25, command=lambda: print("a")).place(x=5,y=232)
      ctk.CTkButton(modules_frame01_01, text="Stop", fg_color=c2, hover_color=c5, width=60, height=25, command=lambda: print("a")).place(x=70,y=232)

      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Join Status", font=("Roboto", 12)).place(x=205,y=30)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.suc_joiner_Label, font=("Roboto", 12)).place(x=210,y=58)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.fai_joiner_Label, font=("Roboto", 12)).place(x=210,y=83)

      modules_frame01_02 = ctk.CTkFrame(module_frame, width=470, height=300, border_width=0, fg_color=c1)
      modules_frame01_02.grid(row=0, column=1, padx=6, pady=6)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", text="Leaver", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame01_02, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkButton(modules_frame01_02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.leaver_serverid.set("")).place(x=5,y=33)
      ctk.CTkEntry(modules_frame01_02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.leaver_serverid).place(x=85,y=33)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=31)

      CTkLabel(modules_frame01_02, text_color="#fff", text="Delay Time (s)", font=("Roboto", 15)).place(x=5,y=55)
      def show_value01_02(value):
          tooltip01_02.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame01_02, from_=0.1, to=3.0, variable=Setting.delay01_02, command=show_value01_02)
      test.place(x=5,y=80)
      tooltip01_02 = CTkToolTip(test, message="0.1")

      ctk.CTkButton(modules_frame01_02, text="Start", fg_color=c2, hover_color=c5, width=60, height=25, command=lambda: print("a")).place(x=5,y=100)
      ctk.CTkButton(modules_frame01_02, text="Stop", fg_color=c2, hover_color=c5, width=60, height=25, command=lambda: print("a")).place(x=70,y=100)
      
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", text="Leaver Status", font=("Roboto", 12)).place(x=5,y=130)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", textvariable=Setting.suc_leaver_Label, font=("Roboto", 12)).place(x=10,y=155)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", textvariable=Setting.fai_leaver_Label, font=("Roboto", 12)).place(x=10,y=175)

      modules_frame01_03 = ctk.CTkFrame(module_frame, width=470, height=200, border_width=0, fg_color=c1)
      modules_frame01_03.grid(row=1, column=0, padx=6, pady=6)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="VC Joiner", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame01_03, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkButton(modules_frame01_03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.vcjoin_serverid.set("")).place(x=5,y=28)
      ctk.CTkEntry(modules_frame01_03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcjoin_serverid).place(x=85,y=28)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=26)
      ctk.CTkButton(modules_frame01_03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.vcjoin_channelid.set("")).place(x=5,y=57)
      ctk.CTkEntry(modules_frame01_03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcjoin_channelid).place(x=85,y=57)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=55)

      CTkLabel(modules_frame01_03, text_color="#fff", text="Delay Time (s)", font=("Roboto", 15)).place(x=5,y=79)
      def show_value01_03(value):
          tooltip01_03.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame01_03, from_=0.1, to=3.0, variable=Setting.delay01_03, command=show_value01_03)
      test.place(x=5,y=104)
      tooltip01_03 = CTkToolTip(test, message="0.1")

      ctk.CTkButton(modules_frame01_03, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: print("a")).place(x=5,y=124)

      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="VC Joiner Status", font=("Roboto", 12)).place(x=135,y=121)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", textvariable=Setting.suc_vcjoiner_Label, font=("Roboto", 12)).place(x=140,y=146)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", textvariable=Setting.fai_vcjoiner_Label, font=("Roboto", 12)).place(x=140,y=171)

      modules_frame01_04 = ctk.CTkFrame(module_frame, width=470, height=200, border_width=0, fg_color=c1)
      modules_frame01_04.grid(row=1, column=1, padx=6, pady=6)
      tk.Label(modules_frame01_04, bg=c1, fg="#fff", text="VC Leaver", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame01_04, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkButton(modules_frame01_04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.vcleave_serverid.set("")).place(x=5,y=28)
      ctk.CTkEntry(modules_frame01_04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcleave_serverid).place(x=85,y=28)
      tk.Label(modules_frame01_04, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=26)
      ctk.CTkButton(modules_frame01_04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.vcleave_channelid.set("")).place(x=5,y=57)
      ctk.CTkEntry(modules_frame01_04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcleave_channelid).place(x=85,y=57)
      tk.Label(modules_frame01_04, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=55)

      CTkLabel(modules_frame01_04, text_color="#fff", text="Delay Time (s)", font=("Roboto", 15)).place(x=5,y=79)
      def show_value01_04(value):
          tooltip01_04.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame01_04, from_=0.1, to=3.0, variable=Setting.delay01_04, command=show_value01_04)
      test.place(x=5,y=104)
      tooltip01_04 = CTkToolTip(test, message="0.1")

      ctk.CTkButton(modules_frame01_04, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: print("a")).place(x=5,y=124)

      tk.Label(modules_frame01_04, bg=c1, fg="#fff", text="VC Leaver Status", font=("Roboto", 12)).place(x=135,y=121)
      tk.Label(modules_frame01_04, bg=c1, fg="#fff", textvariable=Setting.suc_vcleaver_Label, font=("Roboto", 12)).place(x=140,y=145)
      tk.Label(modules_frame01_04, bg=c1, fg="#fff", textvariable=Setting.fai_vcleaver_Label, font=("Roboto", 12)).place(x=140,y=171)
  
      printl("debug", "Open Join Leave Tab")
        
    if num2 == 2:
      printl("debug", "Open Spammer Tab")
        
  if num1 == 2:
    if num2 == 1:
      modules_frame10_01 = ctk.CTkFrame(module_frame, width=470, height=210, border_width=0, fg_color=c1)
      modules_frame10_01.grid(row=0, column=0, padx=6, pady=6)
      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="Tokens", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame10_01, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkButton(modules_frame10_01, text="Select File", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: print()).place(x=5,y=33)
      ctk.CTkEntry(modules_frame10_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=33)
      ctk.CTkLabel(modules_frame10_01, bg_color=c1, fg_color=c4, text_color="#fff", text="", width=150, height=20, textvariable=Setting.token_filenameLabel).place(x=85,y=33)
      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=31)

      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=70)
      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="Total: 000", font=("Roboto", 12), textvariable=Setting.totaltokenLabel).place(x=10,y=95)
      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="Valid: 000", font=("Roboto", 12), textvariable=Setting.validtokenLabel).place(x=10,y=115)
      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="Invalid: 000", font=("Roboto", 12), textvariable=Setting.invalidtokenLabel).place(x=10,y=135)
      tk.Label(modules_frame10_01, bg=c1, fg="#fff", text="Lock: 000", font=("Roboto", 12), textvariable=Setting.lockedtokenLabel).place(x=110,y=135)
      
      modules_frame10_02 = ctk.CTkFrame(module_frame, width=470, height=210, border_width=0, fg_color=c1)
      modules_frame10_02.grid(row=0, column=1, padx=6, pady=6)
      tk.Label(modules_frame10_02, bg=c1, fg="#fff", text="Proxies", font=("Roboto", 14)).place(x=15,y=0)
      tk.Canvas(modules_frame10_02, bg=c6, highlightthickness=0, height=4, width=470).place(x=0, y=25)
      ctk.CTkCheckBox(modules_frame10_02, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.proxy_enabled ,text="Enabled").place(x=5,y=31)
      def set_socket(socks):
        Setting.proxytype.set(socks)
      ctk.CTkOptionMenu(modules_frame10_02, values=["http", "https", "socks4", "socks5"], fg_color=c2, button_color=c5, button_hover_color=c4, command=set_socket, variable=Setting.proxytype).place(x=5,y=57)
      tk.Label(modules_frame10_02, bg=c1, fg="#fff", text="Socket Type", font=("Roboto", 12)).place(x=150,y=55)
      ctk.CTkButton(modules_frame10_02, text="Select File", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: print()).place(x=5,y=90)
      ctk.CTkEntry(modules_frame10_02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=90)
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
      test = ctk.CTkSlider(modules_frame10_03, from_=0.1, to=3.0, variable=Setting.delay01_03, command=show_value01_05)
      test.place(x=5,y=55)
      tooltip01_05 = CTkToolTip(test, message="0.1")
      
      CTkLabel(modules_frame10_03, text_color="#fff", text="Default Mention Count (m)", font=("Roboto", 15)).place(x=5,y=79)
      def show_value01_06(value):
          tooltip01_06.configure(message=round(value, 1))
      test = ctk.CTkSlider(modules_frame10_03, from_=0.1, to=3.0, variable=Setting.delay01_03, command=show_value01_06)
      test.place(x=5,y=104)
      tooltip01_06 = CTkToolTip(test, message="0.1")
      
      ctk.CTkButton(modules_frame10_03, text="Get Info     ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: print()).place(x=5,y=126)
      invite_url = ctk.CTkEntry(modules_frame10_03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20)
      invite_url.place(x=85,y=126)
      tk.Label(modules_frame10_03, bg=c1, fg="#fff", text="Defalut Sv ID", font=("Roboto", 12)).place(x=240,y=124)

      printl("debug", "Open Setting Tab")
        
    if num2 == 2:
      printl("debug", "Open Debug Tab")

tk.Label(root, bg=c4, width=32, height=720).place(x=0,y=0)
tk.Label(root, bg=c4, text="TWOCOIN RAIDER", fg="#fff", font=("Carlito", 20, "bold")).place(x=13,y=25)

modulelist = ctk.CTkFrame(master=root, width=230, height=720, corner_radius=0, fg_color=c4)
modulelist.place(x=0,y=100)
tk.Canvas(bg=c6, highlightthickness=0, height=2080, width=4).place(x=230, y=0)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Joiner / Leaver", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w", command= lambda: set_moduleframe_scroll(1, 1)).place(x=20,y=12)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Spammer", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w", command= lambda: set_moduleframe_scroll(1, 2)).place(x=20,y=57)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=102)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=148)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=194)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=240)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/setting.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Settings", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w", command= lambda: set_moduleframe_scroll(2, 1)).place(x=20,y=286)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/info.png"),size=(20, 20)), compound="left", fg_color=c4, hover_color=c5, corner_radius=0, text="Debug", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w", command= lambda: set_moduleframe_scroll(2, 2)).place(x=20,y=332)

credit_frame = ctk.CTkFrame(root, width=1020, height=50, fg_color=c1)
credit_frame.place(x=245, y=10)
ctk.CTkButton(master=credit_frame, image=ctk.CTkImage(Image.open("data/link.png"),size=(20, 20)), compound="right", fg_color=c1, text_color="#fff", corner_radius=0, text="", width=20, height=20, font=("Roboto", 16, "bold"), anchor="w", command= lambda: CTkMessagebox(title="Version Info", message=f"Version: {version}\n\nDeveloper: NyaShinn1204\nTester: Mino3753", width=450)).place(x=10,y=10)
ctk.CTkLabel(master=credit_frame, fg_color=c1, text_color="#fff", corner_radius=0, text="Username: "+os.getlogin(), width=20, height=20, font=("Roboto", 16, "bold"), anchor="w").place(x=40,y=5)
ctk.CTkLabel(master=credit_frame, fg_color=c1, text_color="#fff", corner_radius=0, text="Hwid: "+get_hwid(), width=20, height=20, font=("Roboto", 16, "bold"), anchor="w").place(x=40,y=25)

root.mainloop()