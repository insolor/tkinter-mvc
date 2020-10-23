# -*- coding:UTF-8 -*-
__author__ = 'lilei'

import tkinter as tk

class View(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        tk.Label(self, text='My Money', font='14').pack(side='left')
        self.moneyCtrl = tk.Label(self, font='14')
        self.moneyCtrl.pack(side='left', padx=10, pady=10)

class ChangerWidget(tk.Toplevel):
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.addButton = tk.Button(self, text='Add', width=8)
        self.addButton.pack(side='left')
        self.removeButton = tk.Button(self, text='Remove', width=8)
        self.removeButton.pack(side='left')
