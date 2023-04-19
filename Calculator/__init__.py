import main
from tkinter import *

app = main.App()
window = app.window()

array = []
x = 0
y = 80

z = 40

task = ""

def c0():
    global task, task_text
    task += "0"
    task_text.configure(text=task)
def c1():
    global task, task_text
    task += "1"
    task_text.configure(text=task)
def c2():
    global task, task_text
    task += "2"
    task_text.configure(text=task)
def c3():
    global task, task_text
    task += "3"
    task_text.configure(text=task)
def c4():
    global task, task_text
    task += "4"
    task_text.configure(text=task)
def c5():
    global task, task_text
    task += "5"
    task_text.configure(text=task)
def c6():
    global task, task_text
    task += "6"
    task_text.configure(text=task)
def c7():
    global task, task_text
    task += "7"
    task_text.configure(text=task)
def c8():
    global task, task_text
    task += "8"
    task_text.configure(text=task)
def c9():
    global task, task_text
    task += "9"
    task_text.configure(text=task)

def cp():
    global task, task_text
    task += "+"
    task_text.configure(text=task)
def cm():
    global task, task_text
    task += "-"
    task_text.configure(text=task)
def cu():
    global task, task_text
    task += "*"
    task_text.configure(text=task)
def cd():
    global task, task_text
    task += "/"
    task_text.configure(text=task)

def result():
    global task
    try:
        task = str(eval(task))
        task_text.configure(text=task)
    except:
        pass
def delete():
    global task
    task = task[:-1]
    task_text.configure(text=task)
def clear():
    global task
    task = ""
    task_text.configure(text=task)

def dot():
    global task
    task += "."
    task_text.configure(text=task)

buttons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '=', 'C', '<', '.']
buttons_comm = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, cp, cm, cu, cd, result, clear, delete, dot]

task_text = Label(window, text="")
task_text.place(x=0, y=40, width=200)

for i in range(len(buttons)):
    array.append(Button(window, text=buttons[i], command=buttons_comm[i]))
    array[i].place(x=x, y=y, width=z, height=z)
    if x != z*3:
        x += z
    else:
        x = 0
        y += z

window.configure(width=200, height=284)