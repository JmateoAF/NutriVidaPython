from PyQt6.QtWidgets import QMainWindow

class VistaPersona(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SI")
        self.resize(800, 600)

        self.setStyleSheet("background-color: black;")
