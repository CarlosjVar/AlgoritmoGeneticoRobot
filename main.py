from Models.Robot import Robot
import random
def distancia_Al_Objetivo(robot):
    return (objetivo[0]+robot.posicionActual[0])+(objetivo[1]-robot.posicionActual[1])

def Realizar_Siguiente_Accion(robot,terreno):
    siguiente_espacio = robot.revisarFrente()
    ##Iterar por cada casilla del campo de visión , en cada casilla verificar si el comportamiento del robot decide ir por esa casilla,
    ##En caso de que el robot favorezca todas las casillas , se decide avanzar 1 espacio , de no ser así , se verifican los otros comportamientos
    if robot.motor.potencia>=terreno[siguiente_espacio[0]][siguiente_espacio[1]]:
        pass




terreno=[[random.randint(1,4)for i in range (20)]for i in range(20)]
objetivo = (0,19)

# Main program
if __name__ == "__main__":
    print("Algoritmo genetico robot...")
    generacion = []

    for i in range(10):
        robot = Robot()
        generacion.append(robot)
    robot = generacion[0]
    for i in range(5):
        robot.moverAdelante()
    terreno[robot.posicionActual[0]][robot.posicionActual[1]] =5
    for tierra in terreno:
        print(tierra)