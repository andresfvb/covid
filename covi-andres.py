# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:46:25 2021
@author: oscar perez
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# Punto 1

num_pais = len(data)
print("P")
print(num_pais)
print() 
num_pais = len(data)
print("P")
print(num_pais)
print()


#////////////////////////////////

# Punto 2

num_muni = len(data.groupby('Nombre municipio').size())
print("P")
print(num_muni)
print() 

num_muni = len(data.groupby('Nombre municipio').size())
print("P")
print(num_muni)
print()

num_muni = len(data.groupby('Nombre municipio').size())
print("P")
print(num_muni)
print()

#////////////////////////////////

# Punto 3

data['Ubicación del caso'].replace('casa','Casa',inplace=True)
data['Ubicación del caso'].replace('CASA','Casa',inplace=True)
num_encasa = len(data[data['Ubicación del caso'] == 'Casa'])
print("Punto 4")
print(num_encasa)
print() 

num_encasa = len(data[data['Ubicación del caso'] == 'Casa'])
print("Punto 4")
print(num_encasa)
print()


#////////////////////////////////
