import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk, Image

from models.Geneticos import Geneticos


class robotView:
    def __init__(self,root_window,robot,terreno):
        root_window.geometry("430x260")
        self.robotActual = robot
        self.main_container = Frame(root_window)
        self.main_container.grid(row=0, column=0)
        self.info_container = Frame(root_window)
        self.info_container.grid(row=1, column=0)
        self.map_container = Frame(root_window)
        self.map_container.grid(row=0,column=1,rowspan=3)
        self.comportamiento_container = Frame(root_window)
        self.comportamiento_container.grid(row=2,column=0)
        self.robot_input_group = Frame(root_window)
        self.robot_input_group.grid(row=3,column=0,columnspan = 3)
        self.labelPrincipal = Label(self.main_container,text="Información del robot",justify=CENTER)
        self.labelPrincipal.grid(row=0,column=0)
        self.labelBateria = Label(self.info_container,text="Bateria: "+str(robot.bateria.capacidadMaxima))
        self.labelBateria.grid(row=0,column=1)
        self.labelBateriaRestante = Label(self.info_container,text="Bateria restante: "+str(robot.bateria.capacidad))
        self.labelBateriaRestante.grid(row=0,column=2)
        self.labelMotor = Label(self.info_container,text="Motor tipo: "+str(robot.motor.potencia))
        self.labelMotor.grid(row=1,column=1)
        self.labelCamara = Label(self.info_container,text="Camara tipo: "+str(robot.camara.tipo_camara))
        self.labelCamara.grid(row=1,column=2)
        self.labelObjetivo = Label(self.info_container,text="Llegó al objetivo: " + "Si" if robot.completado else "Llegó al objetivo: "+"No")
        self.labelObjetivo.grid(row=2,column=1)
        gen= Geneticos()
        fitness = gen.fitnessbruto(robot)
        self.labelFitness = Label(self.info_container,text="Fitness: "+str(fitness))
        self.labelFitness.grid(row=2,column=2)
        labelComp = Label(self.comportamiento_container,text="Comportamientos")
        labelComp.grid(row= 0,column=0)
        #Setup botones padre
        self.botonPadre = Button(self.robot_input_group,text="Buscar padre")
        self.botonPadre.grid(row=0,column=0)
        self.botonMadre = Button(self.robot_input_group,text="Buscar padre")
        self.botonMadre.grid(row=0,column=1)
        #Setup grid comportamientos
        self.container_porcenajes=Frame(self.comportamiento_container)
        self.container_porcenajes.grid(row=1,column=0)
        for i in range(len(robot.comportamiento.comportamiento)):
            for o in range(len(robot.comportamiento.comportamiento[i])):
                labelComportamiento = Label(self.container_porcenajes,text=str(int(robot.comportamiento.comportamiento[i][o]*100)))
                labelComportamiento.grid(row=i,column=o)

        self.terrenoStored = terreno
        # Cargar imagenes
        self.terreno_normal = ImageTk.PhotoImage(Image.open("assets/normal2.png"))
        self.terreno_moderado = ImageTk.PhotoImage(Image.open("assets/moderado2.png"))
        self.terreno_dificil = ImageTk.PhotoImage(Image.open("assets/dificil2.png"))
        self.terreno_bloqueado = ImageTk.PhotoImage(Image.open("assets/bloqueado2.png"))
        self.robot = ImageTk.PhotoImage(Image.open("assets/robot2.png"))
        # Display del terreno
        self.terrain_grid = [[0 for j in range(20)] for i in range(20)]
        self.terrain_img_grid = [[0 for j in range(20)] for i in range(20)]
        for fila_terreno in range(20):
            for bloque in range(20):
                if self.terrenoStored[fila_terreno][bloque] == 1:
                    bloque_canvas = Canvas(self.map_container, width=10, height=10, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_normal, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas
                elif self.terrenoStored[fila_terreno][bloque] == 2:
                    bloque_canvas = Canvas(self.map_container, width=10, height=10, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_moderado, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas
                elif self.terrenoStored[fila_terreno][bloque] == 3:
                    bloque_canvas = Canvas(self.map_container, width=10, height=10, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_dificil, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas
                else:
                    bloque_canvas = Canvas(self.map_container, width=10, height=10, highlightthickness=0)
                    bloque_canvas.grid(row=fila_terreno, column=bloque)
                    # Guardar referencia en terrain_grid
                    self.terrain_img_grid[fila_terreno][bloque] = bloque_canvas.create_image(0, 0, image=self.terreno_bloqueado, anchor=NW)
                    self.terrain_grid[fila_terreno][bloque] = bloque_canvas
        for grid in robot.recorrido:
            self.terrain_grid[grid[0]][grid[1]].itemconfig(
                self.terrain_img_grid[grid[0]][grid[1]], image=self.robot)
        #Bind botones
        self.botonPadre.bind("<Button-1>", self.buscar_Robot_Padre)
        self.botonMadre.bind("<Button-1>", self.buscar_Robot_Madre)
    def buscar_Robot_Padre(self,event):
        rootRobot = tkinter.Toplevel()
        rootRobot.title("Información del robot")
        viewRobot = robotView(rootRobot, self.robotActual.padres[0], self.terrenoStored)
        rootRobot.mainloop()
        self.botonPadre.bind("<Button-1>", self.buscar_Robot_Padre)
        self.botonMadre.bind("<Button-1>", self.buscar_Robot_Madre)

    def buscar_Robot_Madre(self, event):
        rootRobot = tkinter.Toplevel()
        rootRobot.title("Información del robot")
        viewRobot = robotView(rootRobot, self.robotActual.padres[1], self.terrenoStored)
        rootRobot.mainloop()
        self.botonPadre.bind("<Button-1>", self.buscar_Robot_Padre)
        self.botonMadre.bind("<Button-1>", self.buscar_Robot_Madre)
