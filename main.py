from models.Robot import Robot
from controllers.mainController import MainController
import random
import numpy as np
objetivo = (0,19)
indiceMutacion= 3
##TODO: IMPLEMENTAR MUTACIONES TOMANDO USANDO COMO EQUIVALENTE A LA SUBUNIDAD BIT LAS CELDAS DE LA MATRIZ DE COMPORTAMIENTOS
def Realizar_Siguiente_Accion(robot,terreno):
    campos_Vision = robot.revisar_Alrededor()
    accion = robot.accion(campos_Vision,terreno)
    robot.ultimaAccion = accion[0]
    #accion = [ACCION,DIRECCION(DE SER NECESARIO)]
    print(accion[0])
    if accion[0] == 0:
        if robot.posicionActual[1] == 0:
           return
        elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]-1]:
            return
        else:
            robot.mover_Izquierda()
            robot.bateria.capacidad-=robot.motor.consumo
            robot.distanciaRecorrida +=1
            robot.costoRecorrido+=terreno[robot.posicionActual[0]][robot.posicionActual[1]-1]
    elif accion[0]  == 1:
        if robot.posicionActual[1] == 19:
            print("Estoy al límite")
            return
        elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]+1]:
            print("Potencia no me da")
            return
        else:
            robot.mover_Derecha()
            robot.bateria.capacidad-=robot.motor.consumo
            robot.distanciaRecorrida += 1
            robot.costoRecorrido+=terreno[robot.posicionActual[0]][robot.posicionActual[1]+1]
    elif accion[0]  == 2:
        if robot.posicionActual[0] == 0:
           return
        elif robot.motor.potencia < terreno[robot.posicionActual[0]-1][robot.posicionActual[1]]:
            return
        else:
            robot.mover_Adelante()
            robot.bateria.capacidad-=robot.motor.consumo
            robot.distanciaRecorrida += 1
            robot.costoRecorrido+=terreno[robot.posicionActual[0]-1][robot.posicionActual[1]]
    elif accion[0]  == 3 or accion[0] == 4 :
        if accion[1] == "Norte":
            if robot.posicionActual[0] == 0:
                return
            elif robot.motor.potencia < terreno[robot.posicionActual[0] - 1][robot.posicionActual[1]]:
                return
            else:
                robot.mover_Adelante()
                robot.bateria.capacidad -= robot.motor.consumo
                robot.distanciaRecorrida += 1
                robot.costoRecorrido += terreno[robot.posicionActual[0] - 1][robot.posicionActual[1]]
        elif accion[1] == "Oeste":
            if robot.posicionActual[1] == 0:
                return
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1] - 1]:
                return
            else:
                robot.mover_Izquierda()
                robot.bateria.capacidad -= robot.motor.consumo
                robot.distanciaRecorrida += 1
                robot.costoRecorrido += terreno[robot.posicionActual[0]][robot.posicionActual[1] - 1]
        elif accion[1] == "Este":
            if robot.posicionActual[1] == 19:
                return
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1] + 1]:
                return
            else:
                robot.mover_Derecha()
                robot.bateria.capacidad -= robot.motor.consumo
                robot.distanciaRecorrida += 1
                robot.costoRecorrido+=[robot.posicionActual[0]][robot.posicionActual[1] + 1]
        #MOVER AL SUR
        else:
            if robot.posicionActual[0] == 19 :
                return
            elif robot.motor.potencia < terreno[robot.posicionActual[0]+1][robot.posicionActual[1]]:
                return
            else:
                robot.mover_Atras()
                robot.bateria.capacidad -= robot.motor.consumo
                robot.distanciaRecorrida+=1
                robot.costoRecorrido += terreno[robot.posicionActual[0] + 1][robot.posicionActual[1]]
        #TODO: CODEAR DECISIÓN DIRECCIÓN AL OBJETIVO

        #Robot agotó su batería , por tanto se desactiva
        if (robot.bateria.capacidad<0):
            robot.activo=False
        #Robot llegó a su destino , por tanto cesa sus funciones
        if(robot.posicionActual[0] == objetivo[0] and robot.posicionActual[1] == objetivo[1] ):
            robot.completado=True
def get_poblacion_activa(generacion):
    poblacionActiva = []
    for robot in generacion:
        if (robot.activo )or (not robot.completado) :
            poblacionActiva.append(robot)
    return poblacionActiva
def cargar_Terreno():
    fila_Terreno =open("./_resources/terreno.txt","r")
    if fila_Terreno.mode == "r":
        lineas = fila_Terreno.read().splitlines()
        fila=0
        for linea in lineas:
            tiles = linea.split(",")
            columna =0
            for tile in tiles:
                terreno[fila][columna] = int(tile)
                columna+=1
            fila+=1



terreno=[[0 for i in range (20)]for i in range(20)]

# Main program
if __name__ == "__main__":
    print("Algoritmo genetico robot...")
    # main_controller = MainController()
    # main_controller.run()
    generacion = []
    for i in range(10):
        robot = Robot()
        generacion.append(robot)
    robot = generacion[0]
    robot.motor.potencia=3
    robot.camara.numero_espacios=1
    for comportam in robot.comportamiento.comportamiento:
        print(comportam)
    cargar_Terreno()
    s = input("Digite Y para continuar N para terminar")
    cargar_Terreno()
    while s=="Y":
        Realizar_Siguiente_Accion(robot,terreno)
        entero =terreno[robot.posicionActual[0]][robot.posicionActual[1]]
        terreno[robot.posicionActual[0]][robot.posicionActual[1]] = 5
        for tierra in terreno:
            print(tierra)
        print(robot.bateria.capacidad)
        terreno[robot.posicionActual[0]][robot.posicionActual[1]] = entero
        s = input("Digite Y para continuar N para terminar")
    ###BOCETO
    ###GENERACION
    ###GENERACIONACTIVA = FUNC(GENERACION)
    ###WHILE LEN(GENACTIVA) != 0:
    ###FOR ROBOT IN GENERACION:
    ###     ROBOT.ACCION
    ###Genetics genetics()
    ###for robot in gen:
    ###    genetics.evaluar(robot)
    ###nuevagen=genetics.generarGen

