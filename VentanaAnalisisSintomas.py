from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QCheckBox, QLabel, QPushButton, QComboBox


class VentanaAnalisisSintomas(QMainWindow):
    def __init__(self):
        super().__init__()
      
        self.setWindowTitle('Ver análisis según sintomas')
        self.setFixedSize(350, 200)

        widget = QWidget()
        layout = QGridLayout()

        combo_box_label = QLabel('Genero')
        layout.addWidget(combo_box_label, 0,0)
        self.combo_box = QComboBox()
        self.combo_box.addItem("Hombre")
        self.combo_box.addItem("Mujer")
        layout.addWidget(self.combo_box, 1,0)

        sintomas_label = QLabel('Sintomas iniciales')
        layout.addWidget(sintomas_label, 2,0)
        self.sintomas_combo_box = QComboBox()
        self.sintomas_combo_box.addItem("Visual")
        self.sintomas_combo_box.addItem("Sensorial")
        self.sintomas_combo_box.addItem("Motor")
        self.sintomas_combo_box.addItem("Otro")
        self.sintomas_combo_box.addItem("Visual y sensorial")
        self.sintomas_combo_box.addItem("Visual y motor")
        self.sintomas_combo_box.addItem("Visual y otro")
        self.sintomas_combo_box.addItem("Sensorial y Motor")
        self.sintomas_combo_box.addItem("Sensorial y otro")
        self.sintomas_combo_box.addItem("Motor y otro")
        self.sintomas_combo_box.addItem("Visual, sensorial y motor")
        self.sintomas_combo_box.addItem("Visual, sensorial y otro")
        self.sintomas_combo_box.addItem("Visual, motor y otro")
        self.sintomas_combo_box.addItem("Sensorial, motor y otro")
        self.sintomas_combo_box.addItem("Visual, sensorial, motor y otro")
        layout.addWidget(self.sintomas_combo_box, 3,0)
        

        ver_analisis_button = QPushButton('Ver analisis')
        layout.addWidget(ver_analisis_button, 4,0)

        aceptar_button = QPushButton('Volver')
        layout.addWidget(aceptar_button, 5,0)
        aceptar_button.clicked.connect(self.close)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        





