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
    ultimaAccion = -1
    distanciaRecorrida = 0
    posicionActual = [19,0]
    activo=True
    completado=False
    costoRecorrido=0
    def __init__(self):
        self.comportamiento = Comportamiento()
        self.camara = Camara(random.randint(1,3))
        self.motor = Motor(random.randint(1,3))
        self.bateria = Bateria(random.randint(1,3))
    def accion(self, bloques_adyacentes,terreno):
        accionRealizar =  self.comportamiento.decidirAccion(self.ultimaAccion,bloques_adyacentes,terreno)
        return accionRealizar
    def mover_Adelante(self,tipoTerreno):
        self.posicionActual[0] = self.posicionActual[0] - 1
        if tipoTerreno == 1:
            self.bateria.capacidad-=25
        elif tipoTerreno == 2:
            self.bateria.capacidad -= 35
        else:
            self.bateria.capacidad-=50

    def mover_Derecha(self,tipoTerreno):
        self.posicionActual[1] = self.posicionActual[1] + 1
        if tipoTerreno == 1:
            self.bateria.capacidad-=25
        elif tipoTerreno == 2:
            self.bateria.capacidad -= 35
        else:
            self.bateria.capacidad-=50
    def mover_Atras(self,tipoTerreno):
        self.posicionActual[0] = self.posicionActual[0] + 1
        if tipoTerreno == 1:
            self.bateria.capacidad-=25
        elif tipoTerreno == 2:
            self.bateria.capacidad -= 35
        else:
            self.bateria.capacidad-=50
    def mover_Izquierda(self,tipoTerreno):
        self.posicionActual[1] = self.posicionActual[1] - 1
        if tipoTerreno == 1:
            self.bateria.capacidad-=25
        elif tipoTerreno == 2:
            self.bateria.capacidad -= 35
        else:
            self.bateria.capacidad-=50
    def revisar_Alrededor(self):
        diccEspacios={}
        if (self.camara.numero_espacios==1):

            diccEspacios["Norte"] = [[self.posicionActual[0]-1,self.posicionActual[1]]]
            diccEspacios["Oeste"] = [[self.posicionActual[0],self.posicionActual[1]-1]]
            diccEspacios["Sur"] = [[self.posicionActual[0]+1,self.posicionActual[1]]]
            diccEspacios["Este"] = [[self.posicionActual[0],self.posicionActual[1]+1]]
            return diccEspacios
        elif(self.camara.numero_espacios==2):
            self.bateria.capacidad -= 3
            diccEspacios["Norte"] = [[self.posicionActual[0] - 1,self.posicionActual[1]],
                                     [self.posicionActual[0] - 2,self.posicionActual[1]]]
            diccEspacios["Oeste"] = [[self.posicionActual[0],self.posicionActual[1] - 1],
                                     [self.posicionActual[0],self.posicionActual[1] - 2]]
            diccEspacios["Sur"] = [[self.posicionActual[0] + 1,self.posicionActual[1]],
                                   [self.posicionActual[0] + 2,self.posicionActual[1]]]
            diccEspacios["Este"] = [[self.posicionActual[0],self.posicionActual[1] + 1],
                                    [self.posicionActual[0],self.posicionActual[1] + 2],]
            return diccEspacios
        elif(self.camara.numero_espacios==3):
            self.bateria.capacidad -= 5
            diccEspacios["Norte"] = [[self.posicionActual[0] - 1,self.posicionActual[1]],
                                     [self.posicionActual[0] - 2,self.posicionActual[1]],
                                     [self.posicionActual[0] - 3,self.posicionActual[1]]]
            diccEspacios["Oeste"] = [[self.posicionActual[0],self.posicionActual[1] - 1],
                                     [self.posicionActual[0],self.posicionActual[1] - 2],
                                     [self.posicionActual[0],self.posicionActual[1] - 3]]
            diccEspacios["Sur"] = [[self.posicionActual[0] + 1,self.posicionActual[1]],
                                   [self.posicionActual[0] + 2,self.posicionActual[1]],
                                   [self.posicionActual[0] + 3,self.posicionActual[1]]]
            diccEspacios["Este"] = [[self.posicionActual[0],self.posicionActual[1] + 1],
                                    [self.posicionActual[0],self.posicionActual[1] + 2 ],
                                    [self.posicionActual[0],self.posicionActual[1] + 3]]
            return diccEspacios










