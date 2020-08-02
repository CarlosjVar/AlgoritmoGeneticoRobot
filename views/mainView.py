from tkinter import *


class MainView:

    def __init__(self, root_window):
        self.main_container = Frame(root_window)
        self.main_container.grid(row=0, column=0)
        self.test_btn = Button(self.main_container, text="Hello World", padx=6, pady=4)
        self.test_btn.grid(row=0, column=0)
