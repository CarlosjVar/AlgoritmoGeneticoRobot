import tkinter
from views.mainView import MainView
from helpers import cargar_terreno

class MainController:

    def __init__(self):
        self.root = tkinter.Tk()
        self.terreno = cargar_terreno()
        self.main_view = MainView(self.root, self.terreno)

    def run(self):
        self.root.title("Path finder robot")
        self.root.mainloop()
