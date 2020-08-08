class Camara:

    def __init__(self, tipo_camara):
        if tipo_camara == 1:
            self.consumo = 0
            self.costo = 15
            self.numero_espacios = 1
            self.tipo_camara = 1
        elif tipo_camara == 2:
            self.consumo = 1
            self.costo = 20
            self.numero_espacios = 2
            self.tipo_camara = 2
        else:
            self.consumo = 2
            self.costo = 25
            self.numero_espacios = 3
            self.tipo_camara = 3
