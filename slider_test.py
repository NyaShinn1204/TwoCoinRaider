import customtkinter as ctk

app = ctk.CTk()
app.geometry("400x400")

def clear_frame(frame):
  for widget in frame.winfo_children():
    widget.destroy()
  frame.pack_forget()

def load_lol():
    frame_scroll = ctk.CTkFrame(app, width=250, height=250)
    frame_scroll.place(x=15, y=15)
    clear_frame(frame_scroll)
    def checkbox_event01():
        global test1_1,test1_2
        print("checkbox 01, current value:", check_var01.get())
        if check_var01.get() == "on":
            test1_1 = ctk.CTkLabel(frame_scroll, text="test1")
            test1_2 = ctk.CTkLabel(frame_scroll, text="test2")
            test1_1.place(x=checkbox01_x, y=checkbox01_y+25)
            test1_2.place(x=checkbox01_x, y=checkbox01_y+50)
            checkbox02.place(x=checkbox01_x,y=checkbox01_y+80)
        if check_var01.get() == "on" and check_var02.get() == "on":
            test2_1.place(x=checkbox02_x, y=checkbox02_y+25+40)
            test2_2.place(x=checkbox02_x, y=checkbox02_y+50+40)
        if check_var01.get() == "off":
            test1_1.destroy()
            test1_2.destroy()
            checkbox02.place(x=checkbox01_x,y=checkbox01_y+40)
        if check_var01.get() == "off" and check_var02.get() == "on":
            test2_1.place(x=checkbox02_x, y=checkbox02_y+25)
            test2_2.place(x=checkbox02_x, y=checkbox02_y+50)
    def checkbox_event02():
        global test2_1,test2_2
        print("checkbox 02, current value:", check_var02.get())
        if check_var02.get() == "on":
            test2_1 = ctk.CTkLabel(frame_scroll, text="test1")
            test2_2 = ctk.CTkLabel(frame_scroll, text="test2")
            test2_1.place(x=checkbox02_x, y=checkbox02_y+25)
            test2_2.place(x=checkbox02_x, y=checkbox02_y+50)
            #checkbox02.place(x=checkbox01_x,y=checkbox01_y+80)
        if check_var01.get() == "on" and check_var02.get() == "on":
            test2_1.place(x=checkbox02_x, y=checkbox02_y+25+40)
            test2_2.place(x=checkbox02_x, y=checkbox02_y+50+40)
        if check_var02.get() == "off":
            test2_1.destroy()
            test2_2.destroy()
            #checkbox02.place(x=checkbox01_x,y=checkbox01_y+40)

    check_var01 = ctk.StringVar(value="off")
    check_var02 = ctk.StringVar(value="off")
    checkbox01 = ctk.CTkCheckBox(frame_scroll, text="CTkCheckBox01", command=checkbox_event01,
                                         variable=check_var01, onvalue="on", offvalue="off")
    checkbox01.place(x=50,y=50)
    app.update()
    checkbox01_x = checkbox01.winfo_rootx() - frame_scroll.winfo_rootx()
    checkbox01_y = checkbox01.winfo_rooty() - frame_scroll.winfo_rooty()
    print(checkbox01_y, checkbox01_x)
    checkbox02= ctk.CTkCheckBox(frame_scroll, text="CTkCheckBox02", command=checkbox_event02,
                                         variable=check_var02, onvalue="on", offvalue="off")
    checkbox02.place(x=checkbox01_x,y=checkbox01_y+40)
    app.update()
    checkbox02_x = checkbox02.winfo_rootx() - frame_scroll.winfo_rootx()
    checkbox02_y = checkbox02.winfo_rooty() - frame_scroll.winfo_rooty()
load_lol()
app.mainloop()