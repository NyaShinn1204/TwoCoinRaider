import colorama
import subprocess
import tkinter as tk
import customtkinter as ctk
from customtkinter import *
from PIL import Image
from colorama import Fore, Back, Style
from CTkMessagebox import CTkMessagebox
import webbrowser
import threading
import requests
import json
import os

import module.token_checker as token_checker
import module.proxy_checker as proxy_checker
import module.joiner as module_joiner
import module.leaver as module_leaver
import module.spam.spammer as module_spammer
import module.vcspam as module_vc
import module.spam.reply as module_reply

colorama.init(autoreset=True)
root = tk.Tk()
root.geometry("1280x720")
root.resizable(0, 0)
root.title("TwoCoinRaider")
root.configure(bg="#213A3E")

class Setting:
  tokens = []
  validtoken = 0
  invalidtoken = 0
  
  # enabled ck.button
  proxy_enabled = tk.BooleanVar()
  proxy_enabled.set("False")
  
  token_filenameLabel = tk.StringVar()
  token_filenameLabel.set("")
  totaltokenLabel = tk.StringVar()
  totaltokenLabel.set("Total: 000")
  validtokenLabel = tk.StringVar()
  validtokenLabel.set("Valid: 000")
  invalidtokenLabel = tk.StringVar()
  invalidtokenLabel.set("Invalid: 000")

  proxytype = "http"
  proxies = []
  vaildproxies = 0
  invaildproxies = 0

  http_value = BooleanVar()
  http_value.set("False")
  socks4_value = BooleanVar()
  socks4_value.set("True")
  socks5_value = BooleanVar()
  socks5_value.set("True")
  proxysetting = BooleanVar()
  proxysetting.set("False")

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
  
  suc_joiner_Label = tk.StringVar()
  suc_joiner_Label.set("Success: 000")
  fai_joiner_Label = tk.StringVar()
  fai_joiner_Label.set("Failed: 000")
  
  suc_leaver_Label = tk.StringVar()
  suc_leaver_Label.set("Success: 000")
  fai_leaver_Label = tk.StringVar()
  fai_leaver_Label.set("Failed: 000")
  
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
  
  spam_allping = BooleanVar()
  spam_allping.set("False")
  spam_allch = BooleanVar()
  spam_allch.set("False")
  spam_rdstring = BooleanVar()
  spam_rdstring.set("False")
  spam_ratefixer = BooleanVar()
  spam_ratefixer.set("False")

  reply_allping = BooleanVar()
  reply_allping.set("False")
  reply_allmg = BooleanVar()
  reply_allmg.set("False")
  reply_rdstring = BooleanVar()
  reply_rdstring.set("False")
  reply_ratefixer = BooleanVar()
  reply_ratefixer.set("False")
  
  delay01 = tk.DoubleVar()
  delay01.set(0.1)
  
  delay02 = tk.DoubleVar()
  delay02.set(0.1)
  
  delay03 = tk.DoubleVar()
  delay03.set(0.1)
    
  delay04 = tk.DoubleVar()
  delay04.set(0.1)
  
  delay91 = tk.DoubleVar()
  delay91.set(0.1)
  
  mention_count_def = tk.DoubleVar()
  mention_count_def.set(20)
  
  joiner_link = tk.StringVar()
  joiner_link.set("")
  bypass_ms = BooleanVar()
  bypass_ms.set("False")
  joiner_serverid = tk.StringVar()
  joiner_serverid.set("")
  leaver_serverid = tk.StringVar()
  leaver_serverid.set("")
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
  
  voicefile = []
  
class SettingVariable:
  joinerresult_success = 0
  joinerresult_failed = 0
  leaverresult_success = 0
  leaverresult_failed = 0
  nmspamresult_success = 0
  nmspamresult_failed = 0
  replyspamresult_success = 0
  replyspamresult_failed = 0

# value def
def clear_entry01():
  Setting.joiner_link.set("")
def clear_entry02():
  Setting.joiner_serverid.set("")
def clear_entry03():
  Setting.leaver_serverid.set("")
def clear_entry04():
  Setting.spam_serverid.set("")
def clear_entry05():
  Setting.spam_channelid.set("")
def clear_entry04():
  Setting.reply_serverid.set("")
def clear_entry05():
  Setting.reply_channelid.set("")
def clear_entry05():
  Setting.reply_messageid.set("")
def clear_entry11():
  Setting.vcspam_serverid.set("")
def clear_entry12():
  Setting.vcspam_channelid.set("") 
  
def get_info():
  invite_code = invite_url.get()
  print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py:180] Connecting API Server...")
  res = requests.get(f"https://discord.com/api/v9/invites/{invite_code}?with_counts=true&with_expiration=true")
  if res.status_code == 200:
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py:180] Successfull Get Info")
    info = json.loads(res.text)
    print(f"""
----------
Server ID 
{info["guild"]["id"]}
----------
Server Name
{info["guild"]["name"]}

Server Description
{info["guild"]["description"]}
----------
Member Count
{str(info["approximate_member_count"])}

Boost Count
{str(info["guild"]["premium_subscription_count"])}
----------""")
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py:180] End Info")
    Setting.joiner_serverid.set(info["guild"]["id"])
    Setting.leaver_serverid.set(info["guild"]["id"])
    Setting.spam_serverid.set(info["guild"]["id"])
    Setting.reply_serverid.set(info["guild"]["id"])
    Setting.vcspam_serverid.set(info["guild"]["id"])
    serverid = info["guild"]["id"]
    servername = info["guild"]["name"]
    serverdescription = info["guild"]["description"]
    membercount = str(info["approximate_member_count"])
    boostcount = str(info["guild"]["premium_subscription_count"])
    CTkMessagebox(title="Invite Info", message=f"Server ID: {serverid}\nServer Name: {servername}\nServer Description: {serverdescription}\n\nMember Count: {membercount}\nBoost Count: {boostcount}", width=450)
  if res.status_code == 404:
    print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [main.py:180] Unknown Invite")

def get_hwid():
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n")+2
    uuid = uuid[pos1:-15]
    return uuid

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
    global voicefile
    fTyp = [("", "*.mp3")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(
        filetype=fTyp, initialdir=iFile, title="Select Voice File")
    if filepath == "":
        return
    voicefile = filepath
    Setting.voicefile = voicefile
    if voicefile == []:
        return
    voicefile_show = voicefile.split('/')[len(voicefile.split('/'))-1]
    Setting.voicefile_filenameLabel.set(voicefile_show)

def token_load():
  fTyp = [("", "*.txt")]
  iFile = os.path.abspath(os.path.dirname(__file__))
  filepath = filedialog.askopenfilename(
      filetype=fTyp, initialdir=iFile, title="Select Tokens")
  if filepath == "":
      return
  if os.path.exists(r"config.json"):
    print()
  else:
    tokens = open(filepath, 'r').read().splitlines()
    with open('config.json', 'w') as creating_new_json_file:
      pass
    token_file_path = {
      "token_path": filepath
    }
    tokens_file = json.dumps(token_file_path)
    with open("config.json", "w") as configfile:
      configfile.write(tokens_file)
  if tokens == []:
      return
  Setting.tokens = []
  Setting.validtoken = 0
  Setting.invalidtoken = 0
  Setting.token_filenameLabel.set(os.path.basename(filepath))
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

def proxy_load():
  fTyp = [("", "*.txt")]
  iFile = os.path.abspath(os.path.dirname(__file__))
  filepath = filedialog.askopenfilename(
      filetype=fTyp, initialdir=iFile, title="Select Proxies")
  if filepath == "":
      return
  proxies = open(filepath, 'r').read().splitlines()
  if proxies == []:
      return
  Setting.proxies = []
  Setting.vaildproxies = 0
  Setting.invaildproxies = 0
  Setting.totalProxiesLabel.set("Total: "+str(len(proxies)).zfill(3))
  proxy_checker.check(update_proxy, proxies, Setting.proxytype)
  threading.Thread(target=proxy_checker.check(update_proxy, proxies, Setting.proxytype))
     
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

def module_thread(num):
  tokens = Setting.tokens
  proxies = Setting.proxies
  proxytype = Setting.proxytype
  proxysetting = Setting.proxy_enabled
  delay = Setting.delay91.get()
  print(tokens)
  if num == 1_1:
    serverid = str(Setting.joiner_serverid.get())
    invitelink = Setting.joiner_link.get()
    memberscreen = Setting.bypass_ms.get()
    
    delay = Setting.delay01.get()
    
    if invitelink == "":
        print("[-] InviteLink is not set")
        return
    if invitelink.__contains__('discord.gg/'):
        invitelink = invitelink.replace('discord.gg/', '').replace('https://', '').replace('http://', '')
    elif invitelink.__contains__('discord.com/invite/'):
        invitelink = invitelink.replace('discord.com/invite/', '').replace('https://', '').replace('http://', '')
    try:
        invitelink = invitelink.split(".gg/")[1]
    except:
        pass
    if memberscreen == True:
        if serverid == "":
            print("[-] ServerID is not set")
            return
          
    threading.Thread(target=module_joiner.start, args=(tokens, serverid, invitelink, memberscreen, delay, module_status)).start()
    
  if num == 2_1:
    serverid = Setting.leaver_serverid.get()
    
    delay = Setting.delay02.get()
    
    threading.Thread(target=module_leaver.start, args=(serverid, delay, tokens)).start()
  
  if num == 2_2:
    threading.Thread(target=module_leaver.stop).start()
  
  if num == 3_1:
    serverid = str(Setting.spam_serverid.get())
    channelid = str(Setting.spam_channelid.get())
    allchannel = Setting.spam_allch.get()
    allping = Setting.spam_allping.get()
    randomstring = Setting.spam_rdstring.get()
    ratelimit = Setting.spam_ratefixer.get()
    
    contents = spam_message.get("0.0","end-1c")
    mentions = Setting.mention_count_def.get()
    
    delay = Setting.delay03.get()
    
    if serverid == "":
        print("[-] ServerID is not set")
        return
    if channelid == "":
        print("[-] ChannelID is not set")
        return    

    threading.Thread(target=module_spammer.start, args=(delay, tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, contents, allchannel, allping, mentions, randomstring, ratelimit)).start()
    
  if num == 3_2:
    module_spammer.stop()
  
  if num == 4_1:
    serverid = Setting.vcspam_serverid.get()
    channelid = Setting.vcspam_channelid.get()
    voicefile = Setting.voicefile
        
    try:
        ffmpeg = os.path.join(os.getcwd(),"ffmpeg.exe")
    except:
        print("Error load ffmpeg")
        ffmpeg = ffmpeg_load()
        
    threading.Thread(target=module_vc.start, args=(delay, tokens, serverid, channelid, ffmpeg, voicefile)).start()
    
  if num == 4_2:
    threading.Thread(target=module_vc.stop).start()
    
  if num == 5_1:
    serverid = str(Setting.reply_serverid.get())
    channelid = str(Setting.reply_channelid.get())
    messageid = str(Setting.reply_messageid.get())
    allmg = Setting.reply_allmg.get()
    allping = Setting.reply_allping.get()
    randomstring = Setting.reply_rdstring.get()
    ratelimit = Setting.reply_ratefixer.get()
    
    contents = reply_message.get("0.0","end-1c")
    mentions = Setting.mention_count_def.get()
    
    delay = Setting.delay04.get()
    
    if serverid == "":
        print("[-] ServerID is not set")
        return
    if channelid == "":
        print("[-] ChannelID is not set")
        return  
    if messageid == "":
        print("[-] ChannelID is not set")
        return    

    threading.Thread(target=module_reply.start, args=(delay, tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, messageid, contents, allmg, allping, mentions, randomstring, ratelimit)).start()
    
  if num == 5_2:
    module_reply.stop()

def module_status(num1, num2):
  if num1 == 1:
    if num2 == 1:
      SettingVariable.joinerresult_success +=1
      Setting.suc_joiner_Label.set("Success: "+str(SettingVariable.joinerresult_success).zfill(3))
    if num2 == 1:
      SettingVariable.joinerresult_failed +=1
      Setting.fai_joiner_Label.set("Failed: "+str(SettingVariable.joinerresult_failed).zfill(3))
  if num1 == 2:
    if num2 == 1:
      SettingVariable.leaverresult_success +=1
      Setting.suc_leaver_Label.set("Success: "+str(SettingVariable.leaverresult_success).zfill(3))
    if num2 == 2:
      SettingVariable.leaverresult_failed +=1
      Setting.fai_leaver_Label.set("Failed: "+str(SettingVariable.leaverresult_failed).zfill(3))
  if num1 == 3:
    if num2 == 1:
      SettingVariable.nmspamresult_success +=1
      Setting.suc_nmspam_Label.set("Success: "+str(SettingVariable.nmspamresult_success).zfill(3))
    if num2 == 2:
      SettingVariable.nmspamresult_failed +=1
      Setting.fai_nmspam_Label.set("Failed: "+str(SettingVariable.nmspamresult_failed).zfill(3))
  if num1 == 4:
    if num2 == 1:
      SettingVariable.replyspamresult_success +=1
      Setting.suc_replyspam_Label.set("Success: "+str(SettingVariable.replyspamresult_success).zfill(3))
    if num2 == 2:
      SettingVariable.replyspamresult_failed +=1
      Setting.fai_replyspam_Label.set("Failed: "+str(SettingVariable.replyspamresult_failed).zfill(3))      
        
def set_moduleframe(num1, num2):
  global invite_url
  frame = module_frame = ctk.CTkFrame(root, width=990, height=680)
  module_frame.place(x=270, y=20)
  module_frame.configure(fg_color="#28464B")
  clear_frame(frame)
  if num1 == 1:
    if num2 == 1:
      # Joiner Frame
      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=250, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.place(x=20,y=20)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="Joiner", font=("Roboto", 14)).place(x=35,y=-1)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, text="Bypass MemberScreen", variable=Setting.bypass_ms).place(x=5,y=11)
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry01).place(x=5,y=40)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.joiner_link).place(x=85,y=40)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Invite Link", font=("Roboto", 12)).place(x=240,y=38)
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry02).place(x=5,y=69)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.joiner_serverid).place(x=85,y=69)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=67)
      
      def slider_event01(value):
        tk.Label(module_frame, bg="#28464B", fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=225,y=111)
      
      ctk.CTkSlider(module_setting_frame, from_=0.1, to=3.0, variable=Setting.delay01, command=slider_event01).place(x=5,y=96)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(Setting.delay01.get(),1), font=("Roboto", 12)).place(x=205,y=91)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=91)
      
      ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(1_1)).place(x=5,y=116)
      ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(1_2)).place(x=70,y=116)
      
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=146)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.suc_joiner_Label, font=("Roboto", 12)).place(x=10,y=174)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.fai_joiner_Label, font=("Roboto", 12)).place(x=10,y=199)
      
      
      # Leaver Frame
      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=175, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.place(x=400,y=20)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="Leaver", font=("Roboto", 14)).place(x=415,y=-1)
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry03).place(x=5,y=13)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.leaver_serverid).place(x=85,y=13)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=11)
      
      def slider_event02(value):
        tk.Label(module_frame, bg="#28464B", fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=605,y=55)
      
      ctk.CTkSlider(module_setting_frame, from_=0.1, to=3.0, variable=Setting.delay02, command=slider_event02).place(x=5,y=40)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(Setting.delay02.get(),1), font=("Roboto", 12)).place(x=205,y=35)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=35)
      
      ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(2_1)).place(x=5,y=60)
      ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(2_2)).place(x=70,y=60)
      
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=90)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.suc_leaver_Label, font=("Roboto", 12)).place(x=10,y=115)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.fai_leaver_Label, font=("Roboto", 12)).place(x=10,y=135)
      
      print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py:676] Open Join Leave Tab")
    
    if num2 == 2:
      ## Spammer
      #module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=250, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      #module_setting_frame.place(x=20,y=20)
      #tk.Label(module_frame, bg="#28464B", fg="#fff", text="Spammer", font=("Roboto", 14)).place(x=35,y=-1)
      #ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allping ,text="All Ping").place(x=5,y=11)
      #ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allch ,text="All Ch").place(x=5,y=33)
      #ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_rdstring ,text="Random String").place(x=5,y=55)
      #ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_ratefixer ,text="RateLimitFixer").place(x=5,y=77)
      #ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry04).place(x=5,y=106)
      #ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.spam_serverid).place(x=85,y=106)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=104)
      #ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry05).place(x=5,y=135)
      #ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.spam_channelid).place(x=85,y=135)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=133)
      #
      #def slider_event03(value):
      #  tk.Label(module_frame, bg="#28464B", fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=225,y=175)
      #
      #ctk.CTkSlider(module_setting_frame, from_=0.1, to=3.0, variable=Setting.delay03, command=slider_event03).place(x=5,y=160)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(Setting.delay03.get(),1), font=("Roboto", 12)).place(x=205,y=155)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=155)
      #
      #spam_message = ctk.CTkTextbox(module_setting_frame, bg_color="#28464B", fg_color="#275258", text_color="#fff", width=150, height=60)
      #spam_message.place(x=120,y=11)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Message", font=("Roboto", 12)).place(x=275,y=25)
      #  
      #ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(3_1)).place(x=5,y=182)
      #ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(3_2)).place(x=70,y=182)

      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=175)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.suc_nmspam_Label, font=("Roboto", 12)).place(x=140,y=200)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.fai_nmspam_Label, font=("Roboto", 12)).place(x=140,y=220)
      #     
      ## VC Spam
      #module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=175, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      #module_setting_frame.place(x=400,y=20)
      #tk.Label(module_frame, bg="#28464B", fg="#fff", text="VC Spammer", font=("Roboto", 14)).place(x=435,y=-1)
      #ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry11).place(x=5,y=13)
      #ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.vcspam_serverid).place(x=85,y=13)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=11)
      #ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry12).place(x=5,y=42)
      #ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.vcspam_channelid).place(x=85,y=42)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=40)
      #ctk.CTkButton(module_setting_frame, text="Select File", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=lambda: voice_load()).place(x=5,y=71)
      #ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=71)
      #ctk.CTkLabel(module_setting_frame, bg_color="#28464B", fg_color="#275258", text_color="#fff", text="", width=150, height=20, textvariable=Setting.voicefile_filenameLabel).place(x=85,y=71)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=69)

      #ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(4_1)).place(x=5,y=102)
      #ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(4_2)).place(x=70,y=102)

      ## Reply Spam
      #module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=250, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      #module_setting_frame.place(x=20,y=300)
      #tk.Label(module_frame, bg="#28464B", fg="#fff", text="Reply", font=("Roboto", 14)).place(x=35,y=279)
      #ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_allping ,text="All Ping").place(x=5,y=11)
      #ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_allmg ,text="All Mg").place(x=5,y=33)
      #ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_rdstring ,text="Random String").place(x=5,y=55)
      #ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_ratefixer ,text="RateLimitFixer").place(x=5,y=77)
      #
      #ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry04).place(x=5,y=106)
      #ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.reply_serverid).place(x=85,y=106)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=104)
      #
      #ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry05).place(x=5,y=135)
      #ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.reply_channelid).place(x=85,y=135)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=133)
      #
      #ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry05).place(x=5,y=164)
      #ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.reply_messageid).place(x=85,y=164)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Message ID", font=("Roboto", 12)).place(x=240,y=162)
      #
      #def slider_event04(value):
      #  tk.Label(module_frame, bg="#28464B", fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=225,y=482)
      #
      #ctk.CTkSlider(module_setting_frame, from_=0.1, to=3.0, variable=Setting.delay04, command=slider_event04).place(x=5,y=189)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(Setting.delay04.get(),1), font=("Roboto", 12)).place(x=205,y=184)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=184)
      #
      #reply_message = ctk.CTkTextbox(module_setting_frame, bg_color="#28464B", fg_color="#275258", text_color="#fff", width=150, height=60)
      #reply_message.place(x=120,y=11)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Message", font=("Roboto", 12)).place(x=275,y=25)
  
      #ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(5_1)).place(x=5,y=209)
      #ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(5_2)).place(x=70,y=209)

      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=175)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.suc_nmspam_Label, font=("Roboto", 12)).place(x=140,y=200)
      #tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.fai_nmspam_Label, font=("Roboto", 12)).place(x=140,y=220)
      
      set_moduleframe_scroll(num1, num2)
      
      print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py:677] Open Spam Tab")

  if num1 == 2:
    if num2 == 1:
      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=145, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.place(x=20,y=20)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="Tokens", font=("Roboto", 14)).place(x=35,y=4)
      ctk.CTkButton(module_setting_frame, text="Select File", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=lambda: token_load()).place(x=5,y=13)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=13)
      ctk.CTkLabel(module_setting_frame, bg_color="#28464B", fg_color="#275258", text_color="#fff", text="", width=150, height=20, textvariable=Setting.token_filenameLabel).place(x=85,y=13)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=11)
      
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=50)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Total: 000", font=("Roboto", 12), textvariable=Setting.totaltokenLabel).place(x=10,y=75)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Valid: 000", font=("Roboto", 12), textvariable=Setting.validtokenLabel).place(x=10,y=95)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Invalid: 000", font=("Roboto", 12), textvariable=Setting.invalidtokenLabel).place(x=10,y=115)
      
      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=165, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.place(x=400,y=20)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="Proxies", font=("Roboto", 14)).place(x=415,y=4)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.proxy_enabled ,text="Enabled").place(x=5,y=11)
      ctk.CTkButton(module_setting_frame, text="Select File", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=lambda: proxy_load()).place(x=5,y=40)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=40)
      ctk.CTkLabel(module_setting_frame, bg_color="#28464B", fg_color="#275258", text_color="#fff", text="", width=150, height=20, textvariable=Setting.proxy_filenameLabel).place(x=85,y=40)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=37)
      
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=70)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Total: 000", font=("Roboto", 12), textvariable=Setting.totalProxiesLabel).place(x=10,y=95)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Valid: 000", font=("Roboto", 12), textvariable=Setting.validProxiesLabel).place(x=10,y=115)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Invalid: 000", font=("Roboto", 12), textvariable=Setting.invalidProxiesLabel).place(x=10,y=135)

      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=145, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.place(x=20,y=200)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="Settings", font=("Roboto", 14)).place(x=35,y=184)
      def slider_event91(value):
        tk.Label(module_frame, bg="#28464B", fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=225,y=210)
      ctk.CTkSlider(module_setting_frame, from_=0.1, to=3.0, variable=Setting.delay91, command=slider_event91).place(x=5,y=15)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(Setting.delay91.get(),1), font=("Roboto", 12)).place(x=205,y=10)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Defalut Delay", font=("Roboto", 12)).place(x=240,y=10)
      def slider_event92(value):
        tk.Label(module_frame, bg="#28464B", fg="#fff", text="        ", font=("Roboto", 12)).place(x=225,y=240)
        tk.Label(module_frame, bg="#28464B", fg="#fff", text=round(value), font=("Roboto", 12)).place(x=225,y=240)
      ctk.CTkSlider(module_setting_frame, from_=1, to=50, variable=Setting.mention_count_def, command=slider_event92).place(x=5,y=45)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(Setting.mention_count_def.get()), font=("Roboto", 12)).place(x=205,y=40)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Defalut Mt Ct", font=("Roboto", 12)).place(x=240,y=40)
      ctk.CTkButton(module_setting_frame, text="Get Info     ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=lambda: get_info()).place(x=5,y=106)
      invite_url = ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20)
      invite_url.place(x=85,y=106)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Defalut Sv ID", font=("Roboto", 12)).place(x=240,y=104)
      
      print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py:678] Open Settings Tab")
    if num2 == 2:
      tk.Label(module_frame, text="TwoCoin Github: ", bg="#28464B", fg="#4D8387", font=("Roboto", 12)).place(x=10,y=10)
      link01 = tk.Label(module_frame, text="GitHub link", bg="#28464B", fg="#fff", font=("Roboto", 12))
      link01.place(x=130,y=10)
      link01.bind("<Button-1>", lambda e:webbrowser.open_new("https://github.com/NyaShinn1204/TwoCoinRaider"))
      tk.Label(module_frame, text="TwoCoin discord: ", bg="#28464B", fg="#4D8387", font=("Roboto", 12)).place(x=10,y=35)
      link02 = tk.Label(module_frame, text="Discord invite link", bg="#28464B", fg="#fff", font=("Roboto", 12))
      link02.place(x=135,y=35)
      link02.bind("<Button-1>", lambda e:webbrowser.open_new("https://discord.gg/ntra"))
      
      print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py:679] Open Abouts Tab")

def set_moduleframe_scroll(num1, num2):
  global spam_message, reply_message
  frame = module_frame = ctk.CTkScrollableFrame(root, width=970, height=660)
  module_frame.place(x=270, y=20)
  module_frame.configure(fg_color="#28464B")
  clear_frame(frame)
  if num1 == 1:
    if num2 == 2: # Spammer Tab
      # Spammer
      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=250, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.grid(row=0, column=0, padx=12, pady=12)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="Spammer", font=("Roboto", 14)).place(x=30,y=-6)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allping ,text="All Ping").place(x=5,y=11)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allch ,text="All Ch").place(x=5,y=33)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_rdstring ,text="Random String").place(x=5,y=55)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_ratefixer ,text="RateLimitFixer").place(x=5,y=77)
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry04).place(x=5,y=106)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.spam_serverid).place(x=85,y=106)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=104)
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry05).place(x=5,y=135)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.spam_channelid).place(x=85,y=135)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=133)
      
      def slider_event03(value):
        tk.Label(module_frame, bg="#28464B", fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=225,y=175)
      
      ctk.CTkSlider(module_setting_frame, from_=0.1, to=3.0, variable=Setting.delay03, command=slider_event03).place(x=5,y=160)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(Setting.delay03.get(),1), font=("Roboto", 12)).place(x=205,y=155)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=155)
      
      spam_message = ctk.CTkTextbox(module_setting_frame, bg_color="#28464B", fg_color="#275258", text_color="#fff", width=150, height=60)
      spam_message.place(x=120,y=11)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Message", font=("Roboto", 12)).place(x=275,y=25)
        
      ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(3_1)).place(x=5,y=182)
      ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(3_2)).place(x=70,y=182)

      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=175)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.suc_nmspam_Label, font=("Roboto", 12)).place(x=140,y=200)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.fai_nmspam_Label, font=("Roboto", 12)).place(x=140,y=220)

      # VC Spam
      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=175, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.place(x=390,y=12)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="VC Spammer", font=("Roboto", 14)).place(x=435,y=-6)
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry11).place(x=5,y=13)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.vcspam_serverid).place(x=85,y=13)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=11)
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry12).place(x=5,y=42)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.vcspam_channelid).place(x=85,y=42)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=40)
      ctk.CTkButton(module_setting_frame, text="Select File", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=lambda: voice_load()).place(x=5,y=71)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=71)
      ctk.CTkLabel(module_setting_frame, bg_color="#28464B", fg_color="#275258", text_color="#fff", text="", width=150, height=20, textvariable=Setting.voicefile_filenameLabel).place(x=85,y=71)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=69)

      ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(4_1)).place(x=5,y=102)
      ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(4_2)).place(x=70,y=102)

      # Reply Spam
      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=275, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.grid(row=1, column=0, padx=12, pady=20)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="Reply", font=("Roboto", 14)).place(x=30,y=274)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_allping ,text="All Ping").place(x=5,y=11)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_allmg ,text="All Mg").place(x=5,y=33)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_rdstring ,text="Random String").place(x=5,y=55)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_ratefixer ,text="RateLimitFixer").place(x=5,y=77)
      
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry04).place(x=5,y=106)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.reply_serverid).place(x=85,y=106)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=104)
      
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry05).place(x=5,y=135)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.reply_channelid).place(x=85,y=135)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=133)
      
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry05).place(x=5,y=164)
      ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20, textvariable=Setting.reply_messageid).place(x=85,y=164)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Message ID", font=("Roboto", 12)).place(x=240,y=162)
      
      def slider_event04(value):
        tk.Label(module_frame, bg="#28464B", fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=225,y=482)
      
      ctk.CTkSlider(module_setting_frame, from_=0.1, to=3.0, variable=Setting.delay04, command=slider_event04).place(x=5,y=189)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(Setting.delay04.get(),1), font=("Roboto", 12)).place(x=205,y=184)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=184)
      
      reply_message = ctk.CTkTextbox(module_setting_frame, bg_color="#28464B", fg_color="#275258", text_color="#fff", width=150, height=60)
      reply_message.place(x=120,y=11)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Message", font=("Roboto", 12)).place(x=275,y=25)
  
      ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(5_1)).place(x=5,y=209)
      ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(5_2)).place(x=70,y=209)

      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=202)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.suc_replyspam_Label, font=("Roboto", 12)).place(x=140,y=227)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable=Setting.fai_replyspam_Label, font=("Roboto", 12)).place(x=140,y=247)
      
print(f"""          
       &#BB#&       
     B?^:::^~?B        _______             _____      _       _____       _     _             
    P^:::^^^^^^P      |__   __|           / ____|    (_)     |  __ \     (_)   | |          
    J~~^^~~~~~~J         | |_      _____ | |     ___  _ _ __ | |__) |__ _ _  __| | ___ _ __ 
    B7~!!~~~!~7B         | \ \ /\ / / _ \| |    / _ \| | '_ \|  _  // _` | |/ _` |/ _ \ '__|
     #5J7777J55          | |\ V  V / (_) | |___| (_) | | | | | | \ \ (_| | | (_| |  __/ |    　
       &&&&&&&           |_| \_/\_/ \___/ \_____\___/|_|_| |_|_|  \_\__,_|_|\__,_|\___|_|   
                                            This Software was Paid Only                                                     
                                       
You HWID: [{get_hwid()}]                
-----------------------""")
if os.path.exists(r"config.json"):
  cfg = open("config.json", "r")
  settings = json.load(cfg)
  filepath = settings["token_path"]
  tokens = open(filepath, 'r').read().splitlines()
  Setting.tokens = []
  Setting.validtoken = 0
  Setting.invalidtoken = 0
  Setting.token_filenameLabel.set(os.path.basename(filepath))
  Setting.totaltokenLabel.set("Total: "+str(len(tokens)).zfill(3))
  threading.Thread(target=token_checker.check(tokens, update_token)).start()
  print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py:21] Loading Tkinter")
else:
  print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py:162] token path not found. Please point to it manually.")
  token_load()
  print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py:21] Loading Tkinter")

tk.Label(bg="#142326", width=35, height=720).place(x=0,y=0)

ctk.CTkLabel(master=root, bg_color="#142326", text="", image=ctk.CTkImage(Image.open("data/coin.png"),size=(80, 80))).place(x=20,y=20)
tk.Label(bg="#142326", text="Two Coin", fg="#fff", font=("Roboto", 20)).place(x=100,y=10)
tk.Label(bg="#142326", text="Raider", fg="#fff", font=("Roboto", 20)).place(x=160,y=40)
tk.Label(bg="#142326", text="v1.0.1", fg="#F8F8F8", font=("Roboto", 18)).place(x=100,y=70)

modulelist = ctk.CTkFrame(master=root, width=250, height=500, border_width=0, bg_color="#142326", fg_color="#142326")
modulelist.place(x=0,y=100)

ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(25, 25)), compound="left", fg_color="#28464B", bg_color="#142326", hover_color="#2C8C99", text="Joiner / Leaver           ", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(1, 1)).place(x=20,y=20)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(25, 25)), compound="left", fg_color="#28464B", bg_color="#142326", hover_color="#2C8C99", text="Spammer                     ", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(1, 2)).place(x=20,y=60)
ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color="#28464B", bg_color="#142326", hover_color="#2C8C99", text="Setting                          ", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 1)).place(x=20,y=620)
ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color="#28464B", bg_color="#142326", hover_color="#2C8C99", text="About                            ", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 2)).place(x=20,y=660)

set_moduleframe(2, 2)

root.mainloop()