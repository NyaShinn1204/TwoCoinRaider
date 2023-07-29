import subprocess
import tkinter as tk
import customtkinter as ctk
from PIL import Image

root = tk.Tk()
root.geometry("1280x720")
root.resizable(0, 0)
root.title("TwoCoinRaider")
root.configure(bg="#213A3E")

join_delay = tk.DoubleVar()
join_delay.set(0.1)

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
  frame = module_frame = ctk.CTkFrame(root, width=990, height=680)
  module_frame.place(x=270, y=20)
  module_frame.configure(fg_color="#28464B")
  clear_frame(frame)
  if num1 == 1:
    if num2 == 1:
      # Joiner Frame
      def slider_event01(value):
        tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(value,1), font=("Roboto", 12)).place(x=205,y=35)
      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=175, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.place(x=20,y=20)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="Joiner", font=("Roboto", 14)).place(x=35,y=4)
      ctk.CTkCheckBox(module_setting_frame, bg_color="#28464B", text_color="#fff", border_color="#C0C0C0", checkbox_width=20, checkbox_height=20, hover=False, border_width=3, text="Bypass MemberScreen").place(x=5,y=11)
      ctk.CTkSlider(module_setting_frame, from_=0.1, to=3.0, variable=join_delay, command=slider_event01).place(x=5,y=40)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text=round(join_delay.get(),1), font=("Roboto", 12)).place(x=205,y=35)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Delay", font=("Roboto", 12)).place(x=240,y=35)
      
      ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60).place(x=5,y=60)
      ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60).place(x=70,y=60)
      
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=90)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Success: 000", font=("Roboto", 12)).place(x=10,y=115)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Failed: 000", font=("Roboto", 12)).place(x=10,y=135)
      
      
      # Leaver Frame
      module_setting_frame = ctk.CTkFrame(module_frame, width=350, height=175, border_width=1, border_color="#C0C0C0", fg_color="#28464B")
      module_setting_frame.place(x=400,y=20)
      tk.Label(module_frame, bg="#28464B", fg="#fff", text="Leaver", font=("Roboto", 14)).place(x=415,y=4)
      
      ctk.CTkButton(module_setting_frame, text="Start", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60).place(x=5,y=60)
      ctk.CTkButton(module_setting_frame, text="Stop", fg_color="#25747D", hover_color="#2C8C99", border_width=1, border_color="#C0C0C0", width=60).place(x=70,y=60)
      
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Status", font=("Roboto", 12)).place(x=5,y=90)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Success: 000", font=("Roboto", 12)).place(x=10,y=115)
      tk.Label(module_setting_frame, bg="#28464B", fg="#fff", text="Failed: 000", font=("Roboto", 12)).place(x=10,y=135)
      
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
print("Loading....")

tk.Label(bg="#142326", width=35, height=720).place(x=0,y=0)

ctk.CTkLabel(master=root, bg_color="#142326", text="", image=ctk.CTkImage(Image.open("data/coin.png"),size=(80, 80))).place(x=20,y=20)
tk.Label(bg="#142326", text="Two Coin", fg="#fff", font=("Roboto", 20)).place(x=100,y=10)
tk.Label(bg="#142326", text="Raider", fg="#fff", font=("Roboto", 20)).place(x=160,y=40)
tk.Label(bg="#142326", text="v1.0.0", fg="#F8F8F8", font=("Roboto", 18)).place(x=100,y=70)

ctk.CTkButton(master=root, fg_color="#28464B", hover_color="#2C8C99", text="Joiner / Leaver", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(1, 1)).place(x=20,y=120)
ctk.CTkButton(master=root, image=ctk.CTkImage(Image.open("data/info.png"),size=(25, 25)), compound="left", fg_color="#28464B", hover_color="#2C8C99", text="About", width=210, height=35, font=("Roboto", 18, "normal"), command= lambda: set_moduleframe(2, 1)).place(x=20,y=660)

root.mainloop()