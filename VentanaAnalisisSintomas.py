from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QCheckBox, QLabel, QPushButton, QComboBox

class VentanaAnalisisSintomas(QMainWindow):
    def __init__(self):
        super().__init__()
      
        self.setWindowTitle('Ver análisis según sintomas')
        self.setFixedSize(350, 350)

        widget = QWidget()
        layout = QGridLayout()

        combo_box_label = QLabel('Genero')
        layout.addWidget(combo_box_label, 0,0)
        self.combo_box = QComboBox()
        self.combo_box.addItem("Hombre")
        self.combo_box.addItem("Mujer")
        layout.addWidget(self.combo_box, 1,0)

        checkbox_label = QLabel('Sintomas iniciales')
        layout.addWidget(checkbox_label, 2,0)
        checkbox1 = QCheckBox('Visual')
        layout.addWidget(checkbox1, 3,0)
        checkbox2 = QCheckBox('Sensorial')
        layout.addWidget(checkbox2, 4,0)
        checkbox3 = QCheckBox('Motor')
        layout.addWidget(checkbox3, 5,0)
        checkbox4 = QCheckBox('Otro')
        layout.addWidget(checkbox4, 6,0)

        ver_analisis_button = QPushButton('Aceptar')
        layout.addWidget(ver_analisis_button, 7,0)


        aceptar_button = QPushButton('Aceptar')
        layout.addWidget(aceptar_button, 7,0)
        aceptar_button.clicked.connect(self.close)

        


        widget.setLayout(layout)
        self.setCentralWidget(widget)

        





