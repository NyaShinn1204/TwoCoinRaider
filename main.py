import subprocess
import tkinter as tk
import customtkinter as ctk
from customtkinter import *
from PIL import Image
import threading
import os

import module.token_checker as token_checker
import module.leaver as module_leaver

root = tk.Tk()
root.geometry("1280x720")
root.resizable(0, 0)
root.title("TwoCoinRaider")
root.configure(bg="#213A3E")

class Setting:
  tokens = []
  validtoken = 0
  invalidtoken = 0
  
  token_filenameLabel = tk.StringVar()
  token_filenameLabel.set("")
  totaltokenLabel = tk.StringVar()
  totaltokenLabel.set("Total: 000")
  validtokenLabel = tk.StringVar()
  validtokenLabel.set("Valid: 000")
  invalidtokenLabel = tk.StringVar()
  invalidtokenLabel.set("Invalid: 000")
  
  suc_leaver_Label = tk.StringVar()
  suc_leaver_Label.set("Success: 000")
  fai_leaver_Label = tk.StringVar()
  fai_leaver_Label.set("Failed: 000")
  
  delay01 = tk.DoubleVar()
  delay01.set(0.1)
  delay02 = tk.DoubleVar()
  delay02.set(0.1)
  
class SettingVariable:
  leaverresult_success = 0
  leaverresult_failed = 0

def get_hwid():
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n")+2
    uuid = uuid[pos1:-15]
    return uuid

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def module_thread(num):
  tokens = Setting.tokens
  print(tokens)
  if num == 2_1:
    serverid = leaver_serverid.get()
    delay = Setting.delay02.get()
    
    threading.Thread(target=module_leaver.start, args=(serverid, delay, tokens)).start()
  
  if num == 2_2:
    threading.Thread(target=module_leaver.stop).start()

def module_status(num1, num2):
  if num1 == 2:
    if num2 == 1:
      SettingVariable.leaverresult_success +=1
      Setting.suc_leaver_Label.set("Success: "+str(SettingVariable.leaverresult_success).zfill(3))
    if num2 == 2:
      SettingVariable.leaverresult_failed +=1
      Setting.fai_leaver_Label.set("Failed: "+str(SettingVariable.leaverresult_failed).zfill(3))
    
    
def set_moduleframe(num1, num2):
  global joiner_link,leaver_serverid
  frame = module_frame = ctk.CTkFrame(root, width=990, height=680)
  module_frame.place(x=270, y=20)
  module_frame.configure(fg_color="#28464B")
  clear_frame(frame)
  if num1 == 1:
    if num2 == 1:
      # Joiner Frame
      def slider_event01(value):
        tk.Label(module_frame, bg="#28464B", fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=225,y=55)
      def slider_event02(value):
        tk.Label(module_frame, bg="#28464B", fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=605,y=55)
      def clear_entry01():
        joiner_link.delete(0,tk.END)
      def clear_entry02():
        leaver_serverid.delete(0,tk.END)
      
      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=200, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.place(x=20,y=20)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="Joiner", font=("Roboto", 14)).place(x=35,y=4)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, text="Bypass MemberScreen").place(x=5,y=11)
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry01).place(x=5,y=40)
      joiner_link = ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20)
      joiner_link.place(x=85,y=40)  #27
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Invite Link", font=("Roboto", 12)).place(x=240,y=38)
      ctk.CTkSlider(module_setting_frame, from_=0.1, to=3.0, variable=Setting.delay01, command=slider_event01).place(x=5,y=67)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(Setting.delay01.get(),1), font=("Roboto", 12)).place(x=205,y=62)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=62)
      
      ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(1_1)).place(x=5,y=87)
      ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(1_2)).place(x=70,y=87)
      
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=117)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Success: 000", font=("Roboto", 12)).place(x=10,y=142)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Failed: 000", font=("Roboto", 12)).place(x=10,y=162)
      
      
      # Leaver Frame
      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=175, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.place(x=400,y=20)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="Leaver", font=("Roboto", 14)).place(x=415,y=4)
      ctk.CTkButton(module_setting_frame, text="Clear        ", fg_color="#25747D", hover_color="#2C8C99", width=75, height=25, command=clear_entry02).place(x=5,y=13)
      leaver_serverid = ctk.CTkEntry(module_setting_frame, bg_color="#28464B", fg_color="#275258", border_color="#275258", text_color="#fff", width=150, height=20)
      leaver_serverid.place(x=85,y=13)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Server ID", font=("Roboto", 12)).place(x=240,y=11)
      ctk.CTkSlider(module_setting_frame, from_=0.1, to=3.0, variable=Setting.delay02, command=slider_event02).place(x=5,y=40)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(Setting.delay02.get(),1), font=("Roboto", 12)).place(x=205,y=35)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=35)
      
      ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(2_1)).place(x=5,y=60)
      ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60, height=25, command=lambda: module_thread(2_2)).place(x=70,y=60)
      
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=90)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable="Success: 000", font=("Roboto", 12)).place(x=10,y=115)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", textvariable="Failed: 000", font=("Roboto", 12)).place(x=10,y=135)
      
      print("1-1")
  if num1 == 2:
    def token_load():
      fTyp = [("", "*.txt")]
      iFile = os.path.abspath(os.path.dirname(__file__))
      filepath = filedialog.askopenfilename(
          filetype=fTyp, initialdir=iFile, title="Select Tokens")
      if filepath == "":
          return
      tokens = open(filepath, 'r').read().splitlines()
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
    if num2 == 1:
      print("2-1")
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
    if num2 == 2:
      print("2-2")

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
-----------------------""")
print("Loading....")

tk.Label(bg="#142326", width=35, height=720).place(x=0,y=0)

ctk.CTkLabel(master=root, bg_color="#142326", text="", image=ctk.CTkImage(Image.open("data/coin.png"),size=(80, 80))).place(x=20,y=20)
tk.Label(bg="#142326", text="Two Coin", fg="#fff", font=("Roboto", 20)).place(x=100,y=10)
tk.Label(bg="#142326", text="Raider", fg="#fff", font=("Roboto", 20)).place(x=160,y=40)
tk.Label(bg="#142326", text="v1.0.0", fg="#F8F8F8", font=("Roboto", 18)).place(x=100,y=70)

ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(25, 25)), compound="left", fg_color="#28464B", bg_color="#142326", hover_color="#2C8C99", text="Joiner / Leaver           ", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(1, 1)).place(x=20,y=120)
ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color="#28464B", bg_color="#142326", hover_color="#2C8C99", text="Setting                          ", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 1)).place(x=20,y=620)
ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color="#28464B", bg_color="#142326", hover_color="#2C8C99", text="About                            ", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 2)).place(x=20,y=660)

root.mainloop()