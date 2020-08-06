import random

import numpy as np
from operator import itemgetter
from helpers import flip
from models.Robot import Robot
indiceMutacion= 3
objetivo = (0,19)
class Geneticos:
    def __init__(self):
        self.valores_Fitness = []
        self.promedioFitness = 0
        self.newGen=[]
    #TODO: AGREGAR FITNESS BASADO EN TIEMPO
    def fitnessGeneracion(self,robots):
        for robot in robots:
            self.fitness(robot)
        fitnessValores=[]
        for dic in self.valores_Fitness:
            fitnessValores.append(dic["Fitness"])
        self.promedioFitness=np.average(fitnessValores)
        sumaValores=np.sum(fitnessValores)
        for dic in self.valores_Fitness :
            dic["Normalizado"] = dic["Fitness"]/sumaValores
        listSorted= sorted(self.valores_Fitness,key=itemgetter("Fitness"),reverse=True)
        for i in range(5):
            robot
            self.newGen.append(listSorted[i]["Robot"])
        while len(self.newGen)<10:
            self.cruce()
        print(len(self.newGen))


    def fitness(self,robot):
        distancia = self.distancia_Al_Objetivo(robot)
        fitDist = self.fitness_Distancia(distancia)
        fitTravelled = self.fitness_Travelled(robot.distanciaRecorrida)
        fitHardw=self.fitness_Hardware(robot)
        fitBatt=self.fitness_Battery(robot.bateria)
        fitCost=self.fitness_CostoRecorrido(robot.costoRecorrido)
        robFitness= {}
        robFitness["Robot"] = robot
        robFitness["Fitness"] = fitDist+fitTravelled+fitHardw+fitBatt+fitCost
        print("FitnessDist",fitDist,"\n Fitness Recorrido",fitTravelled,"\n Fitness Hard",fitHardw,"Fitness Bateria",fitBatt,"\nFitness costo",fitCost,"\n Recorrí" ,
              robot.distanciaRecorrida, "\n Usos de la camara",robot.usosCamara,"\n Costo de usar la camara",robot.camara.consumo,"Watts","\n Usos del motor",robot.usosMotor)
        self.valores_Fitness.append(robFitness)
    def cruce(self):
        padre=0
        madre=0
        while padre==0:
            for robot in self.valores_Fitness:
                if(flip(robot["Normalizado"])):
                    padre=robot["Robot"]
        while madre==0:
            for robot in self.valores_Fitness:
                if(flip(robot["Normalizado"])):
                    if not (robot["Robot"].id == padre.id):
                        madre=robot["Robot"]
        robotcin = Robot(padre,madre)
        self.newGen.append(robotcin)


        pass
    def distancia_Al_Objetivo(self, robot):
        return (objetivo[0] + robot.posicionActual[0]) + (objetivo[1] - robot.posicionActual[1])
    def fitness_Distancia(self,distancia):
        if distancia==0:
            return 90
        return 80//distancia
    #TODO: Analizar caso spawn cercano al objetivo
    def fitness_CostoRecorrido(self,costoRecorrido):
        return 1300//costoRecorrido

    #TODO: Analizar caso spawn cercano al objetivo
    def fitness_Travelled(self,travelledDist):
        return 1100//travelledDist
    def fitness_Hardware(self,robot):
        return 1100//(robot.motor.costo+robot.camara.costo+robot.bateria.costo)
    def fitness_Battery(self,bateria):
        if(bateria.tipo_Bateria==1):
            return bateria.capacidad//10
        elif(bateria.tipo_Bateria==2):
            return  bateria.capacidad//15
        elif(bateria.tipo_Bateria==3):
            return  bateria.capacidad//20


def Realizar_Siguiente_Accion(robot,terreno):
    campos_Vision = robot.revisar_Alrededor()
    accion = robot.accion(campos_Vision,terreno)
    robot.ultimaAccion = accion[0]
    #accion = [ACCION,DIRECCION(DE SER NECESARIO)]
    if accion[0] == 0:
        if robot.posicionActual[1] == 0:
            pass
        elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]-1]:
            robot.activo=False
        else:
            robot.mover_Izquierda(terreno[robot.posicionActual[0]][robot.posicionActual[1]])

            robot.costoRecorrido+=terreno[robot.posicionActual[0]][robot.posicionActual[1]+1]
    elif accion[0]  == 1:
        if robot.posicionActual[1] == 19:
            pass
        elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]+1]:
            robot.activo=False
        else:
            robot.mover_Derecha(terreno[robot.posicionActual[0]][robot.posicionActual[1]])

            robot.costoRecorrido+=terreno[robot.posicionActual[0]][robot.posicionActual[1]-1]
    elif accion[0]  == 2:
        if robot.posicionActual[0] == 0:
            pass
        elif robot.motor.potencia < terreno[robot.posicionActual[0]-1][robot.posicionActual[1]]:
            robot.activo = False

        else:
            robot.mover_Adelante(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
            robot.costoRecorrido+=terreno[robot.posicionActual[0]+1][robot.posicionActual[1]]
    elif accion[0]  == 3 or accion[0] == 4:
        if accion[1] == "Norte":
            if robot.posicionActual[0] == 0:
                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0] - 1][robot.posicionActual[1]]:
                robot.activo = False
            else:
                robot.mover_Adelante(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido += terreno[robot.posicionActual[0] + 1][robot.posicionActual[1]]
        elif accion[1] == "Oeste":
            if robot.posicionActual[1] == 0:
                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1] - 1]:
                robot.activo=False
            else:
                robot.mover_Izquierda(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido += terreno[robot.posicionActual[0]][robot.posicionActual[1] + 1]
        elif accion[1] == "Este":
            if robot.posicionActual[1] == 19:
                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1] + 1]:
                robot.activo=False
            else:
                robot.mover_Derecha(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido+=terreno[robot.posicionActual[0]][robot.posicionActual[1]-1]
        #MOVER AL SUR
        else:
            if robot.posicionActual[0] == 19 :

                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0]+1][robot.posicionActual[1]]:
                robot.activo=False
            else:
                robot.mover_Atras(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido += terreno[robot.posicionActual[0] - 1][robot.posicionActual[1]]
    # DIRECCIÓN AL OBJETIVO
    elif accion[0] == 5:
        #Norte
        if robot.posicionActual[0] > objetivo[0]:
            robot.mover_Adelante(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
            robot.costoRecorrido += terreno[robot.posicionActual[0] + 1][robot.posicionActual[1]]
        #Sur
        elif robot.posicionActual[0] < objetivo[0]:
            robot.mover_Atras(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
            robot.costoRecorrido += terreno[robot.posicionActual[0] - 1][robot.posicionActual[1]]
        #Oeste
        elif robot.posicionActual[1] > objetivo[1]:
            robot.mover_Izquierda(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
            robot.costoRecorrido += terreno[robot.posicionActual[0]][robot.posicionActual[1] + 1]
        #Este
        elif robot.posicionActual[1] < objetivo[1]:
            robot.mover_Derecha(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
            robot.costoRecorrido += terreno[robot.posicionActual[0]][robot.posicionActual[1]-1]



    #Robot agotó su batería , por tanto se desactiva
    if (robot.bateria.capacidad<=0):
        robot.bateria.capacidad=0
        robot.activo=False
        robot.completado=True
    #Robot llegó a su destino , por tanto cesa sus funciones
    if(robot.posicionActual[0] == objetivo[0] and robot.posicionActual[1] == objetivo[1] ):
        print("Robot en objetivo")
        robot.completado=True
        robot.activo=False
def get_poblacion_activa(generacion):
    poblacionActiva = []
    for robot in generacion:
        if (robot.activo) :
            poblacionActiva.append(robot)
        elif not robot.completado :
            poblacionActiva.append(robot)
    return poblacionActiva

def crearNuevaGen(generacion):
    gen = Geneticos()
    gen.fitnessGeneracion(generacion)
    return [gen.promedioFitness,gen.newGen]


