class Bateria:
    capacidad = 0
    costo = 0

    def __init__(self,tipoBateria):
        if tipoBateria == 1:
            self.capacidad = 150
            self.costo = 25
        elif tipoBateria == 2:
            self.capacidad = 300
            self.costo = 30
        else:
            self.capacidad = 450
            self.costo = 45