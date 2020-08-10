import random
import uuid
from models.Bateria import Bateria
from models.Camara import Camara
from models.Motor import Motor
from models.Comportamiento import Comportamiento


class Robot:
    def __init__(self,padre=0,madre=0):
        if padre == 0:
            self.usosMotor = 0
            self.comportamiento = Comportamiento()
            self.camara = Camara(random.randint(1,3))
            self.motor = Motor(random.randint(1,3))
            self.bateria = Bateria(random.randint(1,3))
            self.posicionActual = [19,0]
            self.recorrido = []
            self.padres = []
            self.ultimaAccion = -1
            self.distanciaRecorrida = 0
            self.activo = True
            self.completado = False
            self.costoRecorrido = 0
            self.id= uuid.uuid1()
            self.usosCamara = 0
        else:
            self.comportamiento= Comportamiento()
            self.comportamiento.comportamiento= padre.comportamiento.comportamiento[0:len(padre.comportamiento.comportamiento)//2] + madre.comportamiento.comportamiento[len(padre.comportamiento.comportamiento)//2:len(padre.comportamiento.comportamiento)]
            if random.randint(1,2) == 1:
                self.bateria = Bateria(padre.bateria.tipo_Bateria)
                self.motor = Motor(madre.motor.potencia)
                self.camara = Camara(madre.camara.tipo_camara)
            else:
                self.bateria = Bateria(madre.bateria.tipo_Bateria)
                self.motor = Motor(padre.motor.potencia)
                self.camara = Camara(padre.camara.tipo_camara)
            self.posicionActual = [19, 0]
            self.recorrido = []
            self.padres = [padre,madre]
            self.ultimaAccion = -1
            self.distanciaRecorrida = 0
            self.activo = True
            self.completado = False
            self.costoRecorrido = 0
            self.id = uuid.uuid1()


    def reinicarStats(self):
        self.posicionActual = [19, 0]
        self.recorrido = []
        self.ultimaAccion = -1
        self.distanciaRecorrida = 0
        self.activo = True
        self.completado = False
        self.costoRecorrido = 0
        self.bateria.capacidad = self.bateria.capacidadMaxima

    def accion(self, bloques_adyacentes,terreno):
        accionRealizar =  self.comportamiento.decidirAccion(self.ultimaAccion,bloques_adyacentes,terreno)
        return accionRealizar

    def mover_Adelante(self,tipoTerreno):
        self.distanciaRecorrida+=1
        self.recorrido.append([self.posicionActual[0]-1,self.posicionActual[1]])
        self.posicionActual[0] = self.posicionActual[0] - 1
        if tipoTerreno == 1:
            self.bateria.capacidad-=7
        elif tipoTerreno == 2:
            self.bateria.capacidad -= 14
        else:
            self.bateria.capacidad-=21

    def mover_Derecha(self,tipoTerreno):
        self.distanciaRecorrida+=1
        self.recorrido.append([self.posicionActual[0],self.posicionActual[1]+1])
        self.posicionActual[1] = self.posicionActual[1] + 1
        if tipoTerreno == 1:
            self.bateria.capacidad-=7
        elif tipoTerreno == 2:
            self.bateria.capacidad -=14
        else:
            self.bateria.capacidad-=21

    def mover_Atras(self,tipoTerreno):
        self.distanciaRecorrida+=1
        self.recorrido.append([self.posicionActual[0]+1,self.posicionActual[1]])
        self.posicionActual[0] = self.posicionActual[0] + 1
        if tipoTerreno == 1:
            self.bateria.capacidad-=7
        elif tipoTerreno == 2:
            self.bateria.capacidad-= 14
        else:
            self.bateria.capacidad-=21

    def mover_Izquierda(self,tipoTerreno):
        self.distanciaRecorrida+=1
        self.recorrido.append([self.posicionActual[0],self.posicionActual[1]-1])
        self.posicionActual[1] = self.posicionActual[1] - 1
        self.recorrido.append(self.posicionActual)
        if tipoTerreno == 1:
            self.bateria.capacidad-=7
        elif tipoTerreno == 2:
            self.bateria.capacidad -=14
        elif tipoTerreno == 3:
            self.bateria.capacidad-=21

    def revisar_Alrededor(self):
        diccEspacios={}
        if (self.camara.numero_espacios==1):
            diccEspacios["Norte"] = [[self.posicionActual[0]-1,self.posicionActual[1]]]
            diccEspacios["Oeste"] = [[self.posicionActual[0],self.posicionActual[1]-1]]
            diccEspacios["Sur"] = [[self.posicionActual[0]+1,self.posicionActual[1]]]
            diccEspacios["Este"] = [[self.posicionActual[0],self.posicionActual[1]+1]]
            self.bateria.capacidad-=self.camara.consumo
            return diccEspacios
        elif(self.camara.numero_espacios==2):
            diccEspacios["Norte"] = [[self.posicionActual[0] - 1,self.posicionActual[1]],
                                     [self.posicionActual[0] - 2,self.posicionActual[1]]]
            diccEspacios["Oeste"] = [[self.posicionActual[0],self.posicionActual[1] - 1],
                                     [self.posicionActual[0],self.posicionActual[1] - 2]]
            diccEspacios["Sur"] = [[self.posicionActual[0] + 1,self.posicionActual[1]],
                                   [self.posicionActual[0] + 2,self.posicionActual[1]]]
            diccEspacios["Este"] = [[self.posicionActual[0],self.posicionActual[1] + 1],
                                    [self.posicionActual[0],self.posicionActual[1] + 2],]
            self.bateria.capacidad -= self.camara.consumo
            return diccEspacios
        elif(self.camara.numero_espacios==3):
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
            self.bateria.capacidad -= self.camara.consumo
            return diccEspacios










