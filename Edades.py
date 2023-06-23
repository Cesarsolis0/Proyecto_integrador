import pandas as pd
import matplotlib.pyplot as plt

def mostrar_edades(self):

    dataset = pd.read_csv("dataset_esclerosis.csv")

    tercera_columna = tuple(dataset.iloc[:, 2])

    numdepersonas = len(tercera_columna)

    # Calcular la edad menor, mayor y media
    edad_menor = min(tercera_columna)
    edad_mayor = max(tercera_columna)
    media_edad = round(sum(tercera_columna) / numdepersonas)

    # Crear el gráfico de barras
    plt.bar(range(numdepersonas), tercera_columna)

    # Resaltar la edad menor, mayor y media
    plt.axhline(y=edad_menor, color='r', linestyle='--', label='Edad Menor')
    plt.axhline(y=edad_mayor, color='y', linestyle='--', label='Edad Mayor')
    plt.axhline(y=media_edad, color='g', linestyle='--', label='Edad Media')

    #asignar los label que apareceran en pantalla
    plt.xlabel('Índice de personas')
    plt.ylabel('Edad')
    plt.title('Edades de las personas')

    plt.legend()
    plt.show()
