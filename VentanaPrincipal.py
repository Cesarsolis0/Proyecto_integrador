import sys
import pandas as pd
from PyQt6.QtWidgets import QWidget , QApplication , QPushButton, QFileDialog , QLabel , QComboBox , QMessageBox, QGridLayout, QMainWindow
import matplotlib.pyplot as plt
from VentanaRendimiento import *
from VentanaResultados import *
from VentanaAnalisisSintomas import *
from tratamiento_dataset import *


class VentanaPrincipal(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.inicializarui()
        self.dataset_original = None
        self.dataset_tratado = None

    def inicializarui(self):
        self.setFixedSize(350,400)
        self.setWindowTitle("Ventana principal")
        self.contenido()
        self.show()

    def contenido(self):

        widget = QWidget()
        grid_layout = QGridLayout()

        self.cargar_button = QPushButton("Cargar dataset",self)
        self.cargar_button.setFixedSize(335,60)
        self.cargar_button.clicked.connect(self.cargar_dataset)
        

        texto_label = QLabel("Todas las Variables")

        self.combo_box = QComboBox()
        self.combo_box.addItem("Variables")
        self.combo_box.setEnabled(False)

        variables_filtradas_label = QLabel("variables filtradas")
        self.variables_filtradas_combo_box = QComboBox()
        self.variables_filtradas_combo_box.addItem("Variables")
        self.variables_filtradas_combo_box.setEnabled(False)

        self.nulos_label = QLabel("Cantidad de Nulos:")
        self.nulos_Age_label = QLabel("Cantidad de Nulos edad:")
        self.nulos_genero_label = QLabel("Cantidad de Nulos genero:")
        self.nulos_sintomas_label = QLabel("Cantidad de Nulos sintomas iniciales:")


        texto2_label = QLabel("Analizar datos")

        self.resultados_button = QPushButton("Ver análisis")
        self.resultados_button.clicked.connect(self.mostrar_ventana_resultados)
        self.resultados_button.setEnabled(False)


        self.tratamiento_button = QPushButton("Analisis según sintomas")
        self.tratamiento_button.clicked.connect(self.mostrar_ventana_analisis_sint)
        self.tratamiento_button.setEnabled(False)

        grid_layout.addWidget(self.cargar_button,0,0,2,2)
        grid_layout.addWidget(texto_label,1,0,3,1)
        grid_layout.addWidget(self.combo_box,2,0,2,1)
        grid_layout.addWidget(variables_filtradas_label,1,1,3,1)
        grid_layout.addWidget(self.variables_filtradas_combo_box,2,1,2,1)
        grid_layout.addWidget(self.nulos_label,3,0,3,2)
        grid_layout.addWidget(self.nulos_Age_label,4,0,3,2)
        grid_layout.addWidget(self.nulos_genero_label,5,0,3,2)
        grid_layout.addWidget(self.nulos_sintomas_label,6,0,3,2)
        grid_layout.addWidget(texto2_label,7,0,3,2)
        grid_layout.addWidget(self.resultados_button,8,0,2,1)
        grid_layout.addWidget(self.tratamiento_button,8,1,2,1)
        # grid_layout.addWidget(self.tratamiento_button,5,0,2,1)

        widget.setLayout(grid_layout)
        self.setCentralWidget(widget)


    def cargar_dataset(self):
        # abre una ventana en la cual podemos seleccionar el archivo que contiene el dataset
        ruta_dataset, _ = QFileDialog.getOpenFileName(self, 'Seleccionar archivo CSV', '', 'solo archivos CSV (*.csv)')
        # ,_ desempaqueta la tupla y solo asigna la ruta del archivo a la variable 

        if ruta_dataset:
            self.variables_filtradas_combo_box.setEnabled(True)
            self.resultados_button.setEnabled(True)
            self.tratamiento_button.setEnabled(True)
            self.combo_box.setEnabled(True)

        if ruta_dataset:
            self.dataset_original = pd.read_csv(ruta_dataset)
            self.combo_box.clear()  #elimina los datos ingresados para añadir los nuevos
            for columna in self.dataset_original.columns:
                self.combo_box.addItem(columna)

            self.dataset_tratado = eliminar_columnas_innecesarias(self.dataset_original)
            self.variables_filtradas_combo_box.clear()
            for columna in self.dataset_tratado.columns:
                self.variables_filtradas_combo_box.addItem(columna)
            
            self.nulos_label.setText(f"Cantidad de Nulos: {cantidad_nulos(self.dataset_tratado)}")
            self.nulos_Age_label.setText(f"Cantidad de Nulos en Edad: {cantidad_nulos(self.dataset_tratado, 'Age')}")
            self.nulos_genero_label.setText(f"Cantidad de Nulos genero: {cantidad_nulos(self.dataset_tratado, 'Gender')}")
            self.nulos_sintomas_label.setText(f"Cantidad de Nulos sintomas iniciales: {cantidad_nulos(self.dataset_tratado, 'Initial_Symptom')}")

        else:
            QMessageBox.warning(self,"Error","No se ha seleccionado ningun dataset",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
    def mostrar_ventana_resultados(self):
        self.ventana_resultados = VentanaResultados(self.dataset_tratado)
        self.ventana_resultados.show()
        
    def mostrar_ventana_analisis_sint(self):
        self.ventana_analisis_sint = VentanaAnalisisSintomas()
        self.ventana_analisis_sint.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaPrincipal()
    sys.exit(app.exec())

