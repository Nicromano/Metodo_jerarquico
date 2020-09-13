# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:49:35 2020

@author: NICROMANO
"""

from Helpers import  encontrarMenor, nVariablesCluster, esMatrizTransformada, transformarMatriz
from Enlaces import enlacePromedio, enlaceCompleto, enlaceSimple
from Distancias import calculaDistancia

def agruparCluster(matriz, enlace, metodo = None):
    cluster = []
    if metodo != None:
        matriz = calculaDistancia(matriz, metodo)
    if not esMatrizTransformada(matriz):
        matriz = transformarMatriz(matriz)
    copia = matriz
    while(len(matriz)!=2):
        matriz_copia = matriz
        menor, x, y = encontrarMenor(matriz)
        matriz = matriz.drop([y], axis=1)
        matriz = matriz.drop([y], axis=0)
        matriz = matriz.rename(columns={x: "({},{})".format(x,y)})
        matriz = matriz.rename(index={x: "({},{})".format(x,y)})
        if enlace == 'simple':
            matriz = enlaceSimple(matriz, matriz_copia, x, y)
        if enlace == 'completo':
            matriz = enlaceCompleto(matriz, matriz_copia, x, y)
        if enlace == 'promedio':
            matriz = enlacePromedio(matriz, matriz_copia, x, y, copia)
        cluster.append([x, y, menor, nVariablesCluster(copia, x) + nVariablesCluster(copia, y)])
    return matriz, cluster, obtenerUltimoCluster(matriz)

def generarCorte(cluster):
    pass

def obtenerDendrograma():
    pass