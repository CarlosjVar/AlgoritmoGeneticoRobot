class Robot:
    # Arreglar cadena Markov
    mover_izquierda = 0
    mover_derecha = 0
    preferir_moderado = 0
    preferir_normal = 0
    preferir_dificil = 0

    recorrido = []
    padres = []
    camara = 0
    motor = 0
    bateria = 0

    def __init__(self, moverI, moverD, pModerado, pNormal, pDificil, padres):
        self.mover_izquierda = moverI
        self.mover_derecha = moverD
        self.preferir_moderado = pModerado
        self.preferir_dificil = pDificil
        self.preferir_normal = pNormal
        self.padres = padres
        pass
class Bateria:
    capacidad = 0
    costo = 0
    def __init__(self,capacidad):
        self.capacidad = capacidad
        pass

class Motor:
    consumo = 0
    costo = 0
    potencia = 0
    def __init__(self,consumo,costo,potencia):
        self.consumo = consumo
        self.costo = costo
        self.potencia = potencia
        pass

class Camara:
    consumo = 0
    costo = 0
    numero_espacios = 0
    def __init__(self,consumo,costo,numero_espacios):
        self.consumo = consumo
        self.costo = costo
        self.numero_espacios = numero_espacios
        pass

class Comportamientos:
    comportamiento = [["p","e","p","i","to"] for i in range(5)]
    def __init__(self):
        pass


