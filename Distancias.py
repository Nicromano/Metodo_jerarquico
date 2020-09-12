# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:52:04 2020

@author: NICROMANO
"""

import math
import pandas as pd 
from Helpers import cambiarKey, transformarMatriz

def calcularEuclidean(lista):
    calculo = []
    for i in range(0,len(lista), 2):
        if i+1 < len(lista):
            calculo.append((lista[i]-lista[i+1])**2)
    return math.sqrt(sum(calculo))
    
def calcularManhattan(lista):
    calculo = []
    for i in range(0, len(lista), 2):
        if i+1 < len(lista):
            calculo.append(math.fabs(lista[i]-lista[i+1]))
    return sum(calculo)
     
    
def calcularPearson(lista):
    xi = []
    yi = []
    xy = []
    for i in range(0, len(lista), 2):
        #obtener valores de x
        if(i+1) < len(lista):
            xi.append(lista[i])
            yi.append(lista[i+1])
            xy.append(lista[i]*lista[i+1])
    x2 = sum(list(map(lambda i: i**2, xi)))
    y2 = sum(list(map(lambda i: i**2, yi)))
    xi = sum(xi)
    yi = sum(yi)
    xy = sum(xy)
    m = len(lista)/2
    p = float((xy-(xi*yi/m))/(math.sqrt((x2 - (xi**2/m))*(y2-(yi**2/m)))))
    return  1-p 

                
def calculaDistancia(datos, metodo):
    fil = []
    matriz = pd.DataFrame(0.0 ,index=datos[0],columns= datos[0])
    for  row1 in range(0, len(datos)):
        for row2 in range(0, len(datos)):
            for col in range(1, len(datos.columns)):
                fil.append(datos[col][row1])
                fil.append(datos[col][row2])
            if metodo == 'euclidean':
                matriz[cambiarKey(matriz, row1)][cambiarKey(matriz, row2)] = calcularEuclidean(fil)
            if metodo == 'manhattan':
                matriz[cambiarKey(matriz, row1)][cambiarKey(matriz, row2)] = calcularManhattan(fil)
            if metodo == 'pearson':
                matriz[cambiarKey(matriz, row1)][cambiarKey(matriz, row2)] = calcularPearson(fil)
            fil.clear()
    return transformarMatriz(matriz)
