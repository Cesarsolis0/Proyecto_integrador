import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#Calcular porcentajes de mujeres y hombres con la enfermedad (uso de listas)

def porcentaje_genero_enfermedad(data, genero_str):
    mujeres_enfermas = []
    hombres_enfermos = []

    for _, row in data.iterrows():
        genero = row['Gender']

        if genero == 2:
            mujeres_enfermas.append(row)
        elif genero == 1:
            hombres_enfermos.append(row)

    total_personas = len(data)  
    total_mujeres = len(mujeres_enfermas)
    total_hombres = len(hombres_enfermos)

    porcentaje_mujeres_enfermas = (total_mujeres / total_personas) * 100
    porcentaje_hombres_enfermos = (total_hombres / total_personas) * 100

    if genero_str == 'hombre':
        return porcentaje_hombres_enfermos
    elif genero_str == 'mujer':
        return porcentaje_mujeres_enfermas

def porcentaje_sintomas_iniciales(data):
    # Initial_Symptoms: 1=visual, 2=sensory, 3=motor, 4=other, 
    # 5= visual and sensory, 6=visual and motor, 7=visual and 
    # others, 8=sensory and motor, 9=sensory and other, 10=motor 
    # and other, 11=Visual, sensory and motor, 12=visual, sensory 
    # and other, 13=Visual, motor and other, 14=Sensory, motor and 
    # other, 15=visual,sensory,motor and other

    lista_porcentajes = []

    for i in range(1, 16):
        sintomas_iniciales = data['Initial_Symptom'].tolist()
        sintoma_objetivo = i  
        cantidad_sintoma = sintomas_iniciales.count(sintoma_objetivo)

        total_personas = len(sintomas_iniciales)
        porcentaje = (cantidad_sintoma / total_personas) * 100

        lista_porcentajes.append(porcentaje)

    

    y = np.array(lista_porcentajes)


    mylabels = ['Visual {:.2f}%'.format(lista_porcentajes[0]), 'sensory {:.2f}%'.format(lista_porcentajes[1]), 'motor {:.2f}%'.format(lista_porcentajes[2]), 'other {:.2f}%'.format(lista_porcentajes[3]), 'visual and sensory {:.2f}%'.format(lista_porcentajes[4]),
                 'visual and motor {:.2f}%'.format(lista_porcentajes[5]), 'visual and others {:.2f}%'.format(lista_porcentajes[6]), 'sensory and motor {:.2f}%'.format(lista_porcentajes[7]), 
                 'sensory and other {:.2f}%'.format(lista_porcentajes[8]), 'motor and other {:.2f}%'.format(lista_porcentajes[9]), 'Visual, sensory and motor {:.2f}%'.format(lista_porcentajes[10]),
                 'visual, sensory and other {:.2f}%'.format(lista_porcentajes[11]), 'Visual, motor and other {:.2f}%'.format(lista_porcentajes[12]), 'Sensory, motor and other {:.2f}%'.format(lista_porcentajes[13]),
                 'visual,sensory,motor and other {:.2f}%'.format(lista_porcentajes[14])]
    
    plt.figure(figsize=(4,3))
    plt.pie(y, labels = mylabels)
    plt.show()

def mostrar_edades(data):
    #selecionamos todas las filas del dataset,y la tercera columna con el index 2 para obtener la informacion 
    # de la tercera columna y guardarla en una tupla
    tercera_columna = tuple(data['Age'])

    numdepersonas = len(data['Age'])

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

    
    




    

    

    

    

    






