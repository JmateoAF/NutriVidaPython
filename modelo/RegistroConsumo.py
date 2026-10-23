class RegistroConsumo:
    def __init__(self, fecha, cantidadPorciones):
        self.fecha = fecha
        self.cantidadPorciones = cantidadPorciones

    def calcularTotalCalorias(self):
        pass

    #Solo para poner asoasicion entre clases
    def conoceAlimento(self, objetoAlimento):
        self.objetoAlimento = objetoAlimento
        self.objetoAlimento.si()

    #Solo para poner asociacion entre clases
    def xd(self):
        print("xd")
