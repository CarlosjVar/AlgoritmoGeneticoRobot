from models.Robot import Robot
from controllers.mainController import MainController

objetivo = (0,19)
##TODO: IMPLEMENTAR MUTACIONES TOMANDO USANDO COMO EQUIVALENTE A LA SUBUNIDAD BIT LAS CELDAS DE LA MATRIZ DE COMPORTAMIENTOS


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
