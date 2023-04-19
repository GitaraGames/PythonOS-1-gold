from main import *
from tkinter import *
from tkinter import Listbox
import os

app = App()
window = app.window()

lb = Listbox(window)
lb.place(x=0, y=25, width=280, height=250)

for file in os.listdir(r'files/'):
    lb.insert(END, os.path.join(r'files/', file))

window.configure(width=300, height=284)