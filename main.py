#REALIZADO POR: JOSTIN AUCANCELA Y JOSÉ TENESACA

import sys
from PyQt6.QtWidgets import QApplication

from modelo.SistemaNutricional import SistemaNutricional
from controlador.ControladorPrincipal import ControladorPrincipal

if __name__ == "__main__":
    app = QApplication(sys.argv)

    modelo_sistema_nutricional = SistemaNutricional()
    controlador_principal = ControladorPrincipal(modelo_sistema_nutricional)

    sys.exit(app.exec())