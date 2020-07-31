from models.Robot import Robot


# Main program
if __name__ == "__main__":
    print("Algoritmo genetico robot...")
    generacion = []
    for i in range(10):
        robot = Robot()
        generacion.append(robot)
    for robot in generacion:
        print(robot.bateria.costo)
