# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:10:45 2020

@author: NICROMANO
"""
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import numpy as np

X = np.array([[5,3],
    [10,15],
    [15,12],
    [24,10],
    [30,30],
    [85,70],
    [71,80],
    [60,78],
    [70,55],
    [80,91],])
print(X)
linked = linkage(X, 'single')
print(linkage)
labelList = range(1, 11)
plt.figure(figsize=(10, 7))
print(linked)
dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.show