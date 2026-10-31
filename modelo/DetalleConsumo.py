class DetalleConsumo:
    # este constructor recibe el tipo de comida, la cantidad, y todo el objeto completo de alimento
    def __init__(self, tipo_comida, cantidad_porciones, alimento_consumido):
        self.tipo_comida = tipo_comida
        self.cantidad_porciones = cantidad_porciones
        self.alimento_consumido = alimento_consumido

    def calcular_subtotal_calorias(self):
        subtotal = self.cantidad_porciones * self.alimento_consumido.calorias
        return round(subtotal, 2)