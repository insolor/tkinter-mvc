import tkinter as tk


class ChangerView(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.add_button = tk.Button(self, text='Add', width=8)
        self.add_button.pack(side='left')
        self.remove_button = tk.Button(self, text='Remove', width=8)
        self.remove_button.pack(side='left')
