import numpy as np
import random

class Comportamiento:
    ##Indices de comportamintos
    #Las filas de la matriz representan la acción anterior y las columnas la accion a elegir
    #0 Mover izquierda indifente
    #1 Mover derecha indifente
    #2 Mover frente indifente
    #3 Preferir terreno menor coste
    #4 Preferir terreno mayor coste
    #5 Preferir direccion objetivo
    def __init__(self):

        self.comportamiento = [[random.random() for i in range(6)] for i in range(6)]
        for i in range(6):
            sumaNormalizar = 0
            for o in range(6):
                rand = random.random()
                self.comportamiento[i][o] = rand
                sumaNormalizar += rand
            for o in range(6):
                self.comportamiento[i][o] = self.comportamiento[i][o] / sumaNormalizar
    def decidirAccion(self,accionAnterior,campos_Vision,terreno):
        costoNorte = 0
        costoSur = 0
        costoEste = 0
        costoOeste = 0
        camposNorte=campos_Vision["Norte"]
        camposSur=campos_Vision["Sur"]
        camposEste=campos_Vision["Este"]
        camposOeste=campos_Vision["Oeste"]
        for tupleEspacio in camposNorte:
            if(tupleEspacio[0]>=0 and tupleEspacio[0]<20) and (tupleEspacio[1]>=0 and tupleEspacio[1]<20):
                costoNorte+=terreno[tupleEspacio[0]][tupleEspacio[1]]
            else:
                break
        for tupleEspacio in camposSur:
            if (tupleEspacio[0] >= 0 and tupleEspacio[0] < 20) and (tupleEspacio[1] >= 0 and tupleEspacio[1] < 20):
                costoSur += terreno[tupleEspacio[0]][tupleEspacio[1]]
            else:
                break
        for tupleEspacio in camposEste:
            if (tupleEspacio[0] >= 0 and tupleEspacio[0] < 20) and (tupleEspacio[1] >= 0 and tupleEspacio[1] < 20):
                costoEste += terreno[tupleEspacio[0]][tupleEspacio[1]]
            else:
                break
        for tupleEspacio in camposOeste:
            if (tupleEspacio[0] >= 0 and tupleEspacio[0] < 20) and (tupleEspacio[1] >= 0 and tupleEspacio[1] < 20):
                costoOeste += terreno[tupleEspacio[0]][tupleEspacio[1]]
            else:
                break
        accionGanadora=-1
        if accionAnterior == -1:
            acciones = self.comportamiento[random.randint(0,5)]
            while accionGanadora == -1:
                accionGanadora = self.verificarProbabilidad(acciones)
        else:
            acciones = self.comportamiento[accionAnterior]
            while accionGanadora == -1:
                accionGanadora = self.verificarProbabilidad(acciones)
        direccion = ""
        #Prefirió menor coste
        if(accionGanadora == 3):
            mini = 100
            if(costoNorte<mini and costoNorte>0):
                min=costoNorte
                direccion="Norte"
            if costoSur<mini and costoSur>0:
                min=costoSur
                direccion="Sur"
            if costoEste<mini and costoEste>0:
                min=costoEste
                direccion="Este"
            if costoOeste<mini and costoOeste>0:
                min=costoOeste
                direccion="Oeste"
        #Prefirió mayor coste
        elif(accionGanadora == 4):
            maxi = 0
            if (costoNorte > maxi):
                maxi = costoNorte
                direccion = "Norte"
            if costoSur > maxi:
                maxi = costoSur
                direccion = "Sur"
            if costoEste > maxi:
                maxi = costoEste
                direccion = "Este"
            if costoOeste > maxi:
                maxi = costoOeste
                direccion = "Oeste"
        return [accionGanadora,direccion]
    def verificarProbabilidad(self,acciones):
        for i in range(len(acciones)):
            if self.flip(acciones[i]):
                return i
        return -1
    def flip(self,prob):
        if random.random() < prob:
            return True
        else:
            return False
