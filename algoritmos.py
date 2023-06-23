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

print(f"Total de personas: {total_personas}")
print(f"Total de mujeres enfermas: {total_mujeres_enfermas}")
print(f"Total de hombres enfermos: {total_hombres_enfermos}")
print(f"Porcentaje de mujeres enfermas: {porcentaje_mujeres_enfermas}%")
print(f"Porcentaje de hombres enfermos: {porcentaje_hombres_enfermos}%")
    

