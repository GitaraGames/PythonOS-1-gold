import main
from tkinter import *

app = main.MainMenu()
window = app.window()

# Notepad
button_notepad = Button(window, text="Notepad", command=lambda:exec(open("Notepad/__init__.py", "r").read()))
button_notepad.pack()
# Music Player
button_music = Button(window, text="Audio Player", command=lambda:exec(open("Audio Player/__init__.py", "r").read()))
button_music.pack()
# Calculator
button_calculator = Button(window, text="Calculator", command=lambda:exec(open("Calculator/__init__.py", "r").read()))
button_calculator.pack()
# Exploer
button_exploer = Button(window, text="Exploer", command=lambda:exec(open("Exploer/__init__.py", "r").read()))
button_exploer.pack()

button_shutdown = Button(window, text="Shutdown", command=lambda:exit())
button_shutdown.pack()