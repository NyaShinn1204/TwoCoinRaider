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
if theme == "twocoin":
    c1 = "#28464B"
    c2 = "#213A3E"
    c3 = "#00484C"
    c4 = "#142326"
    c5 = "#2C8C99"

root = tk.Tk()
root.geometry("1280x720")
root.resizable(0, 0)
root.title("TwoCoinRaider | "+version)
root.iconbitmap(default="data/favicon.ico")
root.configure(bg=c2)

class Setting:
  voicefile = []
  tokens = []
  validtoken = 0
  invalidtoken = 0
  lockedtoken = 0
  
  # enabled ck.button
  proxy_enabled = tk.BooleanVar()
  proxy_enabled.set(False)
  
  token_filenameLabel = tk.StringVar()
  token_filenameLabel.set("")
  totaltokenLabel = tk.StringVar()
  totaltokenLabel.set("Total: 000")
  validtokenLabel = tk.StringVar()
  validtokenLabel.set("Valid: 000")
  invalidtokenLabel = tk.StringVar()
  invalidtokenLabel.set("Invalid: 000")
  lockedtokenLabel = tk.StringVar()
  lockedtokenLabel.set("Locked: 000")
  
  proxytype = tk.StringVar()
  proxytype.set("http")
  proxies = []
  totalproxies = 0
  vaildproxies = 0
  invaildproxies = 0

  proxysetting = tk.BooleanVar()
  proxysetting.set(False)

  proxy_filenameLabel = tk.StringVar()
  proxy_filenameLabel.set("")
  totalProxiesLabel = tk.StringVar()
  totalProxiesLabel.set("Total: 000")
  validProxiesLabel = tk.StringVar()
  validProxiesLabel.set("Valid: 000")
  invalidProxiesLabel = tk.StringVar()
  invalidProxiesLabel.set("Invalid: 000")
  
  # joiner
  suc_joiner_Label = tk.StringVar()
  suc_joiner_Label.set("Success: 000")
  fai_joiner_Label = tk.StringVar()
  fai_joiner_Label.set("Failed: 000")
    
  delay01_01 = tk.DoubleVar()
  delay01_01.set(0.1)

  joiner_link = tk.StringVar()
  joiner_link.set("")
  bypass_ms = tk.BooleanVar()
  bypass_ms.set(False)
  bypass_cap = tk.BooleanVar()
  bypass_cap.set(False)
  delete_join_ms = tk.BooleanVar()
  delete_join_ms.set("False")
  joiner_serverid = tk.StringVar()
  joiner_serverid.set("")
  joiner_channelid = tk.StringVar()
  joiner_channelid.set("")
  
class SettingVariable:
  joinerresult_success = 0
  joinerresult_failed = 0
  bms_joinerresult_success = 0
  bms_joinerresult_failed = 0
  bh_joinerresult_success = 0
  bh_joinerresult_failed = 0
  djm_joinerresult_success = 0
  djm_joinerresult_failed = 0

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
            modules_frame01_01.grid(row=0, column=0, padx=12, pady=12)
            tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Joiner", font=("Roboto", 14)).place(x=15,y=0)
            tk.Canvas(modules_frame01_01, bg=c3, highlightthickness=0, height=4, width=470).place(x=0, y=25)
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
            CTkLabel(modules_frame01_01, text_color="#fff", text="Delay Time (s)", font=("Roboto", 15)).place(x=5,y=100)
            def show_value01_01(value):
                tooltip.configure(message=round(value, 1))
            test = ctk.CTkSlider(modules_frame01_01, from_=0.1, to=3.0, variable=Setting.delay01_01, command=show_value01_01)
            test.place(x=5,y=125)
            tooltip = CTkToolTip(test, message="0.1")

            ctk.CTkButton(modules_frame01_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.joiner_link.set("")).place(x=5,y=144)
            ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_link).place(x=85,y=144)
            tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Invite Link", font=("Roboto", 12)).place(x=240,y=142)
            ctk.CTkButton(modules_frame01_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.joiner_serverid.set("")).place(x=5,y=173)
            ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_serverid).place(x=85,y=173)
            tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=171)
            ctk.CTkButton(modules_frame01_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: Setting.joiner_channelid.set("")).place(x=5,y=202)
            ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_channelid).place(x=85,y=202)
            tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=200)

            ctk.CTkButton(modules_frame01_01, text="Start", fg_color=c2, hover_color=c5, width=60, height=25, command=lambda: print("a")).place(x=5,y=230)
            ctk.CTkButton(modules_frame01_01, text="Stop", fg_color=c2, hover_color=c5, width=60, height=25, command=lambda: print("a")).place(x=70,y=230)

            tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Join Status", font=("Roboto", 12)).place(x=205,y=30)
            tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.suc_joiner_Label, font=("Roboto", 12)).place(x=210,y=58)
            tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.fai_joiner_Label, font=("Roboto", 12)).place(x=210,y=83)
            #tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Bypass MemberScreen Status", font=("Roboto", 12)).place(x=205,y=110)
            #tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.bms_suc_joiner_Label, font=("Roboto", 12)).place(x=210,y=138)
            #tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.bms_fai_joiner_Label, font=("Roboto", 12)).place(x=210,y=163)
            #tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Bypass hCaptcha Status", font=("Roboto", 12)).place(x=5,y=190)
            #tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.bh_suc_joiner_Label, font=("Roboto", 12)).place(x=5,y=218)
            #tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.bh_fai_joiner_Label, font=("Roboto", 12)).place(x=5,y=243)
            #tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Delete Join Meassge Status", font=("Roboto", 12)).place(x=205,y=190)
            #tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.djm_suc_joiner_Label, font=("Roboto", 12)).place(x=210,y=218)
            #tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.djm_fai_joiner_Label, font=("Roboto", 12)).place(x=210,y=243)

            modules_frame01_02 = ctk.CTkFrame(module_frame, width=470, height=300, border_width=0, fg_color=c1)
            modules_frame01_02.grid(row=0, column=1, padx=3, pady=12)
    
            printl("debug", "Open Join Leave Tab")
            
        if num2 == 2:
            printl("debug", "Open Spammer Tab")
            
    if num1 == 2:
        if num2 == 1:
            printl("debug", "Open Setting Tab")
            
        if num2 == 2:
            printl("debug", "Open Debug Tab")

tk.Label(root, bg=c4, width=32, height=720).place(x=0,y=0)
tk.Label(root, bg=c4, text="TWOCOIN RAIDER", fg="#fff", font=("Carlito", 20, "bold")).place(x=13,y=25)

modulelist = ctk.CTkFrame(master=root, width=230, height=720, corner_radius=0, fg_color=c4)
modulelist.place(x=0,y=100)
tk.Canvas(bg=c3, highlightthickness=0, height=2080, width=4).place(x=230, y=10)
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