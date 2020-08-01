import numpy as np


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
    def decidirAccion(self,accionAnterior,tipoTerreno,puedeAvanzar):
        #if avanzar
        #if gderecha
        #if gizquierda
        pass