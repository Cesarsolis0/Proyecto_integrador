import sys
import pandas as pd
from PyQt6.QtWidgets import QWidget , QApplication , QPushButton , QVBoxLayout , QHBoxLayout , QFileDialog , QLabel , QComboBox , QMessageBox

class ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarui()

    def inicializarui(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle("Ventana principal")
        self.contenido()
        self.show()

    def contenido(self):

        cargar_button = QPushButton("Cargar dataset")
        cargar_button.clicked.connect(self.cargar_dataset)

        texto_label = QLabel("Variables")

        self.combo_box = QComboBox()
        self.combo_box.addItem("Variables")

        ver_button = QPushButton("Ver grafico")

        texto2_label = QLabel("Analizar datos")

        resultados_button = QPushButton("Resultados")

        rendimiento_button = QPushButton("Ver rendimiento")

        tratamiento_button = QPushButton("Recomendar tratamiento")
        
        HLayout = QHBoxLayout()
        HLayout.addWidget(self.combo_box)
        HLayout.addWidget(ver_button)

        HLayout1 = QHBoxLayout()
        HLayout1.addWidget(resultados_button)
        HLayout1.addWidget(rendimiento_button)

        Vlayout = QVBoxLayout()
        Vlayout.addWidget(cargar_button)
        Vlayout.addWidget(texto_label)
        Vlayout.addLayout(HLayout)
        Vlayout.addWidget(texto2_label)
        Vlayout.addLayout(HLayout1)
        Vlayout.addWidget(tratamiento_button)
        self.setLayout(Vlayout)

    def cargar_dataset(self):
        # abre una ventana en la cual podemos seleccionar el archivo que contiene el dataset
        ruta_dataset, _ = QFileDialog.getOpenFileName(self, 'Seleccionar archivo CSV', '', 'solo archivos CSV (*.csv)')
        # ,_ desempaqueta la tupla y solo asigna la ruta del archivo a la variable 
        if ruta_dataset != " ":
            dataset = pd.read_csv(ruta_dataset)
            self.combo_box.clear()  #elimina los datos ingresados para añadir los nuevos
            for columna in dataset.columns:
                self.combo_box.addItem(columna)
        else:
            QMessageBox.warning(self,"error","no se ha seleccionado ningun dataset",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ventana()
    sys.exit(app.exec())