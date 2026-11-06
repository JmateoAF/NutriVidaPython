from pathlib import Path
from PyQt6 import uic

class ControladorPersona:
    def __init__(self, sistema_nutricional):
        self.sistema_nutricional = sistema_nutricional

        ruta = str(Path(__file__).resolve().parent.parent / 'vista' / 'VentanaPrincipal.ui')
        self.vista = uic.loadUi(ruta)

        self.vista.btnGuardar.clicked.connect(self.registrar_persona)

        self.vista.show()

    def registrar_persona(self):
            pass