
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QHeaderView, QWidget, QGridLayout, QTableWidgetItem, QTableWidget
from PyQt6.QtCore import Qt

class VentanaRendimiento(QMainWindow):
    def __init__(self, metodo, tiempo):
        super().__init__()

        self.setWindowTitle('Ver rendimiento')
        self.setFixedSize(470, 100)

        self.metodo = metodo
        self.tiempo = tiempo

        widget = QWidget()
        layout = QGridLayout()
        
        #tabla
        self.table = QTableWidget(0, 2) 

        self.table.setHorizontalHeaderLabels(["Método", "Tiempo de ejecución"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.agregar_fila_tabla(self.metodo, self.tiempo)

    
        layout.addWidget(self.table)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def agregar_fila_tabla(self, metodo, tiempo):

            # Agrega una fila
            row = self.table.rowCount()
            self.table.insertRow(row)
            
            # Agrega elementos a las celdas
            item1 = QTableWidgetItem(metodo)
            item1.setFlags(item1.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 0, item1)

            item2 = QTableWidgetItem(tiempo)
            item2.setFlags(item2.flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.table.setItem(row, 1, item2)





        



