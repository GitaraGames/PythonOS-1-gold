from tkinter import *
from tkinter.scrolledtext import ScrolledText
import pygame
import os

class OS():
    def __init__(self):
        self.width = 700
        self.height = 400
        self.color = "blue"
        self.desktop_color = "blue"
        self.buttons_color = "light blue"
        self.buttons_text_color = "black"
        self.language = "en/en" # (en/en) or (ru/ru)

        self.en = ["Welcome to Python OS!", "Register user", "Restart PythonOS",
                   "Menu", "This PC"]
        self.ru = ["Добро пожаловать в Python OS!", "Регистрация пользователя",
                   "Перезагрузите PythonOS", "Меню", "Этот ПК"]
        self.lang = self.en

        self.load_settings()

        if self.language == "ru/ru":
            self.lang = self.ru

        print("OS is started...")
        self.os = Tk()
        print("Created window...")
        self.os.title('PythonOS')
        self.os.geometry('%sx%s' % (self.width, self.height))
        self.os.configure(background=self.color)
        print("Set background color...")
        self.os.resizable(False, False)

        self.user_data = self.load_user_data()

        if self.user_data == "Error!":
            self.register_intarface()
        else:
            self.enter_intarface()

    def desktop(self):
        # global objects
        global text_login1, text_pass1, btn1
        # destroy objects
        text_pass1.destroy()
        text_login1.destroy()
        btn1.destroy()

        # Start Work
        self.os.configure(background=self.desktop_color)
        self.panel = Button(self.os, bg=self.buttons_color, fg=self.buttons_text_color, state="disable")
        self.menu = Button(self.os, text=self.lang[3], bg=self.buttons_color, fg=self.buttons_text_color, command=self.menu_open)
        self.menu.place(x=0, y=0, width=self.width/4)
        self.panel.place(x=0, y=0, width=self.width)
        print('work')
        this_pc = Button(self.os, text=self.lang[4], command=self.thisPC)
        this_pc.place(x=20, y=30, width=60, height=60)

    def thisPC(self):
        app = App()
        window = app.window()

        btn = Button(window, text="Save", command=lambda: self.saveSettings(st.get("1.0", END)))
        btn.place(x=0, y=20, width=250)

        st = ScrolledText(window)
        st.place(x=0, y=40, width=250, height=160)

        file = open("system/settings.init", "r")
        commands = file.read()
        file.close()

        st.insert(INSERT, commands)

        window.configure(width=250, height=200)
    def saveSettings(self, textSet):
        file = open("system/settings.init", "w")
        file.write(textSet)
        file.close()

    def menu_open(self):
        file = open("menu/__init__.py", "r")
        exec(file.read())
        file.close()

    def load_settings(self):
        file = open("system/settings.init", "r")
        exec(file.read())
        file.close()
    def load_user_data(self):
        try:
            file = open("users/user.init", "r")
            data = file.read()
            file.close()
            return data
        except:
            return "Error!"

    def register_intarface(self):
        global text_login, text_pass, btn
        text_reg = Label(self.os, text=self.lang[1], bg=self.color, fg="white", font=("Arial", 25))
        text_login = Entry(self.os, width=25)
        text_login.place(x=self.width/2, y=self.height/2, anchor="center")
        text_pass = Entry(self.os, width=25, show="*", fg="black")
        text_pass.place(x=self.width / 2, y=self.height / 2 + 25, anchor="center")
        text_reg.place(x=self.width / 2, y=self.height / 2 - 50, anchor="center")

        btn = Button(self.os, text="OK", command=self.reg_ok, width=16, bg=self.buttons_color, fg=self.buttons_text_color, font=("Arial", 13))
        btn.place(x=self.width / 2, y=self.height / 2 + 55, anchor="center")

    def enter_intarface(self):
        global text_login1, text_pass1, btn1
        text_login1 = Entry(self.os, width=25)
        text_login1.place(x=self.width/2, y=self.height/2, anchor="center")
        text_pass1 = Entry(self.os, width=25, show="*", fg="black")
        text_pass1.place(x=self.width / 2, y=self.height / 2 + 25, anchor="center")

        btn1 = Button(self.os, text="OK", command=self.ent_ok, width=16, bg=self.buttons_color, fg=self.buttons_text_color, font=("Arial", 13))
        btn1.place(x=self.width / 2, y=self.height / 2 + 55, anchor="center")

    def reg_ok(self):
        global text_login, text_pass, btn
        if text_login.get() != "" and text_pass.get() != "":
            file = open("users/user.init", "w")
            file.write("%s %s" % (text_login.get(), text_pass.get()))
            file.close()

            btn.destroy()
            Label(self.os, text=self.lang[2], bg=self.color, fg="white", font=("Arial", 12)).place(x=self.width / 2, y=self.height / 2 + 55, anchor="center")

    def ent_ok(self):
        global text_login1, text_pass1, btn1
        res_log = "%s %s" % (text_login1.get(), text_pass1.get())
        if res_log == self.user_data:
            self.desktop()

    def mainloop(self):
        print("Welcome to PythonOS!")
        self.os.mainloop()

class App():
    def __init__(self):
        self.color = "dark blue"
        self.desktop_color = "dark blue"
        self.buttons_color = "light blue"
        self.buttons_text_color = "black"
        self.width = 700
        self.height = 400
        self.language = "en/en"  # (en/en) or (ru/ru)

        file = open("system/settings.init", "r")
        exec(file.read())
        file.close()
    def window(self):
        app_window = Frame(relief="raised", borderwidth=2)
        app_window.place(x=self.width/2, y=self.height/2, anchor="center")
        btn = Button(app_window, text="x", bg="red", command=lambda:app_window.destroy())
        btn.place(x=0, y=0)
        return app_window

class MainMenu():
    def __init__(self):
        self.color = "dark blue"
        self.desktop_color = "dark blue"
        self.buttons_color = "light blue"
        self.buttons_text_color = "black"
        self.width = 700
        self.height = 400
        self.language = "en/en"  # (en/en) or (ru/ru)

        file = open("system/settings.init", "r")
        exec(file.read())
        file.close()
    def window(self):
        app_window = Frame()
        app_window.place(x=self.width/2, y=self.height/2, anchor="center")
        btn = Button(app_window, text="x", bg="red", command=lambda:app_window.destroy())
        btn.pack()
        return app_window
    def shutdown(self):
        exit()

if __name__ == "__main__":
    PythonOS = OS()
    PythonOS.mainloop()