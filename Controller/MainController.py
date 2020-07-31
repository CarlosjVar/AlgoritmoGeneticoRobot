from Models.Robot import Robot

generacion= []
for i in range (10):
    robot = Robot()
    generacion.append(robot)
for robot in generacion:
    print(robot.bateria.costo)

