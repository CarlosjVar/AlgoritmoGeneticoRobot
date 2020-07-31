class Camara:
    consumo = 0
    costo = 0
    numero_espacios = 0
    def __init__(self, tipocamara):
        if tipocamara == 1:
            self.consumo = 0
            self.costo = 15
            self.numero_espacios = 1
        elif tipocamara == 2:
            self.consumo = 3
            self.costo = 20
            self.numero_espacios = 2
        else:
            self.consumo = 5
            self.costo = 25
            self.numero_espacios = 3