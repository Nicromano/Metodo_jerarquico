# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:55:04 2020

@author: NICROMANO
"""

import pandas as pd 
import math
from Distancias import calculaDistancia
from Jerarquico import agruparCluster
from Helpers import transformarMatriz


if __name__ == '__main__':
    data = pd.read_csv('data.csv', sep=',', header=None)
    matriz_distancia = transformarMatriz(data) #calculaDistancia(data, 'euclidean')
    print(matriz_distancia)
    copia_matriz = matriz_distancia
    while len(matriz_distancia) != 2:
        matriz_distancia, cluster = agruparCluster(matriz_distancia, 'promedio', copia_matriz)
    print(matriz_distancia)
    print(cluster)
    
    
    
    
    
    
    
    

            


    
    