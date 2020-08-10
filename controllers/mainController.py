import tkinter
from views.mainView import MainView
from models.Robot import Robot
from helpers import cargar_terreno
from genetics import get_poblacion_activa, crearNuevaGen, realizar_siguiente_accion
from views.robotView import robotView


class MainController:
    generacionActual= []
    generacionesPasadas = []

    def __init__(self):
        self.root = tkinter.Tk()
        self.terreno = cargar_terreno()
        self.main_view = MainView(self.root, self.terreno)
        self.generacion_elegida = []
        # Set event listeners
        self.main_view.iniciar_btn.bind("<Button-1>", self.iniciar_busqueda_camino)
        self.main_view.search_generation_btn.bind("<Button-1>", self.buscar_generacion)
        self.main_view.search_robot_btn.bind("<Button-1>",self.buscar_robot)
    def run(self):
        self.root.title("Path finder robot")
        self.root.mainloop()

    def iniciar_busqueda_camino(self,event):
        for i in range(10):
            self.generacionActual.append(Robot())
        fitness = 0
        while fitness < 100:

            poblacioActiva = get_poblacion_activa(self.generacionActual)
            if len(poblacioActiva) == 0:
                self.main_view.reiniciar()
                robotcompletado=False
                for rob in self.generacionActual:
                    self.main_view.updateImg(rob.posicionActual)
                    if(self.main_view.checkbox_value.get()):
                        if(rob.completado):
                            robotcompletado=True
                            break
                        pass
                if robotcompletado:
                    break
                self.generacionesPasadas.append(self.generacionActual)
                resultadosCruce = crearNuevaGen(self.generacionActual)
                fitness = resultadosCruce[0]
                self.generacionActual = resultadosCruce[1]
                if fitness <100:
                    for robot in self.generacionActual:
                        robot.reinicarStats()
            for rob in poblacioActiva:
                realizar_siguiente_accion(rob, self.terreno)
        # Set fitness label
        print(fitness)
        self.main_view.generation_fitness_label.config(text="Fitness: " + str(fitness))
        o=0
        for robot in self.generacionActual:
            if robot.completado:
                o+=1
        print("Llegaron ",o)
        print(len(self.generacionesPasadas))
        self.main_view.generation_number_label.config(text="Generaciones: " + str(len(self.generacionesPasadas)))

    def buscar_generacion(self, event):
        # Get generation value
        generation_number = int(self.main_view.generation_input_field.get())
        # Validate input
        # TODO: Validar que la entrada solo sean numeros
        if generation_number > len(self.generacionesPasadas) or generation_number == 0:
            self.main_view.show_error_message("Numero de generacion fuera de rango")
            return
        # Get generation and show robots
        self.generation_elegida = self.generacionesPasadas[generation_number - 1]
        self.main_view.reiniciar()
        for robot in self.generation_elegida:
            self.main_view.updateImg(robot.posicionActual)
        self.main_view.search_robot_btn["state"]='normal'
    def buscar_robot(self,event):
        rootRobot = tkinter.Toplevel()
        rootRobot.title("Información del robot")
        indiceRobot=int(self.main_view.robot_input_combo.get())-1
        robot = self.generation_elegida[indiceRobot]
        viewRobot = robotView(rootRobot,robot,self.terreno)
        rootRobot.mainloop()
        viewRobot.botonPadre.bind("<Button-1>",self.buscar_Robot_Parent())


        pass


    def mostrarRobots(self):
        for rob in self.generacionActual:
            self.main_view.updateImg(rob.posicionActual)