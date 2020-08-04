import numpy as np

from models.Robot import Robot

objetivo = (0,19)
class Geneticos:
    valores_Fitness = []
    valores_Fitness_Normalizados = []
    promedioFitness = 0
    def fitnessGeneracion(self,robots):
        for robot in robots:
            self.fitness(robot)
        self.promedioFitness = np.average(self.valores_Fitness)
        sumaValores=np.sum(self.valores_Fitness)
        for valor in self.valores_Fitness:
            normalizado = valor/sumaValores
            self.valores_Fitness_Normalizados.append(normalizado)

    def fitness(self,robot):
        distancia = self.distancia_Al_Objetivo(robot)
        fitDist = self.fitness_Distancia(distancia)
        fitTravelled = self.fitness_Travelled(robot.distanciaRecorrida)
        fitHardw=self.fitness_Hardware(robot)
        fitBatt=self.fitness_Battery(robot.bateria)
        fitCost=self.fitness_CostoRecorrido(robot)
        self.valores_Fitness.append(fitDist+fitTravelled+fitHardw+fitBatt+fitCost)
    def distancia_Al_Objetivo(self, robot):
        return (objetivo[0] + robot.posicionActual[0]) + (objetivo[1] - robot.posicionActual[1])
    #Maxima distancia posible = 38
    def fitness_Distancia(self,distancia):
        if distancia==0:
            return 90
        return 80//distancia
    def fitness_CostoRecorrido(self,costoRecorrido):
        return 1300//costoRecorrido
    def fitness_Travelled(self,travelledDist):
        return 1100//travelledDist
    ##Posibles valores de la suma del costo
    ## Motor 1,camara 1,bateria 1 : 65
    ## Motor 1,camara 1,bateria 2 : 70
    ## Motor 1,camara 1,bateria 3 : 80
    ## Motor 1,camara 2,bateria 1 : 70
    ## Motor 1,camara 2,bateria 2 : 75
    ## Motor 1,camara 2,bateria 3 : 90
    ## Motor 1,camara 3,bateria 1 : 75
    ## Motor 1,camara 3,bateria 2 : 80
    ## Motor 1,camara 3,bateria 3 : 95
    ## Motor 2,camara 1,bateria 1 : 75
    ## Motor 2,camara 1,bateria 2 : 80
    ## Motor 2,camara 1,bateria 3 : 95
    ## Motor 2,camara 2,bateria 1 : 80
    ## Motor 2,camara 2,bateria 2 : 85
    ## Motor 2,camara 2,bateria 3 : 100
    ## Motor 2,camara 3,bateria 1 : 85
    ## Motor 2,camara 3,bateria 2 : 90
    ## Motor 2,camara 3,bateria 3 : 105
    ## Motor 3,camara 1,bateria 1 : 90
    ## Motor 3,camara 1,bateria 2 : 95
    ## Motor 3,camara 1,bateria 3 : 110
    ## Motor 3,camara 2,bateria 1 : 95
    ## Motor 3,camara 2,bateria 2 : 100
    ## Motor 3,camara 2,bateria 3 : 115
    ## Motor 3,camara 3,bateria 1 : 100
    ## Motor 3,camara 3,bateria 2 : 105
    ## Motor 3,camara 3,bateria 3 : 120
    def fitness_Hardware(self,robot):
        return 1100//(robot.motor.costo+robot.camara.costo+robot.bateria.costo)
    def fitness_Battery(self,bateria):
        if(bateria.tipo_Bateria==1):
            return bateria.capacidad//2.5
        elif(bateria.tipo_Bateria==2):
            return  bateria.capacidad//4.25
        elif(bateria.tipo_Bateria==3):
            return  bateria.capacidad//5.95


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
            robot.distanciaRecorrida +=1
            robot.costoRecorrido+=terreno[robot.posicionActual[0]][robot.posicionActual[1]+1]
    elif accion[0]  == 1:
        if robot.posicionActual[1] == 19:
            pass
        elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]+1]:
            robot.activo=False
        else:
            robot.mover_Derecha(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
            robot.distanciaRecorrida += 1
            robot.costoRecorrido+=terreno[robot.posicionActual[0]][robot.posicionActual[1]-1]
    elif accion[0]  == 2:
        if robot.posicionActual[0] == 0:
            pass
        elif robot.motor.potencia < terreno[robot.posicionActual[0]-1][robot.posicionActual[1]]:
            robot.activo = False

        else:
            robot.mover_Adelante(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
            robot.distanciaRecorrida += 1
            robot.costoRecorrido+=terreno[robot.posicionActual[0]+1][robot.posicionActual[1]]
    elif accion[0]  == 3 or accion[0] == 4 :
        if accion[1] == "Norte":
            if robot.posicionActual[0] == 0:
                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0] - 1][robot.posicionActual[1]]:
                robot.activo = False
            else:
                robot.mover_Adelante(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.distanciaRecorrida += 1
                robot.costoRecorrido += terreno[robot.posicionActual[0] + 1][robot.posicionActual[1]]
        elif accion[1] == "Oeste":
            if robot.posicionActual[1] == 0:
                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1] - 1]:
                robot.activo=False
            else:
                robot.mover_Izquierda(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.distanciaRecorrida += 1
                robot.costoRecorrido += terreno[robot.posicionActual[0]][robot.posicionActual[1] + 1]
        elif accion[1] == "Este":
            if robot.posicionActual[1] == 19:
                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1] + 1]:
                robot.activo=False
            else:
                robot.mover_Derecha(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.distanciaRecorrida += 1
                robot.costoRecorrido+=terreno[robot.posicionActual[0]][robot.posicionActual[1]-1]
        #MOVER AL SUR
        else:
            if robot.posicionActual[0] == 19 :

                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0]+1][robot.posicionActual[1]]:
                robot.activo=False
            else:
                robot.mover_Atras(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.distanciaRecorrida+=1
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
    if (robot.bateria.capacidad<0):
        robot.activo=False
    #Robot llegó a su destino , por tanto cesa sus funciones
    if(robot.posicionActual[0] == objetivo[0] and robot.posicionActual[1] == objetivo[1] ):
        robot.completado=True


def get_poblacion_activa(generacion):
    poblacionActiva = []
    for robot in generacion:
        if (robot.activo) :
            poblacionActiva.append(robot)
        elif robot.completado :
            poblacionActiva.append(robot)

    return poblacionActiva

def crearNuevaGen(generacion):
    pass

