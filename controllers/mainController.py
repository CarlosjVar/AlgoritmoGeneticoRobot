import tkinter
from views.mainView import MainView
from models.Robot import Robot
from helpers import cargar_terreno
from genetics import get_poblacion_activa, crearNuevaGen, realizar_siguiente_accion


class MainController:
    generacionActual= []
    generacionesPasadas = [[]]

    def __init__(self):
        self.root = tkinter.Tk()
        self.terreno = cargar_terreno()
        self.main_view = MainView(self.root, self.terreno)
        self.main_view.iniciar_btn.bind("<Button-1>", self.iniciar_busqueda_camino)

    def run(self):
        self.root.title("Path finder robot")
        self.root.mainloop()

    def iniciar_busqueda_camino(self,event):
        for i in range(10):
            self.generacionActual.append(Robot())
        fitness = 0
        while fitness < 175:
            poblacioActiva = get_poblacion_activa(self.generacionActual)
            if len(poblacioActiva) == 0:
                for rob in self.generacionActual:
                    # self.main_view.updateImg(rob.posicionActual)
                    pass
                self.generacionesPasadas.append(self.generacionActual)
                resultadosCruce = crearNuevaGen(self.generacionActual)
                fitness = resultadosCruce[0]
                self.generacionActual = resultadosCruce[1]
            for rob in poblacioActiva:
                realizar_siguiente_accion(rob, self.terreno)
        # Set fitness label
        print(fitness)
        self.main_view.generation_fitness_label.config(text="Fitness: " + str(fitness))
        for robot in self.generacionActual:
            robot.reinicarStats()
        poblacioActiva = get_poblacion_activa(self.generacionActual)
        while len(poblacioActiva) > 0:
            poblacioActiva = get_poblacion_activa(self.generacionActual)
            for rob in poblacioActiva:
                realizar_siguiente_accion(rob, self.terreno)
        for robot in self.generacionActual:
            self.main_view.updateImg(robot.posicionActual)
        # Set generations number
        print(len(self.generacionesPasadas))
        self.main_view.generation_number_label.config(text="Generaciones: " + str(len(self.generacionesPasadas)))


    def mostrarRobots(self):
        for rob in self.generacionActual:
            self.main_view.updateImg(rob.posicionActual)