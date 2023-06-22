import sys
from PyQt6.QtWidgets import QWidget , QApplication , QPushButton , QVBoxLayout , QHBoxLayout , QLabel , QComboBox , QGridLayout, QMainWindow
from rendimiento import *
from cargar_dataset import cargar_dataset
from grafico_general import mostrar_grafico_general


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializarui()
        self.dataset = None

    def inicializarui(self):
        self.setFixedSize(350,350)
        self.setWindowTitle("Ventana principal")
        self.contenido()
        self.show()

    def contenido(self):

        widget = QWidget()
        grid_layout = QGridLayout()

        cargar_button = QPushButton("Cargar dataset")
        cargar_button.clicked.connect(lambda:cargar_dataset(self)) #lambda es una funcion anonima que recibe el metodo carhar dataset con el fin de no declarar una funcion y ahorrar lineas 

        texto_label = QLabel("Variables")

        self.combo_box = QComboBox()
        self.combo_box.addItem("Variables")

        ver_button = QPushButton("Ver grafico")
        ver_button.clicked.connect(lambda:mostrar_grafico_general(self))

        texto2_label = QLabel("Analizar datos")

        resultados_button = QPushButton("Resultados")

        rendimiento_button = QPushButton("Ver rendimiento")
        rendimiento_button.clicked.connect(self.mostrar_ventana_rendimiento)



        tratamiento_button = QPushButton("Recomendar tratamiento")

        grid_layout.addWidget(cargar_button,0,0,2,2)
        grid_layout.addWidget(texto_label,1,0,3,1)
        grid_layout.addWidget(self.combo_box,2,0,2,1)
        grid_layout.addWidget(ver_button,2,1,2,1)
        grid_layout.addWidget(texto2_label,3,0,3,1)
        grid_layout.addWidget(resultados_button,4,0,2,1)
        grid_layout.addWidget(rendimiento_button,4,1,2,1)
        grid_layout.addWidget(tratamiento_button,5,0,2,1)
        

        widget.setLayout(grid_layout)
        self.setCentralWidget(widget)

        
        # HLayout = QHBoxLayout()
        # HLayout.addWidget(self.combo_box)
        # HLayout.addWidget(ver_button)

        # HLayout1 = QHBoxLayout()
        # HLayout1.addWidget(resultados_button)
        # HLayout1.addWidget(rendimiento_button)

        # Vlayout = QVBoxLayout()
        # Vlayout.addWidget(cargar_button)
        # Vlayout.addWidget(texto_label)
        # Vlayout.addLayout(HLayout)
        # Vlayout.addWidget(texto2_label)
        # Vlayout.addLayout(HLayout1)
        # Vlayout.addWidget(tratamiento_button)
        # self.setLayout(Vlayout)

    def mostrar_ventana_rendimiento(self):
        self.ventana_rendimiento = VentanaRendimiento()
        self.ventana_rendimiento.show()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    sys.exit(app.exec())


