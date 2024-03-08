from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()

st.title("Shutdown")
st.geometry("500x500")
st.resizable(height=False, width=False)
st.config(bg="#040D12")
st_Button = Button(st, text = "Restart", font = ("Time New Roman", 30,), relief = RAISED, command=restart)
st_Button.place(x = 150, y = 100, height = 80, width = 200 )

st_Button = Button(st, text = "Shutdown", font = ("Time New Roman", 30,), relief = RAISED, command=shutdown)
st_Button.place(x = 150, y = 300, height = 80, width = 200 )

st.mainloop() 