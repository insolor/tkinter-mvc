# -*- coding:UTF-8 -*-
__author__ = 'lilei'

import tkinter as tk


class MainView(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        tk.Label(self, text='My Money', font='14').pack(side='left')
        self.money_ctrl = tk.Label(self, font='14')
        self.money_ctrl.pack(side='left', padx=10, pady=10)
