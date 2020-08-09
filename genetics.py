from models.Geneticos import Geneticos


def realizar_siguiente_accion(robot, terreno):
    """Realiza la siguiente accion del robot

    :param robot: El robot que realizara la accion
    :param terreno: El terreno sobre el que se esta trabajando
    :return: No retorna nada
    """
    # TODO: Se habia cambiado index en comparacion de potencia
    objetivo = (0, 19)
    campos_Vision = robot.revisar_Alrededor()
    accion = robot.accion(campos_Vision,terreno)
    robot.ultimaAccion = accion[0]
    print(robot.posicionActual[0],robot.posicionActual[1])
    #accion = [ACCION,DIRECCION(DE SER NECESARIO)]
    if accion[0] == 0:
        if robot.posicionActual[1] == 0:
            if (robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]):
                robot.activo = False
            pass
        elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]:
            robot.activo = False
        else:
            print("Mover izquierda")
            robot.mover_Izquierda(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
            robot.costoRecorrido += terreno[robot.posicionActual[0]][robot.posicionActual[1]+1]
    elif accion[0]  == 1:
        if robot.posicionActual[1] == 19:
            if (robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]):
                robot.activo = False
            pass
        elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]:
            robot.activo = False
        else:
            robot.mover_Derecha(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
            print("Mover derecga")
            robot.costoRecorrido += terreno[robot.posicionActual[0]][robot.posicionActual[1] - 1]
    elif accion[0]  == 2:
        if robot.posicionActual[0] == 0:
            if (robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]):
                robot.activo = False
            pass
        elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]:
            robot.activo = False

        else:
            print("Mover adelante")
            robot.mover_Adelante(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
            robot.costoRecorrido += terreno[robot.posicionActual[0] + 1][robot.posicionActual[1]]
    elif accion[0]  == 3 or accion[0] == 4:
        if accion[1] == "Norte":
            if robot.posicionActual[0] == 0:
                if (robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]):
                    robot.activo=False
                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]:
                robot.activo = False
            else:
                print("Mover adelante")
                robot.mover_Adelante(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido += terreno[robot.posicionActual[0] + 1][robot.posicionActual[1]]
        elif accion[1] == "Oeste":
            if robot.posicionActual[1] == 0:
                if (robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]):
                    robot.activo=False
                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]:
                robot.activo = False
            else:
                print("Mover izquierda")
                robot.mover_Izquierda(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido += terreno[robot.posicionActual[0]][robot.posicionActual[1] + 1]
        elif accion[1] == "Este":
            if robot.posicionActual[1] == 19:
                if (robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]):
                    robot.activo=False
                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]:
                robot.activo = False
            else:
                print("Mover derecha")
                robot.mover_Derecha(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido+=terreno[robot.posicionActual[0]][robot.posicionActual[1]-1]
        #MOVER AL SUR
        else:
            if robot.posicionActual[0] == 19 :
                if (robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]):
                    robot.activo=False
                pass
            elif robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]:
                robot.activo = False
            else:
                print("Mover atras")
                robot.mover_Atras(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido += terreno[robot.posicionActual[0] - 1][robot.posicionActual[1]]
    # DIRECCIÓN AL OBJETIVO
    elif accion[0] == 5:
        #Norte
        # TODO: Agregar validacion de moto/terreno
        if (robot.posicionActual[0] > objetivo[0]) :
            if robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]:
                robot.activo=False
            else:
                print("Mover adelante")
                robot.mover_Adelante(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido += terreno[robot.posicionActual[0] + 1][robot.posicionActual[1]]
        #Sur
        elif (robot.posicionActual[0] < objetivo[0]) :
            if robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]:
                robot.activo=False
            else:
                print("Mover atras")
                robot.mover_Atras(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido += terreno[robot.posicionActual[0] - 1][robot.posicionActual[1]]
        #Oeste
        elif (robot.posicionActual[1] > objetivo[1]) :
            if robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]:
                robot.activo=False
            else:
                print("Mover izquierda")
                robot.mover_Izquierda(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido += terreno[robot.posicionActual[0]][robot.posicionActual[1] + 1]
        #Este
        elif (robot.posicionActual[1] < objetivo[1]):
            if robot.motor.potencia < terreno[robot.posicionActual[0]][robot.posicionActual[1]]:
                robot.activo=False
            else:
                print("Mover derecha")
                robot.mover_Derecha(terreno[robot.posicionActual[0]][robot.posicionActual[1]])
                robot.costoRecorrido += terreno[robot.posicionActual[0]][robot.posicionActual[1]-1]

    # Robot agotó su batería, por tanto se desactiva
    if robot.bateria.capacidad <= 0:
        robot.bateria.capacidad = 0
        robot.activo = False
        robot.completado = True

    # Robot llegó a su destino , por tanto cesa sus funciones
    if robot.posicionActual[0] == objetivo[0] and robot.posicionActual[1] == objetivo[1]:
        robot.completado = True
        robot.activo = False
    print(robot.activo)

def get_poblacion_activa(generacion):
    """Obtiene la poblacion activa de la generacion actual

    :param generacion: La generacion actual
    :return: La poblacion de robots activa
    """
    poblacionActiva = []
    for robot in generacion:
        if robot.activo:
            poblacionActiva.append(robot)
    return poblacionActiva


def crearNuevaGen(generacion):
    """Crea una nueva generacion de robots

    :param generacion: La generacion actual
    :return: El promedio del fitness y la nueva generacion
    """
    gen = Geneticos()
    gen.fitnessGeneracion(generacion)
    return [gen.promedioFitness, gen.newGen]
