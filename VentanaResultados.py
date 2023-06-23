from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QGridLayout
import matplotlib.pyplot as plt
import numpy as np
from algoritmos_analisis import *


class VentanaResultados(QMainWindow):

    def __init__(self):
        super().__init__()

        self.dataset = pd.read_csv('dataset_esclerosis.csv')

        self.setWindowTitle('Ver análisis')

        # Configuramos el tamaño de la ventana
        self.setFixedSize(350, 350)

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

        
        aceptar_button = QPushButton('Aceptar')
        aceptar_button.clicked.connect(self.close)

        
        layout.addWidget(porcentaje_genero_label, 0,0)
        layout.addWidget(porcentaje_genero_button, 0,1)
        layout.addWidget(porcentaje_sintomas_label, 1,0)
        layout.addWidget(porcentaje_sintomas_button, 1,1)
        layout.addWidget(grafico_Edades_label, 2,0)
        layout.addWidget(grafico_Edades_button, 2,1)
        layout.addWidget(aceptar_button, 3,0)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def mostrar_grafico_porcentaje_genero(self):

        porcen_mujer = porcentaje_genero_enfermedad(self.dataset, 'mujer')
        porcen_hombre = porcentaje_genero_enfermedad(self.dataset, 'hombre')

        y = np.array([porcen_mujer, porcen_hombre])
        mylabels = ['Mujeres {:.2f}%'.format(porcen_mujer) , 'Hombres {:.2f}%'.format(porcen_hombre) ]

        plt.figure(figsize=(4,3))
        plt.pie(y, labels = mylabels)
        plt.show()

    def mostrar_grafico_porcentaje_sintomas(self):
        porcentaje_sintomas_iniciales(self.dataset)

    def mostrar_grafico_Edades(self):
        mostrar_edades(self.dataset)



    



        
