objetivo = (0,19)
class Geneticos:
    valores_Fitness = []
    valores_Fitness_Normalizados = []

    def fitness(self,robot):
        distancia = self.distancia_Al_Objetivo(robot)
        fitDist = self.fitness_Distancia(distancia)
        fitTravelled = self.fitness_Travelled(robot.distanciaRecorrida)
        fitHardw=self.fitness_Hardware(robot)
        fitBatt=self.fitness_Battery(robot.bateria)
        self.valores_Fitness.append(fitDist+fitTravelled+fitHardw+fitBatt)
    def distancia_Al_Objetivo(self, robot):
        return (objetivo[0] + robot.posicionActual[0]) + (objetivo[1] - robot.posicionActual[1])
    #Maxima distancia posible = 38
    def fitness_Distancia(self,distancia):
        if distancia==0:
            return 90
        return 80//distancia
    def fitness_CostoRecorrido(self,costoRecorrido):
        pass
    def fitness_Travelled(self,travelledDist):
        return 1300//travelledDist
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
        return 900//(robot.motor.costo+robot.camara.costo+robot.bateria.costo)
    def fitness_Battery(self,bateria):
        return bateria.capacidad//10





