import pandas as pd
#Primero se importa pandas para el tratamiento del Dataset
# Cargar el archivo CSV en un DataFrame


def eliminar_columnas_innecesarias(dataset):

    # Obtener los nombres de las columnas a eliminar
    columnas_a_eliminar = ['Id','Schooling','Breastfeeding', 'Varicella', 'Mono_or_Polysymptomatic', 'Oligoclonal_Bands', 'LLSSEP', 'ULSSEP', 'VEP', 'BAEP', 'Periventricular_MRI', 'Cortical_MRI', 'Infratentorial_MRI', 'Spinal_Cord_MRI', 'Initial_EDSS', 'Final_EDSS', 'group']

    # Eliminar las columnas del DataFrame
    dataset = dataset.drop(columnas_a_eliminar, axis=1)

    return dataset

def cantidad_nulos(dataset, columna=None):
    data = dataset
    if columna == None:
        nulos = data.isnull()
        cantidad_nulos = nulos.sum()
        total_nulos = cantidad_nulos.sum()
        return total_nulos
    else:
        cantidad_nulos_columna = data[columna].isnull().sum()
        return cantidad_nulos_columna





