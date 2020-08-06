from models.Robot import Robot
from controllers.mainController import MainController

objetivo = (0,19)
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

# Main program
if __name__ == "__main__":
    print("Algoritmo genetico robot...")
    main_controller = MainController()
    main_controller.run()
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
