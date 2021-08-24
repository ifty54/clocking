# clocking
from tkinter import *
from tkinter.ttk import *

from time import strftime
#creating UI
root = Tk()
root.title("Tick Tock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("DS-DIGI", 80), background = "black", foreground = "blue")
label.pack(anchor='center')
time()

mainloop()
