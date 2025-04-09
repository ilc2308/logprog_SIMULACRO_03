# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 08:08:09 2025

@author: B09S205est
"""

#Simulacro
import random
def calcular_total_ordenes(diccionario, criterio):
    total_encargos = 0

    # Definición del valor según el criterio
    if criterio == 'nulas':
        valor_rastreado = 0
    elif criterio == 'prioritaria':
        valor_rastreado = 10
    else:
        # Si el criterio no es válido, devolvemos un mensaje de error o simplemente 0
       return "Criterio no válido."


    # Comprobar si hay al menos un encargo en el diccionario
    if not diccionario:
        return total_encargos  # Si el diccionario está vacío, no hay encargos

    # Se determina cuántas categorías se examinarán
    llave1 = list(diccionario.keys())[0]  # Obtener la primera llave disponible
    total_categorias = len(diccionario[llave1].keys())  # Número de categorías en la primera orden

    # Aquí se cuenta cuántos encargos tienen el valor buscado en todas sus categorías
    for encargo in diccionario.keys():
        valores_encontrados = 0

        # Revisamos para cada categoría si tiene el valor buscado
        for categoria in diccionario[encargo].keys():
            if diccionario[encargo][categoria] == valor_rastreado:
                valores_encontrados += 1

        # Si la cantidad de valores encontrados coincide con la cantidad de categorías
        # Esa orden cumple con el criterio de contabilización
        if valores_encontrados == total_categorias:
            total_encargos += 1

    return total_encargos

#Función Principal
total_encargos=1000
categorias=['Tuberías','Acabados','Cimentación','Estructura','Techos']
min_cantidad=0
max_cantidad=10

print('Un programa para simular la creación de pedidos de materiales de construcción.')
print(f'Se simularán {total_encargos} en las siguientes categorias:')

for seccion in categorias:
    print(f'- {seccion}')

#Diccionario de los encargos
dicc_encargos={}

#Generación de los encargos
print('\nDetalle de las ordenes simuladas:')
for encargo in range(total_encargos):
    requisicion = {}
    for una_seccion in categorias:
        cantidad = random.randint(min_cantidad, max_cantidad)
        requisicion[una_seccion] = cantidad

    #Colocamos el número de orden como una cadena de caracteres
    # para que funcione como llave del diccionario
    dicc_encargos[str(encargo+1)] = requisicion
    
print(f'El diccionario de encargos tiene {len(dicc_encargos)} encargos')

#Visualizamos el contenido del diccionario
for llave in dicc_encargos.keys():
    print(f'Orden No. {llave}:')
    for rubro_producto in dicc_encargos[llave]:
        print(f'\t- {rubro_producto}: {dicc_encargos[llave][rubro_producto]}')
    
#Totalización de los encargos

total_encargos_nulos = calcular_total_ordenes(dicc_encargos, 'nulas')
total_encargos_prioritarios = calcular_total_ordenes(dicc_encargos, 'prioritaria')

#Porcentaje de los encargos
porcentaje_encargos_nulos = (total_encargos_nulos / total_encargos) * 100
porcentaje_encargos_prioritarios = (total_encargos_prioritarios / total_encargos) * 100

print('\n*** Resultados ***')
print(f'Total encargos nulos: {total_encargos_nulos}, que equivalen al {porcentaje_encargos_nulos:.2f} %')
print(f'Total encargos proritarios: {total_encargos_prioritarios}, que equivalen al {porcentaje_encargos_prioritarios:.2f} %')
    
    