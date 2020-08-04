import tkinter
from views.mainView import MainView
from helpers import cargar_terreno
from models.Robot import Robot

class MainController:
    generacionActual= []
    generacionesPasadas=[[]]
    def __init__(self):
        self.root = tkinter.Tk()
        self.terreno = cargar_terreno()
        self.main_view = MainView(self.root, self.terreno)
        self.main_view.iniciar_btn.bind("<Button-1>",self.Iniciar)

    def run(self):
        self.root.title("Path finder robot")
        self.root.mainloop()
    def Iniciar(self,event):
        for i in range(10):
            robot = Robot()
            self.generacionActual.append(robot)
        for rob in self.generacionActual:
            print(rob.motor.potencia)


