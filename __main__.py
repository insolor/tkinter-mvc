# -*- coding:UTF-8 -*-
__author__ = 'lilei'

import tkinter as tk
from controllers import MainController


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    app = MainController(root)
    root.mainloop()
