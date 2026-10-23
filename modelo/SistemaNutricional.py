from modelo.Alimento import Alimento
from modelo.Persona import Persona
from modelo.RegistroConsumo import RegistroConsumo


class SistemaNutricional:
    #NECESITAMOS ARREGLAR ESTA CLASE
    def __init__(self, personas, alimentos, consumos, cedula, nombrePersona, edad, peso, estatura, metaCaloricaDiaria, fecha, cantidadPorciones, codigo, nombreAlimento, calorias, proteinas, carbohidratos, grasas):
        self.personas = personas
        self.alimentos = alimentos
        self.consumos = consumos
        #Para representar composicion
        self.objetoPersona = Persona(cedula, nombrePersona, edad, peso, estatura, metaCaloricaDiaria)
        self.objetoRegistroConsumo = RegistroConsumo(fecha, cantidadPorciones)
        self.objetoAlimento = Alimento(codigo, nombreAlimento, calorias, proteinas, carbohidratos, grasas)

    def serializarDatos(self):
        pass

    def desearilizarDatos(self):
        pass