class Bateria:
    capacidad = 0
    costo = 0
    tipo_Bateria = 0
    def __init__(self,tipoBateria):
        if tipoBateria == 1:
            self.capacidad = 150
            self.costo = 25
            tipo_Bateria = 1
        elif tipoBateria == 2:
            self.capacidad = 225
            self.costo = 30
            tipo_Bateria = 2
        else:
            self.capacidad = 300
            self.costo = 45
            tipo_Bateria =  3