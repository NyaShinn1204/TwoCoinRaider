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
  tokens = []
  voicefile = []
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
  
  voicefile_filenameLabel = tk.StringVar()
  voicefile_filenameLabel.set("")
  
  # joiner
  suc_joiner_Label = tk.StringVar()
  suc_joiner_Label.set("Success: 000")
  fai_joiner_Label = tk.StringVar()
  fai_joiner_Label.set("Failed: 000")
  
  # leaver
  suc_leaver_Label = tk.StringVar()
  suc_leaver_Label.set("Success: 000")
  fai_leaver_Label = tk.StringVar()
  fai_leaver_Label.set("Failed: 000")
  
  # vc joiner
  suc_vcjoiner_Label = tk.StringVar()
  suc_vcjoiner_Label.set("Success: 000")
  fai_vcjoiner_Label = tk.StringVar()
  fai_vcjoiner_Label.set("Failed: 000")

  # vc leaver
  suc_vcleaver_Label = tk.StringVar()
  suc_vcleaver_Label.set("Success: 000")
  fai_vcleaver_Label = tk.StringVar()
  fai_vcleaver_Label.set("Failed: 000")  

  # nm spam
  suc_nmspam_Label = tk.StringVar()
  suc_nmspam_Label.set("Success: 000")
  fai_nmspam_Label = tk.StringVar()
  fai_nmspam_Label.set("Failed: 000")
  
  # reply spam
  suc_replyspam_Label = tk.StringVar()
  suc_replyspam_Label.set("Success: 000")
  fai_replyspam_Label = tk.StringVar()
  fai_replyspam_Label.set("Failed: 000")
  
  # ticket spam
  suc_ticketspam_Label = tk.StringVar()
  suc_ticketspam_Label.set("Success: 000")
  fai_ticketspam_Label = tk.StringVar()
  fai_ticketspam_Label.set("Failed: 000")
  
  # vc spam
  suc_vcspam_Label = tk.StringVar()
  suc_vcspam_Label.set("Success: 000")
  fai_vcspam_Label = tk.StringVar()
  fai_vcspam_Label.set("Failed: 000")
  
  # slash spam
  suc_shspam_Label = tk.StringVar()
  suc_shspam_Label.set("Success: 000")
  fai_shspam_Label = tk.StringVar()
  fai_shspam_Label.set("Failed: 000")
  
  # reaction spam
  suc_reactionspam_Label = tk.StringVar()
  suc_reactionspam_Label.set("Success: 000")
  fai_reactionspam_Label = tk.StringVar()
  fai_reactionspam_Label.set("Failed: 000")
  
  # token onliner
  suc_tokenonliner_Label = tk.StringVar()
  suc_tokenonliner_Label.set("Success: 000")
  fai_tokenonliner_Label = tk.StringVar()
  fai_tokenonliner_Label.set("Failed: 000")
  
  spam_allping = tk.BooleanVar()
  spam_allping.set(False)
  spam_allch = tk.BooleanVar()
  spam_allch.set(False)
  spam_rdstring = tk.BooleanVar()
  spam_rdstring.set(False)
  spam_ratefixer = tk.BooleanVar()
  spam_ratefixer.set(False)
  spam_randomconvert = tk.BooleanVar()
  spam_randomconvert.set(False)

  reply_allping = tk.BooleanVar()
  reply_allping.set(False)
  reply_allmg = tk.BooleanVar()
  reply_allmg.set(False)
  reply_rdstring = tk.BooleanVar()
  reply_rdstring.set(False)
  reply_ratefixer = tk.BooleanVar()
  reply_ratefixer.set(False)
  
  ticket_ratefixer = tk.BooleanVar()
  ticket_ratefixer.set(False) 
  
  slash_ratefixer = tk.BooleanVar()
  slash_ratefixer.set(False) 
  
  sbspam_rdsounds = tk.BooleanVar()
  sbspam_rdsounds.set(False)
  
  delay01_01 = tk.DoubleVar()
  delay01_01.set(0.1)
  
  delay01_02 = tk.DoubleVar()
  delay01_02.set(0.1)
  
  delay01_03 = tk.DoubleVar()
  delay01_03.set(0.1)

  delay01_04 = tk.DoubleVar()
  delay01_04.set(0.1)
  
  mention_count_def = tk.DoubleVar()
  mention_count_def.set(20)
  
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
  leaver_serverid = tk.StringVar()
  leaver_serverid.set("")
  vcjoin_channelid = tk.StringVar()
  vcjoin_channelid.set("")
  vcjoin_serverid = tk.StringVar()
  vcjoin_serverid.set("")
  vcleave_channelid = tk.StringVar()
  vcleave_channelid.set("")
  vcleave_serverid = tk.StringVar()
  vcleave_serverid.set("")
  spam_serverid = tk.StringVar()
  spam_serverid.set("")
  spam_channelid = tk.StringVar()
  spam_channelid.set("")
  reply_serverid = tk.StringVar()
  reply_serverid.set("")
  reply_channelid = tk.StringVar()
  reply_channelid.set("")
  reply_messageid = tk.StringVar()
  reply_messageid.set("")
  vcspam_serverid = tk.StringVar()
  vcspam_serverid.set("")
  vcspam_channelid = tk.StringVar()
  vcspam_channelid.set("")
  sbspam_serverid = tk.StringVar()
  sbspam_serverid.set("")
  sbspam_channelid = tk.StringVar()
  sbspam_channelid.set("")
  ticket_serverid = tk.StringVar()
  ticket_serverid.set("")
  ticket_channelid = tk.StringVar()
  ticket_channelid.set("")
  ticket_messageid = tk.StringVar()
  ticket_messageid.set("")
  slash_serverid = tk.StringVar()
  slash_serverid.set("")
  slash_channelid = tk.StringVar()
  slash_channelid.set("")
  slash_applicationid = tk.StringVar()
  slash_applicationid.set("")
  slash_commandname = tk.StringVar()
  slash_commandname.set("")
  slash_subcommandname = tk.StringVar()
  slash_subcommandname.set("")
  slash_subcommandname_value = tk.StringVar()
  slash_subcommandname_value.set("")
  reaction_channelid = tk.StringVar()
  reaction_channelid.set("")
  reaction_messageid = tk.StringVar()
  reaction_messageid.set("")
  reaction_emoji = tk.StringVar()
  reaction_emoji.set("")

class SettingVariable:
  joinerresult_success = 0
  joinerresult_failed = 0
  leaverresult_success = 0
  leaverresult_failed = 0
  nmspamresult_success = 0
  nmspamresult_failed = 0
  vcjoinerresult_success = 0
  vcjoinerresult_failed = 0
  vcleaverresult_success = 0
  vcleaverresult_failed = 0
  replyspamresult_success = 0
  replyspamresult_failed = 0
  ticketspamresult_success = 0
  ticketspamresult_failed = 0
  slashspamresult_success = 0
  slashspamresult_failed = 0
  vcspamresult_success = 0
  vcspamresult_failed = 0

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
            modules_frame01_02.grid(row=0, column=1, padx=3, pady=12)
            tk.Label(modules_frame01_02, bg=c1, fg="#fff", text="Leaver", font=("Roboto", 14)).place(x=15,y=0)
            tk.Canvas(modules_frame01_02, bg=c3, highlightthickness=0, height=4, width=470).place(x=0, y=25)
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
            modules_frame01_03.grid(row=1, column=0, padx=3, pady=12)
            tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="VC Joiner", font=("Roboto", 14)).place(x=15,y=0)
            tk.Canvas(modules_frame01_03, bg=c3, highlightthickness=0, height=4, width=470).place(x=0, y=25)
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
            modules_frame01_04.grid(row=1, column=1, padx=3, pady=12)
            tk.Label(modules_frame01_04, bg=c1, fg="#fff", text="VC Leaver", font=("Roboto", 14)).place(x=15,y=0)
            tk.Canvas(modules_frame01_04, bg=c3, highlightthickness=0, height=4, width=470).place(x=0, y=25)
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