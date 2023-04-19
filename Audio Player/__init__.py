import main
from tkinter import *
import pygame

def play():
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()

file = 'audio_kalimba.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Audio Player/audio_kalimba.mp3")

app = main.App()
window = app.window()
text = Label(window, text="Music Player")
text.place(x=0, y=25)

btn = Button(window, text="Play", command=play)
btn.place(x=0, y=50, width=200, height=25)
btn2 = Button(window, text="Stop", command=stop)
btn2.place(x=0, y=75, width=200, height=25)

window.configure(width=200, height=120)