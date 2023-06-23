import pandas as pd
from anytree import Node, RenderTree

data = pd.read_csv('dataset_esclerosis.csv')

root = Node("Root")

for _, row in data.iterrows():
    genero = row['Gender']
    
    genero_node = Node(genero, parent=root)

total_personas = len(data)
total_mujeres_enfermas = sum(data['enfermedad'][data['genero'] == 'mujer'])
total_hombres_enfermos = sum(data['enfermedad'][data['genero'] == 'hombre'])

porcentaje_mujeres_enfermas = (total_mujeres_enfermas / total_personas) * 100
porcentaje_hombres_enfermos = (total_hombres_enfermos / total_personas) * 100

    

