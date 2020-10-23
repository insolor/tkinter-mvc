# -*- coding:UTF-8 -*-
__author__ = 'lilei'

from models import MainModel
from views import MainView, ChangerView


class MainController:
    def __init__(self, root):
        self.model = MainModel()
        self.main_view = MainView(root)
        self.main_view.money_ctrl.config(textvariable=self.model.my_money_var)
        self.changer_view = ChangerView(self.main_view)
        self.changer_view.add_button.config(command=self.add_money)
        self.changer_view.remove_button.config(command=self.remove_money)

    def add_money(self):
        self.model.my_money += 10

    def remove_money(self):
        self.model.my_money -= 10
