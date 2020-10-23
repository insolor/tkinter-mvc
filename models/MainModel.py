# -*- coding:UTF-8 -*-
__author__ = 'lilei'

import tkinter as tk

class Model:
    def __init__(self):
        self.myMoney = tk.IntVar()

    def addMoney(self, value):
        self.myMoney.set(self.myMoney.get() + value)

    def removeMoney(self, value):
        self.myMoney.set(self.myMoney.get() - value)