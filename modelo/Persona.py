class Persona:
    def __init__(self, cedula, nombre, edad, peso, estatura, metaCaloricaDiaria):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self.metaCaloricaDiaria = metaCaloricaDiaria

    #Solo para poner asoasicion entre clases
    def conoceRegistroConsumo(self, objetoRegistroConsumo):
        self.objetoRegistroConsumo = objetoRegistroConsumo
        self.objetoRegistroConsumo.xd()
