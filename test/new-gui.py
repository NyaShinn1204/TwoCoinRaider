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

colorama.init(autoreset=True)

version = "v1.0.3β"

c1 = "#28464B"
c2 = "#25747D"
c3 = "#C0C0C0"
c4 = "#275258"
c5 = "#2C8C99"

root = tk.Tk()
root.geometry("1280x720")
#root.resizable(0, 0)
root.title("TwoCoinRaider | "+version)
root.iconbitmap(default="data/favicon.ico")
root.configure(bg="#213A3E")


tk.Label(bg="#142326", width=32, height=720).place(x=0,y=0)
tk.Label(bg="#142326", text="TWOCOIN RAIDER", fg="#fff", font=("Carlito", 20, "bold")).place(x=13,y=25)
#ctk.CTkLabel(master=root, bg_color="#142326", text="", image=ctk.CTkImage(Image.open("data/coin.png"),size=(80, 80))).place(x=20,y=20)
#tk.Label(bg="#142326", text="Two Coin", fg="#fff", font=("Roboto", 20)).place(x=100,y=10)
#tk.Label(bg="#142326", text="Raider", fg="#fff", font=("Roboto", 20)).place(x=160,y=40)
#tk.Label(bg="#142326", text=version, fg="#F8F8F8", font=("Roboto", 18)).place(x=100,y=70)

modulelist = ctk.CTkFrame(master=root, width=230, height=720, border_width=0, bg_color="#fff", fg_color="#fff")
modulelist.place(x=0,y=100)
#ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="Joiner / Leaver", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe_scroll(1, 1),anchor=tk.W).place(x=20,y=20)
#ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="Spammer", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe_scroll(1, 2),anchor=tk.W).place(x=20,y=60)
#ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="Setting", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 1),anchor=tk.W).place(x=20,y=620)
#ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color=c1, bg_color="#142326", hover_color=c5, text="About", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 2),anchor=tk.W).place(x=20,y=660)

root.mainloop()