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
