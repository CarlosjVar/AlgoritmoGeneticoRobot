class Camara:

    def __init__(self, tipocamara):
        if tipocamara == 1:
            self.consumo = 0
            self.costo = 15
            self.numero_espacios = 1
            self.tipo_camara = 1
        elif tipocamara == 2:
            self.consumo = 3
            self.costo = 20
            self.numero_espacios = 2
            self.tipo_camara = 2
        else:
            self.consumo = 5
            self.costo = 25
            self.numero_espacios = 3
            self.tipo_camara = 3
