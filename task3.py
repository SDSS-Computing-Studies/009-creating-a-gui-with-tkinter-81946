#python3

import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("280x135")
#-------------------------------------------
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)

label2 = tk.Label(window,text = "Pochacco!")

label3 = tk.Label(window,text="A cuddly little puppy! This is from the same creators \n who brought you Keropi and Kero Kero", bg="#50FFFA")





#-----------------------------------
label1.place(x=100,y=0)
label2.place(x=180,y=50)
label3.place(x=0,y=100)







#-----------------------------------
window.mainloop()