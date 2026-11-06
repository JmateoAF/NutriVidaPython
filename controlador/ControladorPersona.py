from pathlib import Path
from PyQt6 import QtWidgets, uic

class ControladorPersona:
    def __init__(self, sistema_nutricional):
        self.sistema_nutricional = sistema_nutricional

        self.vista = QtWidgets.QMainWindow()
        ui_path = str(Path(__file__).resolve().parent.parent / 'vista' / 'VistaPrincipal.ui')
        uic.loadUi(ui_path, self.vista)

        self.vista.centralwidget.btnGuardar.clicked.connect(self.registrar_persona)

        self.vista.show()

    def registrar_persona(self):
            pass