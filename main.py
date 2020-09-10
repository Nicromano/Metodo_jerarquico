# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:55:04 2020

@author: NICROMANO
"""

import pandas as pd 
import math
from functools import reduce

data = pd.read_csv('Dataset.csv', sep=',', header=None)
#data = pd.read_csv('data.csv', sep=',', header=None)

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
    menor = max(matriz.max())
    for i in range(0, len(matriz)-1):
        for j in range(i+1, len(matriz.columns)):
            if matriz[cambiarKey(matriz, j)][cambiarKey(matriz, i)] < menor:
                menor = matriz[cambiarKey(matriz, j)][cambiarKey(matriz, i)]
                x = j 
                y = i 
    if x < y:
        return  cambiarKey(matriz, x), cambiarKey( matriz, y)
    return  cambiarKey( matriz, y), cambiarKey(matriz, x)

def enlacePromedio(matriz, copia_matriz, x, y):
    
    #encontrar cuantas variables hay en cada cluster a unir
    Nx = nVariablesCluster(x)
    Ny = nVariablesCluster(y)
    
    pass

def nVariablesCluster(cluster):
    variables = 0
    for i in data[0]:
        if i in cluster:
            variables = variables +1
    return variables
    
def enlaceCompleto(matriz, matriz_copia, x, y):
    for i in range(0, matriz.index.values.tolist().index("({},{})".format(x,y))):
        j = matriz.index.values.tolist()[i]
        if matriz_copia[x][j] != '--':
            if matriz_copia[y][j] != '--':
                if matriz_copia[x][j] > matriz_copia[y][j]:
                    matriz["({},{})".format(x,y)][i] = matriz_copia[x][j] 
                else: 
                    matriz["({},{})".format(x,y)][i] = matriz_copia[y][j] 
            else:
                if matriz_copia[x][j] > matriz_copia[j][y]:
                    matriz["({},{})".format(x,y)][i] = matriz_copia[x][j] 
                else: 
                    matriz["({},{})".format(x,y)][i] = matriz_copia[j][y]
        else:
            if matriz_copia[y][j] != '--':
                if matriz_copia[j][x] > matriz_copia[y][j]:
                    matriz["({},{})".format(x,y)][i] = matriz_copia[j][x] 
                else: 
                    matriz["({},{})".format(x,y)][i] = matriz_copia[y][j] 
            else:
                if matriz_copia[j][x] > matriz_copia[j][y]:
                    matriz["({},{})".format(x,y)][i] = matriz_copia[j][x] 
                else: 
                    matriz["({},{})".format(x,y)][i] = matriz_copia[j][y] 
                
                
    for i in range(matriz.index.values.tolist().index("({},{})".format(x,y))+1, len(matriz)):
        j = matriz.index.values.tolist()[i]
        if matriz_copia[j][x] != '--':
            if matriz_copia[y][j] != '--':
                if matriz_copia[j][x] > matriz_copia[y][j]:
                    matriz[j]["({},{})".format(x,y)] = matriz_copia[j][x]
                else:
                    matriz[j]["({},{})".format(x,y)] = matriz_copia[y][j]
            else:
                if matriz_copia[j][x] > matriz_copia[j][y]:
                    matriz[j]["({},{})".format(x,y)] = matriz_copia[j][x]
                else:
                    matriz[j]["({},{})".format(x,y)] = matriz_copia[j][y]
        else:
            if matriz_copia[y][j] != '--':
                if matriz_copia[x][j] > matriz_copia[y][j]:
                    matriz[j]["({},{})".format(x,y)] = matriz_copia[x][j]
                else:
                    matriz[j][ "({},{})".format(x,y)] = matriz_copia[y][j]
            else: 
                if matriz_copia[x][j] > matriz_copia[j][y]:
                    matriz[j][ "({},{})".format(x,y)] = matriz_copia[x][j]
                else:
                    matriz[j][ "({},{})".format(x,y)] = matriz_copia[j][y]
    return matriz


def enlaceSimple(matriz, matriz_copia, x, y):
    for i in range(0, matriz.index.values.tolist().index("({},{})".format(x,y))):
        j = matriz.index.values.tolist()[i]
        if matriz_copia[x][j] != '--':
            if matriz_copia[y][j] != '--':
                if matriz_copia[x][j] < matriz_copia[y][j]:
                    matriz["({},{})".format(x,y)][i] = matriz_copia[x][j] 
                else: 
                    matriz["({},{})".format(x,y)][i] = matriz_copia[y][j] 
            else:
                if matriz_copia[x][j] < matriz_copia[j][y]:
                    matriz["({},{})".format(x,y)][i] = matriz_copia[x][j] 
                else: 
                    matriz["({},{})".format(x,y)][i] = matriz_copia[j][y]
        else:
            if matriz_copia[y][j] != '--':
                if matriz_copia[j][x] < matriz_copia[y][j]:
                    matriz["({},{})".format(x,y)][i] = matriz_copia[j][x] 
                else: 
                    matriz["({},{})".format(x,y)][i] = matriz_copia[y][j] 
            else:
                if matriz_copia[j][x] < matriz_copia[j][y]:
                    matriz["({},{})".format(x,y)][i] = matriz_copia[j][x] 
                else: 
                    matriz["({},{})".format(x,y)][i] = matriz_copia[j][y] 
                
                
    for i in range(matriz.index.values.tolist().index("({},{})".format(x,y))+1, len(matriz)):
        j = matriz.index.values.tolist()[i]
        if matriz_copia[j][x] != '--':
            if matriz_copia[y][j] != '--':
                if matriz_copia[j][x] < matriz_copia[y][j]:
                    matriz[j]["({},{})".format(x,y)] = matriz_copia[j][x]
                else:
                    matriz[j]["({},{})".format(x,y)] = matriz_copia[y][j]
            else:
                if matriz_copia[j][x] < matriz_copia[j][y]:
                    matriz[j]["({},{})".format(x,y)] = matriz_copia[j][x]
                else:
                    matriz[j]["({},{})".format(x,y)] = matriz_copia[j][y]
        else:
            if matriz_copia[y][j] != '--':
                if matriz_copia[x][j] < matriz_copia[y][j]:
                    matriz[j]["({},{})".format(x,y)] = matriz_copia[x][j]
                else:
                    matriz[j][ "({},{})".format(x,y)] = matriz_copia[y][j]
            else: 
                if matriz_copia[x][j] < matriz_copia[j][y]:
                    matriz[j][ "({},{})".format(x,y)] = matriz_copia[x][j]
                else:
                    matriz[j][ "({},{})".format(x,y)] = matriz_copia[j][y]
    return matriz        

def cambiarClave(num):
    return data[0][num]

def cambiarKey(matriz, num):
    return matriz.index.values.tolist()[num]
 
                
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

    return transformarMatriz(matriz)

def transformarMatriz(matriz):
    for i in range(0, len(matriz.columns)):
        for j in range(0, i):
            matriz[cambiarKey(matriz, j)][cambiarKey(matriz, i)] = "--"
    return matriz
    
def obtenerUltimoCluster(matriz):
    return "({},{})".format(list(matriz.columns)[1],matriz.index.values.tolist()[0]) 
    
def agruparCluster(matriz, enlace):
    matriz_copia = matriz
    x, y = encontrarMenor(matriz)
    matriz = matriz.drop([y], axis=1)
    matriz = matriz.drop([y], axis=0)
    matriz = matriz.rename(columns={x: "({},{})".format(x,y)})
    matriz = matriz.rename(index={x: "({},{})".format(x,y)})
    matriz = enlace(matriz, matriz_copia, x, y)
    
    return matriz, obtenerUltimoCluster(matriz)

    
if __name__ == '__main__':
    #matriz_distancia =  data #calculaDistancia(data, calcularEuclidean)
    #print(matriz_distancia)
    #matriz_distancia = transformarMatriz(matriz_distancia)
    #print(matriz_distancia)
    
 
    #while len(matriz_distancia) != 2:
        #matriz_distancia, cluster = agruparCluster(matriz_distancia, enlaceCompleto)
    #print(matriz_distancia)
    #print("Ultimo cluster", cluster)
    
    
    
    
    
    
    
    

            


    
    