# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:55:04 2020

@author: NICROMANO
"""

import pandas as pd 
import math
from functools import reduce

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
    return menor, cambiarClave(x), cambiarClave(y)

def cambiarClave(num):
    if num == 0:
        return 'A'
    if num == 1:
        return 'B'
    if num == 2:
        return 'C'
    if num == 3:
        return 'D'
    if num == 4:
        return 'E'
    if num == 5:
        return 'F'
    if num == 6:
        return 'G'
    if num == 7:
        return 'H'
    
def cambiarMatriz(matriz):
    for i in range(0, len(matriz.columns)):
        for j in range(0, i):
            matriz[cambiarClave(j)][cambiarClave(i)] = "--"
    return matriz
            
def calculaDistancia(datos, matriz, metodo):
    fil = []
    for  row1 in range(0, len(data)):
        for row2 in range(0, len(data)):
            for col in range(1, len(data.columns)):
                fil.append(data[col][row1])
                fil.append(data[col][row2])
            matriz[cambiarClave(row1)][cambiarClave(row2)] = metodo(fil)
            fil.clear()
    return matriz
      
if __name__ == '__main__':
    data = pd.read_csv('Dataset.csv', sep=',', header=None)
    matriz_distancia = pd.DataFrame(0.0 ,index=data[0],columns= data[0])
    calculaDistancia(data, matriz_distancia, calcularEuclidean)
    cambiarMatriz(matriz_distancia)
    menor, x, y = encontrarMenor(matriz_distancia)
    
    
    
    

            


    
    