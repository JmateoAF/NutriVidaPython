#REALIZADO POR: JOSTIN AUCANCELA Y JOSÉ TENESACA

import sys
from PyQt6.QtWidgets import QApplication

from modelo.SistemaNutricional import SistemaNutricional
from controlador.ControladorPersona import ControladorPersona

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    modelo_sistema_nutricional = SistemaNutricional()
    controlador_persona = ControladorPersona(modelo_sistema_nutricional)

    sys.exit(app.exec())