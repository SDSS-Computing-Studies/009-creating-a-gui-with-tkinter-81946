#python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("320x50")
#-----------------------------


entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=10)

label1 = tk.Label(window,text="X")

entry2 = tk.Entry(window,text="Entry widgets can be typed in", width=10)

button1 = tk.Button(window,text="=")

entry3 = tk.Entry(window,text="Entry widgets can be typed in", width=25)
#----------------------------
entry1.pack(side=LEFT)
label1.pack(side=LEFT)
entry2.pack(side=LEFT)
button1.pack(side=LEFT)
entry3.pack(side=LEFT)

window.mainloop()