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
from scipy.cluster import hierarchy
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv('data.csv', sep=',', header=None)
    matriz_distancia = transformarMatriz(data) #calculaDistancia(data, 'euclidean')
    copia_matriz = matriz_distancia
    matriz_result, cluster = agruparCluster(matriz_distancia, 'promedio', copia_matriz)
    print(cluster)

    
    
    ytdist = np.array([662., 877., 255., 412., 996., 295., 468., 268., 400., 754., 564., 138., 219., 869., 669.])
    Z = hierarchy.linkage(ytdist, 'single')
    plt.figure()
    print(type(Z))
    print(Z)
    dn = hierarchy.dendrogram(Z)
   
    

    
    
    
    
    
    
    
    
    

            


    
    