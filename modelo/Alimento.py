class Alimento:
    def __init__(self, codigo, nombre, calorias, proteinas, carbohidratos, grasas):
        self.codigo = codigo
        self.nombre = nombre
        self.calorias = calorias
        self.proteinas = proteinas
        self.carbohidratos = carbohidratos
        self.grasas = grasas

    #Solo para poner asosiacion entre clases
    def si(self):
        print("si")