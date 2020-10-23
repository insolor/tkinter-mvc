# -*- coding:UTF-8 -*-
__author__ = 'lilei'

if __name__ == '__main__':
    import tkinter as tk
    from controllers.MainController import Controller

    root = tk.Tk()
    root.withdraw()
    app = Controller(root)
    root.mainloop()

