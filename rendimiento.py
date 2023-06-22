import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTableWidget, QHeaderView, QWidget, QGridLayout

# Definimos una clase que hereda de QMainWindow
class VentanaRendimiento(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ver rendimiento')

        # Configuramos el tamaño de la ventana
        self.setFixedSize(350, 350)

        widget = QWidget()
        layout = QGridLayout()

        #tabla
        self.table = QTableWidget(0, 2) 

        self.table.setHorizontalHeaderLabels(["Método", "Tiempo de ejecución"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout.addWidget(self.table)

        widget.setLayout(layout)
        self.setCentralWidget(widget)


# app = QApplication(sys.argv)

# ventana = VentanaRendimiento()

# ventana.show()

# sys.exit(app.exec())
