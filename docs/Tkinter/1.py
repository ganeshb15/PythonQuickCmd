from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox as mb
from tkinter import filedialog
from tkinter.filedialog import askopenfile



root = Tk() 
root.title("TitleName")
root.geometry('200x200') 


RedScale = Scale(root, from_=0, to=255,orient=HORIZONTAL)
RedScale.pack()
RedScale.place(x=0,y=0)

mainloop()

#RedScale.get()
