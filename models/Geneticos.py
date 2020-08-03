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
    def fitness_Distancia(self,distancia):
        return 150/distancia
    def fitness_Travelled(self,travelledDist):
        return 200/travelledDist
    def fitness_Hardware(self,robot):
        return 100/(robot.motor.costo+robot.camara.costo+robot.bateria.costo)
    def fitness_Battery(self,bateria):
        return round(0.7*bateria.capacidad)





