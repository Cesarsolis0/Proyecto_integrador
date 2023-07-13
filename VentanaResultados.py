from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QGridLayout
import matplotlib.pyplot as plt
import numpy as np
from algoritmos_analisis import *
import time
from VentanaRendimiento import *


class VentanaResultados(QMainWindow):

    def __init__(self, data):
        super().__init__()

        self.dataset = data

        self.setWindowTitle('Ver análisis')

        # Configuramos el tamaño de la ventana
        self.setFixedSize(400, 250)

        widget = QWidget()
        layout = QGridLayout()

        porcentaje_genero_label = QLabel("Género de enfermos (%)")
        porcentaje_genero_button = QPushButton('Ver')
        porcentaje_genero_button.clicked.connect(self.mostrar_grafico_porcentaje_genero)

        porcentaje_sintomas_label = QLabel("Personas con tipos de sintomas iniciales (%)")
        porcentaje_sintomas_button = QPushButton('Ver')
        porcentaje_sintomas_button.clicked.connect(self.mostrar_grafico_porcentaje_sintomas)

        grafico_Edades_label = QLabel("Edades")
        grafico_Edades_button = QPushButton("ver")
        grafico_Edades_button.clicked.connect(self.mostrar_grafico_Edades)

        
        aceptar_button = QPushButton('Volver')
        aceptar_button.clicked.connect(self.close)

        layout.addWidget(porcentaje_genero_label, 0,0)
        layout.addWidget(porcentaje_genero_button, 0,1, 1,4)
        layout.addWidget(porcentaje_sintomas_label, 1,0)
        layout.addWidget(porcentaje_sintomas_button, 1,1, 1,4)
        layout.addWidget(grafico_Edades_label, 2,0)
        layout.addWidget(grafico_Edades_button, 2,1, 1,4)
        layout.addWidget(aceptar_button, 3,1, 1,4)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def mostrar_grafico_porcentaje_genero(self):
        t0 = time.time()
        porcen_mujer = porcentaje_genero_enfermedad(self.dataset, 'mujer')
        porcen_hombre = porcentaje_genero_enfermedad(self.dataset, 'hombre')

        y = np.array([porcen_mujer, porcen_hombre])
        mylabels = ['Mujeres {:.2f}%'.format(porcen_mujer) , 'Hombres {:.2f}%'.format(porcen_hombre) ]

        plt.figure(figsize=(4,3))
        plt.pie(y, labels = mylabels)
        plt.show()
        t1 = time.time()
        self.VentanaRendimiento = VentanaRendimiento('Porcentaje de sintomas iniciales - Listas',f'{t1-t0} segundos')
        self.VentanaRendimiento.show()

    def mostrar_grafico_porcentaje_sintomas(self):
        t0 = time.time()
        porcentaje_sintomas_iniciales(self.dataset)
        t1 = time.time()
        self.VentanaRendimiento = VentanaRendimiento('Porcentaje de sintomas iniciales - Listas',f'{t1-t0} segundos')
        self.VentanaRendimiento.show()


    def mostrar_grafico_Edades(self):
        t0 = time.time()
        mostrar_edades(self.dataset)
        t1 = time.time()
        self.VentanaRendimiento = VentanaRendimiento('Porcentaje de edades - tuplas',f'{t1-t0} segundos')
        self.VentanaRendimiento.show()


    




    



        
