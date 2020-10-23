# -*- coding:UTF-8 -*-
__author__ = 'lilei'

from typing import Any, Callable

import tkinter as tk


def wrap_into_property(variable_getter: Callable[[Any], tk.Variable]):
    return property(lambda self: variable_getter(self).get(),
                    lambda self, value: variable_getter(self).set(value))


class MainModel:
    def __init__(self):
        self.my_money_var = tk.IntVar()

    my_money = wrap_into_property(lambda self: self.my_money_var)
