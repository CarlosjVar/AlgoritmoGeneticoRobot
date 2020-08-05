class Bateria:

    def __init__(self,tipoBateria):
        if tipoBateria == 1:
            self.capacidad = 500
            self.costo = 25
            self.tipo_Bateria = 1
        elif tipoBateria == 2:
            self.capacidad = 750
            self.costo = 30
            self.tipo_Bateria = 2
        else:
            self.capacidad = 1000
            self.costo = 45
            self.tipo_Bateria =  3