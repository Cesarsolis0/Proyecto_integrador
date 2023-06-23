from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QGridLayout



class VentanaResultados(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ver análisis')

        # Configuramos el tamaño de la ventana
        self.setFixedSize(350, 350)

        widget = QWidget()
        layout = QGridLayout()


        widget.setLayout(layout)
        self.setCentralWidget(widget)

