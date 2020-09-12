# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:49:35 2020

@author: NICROMANO
"""

from Helpers import  encontrarMenor, nVariablesCluster
from Enlaces import enlacePromedio, enlaceCompleto, enlaceSimple

def agruparCluster(matriz, enlace, original = None):
    cluster = []
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
            matriz = enlacePromedio(matriz, matriz_copia, x, y, original)
        cluster.append([x, y, menor, nVariablesCluster(copia, x) + nVariablesCluster(copia, y)])
    return matriz, cluster

def obtenerDendrograma():
    pass