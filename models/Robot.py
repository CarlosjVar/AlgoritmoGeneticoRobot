import random
from Models.Bateria import Bateria
from Models.Camara import Camara
from Models.Motor import Motor
from Models.Comportamiento import Comportamiento


class Robot:
    comportamiento = []
    recorrido = []
    padres = []
    camara = 0
    motor = 0
    bateria = 0
    costo = 0
    ultimaAccion = -1
    posicionActual = [19,0]
    direccion = 'N'

    def __init__(self):
        self.comportamiento = Comportamiento()
        self.camara = Camara(random.randint(1,3))
        self.motor = Motor(random.randint(1,3))
        self.bateria = Bateria(random.randint(1,3))

    def accion(self, tipoTerreno):
        accionRealizar =  self.comportamiento.decidirAccion()
    def moverAdelante(self):
        if(self.direccion=='N' and (self.posicionActual[0]!=0)):
            self.posicionActual[0] = self.posicionActual[0] - 1
        elif((self.direccion=='S') and (self.posicionActual[0]!=19)):
            self.posicionActual[0] = self.posicionActual[0] + 1
        elif ((self.direccion == 'E') and (self.posicionActual[1] != 19)):
            self.posicionActual[0] = self.posicionActual[1] + 1
        elif ((self.direccion == 'O') and (self.posicionActual[1] != 0)):
            self.posicionActual[0] = self.posicionActual[1] - 1








