from tkinter import ttk
from tkinter import *

win = Tk()

win.geometry("750x250")

def displat():
    global entry
    str = entry.get()
    label.configure(text=str)



entry = Entry(win, width=40)
entry.focus_set()
entry.pack()

label = Label(win, text="", font=("Courier 22 bold"))
label.pack()

ttk.Button(win, text="Okay", width=20, command= displat).pack(pady=20)
win.mainloop()