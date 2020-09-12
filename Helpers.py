# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:59:17 2020

@author: NICROMANO
"""

def encontrarMenor(matriz):
    menor = max(matriz.max())
    for i in range(0, len(matriz)-1):
        for j in range(i+1, len(matriz.columns)):
            if matriz[cambiarKey(matriz, j)][cambiarKey(matriz, i)] < menor:
                menor = matriz[cambiarKey(matriz, j)][cambiarKey(matriz, i)]
                x = j 
                y = i 
    if x < y:
        return  menor, cambiarKey(matriz, x), cambiarKey( matriz, y)
    return  menor, cambiarKey( matriz, y), cambiarKey(matriz, x)


def obtenerUltimoCluster(matriz):
    return "({},{})".format(list(matriz.columns)[1],matriz.index.values.tolist()[0]) 

def transformarMatriz(matriz):
    for i in range(0, len(matriz.columns)):
        for j in range(0, i):
            matriz[cambiarKey(matriz, j)][cambiarKey(matriz, i)] = "--"
    
    #renombrar columnas y filas
    for i in matriz.index.values.tolist():
        matriz = matriz.rename(columns={i: str(i)})
        matriz = matriz.rename(index={i: str(i)})
    return matriz
 
    
def cambiarKey(matriz, num):
    return matriz.index.values.tolist()[num]
 
def nVariablesCluster(matriz, cluster):
    variables = 0
    cluster = str(cluster)
    for i in matriz.index.values.tolist():
        i = str(i)
        if i in cluster:
            variables = variables +1
    return variables

def sumatoriaDistanciaProm(matriz, x, y):
    distA =[]
    distB = []
    while nVariablesCluster(matriz,x) != 0:
        x, variable = obtenerVariable(matriz, str(x))    
        distA.append(variable)
    while nVariablesCluster(matriz, y) != 0:
        y, variable = obtenerVariable(matriz, str(y))
        distB.append(variable)
        
    suma = 0
    
    for i in distA:
        for j in distB:
            if(matriz[i][j] != '--'):
                suma = suma + matriz[i][j]
            else:
                 suma = suma + matriz[j][i]    
    return suma       
        
def obtenerVariable(matriz, cluster):
    variable = ''
    #print(cluster, variable)
    cluster = str(cluster)
    for i in  matriz.index.values.tolist():
        i = str(i)
        if  i in cluster:
            variable = i
            cluster = cluster.replace(i, '')
            break
    
    return cluster, variable
