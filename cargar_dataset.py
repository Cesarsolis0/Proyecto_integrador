import pandas as pd
from PyQt6.QtWidgets import QFileDialog , QMessageBox

def cargar_dataset(self):
        # abre una ventana en la cual podemos seleccionar el archivo que contiene el dataset
        ruta_dataset, _ = QFileDialog.getOpenFileName(self, 'Seleccionar archivo CSV', '', 'solo archivos CSV (*.csv)')
        # ,_ desempaqueta la tupla y solo asigna la ruta del archivo a la variable 

        if ruta_dataset:
            self.ver_button.setEnabled(True)
            self.resultados_button.setEnabled(True)
            self.rendimiento_button.setEnabled(True)
            self.tratamiento_button.setEnabled(True)
            self.combo_box.setEnabled(True)

        if ruta_dataset:
            self.dataset = pd.read_csv(ruta_dataset)
            self.combo_box.clear()  #elimina los datos ingresados para añadir los nuevos
            for columna in self.dataset.columns:
                self.combo_box.addItem(columna)
        else:
            QMessageBox.warning(self,"Error","No se ha seleccionado ningun dataset",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            