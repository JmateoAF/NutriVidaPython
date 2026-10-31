class RegistroDiario:
    def __init__(self, fecha):
        self.fecha = fecha

def calcular_total_dia(self, detalles_del_dia):
    total_calorias = 0.0
    for detalle in detalles_del_dia:
        total_calorias += detalle.calcular_subtotal_calorias()

    return round(total_calorias, 2)