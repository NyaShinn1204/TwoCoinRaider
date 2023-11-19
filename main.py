import colorama
import subprocess
import tkinter as tk
import customtkinter as ctk
from customtkinter import *
from PIL import Image
from colorama import Fore
from CTkMessagebox import CTkMessagebox
import webbrowser
import threading
import requests
import json
import os
import time

import module.token_checker as token_checker
import module.proxy_checker as proxy_checker
import module.joiner as module_joiner
import module.leaver as module_leaver
import module.spam.spammer as module_spammer
import module.vcspam as module_vc
import module.spam.reply as module_reply
import module.spam.ticket as module_ticket
import module.spam.slash as module_slash

import bypass.solver.solver as solver

colorama.init(autoreset=True)
root = tk.Tk()
root.geometry("1280x720")
root.resizable(0, 0)
root.title("TwoCoinRaider")
root.iconbitmap(default="data/favicon.ico")
root.configure(bg="#213A3E")

version = "v1.0.3pre-α"
 
class Setting:
  tokens = []
  validtoken = 0
  invalidtoken = 0
  
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
  
  proxytype = tk.StringVar()
  proxytype.set("")
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
  
  # ticket spam
  suc_ticketspam_Label = tk.StringVar()
  suc_ticketspam_Label.set("Success: 000")
  fai_ticketspam_Label = tk.StringVar()
  fai_ticketspam_Label.set("Failed: 000")
  
  # slash spam
  suc_shspam_Label = tk.StringVar()
  suc_shspam_Label.set("Success: 000")
  fai_shspam_Label = tk.StringVar()
  fai_shspam_Label.set("Failed: 000")
  
  spam_allping = tk.BooleanVar()
  spam_allping.set(False)
  spam_allch = tk.BooleanVar()
  spam_allch.set(False)
  spam_rdstring = tk.BooleanVar()
  spam_rdstring.set(False)
  spam_ratefixer = tk.BooleanVar()
  spam_ratefixer.set(False)

  reply_allping = tk.BooleanVar()
  reply_allping.set(False)
  reply_allmg = tk.BooleanVar()
  reply_allmg.set(False)
  reply_rdstring = tk.BooleanVar()
  reply_rdstring.set(False)
  reply_ratefixer = tk.BooleanVar()
  reply_ratefixer.set(False)
  
  slash_ratefixer = tk.BooleanVar()
  slash_ratefixer.set(False) 
  
  sbspam_rdsounds = tk.BooleanVar()
  sbspam_rdsounds.set(False)
  
  delay01 = tk.DoubleVar()
  delay01.set(0.1)
  
  delay02 = tk.DoubleVar()
  delay02.set(0.1)
  
  delay03 = tk.DoubleVar()
  delay03.set(0.1)
    
  delay04 = tk.DoubleVar()
  delay04.set(0.1)
  
  delay05 = tk.DoubleVar()
  delay05.set(0.1)
  
  delay91 = tk.DoubleVar()
  delay91.set(0.1)
  
  mention_count_def = tk.DoubleVar()
  mention_count_def.set(20)
  
  joiner_link = tk.StringVar()
  joiner_link.set("")
  bypass_ms = tk.BooleanVar()
  bypass_ms.set(False)
  bypass_cap = tk.BooleanVar()
  bypass_cap.set(False)
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
  
  voicefile = []

c1 = "#28464B"
c2 = "#25747D"
c3 = "#C0C0C0"
c4 = "#275258"
c5 = "#2C8C99"

class SettingVariable:
  joinerresult_success = 0
  joinerresult_failed = 0
  leaverresult_success = 0
  leaverresult_failed = 0
  nmspamresult_success = 0
  nmspamresult_failed = 0
  replyspamresult_success = 0
  replyspamresult_failed = 0
  ticketspamresult_success = 0
  ticketspamresult_failed = 0
  slashspamresult_success = 0
  slashspamresult_failed = 0

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
def clear_entry06():
  Setting.reply_serverid.set("")
def clear_entry07():
  Setting.reply_channelid.set("")
def clear_entry08():
  Setting.reply_messageid.set("")
def clear_entry11():
  Setting.vcspam_serverid.set("")
def clear_entry12():
  Setting.vcspam_channelid.set("") 
def clear_entry13():
  Setting.sbspam_serverid.set("")
def clear_entry14():
  Setting.sbspam_channelid.set("")
def clear_entry15():
  Setting.ticket_serverid.set("")
def clear_entry16():
  Setting.ticket_channelid.set("")
def clear_entry17():
  Setting.ticket_messageid.set("")
def clear_entry18():
  Setting.slash_serverid.set("")
def clear_entry19():
  Setting.slash_channelid.set("")
def clear_entry20():
  Setting.slash_applicationid.set("")
def clear_entry21():
  Setting.slash_commandname.set("")
def clear_entry22():
  Setting.slash_subcommandname.set("")
def clear_entry23():
  Setting.slash_subcommandname_value.set("")
  
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
  print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] Connecting API Server...")
  res = requests.get(f"https://discord.com/api/v9/invites/{invite_code}?with_counts=true&with_expiration=true")
  if res.status_code == 200:
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] Successfull Get Info")
    info = json.loads(res.text)
    serverid = info["guild"]["id"]
    servername = info["guild"]["name"]
    serverdescription = info["guild"]["description"]
    membercount = str(info["approximate_member_count"])
    boostcount = str(info["guild"]["premium_subscription_count"])
    print(f"""----------\nServer ID\n{serverid}\n----------\nServer Name\n{servername}\n\nServer Description\n{serverdescription}\n----------\nMember Count\n{membercount}\n\nBoost Count\n{boostcount}\n----------""")
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] End Info")
    Setting.joiner_link.set(invite_code)
    Setting.joiner_serverid.set(serverid)
    Setting.leaver_serverid.set(serverid)
    Setting.spam_serverid.set(serverid)
    Setting.reply_serverid.set(serverid)
    Setting.vcspam_serverid.set(serverid)
    Setting.ticket_serverid.set(serverid)
    CTkMessagebox(title="Invite Info", message=f"Server ID: {serverid}\nServer Name: {servername}\nServer Description: {serverdescription}\n\nMember Count: {membercount}\nBoost Count: {boostcount}", width=450)
  if res.status_code == 404:
    print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [main.py] Unknown Invite")

def get_hwid():
  if os.name == 'posix':
    uuid = "Linux User Nothing HWID"
    return uuid
  else:
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n")+2
    uuid = uuid[pos1:-15]
    return uuid

def config_check():
  if os.path.exists(r"config.json"):
    filepath = json.load(open("config.json", "r"))["token_path"]
    tokens = open(filepath, 'r').read().splitlines()
    Setting.tokens = []
    Setting.validtoken = 0
    Setting.invalidtoken = 0
    Setting.token_filenameLabel.set(os.path.basename(filepath))
    Setting.totaltokenLabel.set("Total: "+str(len(tokens)).zfill(3))
    threading.Thread(target=token_checker.check(tokens, update_token)).start()
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] Config Found")
    return True
  else:
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] Config Not Found")
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] token path not found. Please point to it manually.")
    token_load()
    return False

def ffmpeg_check():
  ffmpeg_path = os.path.join(os.getcwd(),"ffmpeg.exe")
  if os.path.exists(ffmpeg_path):
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] FFmpeg Found")
  else :
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] FFmpeg Not Found")
    ffmpeg_dl()

def ffmpeg_dl():
  with open("ffmpeg.exe" ,mode='wb') as f:
    f.write(requests.get("https://github.com/n00mkrad/smol-ffmpeg/releases/download/v1/ffmpeg.exe").content)
    print("Downloaded FFmpeg.")

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
    with open('config.json', 'w'):
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

# Proxy Tab
def proxy_load():
  threading.Thread(target=proxy_main).start()
  
def proxy_main():
  summon_select()
  proxy_type = Setting.proxytype.get()
  print(proxy_type)
  if proxy_type == "":
    print("[-] Cancel proxy")
    return
  proxy_filepath()

def proxy_filepath():
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

def summon_select():
  window01 = tk.Tk()
  window01.title("Select Proxy Type")
  window01.geometry("400x270")
  window01.configure(bg="#262626")
  main_font = ctk.CTkFont(family="Helvetica", size=12)
    
  def socks4():
    Setting.proxytype.set("socks4")
    window01.destroy()
  def socks5():
    Setting.proxytype.set("socks5")
    window01.destroy()
  def http():
    Setting.proxytype.set("http")
    window01.destroy()
  def https():
    Setting.proxytype.set("https")
    window01.destroy()
  def close():
    Setting.proxytype.set("")
    window01.destroy()
  
  type01 = ctk.CTkButton(master=window01,command=socks4,text="Socks4",font=main_font,text_color="white",hover=True,hover_color="#3f98d7",height=30,width=100,border_width=2,corner_radius=20,border_color="#2d6f9e",bg_color="#262626",fg_color= "#3b8cc6")
  type01.place(x= 15, y= 15)
  type02 = ctk.CTkButton(master=window01,command=socks5,text="Socks5",font=main_font,text_color="white",hover=True,hover_color="#3f98d7",height=30,width=100,border_width=2,corner_radius=20,border_color="#2d6f9e",bg_color="#262626",fg_color= "#3b8cc6")
  type02.place(x= 15, y= 60)
  type03 = ctk.CTkButton(master=window01,command=http,text="Http",font=main_font,text_color="white",hover=True,hover_color="#3f98d7",height=30,width=100,border_width=2,corner_radius=20,border_color="#2d6f9e",bg_color="#262626",fg_color= "#3b8cc6")
  type03.place(x= 15, y= 105)
  type04 = ctk.CTkButton(master=window01,command=https,text="Https",font=main_font,text_color="white",hover=True,hover_color="#3f98d7",height=30,width=100,border_width=2,corner_radius=20,border_color="#2d6f9e",bg_color="#262626",fg_color= "#3b8cc6")
  type04.place(x= 15, y= 150)
  type05 = ctk.CTkButton(master=window01,command=close,text="Close",font=main_font,text_color="white",hover=True,hover_color="#3f98d7",height=30,width=100,border_width=2,corner_radius=20,border_color="#2d6f9e",bg_color="#262626",fg_color= "#3b8cc6")
  type05.place(x= 15, y= 195)
  
  window01.mainloop()

def clear_frame(frame):
  for widget in frame.winfo_children():
    widget.destroy()

def module_thread(num):
  tokens = Setting.tokens
  proxies = Setting.proxies
  proxytype = Setting.proxytype.get()
  proxysetting = Setting.proxy_enabled
  delay = Setting.delay91.get()
  print(tokens)
  if num == 1_1:
    serverid = str(Setting.joiner_serverid.get())
    invitelink = Setting.joiner_link.get()
    memberscreen = Setting.bypass_ms.get()
    bypasscaptcha = Setting.bypass_cap.get()
    
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
    if bypasscaptcha == True:
      if answers == "":
        print("[-] Please Select API Service")
        return
      else:
        if apis == "":
          print("[-] Please Input API Keys")
    else:
      answers = None
      apis = None
          
    threading.Thread(target=module_joiner.start, args=(tokens, serverid, invitelink, memberscreen, delay, module_status, answers, apis, bypasscaptcha)).start()
    
  if num == 2_1:
    serverid = Setting.leaver_serverid.get()
    
    delay = Setting.delay02.get()
    
    if serverid == "":
      print("[-] ServerID is not set")
      return
    
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
      
    if serverid == "":
      print("[-] ServerID is not set")
      return
    if channelid == "":
      print("[-] ChannelID is not set")
      return  
       
    try:
      ffmpeg = os.path.join(os.getcwd(),"ffmpeg.exe")
    except:
      print("Error load ffmpeg")
      ffmpeg = ffmpeg_load()
        
    threading.Thread(target=module_vc.start, args=(delay, tokens, serverid, channelid, ffmpeg, voicefile)).start()
        
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
    
  if num == 6_1:
    serverid = str(Setting.ticket_serverid.get())
    channelid = str(Setting.ticket_channelid.get())
    messageid = str(Setting.ticket_messageid.get())
    
    if serverid == "":
      print("[-] ServerID is not set")
      return
    if channelid == "":
      print("[-] ChannelID is not set")
      return   
    if messageid == "":
      print("[-] MessageID is not set")
      return
    
    threading.Thread(target=module_ticket.start, args=(delay, tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, messageid)).start()
    
  if num == 7_1:
    serverid = str(Setting.slash_serverid.get())
    channelid = str(Setting.slash_channelid.get())
    applicationid = str(Setting.slash_applicationid.get())
    commandname = str(Setting.slash_commandname.get())
    subcommandname = str(Setting.slash_subcommandname.get())
    subcommandname_value = str(Setting.slash_subcommandname_value.get())
    ratelimit = Setting.slash_ratefixer.get()
    
    delay = Setting.delay05.get()
    
    if serverid == "":
      print("[-] ServerID is not set")
      return
    if channelid == "":
      print("[-] ChannelID is not set")
      return   
    if applicationid == "":
      print("[-] ApplicationID is not set")
      return
    
    threading.Thread(target=module_slash.start, args=(delay, tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, applicationid, commandname, subcommandname, subcommandname_value, ratelimit)).start()

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
  if num1 == 5:
    if num2 == 1:
      SettingVariable.ticketspamresult_success +=1
      Setting.suc_ticketspam_Label.set("Success: "+str(SettingVariable.ticketspamresult_success).zfill(3))
    if num2 == 2:
      SettingVariable.ticketspamresult_failed +=1
      Setting.fai_ticketspam_Label.set("Failed: "+str(SettingVariable.ticketspamresult_failed).zfill(3))      
        
def set_moduleframe(num1, num2):
  global invite_url
  frame = module_frame = ctk.CTkFrame(root, width=990, height=680)
  module_frame.place(x=270, y=20)
  module_frame.configure(fg_color=c1)
  clear_frame(frame)
  if num1 == 1:
    if num2 == 1:        
      def hcaptcha_select():
        global answers, apis
        if Setting.bypass_cap.get() == True:
          answer_list = ['1','2','3']
          answer = ctk.CTkInputDialog(text = "Select Sovler\n1, CapSolver\n2, CapMonster\n3, 2Cap")
          answers = answer.get_input()
          if answers in answer_list:
            print("[+] Select " + answers)
            api = ctk.CTkInputDialog(text = "Input API Key")
            apis = api.get_input()
            if apis == "":
              print("[-] Not Set. Please Input")
              Setting.bypass_cap.set(False)
            else:
              print("[+] Insert API Key " + apis)
              print("[~] Checking Balance...")
              if answers == "1":
                if solver.get_balance_capsolver(apis) == 0.0:
                  print("[-] Not Working Or Balance 0.0$ API Key "+ apis)
                  Setting.bypass_cap.set(False)
              if answers == "2":
                if solver.get_balance_capmonster(apis) == 0.0:
                  print("[-] Not Working Or Balance 0.0$ API Key "+ apis)
                  Setting.bypass_cap.set(False)
              if answers == "3":
                if solver.get_balance_2cap(apis) == 0.0:
                  print("[-] Not Working Or Balance 0.0$ API Key "+ apis)
                  Setting.bypass_cap.set(False)
          else:
            print("[-] Not Set. Please Input")
            Setting.bypass_cap.set(False)
      # Joiner Frame
      modules_frame = ctk.CTkFrame(module_frame, width=350, height=275, border_width=1, border_color=c3, fg_color=c1)
      modules_frame.place(x=20,y=20)
      tk.Label(module_frame, bg=c1, fg="#fff", text="Joiner", font=("Roboto", 14)).place(x=35,y=-1)
      ctk.CTkCheckBox(modules_frame, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, text="Bypass MemberScreen", variable=Setting.bypass_ms).place(x=5,y=11)
      ctk.CTkCheckBox(modules_frame, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, text="Bypass hCaptcha", variable=Setting.bypass_cap, command=hcaptcha_select).place(x=5,y=35) 
      ctk.CTkButton(modules_frame, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry01).place(x=5,y=74) #40
      ctk.CTkEntry(modules_frame, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_link).place(x=85,y=74)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Invite Link", font=("Roboto", 12)).place(x=240,y=72) #38
      ctk.CTkButton(modules_frame, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry02).place(x=5,y=103)
      ctk.CTkEntry(modules_frame, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_serverid).place(x=85,y=103)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=101)
            
      def slider_event01(value):
        tk.Label(module_frame, bg=c1, fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=225,y=145)
      
      ctk.CTkSlider(modules_frame, from_=0.1, to=3.0, variable=Setting.delay01, command=slider_event01).place(x=5,y=130)
      tk.Label(modules_frame, bg=c1, fg="#fff", text=round(Setting.delay01.get(),1), font=("Roboto", 12)).place(x=205,y=125)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=125)
      
      ctk.CTkButton(modules_frame, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(1_1)).place(x=5,y=150)
      ctk.CTkButton(modules_frame, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(1_2)).place(x=70,y=150)
      
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=180)
      tk.Label(modules_frame, bg=c1, fg="#fff", textvariable=Setting.suc_joiner_Label, font=("Roboto", 12)).place(x=10,y=208)
      tk.Label(modules_frame, bg=c1, fg="#fff", textvariable=Setting.fai_joiner_Label, font=("Roboto", 12)).place(x=10,y=233)
      
      
      # Leaver Frame
      modules_frame = ctk.CTkFrame(module_frame, width=350, height=175, border_width=1, border_color=c3, fg_color=c1)
      modules_frame.place(x=400,y=20)
      tk.Label(module_frame, bg=c1, fg="#fff", text="Leaver", font=("Roboto", 14)).place(x=415,y=-1)
      ctk.CTkButton(modules_frame, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry03).place(x=5,y=13)
      ctk.CTkEntry(modules_frame, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.leaver_serverid).place(x=85,y=13)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=11)
      
      def slider_event02(value):
        tk.Label(module_frame, bg=c1, fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=605,y=55)
      
      ctk.CTkSlider(modules_frame, from_=0.1, to=3.0, variable=Setting.delay02, command=slider_event02).place(x=5,y=40)
      tk.Label(modules_frame, bg=c1, fg="#fff", text=round(Setting.delay02.get(),1), font=("Roboto", 12)).place(x=205,y=35)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=35)
      
      ctk.CTkButton(modules_frame, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_1)).place(x=5,y=60)
      ctk.CTkButton(modules_frame, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_2)).place(x=70,y=60)
      
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=90)
      tk.Label(modules_frame, bg=c1, fg="#fff", textvariable=Setting.suc_leaver_Label, font=("Roboto", 12)).place(x=10,y=115)
      tk.Label(modules_frame, bg=c1, fg="#fff", textvariable=Setting.fai_leaver_Label, font=("Roboto", 12)).place(x=10,y=135)
      
      print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] Open Join Leave Tab")
    
  if num1 == 2:
    if num2 == 1:
      modules_frame = ctk.CTkFrame(module_frame, width=350, height=145, border_width=1, border_color=c3, fg_color=c1)
      modules_frame.place(x=20,y=20)
      tk.Label(module_frame, bg=c1, fg="#fff", text="Tokens", font=("Roboto", 14)).place(x=35,y=4)
      ctk.CTkButton(modules_frame, text="Select File", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: token_load()).place(x=5,y=13)
      ctk.CTkEntry(modules_frame, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=13)
      ctk.CTkLabel(modules_frame, bg_color=c1, fg_color=c4, text_color="#fff", text="", width=150, height=20, textvariable=Setting.token_filenameLabel).place(x=85,y=13)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=11)
      
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=50)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Total: 000", font=("Roboto", 12), textvariable=Setting.totaltokenLabel).place(x=10,y=75)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Valid: 000", font=("Roboto", 12), textvariable=Setting.validtokenLabel).place(x=10,y=95)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Invalid: 000", font=("Roboto", 12), textvariable=Setting.invalidtokenLabel).place(x=10,y=115)
      
      modules_frame = ctk.CTkFrame(module_frame, width=350, height=165, border_width=1, border_color=c3, fg_color=c1)
      modules_frame.place(x=400,y=20)
      tk.Label(module_frame, bg=c1, fg="#fff", text="Proxies", font=("Roboto", 14)).place(x=415,y=4)
      ctk.CTkCheckBox(modules_frame, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.proxy_enabled ,text="Enabled").place(x=5,y=11)
      ctk.CTkButton(modules_frame, text="Select File", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: proxy_load()).place(x=5,y=40)
      ctk.CTkEntry(modules_frame, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=40)
      ctk.CTkLabel(modules_frame, bg_color=c1, fg_color=c4, text_color="#fff", text="", width=150, height=20, textvariable=Setting.proxy_filenameLabel).place(x=85,y=40)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=37)
      
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=70)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Total: 000", font=("Roboto", 12), textvariable=Setting.totalProxiesLabel).place(x=10,y=95)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Valid: 000", font=("Roboto", 12), textvariable=Setting.validProxiesLabel).place(x=10,y=115)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Invalid: 000", font=("Roboto", 12), textvariable=Setting.invalidProxiesLabel).place(x=10,y=135)

      modules_frame = ctk.CTkFrame(module_frame, width=350, height=145, border_width=1, border_color=c3, fg_color=c1)
      modules_frame.place(x=20,y=200)
      tk.Label(module_frame, bg=c1, fg="#fff", text="Settings", font=("Roboto", 14)).place(x=35,y=184)
      
      def slider_event91(value):
        tk.Label(modules_frame, bg=c1, fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=205,y=10)
        
      ctk.CTkSlider(modules_frame, from_=0.1, to=3.0, variable=Setting.delay91, command=slider_event91).place(x=5,y=15)
      tk.Label(modules_frame, bg=c1, fg="#fff", text=round(Setting.delay91.get(),1), font=("Roboto", 12)).place(x=205,y=10)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Defalut Delay", font=("Roboto", 12)).place(x=240,y=10)
      
      def slider_event92(value):
        tk.Label(modules_frame, bg=c1, fg="#fff", text="        ", font=("Roboto", 12)).place(x=205,y=40)
        tk.Label(modules_frame, bg=c1, fg="#fff", text=round(value), font=("Roboto", 12)).place(x=205,y=40)
        
      ctk.CTkSlider(modules_frame, from_=1, to=50, variable=Setting.mention_count_def, command=slider_event92).place(x=5,y=45)
      tk.Label(modules_frame, bg=c1, fg="#fff", text=round(Setting.mention_count_def.get()), font=("Roboto", 12)).place(x=205,y=40)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Defalut Mt Ct", font=("Roboto", 12)).place(x=240,y=40)
      ctk.CTkButton(modules_frame, text="Get Info     ", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: get_info()).place(x=5,y=106)
      invite_url = ctk.CTkEntry(modules_frame, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20)
      invite_url.place(x=85,y=106)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Defalut Sv ID", font=("Roboto", 12)).place(x=240,y=104)
      
      print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] Open Settings Tab")
    if num2 == 2:
      tk.Label(module_frame, text="TwoCoin Github: ", bg=c1, fg="#4D8387", font=("Roboto", 12)).place(x=10,y=10)
      link01 = tk.Label(module_frame, text="GitHub link", bg=c1, fg="#fff", font=("Roboto", 12))
      link01.place(x=135,y=10)
      link01.bind("<Button-1>", lambda e:webbrowser.open_new("https://github.com/NyaShinn1204/TwoCoinRaider"))
      tk.Label(module_frame, text="TwoCoin discord: ", bg=c1, fg="#4D8387", font=("Roboto", 12)).place(x=10,y=35)
      link02 = tk.Label(module_frame, text="Discord invite link", bg=c1, fg="#fff", font=("Roboto", 12))
      link02.place(x=140,y=35)
      link02.bind("<Button-1>", lambda e:webbrowser.open_new("https://discord.gg/ntra"))
      
      print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] Open Abouts Tab")

def set_moduleframe_scroll(num1, num2):
  global spam_message, reply_message
  frame = module_frame = ctk.CTkScrollableFrame(root, width=970, height=660)
  module_frame.place(x=270, y=20)
  module_frame.configure(fg_color=c1)
  clear_frame(frame)
  if num1 == 1:
    if num2 == 2: # Spammer Tab
      # Spammer
      modules_frame01 = ctk.CTkFrame(module_frame, width=400, height=300, border_width=1, border_color=c3, fg_color=c1)
      modules_frame01.grid(row=0, column=0, padx=12, pady=12)
      tk.Label(modules_frame01, bg=c1, fg="#fff", text="Spammer", font=("Roboto", 12)).place(x=10,y=2)
      ctk.CTkCheckBox(modules_frame01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allping ,text="All Ping").place(x=5,y=26)
      ctk.CTkCheckBox(modules_frame01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allch ,text="All Ch").place(x=5,y=48)
      ctk.CTkCheckBox(modules_frame01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_rdstring ,text="Random String").place(x=5,y=70)
      ctk.CTkCheckBox(modules_frame01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_ratefixer ,text="RateLimitFixer").place(x=5,y=92)
      ctk.CTkButton(modules_frame01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry04).place(x=5,y=121)
      ctk.CTkEntry(modules_frame01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.spam_serverid).place(x=85,y=121)
      tk.Label(modules_frame01, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=119)
      ctk.CTkButton(modules_frame01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry05).place(x=5,y=150)
      ctk.CTkEntry(modules_frame01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.spam_channelid).place(x=85,y=150)
      tk.Label(modules_frame01, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=148)

      def slider_event11(value):
        tk.Label(modules_frame01, bg=c1, fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=205,y=172)
      
      ctk.CTkSlider(modules_frame01, from_=0.1, to=3.0, variable=Setting.delay03, command=slider_event11).place(x=5,y=177)
      tk.Label(modules_frame01, bg=c1, fg="#fff", text=round(Setting.delay03.get(),1), font=("Roboto", 12)).place(x=205,y=172)
      tk.Label(modules_frame01, bg=c1, fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=170)
       
      spam_message = ctk.CTkTextbox(modules_frame01, bg_color=c1, fg_color=c4, text_color="#fff", width=150, height=60)
      spam_message.place(x=120,y=26)
      tk.Label(modules_frame01, bg=c1, fg="#fff", text="Message", font=("Roboto", 12)).place(x=275,y=40)
        
      ctk.CTkButton(modules_frame01, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(3_1)).place(x=5,y=197)
      ctk.CTkButton(modules_frame01, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(3_2)).place(x=70,y=197)

      tk.Label(modules_frame01, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=190)
      tk.Label(modules_frame01, bg=c1, fg="#fff", textvariable=Setting.suc_nmspam_Label, font=("Roboto", 12)).place(x=140,y=215)
      tk.Label(modules_frame01, bg=c1, fg="#fff", textvariable=Setting.fai_nmspam_Label, font=("Roboto", 12)).place(x=140,y=235)

      # Reply Spam
      modules_frame02 = ctk.CTkFrame(module_frame, width=400, height=300, border_width=1, border_color=c3, fg_color=c1)
      modules_frame02.grid(row=0, column=1, padx=12, pady=12)
      tk.Label(modules_frame02, bg=c1, fg="#fff", text="Reply", font=("Roboto", 12)).place(x=10,y=2)
      ctk.CTkCheckBox(modules_frame02, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_allping ,text="All Ping").place(x=5,y=26)
      ctk.CTkCheckBox(modules_frame02, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_allmg ,text="All Mg").place(x=5,y=48)
      ctk.CTkCheckBox(modules_frame02, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_rdstring ,text="Random String").place(x=5,y=70)
      ctk.CTkCheckBox(modules_frame02, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_ratefixer ,text="RateLimitFixer").place(x=5,y=92)
      
      ctk.CTkButton(modules_frame02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry06).place(x=5,y=121)
      ctk.CTkEntry(modules_frame02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reply_serverid).place(x=85,y=121)
      tk.Label(modules_frame02, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=119)
      
      ctk.CTkButton(modules_frame02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry07).place(x=5,y=150)
      ctk.CTkEntry(modules_frame02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reply_channelid).place(x=85,y=150)
      tk.Label(modules_frame02, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=148)
      
      ctk.CTkButton(modules_frame02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry08).place(x=5,y=179)
      ctk.CTkEntry(modules_frame02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reply_messageid).place(x=85,y=179)
      tk.Label(modules_frame02, bg=c1, fg="#fff", text="Message ID", font=("Roboto", 12)).place(x=240,y=177)
      
      def slider_event12(value):
        tk.Label(modules_frame02, bg=c1, fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=208,y=201)
      
      ctk.CTkSlider(modules_frame02, from_=0.1, to=3.0, variable=Setting.delay04, command=slider_event12).place(x=5,y=204)
      tk.Label(modules_frame02, bg=c1, fg="#fff", text=round(Setting.delay04.get(),1), font=("Roboto", 12)).place(x=208,y=201)
      tk.Label(modules_frame02, bg=c1, fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=199)
      
      reply_message = ctk.CTkTextbox(modules_frame02, bg_color=c1, fg_color=c4, text_color="#fff", width=150, height=60)
      reply_message.place(x=120,y=26)
      tk.Label(modules_frame02, bg=c1, fg="#fff", text="Message", font=("Roboto", 12)).place(x=275,y=40)
  
      ctk.CTkButton(modules_frame02, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(5_1)).place(x=5,y=224)
      ctk.CTkButton(modules_frame02, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(5_2)).place(x=70,y=224)

      tk.Label(modules_frame02, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=217)
      tk.Label(modules_frame02, bg=c1, fg="#fff", textvariable=Setting.suc_replyspam_Label, font=("Roboto", 12)).place(x=140,y=242)
      tk.Label(modules_frame02, bg=c1, fg="#fff", textvariable=Setting.fai_replyspam_Label, font=("Roboto", 12)).place(x=140,y=262)

      # Ticket Spam
      modules_frame04 = ctk.CTkFrame(module_frame, width=400, height=200, border_width=1, border_color=c3, fg_color=c1)
      modules_frame04.grid(row=1, column=0, padx=12, pady=12)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Ticket Spammer", font=("Roboto", 12)).place(x=10,y=2)
      ctk.CTkButton(modules_frame04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry15).place(x=5,y=28)
      ctk.CTkEntry(modules_frame04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.ticket_serverid).place(x=85,y=28)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=26)
      ctk.CTkButton(modules_frame04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry16).place(x=5,y=57)
      ctk.CTkEntry(modules_frame04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.ticket_channelid).place(x=85,y=57)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=55)
      ctk.CTkButton(modules_frame04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry17).place(x=5,y=86)
      ctk.CTkEntry(modules_frame04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.ticket_messageid).place(x=85,y=86)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Message ID", font=("Roboto", 12)).place(x=240,y=84)

      ctk.CTkButton(modules_frame04, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(6_1)).place(x=5,y=117)
      
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=85,y=110)
      tk.Label(modules_frame04, bg=c1, fg="#fff", textvariable=Setting.suc_ticketspam_Label, font=("Roboto", 12)).place(x=90,y=135)
      tk.Label(modules_frame04, bg=c1, fg="#fff", textvariable=Setting.fai_ticketspam_Label, font=("Roboto", 12)).place(x=90,y=160)

      # VC Spam
      modules_frame03 = ctk.CTkFrame(module_frame, width=400, height=200, border_width=1, border_color=c3, fg_color=c1)
      modules_frame03.grid(row=1, column=1, padx=12, pady=12)
      tk.Label(modules_frame03, bg=c1, fg="#fff", text="VC Spammer", font=("Roboto", 12)).place(x=10,y=2)
      ctk.CTkButton(modules_frame03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry11).place(x=5,y=28)
      ctk.CTkEntry(modules_frame03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcspam_serverid).place(x=85,y=28)
      tk.Label(modules_frame03, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=26)
      ctk.CTkButton(modules_frame03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry12).place(x=5,y=57)
      ctk.CTkEntry(modules_frame03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcspam_channelid).place(x=85,y=57)
      tk.Label(modules_frame03, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=55)
      ctk.CTkButton(modules_frame03, text="Select File", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: voice_load()).place(x=5,y=86)
      ctk.CTkEntry(modules_frame03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=86)
      ctk.CTkLabel(modules_frame03, bg_color=c1, fg_color=c4, text_color="#fff", text="", width=150, height=20, textvariable=Setting.voicefile_filenameLabel).place(x=85,y=86)
      tk.Label(modules_frame03, bg=c1, fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=84)

      ctk.CTkButton(modules_frame03, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(4_1)).place(x=5,y=117)

      # Slash Spam
      modules_frame04 = ctk.CTkFrame(module_frame, width=400, height=300, border_width=1, border_color=c3, fg_color=c1)
      modules_frame04.grid(row=2, column=0, padx=12, pady=12)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Slash Spammer", font=("Roboto", 12)).place(x=10,y=2)
      ctk.CTkButton(modules_frame04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry18).place(x=5,y=28)
      ctk.CTkEntry(modules_frame04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_serverid).place(x=85,y=28)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=26)
      ctk.CTkButton(modules_frame04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry19).place(x=5,y=57)
      ctk.CTkEntry(modules_frame04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_channelid).place(x=85,y=57)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=55)
      ctk.CTkButton(modules_frame04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry20).place(x=5,y=86)
      ctk.CTkEntry(modules_frame04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_applicationid).place(x=85,y=86)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Application ID", font=("Roboto", 12)).place(x=240,y=84)
      ctk.CTkButton(modules_frame04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry21).place(x=5,y=115)
      ctk.CTkEntry(modules_frame04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_commandname).place(x=85,y=115)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Command Name", font=("Roboto", 12)).place(x=240,y=113)
      ctk.CTkButton(modules_frame04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry22).place(x=5,y=144)
      ctk.CTkEntry(modules_frame04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_subcommandname).place(x=85,y=144)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="SubCommand Name", font=("Roboto", 12)).place(x=240,y=142)
      ctk.CTkButton(modules_frame04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry23).place(x=5,y=173)
      ctk.CTkEntry(modules_frame04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_subcommandname_value).place(x=85,y=173)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="SubCommand Value", font=("Roboto", 12)).place(x=240,y=171)

      def slider_event13(value):
        tk.Label(modules_frame04, bg=c1, fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=208,y=200)
      
      ctk.CTkSlider(modules_frame04, from_=0.1, to=3.0, variable=Setting.delay05, command=slider_event13).place(x=5,y=205)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text=round(Setting.delay05.get(),1), font=("Roboto", 12)).place(x=208,y=200)
      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=198)

      ctk.CTkButton(modules_frame04, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(7_1)).place(x=5,y=225)
      ctk.CTkButton(modules_frame04, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(7_2)).place(x=70,y=225)

      tk.Label(modules_frame04, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=218)
      tk.Label(modules_frame04, bg=c1, fg="#fff", textvariable=Setting.suc_shspam_Label, font=("Roboto", 12)).place(x=140,y=243)
      tk.Label(modules_frame04, bg=c1, fg="#fff", textvariable=Setting.fai_shspam_Label, font=("Roboto", 12)).place(x=140,y=268)

      print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] Open Spam Tab")
      
print(f"""          
       &#BB#&       
     B?^:::^~?B        _______             _____      _       _____       _     _             
    P^:::^^^^^^P      |__   __|           / ____|    (_)     |  __ \     (_)   | |          
    J~~^^~~~~~~J         | |_      _____ | |     ___  _ _ __ | |__) |__ _ _  __| | ___ _ __ 
    B7~!!~~~!~7B         | \ \ /\ / / _ \| |    / _ \| | '_ \|  _  // _` | |/ _` |/ _ \ '__|
     #5J7777J55          | |\ V  V / (_) | |___| (_) | | | | | | \ \ (_| | | (_| |  __/ |    　
       &&&&&&&           |_| \_/\_/ \___/ \_____\___/|_|_| |_|_|  \_\__,_|_|\__,_|\___|_|   
                                            This Software was Paid Only                                                     
                                       
You HWID: [{get_hwid()}]                Version: [{version}]
-----------------------""")
ffmpeg_check()
if config_check():
  print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] Loading Tkinter")
else:
  print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [main.py] Loading Tkinter")

tk.Label(bg="#142326", width=35, height=720).place(x=0,y=0)

ctk.CTkLabel(master=root, bg_color="#142326", text="", image=ctk.CTkImage(Image.open("data/coin.png"),size=(80, 80))).place(x=20,y=20)
tk.Label(bg="#142326", text="Two Coin", fg="#fff", font=("Roboto", 20)).place(x=100,y=10)
tk.Label(bg="#142326", text="Raider", fg="#fff", font=("Roboto", 20)).place(x=160,y=40)
tk.Label(bg="#142326", text=version, fg="#F8F8F8", font=("Roboto", 18)).place(x=100,y=70)

modulelist = ctk.CTkFrame(master=root, width=250, height=500, border_width=0, bg_color="#142326", fg_color="#142326")
modulelist.place(x=0,y=100)

ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="Joiner / Leaver           ", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(1, 1)).place(x=20,y=20)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="Spammer                     ", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe_scroll(1, 2)).place(x=20,y=60)
ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="Setting                          ", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 1)).place(x=20,y=620)
ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="About                            ", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 2)).place(x=20,y=660)

set_moduleframe(2, 2)

root.mainloop()