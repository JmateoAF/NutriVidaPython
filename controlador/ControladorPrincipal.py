from PyQt6 import QtWidgets, uic
from pathlib import Path

class ControladorPrincipal:
    def __init__(self, modelo_sistema_nutricional):
        self.modelo_sistema_nutricional = modelo_sistema_nutricional

        #Ruta de donde estan todas las vistas
        self.direccion_vistas = Path(__file__).resolve().parent.parent / "vista"

        #Cargamos la vista principal y las demas vistas
        self.vista_principal = QtWidgets.QMainWindow()
        uic.loadUi(str(self.direccion_vistas / "VentanaPrincipal.ui"), self.vista_principal)

        self.vista_personas = QtWidgets.QWidget()
        uic.loadUi(str(self.direccion_vistas / "VentanaPersona.ui"), self.vista_personas)

        #Cargamos las vistas dentro de cada pestaña
        self.vista_principal.tabPersonas.layout().addWidget(self.vista_personas)

        self.vista_principal.show()