import sys
from PyQt6.QtWidgets import QApplication

from vista.VistaPersona import VistaPersona

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VistaPersona()
    window.show()
    sys.exit(app.exec())