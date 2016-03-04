#!/usr/bin/env python
# coding=utf-8

# ==============================================================================
# title           : parseMatlabMesh.py
# description     : This will load a .mat containing a Brainstorm mesh.
# author          : Guillaume Dumas
# date            : 2016-03-02
# version         : 0.1
# usage           : python parseMatlabMesh.py filename.mat
# notes           :
# python_version  : 2.7, 3.5
# ==============================================================================

from scipy.io import loadmat
from sys import argv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print("Load " + argv[1])
data = loadmat(file_name=argv[1])
print(data.keys())
key = 'ctx'  # Which key shall we select?
print(data[key].dtype.names)
var = 'Vertices'  # Which variable shall we select?
l = [i for i, k in enumerate(data[key].dtype.names) if k == var]
ver = data[key][0][0][l[0]]
print(ver)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(ver[:, 0], ver[:, 1], ver[:, 2], c='k', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
