from modelo.Alimento import Alimento

class ComidaSolida(Alimento):
    def __init__(self, codigo, nombre, calorias, proteinas, carbohidratos, grasas, gramos):
        super().__init__(codigo, nombre, calorias, proteinas, carbohidratos, grasas)
        self.gramos = gramos