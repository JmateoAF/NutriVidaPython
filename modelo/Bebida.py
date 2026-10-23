from modelo.Alimento import Alimento

class Bebida(Alimento):
    def __init__(self, codigo, nombre, calorias, proteinas, carbohidratos, grasas, mililitros, esAlcolica):
        super().__init__(codigo, nombre, calorias, proteinas, carbohidratos, grasas)
        self.mililitros = mililitros
        self.esAlcolica = esAlcolica