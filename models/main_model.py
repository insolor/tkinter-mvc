import tkinter as tk

from .tk_variable_descriptors import tk_variable


class MainModel:
    my_money_var, my_money = tk_variable(tk.IntVar)
