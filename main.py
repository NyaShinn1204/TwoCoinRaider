import subprocess
import tkinter as tk
import customtkinter as ctk
from PIL import Image

def get_hwid():
    cmd = 'wmic csproduct get uuid'
    uuid = str(subprocess.check_output(cmd))
    pos1 = uuid.find("\\n")+2
    uuid = uuid[pos1:-15]
    return uuid

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def set_moduleframe(num1, num2):
  frame = module_frame = ctk.CTkFrame(root, width=1010, height=700)
  module_frame.place(x=260, y=10)
  module_frame.configure(fg_color="#28464B")
  clear_frame(frame)
  if num1 == 1:
    if num2 == 1:
      print("1-1")
  if num1 == 2:
    if num2 == 1:
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
print("[+] Loading....")

root = tk.Tk()
root.geometry("1280x720")
root.resizable(0, 0)
root.title("TwoCoinRaider")
root.configure(bg="#213A3E")

tk.Label(bg="#142326", width=35, height=720).place(x=0,y=0)

ctk.CTkLabel(master=root, bg_color="#142326", text="", image=ctk.CTkImage(Image.open("data/coin.png"),size=(80, 80))).place(x=20,y=20)
tk.Label(bg="#142326", text="Two Coin", fg="#fff", font=("Roboto", 20)).place(x=100,y=10)
tk.Label(bg="#142326", text="Raider", fg="#fff", font=("Roboto", 20)).place(x=160,y=40)
tk.Label(bg="#142326", text="v1.0.0", fg="#F8F8F8", font=("Roboto", 18)).place(x=100,y=70)

ctk.CTkButton(master=root, fg_color="#28464B", hover_color="#2C8C99", text="Joiner / Leaver", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(1, 1)).place(x=20,y=120)
ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color="#28464B", hover_color="#2C8C99", text="About", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 1)).place(x=20,y=660)

root.mainloop()