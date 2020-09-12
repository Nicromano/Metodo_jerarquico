# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:49:58 2020

@author: NICROMANO
"""

from Helpers import nVariablesCluster, sumatoriaDistanciaProm

def enlacePromedio(matriz, copia_matriz, x, y, original):
    
    print('Comienzo de iteración')
    for i in range(0, matriz.index.values.tolist().index("({},{})".format(x,y))):
        j = matriz.index.values.tolist()[i]
        Nx = nVariablesCluster(original, "({},{})".format(x,y))
        Ny = nVariablesCluster(original, str(j))
        matriz["({},{})".format(x,y)][j] = (1/(Nx*Ny))*sumatoriaDistanciaProm(original, "({},{})".format(x,y), j)
        print("Total", matriz["({},{})".format(x,y)][j])
    print("fin columnas")
    for i in range(matriz.index.values.tolist().index("({},{})".format(x,y))+1, len(matriz)):
        j = matriz.index.values.tolist()[i]
        Nx = nVariablesCluster(original, "({},{})".format(x,y))
        Ny = nVariablesCluster(original, str(j))
        print("n:", Nx, Ny)
        matriz[j]["({},{})".format(x,y)] = (1/(Nx*Ny))*sumatoriaDistanciaProm(original, j, "({},{})".format(x,y))
        print("Total", matriz[j]["({},{})".format(x,y)])
    print("fin de iteración") 
    print(matriz)
    return matriz
  

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
