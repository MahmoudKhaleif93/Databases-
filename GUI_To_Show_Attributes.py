from tkinter import *
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
import guizero 

window = Tk()


window.title("Welcome to Testing Department")
window.geometry('700x700')
menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='New project')
lbl = Label(window,text="Project name",font = "Helvetica 16 bold italic")
lbl.grid(column=1, row=20)
txt = Entry(window,width=30)
txt.grid(column=2, row=20)
lbl1 = Label(window, text="software version",font = "Helvetica 16 bold italic")
lbl1.grid(column=1, row=30)
txt1 = Entry(window,width=30)
txt1.grid(column=2, row=30)
lbl2 = Label(window, text="number of process",font = "Helvetica 16 bold italic")
lbl2.grid(column=1, row=40)
txt2 = Entry(window,width=30)
txt2.grid(column=2, row=40)
def clicked():
    #root=Tk()
    print ("gggg",txt.get())
    Window1=tk.Toplevel(window)
    
    
Button= Button(window,text="enter",bg='blue',command=clicked).place(x=500 , y=30)
Button.grid(column=40,row=10).place(x=500 , y=30)
Button.pack()
    
    
    
#new_item.add_separator()

new_item.add_command(label='Edit')
new_item.add_command(label='Save')
new_item.add_command(label='Exit')
menu.add_cascade(label='File', menu=new_item)



window.config(menu=menu)

window.mainloop()

