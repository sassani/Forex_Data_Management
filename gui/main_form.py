import os
import sys
import json
# import requests as req
# import pandas as pd
# import numpy as np

ROOT = os.getcwd()
sys.path.append(ROOT)

import tkinter as tk


class MainForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.dialog = tk.Button(self, text="Open", fg="green", command=self.open_dialog)
        self.dialog.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def open_dialog(self):
        print("OPEN DIALOG!!")
        pass


    # def show(self):
root = tk.Tk()
app = MainForm(master=root)
app.mainloop()