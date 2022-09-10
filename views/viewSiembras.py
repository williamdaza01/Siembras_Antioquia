# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 08:45:15 2022

@author: WINDOWS 11
"""

import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Siembras Antioquia")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_749=tk.Label(root)
        GLabel_749["cursor"] = "spider"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_749["font"] = ft
        GLabel_749["fg"] = "#11e444"
        GLabel_749["justify"] = "center"
        GLabel_749["text"] = "Siembras Vigiladas por Corantioquia"
        GLabel_749.place(x=120,y=30,width=358,height=38)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
