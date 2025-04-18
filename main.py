# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 15:02:44 2025

@author: B15S301est
"""

#Simulacro 03
import random
total_encargos=1000
categorias=['Tuberías','Acabados','Cimentación','Estructura','Techos']
min_cantidad=0
max_cantidad=10
#Diccionario para almacenar los encargos
encargos={}

#Generación de las ordenes
for num_encargo in range(total_encargos+1):
    encargo={} #Diccionario para un solo encargo
    for categoria in categorias:
        encargo[categoria]=random.randint(min_cantidad,max_cantidad)
    encargos[f'encargo_{num_encargo}']=encargo
    
#Función para las ordenes especiales
def calcular_total_ordenes(dicc_encargos,criterio):
    encargos_totales=0
    for encargo in dicc_encargos.values():
        valores=list(encargo.values())
        if criterio =='nulas' and valores.count(0)>=2:
            encargos_totales+=1
        elif criterio =='prioritarias' and valores.count(10)>=2:
            encargos_totales+=1
    return encargos_totales

#Conteo de encargos nulos y prioritarios:
nulas=calcular_total_ordenes(encargos,"nulas")
prioritarias=calcular_total_ordenes(encargos,"prioritarias")

#Porcentaje de los encargos
porcentaje_encargos_nulos = (nulas / total_encargos) * 100
porcentaje_encargos_prioritarios = (prioritarias / total_encargos) * 100


print('Resultados de la Simulación')
print(f'Encargos Nulos: {nulas}, lo que equivalen al {porcentaje_encargos_nulos:.2f}%')
print(f'Encargos Prioritarios: {prioritarias}, lo que equivalen al {porcentaje_encargos_prioritarios:.2f}%')