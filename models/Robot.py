import random
from models.Bateria import Bateria
from models.Camara import Camara
from models.Motor import Motor
from models.Comportamiento import Comportamiento


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

    def accion(self, tipoTerreno):
        accionRealizar =  self.comportamiento.decidirAccion()







