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

import module.token_checker as token_checker
import module.proxy_checker as proxy_checker
import module.joiner as module_joiner
import module.leaver as module_leaver
import module.spam.spammer as module_spammer
import module.vcspam as module_vc
import module.spam.reply as module_reply
import module.spam.ticket as module_ticket
import module.spam.slash as module_slash
import module.spam.reaction as module_reaction

import bypass.solver.solver as solver

colorama.init(autoreset=True)

version = "v1.0.3β"

root = tk.Tk()
root.geometry("1280x720")
root.resizable(0, 0)
root.title("TwoCoinRaider | "+version)
root.iconbitmap(default="data/favicon.ico")
root.configure(bg="#213A3E")
 
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
  vcspamresult_success = 0
  vcspamresult_failed = 0

# value def
def clear_entry01_01():
  Setting.joiner_link.set("")
def clear_entry01_02():
  Setting.joiner_serverid.set("")
def clear_entry01_03():
  Setting.joiner_channelid.set("")
def clear_entry02_01():
  Setting.leaver_serverid.set("")
def clear_entry03_01():
  Setting.vcjoin_serverid.set("")
def clear_entry03_02():
  Setting.vcjoin_channelid.set("")
def clear_entry04_01():
  Setting.vcleave_serverid.set("")
def clear_entry04_02():
  Setting.vcleave_channelid.set("")
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
def clear_entry24():
  Setting.reaction_channelid.set("")
def clear_entry25():
  Setting.reaction_messageid.set("")
def clear_entry26():
  Setting.reaction_emoji.set("")

def get_filename():
  return os.path.basename(__file__)

def printl(num, data):
  if num == "error":
    print(f"[{Fore.LIGHTRED_EX}Error{Fore.RESET}] [{get_filename()}] " + data)
  if num == "debug":
    print(f"[{Fore.LIGHTCYAN_EX}Debug{Fore.RESET}] [{get_filename()}] " + data)
  if num == "info":
    print(f"[{Fore.LIGHTGREEN_EX}Info{Fore.RESET}] [{get_filename()}] " + data)
    
  

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
    print(f"""----------\nServer ID\n{serverid}\n----------\nServer Name\n{servername}\n\nServer Description\n{serverdescription}\n----------\nMember Count\n{membercount}\n\nBoost Count\n{boostcount}\n----------""")
    printl("debug", "End Info")
    Setting.joiner_link.set(invite_code)
    Setting.joiner_serverid.set(serverid)
    Setting.leaver_serverid.set(serverid)
    Setting.spam_serverid.set(serverid)
    Setting.reply_serverid.set(serverid)
    Setting.vcspam_serverid.set(serverid)
    Setting.ticket_serverid.set(serverid)
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
  if os.path.exists(r"config.json"):
    filepath = json.load(open("config.json", "r"))["token_path"]
    tokens = open(filepath, 'r').read().splitlines()
    Setting.tokens = []
    Setting.validtoken = 0
    Setting.invalidtoken = 0
    Setting.token_filenameLabel.set(os.path.basename(filepath))
    Setting.totaltokenLabel.set("Total: "+str(len(tokens)).zfill(3))
    threading.Thread(target=token_checker.check(tokens, update_token)).start()
    printl("debug", "Config Found")
    return True
  else:
    printl("debug", "Config Not Found")
    printl("debug", "token path not found. Please point to it manually.")
    token_load()
    return False

def ffmpeg_check():
  ffmpeg_path = os.path.join(os.getcwd(),"./data/ffmpeg.exe")
  if os.path.exists(ffmpeg_path):
    printl("debug", "FFmpeg Found")
  else :
    printl("debug", "FFmpeg Not Found")
    download_file("ffmpeg")
  dll_path = os.path.join(os.getcwd(),"./data/libopus.dll")
  if os.path.exists(dll_path):
    printl("debug", "FFmpeg lib Found")
  else :
    printl("debug", "FFmpeg lib Not Found")
    download_file("ffmpeg-dll")

def download_file(type):
  if type == "ffmpeg":
    with open("./data/ffmpeg.exe" ,mode='wb') as f:
      f.write(requests.get("https://github.com/NyaShinn1204/twocoin-assets/raw/main/ffmpeg.exe").content)
      printl("info", "Downloaded FFmpeg.")
  if type == "ffmpeg-dll":
    with open("./data/libopus.dll" ,mode='wb') as f:
      f.write(requests.get("https://github.com/NyaShinn1204/twocoin-assets/raw/main/libopus.dll").content)
      printl("info", "Downloaded FFmpeg Dll.")
      
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

def module_thread(num):
  global answers, apis
  tokens = Setting.tokens
  proxies = Setting.proxies
  proxytype = Setting.proxytype.get()
  proxysetting = Setting.proxy_enabled
  delay = Setting.delay91.get()
  print(tokens)
  if num == 1_1_1:
    serverid = str(Setting.joiner_serverid.get())
    join_channelid = str(Setting.joiner_channelid.get())
    invitelink = Setting.joiner_link.get()
    memberscreen = Setting.bypass_ms.get()
    delete_joinms = Setting.delete_join_ms.get()
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
        print("[-] 代わりにInvite CodeからServerIDを取得します")
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
    if delete_joinms == "":
      if join_channelid == "":
        print("[-] Join ChannelID is not set")
        return

    threading.Thread(target=module_joiner.start, args=(tokens, serverid, invitelink, memberscreen, delay, module_status, answers, apis, bypasscaptcha, delete_joinms, join_channelid)).start()

  if num == 1_2_1:
    serverid = Setting.leaver_serverid.get()

    delay = Setting.delay02.get()

    if serverid == "":
      print("[-] ServerID is not set")
      return

    threading.Thread(target=module_leaver.start, args=(serverid, delay, tokens)).start()

  if num == 1_2_2:
    threading.Thread(target=module_leaver.stop).start()

  if num == 2_3_1:
    serverid = str(Setting.spam_serverid.get())
    channelid = str(Setting.spam_channelid.get())
    allchannel = Setting.spam_allch.get()
    allping = Setting.spam_allping.get()
    randomstring = Setting.spam_rdstring.get()
    ratelimit = Setting.spam_ratefixer.get()
    randomconvert = Setting.spam_randomconvert.get()

    contents = spam_message.get("0.0","end-1c")
    mentions = Setting.mention_count_def.get()

    delay = Setting.delay03.get()

    if serverid == "":
      print("[-] ServerID is not set")
      return
    if channelid == "":
      print("[-] ChannelID is not set")
      return    

    threading.Thread(target=module_spammer.start, args=(delay, tokens, module_status, proxysetting, proxies, proxytype, serverid, channelid, contents, allchannel, allping, mentions, randomstring, ratelimit, randomconvert)).start()

  if num == 2_3_2:
    threading.Thread(target=module_spammer.stop).start()
   
  if num == 2_4_1:
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

    threading.Thread(target=module_vc.start, args=(delay, tokens, module_status, serverid, channelid, ffmpeg, voicefile)).start()

  if num == 2_5_1:
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

  if num == 2_5_2:
    threading.Thread(target=module_reply.stop).start()

  if num == 2_6_1:
    serverid = str(Setting.ticket_serverid.get())
    channelid = str(Setting.ticket_channelid.get())
    messageid = str(Setting.ticket_messageid.get())
    ratelimit = Setting.ticket_ratefixer.get()

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

  if num == 2_6_2:
    threading.Thread(target=module_ticket.stop).start()

  if num == 2_7_1:
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

  if num == 2_7_2:
    threading.Thread(target=module_slash.stop).start()

  if num == 2_8_1:
    channelid = str(Setting.reaction_channelid.get())
    messageid = str(Setting.reaction_messageid.get())
    emoji = str(Setting.reaction_emoji.get())

    if channelid == "":
      print("[-] ChannelID is not set")
      return
    if messageid == "":
      print("[-] Messageid is not set")
      return   
    if emoji == "":
      print("[-] Emoji is not set")
      return

    threading.Thread(target=module_reaction.start, args=(delay, tokens, proxysetting, proxies, proxytype, channelid, messageid, emoji)).start()

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
  if num1 == 6:
    if num2 == 1:
      SettingVariable.vcspamresult_success +=1
      Setting.suc_vcspam_Label.set("Success: "+str(SettingVariable.vcspamresult_success).zfill(3))
    if num2 == 2:
      SettingVariable.vcspamresult_failed +=1
      Setting.fai_vcspam_Label.set("Failed: "+str(SettingVariable.vcspamresult_failed).zfill(3))      

def set_moduleframe(num1, num2):
  global invite_url
  frame = module_frame = ctk.CTkFrame(root, width=990, height=680)
  module_frame.place(x=270, y=20)
  module_frame.configure(fg_color=c1)
  clear_frame(frame)
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
      
      modules_frame = ctk.CTkFrame(module_frame, width=350, height=195, border_width=1, border_color=c3, fg_color=c1)
      modules_frame.place(x=400,y=20)
      tk.Label(module_frame, bg=c1, fg="#fff", text="Proxies", font=("Roboto", 14)).place(x=415,y=4)
      ctk.CTkCheckBox(modules_frame, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.proxy_enabled ,text="Enabled").place(x=5,y=11)
      def set_socket(socks):
        Setting.proxytype.set(socks)
      ctk.CTkOptionMenu(modules_frame, values=["http", "https", "socks4", "socks5"], fg_color=c2, button_color=c5, button_hover_color=c4, command=set_socket, variable=Setting.proxytype).place(x=5,y=37)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Socket Type", font=("Roboto", 12)).place(x=150,y=35)
      ctk.CTkButton(modules_frame, text="Select File", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: proxy_load()).place(x=5,y=70)
      ctk.CTkEntry(modules_frame, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=70)
      ctk.CTkLabel(modules_frame, bg_color=c1, fg_color=c4, text_color="#fff", text="", width=150, height=20, textvariable=Setting.proxy_filenameLabel).place(x=85,y=70)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=67)

      tk.Label(modules_frame, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=100)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Total: 000", font=("Roboto", 12), textvariable=Setting.totalProxiesLabel).place(x=10,y=125)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Valid: 000", font=("Roboto", 12), textvariable=Setting.validProxiesLabel).place(x=10,y=145)
      tk.Label(modules_frame, bg=c1, fg="#fff", text="Invalid: 000", font=("Roboto", 12), textvariable=Setting.invalidProxiesLabel).place(x=10,y=165)

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

      printl("debug", "Open Settings Tab")
    if num2 == 2:
      tk.Label(module_frame, text="TwoCoin Github: ", bg=c1, fg="#4D8387", font=("Roboto", 12)).place(x=10,y=10)
      link01 = tk.Label(module_frame, text="GitHub link", bg=c1, fg="#fff", font=("Roboto", 12))
      link01.place(x=140,y=10)
      link01.bind("<Button-1>", lambda e:webbrowser.open_new("https://github.com/NyaShinn1204/TwoCoinRaider"))
      tk.Label(module_frame, text="TwoCoin discord: ", bg=c1, fg="#4D8387", font=("Roboto", 12)).place(x=10,y=35)
      link02 = tk.Label(module_frame, text="Discord invite link", bg=c1, fg="#fff", font=("Roboto", 12))
      link02.place(x=140,y=35)
      link02.bind("<Button-1>", lambda e:webbrowser.open_new("https://discord.gg/ntra"))
      tk.Label(module_frame, text="TwoCoin version: ", bg=c1, fg="#4D8387", font=("Roboto", 12)).place(x=10,y=60)
      tk.Label(module_frame, text=version, bg=c1, fg="#fff", font=("Roboto", 12)).place(x=140,y=60)

      printl("debug", "Open Abouts Tab")

def set_moduleframe_scroll(num1, num2):
  global spam_message, reply_message
  frame_scroll = module_frame = ctk.CTkScrollableFrame(root, width=970, height=660)
  module_frame.place(x=270, y=20)
  module_frame.configure(fg_color=c1)
  clear_frame(frame_scroll)
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
              print("[~] Checking API Key: " + apis)
              if answers == "1":
                if solver.get_balance_capsolver(apis) == 0.0:
                  Setting.bypass_cap.set(False)
              if answers == "2":
                if solver.get_balance_capmonster(apis) == 0.0:
                  Setting.bypass_cap.set(False)
              if answers == "3":
                if solver.get_balance_2cap(apis) == 0.0:
                  Setting.bypass_cap.set(False)
          else:
            print("[-] Not Set. Please Input")
            Setting.bypass_cap.set(False)

      # Joiner Frame
      modules_frame01_01 = ctk.CTkFrame(module_frame, width=350, height=300, border_width=1, border_color=c3, fg_color=c1)
      modules_frame01_01.grid(row=0, column=0, padx=12, pady=12)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Joiner", font=("Roboto", 14)).place(x=10,y=2)
      ctk.CTkCheckBox(modules_frame01_01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, text="Bypass MemberScreen", variable=Setting.bypass_ms).place(x=5,y=31)
      ctk.CTkCheckBox(modules_frame01_01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, text="Bypass hCaptcha", variable=Setting.bypass_cap, command=hcaptcha_select).place(x=5,y=55) 
      ctk.CTkCheckBox(modules_frame01_01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, text="Delete Join Message", variable=Setting.delete_join_ms).place(x=150,y=55) 
      ctk.CTkButton(modules_frame01_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry01_01).place(x=5,y=84) #40
      ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_link).place(x=85,y=84)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Invite Link", font=("Roboto", 12)).place(x=240,y=82) #38
      ctk.CTkButton(modules_frame01_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry01_02).place(x=5,y=113)
      ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_serverid).place(x=85,y=113)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=111)
      ctk.CTkButton(modules_frame01_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry01_03).place(x=5,y=142)
      ctk.CTkEntry(modules_frame01_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.joiner_channelid).place(x=85,y=142)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=140)
      
      def slider_event01(value):
        tk.Label(modules_frame01_01, bg=c1, fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=205,y=164)

      ctk.CTkSlider(modules_frame01_01, from_=0.1, to=3.0, variable=Setting.delay01, command=slider_event01).place(x=5,y=169)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text=round(Setting.delay01.get(),1), font=("Roboto", 12)).place(x=205,y=164)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=164)

      ctk.CTkButton(modules_frame01_01, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(1_1_1)).place(x=5,y=190)
      ctk.CTkButton(modules_frame01_01, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(1_1_2)).place(x=70,y=190)

      tk.Label(modules_frame01_01, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=220)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.suc_joiner_Label, font=("Roboto", 12)).place(x=10,y=248)
      tk.Label(modules_frame01_01, bg=c1, fg="#fff", textvariable=Setting.fai_joiner_Label, font=("Roboto", 12)).place(x=10,y=273)

      # Leaver Frame
      modules_frame01_02 = ctk.CTkFrame(module_frame, width=350, height=200, border_width=1, border_color=c3, fg_color=c1)
      modules_frame01_02.grid(row=0, column=1, padx=12, pady=12)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", text="Leaver", font=("Roboto", 14)).place(x=10,y=2)
      ctk.CTkButton(modules_frame01_02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry02_01).place(x=5,y=33)
      ctk.CTkEntry(modules_frame01_02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.leaver_serverid).place(x=85,y=33)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=31)

      def slider_event02(value):
        tk.Label(module_frame, bg=c1, fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=605,y=75)

      ctk.CTkSlider(modules_frame01_02, from_=0.1, to=3.0, variable=Setting.delay02, command=slider_event02).place(x=5,y=60)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", text=round(Setting.delay02.get(),1), font=("Roboto", 12)).place(x=205,y=55)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=55)

      ctk.CTkButton(modules_frame01_02, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(1_2_1)).place(x=5,y=80)
      ctk.CTkButton(modules_frame01_02, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(1_2_2)).place(x=70,y=80)

      tk.Label(modules_frame01_02, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=110)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", textvariable=Setting.suc_leaver_Label, font=("Roboto", 12)).place(x=10,y=135)
      tk.Label(modules_frame01_02, bg=c1, fg="#fff", textvariable=Setting.fai_leaver_Label, font=("Roboto", 12)).place(x=10,y=155)

      # VC Joiner Frame
      modules_frame01_03 = ctk.CTkFrame(module_frame, width=350, height=175, border_width=1, border_color=c3, fg_color=c1)
      modules_frame01_03.grid(row=1, column=0, padx=12, pady=12)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="VC Joiner", font=("Roboto", 14)).place(x=10,y=2)
      ctk.CTkButton(modules_frame01_03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry03_01).place(x=5,y=28)
      ctk.CTkEntry(modules_frame01_03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcjoin_serverid).place(x=85,y=28)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=26)
      ctk.CTkButton(modules_frame01_03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry03_02).place(x=5,y=57)
      ctk.CTkEntry(modules_frame01_03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcjoin_channelid).place(x=85,y=57)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=55)

      ctk.CTkButton(modules_frame01_03, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_6_1)).place(x=5,y=88)

      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=81)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", textvariable=Setting.suc_vcjoiner_Label, font=("Roboto", 12)).place(x=140,y=106)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", textvariable=Setting.fai_vcjoiner_Label, font=("Roboto", 12)).place(x=140,y=131)

      # VC Leaver Frame
      modules_frame01_03 = ctk.CTkFrame(module_frame, width=350, height=175, border_width=1, border_color=c3, fg_color=c1)
      modules_frame01_03.grid(row=1, column=1, padx=12, pady=12)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="VC Leaver", font=("Roboto", 14)).place(x=10,y=2)
      ctk.CTkButton(modules_frame01_03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry04_01).place(x=5,y=28)
      ctk.CTkEntry(modules_frame01_03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcleave_serverid).place(x=85,y=28)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=26)
      ctk.CTkButton(modules_frame01_03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry04_02).place(x=5,y=57)
      ctk.CTkEntry(modules_frame01_03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcleave_channelid).place(x=85,y=57)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=55)
       
      ctk.CTkButton(modules_frame01_03, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_6_1)).place(x=5,y=88)

      tk.Label(modules_frame01_03, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=81)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", textvariable=Setting.suc_vcleaver_Label, font=("Roboto", 12)).place(x=140,y=106)
      tk.Label(modules_frame01_03, bg=c1, fg="#fff", textvariable=Setting.fai_vcleaver_Label, font=("Roboto", 12)).place(x=140,y=131)
            
      printl("debug", "Open Join Leave Tab")

    if num2 == 2: # Spammer Tab
      # Spammer
      modules_frame02_01 = ctk.CTkFrame(module_frame, width=400, height=300, border_width=1, border_color=c3, fg_color=c1)
      modules_frame02_01.grid(row=0, column=0, padx=12, pady=12)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text="Spammer", font=("Roboto", 12)).place(x=10,y=2)
      ctk.CTkCheckBox(modules_frame02_01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allping ,text="All Ping").place(x=5,y=26)
      ctk.CTkCheckBox(modules_frame02_01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_allch ,text="All Ch").place(x=5,y=48)
      ctk.CTkCheckBox(modules_frame02_01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_rdstring ,text="Random String").place(x=5,y=70)
      ctk.CTkCheckBox(modules_frame02_01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_ratefixer ,text="RateLimitFixer").place(x=5,y=92)
      ctk.CTkCheckBox(modules_frame02_01, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.spam_randomconvert ,text="RandomConvert").place(x=150,y=92)
      ctk.CTkButton(modules_frame02_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry04).place(x=5,y=121)
      ctk.CTkEntry(modules_frame02_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.spam_serverid).place(x=85,y=121)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=119)
      ctk.CTkButton(modules_frame02_01, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry05).place(x=5,y=150)
      ctk.CTkEntry(modules_frame02_01, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.spam_channelid).place(x=85,y=150)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=148)

      def slider_event11(value):
        tk.Label(modules_frame02_01, bg=c1, fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=205,y=172)
      
      ctk.CTkSlider(modules_frame02_01, from_=0.1, to=3.0, variable=Setting.delay03, command=slider_event11).place(x=5,y=177)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text=round(Setting.delay03.get(),1), font=("Roboto", 12)).place(x=205,y=172)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=170)
       
      spam_message = ctk.CTkTextbox(modules_frame02_01, bg_color=c1, fg_color=c4, text_color="#fff", width=150, height=60)
      spam_message.place(x=120,y=26)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text="Message", font=("Roboto", 12)).place(x=275,y=40)
        
      ctk.CTkButton(modules_frame02_01, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_3_1)).place(x=5,y=197)
      ctk.CTkButton(modules_frame02_01, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_3_2)).place(x=70,y=197)

      tk.Label(modules_frame02_01, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=190)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", textvariable=Setting.suc_nmspam_Label, font=("Roboto", 12)).place(x=140,y=215)
      tk.Label(modules_frame02_01, bg=c1, fg="#fff", textvariable=Setting.fai_nmspam_Label, font=("Roboto", 12)).place(x=140,y=235)

      # Reply Spam
      modules_frame02_02 = ctk.CTkFrame(module_frame, width=400, height=300, border_width=1, border_color=c3, fg_color=c1)
      modules_frame02_02.grid(row=0, column=1, padx=12, pady=12)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Reply", font=("Roboto", 12)).place(x=10,y=2)
      ctk.CTkCheckBox(modules_frame02_02, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_allping ,text="All Ping").place(x=5,y=26)
      ctk.CTkCheckBox(modules_frame02_02, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_allmg ,text="All Mg").place(x=5,y=48)
      ctk.CTkCheckBox(modules_frame02_02, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_rdstring ,text="Random String").place(x=5,y=70)
      ctk.CTkCheckBox(modules_frame02_02, bg_color=c1, text_color="#fff", border_color=c3, checkbox_width=20, checkbox_height=20, hover=False, border_width=3, variable=Setting.reply_ratefixer ,text="RateLimitFixer").place(x=5,y=92)
      
      ctk.CTkButton(modules_frame02_02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry06).place(x=5,y=121)
      ctk.CTkEntry(modules_frame02_02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reply_serverid).place(x=85,y=121)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=119)
      
      ctk.CTkButton(modules_frame02_02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry07).place(x=5,y=150)
      ctk.CTkEntry(modules_frame02_02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reply_channelid).place(x=85,y=150)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=148)
      
      ctk.CTkButton(modules_frame02_02, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry08).place(x=5,y=179)
      ctk.CTkEntry(modules_frame02_02, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reply_messageid).place(x=85,y=179)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Message ID", font=("Roboto", 12)).place(x=240,y=177)
      
      def slider_event12(value):
        tk.Label(modules_frame02_02, bg=c1, fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=208,y=201)
      
      ctk.CTkSlider(modules_frame02_02, from_=0.1, to=3.0, variable=Setting.delay04, command=slider_event12).place(x=5,y=204)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text=round(Setting.delay04.get(),1), font=("Roboto", 12)).place(x=208,y=201)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=199)
      
      reply_message = ctk.CTkTextbox(modules_frame02_02, bg_color=c1, fg_color=c4, text_color="#fff", width=150, height=60)
      reply_message.place(x=120,y=26)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Message", font=("Roboto", 12)).place(x=275,y=40)

      ctk.CTkButton(modules_frame02_02, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_5_1)).place(x=5,y=224)
      ctk.CTkButton(modules_frame02_02, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_5_2)).place(x=70,y=224)

      tk.Label(modules_frame02_02, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=217)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", textvariable=Setting.suc_replyspam_Label, font=("Roboto", 12)).place(x=140,y=242)
      tk.Label(modules_frame02_02, bg=c1, fg="#fff", textvariable=Setting.fai_replyspam_Label, font=("Roboto", 12)).place(x=140,y=262)

      # Ticket Spam
      modules_frame02_04 = ctk.CTkFrame(module_frame, width=400, height=200, border_width=1, border_color=c3, fg_color=c1)
      modules_frame02_04.grid(row=1, column=0, padx=12, pady=12)
      tk.Label(modules_frame02_04, bg=c1, fg="#fff", text="Ticket Spammer", font=("Roboto", 12)).place(x=10,y=2)
      ctk.CTkButton(modules_frame02_04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry15).place(x=5,y=28)
      ctk.CTkEntry(modules_frame02_04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.ticket_serverid).place(x=85,y=28)
      tk.Label(modules_frame02_04, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=26)
      ctk.CTkButton(modules_frame02_04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry16).place(x=5,y=57)
      ctk.CTkEntry(modules_frame02_04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.ticket_channelid).place(x=85,y=57)
      tk.Label(modules_frame02_04, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=55)
      ctk.CTkButton(modules_frame02_04, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry17).place(x=5,y=86)
      ctk.CTkEntry(modules_frame02_04, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.ticket_messageid).place(x=85,y=86)
      tk.Label(modules_frame02_04, bg=c1, fg="#fff", text="Message ID", font=("Roboto", 12)).place(x=240,y=84)

      ctk.CTkButton(modules_frame02_04, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_6_1)).place(x=5,y=117)
      ctk.CTkButton(modules_frame02_04, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_6_2)).place(x=70,y=117)

      tk.Label(modules_frame02_04, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=110)
      tk.Label(modules_frame02_04, bg=c1, fg="#fff", textvariable=Setting.suc_ticketspam_Label, font=("Roboto", 12)).place(x=140,y=135)
      tk.Label(modules_frame02_04, bg=c1, fg="#fff", textvariable=Setting.fai_ticketspam_Label, font=("Roboto", 12)).place(x=140,y=160)

      # VC Spam
      modules_frame02_03 = ctk.CTkFrame(module_frame, width=400, height=200, border_width=1, border_color=c3, fg_color=c1)
      modules_frame02_03.grid(row=1, column=1, padx=12, pady=12)
      tk.Label(modules_frame02_03, bg=c1, fg="#fff", text="VC Spammer", font=("Roboto", 12)).place(x=10,y=2)
      ctk.CTkButton(modules_frame02_03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry11).place(x=5,y=28)
      ctk.CTkEntry(modules_frame02_03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcspam_serverid).place(x=85,y=28)
      tk.Label(modules_frame02_03, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=26)
      ctk.CTkButton(modules_frame02_03, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry12).place(x=5,y=57)
      ctk.CTkEntry(modules_frame02_03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.vcspam_channelid).place(x=85,y=57)
      tk.Label(modules_frame02_03, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=55)
      ctk.CTkButton(modules_frame02_03, text="Select File", fg_color=c2, hover_color=c5, width=75, height=25, command=lambda: voice_load()).place(x=5,y=86)
      ctk.CTkEntry(modules_frame02_03, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, state="disabled").place(x=85,y=86)
      ctk.CTkLabel(modules_frame02_03, bg_color=c1, fg_color=c4, text_color="#fff", text="", width=150, height=20, textvariable=Setting.voicefile_filenameLabel).place(x=85,y=86)
      tk.Label(modules_frame02_03, bg=c1, fg="#fff", text="File Name", font=("Roboto", 12)).place(x=240,y=84)

      ctk.CTkButton(modules_frame02_03, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_4_1)).place(x=5,y=117)

      tk.Label(modules_frame02_03, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=110)
      tk.Label(modules_frame02_03, bg=c1, fg="#fff", textvariable=Setting.suc_vcspam_Label, font=("Roboto", 12)).place(x=140,y=135)
      tk.Label(modules_frame02_03, bg=c1, fg="#fff", textvariable=Setting.fai_vcspam_Label, font=("Roboto", 12)).place(x=140,y=160)

      # Slash Spam
      modules_frame02_05 = ctk.CTkFrame(module_frame, width=400, height=300, border_width=1, border_color=c3, fg_color=c1)
      modules_frame02_05.grid(row=2, column=0, padx=12, pady=12)
      tk.Label(modules_frame02_05, bg=c1, fg="#fff", text="Slash Spammer", font=("Roboto", 12)).place(x=10,y=2)
      ctk.CTkButton(modules_frame02_05, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry18).place(x=5,y=28)
      ctk.CTkEntry(modules_frame02_05, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_serverid).place(x=85,y=28)
      tk.Label(modules_frame02_05, bg=c1, fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=26)
      ctk.CTkButton(modules_frame02_05, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry19).place(x=5,y=57)
      ctk.CTkEntry(modules_frame02_05, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_channelid).place(x=85,y=57)
      tk.Label(modules_frame02_05, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=55)
      ctk.CTkButton(modules_frame02_05, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry20).place(x=5,y=86)
      ctk.CTkEntry(modules_frame02_05, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_applicationid).place(x=85,y=86)
      tk.Label(modules_frame02_05, bg=c1, fg="#fff", text="Application ID", font=("Roboto", 12)).place(x=240,y=84)
      ctk.CTkButton(modules_frame02_05, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry21).place(x=5,y=115)
      ctk.CTkEntry(modules_frame02_05, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_commandname).place(x=85,y=115)
      tk.Label(modules_frame02_05, bg=c1, fg="#fff", text="Command Name", font=("Roboto", 12)).place(x=240,y=113)
      ctk.CTkButton(modules_frame02_05, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry22).place(x=5,y=144)
      ctk.CTkEntry(modules_frame02_05, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_subcommandname).place(x=85,y=144)
      tk.Label(modules_frame02_05, bg=c1, fg="#fff", text="SubCommand Name", font=("Roboto", 12)).place(x=240,y=142)
      ctk.CTkButton(modules_frame02_05, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry23).place(x=5,y=173)
      ctk.CTkEntry(modules_frame02_05, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.slash_subcommandname_value).place(x=85,y=173)
      tk.Label(modules_frame02_05, bg=c1, fg="#fff", text="SubCommand Value", font=("Roboto", 12)).place(x=240,y=171)

      def slider_event13(value):
        tk.Label(modules_frame02_05, bg=c1, fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=208,y=200)
      
      ctk.CTkSlider(modules_frame02_05, from_=0.1, to=3.0, variable=Setting.delay05, command=slider_event13).place(x=5,y=205)
      tk.Label(modules_frame02_05, bg=c1, fg="#fff", text=round(Setting.delay05.get(),1), font=("Roboto", 12)).place(x=208,y=200)
      tk.Label(modules_frame02_05, bg=c1, fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=198)

      ctk.CTkButton(modules_frame02_05, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_7_1)).place(x=5,y=225)
      ctk.CTkButton(modules_frame02_05, text="Stop", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_7_2)).place(x=70,y=225)

      tk.Label(modules_frame02_05, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=135,y=218)
      tk.Label(modules_frame02_05, bg=c1, fg="#fff", textvariable=Setting.suc_shspam_Label, font=("Roboto", 12)).place(x=140,y=243)
      tk.Label(modules_frame02_05, bg=c1, fg="#fff", textvariable=Setting.fai_shspam_Label, font=("Roboto", 12)).place(x=140,y=268)

      # Reaction Spam & Soon Module
      modules_frame02_06 = ctk.CTkFrame(module_frame, width=400, height=300, fg_color=c1)
      modules_frame02_06.grid(row=2, column=1, padx=12, pady=12)
      # Reaction
      modules_frame02_07 = ctk.CTkFrame(modules_frame02_06, width=400, height=195, border_width=1, border_color=c3, fg_color=c1)
      modules_frame02_07.grid(row=0, pady=5)
      tk.Label(modules_frame02_07, bg=c1, fg="#fff", text="Reaction Spammer", font=("Roboto", 12)).place(x=10,y=2)
      ctk.CTkButton(modules_frame02_07, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry24).place(x=5,y=28)
      ctk.CTkEntry(modules_frame02_07, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reaction_channelid).place(x=85,y=28)
      tk.Label(modules_frame02_07, bg=c1, fg="#fff", text="Channel ID", font=("Roboto", 12)).place(x=240,y=26)
      ctk.CTkButton(modules_frame02_07, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry25).place(x=5,y=57)
      ctk.CTkEntry(modules_frame02_07, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reaction_messageid).place(x=85,y=57)
      tk.Label(modules_frame02_07, bg=c1, fg="#fff", text="Message ID", font=("Roboto", 12)).place(x=240,y=55)
      ctk.CTkButton(modules_frame02_07, text="Clear        ", fg_color=c2, hover_color=c5, width=75, height=25, command=clear_entry26).place(x=5,y=86)
      ctk.CTkEntry(modules_frame02_07, bg_color=c1, fg_color=c4, border_color=c4, text_color="#fff", width=150, height=20, textvariable=Setting.reaction_emoji).place(x=85,y=86)
      tk.Label(modules_frame02_07, bg=c1, fg="#fff", text="Emoji  e.x. :skull:", font=("Roboto", 12)).place(x=240,y=84)
      
      ctk.CTkButton(modules_frame02_07, text="Start", fg_color=c2, hover_color=c5, border_width=1, border_color=c3, width=60, height=25, command=lambda: module_thread(2_8_1)).place(x=5,y=117)

      tk.Label(modules_frame02_07, bg=c1, fg="#fff", text="Status", font=("Roboto", 12)).place(x=70,y=110)
      tk.Label(modules_frame02_07, bg=c1, fg="#fff", textvariable=Setting.suc_reactionspam_Label, font=("Roboto", 12)).place(x=75,y=135)
      tk.Label(modules_frame02_07, bg=c1, fg="#fff", textvariable=Setting.fai_reactionspam_Label, font=("Roboto", 12)).place(x=75,y=160)
      
      # Soon
      modules_frame02_08 = ctk.CTkFrame(modules_frame02_06, width=400, height=95, border_width=1, border_color=c3, fg_color=c1)
      modules_frame02_08.grid(row=1, pady=5)
      tk.Label(modules_frame02_08, bg=c1, fg="#fff", text="Soon Module", font=("Roboto", 12)).place(x=10,y=2)
      tk.Label(modules_frame02_08, bg=c1, fg="#fff", text="Release For v1.0.3β", font=("Roboto", 12)).place(x=10,y=20)

      printl("debug", "Open Spam Tab")
      
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
config_check()
printl("debug", "Loading Tkinter")

tk.Label(bg="#142326", width=35, height=720).place(x=0,y=0)

ctk.CTkLabel(master=root, bg_color="#142326", text="", image=ctk.CTkImage(Image.open("data/coin.png"),size=(80, 80))).place(x=20,y=20)
tk.Label(bg="#142326", text="Two Coin", fg="#fff", font=("Roboto", 20)).place(x=100,y=10)
tk.Label(bg="#142326", text="Raider", fg="#fff", font=("Roboto", 20)).place(x=160,y=40)
tk.Label(bg="#142326", text=version, fg="#F8F8F8", font=("Roboto", 18)).place(x=100,y=70)

modulelist = ctk.CTkFrame(master=root, width=250, height=500, border_width=0, bg_color="#142326", fg_color="#142326")
modulelist.place(x=0,y=100)

ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="Joiner / Leaver", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe_scroll(1, 1),anchor=tk.W).place(x=20,y=20)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="Spammer", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe_scroll(1, 2),anchor=tk.W).place(x=20,y=60)
ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="Setting", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 1),anchor=tk.W).place(x=20,y=620)
ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="About", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 2),anchor=tk.W).place(x=20,y=660)

set_moduleframe(2, 2)

root.mainloop()

# Todo:
# Rewrite Gui Code
# Rewrite Module Code
# Reset Ticker Spammer Gui&Code