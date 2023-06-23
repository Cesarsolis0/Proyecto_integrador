from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QGridLayout
from Edades import mostrar_edades

class VentanaResultados(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ver análisis')

        # Configuramos el tamaño de la ventana
        self.setFixedSize(350, 350)

        widget = QWidget()
        layout = QGridLayout()

        button_edades = QPushButton('Edades')
        button_edades.clicked.connect(lambda:mostrar_edades(self))

        layout.addWidget(button_edades)

        widget.setLayout(layout)
        self.setCentralWidget(widget)