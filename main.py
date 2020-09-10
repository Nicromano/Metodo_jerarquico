# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:55:04 2020

@author: NICROMANO
"""

import pandas as pd 
import math
from functools import reduce

data = pd.read_csv('Dataset.csv', sep=',', header=None)

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
            calculo.append( math.fabs(lista[i]-lista[i+1]))
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

def encontrarMenor(matriz):
    menor = matriz['B']['A']
    for i in range(0, len(matriz)):
        for j in  range(0, len(matriz.columns)):
            if (i != j ) and (matriz[cambiarClave(j)][cambiarClave(i)] != '--') and (matriz[cambiarClave(j)][cambiarClave(i)] < menor):
                menor = matriz[cambiarClave(j)][cambiarClave(i)]
                x = j 
                y = i 
    if x < y:
        return menor, cambiarClave(x), cambiarClave(y)
    return menor, cambiarClave(y), cambiarClave(x)

def cambiarClave(num):
    return data[0][num]
 
                
def calculaDistancia(datos, metodo):
    fil = []
    matriz = pd.DataFrame(0.0 ,index=data[0],columns= data[0])
    for  row1 in range(0, len(data)):
        for row2 in range(0, len(data)):
            for col in range(1, len(data.columns)):
                fil.append(data[col][row1])
                fil.append(data[col][row2])
            matriz[cambiarClave(row1)][cambiarClave(row2)] = metodo(fil)
            fil.clear()
    for i in range(0, len(matriz.columns)):
        for j in range(0, i):
            matriz[cambiarClave(j)][cambiarClave(i)] = "--"
    return matriz
  
def agruparCluster(matriz):
    matriz_copia = matriz
    print(matriz_copia)
    menor, x, y = encontrarMenor(matriz)
    matriz = matriz.drop([y], axis=1)
    matriz = matriz.drop([y], axis=0)
    matriz = matriz.rename(columns={x: "{},{}".format(x,y)})
    matriz = matriz.rename(index={x: "{},{}".format(x,y)})
    
    for i in range(0, matriz_distancia.index.values.tolist().index(x)):
        j = matriz_distancia.index.values.tolist()[i]
        print(matriz_copia[x][j], matriz_copia[y][j])
        if matriz_copia[x][j] < matriz_copia[y][j]:
            matriz["{},{}".format(x,y)][i] = matriz_copia[x][j] 
        else: 
            matriz["{},{}".format(x,y)][i] = matriz_copia[y][j] 
            
    print(matriz)
    
if __name__ == '__main__':
    matriz_distancia = calculaDistancia(data, calcularEuclidean)
    agruparCluster(matriz_distancia)
    
    
    
    
    
    
    

            


    
    