from models.Robot import Robot
from controllers.mainController import MainController
import random


def distancia_Al_Objetivo(robot):
    return (objetivo[0]+robot.posicionActual[0])+(objetivo[1]-robot.posicionActual[1])


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
    elif accion[0]  == 2:
        if robot.posicionActual[0] == 0:
           return
        elif robot.motor.potencia < terreno[robot.posicionActual[0]-1][robot.posicionActual[1]]:
            return
        else:
            robot.mover_Adelante()
            robot.bateria.capacidad-=robot.motor.consumo
    elif accion[0]  == 3 or accion[0] == 4 :
        print(accion[1])
        if accion[1] == "Norte":
            if robot.posicionActual[0] == 0:
                return
            elif robot.motor.potencia < terreno[robot.posicionActual[0] - 1][robot.posicionActual[1]]:
                return
            else:
                robot.mover_Adelante()
                robot.bateria.capacidad -= robot.motor.consumo
        elif accion[1] == "Oeste":
            if robot.posicionActual[1] == 0:
                return
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1] - 1]:
                return
            else:
                robot.mover_Izquierda()
                robot.bateria.capacidad -= robot.motor.consumo
        elif accion[1] == "Este":
            if robot.posicionActual[1] == 19:
                return
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1] + 1]:
                return
            else:
                robot.mover_Derecha()
                robot.bateria.capacidad -= robot.motor.consumo
        #MOVER AL SUR
        else:
            if robot.posicionActual[0] == 19 :
                return
            elif robot.motor.potencia < terreno[robot.posicionActual[0]+1][robot.posicionActual[1]]:
                return
            else:
                robot.mover_Atras()
                robot.bateria.capacidad -= robot.motor.consumo
        #TODO: CODEAR DECISIÓN DIRECCIÓN AL OBJETIVO




terreno=[[random.randint(1,3)for i in range (20)]for i in range(20)]
objetivo = (0,19)

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
    s = input("Digite Y para continuar N para terminar")
    while s=="Y":

        Realizar_Siguiente_Accion(robot,terreno)
        entero =terreno[robot.posicionActual[0]][robot.posicionActual[1]]
        terreno[robot.posicionActual[0]][robot.posicionActual[1]] = 5
        for tierra in terreno:
            print(tierra)
        print(robot.posicionActual)
        terreno[robot.posicionActual[0]][robot.posicionActual[1]] = entero
        s = input("Digite Y para continuar N para terminar")
