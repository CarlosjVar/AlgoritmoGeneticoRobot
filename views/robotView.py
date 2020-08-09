from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from PIL import ImageTk, Image
class robotView:
    def __init__(self,root_window,robot):
        root_window.geometry("500x500")
        self.main_container = Frame(root_window)
        self.main_container.grid(row=0, column=0)
        self.info_container = Frame(root_window)
        self.info_container.grid(row=1, column=0)
        self.comportamiento_container = Frame(root_window)
        self.comportamiento_container.grid(row=2,column=0)
        self.labelPrincipal = Label(self.main_container,text="Información del robot",justify=CENTER)
        self.labelPrincipal.grid(row=0,column=0)
        self.labelBateria = Label(self.info_container,text="Bateria: "+str(robot.bateria.capacidadMaxima))
        self.labelBateria.grid(row=0,column=1)
        self.labelBateriaRestante = Label(self.info_container,text="Motor tipo: "+str(robot.motor.potencia))
        self.labelBateriaRestante.grid(row=0,column=2)
        self.labelMotor = Label(self.info_container,text="Camara tipo: "+str(robot.camara.tipo_camara))
        self.labelMotor.grid(row=1,column=1)
        self.labelCamara = Label(self.info_container,text="Fitness: ")
        self.labelCamara.grid(row=1,column=2)
        self.labelDistancia = Label(self.info_container,text="Fitness: ")
        self.labelDistancia.grid(row=2,column=1)
        self.labelDistanciaRec = Label(self.info_container,text="Fitness: ")
        self.labelDistanciaRec.grid(row=2,column=2)
        labelComp = Label(self.comportamiento_container,text="Comportamientos")
        labelComp.grid(row= 0,column=0)

        self.container_porcenajes=Frame(self.comportamiento_container)
        self.container_porcenajes.grid(row=1,column=0)
        for i in range(len(robot.comportamiento.comportamiento)):
            for o in range(len(robot.comportamiento.comportamiento[i])):
                labelComportamiento = Label(self.container_porcenajes,text=str(int(robot.comportamiento.comportamiento[i][o]*100)))
                labelComportamiento.grid(row=i,column=o)


