# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:55:04 2020

@author: NICROMANO
"""

import pandas as pd 

from Distancias import calculaDistancia
from Jerarquico import agruparCluster


if __name__ == '__main__':
    data = pd.read_csv('data.csv', sep=',', header=None)
    print(data)
    matriz_distancia = data #calculaDistancia(data, "euclidean")
    print(matriz_distancia)
    matriz_result, cluster, agrupaciones = agruparCluster(matriz_distancia, 'promedio')
    print("Matriz resultante: ")
    print(matriz_result)
    print("Cluster: ")
    print(cluster)
    print("Agrupaciones: ")
    print(agrupaciones)
    
   
    
    
    
    
    
    
    
    

            


    
    