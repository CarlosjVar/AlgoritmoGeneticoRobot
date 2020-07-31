import random

import numpy as np
class Robot:
    comportamiento = []
    recorrido = []
    padres = []
    camara = 0
    motor = 0
    bateria = 0
    costo = 0
    def __init__(self):
        self.comportamiento = Comportamiento()
        self.camara = Camara(random.randint(1,3))
        self.motor = Motor(random.randint(1,3))
        self.bateria = Bateria(random.randint(1,3))
    def accion(self,tipoTerreno):
        accionRealizar= self.comportamiento.decidirAccion()

class Bateria:
    capacidad = 0
    costo = 0
    def __init__(self,tipoBateria):
        if(tipoBateria == 1):
            self.capacidad = 150
            self.costo = 25
        elif(tipoBateria == 2):
            self.capacidad = 300
            self.costo = 30
        else:
            self.capacidad = 450
            self.costo = 45
class Camara:
    consumo = 0
    costo = 0
    numero_espacios = 0
    def __init__(self,tipocamara):
        if(tipocamara ==1):
            self.consumo = 0
            self.costo = 15
            self.numero_espacios = 1
        elif(tipocamara == 2):
            self.consumo = 3
            self.costo = 20
            self.numero_espacios = 2
        else:
            self.consumo = 5
            self.costo = 25
            self.numero_espacios = 3
        pass
class Motor:
    consumo = 0
    costo = 0
    potencia = 0
    def __init__(self,tipoMotor):
        if(tipoMotor == 1):
            self.consumo = 7
            self.costo = 25
            self.potencia = 1
        elif(tipoMotor == 2):
            self.consumo = 14
            self.costo = 35
            self.potencia = 2
        else:
            self.consumo = 21
            self.costo = 50
            self.potencia = 3
class Comportamiento:
    ##Indices de comportamintos
    #Las filas de la matriz representan la acción anterior y las columnas la accion a elegir
    #0 Mover izquierda
    #1 Mover derecha
    #2 Mover normal
    #3 Mover moderado
    #4 Mover dificil
    comportamiento = [[np.random.uniform(0.0,1.0) for i in range(5)] for i in range(5)]
    def __init__(self):
        pass
    def decidirAccion(self,accionAnterior,tipoTerreno):
        pass



