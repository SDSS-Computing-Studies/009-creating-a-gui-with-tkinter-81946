#python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterniary Clinic Database")
window.resizable(False,False)
#-------------------------------

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto, borderwidth=3, relief=SUNKEN)

button1 = tk.Button(window,text="Search by Name")

entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=20)

label2 = tk.Label(window,text="Client Database")

label3 = tk.Label(window,text="Name")
label4 = tk.Label(window,text="Type")
label5 = tk.Label(window,text="Breed")
label6 = tk.Label(window,text="Owner")
label7 = tk.Label(window,text="Birthdate")

entry2 = tk.Entry(window,text="Dog Info", width=10)
entry3 = tk.Entry(window,text="Dog Info", width=10)
entry4 = tk.Entry(window,text="Dog Info", width=10)
entry5 = tk.Entry(window,text="Dog Info", width=10)
entry6 = tk.Entry(window,text="Dog Info", width=10)

button2 = tk.Button(window,text="<Previous")
button3 = tk.Button(window,text="Save Entry", borderwidth=3, relief=SUNKEN)
button4 = tk.Button(window,text="Next>")







#---------------------------
label1.grid(row = 1, column = 1)
label2.grid(row = 4, column = 5)


label3.grid(row = 6, column = 1)
label4.grid(row = 6, column = 4)
label5.grid(row = 6, column = 5)
label6.grid(row = 6, column = 7)
label7.grid(row = 6, column = 9)

entry2.grid(row = 7, column = 1)
entry3.grid(row = 7, column = 4)
entry4.grid(row = 7, column = 5)
entry5.grid(row = 7, column = 7)
entry6.grid(row = 7, column = 9)

button2.grid(row = 8, column = 1)
button3.grid(row = 8, column = 5)
button4.grid(row = 8, column = 9)

button1.grid(row = 1, column = 9)
entry1.grid(row = 1, column = 10)



window.mainloop()