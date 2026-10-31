class Persona:
    def __init__(self, cedula, nombre, edad, estatura):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        # Aquí ya no vamos a tener el peso porque el peso es variable y eso guardaremos en las evaluaciones

    #Método para calcular el índice de masa corporal según el último peso registado
    def calcular_imc_actual(self, peso_actual):
        try:
            #la fórmula real del imc:
            # peso(kilos) / (estatura(metros) ** 2)
            imc = peso_actual/(self.estatura ** 2)
            # Redondeo a 2 decimales
            return round(imc, 2)
        except ZeroDivisionError :
        # Esto no vaya a ser que algún chistoso ponga estatura 0
            return 0.0
