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

modulelist = ctk.CTkFrame(master=root, width=230, height=720, corner_radius=0, fg_color="#142326")
modulelist.place(x=0,y=100)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color="#142326", hover_color=c5, corner_radius=0, text="Joiner / Leaver", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=12)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color="#142326", hover_color=c5, corner_radius=0, text="Spammer", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=57)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color="#142326", hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=102)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color="#142326", hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=148)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color="#142326", hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=194)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color="#142326", hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=240)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color="#142326", hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=286)
ctk.CTkButton(master=modulelist, image=ctk.CTkImage(Image.open("data/join_leave.png"),size=(20, 20)), compound="left", fg_color="#142326", hover_color=c5, corner_radius=0, text="Soon", width=195, height=40, font=("Roboto", 16, "bold"), anchor="w").place(x=20,y=332)

root.mainloop()