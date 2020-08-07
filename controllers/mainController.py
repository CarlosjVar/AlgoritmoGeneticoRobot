import tkinter
import threading
import time
from views.mainView import MainView
from helpers import cargar_terreno
from models.Robot import Robot
from models.Geneticos import get_poblacion_activa,crearNuevaGen,Realizar_Siguiente_Accion
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
            self.generacionActual.append(Robot())
        # Setup de los threads
        fitness = 0
        # for individuo in self.generacionActual:
        #     for com in individuo.comportamiento.comportamiento:
        #         print(com)
        #     print("\n")
        while fitness < 170:
            poblacioActiva = get_poblacion_activa(self.generacionActual)
            if (len(poblacioActiva) == 0):
                for rob in self.generacionActual:
                    self.main_view.updateImg(rob.posicionActual)
                self.generacionesPasadas.append(self.generacionActual)
                resultadosCruce = crearNuevaGen(self.generacionActual)
                fitness = resultadosCruce[0]
                self.generacionActual = resultadosCruce[1]
            for rob in poblacioActiva:
                Realizar_Siguiente_Accion(rob, self.terreno)
        print(fitness)
        for robot in self.generacionActual:
            robot.reinicarStats()
        poblacioActiva = get_poblacion_activa(self.generacionActual)
        for rob in poblacioActiva:
            Realizar_Siguiente_Accion(rob, self.terreno)

    def mostrarRobots(self):
        for rob in self.generacionActual:
            self.main_view.updateImg(rob.posicionActual)