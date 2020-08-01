from Models.Robot import Robot
import random
import os
terreno=[[random.randint(1,4)for i in range (20)]for i in range(20)]
objetivo = (0,19)

# Main program
if __name__ == "__main__":
    print("Algoritmo genetico robot...")
    generacion = []
    for i in range(10):
        robot = Robot()
        generacion.append(robot)
    for robot in generacion:
        print(robot.bateria.costo)
    for i in range(5):
        robot.moverAdelante()
    terreno[generacion[0].posicionActual[0]][generacion[0].posicionActual[1]] = 5
    for tierra in terreno:
        print(tierra)