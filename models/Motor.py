class Motor:
    consumo = 0
    costo = 0
    potencia = 0
    tipo_motor = 0
    def __init__(self,tipoMotor):
        if tipoMotor == 1:
            self.consumo = 7
            self.costo = 25
            self.potencia = 1
        elif tipoMotor == 2:
            self.consumo = 14
            self.costo = 35
            self.potencia = 2
        else:
            self.consumo = 21
            self.costo = 50
            self.potencia = 3